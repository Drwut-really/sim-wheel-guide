# Wheel Update — 2026-08-09

Review window: products released or announced since the previous review date (July 10, 2026).

## Method
Web research sweep (14 targeted queries, tightened from a broader 29-query draft after
review) plus a dedup pass against all 270 existing catalog entries. Scope per
`wheel_research_prompt.md`: brand sites / review sites / authorized retailers only;
AliExpress/eBay/Etsy excluded (no Simjack/Simmson this cycle). Preorders admitted on
**hard dates only**.

## New entries added
None. No genuinely new sim racing wheel/rim products released or announced after
2026-07-10 met the bar for inclusion — a valid outcome for a 30-day window.

## Reviewed, nothing to add
- **Thrustmaster Ferrari 499P Centenary Winner Edition** — released June 13, 2026, before
  the review window, and Thrustmaster's bundled-base products don't fit this catalog's
  QR/electronics-wheel or bare-rim schema (no existing Thrustmaster precedent).
- **Acelith RD33** (rally/drift/NASCAR, €79.90) — existing product, not newly announced.
- **Zen's Simwheels ZS-LMP2-X** — appears to be an existing/prior-reviewed product, not
  clearly new since 2026-07-10.
- **MOZA R16 Ultra, R5 Pro; Sim-Lab DDS26/DDS39** — wheelbases, not wheels/rims → out of
  catalog scope.
- **Fanatec × Nissan** (July 7, 2026) — licensing/partnership announcement only, no
  product or specs revealed yet; Fanatec is also out of catalog scope.
- Expo/trade-show sweep: only Gamescom (Aug 26–30) and SimRacing Expo Frankfurt (October)
  found, both after today with no wheel-specific announcements yet.

## Price corrections applied (5)
All verified directly on simracingbay.com during this sweep — SimRacingBay has
restructured pricing across its lineup since the catalog was last checked against that
brand:

| id | Model | Old price | New price | Class |
|----|-------|-----------|-----------|-------|
| 24 | SRB GT3 V2 | €620–€680 | €590–€712 | minor |
| 25 | SRB GT3 V2 SWW2 | €680–€750 | €790–€859 | minor (~+€110) |
| 27 | SRB OMPX GT | €680–€720 | €531–€593 | **major (−€127 to −€149, ~$137–$161)** |
| 28 | SRB BB Ultra V2 | €800–€900 | €399–€468 | **major (−€401 to −€432, ~$430–$465)** |
| 26 | SRB GT3 V2 Special USB | €590–€659 | unchanged | — |

## Data-integrity fix: id 29
The `buy` URL for id 29 ("SRB Ultra Competition Wheel," €750–€850, 20 inputs, orange/
Simucube-wireless) now resolves to a different SimRacingBay product: a bare rim with 0
electronics, dish 0, €99 (€89 carbon). SimRacingBay appears to have discontinued the
combined product and split it into two SKUs — a bare rim (this one) plus the SRB BB
Ultra V2 button box (id 28). Per explicit user direction this cycle, the entry was
rewritten (not just re-priced) to describe the current product: renamed to
"SRB Competition Wheel V2", `conn` changed orange → gray, `inputs` 20 → 0, `dia` unchanged
at 300mm, price €750–€850 → €99 (€89 carbon), and pros/cons/notes rewritten to match,
with the prior spec preserved in the notes field for audit continuity. Confirmed via
WebFetch against https://www.simracingbay.com/product/competition-wheel-v2/.

## Preorder shipping-status notes (informational only — no fields touched beyond id 29 above)
- **Simagic Zeus Formula / GT / Sport** (ids 318–320) — product pages now show plain
  "Add to cart" with no preorder banner; appears to have moved past hard-preorder status
  (original `releaseDate` was 2026-06-10). Prices unchanged.
- **Zen's Simwheels LMZ Evo** (id 297) — still active preorder; delivery has slipped to
  "expected mid-September" per the product page (catalog notes 2026-Q2). Price unchanged.
- **Cube Controls Phoenix** (id 327) — still preorder, not shipped. Cube Controls is on
  summer closure Aug 8–23; shipping resumes Aug 24 with an expected backlog. Price
  unchanged.
- **Sim-Lab GTSL Pro** (id 326) — third-party press reported shipping began "first week
  of August 2026," but Sim-Lab's own product page still shows active "Pre-orders open" at
  the $599 sale price with no explicit ship date. Price unchanged.

## Result
270 entries, unchanged this cycle (no adds/removals). Sections: sim 165, oval 99,
preorder 6. 5 price corrections applied (2 flagged ≥$150) plus 1 data-integrity rewrite
(id 29). Review date bumped to August 9, 2026. `validate.sh` passed.
