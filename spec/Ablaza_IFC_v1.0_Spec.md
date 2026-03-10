# Alexander Santos Ablaza International Fixed Calendar — Version 1.0

# 0) Mission & Vision

**Mission.**  
Provide a human‑centered, scientifically accurate calendar that preserves every living tradition and every historical date, while eliminating structural friction in planning, analytics, and global coordination.

**Vision.**  
A globally usable, culturally respectful fixed calendar that **does not disrupt** Gregorian civil timekeeping, but **refactors** it into a simpler, equal‑month framework — enabling people, institutions, and systems to plan more fairly and think more clearly about time.

# 1) Goals of the Design

A‑IFC is engineered to meet these non‑negotiable goals:

1. **Compatibility & Continuity**  
   - Preserve all civil dates and records through a **day‑of‑year (DOY)–preserving conversion** with Gregorian.  
   - Keep **every day real** — no off‑week “blank” days, no week breaks.

2. **Religious & Cultural Respect**  
   - Maintain an uninterrupted **7‑day weekly cycle** for all observances.  
   - Avoid any constructs that would invalidate weekly traditions.

3. **Seasonal Accuracy**  
   - Match the Gregorian engineered average of **365.2425 days** to stay aligned with the tropical (seasonal) year over millennia.

4. **Structural Simplicity**  
   - **13 months × 28 days** base → each month = **exactly 4 weeks**.  
   - Predictable quarters and cleaner analytics for finance, ops, and education.

5. **Astronomical Clarity**  
   - **Day‑of‑Sol** explicitly marks the **June solstice** within **Sol**.  
   - A single **international anchor holiday** (ISD) provides a global focal point.

6. **Operational Feasibility**  
   - Printable and digital calendars remain **weekday‑accurate**.  
   - Converters and annual data packs (CSV/JSON) make adoption **drop‑in** for systems.
  
 
# 2) Year Structure (Canonical)

- **Base:** 13 months × 28 days = **364**.
- **Sol‑29:** occurs **every year** as a *normal, counted day* (no off‑week logic).
- **Dec‑29:** occurs **only in Gregorian leap years** as a *normal, counted day*, Gregorian leap years (4/100/400 rule) → average **365.2425** days.
- **Weeks:** always 7 days; **no 8‑day weeks**; no skipped weekdays.

**Average Year = 365.2425 days**  
13×28 (364) + **Sol‑29** annual (+1) + **Dec‑29** in 1/4 of years (−3/400 century rule) = **365.2425**.


# 3) Astronomical Anchors

**3.1 Day‑of‑Sol (June Solstice).**  
- **Common years:** **Sol‑4**  
- **Leap years:** **Sol‑5**  
This places the label inside the civil **June 20–22** solstice window (≈ Gregorian DOY 172/173; typically commonly June 21) and keeps long‑term seasonal stability through the 365.2425 engineered average.
- **Mid‑Year Day:** **Sol‑15** (calendar midpoint of 364‑day base).
- **The mid year day is the half year day count of the year in 365 at 183 or 184 day of year at month of Sol day 15.**

**3.2 International Sol Day (ISD).**  
- **Date:** **Sol‑12** every year  **A day in month of Sol shall be decided for international day, it can be from Sol-12 to Sol-15**
- **Type:** normal, counted weekday (no off‑week logic)  
- **Purpose:** globally recognized mid‑year anchor for culture, science, and unity  
- **Display:** mark with **🔆 “International Sol Day (Sol‑12)”**  
- **Policy:** jurisdictions MAY designate as a public holiday; organizations MAY adopt as a paid holiday or observance.
- Aligns with the calendar’s astronomical focus on Sol and the June solstice,
- Is predictable year‑to‑year, requires no off‑week days, and remains compatible with all national holiday systems and payroll/legal calendars.
- Avoids crowding near Sol‑1..5 is already use to mark Day of Sol from Gregorian Calendar June Solstice.
- Sits comfortably after the solstice label while leaving room before Sol‑29 (the annual real add).

# 4) Mid‑Year Day (Observance)

**Name:** Mid‑Year Day  
**Date:** **Sol‑15** (the midpoint of the 364‑day base: 6×28 = 168; 168 + 15 = DOY 183)  
**Type:** normal, counted weekday; **non‑statutory** by default  
**Purpose:** ceremonial midpoint of the **13×28** structure (calendar symmetry), distinct from the astronomical solstice which is earlier in Sol.  
**Note:** This observance is orthogonal to Day‑of‑Sol; it celebrates the calendar’s internal symmetry.
- International Holiday Anchor (June Sol)

**4.1 Purpose: **
- To establish a single, globally recognized observance in the Ablaza's/Alexan's IFC (A‑IFC) that:

You can formally brand this later (e.g., “Global Day of Sol / G‑Sol Day”). For now, the spec name is International Sol Day (ISD).

**4.2 Legal/operational classification**
- ISD is a non‑statutory international observance in the core A‑IFC spec.
- Jurisdictions (countries, states, provinces) MAY classify ISD as a public holiday or as a special observance.
- Organizations MAY treat ISD as paid holiday or company observance.

**4.3 HR/ERP guidance (no “mystery days”)**
- ISD is a normal, counted weekday (no off‑week blank).
- No special week logic is required; it behaves like any fixed date (e.g., Dec‑25 in Gregorian).
- When ISD falls on a weekend, observance rules are at the discretion of the jurisdiction or organization (e.g., “Mondayized” holiday).

**4.4 Interoperability & converters**
- Gregorian mapping: ISD’s A‑IFC date (e.g., Sol‑10) maps to a unique Gregorian date via the day‑of‑year–preserving converter you already published (e.g., in your CSV/JSON tables).
- Lunisolar calendars: treat like any other fixed civil date—publish the cross‑calendar mapping annually in your almanac pack.

**4.5 Display, Etymology & iconography**
- In printable and digital calendars, mark ISD with a 🔆 (or your chosen glyph) and the label “International Sol Day”.
- "Sol" in solstice is derived from the Latin word for "sun". It combines with sistere ("to stand still") to describe the astronomical phenomenon where the sun’s path appears to pause at its northernmost or southernmost limit before reversing direction. It signifies the "sun standing still".


# 5) Leap & Weekday Behavior (Summary)
- **Sol‑29** (annual) and **Dec‑29** (leap‑years) are **real weekdays**.  
- After **Sol‑29**, weekday alignment naturally shifts **+1** for the rest of the year.  
- In leap years, **Dec‑29** prints at year‑end; each new year’s Month‑1 Day‑1 re‑anchors to the **Gregorian Jan‑1 weekday** for printed calendars.  
- No off‑week days; no “blank” days; **7‑day week continuity** is preserved throughout.

 **5.1 Week policy**
- All days are normal weekdays (no off‑week days). Adding Sol‑29 / Dec‑29 naturally shifts later weekday starts; there are no 8‑day weeks.

# 6) Interoperability & Conversion (Recap)

**Principle:** A‑IFC preserves **Gregorian DOY** order. Every Gregorian date maps to exactly one A‑IFC date and vice‑versa.

- **Common year:**
  - DOY 1–168 → Months 1–6 (28 days each)
  - DOY 169–196 → **Sol‑1 … Sol‑28**
  - DOY 197 → **Sol‑29**
  - DOY ≥198 → map DOY−1 into Months 8–13 (28‑day grid)

- **Leap year:**
  - As above, and **DOY 366 → Dec‑29**

**Implications:**
- **No birthdays or holidays are lost.**  
  Example: **Jan 29/30/31 → A‑IFC Feb 1/2/3** deterministically.  
- **Fixed civil holidays** remain in the **same seasons**; labels convert via DOY.  
- **Lunisolar observances** continue via parallel calendars (as today), then publish A‑IFC dates annually.

**Conversions (lossless for civil dates)**

- Preserve Gregorian **day‑of‑year (DOY)** and map mechanically to A‑IFC (see converter tables/API).
- Fixed‑date birthdays & holidays map 1:1 in meaning; no one loses a date (e.g., Jan 29→Feb 1; Jan 30→Feb 2; Jan 31→Feb 3 in A‑IFC).

** Parallel calendars**

- **Julian↔Gregorian:** historical switch tables apply; then use DOY→A‑IFC.
- **Lunisolar (e.g., Chinese):** use official annual civil conversions to Gregorian, then DOY→A‑IFC.
- **Deep history:** provide ΔT (TT−UT) references for eclipse‑dated chronologies.
- **Holidays:** All public holidays per nation will be updated accordingly per each day set in the gregorian calendar mapping to the Alexan International Fixed Calendar accordingly so there zero lossless change.

# 7) Deliverables

- Annual **A‑IFC⇄Gregorian CSV/JSON**, printable 13‑month calendars (Sol‑29/Dec‑29 marked, Day of Sol highlighted), holiday demos, and a public API.

# 8) Public API (suggested)

- `/convert?gregorian=YYYY-MM-DD` → A‑IFC YYYY-M-D
- `/convert?aifc=YYYY-M-D` → Gregorian YYYY-MM-DD
- `/solstice?year=YYYY` → instant UTC + A‑IFC Sol‑n label
- `/julian-to-gregorian?date=YYYY-MM-DD&country=XX`
- `/lunisolar/chinese?gregorian=YYYY-MM-DD`

# 9) Legal & operational notes

- Statutory observances follow **jurisdictional policy**; the converter provides the authoritative A‑IFC date for each fixed civil holiday.
- Time‑scale issues (UTC/TAI/UT1, leap seconds) are orthogonal; systems can continue to timestamp in UTC.

© 2026–2030 Alexander Santos Ablaza. All rights reserved.
