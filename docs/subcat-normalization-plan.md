# Subcat Normalization Plan

Inconsistencies noticed in the catalog's `subcat` field after several waves of additions. **This is a proposal, not yet executed.** Reviewed against the catalog as of 2026-04-25.

## A. Asetek SimSports — three variants of the same idea

Currently three different subcat strings refer to the same brand:

| subcat | count | issue |
|---|---|---|
| `Asetek SimSports (via QR Adapter)` | 4 | preferred form |
| `Asetek SimSports (via adapter)` | 2 | lowercase "adapter" — drift from the canonical version |
| `Asetek via Adapter` | 1 | missing the "SimSports" brand suffix |

**Proposal:** unify all three to `Asetek SimSports (via QR Adapter)`. One `sed`-style pass via the Python regex pattern. Zero entry-data risk; only a label change.

```python
# pseudocode
for line in html:
    line = line.replace('subcat:"Asetek SimSports (via adapter)"', 'subcat:"Asetek SimSports (via QR Adapter)"')
    line = line.replace('subcat:"Asetek via Adapter"', 'subcat:"Asetek SimSports (via QR Adapter)"')
```

After: one Asetek subcat with 7 entries.

## B. Shape-based subcats from the Apr 2026 expansion

When the rim-research expansion landed, some new entries used **shape-based** subcats instead of brand-based ones:

| subcat | count | example IDs |
|---|---|---|
| `Formula` | 14 | id:262 (Ascher YOUR Ultimate), id:269 (MOZA), id:272/273 (Soelpec), id:277/278 (Delta Sim Tech) |
| `GT` | 9 | id:270 (MOZA Mission R variant), id:275 (Rexing), others |
| `GT modular` | 1 | id:267 (Cube Controls Reparto Corse Suede) |
| `Formula/GT licensed` | 1 | id:269 (MOZA Mission R licensed) |
| `Formula licensed` | 1 | id:280 (Trak Racer BWT Alpine F1 A525) |

These scatter wheels by shape across multiple brands. The rest of the catalog uses **brand-based** subcats (`Cube Controls`, `MOZA (via Universal Hub Kit)`, `BavarianSimTec`, etc.). Mixing the two styles makes browsing-by-brand confusing.

**Proposal:** reassign each shape-bucket entry to its proper brand subcat:

| current subcat | id | brand | proposed subcat |
|---|---|---|---|
| `Formula` | 262 | Ascher Racing | `Ascher Racing` |
| `Formula` | 263 | (TBD) | check brand |
| `Formula` | 264 | P1Sim | `P1Sim (French)` |
| `Formula` | 269 | MOZA | `MOZA (via Universal Hub Kit)` |
| `Formula` | 271 | MOZA | `MOZA (via Universal Hub Kit)` |
| `Formula` | 272 | Soelpec | `Soelpec (Netherlands)` |
| `Formula` | 273 | Soelpec | `Soelpec (Netherlands)` |
| `Formula` | 277 | Delta Sim Tech | `Delta Sim Tech` |
| `Formula` | 278 | Delta Sim Tech | `Delta Sim Tech` |
| `Formula` | 279 | PSE | `Precision Sim Engineering` |
| `Formula licensed` | 280 | Trak Racer | new `Trak Racer` (or move under `Formula licensed` if other licensed entries appear) |
| `GT` | 270 | MOZA | `MOZA (via Universal Hub Kit)` |
| `GT` | 275 | Rexing | `Rexing (EU)` |
| `GT` | (others) | various | each → its brand subcat |
| `GT modular` | 267 | Cube Controls | `Cube Controls` |
| `Formula/GT licensed` | 269 | MOZA | `MOZA (via Universal Hub Kit)` |

**Why brand-based wins:** users browsing the catalog typically know the brand they want. Shape is already encoded in the `shape` field (visible on every card). No reason to also use it as a primary group.

**Edge case — orphan brands:** if a brand has only 1 entry (e.g. Cosworth UK, VRS, Hybrid Racing Simulations), it gets a single-entry subcat. That's fine — every brand-button shows its own count, so a "1" is acceptable. Better than scattering them in generic shape buckets.

## C. Future: Standalone Rims tab — size-based subcats

User flagged 2026-04-25 (deferred): replace the brand/shape-based subcats on the **Standalone Rims tab** with **rim-size buttons** (matching the dimensions: 280, 290, 300, 310, 320, 330, 340, 350, 380mm+). The dedicated size-filter row above the cards becomes redundant if subcats do the same job — likely also remove it. Saved as a future task in workflow memory; do not execute until the user revisits.

## D. Execution order (recommended)

1. **A first** — three-way Asetek unification. Zero risk. ~30 seconds.
2. **B second** — shape-bucket → brand reassignment. Verify each entry's brand before reassigning (some shape-bucket entries may have unexpected brand strings). ~10 minutes.
3. **C later** — Standalone Rims size-subcat refactor. Larger UX change; do separately.

## E. Validation after any normalization pass

- `./validate.sh` must pass (parse + schema)
- `grep -c 'subcat:"Asetek SimSports (via adapter)"' index.html` → 0 after Phase A
- `grep -c 'subcat:"Formula"' index.html` → 0 after Phase B (assuming no genuine "Formula" subcat is wanted)
- Spot-check the brand row under Sim Specific tab visually — counts should match before/after total

## F. What this plan does NOT do

- Does not propose merging `Simagic (via MAGLINK)` and `Simagic NEO X (via MAGLINK)` — those are intentionally distinct (NEO X is the modular HUB platform, not the original line)
- Does not touch any data fields other than `subcat`
- Does not modify `brand`, `model`, or any product-fact field
