# Alexander Santos Ablaza International Fixed Calendar — Version 1.0

**A‑IFC v1.0** is an equal‑month calendar (13×28 base) that:

- keeps **every day real** (no off‑week “blank days”),
- adds **Sol‑29** each year and **Dec‑29** in Gregorian leap years,
- matches the Gregorian engineered average **365.2425 days** to stay aligned with the **tropical year** (seasons),
- preserves **birthdays & fixed holidays** via **day‑of‑year (DOY)** mapping (e.g., Jan 29 → Feb 1 in A‑IFC),
- aligns **Day of Sol** with the **June solstice** (Sol‑4 in common, Sol‑5 in leap).

## Get started

- See `SPEC/Ablaza_IFC_v1.0_Spec.md` for the formal rules.
- Converters live in `data/converters/{year}` (CSV & JSON both directions).
- Printable calendars (13 months) live in `/calendars`.

## Regenerate

```bash
python3 scripts/generate_aifc_pack.py 2026 2030
```

# Base: converters + calendars for 2026–2030

```bash
python3 scripts/generate_aifc_pack.py
```

# With holidays & spec

```bash
python3 scripts/generate_aifc_pack.py 2026 2030 --with-holidays --with-spec
```
