# Wheel Update — 2026-08-21

Review window: products released, re-priced or delisted since the previous review date
(August 9, 2026). Twelve-day window, so the release-recency net was deliberately widened
to a full new-to-catalog discovery sweep, as in the 2026-08-09 follow-up pass.

## Method

Two passes:

1. **Web research sweep** per `wheel_research_prompt.md` — brand sites, sim racing news
   sites and authorized retailers. AliExpress/eBay/Etsy excluded (no Simjack/Simmson this
   cycle).
2. **Automated link-rot / delisting sweep (new this cycle).** All 271 `buy` URLs were
   requested directly (`curl -L`, browser UA, follow redirects) and bucketed by HTTP
   status. This is the first cycle to do this systematically, and it is what surfaced the
   discontinuations below — a delisted product is invisible to a keyword search but shows
   up immediately as a 404 on the manufacturer's own product page.

   Result: 185 × 200, 58 × 403, 17 × 202, **11 × 404**. The 403/202 responses are
   Cloudflare bot challenges on `cubecontrols.com`, `sparcousa.com`, `nardi-personal.com`,
   `us.ompracing.com`, `asetek.com`, `leoxz.com` and `cammusracing.com` — not evidence of
   a dead page, and each was left alone. Every 404 was then investigated by hand against
   the brand's own store listing, product sitemap or Shopify product feed.

Where a brand runs Shopify, `\products.json?limit=250` was used to read exact current
variant pricing and stock state rather than trusting a rendered collection page. That
caught one false positive: Simagic's collection page summarised the NEO X series as
"from $239 (reg $329)", but the product page itself still shows $249 (reg $309) — the
catalog value was already correct and was **not** changed.

## New entries added (3)

All three are new *to the catalog* rather than newly released. None of the genuinely
new-since-August-9 announcements qualified (see "Reviewed, nothing to add"), so the sweep
was widened to close verified gaps in existing brand coverage, per the precedent set in
the 2026-08-09 follow-up pass.

| id | Brand | Model | Price | Section |
|----|-------|-------|-------|---------|
| 329 | VNM Simulation | Apex-R | $300 | sim |
| 330 | Simucube | Valo Evo | €924.80–€1,026.59 | sim |
| 331 | GSI | Interlock Ultra 300mm Wheel Rim | $250 | oval |

- **id 329 — VNM Apex-R.** 330mm round, leather over full aluminium, 6 RGB buttons, 4
  twelve-position rotary encoders, 2 seven-way switches, 4-paddle module (aluminium
  shifters + clutch), 9-point RPM LED strip, SimHub-compatible, GX12→USB, 2,300g,
  SKU VNM-SWAPXR01, 20 in stock at $300. Surfaced from VNM's product sitemap while
  chasing the id 92 dead link — it sits directly alongside the GT wheel the catalog
  already carries and was simply never picked up. Also stocked by several EU/NA
  resellers. Input count of 20 uses the same counting convention as the existing VNM
  GT V1 entry, and the breakdown is stated in `notes`.
  - Note: VNM's own page carries two conflicting input lists (a marketing blurb claiming
    "12 customizable RGB buttons; 2 thumb encoders; 2 rotary encoder"). The **Technical
    Parameters** table was treated as authoritative.
- **id 330 — Simucube Valo Evo.** Simucube's first open-top bullhorn rim; re-shapes the
  Valo GT-23 with a leather 315mm rim while keeping the same Valo electronics, paddles
  and Simucube Wireless. 18 programmable RGB LEDs (Link Hub required to drive them),
  1.8kg, 2000mAh NiMH. Released late 2023 and listed on the Simucube **EU** store today,
  but absent from the catalog and absent from the US store — hence the EUR price, unlike
  the other Simucube entries. Inputs set to 20 to match the Valo GT-23 entry, which
  shares its electronics.
- **id 331 — GSI Interlock Ultra 300mm Wheel Rim.** $250, 1,361g, integrated LED Matrix,
  rigid alloy core. The fourth GSI Interlock rim; the catalog already carried GT 300mm,
  GT 320mm and Oval 320mm (ids 323–325) but not this one. Filed `oval`/`300mm` to match
  id 323. Unlike its siblings the LED Matrix is integral rather than optional, and GSI
  explicitly states it is "not intended for use on third party products" — recorded as a
  con, since the other three are universal 70mm PCD.

## Reviewed, nothing to add

- **MOZA × Ford Mustang GTD** — teaser image only ("MOZA Racing x Ford. Coming to
  Gamescom 2026"). No specs, no price, no date. Fails the hard-date preorder bar and the
  verifiable-product bar.
- **Gamescom 2026 (Aug 26–30, Cologne)** — falls *after* this review date. MOZA's stand
  is the July 28 product wave (R16 Ultra, R5 Pro — wheelbases, out of scope) plus MotoGP
  hardware. Nothing wheel-shaped is announced yet. **Next cycle should re-sweep Gamescom
  specifically**; it is the largest concentration of pending announcements this quarter.
- **MOZA × Gran Turismo World Series** (partnership live August 15, 2026) — PS5 hardware
  "in development", no product.
- **Simucube "Valo GT-23 Leather Version"** and **"Tahko Round Orange Edition"** —
  colour/material SKUs of wheels already in the catalog (ids 3, 2/73), not distinct
  products.
- **GSI wheel + Simucube 2 Pro bundles** (published Aug 20, 2026) — wheelbase bundles,
  out of catalog scope.
- **Cube Controls, Ascher Racing, Asetek SimSports** — no new wheel or rim since the last
  review. Cube Controls' summer closure (Aug 8–23) is unchanged from the last cycle's note.

## Discontinuations and delistings found — marked in place

The editorial rules in `wheel_research_prompt.md` allow `price` edits on existing entries
and nothing else, so these were first reported rather than applied. **Per explicit user
direction this cycle**, all four were then marked discontinued *in place*: each keeps its
entry, specs and buy link untouched, and gains one `cons` line plus a `notes` sentence
recording the delisting, the evidence date and where stock can still be found. Nothing
was removed — the same non-destructive treatment given to id 29 on 2026-08-09.

**Confirmed gone from the manufacturer's own store:**

| id | Entry | Evidence |
|----|-------|----------|
| 305 | Simagic GT4 | `simagic.com/products/gt4-formula` returns a real 404 ("Page not found"); absent from the `/collections/steering-wheel` listing. Marketing page `/pages/details-gt4` still resolves but is not purchasable. Still listed by third-party retailers (Simline, Ricmotech, Pit Lane) as remaining stock. |
| 91 | Rexing Mayaris V1.1 | Rexing's steering-wheel category page reports "Showing all 7 results" and lists only the Timun GT v1.1, the Mayaris 2 and a Mayaris 2 "Imperfect Deal" — no V1. The site nav carries a separate "Previous models support" section. Weaker evidence than the two above (absence from a listing, not a positive statement), and the entry's wording says so. |
| 53 | SimCore STD-WS GEN2 | SimCore's shop lists six `std-wd-gen2-*` colourways (wired) and six `std-98-*`, but **no** `std-ws-*` SKU. The wireless variant appears dropped; the wired GEN2 remains at AUD$595. SimCore still sells the Simucube wireless BLE button plate module separately. |

**Retracted — claimed discontinued, then disproved on review (see "Verification passes"):**

- **id 90 Rexing Mayaris 2** — **not discontinued.** Still sold by Rexing directly at
  €1,360 excl. VAT with a 10-day lead time, plus a discounted "Imperfect Deal" unit at
  €1,088 excl. VAT. The marking was applied and then reverted in full.

**Out of stock, not discontinued — no action recommended:**

- **id 303 Simagic FX Formula** — "Sold out" on Simagic's own store, but still listed
  with a live price ($239, reg $359). Price updated; no delisting.
- **id 159 GSI FPE V2 "Simucube" Edition** — sold out on gomezsimindustries.com, but
  **in stock at $1,579 on the Simucube US store**, which is the URL the catalog uses.
  Not a discontinuation.
- **id 7 Simucube × BavarianSimTec Delta Pro SC** — out of stock on both Simucube stores.
  Price corrected; still catalogued.

## Dead `buy` links where the product still exists — four of seven fixed

Pure URL rot from site restructures; the catalog's only broken outbound links. **Per
explicit user direction this cycle**, the four with an exact same-product replacement
were repointed (ids 248, 249, 251, 92 — marked ✅ below, each re-verified 200 after the
edit). The three that would change *which site* the entry points to were left alone for
a later decision (marked ⏸), since repointing them is an editorial choice about sourcing,
not a URL correction.

| id | Entry | Current working URL |
|----|-------|---------------------|
| ✅ 248 | Racetech Flat Suede 350 | `racetech-usa.com/shop/accessories/steering-wheels/flat-wheel` |
| ✅ 249 | Racetech Flat Suede 330 Flat-Bottom | `.../steering-wheels/flat-bottomed-steering-wheel-330mm` |
| ✅ 251 | Racetech Drag 330 | `.../steering-wheels/drag-steering-wheel` |
| ✅ 92 | VNM GT V1 | `vnmsimulation.com/product/vnm-gt-steering-wheel` (slug dropped `-v1`) |
| ⏸ 170 | Sparco P310 | Was a SimCore reseller link; Sparco's own `sparcousa.com/p-310` is live |
| ⏸ 54 | SimCore OMP GT-WS | Pointed at `simcore.com.au/contact-us/`, now 404; site uses `/product/…` paths |
| ⏸ 77 | OMP 320 Alu GT + SC Wireless Button Plate | Pointed at the delisted `std-ws-gen2-stealth` page |

Racetech pricing was re-verified while confirming the moves: $199.99 / $229.99 / $199.99,
matching the catalog's $200 / $230 / $200 — no price drift, purely a URL change.

Two further observations, recorded but not acted on:

- **ids 92 and 99 are duplicates** — the same VNM GT V1 wheel, same specs, same price,
  differing only in prose and `buy` URL (id 99 points at the bare domain). Pre-existing,
  not introduced this cycle.
- **VNM has dropped "V1"** from the product name; it is now just "VNM GT Steering Wheel".
  Model renames are outside the allowed edit set.

## Price corrections applied (12 fields, 11 distinct products)

| id | Model | Old | New | Class |
|----|-------|-----|-----|-------|
| 302 | Simagic FX Pro Formula | $549 (reg $759) | $499 (reg $549) | minor (−$50) |
| 303 | Simagic FX Formula | $289 (reg $359) | $239 (reg $359) | minor (−$50) |
| 306 | Simagic GT1 | $309 | $239 (reg $309) | minor (−$70) |
| 81 | MOZA GS V2P GT | $349 | $369 | minor (+$20) |
| 83 | MOZA Vision GS | $749 | $699 | minor (−$50) |
| ✅ 92 | VNM GT V1 | ~$350–$399 | $405 (reg $450) | minor (+~$51) |
| 99 | VNM GT V1 (dup entry) | ~$350–$399 | $405 (reg $450) | minor (+~$51) |
| 7 | Simucube × BST Delta Pro SC | $1,899+ | $1,799 | minor (−$100) |
| 30 | GSI X-29 | $659–$750 | $650–$895 | minor (+$145 at top of range) |
| 35 | GSI GT-MAX32 | $1,400–$1,600 | $1,385–$1,797 | **major (+$197 at top of range)** |
| 37 | GSI Interlock Base Module + Oval 320mm Rim | $727–$800 | $495–$895 | **major (−$232 at base config)** |
| 71 | GSI Interlock + Oval 320mm Rim | $727–$800 | $495–$895 | **major (−$232 at base config)** |

GSI ranges were rebuilt from the live Shopify variant matrix (paddle count × body
material × LED Matrix × rim), so the new ranges span the true cheapest and dearest
configurations. The old $727–$800 range for ids 37/71 did not correspond to any current
variant pair.

Verified unchanged: Simagic GTS, GT Neo, GT Pro Hub, GT Pro Hub K, NEO X series, Zeus
Formula/GT/Sport; GSI GXL V2, FPE V2, Hyper SL, Hyper P1, Interlock Ultra, GT/Oval rims;
all remaining MOZA wheels; Simucube Savu Pro/Sport, Valo GT-23, Tahko GT-21, Tahko Round;
Racetech 248/249/251.

## Preorder status (both re-checked, no field changes)

- **id 326 — Sim-Lab GTSL Pro.** Still "Pre-orders open" on `sim-lab.us` at $599 (down
  from a $649 list). The US store is no longer showing sold out, which it was on Aug 9,
  but no explicit ship date is published any more — the `releaseDate:"2026-08-24"` from
  last cycle's EU-store statement is left in place. Catalog price `$599–$649` still
  spans the current sale and list prices. **Worth re-checking after Aug 24**: if it
  ships, it should move `preorder` → `sim`.
- **id 297 — Zen's Simwheels LMZ Evo.** Still preorder, "Expected delivery starting at
  Mid-September", From €1,229. `releaseDate:"2026-09"` and price both still correct.

## Result

271 → **274 entries**. Sections: sim 171, oval 101, preorder 2. 3 new entries added
(329, 330, 331, all `isNew:true`); 1 stale `isNew` flag cleared (328, from the 2026-08-09
cycle); 12 price fields corrected across 11 products (3 flagged ≥$150); review date
bumped to August 21, 2026. `validate.sh` passed.

Follow-up pass, same day, on user direction: ids 53, 90, 91 and 305 marked discontinued
in place (one `cons` line and one `notes` sentence each; no specs, prices or buy links
touched), and four dead `buy` URLs repointed (248, 249, 251, 92), all four re-verified
200. Entry count, section counts and every price are unchanged by that pass, and
`validate.sh` passed again.

One structural bug fixed in passing: id 328 was the final array element and carried no
trailing comma, so appending after it produced the exact "missing comma between entries
with a `// comment` between them" syntax error listed in the project's known-bugs notes.
Caught by `validate.sh` before commit.


---

# Verification passes (post-commit review)

The first commit was reviewed adversarially — attacking each claim rather than
re-confirming it. Three passes; two found real defects in my own work.

## Pass 1 — structure

All three new entries carry every required field; all three `subcat` values land in
buckets that already exist in their section (`VNM Simulation` 3, `Simucube Brand` 9,
`300mm` 5); no duplicate IDs; `isNew` is exactly {329, 330, 331}. Confirmed the new
id 331 (Interlock Ultra 300mm **rim**, $250, `conn:"gray"`, 0 inputs) does not duplicate
the existing id 36 (Interlock Ultra **module**, $695–$925, `conn:"blue"`, 30 inputs).

## Pass 2 — price precision (5 defects found in my own edits)

Reading Shopify's variant feed with `compare_at_price`, rather than a rendered page,
showed I had collapsed several variant ranges to a single figure:

| id | Model | I had written | Correct | Why |
|----|-------|---------------|---------|-----|
| 306 | Simagic GT1 | $239 (reg $309) | $239–$269 (reg $309–$329) | SR variants $239, SD variants $269 — the entry covers both |
| 313 | Simagic NEO X-350W | $249 (reg $309) | $239 (reg $329) | The one NEO X variant priced differently from its three siblings; I had applied the sibling price to all four |
| 308 | Simagic GT Pro Hub K | $339 | $299–$339 | Leather bundles are $299 (reg $369); the entry explicitly covers the bundle options |
| 81 | MOZA GS V2P GT | $369 | $369 (sale, reg $399) | Live compare-at price; matches the style of sibling MOZA entries |
| 83 | MOZA Vision GS | $699 | $699 (sale, reg $749) | Same |

Verified correct and left alone: id 307 GT Pro Hub ($339 — the $438–$448 variants bundle
a rim, which that entry explicitly excludes), ids 310–312 NEO X ($249/reg $309), id 304
GTS, id 309 GT Neo, id 302 FX Pro, id 303 FX Formula, ids 318–320 Zeus, and the GSI
ranges rebuilt in the first commit (30, 35, 37, 71).

## Pass 3 — attacking the discontinuation claims (1 claim retracted)

Each of the four claims was re-tested against a *different* source than the one that
produced it.

- **id 305 Simagic GT4 — HOLDS, strengthened.** Simagic's full Shopify feed carries 114
  products and **zero** handles containing `gt4`, alongside the hard 404. Positive
  evidence from a live feed, not an absence in a sitemap.
- **id 53 SimCore STD-WS GEN2 — HOLDS, strengthened.** SimCore's own product search for
  "STD-WS" returns **"No products were found"** — a positive statement from the site
  itself, not an inference.
- **id 90 Rexing Mayaris 2 — RETRACTED. The claim was wrong.** Rexing's steering-wheel
  *category page* shows the Mayaris 2 in stock at €1,360 excl. VAT with a 10-day lead
  time. My evidence had been its absence from `rexing.eu/product-sitemap.xml` — and that
  sitemap is simply stale: it omits the live product URL
  (`/product/rexing-formula-steering-wheel-mayaris-2/`) *and* the "Previous models
  support" page that appears in the site nav. The discontinued `cons` line and `notes`
  sentence were both removed.
- **id 91 Rexing Mayaris V1.1 — HELD, but wording weakened.** Still absent from a
  complete "Showing all 7 results" category listing, which is real evidence — but it is
  absence-from-a-listing, not a positive statement, and the note now says exactly that
  instead of asserting Rexing "no longer sells it directly".

**Lesson for the next cycle, and for `wheel_research_prompt.md`:** a sitemap is not a
catalog. Rexing's product sitemap was stale in both directions. Delisting claims should
require either a hard 404 *plus* absence from a live product feed or category listing, or
a positive "not found" from the site's own search — never a sitemap absence alone.

## Corrections that followed from Pass 3

- **id 90 Mayaris 2** — discontinued marking reverted; `buy` repointed to the live slug
  `/product/rexing-formula-steering-wheel-mayaris-2/` (the old `/rexing-formula-wheel-mayaris-2/`
  404s — same-product URL rot, the class approved for fixing); price `~€1,100–€1,300` →
  `€1360 (export) / €1700 (EU)`, matching the excl./incl.-VAT convention already used by
  the Timun entry (25% HR VAT: 1360 × 1.25 = 1700). This is a **major** increase against
  the stale catalog figure. The first `cons` line, which quoted the old "~€1,100+" price,
  was updated to match.
- **id 275 Rexing Timun GT** — `€1340 (export) / €1675 (EU)` → `€1420 (export) / €1775
  (EU)`; also now shown out of stock on Rexing's own store. Minor (+€80 export).

## Coverage limits — stated plainly

- **75 entries were never link-verified.** `cubecontrols.com` (17), `sparcousa.com` (16),
  `nardi-personal.com` (16), `us.ompracing.com` (13), `asetek.com` (7), `leoxz.com` (5)
  and `cammusracing.com` (1) return 403/202 bot challenges. Spot-checking confirmed the
  bodies are small challenge pages with no 404 language, and Cube Controls' Phoenix page
  was reachable by a second route and is live — but "probably fine" is not "verified",
  and these entries carry no link-rot guarantee from this cycle.
- **Cube Controls prices were not systematically re-checked** for the same reason. The
  one entry that was checked (id 327 Phoenix) is correct: €963 incl. VAT on the product
  page, matching the catalog's "From €789 (€963 incl. VAT)" at 22% IT VAT.
- **Gamescom 2026 (Aug 26–30) is not covered** — it opens after this review date.

## Pre-existing data-quality issues found while verifying (not fixed)

- **id 261 Cube Controls GT Sport (Wireless)** has `price:"€?"` — a placeholder, not a
  price.
- **Duplicate entries:** ids 37/71 (GSI Interlock + Oval 320mm Rim — identical product
  and URL), ids 92/99 (VNM GT V1), and probably ids 93/100 (Soelpec Spectra XR) and
  2/73 (Simucube Tahko Round). Ids 43/160/161 share one P1Sim URL but are distinct
  models.

## Final state after all passes

274 entries, sections sim 171 / oval 101 / preorder 2, `isNew` = {329, 330, 331},
`validate.sh` passing. Three entries marked discontinued in place (53, 91, 305), one
retracted (90). 19 price fields corrected in total across both commits.
