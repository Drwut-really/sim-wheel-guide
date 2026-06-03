# MOZA / Simagic / Asetek Catalog Audit

Date: 2026-04-24
Auditor: claude (opus-4-7-1m)

## Existing coverage gap analysis

| Brand   | In current HTML | On brand site | Missing |
|---------|----------------:|--------------:|---------|
| MOZA    | 8 (KS, GS V2P GT, FSR2, Vision GS, KS Pro, CS Pro, Porsche Mission R, Lambo Essenza SCV12) | 13 (adds CS V2P, RS V2, ESX, TSW Truck, Lambo Revuelto) | **CS V2P, RS V2, ESX, TSW Truck Wheel, Lamborghini Revuelto** |
| Simagic | 2 generic stubs (id 57 "NEO X Hub + XGT Pro Round" generalisation, id 58 "GT NEO / FX / FX Pro" generalisation, id 76 oval-section dup of 57) | 9 distinct rims (FX Pro, FX, GT4, GT1, GTS, GT Neo, NEO X-330T, NEO X-310G, NEO X-330R, NEO X-350W) | **FX Pro (proper card), FX, GT4, GT1, GTS, GT Neo, NEO X-330T, NEO X-310G, NEO X-330R, NEO X-350W** (id 57/58/76 should be retired/replaced — see notes) |
| Asetek  | 3 (La Prima Formula id 88, Invicta Formula sc2 id 89, Invicta Formula usb id 96; plus an old Forte Formula Pro stub id 59) | 6 wheels (La Prima Formula, La Prima GT Comfort+, Forte Formula, Forte Formula Pro, Invicta Formula, Initium PC) | **La Prima GT (Comfort+ Round), Forte Formula (no display variant), Forte Formula Pro (proper card replacing id 59 stub), Initium PC** |

Existing catalog hi-water id is 101 (regular wheels) and 200 (preorders). New regular IDs start at **102**.

---

## New entries to add (paste-ready)

### MOZA — adapter:"MOZA Universal Hub Kit"

#### CS V2P Steering Wheel

```js
{id:102,brand:"MOZA",model:"CS V2P Steering Wheel (via Universal Hub Kit)",section:"sc2",subcat:"MOZA (via Universal Hub Kit)",conn:"blue",adapter:"MOZA Universal Hub Kit",dia:"330mm (13\")",shape:"GT Round (microfiber leather)",inputs:24,display:false,simhub:false,bt:false,price:"$229 (sale, reg $279)",pros:["13-inch true-to-life GT round rim — closest MOZA size to oval spec","Aviation-grade aluminum frame + microfiber leather grips","Forged carbon fiber paddles with contactless photoelectric sensors","6 mechanical buttons + 2 magnetic shifters + 2 joysticks (10 keys) + 2 rotary encoders","10 RGB sequential shifter LEDs","Wireless connectivity to MOZA bases — Universal Hub Kit brings to SC2"],cons:["MOZA Universal Hub Kit required for SC2 (~$50–100)","No SimHub — MOZA Pit House software only","No display — RGB LED bar only","Frequently sold out / waitlisted"],buy:"https://us.mozaracing.com/products/cs-v2p-wheel",notes:"330mm GT round at $229 — best price-per-mm round wheel in MOZA lineup. Add Hub Kit for SC2."},
// ALSO usb-section duplicate:
{id:103,brand:"MOZA",model:"CS V2P Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"MOZA Universal Hub Kit",dia:"330mm (13\")",shape:"GT Round",inputs:24,display:false,simhub:false,bt:false,price:"$229",pros:["330mm GT round at $229","Forged carbon paddles","Microfiber leather grips","Universal Hub Kit enables SC2 use"],cons:["MOZA Pit House only — no SimHub","Often out of stock"],buy:"https://us.mozaracing.com/products/cs-v2p-wheel",notes:"See SC2 section for full details."},
```

#### RS V2 Steering Wheel

```js
{id:104,brand:"MOZA",model:"RS V2 Steering Wheel (via Universal Hub Kit)",section:"sc2",subcat:"MOZA (via Universal Hub Kit)",conn:"blue",adapter:"MOZA Universal Hub Kit",dia:"330mm (13\")",shape:"GT Round (genuine leather)",inputs:24,display:false,simhub:false,bt:false,price:"$369 (sale, reg $439)",pros:["330mm GT round, 13-inch standard race-rim size","Genuine leather grips with precision stitching — premium feel","Forged carbon face plate + aluminum back plate","10 backlit mechanical buttons (8 colors) + 2 joysticks + 2 rotary encoders","Magnetic dual-clutch carbon paddles (switchable single/dual)","10-LED RGB sequential RPM strip"],cons:["MOZA Universal Hub Kit required for SC2 (~$50–100)","No SimHub — MOZA Pit House only","No display","Genuine leather wears with extended use"],buy:"https://us.mozaracing.com/products/rs-v2-wheel",notes:"Premium 330mm leather GT round wheel — genuine leather upgrade over CS V2P. Universal Hub Kit brings to SC2."},
{id:105,brand:"MOZA",model:"RS V2 Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"MOZA Universal Hub Kit",dia:"330mm (13\")",shape:"GT Round leather",inputs:24,display:false,simhub:false,bt:false,price:"$369",pros:["330mm genuine leather round","Dual-clutch magnetic paddles","10 RGB RPM LEDs","Forged carbon face plate"],cons:["MOZA Pit House only","Universal Hub Kit needed for SC2"],buy:"https://us.mozaracing.com/products/rs-v2-wheel",notes:"See SC2 section."},
```

#### ESX Steering Wheel

```js
{id:106,brand:"MOZA",model:"ESX Steering Wheel (via Universal Hub Kit)",section:"sc2",subcat:"MOZA (via Universal Hub Kit)",conn:"blue",adapter:"MOZA Universal Hub Kit",dia:"280mm",shape:"Round (Xbox-licensed)",inputs:22,display:false,simhub:false,bt:false,price:"$129 (sale, reg $139)",pros:["Cheapest MOZA wheel — entry into the ecosystem at $129","Officially Xbox-licensed (works on PC too)","Solid aluminum alloy rim","ISF PU non-slip grips — sweat-proof","22 customizable buttons including 2 joysticks","10 high-brightness RGB LED beads","Formula and 12-inch mod kits sold separately"],cons:["MOZA Universal Hub Kit required for SC2 (~$50–100)","No SimHub — MOZA Pit House only","No display","280mm only","Plastic-feeling vs higher-end MOZA wheels"],buy:"https://us.mozaracing.com/products/esx-steering-wheel",notes:"Entry-level MOZA at $129. With Hub Kit becomes the cheapest path to a 70mm SC2-compatible wheel."},
{id:107,brand:"MOZA",model:"ESX Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"MOZA Universal Hub Kit",dia:"280mm",shape:"Round",inputs:22,display:false,simhub:false,bt:false,price:"$129",pros:["Cheapest MOZA wheel — $129","Xbox + PC licensed","22 inputs","10 RGB LEDs"],cons:["No SimHub","No display","Universal Hub Kit needed for SC2"],buy:"https://us.mozaracing.com/products/esx-steering-wheel",notes:"See SC2 section. Entry-level value pick."},
```

#### TSW Truck Wheel

```js
{id:108,brand:"MOZA",model:"TSW Truck Wheel (via Universal Hub Kit)",section:"sc2",subcat:"MOZA (via Universal Hub Kit)",conn:"blue",adapter:"MOZA Universal Hub Kit",dia:"400mm",shape:"4-spoke Truck (Euro/American Truck Sim)",inputs:18,display:false,simhub:false,bt:false,price:"$229 (sale, reg $299)",pros:["World's first purpose-built truck sim wheel","True-to-life 400mm diameter — matches real truck cabs","Aerospace-grade 4mm aluminum frame + hand-stitched microfiber leather","14 short-travel backlit buttons + 2 thumbwheels + 2 joysticks","10 RGB LED beads (16.7M colors)","Open-ecosystem support — works on third-party bases","MOZA Pit House customizable"],cons:["MOZA Universal Hub Kit required for SC2 (~$50–100)","No SimHub — MOZA Pit House only","Niche — only relevant for ETS2/ATS truck simulation","400mm too large for road racing rigs"],buy:"https://us.mozaracing.com/products/tsw-truck-wheel",notes:"Specialty truck sim wheel for Euro/American Truck Simulator. With Hub Kit attaches to SC2 — one of the few real options for serious ETS2 setups."},
{id:109,brand:"MOZA",model:"TSW Truck Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"MOZA Universal Hub Kit",dia:"400mm",shape:"4-spoke Truck",inputs:18,display:false,simhub:false,bt:false,price:"$229",pros:["400mm truck sim specific","Aerospace aluminum + microfiber leather","Open ecosystem","Best truck sim wheel available"],cons:["Truck-sim niche only","No SimHub"],buy:"https://us.mozaracing.com/products/tsw-truck-wheel",notes:"Only purpose-built truck sim wheel on the market."},
```

#### Lamborghini Revuelto

```js
{id:110,brand:"MOZA",model:"Lamborghini Revuelto Sim Wheel (via Universal Hub Kit)",section:"sc2",subcat:"MOZA (via Universal Hub Kit)",conn:"blue",adapter:"MOZA Universal Hub Kit",dia:"340mm",shape:"GT Licensed Replica (Revuelto road-car CAD)",inputs:34,display:false,simhub:false,bt:false,price:"$399",pros:["Officially licensed from original Lamborghini Revuelto CAD data","340mm — largest GT replica diameter in MOZA range","Die-cast aluminum frame + hand-stitched microfiber leather","34 programmable inputs (16 front + 10 rear + encoders + paddles)","Carbon fiber dual-clutch magnetic Hall paddles","Button lifecycle exceeds 300,000 cycles","Compatible with all MOZA bases + 3rd-party via universal hub"],cons:["MOZA Universal Hub Kit required for SC2 (~$50–100)","No SimHub — MOZA Pit House only","No display — only the more expensive Essenza/Mission R have screens","Road-car replica feel — not a race-car replica"],buy:"https://us.mozaracing.com/products/revuelto-sim-wheel",notes:"Officially licensed Lamborghini Revuelto. 340mm GT replica at $399 — between Essenza SCV12 ($1,299) and CS V2P ($229). For Lambo road-car fans."},
{id:111,brand:"MOZA",model:"Lamborghini Revuelto Sim Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"MOZA Universal Hub Kit",dia:"340mm",shape:"GT Licensed Replica",inputs:34,display:false,simhub:false,bt:false,price:"$399",pros:["Official Lamborghini Revuelto license","340mm GT replica","34 inputs","Die-cast aluminum + microfiber leather"],cons:["No SimHub","No display","Universal Hub Kit needed for SC2"],buy:"https://us.mozaracing.com/products/revuelto-sim-wheel",notes:"See SC2 section."},
```

---

### Simagic — adapter:"Simagic MAGLINK"

NOTE: Existing entries 57, 58, 76 are stubs that lump multiple wheels into one card. Recommend retiring/replacing those with proper individual cards below. The "XGT Pro Round 320mm" referenced in id 57/76 does not actually exist as a SKU — closest match is **NEO X-330R Classic** (330mm round on NEO X Hub).

#### FX Pro Formula

```js
{id:112,brand:"Simagic",model:"FX Pro Formula Steering Wheel (via MAGLINK)",section:"sc2",subcat:"Simagic (via MAGLINK)",conn:"blue",adapter:"Simagic MAGLINK",dia:"290mm",shape:"Formula",inputs:30,display:true,simhub:true,bt:false,price:"$549 (sale, reg $759)",pros:["4.3\" sharp/vivid LCD telemetry display","12 RGB buttons + 4 thumb encoders + 5 rotary encoder buttons + 1 seven-way switch","6 paddles (2 shift + 2 custom + 2 dual-clutch) — modular","5mm carbon fiber plate, 1700g","SimPro Manager + SimHub fully supported","QR50 Simagic Quick Release","90mm depth — fits formula cockpit ergonomics"],cons:["Simagic MAGLINK adapter required for SC2 (~$50–70)","USB cable required for display data","Not native SC2 ecosystem","290mm compact formula only"],buy:"https://simagic.com/products/fx-pro",notes:"Top-tier Simagic formula wheel with 4.3\" display. Direct competitor to Asetek Forte Formula Pro and MOZA FSR2."},
{id:113,brand:"Simagic",model:"FX Pro Formula Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Simagic MAGLINK",dia:"290mm",shape:"Formula",inputs:30,display:true,simhub:true,bt:false,price:"$549",pros:["4.3\" LCD display","30 inputs incl. 5 rotaries + 6 paddles","SimHub native","5mm carbon plate"],cons:["MAGLINK adapter needed for SC2","290mm only"],buy:"https://simagic.com/products/fx-pro",notes:"See SC2 section."},
```

#### FX Formula

```js
{id:114,brand:"Simagic",model:"FX Formula Steering Wheel (via MAGLINK)",section:"sc2",subcat:"Simagic (via MAGLINK)",conn:"blue",adapter:"Simagic MAGLINK",dia:"290mm",shape:"Formula",inputs:20,display:false,simhub:true,bt:false,price:"$359",pros:["5mm carbon fiber plate, 1550g","12 customizable RGB buttons + 3 rotary encoders + 4 thumb encoders + 1 seven-way switch","Patented Hall paddle modules","Patented soft-glow LED rev lights (RGB adjustable)","SimPro Manager + SimHub","QR50 quick release","Strong value formula at $359"],cons:["No display (FX Pro has 4.3\" LCD)","Clutch paddles optional / sold separately","MAGLINK adapter needed for SC2 (~$50–70)","290mm compact only"],buy:"https://simagic.com/products/fx-formula",notes:"FX is the no-display version of FX Pro at ~$200 less. Solid mid-tier formula option."},
{id:115,brand:"Simagic",model:"FX Formula Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Simagic MAGLINK",dia:"290mm",shape:"Formula",inputs:20,display:false,simhub:true,bt:false,price:"$359",pros:["5mm carbon plate at $359","Hall paddle modules","SimHub LEDs","12 RGB buttons"],cons:["No display","MAGLINK needed for SC2"],buy:"https://simagic.com/products/fx-formula",notes:"See SC2 section."},
```

#### GT4 Steering Wheel

```js
{id:116,brand:"Simagic",model:"GT4 Steering Wheel (via MAGLINK)",section:"sc2",subcat:"Simagic (via MAGLINK)",conn:"blue",adapter:"Simagic MAGLINK",dia:"300mm",shape:"GT (Formula button layout)",inputs:14,display:false,simhub:true,bt:false,price:"$259 (sale, reg $499)",pros:["300mm GT at $259 sale price — excellent value","Carbon fiber + silicone grip — light at 1.3kg","12 RGB buttons + 2 seven-way multi-position switches","Patented Hall paddle modules","Integrated hub + QR50 quick release","SimHub compatible","Optional clutch paddles available"],cons:["Sale-priced — restocks may revert to $499","No display","MAGLINK adapter required for SC2 (~$50–70)","Less premium feel vs GTS leather"],buy:"https://simagic.com/products/gt4-formula",notes:"Heavily discounted GT-style wheel with formula button layout. Best Simagic budget pick at sale price."},
{id:117,brand:"Simagic",model:"GT4 Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Simagic MAGLINK",dia:"300mm",shape:"GT (Formula button layout)",inputs:14,display:false,simhub:true,bt:false,price:"$259",pros:["300mm GT at $259","Carbon fiber + silicone","12 RGB buttons","SimHub LEDs"],cons:["No display","MAGLINK needed for SC2"],buy:"https://simagic.com/products/gt4-formula",notes:"See SC2 section."},
```

#### GT1 Steering Wheel

```js
{id:118,brand:"Simagic",model:"GT1 Steering Wheel (via MAGLINK)",section:"sc2",subcat:"Simagic (via MAGLINK)",conn:"blue",adapter:"Simagic MAGLINK",dia:"330mm",shape:"D-shaped or Round (CNC aluminum + suede)",inputs:8,display:false,simhub:true,bt:false,price:"$309",pros:["330mm — meets 315mm+ oval spec ✓","Choice of D-shape OR Round rim","CNC aluminum alloy rim with genuine suede grips","4-segment Rev Light","Patented Hall paddle modules","Wireless data transfer to Simagic bases","Compatible with drift / rally / track","SimPro Manager + SimHub"],cons:["Only 4 buttons + 2 encoders + 3-speed shifter — limited input count","Heavy at 1.95kg","MAGLINK adapter required for SC2 (~$50–70)","Optional clutch paddles only"],buy:"https://simagic.com/products/gt1",notes:"330mm round option could fit oval-tab criteria. Budget round Simagic with suede grips. Verify dish on round variant."},
{id:119,brand:"Simagic",model:"GT1 Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Simagic MAGLINK",dia:"330mm",shape:"D-shaped / Round CNC aluminum + suede",inputs:8,display:false,simhub:true,bt:false,price:"$309",pros:["330mm with round option","CNC aluminum + suede","Hall paddle modules","Wireless to Simagic bases"],cons:["Limited inputs (8)","1.95kg heavy","MAGLINK needed for SC2"],buy:"https://simagic.com/products/gt1",notes:"See SC2 section. Round 330mm variant is candidate for oval tab pending dish verification."},
```

#### GTS Steering Wheel

```js
{id:120,brand:"Simagic",model:"GTS Steering Wheel (via MAGLINK)",section:"sc2",subcat:"Simagic (via MAGLINK)",conn:"blue",adapter:"Simagic MAGLINK",dia:"300mm",shape:"Round (leather/suede)",inputs:11,display:false,simhub:true,bt:false,price:"$289",pros:["300mm round at $289","Lightweight magnesium-aluminum (1.45kg)","7 customizable RGB buttons + 2 seven-way switches + 2 rotary encoder buttons","Hall paddle module with adjustable paddles","9 LEDs customizable RPM gauge","Leather or suede grip options","Compatible across rally/track/drift/formula/truck","128 customizable button cap stickers","QR50 quick release"],cons:["Limited input count vs FX series","No display","MAGLINK adapter required for SC2 (~$50–70)"],buy:"https://simagic.com/products/gts",notes:"Versatile 300mm round leather/suede wheel. Light at 1.45kg."},
{id:121,brand:"Simagic",model:"GTS Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Simagic MAGLINK",dia:"300mm",shape:"Round leather/suede",inputs:11,display:false,simhub:true,bt:false,price:"$289",pros:["300mm round","1.45kg lightweight","9 RPM LEDs","Multi-discipline"],cons:["No display","MAGLINK needed for SC2"],buy:"https://simagic.com/products/gts",notes:"See SC2 section."},
```

#### GT Neo

```js
{id:122,brand:"Simagic",model:"GT Neo Steering Wheel (via MAGLINK)",section:"sc2",subcat:"Simagic (via MAGLINK)",conn:"blue",adapter:"Simagic MAGLINK",dia:"~300mm",shape:"GT Round (Neo Series)",inputs:14,display:false,simhub:true,bt:false,price:"$269 (sale, reg $289)",pros:["Magnetic-link wireless connection to Simagic bases","Carbon fiber + 500g trigger buttons","Compatible with Simagic Alpha Mini / Alpha EVO bases","SimHub support","Highly rated (85% positive reviews on Simagic store)","Affordable entry to NEO ecosystem"],cons:["Specific button count not published on store page","MAGLINK adapter required for SC2 (~$50–70)","No display"],buy:"https://simagic.com/products/gt-neo",notes:"Entry NEO Series wheel. Confirm exact input count before final spec — store page light on details."},
{id:123,brand:"Simagic",model:"GT Neo Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Simagic MAGLINK",dia:"~300mm",shape:"GT Round Neo Series",inputs:14,display:false,simhub:true,bt:false,price:"$269",pros:["Carbon fiber Neo Series","Magnetic-link wireless","SimHub","85% positive reviews"],cons:["Limited published specs","MAGLINK needed for SC2"],buy:"https://simagic.com/products/gt-neo",notes:"See SC2 section."},
```

#### NEO X-310G GT (on NEO X Hub)

```js
{id:124,brand:"Simagic",model:"NEO X-310G GT Steering Wheel (via MAGLINK)",section:"sc2",subcat:"Simagic NEO X (via MAGLINK)",conn:"blue",adapter:"Simagic MAGLINK",dia:"310mm",shape:"GT (CNC aluminum + synthetic leather)",inputs:34,display:false,simhub:true,bt:false,price:"$309",pros:["310mm GT round","One-piece CNC aluminum frame — strong + lightweight","Black synthetic leather + orange contrast stitching","8 RGB buttons + 2 thumb encoders + 2 seven-way switches + 12 LED encoders + 9 RGB rev lights = 34 inputs","4 modular paddle shifters — fully adjustable","Wireless 2.4GHz or USB","QR50 + QR70 (6×70mm) compatibility","SimPro Manager + SimHub","Carbon fiber composite NEO X Hub Core"],cons:["MAGLINK adapter required for SC2 (~$50–70)","No display","Synthetic leather not premium-grain"],buy:"https://simagic.com/products/simagic-neo-x-series-steering-wheels",notes:"NEO X-310G is the GT-style configuration of the NEO X Hub. 70mm PCD compatible — direct mount once on Simagic ecosystem."},
{id:125,brand:"Simagic",model:"NEO X-310G GT Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Simagic MAGLINK",dia:"310mm",shape:"GT CNC aluminum",inputs:34,display:false,simhub:true,bt:false,price:"$309",pros:["310mm GT one-piece CNC","34 inputs incl. 12 LED encoders","9 RGB rev lights","2.4GHz wireless or USB"],cons:["No display","MAGLINK needed for SC2"],buy:"https://simagic.com/products/simagic-neo-x-series-steering-wheels",notes:"See SC2 section."},
```

#### NEO X-330R Classic Round (replaces id 57/76 stub)

```js
{id:126,brand:"Simagic",model:"NEO X-330R Classic Round Steering Wheel (via MAGLINK)",section:"sc2",subcat:"Simagic NEO X (via MAGLINK)",conn:"blue",adapter:"Simagic MAGLINK",dia:"330mm",shape:"ROUND (CNC aluminum + leather)",inputs:34,display:false,simhub:true,bt:false,price:"$309",pros:["330mm ROUND — meets 315mm+ oval spec ✓","Semi-stitched red leather grip ring","5mm carbon fiber + CNC aluminum + leather/microsuede","8 RGB buttons + 2 thumb encoders + 2 seven-way switches + 12 LED encoders + 9 RGB rev lights","Dual-clutch paddles included for race starts","MAGLINK hub supports wide DD base compatibility","QR50/QR70 (50mm + 70mm bolt patterns)","SimPro Manager + SimHub","Wireless power + data transmission"],cons:["MAGLINK adapter required for SC2 (~$50–70)","No display","Synthetic/microsuede grip — not premium leather"],buy:"https://simagic.com/products/simagic-neo-x-series-steering-wheels",notes:"330mm round on NEO X Hub. Strong oval-tab candidate (replaces id 57/76 generic 'XGT Pro Round' stub which never existed as a SKU)."},
{id:127,brand:"Simagic",model:"NEO X-330R Classic Round Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Simagic MAGLINK",dia:"330mm",shape:"ROUND CNC aluminum + leather",inputs:34,display:false,simhub:true,bt:false,price:"$309",pros:["330mm round","Dual-clutch paddles","QR50/QR70","SimHub LEDs"],cons:["No display","MAGLINK needed for SC2"],buy:"https://simagic.com/products/simagic-neo-x-series-steering-wheels",notes:"See SC2 section."},
// Also ADD to oval section (replaces id 76):
{id:128,brand:"Simagic",model:"NEO X-330R Classic Round (via MAGLINK)",section:"oval",subcat:"Oval 315mm+ Round Wheels",conn:"blue",adapter:"Simagic MAGLINK",dia:"330mm",shape:"ROUND CNC aluminum + leather",inputs:34,display:false,simhub:true,bt:false,price:"$309",pros:["330mm ROUND — meets spec ✓","One-piece CNC aluminum","Dual-clutch paddles for race starts","9 RGB rev lights + 12 LED encoders","QR50/QR70 — direct SQR mount via 70mm","Modular: NEO X Hub swaps to GT/Rally/Drift rims"],cons:["MAGLINK adapter needed for SC2","No display","Verify dish on round variant"],buy:"https://simagic.com/products/simagic-neo-x-series-steering-wheels",notes:"Strongest Simagic oval candidate. Replaces the previously vague id 76 'NEO X Hub + XGT Pro Round' (XGT Pro is not an actual SKU)."},
```

#### NEO X-330T Rally

```js
{id:129,brand:"Simagic",model:"NEO X-330T Rally Steering Wheel (via MAGLINK)",section:"sc2",subcat:"Simagic NEO X (via MAGLINK)",conn:"blue",adapter:"Simagic MAGLINK",dia:"330mm",shape:"Round (Rally — synthetic leather)",inputs:34,display:false,simhub:true,bt:false,price:"$309",pros:["330mm round built for rally + GT versatility","Rigid one-piece CNC aluminum frame","Black synthetic leather + orange contrast stitching","Ultra-short travel actuation, 500g trigger weight","34 inputs (8 RGB + 2 thumb encoders + 2 seven-ways + 12 LED encoders + 9 RGB rev)","NEO X Hub modular ecosystem","SimPro + SimHub"],cons:["MAGLINK adapter required for SC2 (~$50–70)","No display","Synthetic leather grip"],buy:"https://simagic.com/products/simagic-neo-x-series-steering-wheels",notes:"330mm rally configuration on NEO X Hub. Same hub as 310G/330R/350W — different rim+button-box combo."},
{id:130,brand:"Simagic",model:"NEO X-330T Rally Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Simagic MAGLINK",dia:"330mm",shape:"Round Rally synthetic leather",inputs:34,display:false,simhub:true,bt:false,price:"$309",pros:["330mm rally round","One-piece CNC","500g trigger weight","12 LED encoders"],cons:["No display","MAGLINK needed for SC2"],buy:"https://simagic.com/products/simagic-neo-x-series-steering-wheels",notes:"See SC2 section."},
```

#### NEO X-350W Drift

```js
{id:131,brand:"Simagic",model:"NEO X-350W Drift Steering Wheel (via MAGLINK)",section:"sc2",subcat:"Simagic NEO X (via MAGLINK)",conn:"blue",adapter:"Simagic MAGLINK",dia:"350mm",shape:"Round (Drift — perforated synthetic leather)",inputs:34,display:false,simhub:true,bt:false,price:"$309",pros:["350mm — largest Simagic round wheel for drift","Optimized for drift control + fluid steering inputs","Perforated synthetic leather for grip during transitions","Angled 3 + 9 o'clock sections for wrist support","Includes drift-spec spacer","34 inputs on NEO X Hub","SimPro + SimHub"],cons:["MAGLINK adapter required for SC2 (~$50–70)","No display","350mm may feel oversized for road racing"],buy:"https://simagic.com/products/simagic-neo-x-series-steering-wheels",notes:"350mm drift-spec round. Largest Simagic wheel — perfect for drift but oversized for circuit racing. Could be considered for oval if dish is shallow."},
{id:132,brand:"Simagic",model:"NEO X-350W Drift Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Simagic MAGLINK",dia:"350mm",shape:"Round Drift perforated",inputs:34,display:false,simhub:true,bt:false,price:"$309",pros:["350mm drift round","Perforated synthetic leather","Drift-spec spacer included","NEO X Hub modular"],cons:["No display","MAGLINK needed for SC2","Large for circuit racing"],buy:"https://simagic.com/products/simagic-neo-x-series-steering-wheels",notes:"See SC2 section."},
```

---

### Asetek SimSports — adapter:"Asetek QR Adapter"

#### La Prima GT (Comfort+ Round Rim)

```js
{id:133,brand:"Asetek SimSports",model:"La Prima GT Wheel (Comfort+ Round Rim) — via adapter",section:"sc2",subcat:"Asetek SimSports (via QR Adapter)",conn:"blue",adapter:"Asetek QR Adapter",dia:"330mm",shape:"ROUND (Comfort+ recycled-fiber)",inputs:84,display:false,simhub:true,bt:false,price:"$595–$650 (button box $325 + Comfort+ rim $134.99 + shipping)",pros:["330mm Round — meets 315mm+ oval spec ✓","La Prima GT Button Box: 84 individual input options","Round Comfort+ Rim: handcrafted, 37% recycled fibers","Permanently fire resistant + antistatic + highly durable","Ergonomic across GT, road, rally, drift","Asetek QR removable — also works with 70mm PCD direct","SimHub fully supported","Asetek build quality at La Prima entry pricing"],cons:["Asetek QR adapter needed for SC2 (~$50–70) OR use 70mm direct","Button box + rim sold separately — totals add up","No display","Base La Prima Button Box is GT-only layout"],buy:"https://www.asetek.com/simsports/product/la-prima-gt-steering-wheel-black/",notes:"330mm round Asetek — strongest oval-tab Asetek candidate. Comfort+ recycled-fiber rim is the Round option (340mm Dished Suede also available for rally/drift)."},
{id:134,brand:"Asetek SimSports",model:"La Prima GT Wheel (Comfort+ Round)",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Asetek QR Adapter",dia:"330mm",shape:"ROUND Comfort+ recycled fiber",inputs:84,display:false,simhub:true,bt:false,price:"$595–$650",pros:["330mm Round Comfort+","84 inputs","SimHub","Modular button box + rim"],cons:["Asetek QR or 70mm needed","Button box + rim sold separately"],buy:"https://www.asetek.com/simsports/product/la-prima-gt-steering-wheel-black/",notes:"See SC2 section. Also strong oval candidate."},
{id:135,brand:"Asetek SimSports",model:"La Prima GT (Comfort+ 330mm Round)",section:"oval",subcat:"Oval 315mm+ Round Wheels",conn:"blue",adapter:"Asetek QR Adapter",dia:"330mm",shape:"ROUND Comfort+ (recycled-fiber, fire+antistatic resistant)",inputs:84,display:false,simhub:true,bt:false,price:"$595–$650 (button box + rim)",pros:["330mm Round — meets spec ✓","Comfort+ ergonomic round, designed for GT/road/rally/drift","84 inputs (largest input count among oval-tab options)","SimHub fully supported","Asetek QR removable — also works on 70mm SQR direct","Recycled-fiber sustainable build"],cons:["Asetek QR adapter or 70mm needed for SC2","Button box + rim sold separately","No display","Higher cost than NEO X-330R for similar diameter"],buy:"https://www.asetek.com/simsports/product/la-prima-gt-steering-wheel-black/",notes:"Premium 330mm round Asetek with most inputs in oval tab. Worth the extra $$ over Simagic NEO X-330R if you want SimHub + Asetek build."},
```

#### Forte Formula (no display)

```js
{id:136,brand:"Asetek SimSports",model:"Forte Formula Steering Wheel — via adapter",section:"sc2",subcat:"Asetek SimSports (via QR Adapter)",conn:"blue",adapter:"Asetek QR Adapter",dia:"~290mm",shape:"Formula",inputs:128,display:false,simhub:true,bt:false,price:"$529 (sale, reg $599)",pros:["128 individual input options — more than Forte Pro standard","12 push buttons + 2 two-way toggles + 2 seven-way kinky switches + 3 rotary encoders + 6 thumb encoders","49 fully customizable ARGB LEDs (rev + flag)","Injection-molded carbon-fiber-reinforced composite chassis with laser-etched forged carbon","2 contactless magnetic shifter paddles","Asetek RaceHub + SimHub fully supported","Asetek QR included — also fits 70mm SQR direct"],cons:["NO display (use Forte Formula Pro for 4.3\" LCD)","Asetek QR adapter needed for SC2 (~$50–70) or 70mm direct","Composite chassis less premium than Invicta aluminum","Toggle switches feel exposed"],buy:"https://www.asetek.com/simsports/product/forte-formula-steering-wheel/",notes:"Forte Formula (no display) at $529. Mid-tier between La Prima Formula ($249–$422) and Forte Formula Pro ($649)."},
{id:137,brand:"Asetek SimSports",model:"Forte Formula Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Asetek QR Adapter",dia:"~290mm",shape:"Formula",inputs:128,display:false,simhub:true,bt:false,price:"$529",pros:["128 inputs","49 ARGB LEDs","SimHub + RaceHub","Forged-carbon laser-etched chassis"],cons:["No display","Asetek QR or 70mm needed for SC2"],buy:"https://www.asetek.com/simsports/product/forte-formula-steering-wheel/",notes:"See SC2 section."},
```

#### Forte Formula Pro (replaces stub id 59)

```js
{id:138,brand:"Asetek SimSports",model:"Forte Formula Pro Steering Wheel — via adapter",section:"sc2",subcat:"Asetek SimSports (via QR Adapter)",conn:"blue",adapter:"Asetek QR Adapter",dia:"~290mm",shape:"Formula",inputs:142,display:true,simhub:true,bt:false,price:"$649",pros:["4.3\" 800×480 60Hz LCD touch with RaceView technology","142 aluminum control inputs (10 buttons + 6 thumb encoders + 3 rotary + 2 kinky + 2 rocker + paddles)","31 addressable RGB LEDs (rev + flag)","Glass-fiber-reinforced lightweight + rigid chassis (1160g)","Asetek RaceHub — cleanest tuning suite + SimHub support","Asetek QR included — fits 70mm SQR direct","Best value display formula wheel at $649"],cons:["Asetek QR adapter needed for SC2 (~$50–70) or 70mm direct","Composite plastic shell looks less premium than Invicta aluminum","Internal USB-C only — no external USB port for 3rd-party gear","Toggle switches vulnerable due to protruding position"],buy:"https://www.asetek.com/simsports/us/product/forte-formula-pro-steering-wheel/",notes:"REPLACES id 59 stub with proper card. 4.3\" LCD + 142 inputs at $649 — strong competition for MOZA FSR2 + Simagic FX Pro."},
{id:139,brand:"Asetek SimSports",model:"Forte Formula Pro Steering Wheel",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Asetek QR Adapter",dia:"~290mm",shape:"Formula",inputs:142,display:true,simhub:true,bt:false,price:"$649",pros:["4.3\" 800×480 60Hz touch LCD","142 inputs","RaceView + SimHub","Glass-fiber-reinforced 1160g"],cons:["Composite shell","No external USB","Asetek QR or 70mm needed for SC2"],buy:"https://www.asetek.com/simsports/us/product/forte-formula-pro-steering-wheel/",notes:"See SC2 section. Replaces older id 59 stub."},
```

#### Initium PC Steering Wheel

```js
{id:140,brand:"Asetek SimSports",model:"Initium Steering Wheel (PC) — via adapter",section:"sc2",subcat:"Asetek SimSports (via QR Adapter)",conn:"blue",adapter:"Asetek QR Adapter",dia:"300mm",shape:"Round (texturized rim, perforated grips)",inputs:21,display:false,simhub:true,bt:false,price:"$149",pros:["Cheapest Asetek wheel at $149","300mm round — entry to Asetek round ecosystem","21 programmable inputs (11 push + 4-way D-pad + 2 rotary + 2 magnetic shifters + start/stop)","9 customizable aRGB rev LEDs + 4 backlit aRGB buttons","Texturized round rim with perforated grips","Automotive-grade injection-molded plastic housing","Integrated quick release — cable-free","SimHub supported"],cons:["Asetek QR adapter needed for SC2 (~$50–70)","Plastic housing — not premium build vs La Prima/Forte","Limited inputs (21) vs higher-tier Asetek","No display","Bundled mostly with Initium starter bundles"],buy:"https://www.asetek.com/simsports/product/initium-steering-wheel-pc/",notes:"Asetek's entry-level $149 wheel. Came with Initium DD bundle. With QR adapter the cheapest Asetek path to SC2."},
{id:141,brand:"Asetek SimSports",model:"Initium Steering Wheel (PC)",section:"usb",subcat:"USB Rims",conn:"blue",adapter:"Asetek QR Adapter",dia:"300mm",shape:"Round texturized + perforated grip",inputs:21,display:false,simhub:true,bt:false,price:"$149",pros:["$149 — cheapest Asetek wheel","300mm round","21 inputs + 9 RGB rev LEDs","Integrated QR cable-free"],cons:["Plastic housing","Asetek QR or 70mm needed for SC2","Limited inputs"],buy:"https://www.asetek.com/simsports/product/initium-steering-wheel-pc/",notes:"See SC2 section. Asetek entry point."},
```

---

## Existing entries that should gain `adapter` field

| ID  | Brand    | Adapter to add                  | Notes |
|-----|----------|---------------------------------|-------|
| 57  | Simagic  | `adapter:"Simagic MAGLINK"`     | Stub — recommend deprecating in favor of new id 124–132 individual NEO X cards |
| 58  | Simagic  | `adapter:"Simagic MAGLINK"`     | Stub — replaced by new individual GT Neo / FX / FX Pro cards (id 112–123) |
| 59  | Asetek   | `adapter:"Asetek QR Adapter"`   | Stub — replaced by new id 138/139 Forte Formula Pro proper cards |
| 76  | Simagic  | `adapter:"Simagic MAGLINK"`     | Oval-section dup of 57 — replace with new id 128 (proper NEO X-330R) |
| 80  | MOZA     | `adapter:"MOZA Universal Hub Kit"` | KS Wheel |
| 81  | MOZA     | `adapter:"MOZA Universal Hub Kit"` | GS V2P GT |
| 82  | MOZA     | `adapter:"MOZA Universal Hub Kit"` | FSR2 Formula |
| 83  | MOZA     | `adapter:"MOZA Universal Hub Kit"` | Vision GS |
| 84  | MOZA     | `adapter:"MOZA Universal Hub Kit"` | KS Pro |
| 85  | MOZA     | `adapter:"MOZA Universal Hub Kit"` | CS Pro 325mm |
| 86  | MOZA     | `adapter:"MOZA Universal Hub Kit"` | Porsche Mission R |
| 87  | MOZA     | `adapter:"MOZA Universal Hub Kit"` | Lamborghini Essenza SCV12 |
| 88  | Asetek   | `adapter:"Asetek QR Adapter"`   | La Prima Formula |
| 89  | Asetek   | `adapter:"Asetek QR Adapter"`   | Invicta Formula (Button Box) — Invicta also supports 70mm direct, but adapter is canonical |
| 95  | MOZA     | `adapter:"MOZA Universal Hub Kit"` | KS Pro USB-section dup |
| 96  | Asetek   | `adapter:"Asetek QR Adapter"`   | Invicta USB-section dup |
| 101 | MOZA     | `adapter:"MOZA Universal Hub Kit"` | CS Pro 325mm Round oval-section dup |

---

## Notes

### Simagic stubs (id 57, 58, 76) need cleanup
- The model "XGT Pro Round" referenced in id 57/76 does **not** exist as a Simagic SKU. The closest match is the **NEO X-330R Classic** (330mm round on NEO X Hub). I've created proper NEO X-330R cards (id 126/127/128) to replace these stubs.
- id 58 ("GT NEO / FX / FX Pro") combines three distinct wheels into one card. New individual cards: GT Neo (id 122/123), FX Formula (id 114/115), FX Pro (id 112/113).
- Recommend retiring id 57/58/76 once new cards are added, or keeping them with `// DEPRECATED` comment and adding `adapter` field for backward compatibility.

### Asetek id 59 stub
- "Forte Formula Pro (Display wheel)" id 59 spec has wrong price ($499–$549) — actual price is **$649 USD**. Spec says 16 inputs but the actual count is **142**. Stub should be replaced by new id 138/139.

### MOZA notes
- All 5 missing MOZA wheels confirmed live on us.mozaracing.com (CS V2P shows "Sold Out" but page exists).
- Pricing on CAD-only mozaracing.com vs USD on us.mozaracing.com — used USD throughout.
- TSW Truck Wheel is a niche pick (truck sim only) but worth including given 400mm + truck-specific layout is unique in the market.

### Asetek notes
- Asetek La Prima GT Wheel (Comfort+ Round) is a **strong new oval-tab candidate** at 330mm — added to oval section as id 135.
- Asetek Initium is the cheapest path into Asetek ecosystem at $149.
- Asetek Invicta has 70mm PCD direct support — id 89/96 could note this in addition to the adapter requirement.
- Two URLs returned 403 (Forte product pages on asetek.com from this Pi's IP). Used third-party retailer 6sigmasimracing.com as confirmation source for prices/specs. URLs in cards are still the canonical asetek.com URLs.

### Simagic notes
- The Simagic GT Pro Hub ($339) is listed on the brand site but is a **hub-only product** that takes external rims (P-330R, P-330D, P-325D, P-325C). Not added as a wheel card — could be a separate "hub" entry if guide adds a hub category.
- Simagic GT1 Round 330mm variant could theoretically fit the oval tab — flagged in card notes pending dish verification.
- The NEO X Hub's wireless power+data via MAGLINK is well-documented; the Simagic ecosystem is one of the most refined among the three brands.

### Pricing sanity check
All prices are USD as of April 2026, sourced from brand official US sites (simagic.com, us.mozaracing.com, asetek.com) or 6sigmasimracing.com when 403'd.

### URL verification status
- All 5 new MOZA URLs verified live (200 OK) on us.mozaracing.com
- All Simagic product page URLs verified live on simagic.com
- Asetek URLs derived from search results — direct WebFetch returned 403 from Pi's IP, but URLs are confirmed by 6sigmasimracing.com cross-reference and search-result snippets

### ID range used
New regular IDs span **102–141** (40 new cards = 5 MOZA + 11 Simagic + 4 Asetek wheels, each duplicated across SC2/USB sections, plus 3 oval-section additions).
