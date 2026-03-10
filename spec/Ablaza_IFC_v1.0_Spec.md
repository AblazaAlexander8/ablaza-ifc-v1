# Alexander Santos Ablaza International Fixed Calendar — Version 1.0

**Design goals:** equal‑month usability, no drift vs. seasons, no lost birthdays/holidays, real days only, interoperable with historical and parallel calendars.

## Year structure

- 13 months × 28 days = **364** base days.
- **Sol‑29** every year (real day) → 365.
- **Dec‑29** in Gregorian leap years (4/100/400 rule) → average **365.2425** days.

## Astronomy anchors

- **Day of Sol (June solstice):** **Sol‑4** in common years / **Sol‑5** in leap years (≈ Gregorian DOY 172/173; typically June 21).
  **The day of Sol June solstice is usually June 21 in Gregorian calendar so it will fall in month of Sol day 4 in common days but in leap years it will fall in month of Sol day 5 we strictly follow gregorian Day-of-year at 172 day/173 day.**
- **Mid‑Year Day:** **Sol‑15** (calendar midpoint of 364‑day base).
  **The mid year day is the half year day count of the year in 365 at 183 or 184 day of year at month of Sol day 15.**
- **A day in month of Sol shall be decided for international day.

International Holiday Anchor (June Sol)
1) Purpose
To establish a single, globally recognized observance in the Ablaza IFC (A‑IFC) that:

Aligns with the calendar’s astronomical focus on Sol and the June solstice,
Is predictable year‑to‑year, requires no off‑week days, and
Remains compatible with all national holiday systems and payroll/legal calendars.

2) Name
International Sol Day (ISD)

You can formally brand this later (e.g., “Global Day of Sol / G‑Sol Day”). For now, the spec name is International Sol Day (ISD).

3) Placement (choose one policy and publish it)
You have two good, standards‑friendly options. Pick A (fixed) for maximum simplicity, or B (astro‑anchored) if you want the label to track the solstice window more tightly.
A) Fixed‑date policy (simplest, recommended)

ISD = Sol‑12 every year.
Rationale:

Keeps the day stable for operations and international coordination.
Avoids crowding near Sol‑1..5 (which you already use to mark Day of Sol).
Sits comfortably after the solstice label while leaving room before Sol‑29 (the annual real add).

B) Astronomical‑window policy (tighter to the solstice)

Common years: ISD = Sol‑5
Leap years: ISD = Sol‑6
Rationale:
Tracks the Gregorian DOY 172/173 solstice window (≈ June 21) via your Day of Sol = Sol‑4 (common)/Sol‑5 (leap) convention, then places ISD immediately after it for a 1‑day “festival arc.”
Requires a small annual table in the almanac if you ever choose to drift by ±1 based on the exact UTC instant; otherwise keep it at 5/6 as above for stability.

Recommendation: Start with A) Sol‑10 for v1.0. You can always introduce a v1.1 “astro window” variant later with a published almanac table.

4) Legal/operational classification

ISD is a non‑statutory international observance in the core A‑IFC spec.
Jurisdictions (countries, states, provinces) MAY classify ISD as a public holiday or as a special observance.
Organizations MAY treat ISD as paid holiday or company observance.

5) HR/ERP guidance (no “mystery days”)
ISD is a normal, counted weekday (no off‑week blank).
No special week logic is required; it behaves like any fixed date (e.g., Dec‑25 in Gregorian).
When ISD falls on a weekend, observance rules are at the discretion of the jurisdiction or organization (e.g., “Mondayized” holiday).

6) Interoperability & converters
Gregorian mapping: ISD’s A‑IFC date (e.g., Sol‑10) maps to a unique Gregorian date via the day‑of‑year–preserving converter you already published (e.g., in your CSV/JSON tables).
Lunisolar calendars: treat like any other fixed civil date—publish the cross‑calendar mapping annually in your almanac pack.

7) Display & iconography

In printable and digital calendars, mark ISD with a 🔆 (or your chosen glyph) and the label “International Sol Day”.
"Sol" in solstice is derived from the Latin word for "sun". It combines with sistere ("to stand still") to describe the astronomical phenomenon where the sun’s path appears to pause at its northernmost or southernmost limit before reversing direction. It signifies the "sun standing still".

## Week policy

- All days are normal weekdays (no off‑week days). Adding Sol‑29 / Dec‑29 naturally shifts later weekday starts; there are no 8‑day weeks.

## Conversions (lossless for civil dates)

- Preserve Gregorian **day‑of‑year (DOY)** and map mechanically to A‑IFC (see converter tables/API).
- Fixed‑date birthdays & holidays map 1:1 in meaning; no one loses a date (e.g., Jan 29→Feb 1; Jan 30→Feb 2; Jan 31→Feb 3 in A‑IFC).

## Parallel calendars

- **Julian↔Gregorian:** historical switch tables apply; then use DOY→A‑IFC.
- **Lunisolar (e.g., Chinese):** use official annual civil conversions to Gregorian, then DOY→A‑IFC.
- **Deep history:** provide ΔT (TT−UT) references for eclipse‑dated chronologies.
- **Holidays:** All public holidays per nation will be updated accordingly per each day set in the gregorian calendar mapping to the Alexan International Fixed Calendar accordingly so there zero lossless change.

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

© 2026–2030 Alexander Santos Ablaza. All rights reserved.
