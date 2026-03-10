# Alexander Santos Ablaza International Fixed Calendar — Version 1.0

**Design goals:** equal‑month usability, no drift vs. seasons, no lost birthdays/holidays, real days only, interoperable with historical and parallel calendars.

## Year structure

- 13 months × 28 days = **364** base days.
- **Sol‑29** every year (real day) → 365.
- **Dec‑29** in Gregorian leap years (4/100/400 rule) → average **365.2425** days.

## Astronomy anchors

- **Day of Sol (June solstice):** **Sol‑4** in common years / **Sol‑5** in leap years (≈ Gregorian DOY 172/173; typically June 21).
  **The day of Sol June solstice is usually June 21 so it will fall in month of Sol day 4 in common days but in leap years it will fall in month of Sol day 5 we strictly follow gregorian Day-of-year at 172 day/173 day.**
- **Mid‑Year Day:** **Sol‑15** (calendar midpoint of 364‑day base).
  **The mid year day is the half year day count of the year in 365 at 183 or 184 day of year at month of Sol day 15.**
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

© 2026–2030 Alexander Santos Ablaza. All rights reserved.
