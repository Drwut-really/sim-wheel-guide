# Wheel Update — 2026-07-10

Review window: products released or announced since the previous review date (June 30, 2026).

## Method
- MCP search first (SearXNG web search + page reads, crawl4ai/WebFetch for spec pages),
  then a Codex deep-verification sweep to cross-check candidates and catch misses.
- Scope per `wheel_research_prompt.md`: brand sites / review sites / authorized retailers
  only; AliExpress/eBay/Etsy excluded (no Simjack/Simmson this cycle). Preorders admitted
  on **hard dates only**. Fanatec / Logitech / Thrustmaster out of scope.

## New entries added (2)
Both are upcoming with confirmed ~August 2026 ship dates → `section:"preorder"`, `isNew:true`.

- **id 326 — Sim-Lab GTSL Pro** — 300mm inverted-D GT wheel. $599 (reg. $649) US /
  €549 (reg. €599) EU. 12 buttons, 6 rotary encoders, two 7-way thumb switches, magnetic
  double-rocker shifters + dual clutch, 114 telemetry RGB LEDs + 3-8-3 RPM strip, SimHub,
  wired USB, 70mm universal QR, 1,580g. Pre-order shipping first week of August 2026.
  Source: https://sim-lab.us/products/gtsl-pro-sim-racing-steering-wheel ,
  https://simracing-pc.de (ship window).
- **id 327 — Cube Controls Phoenix** — new flagship Formula line. From €789 ex-VAT
  (€963 incl. VAT). Three hub tiers: Base (no clutch), Premium (CNC aluminum, 1 clutch),
  Extreme (3D-printed generative-design titanium hub, 2 clutches). 10 RGB buttons, 4 front
  + 2 thumb rotary encoders, 1 absolute rotary, 2 joysticks, carbon fiber paddles, USB-C
  passthrough, 1000Hz, SimHub, no screen. Preorders open July 10, 2026; ships in ~15
  working days. Source: https://www.cubecontrols.com/product/phoenix/ .

## Prior-run flags cleared
Removed `isNew:true` from ids 323/324/325 (GSI GT/Oval rims added in the June cycle) so the
🆕 tab shows only this cycle's additions.

## Reviewed, nothing to add
- **MOZA** — CES 2026 wheels (KS Pro, CS Pro, Porsche Mission R, Lamborghini Revuelto)
  already in catalog. No new post-June release.
- **Simagic** — Zeus Formula/GT/Sport already tracked. Simucube 3 wheelbase news only.
- **Asetek SimSports** — no new wheel since the Forte/La Prima Next-Gen range; Invicta still
  has no dedicated wheel.
- **GSI** — Hyper P1/SL, GXL/FPE V2, Interlock, new rims all already tracked.
- **Ascher Racing** — only an 8" dashboard accessory + existing Simucube collab.
- **Conspit 280FR** — "coming soon" (Jun 18, 2026), no hard date → excluded per strict bar.
- **MVH Studios GTX 4.0 / GTXR 4.0 Pro** — "coming soon," no firm date → excluded.
- **Fanatec × Nissan** (July 7, 2026) — licensing announcement only, no specs/date, and
  Fanatec is out of catalog scope → excluded.

## Price verification
No ≥$150 change found on flagship wheels from Simucube, Asetek, Cube Controls, Simagic, or
MOZA during this sweep (confirmed via Codex). No existing prices changed this cycle.

## Result
268 → **270 entries**. Sections: sim 165, oval 99, preorder 6. Review date bumped to
July 10, 2026. `validate.sh` passed.
