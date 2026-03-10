# Alexander Santos Ablaza International Fixed Calendar — Version 1.0

**A‑IFC v1.0** is an equal‑month calendar (13×28 base) that corrects the weaknesses of the old International Fixed Calendar while maintaining full compatibility with the Gregorian system.

---

## Alexan International Fixed Calendar (A‑IFC)
A scientifically grounded, culture‑respecting refinement of the earlier International Fixed Calendar — preserving all **7‑day week traditions**, eliminating **mystery days**, and ensuring **complete historical continuity**.

### Why the Original International Fixed Calendar Failed
The original IFC proposed by Moses Cotsworth was rejected by the League of Nations because it introduced **“blank days”** or **non‑weekly days**, breaking the continuous 7‑day religious cycle upheld by major world traditions.

### What We Learned From the Kodak Implementation
Despite being rejected globally, the IFC was successfully used internally by **Kodak for 61 years**, proving the *usability* and *practical efficiency* of a 13‑month equal‑month system.  
However, the presence of “mystery days” meant it could not be adopted universally.

### How A‑IFC Fixes the Missing Link
The **Alexan International Fixed Calendar** resolves these issues by:

- removing all non‑weekly “blank” days,  
- keeping every day a real weekday,  
- preserving all religious and cultural weekly cycles,  
- maintaining scientific accuracy with the Gregorian astronomical year (**365.2425 days**),  
- and retaining perfect alignment with historical dates.

A‑IFC is therefore a **corrected, globally compatible evolution** of the original IFC.

**A-IFC system is built to fix what's actually broken**

What A‑IFC fixes:
- ✔ Month lengths
- ✔ Week alignment
- ✔ Equalized structure
- ✔ Leap-day handling
- ✔ Multi-calendar compatibility

What A‑IFC deliberately does NOT change:
 - ❌ Year numbering
 - ❌ Epoch origin
 - ❌ International legal timebase

--- 
### This is exactly why A‑IFC is practical, adoptable, and compatible. Historians emphasize that the exact birth year of Jesus is not known, and likely several years earlier than AD. To explain that, currently we are 2026 as of this writing so we are using this for internationalization purpose not correcting history. And "2026" is not currently accurate for the historical precision of birth of Jesus Christ but we use it anyway in the Gregorian Calendar.

####  Because the AD/BC system was created using a mistaken estimate of Jesus’ birth year, but the world adopted it anyway.
#### The "AD" system didn't even become standard until centuries later
#### It comes from a calculation error made in the 6th century by a monk named Dionysius Exiguus. He tried to calculate the year of Jesus’ birth and declared that Jesus was born in year 1 AD.
#### But modern historians know today that this is not correct.

---
**Example**

Gregorian: March 9, 2026
A‑IFC: Month 3, Day 12, Year 2026

The year stays the same.
This is how A‑IFC stays drop‑in ready for:

- Business operations
- Government systems
- Financial systems
- Academic timelines
- International coordination
---

## ⭐ Overview

The **Ablaza International Fixed Calendar (A‑IFC)** is a mathematically consistent 13‑month system designed to:

- Maintain **full compatibility** with existing Gregorian dates  
- Provide a **regular, equal‑month structure** for planning and analytics  
- Fix long‑standing Gregorian irregularities  
- Preserve **all real days** (no phantom/off‑week days)  
- Stay aligned with Earth’s seasons via **Day‑of‑Sol** (June solstice)  
- Support global coordination through **International Sol Day (Sol‑12)**  
- We also support other calendar coordination like the Lunar system, and other calendar system.
This calendar does **not replace** the Gregorian system.  
It **refactors and improves** its inconsistencies while staying fully interoperable.

---

## 🌍 A Modern Refinement of the Gregorian Calendar

> *Unlike the original IFC (which had 2 mystery days), A‑IFC keeps all traditions intact and removes all non‑weekly void days.*

A‑IFC ensures:

- **Every day is a real weekday** (no “blank” days)  
- **Sol‑29** is added every year as a real day  
- **Dec‑29** appears only in Gregorian leap years  
- The engineered Gregorian average length (**365.2425**) is maintained  
- **Birthdays and fixed holidays** convert cleanly through day‑of‑year mapping  
  - Example: Jan 29 → A‑IFC Feb 1  
- **Day‑of‑Sol** aligns with the actual June solstice  
  - Sol‑4 (common years)  
  - Sol‑5 (leap years)

---

## 📅 A‑IFC Month Index (Gregorian-Compatible Names)

| Month Number | A‑IFC Name | Notes |
|--------------|------------|--------|
| Month 1 | January | |
| Month 2 | February | |
| Month 3 | March | |
| Month 4 | April | |
| Month 5 | May | |
| Month 6 | June | |
| **Month 7** | **Sol** | **Mid‑year solstice month** |
| Month 8 | July | |
| Month 9 | August | |
| Month 10 | September | |
| Month 11 | October | |
| Month 12 | November | |
| Month 13 | December | |

---

## 🚀 Get Started

- See **`SPEC/Ablaza_IFC_v1.0_Spec.md`** for the formal rules.  
- Converters are in **`data/converters/{year}`** (CSV & JSON).  
- Printable 13‑month calendars are in **`/calendars`**.

---

## 🛠 Regenerate Calendar & Converters

### Base: converters + calendars for 2026–2030

```bash
python3 scripts/generate_aifc_pack.py 2026 2030
```

### Default (2026–2030)

```bash
python3 scripts/generate_aifc_pack.py
```

### With holidays & spec

```bash
python3 scripts/generate_aifc_pack.py 2026 2030 --with-holidays --with-spec
```

---
