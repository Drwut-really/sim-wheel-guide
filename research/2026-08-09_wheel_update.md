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

## Result (first pass)
270 entries, unchanged this pass (no adds/removals). Sections: sim 165, oval 99,
preorder 6. 5 price corrections applied (2 flagged ≥$150) plus 1 data-integrity rewrite
(id 29). Review date bumped to August 9, 2026. `validate.sh` passed.

---

## Follow-up sweep (same day) — preorder shipping-status resolution + broader discovery

### Preorder shipping-status resolution
Checked all 6 preorder entries directly against brand sites for actual ship/in-stock
status rather than trusting stale `releaseDate` values:

- **id 318/319/320 — Simagic Zeus Formula/GT/Sport** — confirmed shipped. Brand pages show
  plain "Add to cart" with no preorder language; corroborated by a published TweakTown
  unboxing review and a Zeus Sport unboxing video. Moved `section:"preorder"` →
  `"sim"`, removed `releaseDate`, dropped the stale "Pre-order — shipping begins..." con
  line from all three. No price change (all three matched current listings exactly).
- **id 327 — Cube Controls Phoenix** — confirmed shipped/in stock. Product page dropped
  preorder language entirely (now "shipping available in 15 working days," a normal
  lead time, not a preorder disclaimer); corroborated by two authorized retailers, one
  showing a "Now In Stock" banner. Moved `section:"preorder"` → `"sim"`, removed
  `releaseDate`, dropped the stale preorder con line, added a note on the Aug 8–23 team
  closure. No price change.
- **id 297 — Zen's Simwheels LMZ Evo** — still genuinely preorder per the brand's own
  page ("Pre-Order" button, "Expected delivery starting at Mid-September"). Kept
  `section:"preorder"`; refreshed `releaseDate` from the stale `"2026-Q2"` to `"2026-09"`
  to match the brand's current estimate.
- **id 326 — Sim-Lab GTSL Pro** — still genuinely preorder; the ship window slipped
  further. Sim-Lab's own EU store now states "Preorders are now open. Shipping starts in
  the 4th week of August" (superseding the earlier third-party "first week of August"
  press reports); the US store shows sold out, not in-stock. Kept
  `section:"preorder"`; refreshed `releaseDate` to `"2026-08-24"` and updated the con
  line/notes to reflect the slip.
- Cleared stale `isNew:true` from ids 326 and 327 (added in the 2026-07-10 cycle, not
  this one) so the 🆕 tab reflects only genuinely new-this-run entries.

### Broader discovery sweep (not time-boxed to "new since July")
Widened the net beyond a recency filter: boutique/indie brand lists, German/French/
Italian/Spanish regional searches for small regional makers, and oval-rim-specific
searches targeting the catalog's thinnest subcats (`340mm` had only 1 entry vs. 49 for
`350mm`). Nearly everything that surfaced was either already in the catalog, a reseller
of an already-cataloged brand (Apevie, Race Anywhere, Advanced SimRacing,
SimRacingZone.pl), console-only cosmetic mods (Acelith Design), or a boutique builder
(Racetek Simulators) whose named wheels aren't independently purchasable — rig-bundle
only, fails the standalone-buy-link sourcing requirement.

**One genuine new-to-catalog product added:**
- **id 328 — Cammus 345mm Universal Round Suede Steering Wheel** — bare rim, $69, 345mm,
  universal 70×70mm 6-hole mount, 950g, suede grip over aluminum alloy. Manufacturer-direct
  listing (cammusracing.com), meets all sourcing rules. Dish isn't explicitly published
  but the product description ("pure round design without chamfered edges") is consistent
  with the flat-profile bare rims already in this price bracket. Filed under `subcat:
  "340mm"` (closest existing bucket; catalog has no 345mm-specific bucket) — bolsters the
  catalog's thinnest oval subcat.

**Considered and excluded:** Cammus GT2 ($299, 300mm, 10 RGB buttons + magnetic paddles).
Real electronics, but locked exclusively to Cammus's own DDWB/LP wheelbases with no
third-party adapter path and no SimHub support, from a budget/unproven brand — would also
require inventing a new `conn` code with no existing ecosystem precedent (unlike
`conn:"simagic"`, which serves a well-established, widely-adopted platform). Judgment
call: excluded as too speculative for a "genuinely new and verifiable" bar; revisit if
Cammus ships a SimHub-compatible firmware or a cross-base adapter.

## Result (final)
270 → **271 entries**. Sections: sim 169, oval 100, preorder 2 (down from 6 — 4 items
confirmed shipped this cycle). 1 new entry added (Cammus 345mm rim, id 328, `isNew:true`).
2 stale `isNew` flags cleared (326, 327). 2 `releaseDate` values refreshed to current
brand-stated estimates (297, 326). `validate.sh` passed.
