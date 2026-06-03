# Missing Sim Racing Wheels Research — 2026-04-25

## Summary

- Brands surveyed: 25
- New candidates identified: 23
- Brands fully covered (no additions found): SRC (SimRacingCoach), VRS, VNM Simulation, GRID/Sim-Lab, SimRacingBay (their own SRB lineup; existing entries cover all confirmed retail SKUs), Cosworth, Heusinkveld One (already in catalog)
- Brands with no current production own-brand standalone USB wheels: SimXperience (only AccuForce-bound rims), Frex (only passive 330/340mm round rims and the existing Type-C V2), Wink Racing (no online presence located), Pro Course Motorsports / Acces Italia (not located as standalone-wheel makers), Ricmotech RST (not own-brand), Simjack (pedals only)
- iSpeedy/Speedmaster: no DD-class own-brand wheel surfaced

## New entries (paste-ready JS objects)

### Cube Controls

```js
{id:?, brand:"Cube Controls", model:"F-PRO Color Edition", section:"sim", subcat:"Formula",
 conn:"mixed", dia:"282mm", shape:"formula closed",
 inputs:32, display:false, simhub:true, bt:true, lights:false,
 price:"€905",
 pros:["12 RGB-backlit buttons","2 toggles with status LEDs","Magnetic switchless paddles + clutch","USB or Bluetooth wireless"],
 cons:["No display","Battery life depends on LED brightness"],
 buy:"https://www.cubecontrols.com/product/f-pro-color-edition/",
 notes:"2025 colour-edition refresh of the F-Pro with red/blue/black thumb encoders, knobs, and grip materials, retaining the magnetic Q-Conn cable and SimHub support."}
```

```js
{id:?, brand:"Cube Controls", model:"CSX-3 Color Edition", section:"sim", subcat:"Formula",
 conn:"mixed", dia:"282mm", shape:"formula closed",
 inputs:38, display:true, simhub:true, bt:true, lights:false,
 price:"€1629",
 pros:["4-inch 800x480 touchscreen","17 RGB LED buttons + 12 momentary","4 or 6 magnetic switchless paddles","Carbon fibre + die-cast aluminium build"],
 cons:["High price","Heavier 1143g for a Formula wheel"],
 buy:"https://www.cubecontrols.com/product/csx-3-color-edition/",
 notes:"Color-edition variant of the CSX-3 in black, red, or blue with the same touchscreen, native SimHub plugin, and Q-Conn magnetic cable connection."}
```

```js
{id:?, brand:"Cube Controls", model:"GT PRO V2 Sport", section:"sim", subcat:"GT",
 conn:"mixed", dia:"320mm", shape:"GT round",
 inputs:18, display:false, simhub:true, bt:true, lights:true,
 price:"€770",
 pros:["320mm round rim with carbon faceplate","USB Q-Conn or Bluetooth dual mode","Backlit buttons with telemetry LEDs","2 or 4 magnetic switchless paddle options"],
 cons:["Smaller 1500mAh battery (4 hours wireless)","Limited input count vs other GT variants"],
 buy:"https://www.cubecontrols.com/product/gt-pro-v2-sport/",
 notes:"Sport variant of the GT Pro V2 with a wireless-capable design and Q-Conn cable, sharing the family magnetic paddles and SimHub plugin."}
```

```js
{id:?, brand:"Cube Controls", model:"GT PRO V2 Zero", section:"sim", subcat:"GT",
 conn:"mixed", dia:"298mm", shape:"GT flat-top flat-bottom",
 inputs:18, display:false, simhub:true, bt:true, lights:true,
 price:"$940",
 pros:["298mm flat-top flat-bottom rim","R-Spec aluminium machined shifters","USB Q-Conn or Bluetooth","Backlit buttons + telemetry LEDs"],
 cons:["1500mAh battery limits wireless to ~4 hours","Aggressive shape not for all drivers"],
 buy:"https://www.cubecontrols.com/product/gt-pro-v2-zero/",
 notes:"Flat-top flat-bottom GT Pro V2 variant aimed at high-precision driving with the same button-box and Q-Conn dual-mode connectivity."}
```

```js
{id:?, brand:"Cube Controls", model:"GT PRO V2 Cube", section:"sim", subcat:"GT",
 conn:"mixed", dia:"320mm", shape:"GT round",
 inputs:18, display:false, simhub:true, bt:true, lights:true,
 price:"$899",
 pros:["GT-Cube Pro Rim with comfort grip","USB Q-Conn or Bluetooth","Magnetic switchless paddles","Backlit buttons + telemetry LEDs"],
 cons:["1500mAh battery 4 hours wireless","No display"],
 buy:"https://www.cubecontrols.com/product/gt-pro-v2-cube/",
 notes:"GT Pro V2 fitted with the GT-Cube Pro Rim, sharing the GT Pro V2 button box electronics and dual USB-C/Bluetooth connection."}
```

```js
{id:?, brand:"Cube Controls", model:"GT PRO V2 Reparto Corse Suede", section:"sim", subcat:"GT",
 conn:"mixed", dia:"300-320mm", shape:"GT flat-bottom",
 inputs:18, display:false, simhub:true, bt:true, lights:true,
 price:"$987",
 pros:["Reparto Corse suede grip","R-Spec machined aluminium shifters","USB Q-Conn or Bluetooth","Up to 40 hours battery life cited"],
 cons:["High price for screenless wheel","Suede wears with sweat"],
 buy:"https://www.cubecontrols.com/product/gt-pro-v2-reparto-corse-suede/",
 notes:"Flat-bottom Reparto Corse rim option for the GT Pro V2 with suede wrapping, dual-mode USB-C and Bluetooth, and SimHub plugin support."}
```

```js
{id:?, brand:"Cube Controls", model:"GT Sport (USB)", section:"sim", subcat:"GT",
 conn:"orange", dia:"290 or 320mm", shape:"GT round",
 inputs:10, display:false, simhub:true, bt:false, lights:false,
 price:"$799 CAD",
 pros:["100% carbon fibre face plate","Genuine suede leather grip","Magnetic adjustable paddle shifters","Accepts aftermarket racing wheels via 6x70mm"],
 cons:["No display, no rev LEDs","Limited input count"],
 buy:"https://pitlanesimracing.com/products/cube-controls-gt-sport-steering-wheel-usb",
 notes:"Wired entry GT wheel with carbon front plate, magnetic paddles, suede grip, and a 6x70mm bolt pattern accepting third-party rims."}
```

```js
{id:?, brand:"Cube Controls", model:"GT Sport (Wireless)", section:"sim", subcat:"GT",
 conn:"mixed", dia:"290 or 320mm", shape:"GT round",
 inputs:14, display:false, simhub:true, bt:true, lights:false,
 price:"€?",
 pros:["USB or Bluetooth dual mode","1500mAh LiPo, up to 40 hours","Carbon fibre face plate","6 backlit buttons + 2 toggles + 4 encoders + 2 joysticks"],
 cons:["No display","Smaller battery vs Reparto Corse"],
 buy:"https://www.amazon.com/Cube-Controls-GT-Sport-Wireless/dp/B0DF5R4Y3L",
 notes:"Wireless-capable variant of the GT Sport with Bluetooth or USB connection and the same 290mm or 320mm rim option."}
```

### Ascher Racing

```js
{id:?, brand:"Ascher Racing", model:"YOUR Ultimate", section:"sim", subcat:"Formula",
 conn:"orange", dia:"300mm", shape:"formula closed",
 inputs:30, display:false, simhub:true, bt:false, lights:true,
 price:"€1699",
 pros:["Custom laser-etched logos","Choice of red, blue, gold or black thumb encoders, knobs, and rotaries","Inspired by McLaren Artura Ultimate","Closed-bottom design"],
 cons:["No screen","High starting price"],
 buy:"https://ascher-racing.com/int/news/post/news-ascher-racing-your-ultimate1",
 notes:"Customizable variant of the Ascher Ultimate launched March 2025 with personalized engraving and color options on the standard Ultimate hardware."}
```

### P1Sim

```js
{id:?, brand:"P1Sim", model:"Beau Rivage Pierre Gasly", section:"sim", subcat:"Formula",
 conn:"orange", dia:"295mm", shape:"formula closed-bottom",
 inputs:38, display:true, simhub:true, bt:false, lights:true,
 price:"€1399",
 pros:["4.3\" Vocore SimHub LCD","11 backlit buttons + 4 push encoders","4 magnetic shifter + 2 clutch paddles","Forged carbon plate and CNC aluminium body"],
 cons:["15 working days lead time","Limited Edition only"],
 buy:"https://p1sim.fr/products/beau-rivage-pierre-gasly-steering-wheel",
 notes:"Pierre Gasly limited-edition closed-bottom formula wheel with 4.3-inch SimHub display, magnetic paddles, 22 RGB LEDs, and forged carbon front plate."}
```

```js
{id:?, brand:"P1Sim", model:"Beau Rivage", section:"sim", subcat:"Formula",
 conn:"purple", adapter:"Simucube Link wireless", dia:"295mm", shape:"formula closed-bottom",
 inputs:38, display:true, simhub:true, bt:false, lights:true,
 price:"€1399",
 pros:["Simucube LightBridge wireless power and data","4.3\" SimHub display","Magnetic shifter + clutch paddles","Forged carbon front plate"],
 cons:["Requires Simucube 3 base","15 working days lead time"],
 buy:"https://p1sim.fr/products/beau-rivage-simucube-link",
 notes:"Closed-bottom formula wheel using Simucube Link Quick Release for brushless contactless power and data on Simucube 3 wheelbases."}
```

### Conspit

```js
{id:?, brand:"Conspit", model:"Max01", section:"sim", subcat:"Formula",
 conn:"orange", dia:"310mm", shape:"formula closed",
 inputs:32, display:true, simhub:true, bt:false, lights:true,
 price:"$850",
 pros:["4-inch SimHub touchscreen","10 backlit buttons + 4 thumb encoders + 4 rotaries","Magnetic carbon shifter + clutch paddles","Single-piece aluminium chassis with 5mm carbon plate"],
 cons:["Clutch paddles low resistance","Buttons feel plasticky"],
 buy:"https://us.passionsim.com/en/products/conspit-max01",
 notes:"Conspit's high-end formula-style wheel with multi-base USB QR adapters and SimHub-driven 4-inch dashboard."}
```

```js
{id:?, brand:"Conspit", model:"310 APEX", section:"sim", subcat:"GT",
 conn:"orange", dia:"310mm", shape:"GT round",
 inputs:104, display:true, simhub:true, bt:false, lights:true,
 price:"$349",
 pros:["2.99-inch LCD with 7 dash pages","Up to 104 configurable inputs","8 RGB illuminated buttons","Eco-friendly microfiber leather grip"],
 cons:["Lower input force may feel light","Mid-tier feel for the price tier"],
 buy:"https://us.passionsim.com/en/products/volant-gt-310-apex-conspit",
 notes:"GT-style wheel with a 2.99-inch display, 33 RGB LEDs, magnetic Hall-sensor paddles, and SimHub plus Conspit Link 2.0 software support."}
```

```js
{id:?, brand:"Conspit", model:"PW1 Formula", section:"sim", subcat:"Formula",
 conn:"orange", dia:"280mm", shape:"formula closed",
 inputs:42, display:true, simhub:true, bt:false, lights:true,
 price:"€1785",
 pros:["4.3-inch 800x480 60Hz display","6-paddle layout with dual-mode clutch","12-layer prepreg carbon construction","CDP 7075 aluminium quick release"],
 cons:["Limited to 500 units","Frequently out of stock"],
 buy:"https://thefrenchsimracer.com/en/products/conspit-pw1-formula-wheel",
 notes:"Limited-edition 280mm formula wheel with a 4.3-inch display, 6 paddles, dual-mode clutch system, and 12 buttons plus 6 encoders and 6 rotaries."}
```

```js
{id:?, brand:"Conspit", model:"H.AO HUB", section:"sim", subcat:"GT modular",
 conn:"orange", dia:"varies (rim-dependent)", shape:"hub + 295/320mm rim options",
 inputs:32, display:true, simhub:true, bt:false, lights:true,
 price:"€500",
 pros:["Carbon fibre hub with 2.99\" display","9 RPM LEDs + illuminated buttons","Modular pairing with RX320, DX320 or CX295 rims","70mm PCD hub accepts third-party rims"],
 cons:["Sold separately from rim","Frequently out of stock"],
 buy:"https://thefrenchsimracer.com/en/products/conspit-hao-hub",
 notes:"Modular carbon-fibre hub with onboard display and inputs that pairs with Conspit's RX320, DX320, or CX295 rims or any third-party 70mm PCD rim."}
```

### MOZA Racing

```js
{id:?, brand:"MOZA", model:"Porsche Mission R", section:"sim", subcat:"Formula/GT licensed",
 conn:"orange", dia:"320mm", shape:"closed-bottom",
 inputs:18, display:true, simhub:false, bt:false, lights:false,
 price:"€1399 / $1299",
 pros:["5.4\" curved 720P 60Hz OLED","Aerospace aluminium frame, faux suede grip","CNC aluminium magnetic shifter + dual clutch","All-aluminium MOZA universal QR"],
 cons:["MOZA Pit House software not SimHub","Initial stock often sold out"],
 buy:"https://mozaracing.com/pages/porsche-mission-r-wheel",
 notes:"Officially licensed Porsche Mission R replica with curved 5.4-inch OLED dashboard, 1.3GHz processor, and 10+ preset UI designs via MOZA Pit House."}
```

```js
{id:?, brand:"MOZA", model:"CS Pro", section:"sim", subcat:"GT",
 conn:"orange", dia:"?mm", shape:"GT3 round",
 inputs:?, display:true, simhub:false, bt:false, lights:true,
 price:"€349 / $329",
 pros:["2.99\" HD screen with MOZA Pit House dash","Microfiber leather GT3 grip","Optional 6-paddle layout","6x70mm bolt pattern third-party compatible"],
 cons:["Not native SimHub","Display limited to MOZA dashboards"],
 buy:"https://mozaracing.com/blogs/news/moza-racing-ces-2026-porsche-mission-r-wheel",
 notes:"CES 2026 GT3-style wheel with onboard 2.99-inch display, optional six-paddle expansion, and an industry-standard 6x70mm hub pattern."}
```

```js
{id:?, brand:"MOZA", model:"KS Pro (CES 2026)", section:"sim", subcat:"Formula",
 conn:"orange", dia:"?mm", shape:"butterfly formula",
 inputs:?, display:true, simhub:false, bt:false, lights:true,
 price:"€349 / $329",
 pros:["2.99\" HD screen","Eco-friendly TPE grip","4 RGB rotary switches + 10 RGB rev + 6 RGB flag lights","Next-gen dual-clutch paddle module"],
 cons:["Pit House dashboards only","Distinct from earlier KS / KS Pro models"],
 buy:"https://mozaracing.com/blogs/news/moza-racing-ces-2026-porsche-mission-r-wheel",
 notes:"CES 2026 update of the KS Pro with butterfly formula shape, 2.99-inch screen, RGB rev and flag lights, and dual-clutch paddles."}
```

### Soelpec

```js
{id:?, brand:"Soelpec", model:"Spectra LT", section:"sim", subcat:"Formula",
 conn:"orange", dia:"302mm", shape:"formula closed",
 inputs:32, display:false, simhub:true, bt:false, lights:true,
 price:"€1199",
 pros:["17 push buttons + 2 7-way switches","3 center encoders + 2 dual-action thumb encoders","Magnetic shifters and dual clutch with Hall sensors","6061 aluminium frame with carbon centre plate"],
 cons:["Screenless variant of Spectra XR","No Bluetooth"],
 buy:"https://soelpec.com/products/soelpec-spectra-lt",
 notes:"Screenless sister of the Spectra XR with the same 302mm chassis, magnetic paddles, and configurable RGB but no front display."}
```

```js
{id:?, brand:"Soelpec", model:"Terra LX", section:"sim", subcat:"Formula",
 conn:"orange", dia:"297mm", shape:"formula closed-bottom",
 inputs:32, display:false, simhub:true, bt:false, lights:true,
 price:"€879",
 pros:["13 push buttons + 2 7-way switches","4 HybridSwitch encoders, 2 dual-action thumb encoders","128 individually addressable RGB LEDs","DuoAct shifter/clutch with tactile + Hall sensors"],
 cons:["No display","No Bluetooth"],
 buy:"https://soelpec.com/products/soelpec-terra-lx",
 notes:"Soelpec's entry/mid formula-style wheel with HybridSwitch encoders, DuoAct shifters, and a closed-bottom design at a lower price than the Spectra range."}
```

### 3DRap

```js
{id:?, brand:"3DRap", model:"VOTA LTE Racing Wheel", section:"sim", subcat:"Formula",
 conn:"orange", dia:"290mm", shape:"formula closed",
 inputs:?, display:false, simhub:true, bt:false, lights:false,
 price:"€189+",
 pros:["Ultra-light 420g","5mm forged carbon monocoque","All major QR systems via 6x70mm adapter","Compatible with all major wheelbases"],
 cons:["Lightweight stripped-down feature set","Pricing scales with options"],
 buy:"https://sim.3drap.it/products/vota-lte-racing-wheel-all-wheelbases-pc",
 notes:"Lightweight 290mm formula wheel built around a 5mm forged carbon monocoque with USB connection and a 3-bolt formula hub plus optional 6x70mm adapter."}
```

### Rexing

```js
{id:?, brand:"Rexing", model:"Timun GT", section:"sim", subcat:"GT",
 conn:"orange", dia:"320mm", shape:"GT round",
 inputs:?, display:true, simhub:true, bt:false, lights:true,
 price:"€1340 (export) / €1675 (EU)",
 pros:["4.3\" USBD480 display","Full carbon fibre construction","Alcantara grips","11 RGB + 6 marshal LEDs"],
 cons:["Windows PC only","High EU price with VAT"],
 buy:"https://rexing.eu/product/rexing-gt-steering-wheel-timun/",
 notes:"Hand-laid full-carbon GT wheel from Croatia with 4.3-inch USBD480 display, Apem buttons, alcantara grips, and SimHub/SimDash/Z1 support."}
```

### BavarianSimTec

```js
{id:?, brand:"BavarianSimTec", model:"OmegaOne", section:"sim", subcat:"Formula",
 conn:"orange", dia:"?mm", shape:"formula closed",
 inputs:35, display:true, simhub:true, bt:false, lights:true,
 price:"€?",
 pros:["4\" VoCore display","15 rev LEDs + 6 marshal LEDs under acrylic glass","Aerospace aluminium monocoque + carbon plate","6 thumb rotaries + 12 buttons + 2 7-way"],
 cons:["Pricing varies by configuration","Weight from 1100g"],
 buy:"https://www.bavariansimtec.com/products/omegaone",
 notes:"Sister of the OmegaPro V2 sharing its monocoque and 4-inch VoCore display with a simplified switchgear and SimHub support."}
```

### Delta Sim Tech

```js
{id:?, brand:"Delta Sim Tech", model:"EVO:NS", section:"sim", subcat:"Formula",
 conn:"orange", adapter:"Asetek QR optional", dia:"300mm", shape:"formula closed",
 inputs:?, display:false, simhub:true, bt:false, lights:true,
 price:"£745",
 pros:["RPM bar instead of full display","Industrial magnetic shifters with 4mm carbon paddles","Dual Hall-sensor clutches (dual or independent)","60A silicone grips and SimHub LED integration"],
 cons:["No screen","4-6 week lead time"],
 buy:"https://www.deltasimtech.com/products/evo-ns",
 notes:"Screenless 300mm formula wheel with industrial magnetic paddles, dual Hall clutches, RaceWare firmware, and SimHub LED control."}
```

```js
{id:?, brand:"Delta Sim Tech", model:"EVO:XN", section:"sim", subcat:"Formula",
 conn:"orange", adapter:"Asetek QR optional", dia:"300mm", shape:"formula closed",
 inputs:38, display:false, simhub:true, bt:false, lights:true,
 price:"£1050",
 pros:["12 illuminated buttons + 4 thumb + 4 front encoders","2 7-way funkys + 4 magnetic + 2 analog paddles","12 RPM + 6 marshal LEDs","5mm forged carbon front face"],
 cons:["No display","Hand-assembled, up to 6-week delivery"],
 buy:"https://www.deltasimtech.com/products/evo-xn",
 notes:"Higher-input screenless variant of the EVO with 12 illuminated buttons, RaceWare firmware, and a high-voltage input ready for power injectors."}
```

### Precision Sim Engineering (PSE)

```js
{id:?, brand:"PSE", model:"ES-Pro", section:"sim", subcat:"Formula",
 conn:"orange", dia:"285mm", shape:"formula closed",
 inputs:109, display:false, simhub:true, bt:false, lights:true,
 price:"£780",
 pros:["10 RGB illuminated buttons + 4 12-position switches","Twin Swiss thumbwheels with 24 input pairs","109 mappable inputs (Select-X)","MK-4 snap shifters + optional clutch paddles"],
 cons:["No display","PC only"],
 buy:"https://www.precisionsimengineering.com/shop-online/es-pro-steering-wheel",
 notes:"Mid-tier 285mm formula wheel using PSE's Select-X architecture with 109 inputs, MK-4 shifters, and Daniel Newman Racing SimHub plugin support."}
```

### Conspit (rim-only — flag for Standalone Rims tab if appropriate)

The Conspit RX320, DX320, and CX295 are rim-only options sold to pair with the H.AO HUB. They are not standalone USB wheels and are likely better catalogued in the Standalone Rims tab if the H.AO HUB is added separately.

### Trak Racer (announced/Q4 2025; verify availability before adding)

Trak Racer announced own-brand FORMULA-PRO and GT-PRO wheels with TJC LED touchscreen displays plus a BWT Alpine F1 A525 1:1 replica wheel ($1999, pre-order with late June 2026 delivery). Direct product pages on trakracer.com return 404 at time of research, so these candidates should be re-verified before listing. The known A525 replica entry is:

```js
{id:?, brand:"Trak Racer", model:"BWT Alpine F1 A525 Replica", section:"sim", subcat:"Formula licensed",
 conn:"orange", dia:"?mm", shape:"formula closed",
 inputs:34, display:true, simhub:true, bt:false, lights:true,
 price:"$1999 (pre-order)",
 pros:["1:1 replica from Alpine CAD data","4.3\" 800x480 touchscreen","15 RGB rev + 6 info LEDs","Dual Hall clutch with 5 modes"],
 cons:["Currently pre-order; late June 2026 delivery","Trak Racer Device Manager required"],
 buy:"https://trakracer.com/products/bwt-alpine-formula-onetm-team-a525-replica-steering-wheel",
 notes:"Officially licensed BWT Alpine F1 A525 replica wheel with a 4.3-inch touchscreen, 12 buttons, 4 push rotaries, 4 thumb encoders, and Hall-sensor clutch paddles."}
```

## Brands surveyed but no new additions found

- **Simucube** — current branded wheels (Tahko Round, Tahko Round Black, Tahko GT-21, Valo GT-23, Valo GT-23 Leather, Valo Evo, Savu Sport, Savu Pro) all already in the catalog. No new 2026 release found beyond Valo Evo (already included).
- **Simagic** — FX, FX Pro, GTS, GT1, GT4, GT Neo, NEO X family, GT Pro Hub variants are reflected. The FX-C and FX-C Pro variants overlap with the existing FX Formula entries; verify if the FX-C is a distinct catalog SKU.
- **MOZA** — older lineup covered; CES 2026 additions (Porsche Mission R, CS Pro, KS Pro CES 2026) added above. Existing entries cover the rest.
- **Asetek SimSports** — existing entries cover Initium PC, La Prima Formula, La Prima GT Comfort+, Forte Formula, Forte Formula Pro, Invicta Formula. Initium Xbox is a console-only variant (skip per project rule); Dished Suede Rim is rim-only (Standalone Rims tab).
- **GSI** — existing entries cover Hyper P1, Hyper SL, FPE V2, GXL V2, X-29, GT-MAX32, Interlock Ultra, Interlock + rim. No new own-brand model surfaced for 2026.
- **VRS** — only DirectForce Pro Formula remains the sole branded wheel.
- **VNM Simulation** — no second own-brand wheel surfaced beyond GT V1.
- **Heusinkveld** — One already in catalog. DisplayDash is a button-box / display hybrid rather than a steering wheel; if a separate "button boxes / dash" tab exists it could go there. It is not a USB sim wheel by definition.
- **SRC (SimRacingCoach)** — full lineup matches existing catalog (USB, PRO USB, Universal Wireless lines).
- **Simline** — replica catalog matches existing entries.
- **HRS Australia** — only confirmed retail SKUs are GT8-BT and GT8-USB MPI310 (existing). The SVGT3 announced in 2021 has no current product page.
- **SimXperience / GS-Cobra** — no standalone USB wheels; all rims are AccuForce-bound.
- **Frex / Frex SGP** — only own-brand standalone product is Type-C V2 (already in catalog).
- **Wink Racing**, **Pro Course Motorsports**, **Acces Italia / TopRacing**, **Ricmotech RST**, **Simjack** (wheels), **Simmson**, **iSpeedy / Speedmaster** — no current production own-brand standalone USB sim wheel located.

## Notes

- Diameters left as `?mm` should be confirmed before adding to the catalog (BavarianSimTec OmegaOne, MOZA CS Pro CES 2026, MOZA KS Pro CES 2026, Trak Racer A525).
- Cube Controls GT Pro V2 also has a Reparto Corse Round Suede, Reparto Corse Zero Suede, Reparto Corse Perforated, and a Rubber variant. The catalog already lists "GT Pro V2" and "GT Pro V2 Reparto Corse Round" — adding all variants risks bloat. Recommend adding only Sport, Zero, and Cube as the architecturally distinct rims.
- The Cube Controls F-Core EVO is in the catalog without disambiguation. The current cubecontrols.com listing splits it into Formula Black, Formula Blue, GT Black, and GT Red variants (€409–€419) — whether to add each variant is an editorial decision.
