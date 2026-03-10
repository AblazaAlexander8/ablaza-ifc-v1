#!/usr/bin/env python3
# Alexander Santos Ablaza International Fixed Calendar — v1.0
# Feasibility pack generator (converters + printable calendars + optional holiday demo & spec)

from datetime import date, timedelta
import csv, json, os, sys
from typing import List, Tuple

# ---------------------------
# CLI ARGS
#   Usage: python3 scripts/generate_aifc_pack.py [START_YEAR] [END_YEAR] [--with-holidays] [--with-spec]
# ---------------------------
START_YEAR = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 2026
END_YEAR   = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 2030
WITH_HOLIDAYS = '--with-holidays' in sys.argv
WITH_SPEC     = '--with-spec' in sys.argv

# ---------------------------
# CORE CALENDAR LOGIC (A‑IFC v1.0)
# ---------------------------

def is_leap(y: int) -> bool:
    """Gregorian leap rule 4/100/400."""
    return (y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0))

def doy(y: int, m: int, d: int) -> int:
    """Gregorian day-of-year."""
    return (date(y, m, d) - date(y, 1, 1)).days + 1

def g2a(y: int, m: int, d: int):
    """Gregorian (y,m,d) -> A‑IFC mapping (month, day, label, DOY, isLeap, isDayOfSol)."""
    D = doy(y, m, d)
    leap = is_leap(y)
    # A‑IFC sections by DOY (remember Sol‑29 exists at DOY 197 every year; Dec‑29 only in leap years)
    if D <= 168:  # Months 1..6 (6×28)
        month = (D - 1) // 28 + 1
        day   = (D - 1) % 28 + 1
        label = ""
    elif 169 <= D <= 196:  # Sol 1..28
        month = 7
        day   = D - 168
        label = ""
    elif D == 197:         # Sol‑29 (annual real day)
        month = 7; day = 29; label = "Sol-29"
    else:
        # After Sol‑29, shift 1 to place into 28‑day grid
        Dp = D - 1
        month = (Dp - 1) // 28 + 1
        day   = (Dp - 1) % 28 + 1
        label = ""
        if leap and D == 366:  # Dec‑29 only in leap years
            month = 13; day = 29; label = "Dec-29"
    day_of_sol = (month == 7 and ((not leap and day == 4) or (leap and day == 5)))
    return month, day, label, D, leap, day_of_sol

def a2g(y: int, month: int, day: int):
    """A‑IFC (y,month,day) -> (Gregorian date, Gregorian DOY)."""
    leap = is_leap(y)
    if month < 7:
        Da = (month - 1) * 28 + day
    elif month == 7:
        Da = 168 + day if day <= 28 else 197
    else:
        base = 197 + (month - 8) * 28
        Da = base + day
        if leap and month == 13 and day == 29:
            Da = 366
    gg = date(y, 1, 1) + timedelta(days=Da - 1)
    return gg, Da

# ---------------------------
# I/O FOLDERS
# ---------------------------

os.makedirs("data/converters", exist_ok=True)
os.makedirs("calendars", exist_ok=True)
os.makedirs("SPEC", exist_ok=True)
os.makedirs("data/holidays", exist_ok=True)

# ---------------------------
# CONVERTERS (both directions)
# ---------------------------

for y in range(START_YEAR, END_YEAR + 1):
    os.makedirs(f"data/converters/{y}", exist_ok=True)

    # Gregorian -> A‑IFC
    rows = []
    last = 366 if is_leap(y) else 365
    for D in range(1, last + 1):
        g = date(y, 1, 1) + timedelta(days=D - 1)
        m, d, label, DD, lp, star = g2a(y, g.month, g.day)
        rows.append({
            "GregorianDate": g.isoformat(),
            "GregorianDOY": D,
            "AIFCYear": y, "AIFCMonth": m, "AIFCDay": d,
            "AIFCLabel": label, "DayOfSol": star
        })
    with open(f"data/converters/{y}/aifc_from_gregorian_{y}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    with open(f"data/converters/{y}/aifc_from_gregorian_{y}.json", "w") as f:
        json.dump(rows, f, indent=2)

    # A‑IFC -> Gregorian
    inv = []
    for m in range(1, 14):
        days = 29 if (m == 7 or (m == 13 and is_leap(y))) else 28
        for d in range(1, days + 1):
            gg, DD = a2g(y, m, d)
            inv.append({
                "AIFCYear": y, "AIFCMonth": m, "AIFCDay": d,
                "GregorianDate": gg.isoformat(), "GregorianDOY": DD
            })
    with open(f"data/converters/{y}/gregorian_from_aifc_{y}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=inv[0].keys())
        w.writeheader(); w.writerows(inv)
    with open(f"data/converters/{y}/gregorian_from_aifc_{y}.json", "w") as f:
        json.dump(inv, f, indent=2)

# ---------------------------
# PRINTABLE CALENDARS (weekday‑accurate)
# ---------------------------

def pad_grid(start_weekday_idx: int, days_in_month: int) -> Tuple[List[str], int]:
    """Render a month grid with correct weekday alignment (Sun‑first header)."""
    header = "Sun Mon Tue Wed Thu Fri Sat"
    lines = [header]
    sun_first_idx = (start_weekday_idx + 1) % 7  # 0=Sun ... 6=Sat

    row = ["   "] * sun_first_idx
    day = 1
    while len(row) < 7 and day <= days_in_month:
        row.append(f"{day:>3}"); day += 1
    row += ["   "] * (7 - len(row))
    lines.append(" ".join(row))

    while day <= days_in_month:
        row = []
        for _ in range(7):
            row.append(f"{day:>3}" if day <= days_in_month else "   ")
            day += 1
        lines.append(" ".join(row))

    next_idx = (start_weekday_idx + days_in_month) % 7
    return lines, next_idx

def inject_star(lines: List[str], star_day: int) -> List[str]:
    out = []
    found = False
    for i, L in enumerate(lines):
        if i == 0: out.append(L); continue
        parts = L.split()
        new_parts = []
        for p in parts:
            try:
                val = int(p)
            except ValueError:
                new_parts.append(p); continue
            if val == star_day and not found:
                new_parts.append(f"{val:>2}★"); found = True
            else:
                new_parts.append(f"{val:>3}")
        out.append(" ".join(new_parts))
    return out

def render_year(y: int) -> None:
    leap = is_leap(y)
    jan1 = date(y, 1, 1)
    start_wd = jan1.weekday()  # Mon=0 ... Sun=6; anchor Month 1 Day 1 to same weekday

    md_lines: List[str] = []
    md_lines.append(f"# A‑IFC {y}\n")
    md_lines.append("**Legend:** ★ = Day of Sol; ✚ = Extra real day (Sol‑29 / Dec‑29)\n")

    # Months 1..6
    for m in range(1, 7):
        lines, start_wd = pad_grid(start_wd, 28)
        md_lines.append(f"\n## Month {m}\n")
        md_lines.append("```text\n" + "\n".join(lines) + "\n```")

    # Month 7 — SOL
    md_lines.append("\n## Month 7 — SOL\n")
    star_day = 5 if leap else 4
    lines, start_wd = pad_grid(start_wd, 28)
    lines = inject_star(lines, star_day)
    md_lines.append("```text\n" + "\n".join(lines) + "\n```")

    # Sol‑29
    md_lines.append("```text\n[29✚]\n```")
    start_wd = (start_wd + 1) % 7

    # Months 8..12
    for m in range(8, 13):
        lines, start_wd = pad_grid(start_wd, 28)
        md_lines.append(f"\n## Month {m}\n")
        md_lines.append("```text\n" + "\n".join(lines) + "\n```")

    # Month 13
    lines, start_wd = pad_grid(start_wd, 28)
    md_lines.append(f"\n## Month 13\n")
    md_lines.append("```text\n" + "\n".join(lines) + "\n```")

    if leap:
        md_lines.append("\n### Extra day in leap year\n")
        md_lines.append("```text\n[29✚]  (Dec‑29)\n```")
        start_wd = (start_wd + 1) % 7

    with open(f"calendars/aifc_calendar_{y}.md", "w") as f:
        f.write("\n".join(md_lines))

for y in range(START_YEAR, END_YEAR + 1):
    render_year(y)

# Optional: holiday demo
if WITH_HOLIDAYS:
    PH_FIXED = [
        (1, 1,  "PH New Year's Day"),
        (4, 9,  "PH Araw ng Kagitingan"),
        (6, 12, "PH Independence Day"),
        (11, 30, "PH Bonifacio Day"),
        (12, 25, "PH Christmas Day"),
        (12, 30, "PH Rizal Day"),
    ]
    US_FIXED = [
        (1, 1,  "US New Year's Day"),
        (7, 4,  "US Independence Day"),
        (11, 11, "US Veterans Day"),
        (12, 25, "US Christmas Day"),
    ]
    with open("data/holidays/holiday_demo_PH_US_2026_2030.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Country", "Holiday", "GregorianDate", "AIFCDate"]) 
        for y in range(START_YEAR, END_YEAR + 1):
            for (m, d, name) in PH_FIXED:
                g = date(y, m, d)
                am, ad, _, _, _, _ = g2a(y, m, d)
                w.writerow(["PH", name, g.isoformat(), f"{y}-{am}-{ad}"])
            for (m, d, name) in US_FIXED:
                g = date(y, m, d)
                am, ad, _, _, _, _ = g2a(y, m, d)
                w.writerow(["US", name, g.isoformat(), f"{y}-{am}-{ad}"])

# Optional: spec one‑pager
if WITH_SPEC:
    SPEC_MD = f"""
# Alexander Santos Ablaza International Fixed Calendar — Version 1.0

**Design goals:** equal‑month usability, no drift vs. seasons, no lost birthdays/holidays, real days only, interoperable with historical and parallel calendars.

## Year structure
- 13 months × 28 days = **364** base days.
- **Sol‑29** every year (real day) → 365.
- **Dec‑29** in Gregorian leap years (4/100/400 rule) → average **365.2425** days.

## Astronomy anchors
- **Day of Sol (June solstice):** **Sol‑4** in common years / **Sol‑5** in leap years (≈ Gregorian DOY 172/173; typically June 21).
- **Mid‑Year Day:** **Sol‑15** (calendar midpoint of 364‑day base).

## Week policy
- All days are normal weekdays (no off‑week days). Adding Sol‑29 / Dec‑29 naturally shifts later weekday starts; there are no 8‑day weeks.

## Conversions (lossless for civil dates)
- Preserve Gregorian **day‑of‑year (DOY)** and map mechanically to A‑IFC (see converter tables/API).
- Fixed‑date birthdays & holidays map 1:1 in meaning; no one loses a date (e.g., Jan 29→Feb 1; Jan 30→Feb 2; Jan 31→Feb 3 in A‑IFC).

## Parallel calendars
- **Julian↔Gregorian:** historical switch tables apply; then use DOY→A‑IFC.
- **Lunisolar (e.g., Chinese):** use official annual civil conversions to Gregorian, then DOY→A‑IFC.
- **Deep history:** provide ΔT (TT−UT) references for eclipse‑dated chronologies.

## Deliverables
- Annual **A‑IFC⇄Gregorian CSV/JSON**, printable 13‑month calendars (Sol‑29/Dec‑29 marked, Day of Sol highlighted), holiday demos, and a public API.

## Public API (suggested)
- `/convert?gregorian=YYYY-MM-DD` → A‑IFC YYYY-M-D
- `/convert?aifc=YYYY-M-D` → Gregorian YYYY-MM-DD
- `/solstice?year=YYYY` → instant UTC + A‑IFC Sol‑n label
- `/julian-to-gregorian?date=YYYY-MM-DD&country=XX`
- `/lunisolar/chinese?gregorian=YYYY-MM-DD`

## Legal & operational notes
- Statutory observances follow **jurisdictional policy**; the converter provides the authoritative A‑IFC date for each fixed civil holiday.
- Time‑scale issues (UTC/TAI/UT1, leap seconds) are orthogonal; systems can continue to timestamp in UTC.

© {START_YEAR}–{END_YEAR} Alexander Santos Ablaza. All rights reserved.
"""
    with open("SPEC/Ablaza_IFC_v1.0_Spec.md", "w") as f:
        f.write(SPEC_MD)

print("A‑IFC pack generated (converters + calendars)" + (" + holidays" if WITH_HOLIDAYS else "") + (" + spec" if WITH_SPEC else ""))