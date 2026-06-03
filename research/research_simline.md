# Simline.eu USB Rim Research

## Context
Source: https://simline.eu — full sweep on 2026-04-24
Total products inspected: ~30 (Simline house wheels, MOZA reseller listings, button plates, bare rims, QRs)
New candidates: 2 (Simline BPv3 Lite + BPv3 Ultimate — universal modular button plates)

The existing wheel guide already has Simline coverage at id 55 as a single aggregated entry covering the car-specific replica wheels: 720s GT3, Huracan GT3, AMG GT3, Corvette C7R, Fiesta WRC, R5 WRC, GT3-R, GT3 Cup, and WRC/TCR. The standalone car-specific button plates sold separately (Button Plate GT3 Cup, Button Plate GT3-R, Button Box Fiesta WRC, WRC/TCR Button Box) are simply the electronics half of those same complete-wheel SKUs — they're duplicates of the existing entry and intentionally omitted here.

The bare rims sold under "Only Rims" (GT3 Cup D-Shape Suede, GT3 Cup R320 Suede, Rally 330/65mm, Rally 350/65mm, U300 Suede/Leather — all ~€131–€155) are pure mechanical rim shells with no electronics, so they fall under "non-wheel accessory" and are out of scope.

Simline also resells MOZA, Simagic, Simucube, and Conspit wheels — those should be sourced from the OEM sites, not added under Simline.

The two **truly new** Simline-house USB candidates are the BPv3 Lite and BPv3 Ultimate — a universal modular button-plate platform that pairs with any rim using either the 3×50.8mm or 6×70mm bolt pattern. Unlike the car-replica wheels in the existing entry, the BPv3 family is rim-agnostic (you can pair it with a Sparco/OMP/Momo round, a D-shape GT, or a smaller formula rim) and is a distinctly different product category — closer to Ascher's B-series button plates than to the GT3 replicas.

## New wheel entries (paste-ready)

```js
// id will be reassigned at integration time — placeholder shown
{id:?, brand:"Simline", model:"BPv3 Ultimate (Universal Button Plate, Dual Clutch)", section:"usb", subcat:"SimLine (Poland)",
 conn:"black", dia:"rim-dependent", shape:"Universal (round/D/oval)", inputs:29, display:false,
 simhub:true, bt:false, price:"€430 (USB) / +~€100 wireless (~$455 USD)",
 pros:["29 functions (extendable +6 via PCB pads) — among the highest input counts on a single button plate","Dual-clutch system with rear-mounted bias potentiometer","MEC/ALPS automotive-grade switches (same as TCR-class race cars, 3.5N actuation)","Two bolt patterns (3×50.8 and 6×70) — pairs with formula rims AND GT/round rims","Forged carbon front face, single-piece CNC aluminum back","Detachable USB cable (no fragile spiral coil failure point)","Optional SC2 wireless module with external antenna and analog signal support","Two Bourns 16-position encoders with push, plus D-pad encoder for menu/brake-bias"],
 cons:["No display — pair with external dash if you need telemetry","Wireless variant adds significant cost","Standalone plate only — rim is sold separately, total cost approaches GT3 replica wheel pricing once paired","No Simagic MAGLINK option — USB or SC wireless only"],
 buy:"https://simline.eu/en/bpv3-ultimate/simline-bpv3-ultimate",
 notes:"Closest competitor to Ascher B24M-SC and SimCore BB Ultra V2. Best Simline pick for builders who want to bring their own rim (Sparco P310, OMP 320, Momo Mod 78, custom carbon GT) and bolt on premium electronics with dual clutch. SQR-direct via 6×70 pattern."},

{id:?, brand:"Simline", model:"BPv3 Lite (Universal Button Plate)", section:"usb", subcat:"SimLine (Poland)",
 conn:"black", dia:"rim-dependent", shape:"Universal (round/D/oval)", inputs:14, display:false,
 simhub:true, bt:false, price:"€330 (USB) / +~€100 wireless (~$350 USD)",
 pros:["Same MEC/APEM automotive switches as the Ultimate at lower cost","Bourns encoders with built-in push","Single-piece CNC aluminum housing — fully rigid","Detachable USB cable (replaceable, no spiral failure)","Universal mounting compatible with most rims (3×50.8 / 6×70)","Optional SC2 wireless"],
 cons:["No dual clutch (Ultimate-only feature)","Fewer inputs than Ultimate (~14 vs 29)","No display","Rim sold separately"],
 buy:"https://simline.eu/en/bpv3-ultimate/simline-bpv3-lite",
 notes:"Entry/intermediate version of the BPv3 platform. Good match for sim racers who want premium MEC switches and the universal mounting flexibility but don't need dual clutch or the full 29-input layout. Pairs naturally with Simline's own bare rims (€131–€155) or any Sparco/OMP round."}
```

## Notes
- **Brand families seen on simline.eu**: Simline (house brand), MOZA (reseller), Simagic (reseller), Simucube (reseller), Conspit (reseller), plus QR adapters (Fanatec QR1/QR2/QR2 PRO, Simagic QR50/70, MOZA QR, Conspit CDP/CDR).
- The existing aggregated Simline entry (id 55) covers all car-replica complete wheels — no new entries needed there.
- Standalone car-specific button plates (GT3 Cup BP €214, GT3-R BP €307, Fiesta WRC BB €231, WRC/TCR BB €378) are the same electronics as their complete-wheel counterparts, just without the rim. The existing entry's pricing range (€450–€900) implicitly covers buying plate + bare rim combos. Adding them as separate entries would be redundant.
- The BPv3 family is genuinely distinct because it's universal/modular rather than car-specific — that's why it warrants its own entry alongside the existing replica-wheel aggregation.
- Pricing converted from PLN at ~4.20 PLN = €1 (rate observed on the Simline page in April 2026). USD approximations use ~€1 = $1.06.
- All BPv3 variants are SQR-direct compatible (6×70 bolt pattern) so no extra adapter needed for Simucube 2.
- Worth flagging for the user: Simline also resells **MOZA ESX, CS v2P, RS v2, TSW Truck** which are NOT in the existing wheel list — but those are MOZA-branded products and should be researched from MOZA's catalog directly, not added under Simline.
