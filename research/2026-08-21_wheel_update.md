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

## Discontinuations and delistings found (reported, catalog NOT edited)

The editorial rules in `wheel_research_prompt.md` allow `price` edits on existing entries
and nothing else, so none of the following were applied. They are recorded here for a
decision.

**Confirmed gone from the manufacturer's own store:**

| id | Entry | Evidence |
|----|-------|----------|
| 305 | Simagic GT4 | `simagic.com/products/gt4-formula` returns a real 404 ("Page not found"); absent from the `/collections/steering-wheel` listing. Marketing page `/pages/details-gt4` still resolves but is not purchasable. Still listed by third-party retailers (Simline, Ricmotech, Pit Lane) as remaining stock. |
| 90 | Rexing Mayaris 2 | Absent from `rexing.eu/product-sitemap.xml`. The sitemap's only complete wheel is the Timun GT (id 275); Mayaris survives only as spare parts (`sticker-set-for-mayaris-2`, `pcb_may1-0`). Third-party retailers (Demon Tweeks, Trak Racer, Simufy, racegear.eu) still list stock. |
| 91 | Rexing Mayaris V1.1 | Same as above. |
| 53 | SimCore STD-WS GEN2 | SimCore's shop lists six `std-wd-gen2-*` colourways (wired) and six `std-98-*`, but **no** `std-ws-*` SKU. The wireless variant appears dropped; the wired GEN2 remains at AUD$595. SimCore still sells the Simucube wireless BLE button plate module separately. |

**Out of stock, not discontinued — no action recommended:**

- **id 303 Simagic FX Formula** — "Sold out" on Simagic's own store, but still listed
  with a live price ($239, reg $359). Price updated; no delisting.
- **id 159 GSI FPE V2 "Simucube" Edition** — sold out on gomezsimindustries.com, but
  **in stock at $1,579 on the Simucube US store**, which is the URL the catalog uses.
  Not a discontinuation.
- **id 7 Simucube × BavarianSimTec Delta Pro SC** — out of stock on both Simucube stores.
  Price corrected; still catalogued.

## Dead `buy` links where the product still exists (reported, not edited)

Pure URL rot from site restructures. The rules forbid editing `buy`, so these are listed
for a decision — they are the catalog's only broken outbound links.

| id | Entry | Current working URL |
|----|-------|---------------------|
| 248 | Racetech Flat Suede 350 | `racetech-usa.com/shop/accessories/steering-wheels/flat-wheel` |
| 249 | Racetech Flat Suede 330 Flat-Bottom | `.../steering-wheels/flat-bottomed-steering-wheel-330mm` |
| 251 | Racetech Drag 330 | `.../steering-wheels/drag-steering-wheel` |
| 92 | VNM GT V1 | `vnmsimulation.com/product/vnm-gt-steering-wheel` (slug dropped `-v1`) |
| 170 | Sparco P310 | Was a SimCore reseller link; Sparco's own `sparcousa.com/p-310` is live |
| 54 | SimCore OMP GT-WS | Pointed at `simcore.com.au/contact-us/`, now 404; site uses `/product/…` paths |
| 77 | OMP 320 Alu GT + SC Wireless Button Plate | Pointed at the delisted `std-ws-gen2-stealth` page |

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
| 92 | VNM GT V1 | ~$350–$399 | $405 (reg $450) | minor (+~$51) |
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

One structural bug fixed in passing: id 328 was the final array element and carried no
trailing comma, so appending after it produced the exact "missing comma between entries
with a `// comment` between them" syntax error listed in the project's known-bugs notes.
Caught by `validate.sh` before commit.
