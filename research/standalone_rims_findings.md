# Real Motorsport Rims Research — 2026-04-25

## Summary
- **Brands surveyed:** Sparco, OMP, Momo, MPI, Atech, Sabelt, Nardi, Personal, Luisi, OBP, Racetech, RRS, Bell, Razor, Tilton, Mountney, NRG, Cube Controls, Wink Racing
- **New candidates ready for catalog:** ~55
- **Skipped/excluded:**
  - Sparco P310, OMP 310 Alu GT, Momo MOD 30, MPI SimMax-D, MPI SimMax MP14 (already in catalog)
  - Sparco P310 Open (back-ordered indefinitely — kept anyway, customer can wait)
  - Mountney (PCD 101mm — incompatible with motorsport 6x70mm hubs)
  - NRG (mass-market aftermarket aesthetic, not pure motorsport)
  - Cube Controls (electronics-equipped — wrong tab)
  - Razor / Tilton (no current production rims)
  - Wink Racing (formula-style only — minimal lineup found)

URL verification: All listed URLs hit 200 in WebFetch unless noted. Sparco USA, Momo Motorsport, MPI, OMP USA, Atech, JHPUSA, Pegasus, OBP all bot-friendly. The OMP USA `us.ompracing.com` deep links work; the `/c/...` index sometimes 404s.

---

## New entries (paste-ready JS objects)

### Sparco — confirmed via sparcousa.com product pages

```js
{id:?, brand:"Sparco", model:"R 383", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke round, suede grip, 39mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$285 (rim only)",
 pros:["Sparco's #1 selling competition rim","Anatomic thick grip","Standard 6x70mm bolt pattern"],
 cons:["No buttons or hardware — needs button plate","Suede only at this price"],
 buy:"https://www.sparcousa.com/r-383",
 notes:"330mm round suede competition rim, 39mm dish."}
```

```js
{id:?, brand:"Sparco", model:"R 383 Logo", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke round, suede with embroidered logo, 39mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$309 (rim only)",
 pros:["Same R 383 geometry","Embroidered Sparco logo","Standard 6x70mm bolt pattern"],
 cons:["Cosmetic premium over R 383","No electronics"],
 buy:"https://www.sparcousa.com/product/r-383-logo",
 notes:"R 383 with embroidered logo."}
```

```js
{id:?, brand:"Sparco", model:"R 330", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke round, leather or suede, 39mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$285 (rim only)",
 pros:["Yellow leather centering stripe","Variable grip diameter","6x70mm bolt pattern"],
 cons:["No flat-bottom version of this SKU","No buttons"],
 buy:"https://www.sparcousa.com/product/r330"}
```

```js
{id:?, brand:"Sparco", model:"R 330B", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke round, blue suede, 39mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$339 (rim only)",
 pros:["Blue suede colorway","Same anatomic grip as R 330","6x70mm bolt pattern"],
 cons:["Color premium","No buttons"],
 buy:"https://www.sparcousa.com/product/r330b"}
```

```js
{id:?, brand:"Sparco", model:"R 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke round, leather or suede, 39mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$285 (rim only)",
 pros:["350mm fits trucks and rally builds","Yellow leather centering stripe","6x70mm bolt pattern"],
 cons:["Larger diameter increases torque demand","No buttons"],
 buy:"https://www.sparcousa.com/product/r350"}
```

```js
{id:?, brand:"Sparco", model:"R 350B", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke round, blue suede, 39mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$339 (rim only)",
 pros:["Blue suede colorway of R 350","Same geometry","6x70mm bolt pattern"],
 cons:["Color premium","No buttons"],
 buy:"https://www.sparcousa.com/product/r350b"}
```

```js
{id:?, brand:"Sparco", model:"R 353", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke flat-bottom, suede, 36mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$295 (rim only)",
 pros:["Flat-bottom for leg clearance","Compact 330mm","6x70mm bolt pattern"],
 cons:["No buttons","Slight premium over R 383"],
 buy:"https://www.sparcousa.com/product/r-353"}
```

```js
{id:?, brand:"Sparco", model:"R 345", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke deep dish, suede or leather, 63mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$285 (rim only)",
 pros:["63mm dish suits classic and rally seating","Yellow leather centering stripe","6x70mm bolt pattern"],
 cons:["Dish reduces effective reach — measure cockpit","No flat-bottom"],
 buy:"https://www.sparcousa.com/r-345"}
```

```js
{id:?, brand:"Sparco", model:"R 325", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke very deep dish, suede, 95mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$285 (rim only)",
 pros:["95mm deep dish for vintage / rally cockpits","Yellow centering stripe","6x70mm bolt pattern"],
 cons:["Very deep — verify clearance to body","No buttons"],
 buy:"https://www.sparcousa.com/r-325"}
```

```js
{id:?, brand:"Sparco", model:"R 368", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"380mm", shape:"3-spoke deep dish, suede, 65mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$275 (rim only)",
 pros:["380mm fits trucks and stock car sims","65mm dish","6x70mm bolt pattern"],
 cons:["Largest Sparco diameter — confirm cockpit clearance","No buttons"],
 buy:"https://www.sparcousa.com/product/r-368"}
```

```js
{id:?, brand:"Sparco", model:"R 215", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"2-spoke deep dish, suede or leather, 90mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$285 (rim only)",
 pros:["Unique 2-spoke design","90mm dish","6x70mm bolt pattern"],
 cons:["2-spoke layout — verify hub clearance","No buttons"],
 buy:"https://www.sparcousa.com/r-215"}
```

```js
{id:?, brand:"Sparco", model:"R 215 Flat", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"2-spoke flat (0mm dish), suede or leather",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$285 (rim only)",
 pros:["Flat 2-spoke variant","Yellow centering stripe","6x70mm bolt pattern"],
 cons:["Flat dish increases distance to driver","No buttons"],
 buy:"https://www.sparcousa.com/product/r-215-flat"}
```

```js
{id:?, brand:"Sparco", model:"R 323", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke round, suede, 39mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$275 (rim only)",
 pros:["Entry-tier R-series","Suede grip","6x70mm bolt pattern"],
 cons:["No flat-bottom variant","No buttons"],
 buy:"https://www.sparcousa.com/product/r-323"}
```

```js
{id:?, brand:"Sparco", model:"R 375", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke round, suede, 36mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$275 (rim only)",
 pros:["350mm with shallow 36mm dish","Suede grip","6x70mm bolt pattern"],
 cons:["No flat-bottom","No buttons"],
 buy:"https://www.sparcousa.com/product/r-375"}
```

```js
{id:?, brand:"Sparco", model:"P 300", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"300mm", shape:"3-spoke flat, suede",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$285 (rim only)",
 pros:["Compact 300mm for formula and karting builds","Flat dish","6x70mm bolt pattern"],
 cons:["Smallest Sparco — heavy on big bases","No buttons"],
 buy:"https://www.sparcousa.com/product/p-300"}
```

```js
{id:?, brand:"Sparco", model:"P 310 Open", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"310mm", shape:"3-spoke flat open-bottom, suede",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$365 (rim only)",
 pros:["Open-bottom layout for ultimate leg clearance","Flat dish","6x70mm bolt pattern"],
 cons:["Premium over standard P 310","Often back-ordered"],
 buy:"https://www.sparcousa.com/product/p-310-open"}
```

### OMP — confirmed via us.ompracing.com product pages

```js
{id:?, brand:"OMP", model:"Targa 330", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke flat suede, oval 37x29mm grip",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$299 (rim only)",
 pros:["OMP best-seller, classic comp rim","Flat dish, 3 anodized spokes","Yellow centering stripe"],
 cons:["No buttons","No flat-bottom variant"],
 buy:"https://www.us.ompracing.com/p/targa-steering-wheel/",
 notes:"OMP Targa 330mm, p/n OD/2005NN."}
```

```js
{id:?, brand:"OMP", model:"WRC", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke semi-dish, suede or leather, 70mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$299 (rim only)",
 pros:["Designed for rally with deep 70mm dish","Round 30mm grip","6x70mm bolt pattern"],
 cons:["Deep dish is rally-specific ergonomics","No buttons"],
 buy:"https://www.us.ompracing.com/p/wrc-steering-wheel/",
 notes:"OMP WRC, p/n OD/1979."}
```

```js
{id:?, brand:"OMP", model:"Corsica 330", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke deep dish, suede, 75mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$275 (rim only)",
 pros:["75mm deep dish suits classic / vintage builds","Premium suede leather","6x70mm bolt pattern"],
 cons:["Deep dish reduces effective reach","No buttons"],
 buy:"https://competitionmotorsport.com/products/omp-corsica-330",
 notes:"OMP Corsica, p/n OD/2012/N. Linked to Competition Motorsport (bot-friendly retailer)."}
```

```js
{id:?, brand:"OMP", model:"Superquadro", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke flat-bottom, anatomical suede, 35x27mm oval grip",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$319 (rim only)",
 pros:["Flat-bottom for leg clearance","Anatomical grip","6x70mm bolt pattern"],
 cons:["No buttons","Suede only"],
 buy:"https://www.us.ompracing.com/p/superquadro-steering-wheel/",
 notes:"OMP Superquadro, p/n OD0-1990."}
```

```js
{id:?, brand:"OMP", model:"Velocita", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"380mm", shape:"3-spoke flat smooth leather, oval 35x30mm grip",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$329 (rim only)",
 pros:["380mm size for stock car / NASCAR sims","Smooth leather grip","6x70mm bolt pattern"],
 cons:["Leather (not suede) — less grip with gloves","No buttons"],
 buy:"https://www.us.ompracing.com/p/steering-wheel-velocita/",
 notes:"OMP Velocita, p/n OD0-2030."}
```

```js
{id:?, brand:"OMP", model:"Velocita Superleggero", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke flat aluminum/suede, 30mm round grip",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$399 (rim only)",
 pros:["40% lighter than standard Velocita","Aluminum + suede construction","6x70mm bolt pattern"],
 cons:["Premium price","No buttons"],
 buy:"https://www.us.ompracing.com/p/velocita-superleggero-suede-leather-350mm-diameter-steering-wheel/",
 notes:"OMP Velocita Superleggero, p/n OD/2020/N."}
```

```js
{id:?, brand:"OMP", model:"Trecento", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"300mm", shape:"3-spoke flat suede leather, lower offset spokes",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$279 (rim only)",
 pros:["Lower-offset spokes for instrument visibility","Compact 300mm","6x70mm bolt pattern"],
 cons:["Compact diameter increases steering effort","No buttons"],
 buy:"https://www.us.ompracing.com/p/trecento-steer-wheel-suede-leathe/",
 notes:"OMP Trecento (race-spec), p/n OD0-1975."}
```

```js
{id:?, brand:"OMP", model:"Trecento Uno", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"300mm", shape:"3-spoke flat polyurethane (anti-skid)",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$209 (rim only)",
 pros:["Anti-skid polyurethane handgrip","Compact 300mm","Affordable entry rim"],
 cons:["Polyurethane wears faster than suede","No buttons"],
 buy:"https://www.us.ompracing.com/p/steering-wheel-trecento-uno/",
 notes:"OMP Trecento Uno (tuning), p/n OD0-1989."}
```

```js
{id:?, brand:"OMP", model:"Rally", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke suede leather rally rim",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$999 (rim only)",
 pros:["Premium suede-leather rally trim","350mm rally diameter","6x70mm bolt pattern"],
 cons:["Significant price step","No buttons"],
 buy:"https://www.us.ompracing.com/p/rally-steer-w-suede-leath/",
 notes:"OMP Rally premium, p/n OD0-2028."}
```

```js
{id:?, brand:"OMP", model:"320 Alu Rally", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"320mm", shape:"3-spoke flat aluminum, suede; co-developed with WRC champion Kalle Rovanperä",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$429 (rim only)",
 pros:["Flat aluminum spokes","Compact 320mm rally diameter","6x70mm bolt pattern"],
 cons:["Often out of stock at OMP USA","No buttons"],
 buy:"https://www.us.ompracing.com/p/steering-wheel-320-alu-rally/",
 notes:"OMP 320 Alu Rally, p/n OD0-2042-A03."}
```

```js
{id:?, brand:"OMP", model:"350 Alu Flat", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke flat aluminum with steering angle indicator",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$429 (rim only)",
 pros:["Flat aluminum spokes","Built-in colored steering angle indicator","6x70mm bolt pattern"],
 cons:["No flat-bottom","No buttons"],
 buy:"https://www.us.ompracing.com/p/flat-steering-wheel-in-aluminium-diam-350-mm-with-colored-steer-angle/",
 notes:"OMP flat-spoke 350mm, p/n OD0-2046."}
```

```js
{id:?, brand:"OMP", model:"320 Hybrid S", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"320mm", shape:"3-spoke flat carbon/aluminum hybrid",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$3,799 (rim only)",
 pros:["Carbon/aluminum hybrid construction","Top-tier OMP comp rim","Used in pro motorsport"],
 cons:["Among most expensive standalone rims","Niche use case"],
 buy:"https://www.us.ompracing.com/p/320-hybrid-s-flat-steering-wheel/",
 notes:"OMP 320 Hybrid S, p/n OD0-2048."}
```

### Momo — confirmed via momomotorsport.com product pages

```js
{id:?, brand:"Momo", model:"MOD. 07", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke round, leather or suede, 72mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$279 (rim only)",
 pros:["Weight-reducing spoke cutouts","Yellow horn button and stitching","6-bolt pattern"],
 cons:["Frequently out of stock","No buttons"],
 buy:"https://momomotorsport.com/steering-wheels/race-steering-wheels/mod-07"}
```

```js
{id:?, brand:"Momo", model:"MOD. 08", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke deep dish, leather or suede, 88mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$279 (rim only)",
 pros:["Deep 88mm dish for vintage / stock car sims","Lightened anodized spokes","6-bolt pattern"],
 cons:["Deep dish reduces reach","No buttons"],
 buy:"https://momomotorsport.com/steering-wheels/race-steering-wheels/mod-08"}
```

```js
{id:?, brand:"Momo", model:"MOD. 78", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke round, leather or suede, 36-40mm dish (also 320 and 350 sizes)",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$279 (rim only)",
 pros:["Inspired by classic Montecarlo design","GT/sedan racing favorite","Multiple sizes"],
 cons:["No buttons","Round only"],
 buy:"https://momomotorsport.com/steering-wheels/race-steering-wheels/mod-78"}
```

```js
{id:?, brand:"Momo", model:"MOD. 80", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"346mm", shape:"3-spoke shallow dish, leather or suede, 33mm dish",
 inputs:2, display:false, simhub:false, bt:false,
 price:"$309 (rim only)",
 pros:["Two pre-installed accessory buttons","6-bolt pattern","Comfort-focused grip"],
 cons:["Buttons need own wiring/circuitry — not USB","No display"],
 buy:"https://momomotorsport.com/steering-wheels/race-steering-wheels/mod-80",
 notes:"Buttons are bare contacts — pair with button plate / external interface."}
```

```js
{id:?, brand:"Momo", model:"MOD. 88", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"320mm", shape:"3-spoke flat-bottom, suede thicker grip, 0mm dish (also 350mm)",
 inputs:2, display:false, simhub:false, bt:false,
 price:"$279 (rim only)",
 pros:["Flat-bottom for leg clearance","Two accessory buttons","6-bolt pattern"],
 cons:["Buttons need own wiring","No encoders or display"],
 buy:"https://momomotorsport.com/steering-wheels/race-steering-wheels/mod-88",
 notes:"Buttons are bare contacts — pair with button plate."}
```

```js
{id:?, brand:"Momo", model:"MOD. Drift", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke deep concave, suede with finger notches, 88mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$279 (rim only)",
 pros:["Deep concave dish for hand-over-hand drifting","Back finger notches","6-bolt pattern"],
 cons:["Drift-specific ergonomics","No buttons"],
 buy:"https://momomotorsport.com/steering-wheels/race-steering-wheels/mod-drift"}
```

```js
{id:?, brand:"Momo", model:"MOD. 30 with Buttons", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"320mm", shape:"3-spoke flat-bottom, leather, 0mm dish, with horn-side accessory buttons",
 inputs:2, display:false, simhub:false, bt:false,
 price:"$279 (rim only)",
 pros:["Two pre-installed accessory buttons","Flat-bottom for leg clearance","6-bolt pattern"],
 cons:["Buttons require own wiring (not USB)","No encoders / paddles / display"],
 buy:"https://momomotorsport.com/steering-wheels/race-steering-wheels/mod-30-buttons",
 notes:"Buttons are bare contacts — pair with button plate or external interface."}
```

```js
{id:?, brand:"Momo", model:"Prototipo Heritage", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke round, distressed leather, 39mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$299 (rim only)",
 pros:["Iconic vintage Prototipo styling","Natural distressed leather","6-bolt pattern"],
 cons:["Heritage trim — not flat-bottom","No buttons"],
 buy:"https://momomotorsport.com/steering-wheels/heritage-steering-wheels/prototipo-heritage"}
```

```js
{id:?, brand:"Momo", model:"Indy Heritage", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke round, mahogany wood with Zebrano gloss, 37mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$389 (rim only)",
 pros:["Mahogany wood rim with brushed aluminum spokes","Engraved Indy insignia","6-bolt pattern"],
 cons:["Wood grip not motorsport-grip texture","Premium price"],
 buy:"https://momomotorsport.com/shop/indy",
 notes:"Heritage wood rim — historical NASCAR / Indy aesthetic."}
```

### MPI — confirmed via maxpapisinc.com and hrsims.com

```js
{id:?, brand:"MPI", model:"SimMax MP15", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"381mm", shape:"3-spoke stock-car oval, Hypergrip cover, 76mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$249 (rim only)",
 pros:["Authentic NASCAR Cup 15-inch geometry","Hypergrip cover","Universal 6x70mm and 3x51mm bolt pattern"],
 cons:["Sim-only — not road-rated","Often out of stock"],
 buy:"https://maxpapisinc.com/product/mpi-sim-mp15/",
 notes:"15-inch sim version of NASCAR MP15."}
```

```js
{id:?, brand:"MPI", model:"SimMax-F", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"324mm", shape:"3-spoke road course style, suede grip, 32mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$219-$287 (rim only)",
 pros:["Road course / formula geometry","Lightweight 1000g","Universal 6x70mm and 3x51mm bolt pattern"],
 cons:["Sim-only","Compact 324mm only"],
 buy:"https://maxpapisinc.com/product/mpi-simmax-f/",
 notes:"MPI road-course style sim wheel, SKU MPI-SIM-F."}
```

```js
{id:?, brand:"MPI", model:"SimMax GT", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"324mm", shape:"3-spoke GT style, microfiber Alcantara + RG no-slip, 32mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$219-$268 (rim only)",
 pros:["GT-style grip with no-slip hand zones","Lightweight 850g","Universal bolt pattern"],
 cons:["Sim-only","Compact 324mm — not for stock car"],
 buy:"https://maxpapisinc.com/product/mpi-simmax-gt/"}
```

```js
{id:?, brand:"MPI", model:"SimMax H60 Drift", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"349mm", shape:"3-spoke drift-style, microfiber Alcantara, 60mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$219 (rim only)",
 pros:["60mm dish for drift seating","Alcantara grip","Universal bolt pattern"],
 cons:["Drift-specific ergonomics","Sim-only"],
 buy:"https://maxpapisinc.com/product/mpi-simmax-h60/"}
```

```js
{id:?, brand:"MPI", model:"GT-RSC-310", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"310mm", shape:"3-spoke flat top/bottom, RG high-grip with cross-stitching, 0mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$479 AUD (rim only)",
 pros:["Inspired by MPI GT12SC used in Australian Supercars","Lightweight 750g","Standard 6x70mm bolt pattern"],
 cons:["Sim-/Touring-spec — limited US distribution","No buttons"],
 buy:"https://hrsims.com/products/mpi-gt-rsc-310-racing-steering-wheel-310mm",
 notes:"Italian-built, individually serial numbered."}
```

### Sabelt — confirmed via Pegasus Auto Racing

```js
{id:?, brand:"Sabelt", model:"2026X", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke flat-bottom, suede with thumb reliefs, 0mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$309 (rim only)",
 pros:["Sabelt is Ferrari and Porsche racing OEM","Flat-bottom design","Bonded suede (no stitching to fail)"],
 cons:["No buttons","No center hole — no horn"],
 buy:"https://www.pegasusautoracing.com/productdetails.asp?RecID=28212",
 notes:"Sabelt 2026X, sold via bot-friendly Pegasus."}
```

```js
{id:?, brand:"Sabelt", model:"2010X", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke flat round, suede, 0mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$306 (rim only)",
 pros:["Aggressive spoke design","Bonded suede grip","6-bolt pattern"],
 cons:["No buttons","Flat dish only"],
 buy:"https://www.pegasusautoracing.com/productdetails.asp?RecID=28213"}
```

```js
{id:?, brand:"Sabelt", model:"2038", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"320mm", shape:"3-spoke flat-bottom, suede, 0mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$340 (rim only)",
 pros:["Compact 320mm flat-bottom","Lightweight 3.1 lb","6-bolt pattern"],
 cons:["No center hole — no horn","No buttons"],
 buy:"https://www.pegasusautoracing.com/productdetails.asp?RecID=35211"}
```

```js
{id:?, brand:"Sabelt", model:"2007X", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke flat round, suede with yellow stripe, 0mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$296 (rim only)",
 pros:["350mm flat dish","Bonded suede","6-bolt pattern"],
 cons:["No buttons","Flat dish increases distance to driver"],
 buy:"https://www.pegasusautoracing.com/productdetails.asp?RecID=28215"}
```

```js
{id:?, brand:"Sabelt", model:"2009X", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke semi-dish, suede, 65mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$276 (rim only)",
 pros:["Semi-dish 65mm geometry","Bonded suede","6-bolt pattern"],
 cons:["No buttons","No flat-bottom"],
 buy:"https://www.pegasusautoracing.com/productdetails.asp?RecID=28214"}
```

```js
{id:?, brand:"Sabelt", model:"2005X", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke deep dish, suede, 90mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$296 (rim only)",
 pros:["Deep 90mm dish for muscle car / vintage builds","Bonded suede","6-bolt pattern"],
 cons:["Deep dish reduces effective reach","No buttons"],
 buy:"https://www.pegasusautoracing.com/productdetails.asp?RecID=28216"}
```

```js
{id:?, brand:"Sabelt", model:"2029", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke flat lightweight aluminum, suede, 0mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$440 (rim only)",
 pros:["30% weight reduction via aluminum rim","Bonded suede","6-bolt pattern"],
 cons:["Premium price","No buttons"],
 buy:"https://www.pegasusautoracing.com/productdetails.asp?RecID=32669"}
```

```js
{id:?, brand:"Sabelt", model:"SW-465", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke semi-dish with teardrop spoke cutouts, suede, 65mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$296 (rim only)",
 pros:["Lightening grooves in spokes","Suede with blue centering stripe","6-bolt pattern"],
 cons:["No buttons","Color-only differentiator from 2009X"],
 buy:"https://www.pegasusautoracing.com/productdetails.asp?RecID=35759"}
```

### Atech — confirmed via atech-racing.com

```js
{id:?, brand:"Atech", model:"3 Spokes 330", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke round, suede leather, flat dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"€154 (rim only, ex-VAT)",
 pros:["Czech-made motorsport rim used in EU rally / circuit","6x70mm bolt pattern","Affordable EU pricing"],
 cons:["EU shipping for US buyers","No buttons"],
 buy:"https://www.atech-racing.com/product/steering-wheels-3-spokes-diam-330/"}
```

```js
{id:?, brand:"Atech", model:"3 Spokes 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke round, suede leather, flat dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"€154 (rim only, ex-VAT)",
 pros:["350mm rally / GT diameter","6x70mm bolt pattern","Czech motorsport build"],
 cons:["EU shipping","No buttons"],
 buy:"https://www.atech-racing.com/product/steering-wheels-3-spokes-diam-350/"}
```

```js
{id:?, brand:"Atech", model:"3 Spokes 350 65mm Deep", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke 65mm deep dish, suede leather",
 inputs:0, display:false, simhub:false, bt:false,
 price:"€158 (rim only, ex-VAT)",
 pros:["65mm dish for classic rally cockpits","6x70mm bolt pattern","Atech motorsport pedigree"],
 cons:["EU shipping","No buttons"],
 buy:"https://www.atech-racing.com/product/steering-wheels-3-spokes-diam-350-65-mm-deep/"}
```

```js
{id:?, brand:"Atech", model:"3 Spokes 350 90mm Deep", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke 90mm deep dish, suede leather",
 inputs:0, display:false, simhub:false, bt:false,
 price:"€161 (rim only, ex-VAT)",
 pros:["Very deep 90mm dish","6x70mm bolt pattern","Atech build"],
 cons:["Deep dish reduces effective reach","No buttons"],
 buy:"https://www.atech-racing.com/product/steering-wheels-3-spokes-diam-350-90-mm-deep/"}
```

```js
{id:?, brand:"Atech", model:"2 Spokes 350 90mm Deep", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"2-spoke 90mm deep dish, suede leather",
 inputs:0, display:false, simhub:false, bt:false,
 price:"€158 (rim only, ex-VAT)",
 pros:["Unique 2-spoke layout","Deep 90mm dish","6x70mm bolt pattern"],
 cons:["2-spoke pattern needs hub clearance check","EU shipping"],
 buy:"https://www.atech-racing.com/product/steering-wheels-2-spokes-diam-350-90-mm-deep/"}
```

### Nardi — confirmed via JHPUSA (US retailer, bot-friendly)

```js
{id:?, brand:"Nardi", model:"Classic 330", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke round, perforated leather with red stitch, ~50mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$405 (rim only)",
 pros:["Italian heritage motorsport brand (since 1932)","Perforated leather grip","6-bolt pattern"],
 cons:["Premium price","No buttons"],
 buy:"https://jhpusa.com/products/nardi-classic-330mm-steering-wheel-black-perforated-leather-red-stitch"}
```

```js
{id:?, brand:"Nardi", model:"Classic 360", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"360mm", shape:"3-spoke round, perforated leather with red stitch, ~50mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$414 (rim only)",
 pros:["Larger 360mm Classic","Perforated leather","6-bolt pattern"],
 cons:["Larger diameter for tight cockpits","No buttons"],
 buy:"https://jhpusa.com/products/nardi-classic-360mm-steering-wheel-black-perforated-leather-red-stitch"}
```

```js
{id:?, brand:"Nardi", model:"Classic 390", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"390mm", shape:"3-spoke round, smooth leather with grey stitch, ~50mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$414 (rim only)",
 pros:["Largest Nardi Classic — fits stock car / NASCAR sims","Smooth leather","6-bolt pattern"],
 cons:["Largest diameter — verify cockpit clearance","No buttons"],
 buy:"https://jhpusa.com/products/nardi-classic-390mm-steering-wheel-black-leather-grey-stitch"}
```

```js
{id:?, brand:"Nardi", model:"Sport Rally Deep Corn 330", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke deep dish round, perforated leather, ~80mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$396 (rim only)",
 pros:["Deep Corn dish geometry — rally classic","Perforated leather","6-bolt pattern"],
 cons:["Deep dish reduces effective reach","No buttons"],
 buy:"https://jhpusa.com/products/nardi-sport-rally-deep-corn-330mm-steering-wheel-black-perforated-leather-red-stitch"}
```

```js
{id:?, brand:"Nardi", model:"Sport Rally Deep Corn 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke deep dish round, perforated leather, ~80mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$396-$450 (rim only)",
 pros:["Iconic Deep Corn rally rim","Perforated leather or suede options","6-bolt pattern"],
 cons:["Deep dish geometry","No buttons"],
 buy:"https://jhpusa.com/products/nardi-sport-rally-deep-corn-350mm-steering-wheel-black-perforated-red-stitch"}
```

```js
{id:?, brand:"Nardi", model:"Gara 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke flat round, perforated leather, ~30mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$387 (rim only)",
 pros:["Race-spec Gara line","Perforated leather grip","6-bolt pattern"],
 cons:["No flat-bottom variant","No buttons"],
 buy:"https://jhpusa.com/products/nardi-gara-350mm-steering-wheel-black-perforated-leather-red-stitching"}
```

```js
{id:?, brand:"Nardi", model:"Gara Sport 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke flat round, perforated leather, ~40mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$423 (rim only)",
 pros:["Sportier Gara variant","Perforated leather","6-bolt pattern"],
 cons:["Premium over standard Gara 350","No buttons"],
 buy:"https://jhpusa.com/products/nardi-gara-sport-350mm-steering-wheel-perforated-leather-red-stitch"}
```

```js
{id:?, brand:"Nardi", model:"3/0 Gara 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke flat round, smooth leather with black stitch, 0mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$369 (rim only)",
 pros:["Flat zero-dish geometry","Smooth leather grip","6-bolt pattern"],
 cons:["Flat dish increases reach distance","No buttons"],
 buy:"https://jhpusa.com/products/nardi-3-0-gara-350mm-steering-wheel-black-leather-black-stitch"}
```

```js
{id:?, brand:"Nardi", model:"Competition 330", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke round, perforated leather, ~30mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$369 (rim only)",
 pros:["Compact 330mm competition rim","Perforated leather","6-bolt pattern"],
 cons:["No flat-bottom variant","No buttons"],
 buy:"https://jhpusa.com/products/nardi-competition-330mm-steering-wheel-black-perforated-leather-grey-stitch"}
```

```js
{id:?, brand:"Nardi", model:"Gara 3/3 365", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"365mm", shape:"3-spoke deep dish round, smooth leather, ~70mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$450 (rim only)",
 pros:["365mm with deep 70mm dish","Smooth leather","6-bolt pattern"],
 cons:["Niche size","Deep dish geometry"],
 buy:"https://jhpusa.com/products/nardi-gara-3-3-365mm-steering-wheel-black-leather-black-stitch"}
```

```js
{id:?, brand:"Nardi", model:"Twin Line 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke round, two-tone smooth leather, ~40mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$378 (rim only)",
 pros:["Two-tone leather styling","Classic Nardi geometry","6-bolt pattern"],
 cons:["Smooth leather (not suede)","No buttons"],
 buy:"https://jhpusa.com/products/nardi-twin-line-350mm-steering-wheel-black-leather-combo"}
```

### Personal — confirmed via JHPUSA

```js
{id:?, brand:"Personal", model:"Neo Grinta 330", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke round, leather or suede, ~40mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$378-$441 (rim only)",
 pros:["Personal/Nardi parent — Italian heritage","Multiple grip and stitch options","6-bolt pattern"],
 cons:["Premium pricing","No buttons"],
 buy:"https://jhpusa.com/products/personal-neo-grinta-330mm-steering-wheel-black-leather-red-stitch"}
```

```js
{id:?, brand:"Personal", model:"Neo Grinta 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke round, leather or suede, ~40mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$378-$441 (rim only)",
 pros:["Larger 350mm Neo Grinta","Leather or suede","6-bolt pattern"],
 cons:["No flat-bottom","No buttons"],
 buy:"https://jhpusa.com/products/personal-neo-grinta-350mm-steering-wheel-black-suede-blue-stitch"}
```

```js
{id:?, brand:"Personal", model:"Grinta 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke round, suede or polyurethane, ~40mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$216-$441 (rim only)",
 pros:["Affordable poly variant","Suede option available","6-bolt pattern"],
 cons:["Polyurethane wears faster than suede","No buttons"],
 buy:"https://jhpusa.com/products/personal-grinta-350mm-steering-wheel-black-suede-red-stitch"}
```

```js
{id:?, brand:"Personal", model:"Trophy 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke round, leather or suede, ~40mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$405-$441 (rim only)",
 pros:["Personal Trophy line","Leather or suede options","6-bolt pattern"],
 cons:["No flat-bottom","No buttons"],
 buy:"https://jhpusa.com/products/personal-trophy-350mm-steering-wheel-black-leather-red-stitch"}
```

```js
{id:?, brand:"Personal", model:"Neo Eagle 340", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"340mm", shape:"3-spoke round, leather, ~40mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$378 (rim only)",
 pros:["Unique 340mm size","Leather grip","6-bolt pattern"],
 cons:["No suede option","No buttons"],
 buy:"https://jhpusa.com/products/personal-neo-eagle-340mm-steering-wheel-black-leather-blue-stitch"}
```

### Luisi — Italian heritage rally rim

```js
{id:?, brand:"Luisi", model:"Mirage Race", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke deep dish, suede or leather, 75mm dish",
 inputs:0, display:false, simhub:false, bt:false,
 price:"€270 (rim only)",
 pros:["Italian handmade — Volanti Luisi (ISO 9001)","75mm rally dish","Includes TÜV report for road use"],
 cons:["6x74mm bolt pattern (verify hub compatibility)","6-8 week delivery from EU","No buttons"],
 buy:"https://en.parts33.com/products/luisi-mirage-race-bs-sportlenkrad-wildleder-schwarz-geschusselt-mit-tuv",
 notes:"6x74mm PCD — slightly different from common 6x70mm; some hubs accept both."}
```

### Racetech — confirmed via racetech-usa.com

```js
{id:?, brand:"Racetech", model:"Flat Suede 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke flat round, suede",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$200 (rim only)",
 pros:["Affordable motorsport rim","Standard 6-hole pattern","Suede grip"],
 cons:["Less brand prestige than Sparco / OMP / Momo","No buttons"],
 buy:"https://racetech-usa.com/shop/Steering/flat-wheel"}
```

```js
{id:?, brand:"Racetech", model:"Flat Suede 330 Flat-Bottom", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke flat-bottom, suede",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$230 (rim only)",
 pros:["Flat-bottom for leg clearance","Compact 330mm","Standard 6-hole pattern"],
 cons:["Less established than Italian brands","No buttons"],
 buy:"https://racetech-usa.com/shop/Steering/flat-bottomed-steering-wheel-330mm"}
```

```js
{id:?, brand:"Racetech", model:"Dished Suede 350", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke deep dish round, suede",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$200 (rim only)",
 pros:["Dished design for muscle car / vintage seating","Suede grip","Standard 6-hole pattern"],
 cons:["No buttons","Brand less common in sim builds"],
 buy:"https://racetech-usa.com/shop/Steering/dished-wheel"}
```

```js
{id:?, brand:"Racetech", model:"Drag 330", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"330mm", shape:"3-spoke round, suede, drag-style geometry",
 inputs:0, display:false, simhub:false, bt:false,
 price:"$200 (rim only)",
 pros:["Drag-style ergonomics","Compact 330mm","Standard 6-hole pattern"],
 cons:["Drag geometry less typical for circuit sims","No buttons"],
 buy:"https://racetech-usa.com/shop/Steering/drag-steering-wheel"}
```

### OBP Motorsport — UK manufacturer

```js
{id:?, brand:"OBP Motorsport", model:"Suede Flat Bottom", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke flat-bottom, suede with weight-reducing spoke holes",
 inputs:0, display:false, simhub:false, bt:false,
 price:"£139 (rim only, approx $176)",
 pros:["UK-made motorsport rim","Holed-out spokes for weight","6-bolt pattern"],
 cons:["UK shipping for US buyers","No buttons"],
 buy:"https://www.obpltd.com/product-page/suede-trimmed-flat-bottom-steering-wheel/",
 notes:"OBP product page returned 403 to bot-fetch; user can verify via direct browser."}
```

```js
{id:?, brand:"OBP Motorsport", model:"Suede Flat Dish", section:"oval", subcat:"Track Rims", conn:"gray",
 dia:"350mm", shape:"3-spoke flat round, suede with weight-reducing spoke holes",
 inputs:0, display:false, simhub:false, bt:false,
 price:"£139 (rim only, approx $176)",
 pros:["UK-made motorsport rim","Lightened spokes","6-bolt pattern"],
 cons:["UK shipping","No buttons"],
 buy:"https://www.obpltd.com/product-page/suede-trimmed-flat-dish-steering-wheel/",
 notes:"OBP product page returned 403 to bot-fetch; user can verify via direct browser."}
```

---

## Brands surveyed but no new additions
- **NRG** — mass-market aftermarket aesthetic; not pure motorsport
- **Cube Controls** — all wheels include electronics (wrong tab — already in Sim Specific)
- **Mountney** — uses 101mm PCD, incompatible with motorsport 6x70mm hubs
- **Razor / Tilton** — no current production rims found
- **Bell Racing** — no current standalone steering wheel rim products in catalog
- **Wink Racing** — formula-only lineup; minimal info
- **Greddy / DAMD / OS Giken** — mostly OEM-replacement rims for road cars, not generic 6x70mm motorsport hubs
- **RRS** — has a small steering-wheel range but full catalog page bot-blocked; left for follow-up if needed

---

## Notes for integration

- **Existing entries to keep**: Sparco P310, OMP 310 Alu GT, Momo MOD 30, MPI SimMax-D, MPI SimMax MP14 (and Simline GT3 Cup R320, Simline Rally 350 — Simline-branded)
- **Bolt pattern**: All Italian / EU motorsport rims here use the **6x70mm** pattern that matches Ascher B24-SC, B16-USB, SimCore STD-WS GEN2, Simline BPv3, and SC2 hubs. Luisi Mirage uses 6x74mm (verify before recommending).
- **Connection**: All `gray` (rim only — no electronics).
- **subcat**: All `"Track Rims"` per existing convention.
- **Section**: `"oval"` per existing standalone-rims tab.
- **IDs**: Placeholder `id:?` — user will renumber from current high-water 174.

URL verification done by WebFetch direct-fetch; all 200 OK except OBP (403 to bot but loads in browser per their site behavior).
