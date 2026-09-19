# Wheel Update — 2026-09-19

Review window: products released, re-priced or delisted since the previous review date
(August 21, 2026). Just under a month, spanning Gamescom 2026 (Aug 26–30) — the largest
concentration of pending sim racing hardware announcements this quarter, and deliberately
left untouched by the previous cycle for this one to sweep.

Ran on the existing `claude/product-releases-pricing-search-lfkzyk` branch, which still
carried an unmerged PR (#3) from the prior cycle. The working tree already included that
PR's changes (GT Sport marked discontinued, GTSL Pro `releaseDate` refreshed to `2026-09`),
so this pass builds on top of it rather than starting fresh.

## Sim-Lab GTSL Pro (id 326) — re-checked, unchanged

Re-verified directly against Sim-Lab's own stores. The US store still states verbatim
**"Pre-orders open"** at $599 (reg. $649), confirmed via both the rendered page and the
Shopify `products.json` variant feed (price 599.00 / compare 649.00, unchanged). No new
ship-date information was found. `releaseDate:"2026-09"` and the `preorder` section both
still hold — no field changes needed.

One dead end worth recording: the EU store's rendered HTML no longer reproduces the
"Preorder. New orders ship from the end of September" banner text that was captured on
Aug 24 — that content appears to load client-side and isn't reliably present in a static
fetch. A third-party German retailer (germansimracing.de) showed "Sold out" rather than
"Preorder" for their own stock, which is weaker, ambiguous, single-retailer evidence (could
mean an early allocation sold through, or could just be generic wording) and was not acted
on — the authoritative source (Sim-Lab's own US store) is unambiguous and unchanged.

## Gamescom 2026 sweep

- **MOZA — four licensed wheel teasers** (Porsche 911 GT3 RS, Ford Mustang GTD,
  Mercedes-Benz GT, Mercedes VISION ONE-ELEVEN-inspired). All confirmed prototypes with no
  price and no hard date — two are stated as "likely 2027," the Ford as "later this year"
  with no month. Fails both the verifiable-product and hard-date preorder bars. Excluded,
  consistent with the Ford Mustang GTD's exclusion in the prior cycle (it was a tease then
  too, and remains one now — Gamescom didn't convert it into an orderable product).
- **Heusinkveld One SC** — a real, distinct second wheel from an established brand
  (Simucube 3-specific, 270mm composite chassis, 1,060g, 4.3" touchscreen, full spec sheet
  published), shown as a working prototype at Sim Gaming Expo Chicago (Sept 18–20, i.e.
  literally this week). **No price and no release date** ("release date yet to be
  announced"). Real product, real specs, established brand — but fails the hard-date and
  price-required bars just as clearly as the MOZA teasers. Flagged for next cycle: this is
  the strongest "not yet, but soon" candidate on the board, since a working prototype at a
  public expo usually precedes a priced preorder by weeks, not months.

## New entry added (1)

| id | Brand | Model | Price | Section |
|----|-------|-------|-------|---------|
| 332 | GSI | Artemis | $1,875 | preorder |

**id 332 — GSI Artemis.** GSI's new flagship wheel, publicly teased in August and formally
launched September 1, 2026 with a 24-hour 10%-off price ($1,687.50) before reverting to
$1,875 — both figures corroborated across two independent sources (GSI's own store and a
third-party news site) and matching exactly. 290mm, Gorilla Glass 4.3" display, 6 thumb
encoders, 3 mode-select rotaries with 8-mode multiplexing via GSI's UltraLink/simOS, 23
telemetry LEDs (4+15+4), 6 ball-bearing paddles standard, CEMS V4 shifters (N52 magnets,
HALL sensors), USB-C passthrough, 70mm adapter plate. Filed `preorder` (not `sim`) because
GSI's own page states "shipping is scheduled to begin in October" with no firmer date —
matching the month-only-date pattern this catalog already uses for id 326 and id 297.

Two data-honesty notes on this entry:
- **Input count (15) is computed, not quoted.** GSI's page states individual counts (6
  thumb encoders + 3 mode-select rotaries + 6 paddles) but never gives a single combined
  total. This catalog's usual convention (sum of physical inputs) was applied and the
  entry's `notes` says so explicitly, rather than presenting 15 as something GSI itself
  claimed.
- **Weight is contradictory on GSI's own page** — one spec block says "1.3 kilograms total
  mass," another says "1.4kg Total Weight," for the same product. Rather than pick one
  silently, the `dia` field omits weight entirely and the conflict is called out in `cons`.
  (First pass at this Artemis page also nearly conflated the "23 telemetry LEDs" figure
  with a total input count — caught and corrected on a second, more targeted fetch before
  the entry was written. Recorded here as a reminder that a paraphrased AI summary of a
  spec page is not itself a source; the second fetch asked for verbatim quotes and that is
  what actually got used.)

## Price drift check (Simagic, MOZA, GSI)

Ran a numeric (not string) comparison of every catalog price against the live Shopify
variant feed for these three brands, to avoid the false positives a naive substring check
produces (`$1,299` vs `1299.00` is the same number, not a drift). One genuine change found:

| id | Model | Old | New | Class |
|----|-------|-----|-----|-------|
| 308 | Simagic GT Pro Hub K | $299–$339 (sale, reg $339–$369) | $339–$369 | minor (sale ended, reverted to list) |

All other Simagic, MOZA and GSI entries checked (30+ products) matched the live feed
exactly once normalized for currency formatting — no other changes.

## Conspit 300GT (id 40) — re-confirmed, not new

A search summary surfaced "Conspit 300 GT, launched August 2026... priced at $399" as if it
were a new product. It is not — it's already catalogued as id 40 at $399–$450, and the
search result's own description (310's electronics on a 300mm cut-top rim) matches the
existing entry precisely. No action. Recorded because it's exactly the kind of stale-search
false positive this project has been burned by before (cf. the Rexing retraction on
2026-08-21) — verify against the current catalog before treating anything as new.

## Still unreachable — Nardi/Personal, Cammus

Both `nardi-personal.com` and `cammusracing.com` were re-tried this cycle (bare `curl`,
full browser headers, and WebFetch) and still return a Cloudflare challenge (202) or an
empty render on every route available in this environment. The Nardi/Personal pricing
question flagged on 2026-08-24 (16 entries reading 5–12% below two authorized dealers, with
no way to establish real MSRP) remains open, as does verification of id 328 (Cammus).

## Result

270 → **271 entries**. Sections: sim 167, oval 101, preorder 3 (297, 326, 332). 1 new entry
(332, `isNew:true`); 3 stale `isNew` flags cleared (329, 330, 331, from the 2026-08-21
cycle); 1 price correction (308). Review date bumped to September 19, 2026. `validate.sh`
passed.
