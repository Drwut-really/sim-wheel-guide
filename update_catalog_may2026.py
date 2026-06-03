#!/usr/bin/env python3
"""
May 2026 catalog update script.
Fixes duplicates, bad fields, and adds new products.
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ────────────────────────────────────────────────────────
# 1. FIX: GT-X2 price  (id:22)
# ────────────────────────────────────────────────────────
html = html.replace(
    '{id:22,brand:"Cube Controls",model:"GT-X2",section:"sim",subcat:"Cube Controls",conn:"blue",dia:"300–320mm",shape:"D-shape GT",inputs:20,display:true,simhub:true,bt:true,price:"€1,692",pros:["5-inch touchscreen","SimHub full display support","2025 GT design","320mm available"],cons:["Very expensive","Bluetooth only","Heavy"],buy:"https://www.cubecontrols.com/product/gtx2/",notes:"Cube\'s GT wheel with display. Accessories: front plate in 4 colors (black/white/green/red); interchangeable grip swaps 30→32cm diameter."}',
    '{id:22,brand:"Cube Controls",model:"GT-X2",section:"sim",subcat:"Cube Controls",conn:"blue",dia:"300–320mm",shape:"D-shape GT",inputs:20,display:true,simhub:true,bt:true,price:"€1,387",pros:["5-inch 854×480 touchscreen with SimHub dashboard","15 RGB RPM LED bar, 6 RGB flag LEDs","10 RGB backlit buttons, 2 front toggles, 2 back toggles, 2 funky switches, 2 thumb encoders","Dual full-aluminium clutch paddles, Hall sensor paddles","Carbon-fiber-reinforced front plate in 4 colors (black/white/green/red)","Die-cast aluminium body"],cons:["Very expensive at €1,387","Bluetooth wireless only, no wired-only option","1,408g, heavier than most GT wheels"],buy:"https://www.cubecontrols.com/product/gtx2/",notes:"Cube\'s GT wheel with 5-inch touchscreen. Interchangeable grip swaps 300→320mm diameter. Accessories: color variants (Black/White/Green/Red front plate); hub included."}'
)

# ────────────────────────────────────────────────────────
# 2. FIX: Heusinkveld One  (id:94) — remove date from model, fix buy URL
# ────────────────────────────────────────────────────────
html = html.replace(
    'model:"One Steering Wheel — Released Fall 2025"',
    'model:"One"'
)
html = html.replace(
    'buy:"https://heusinkveld.com/new-heusinkveld-one-steering-wheel/"',
    'buy:"https://heusinkveld.com/shop/wheel/one/"'
)

# ────────────────────────────────────────────────────────
# 3. FIX: YOUR Ultimate (id:262) — wrong conn (orange→blue), fix buy URL
# ────────────────────────────────────────────────────────
html = html.replace(
    '{id:262, brand:"Ascher Racing", model:"YOUR Ultimate", section:"sim", subcat:"Ascher Racing", conn:"orange", dia:"300mm", shape:"formula closed", inputs:30, display:false, simhub:true, bt:false, lights:true, price:"€1699", pros:["Custom laser-etched logos","Choice of red, blue, gold or black thumb encoders, knobs, and rotaries","Inspired by McLaren Artura Ultimate","Closed-bottom design"], cons:["No screen","High starting price"], buy:"https://ascher-racing.com/int/news/post/news-ascher-racing-your-ultimate1", notes:"Customizable variant of the Ascher Ultimate launched March 2025 with personalized engraving and color options on the standard Ultimate hardware."}',
    '{id:262, brand:"Ascher Racing", model:"YOUR Ultimate", section:"sim", subcat:"Ascher Racing", conn:"blue", dia:"300mm", shape:"Formula Closed", inputs:26, display:true, simhub:true, bt:false, lights:true, price:"From €1,699", pros:["Fully customizable via online configurator: logo, encoder color, knob color","4-inch dashboard with 21 RGB shift LEDs, full SimHub support","14 RGB illuminated buttons, 4 thumb encoders, 2 seven-way joysticks, 2 twelve-position rotaries","Gen6 silenced magnetic double-paddle shifters and dual clutch","USB universal — works on Simucube, Simagic, MOZA, Asetek, VRS, and others","Laser-etched button caps: choose from common symbols or custom"], cons:["Starting at €1,699 before options","No wireless option","USB cable required"], buy:"https://ascher-racing.com/int/catalog/category/view/s/ultimate-konfigurator/id/76/", notes:"Personalized build of the McLaren Artura Ultimate launched March 2025. Choose custom engravings and accent colors via Ascher\'s online configurator."}'
)

# ────────────────────────────────────────────────────────
# 4. REMOVE: stale/duplicate entries
#    ids: 95 (MOZA KS Pro multi-rim), 98 (Heusinkveld One duplicate),
#         269 (MOZA Mission R stub), 270 (MOZA CS Pro stub), 271 (MOZA KS Pro stub)
# ────────────────────────────────────────────────────────

entries_to_remove = [
    # id:95 — combined KS Pro entry superseded by id:84 and id:85
    r'  \{id:95,brand:"MOZA",model:"KS Pro \(multiple rim sizes\)".*?\},\n',
    # id:98 — minimal Heusinkveld One duplicate (full entry is id:94)
    r'  \{id:98,brand:"Heusinkveld",model:"One".*?\},\n',
    # id:269 — MOZA Porsche Mission R stub (superseded by id:86)
    r'  \{id:269, brand:"MOZA", model:"Porsche Mission R".*?\},\n',
    # id:270 — MOZA CS Pro stub (superseded by id:85)
    r'  \{id:270, brand:"MOZA", model:"CS Pro".*?\},\n',
    # id:271 — MOZA KS Pro CES stub (superseded by id:84)
    r'  \{id:271, brand:"MOZA", model:"KS Pro \(CES 2026\)".*?\},\n',
]

for pattern in entries_to_remove:
    html, n = re.subn(pattern, '', html, count=1, flags=re.DOTALL)
    if n == 0:
        print(f"WARNING: pattern not matched: {pattern[:60]}")

# ────────────────────────────────────────────────────────
# 5. ADD: three new entries before the closing ];
# ────────────────────────────────────────────────────────

new_entries = """  {id:292,brand:"Ascher Racing",model:"McLaren Artura Ultimate",section:"sim",subcat:"Ascher Racing",conn:"blue",dia:"300mm",shape:"Formula Closed",inputs:26,display:true,simhub:true,lights:true,price:"€1,499",pros:["4-inch dashboard with 21 RGB shift LEDs, full SimHub support","14 RGB automotive push buttons with telemetry-based lighting","4 thumb encoders, 2 seven-way joysticks, 2 twelve-position rotary switches","Gen6 silenced magnetic double-paddle shifters and dual clutch","USB universal — Simucube, Simagic, MOZA, Asetek, VRS, Fanatec, and others","Interchangeable laser-etched button caps, no-tools swap"],cons:["No wireless option","€1,499 premium for a USB display wheel","3×50mm bolt pattern needs spacer QR for some wheelbases","1,520g — heavier than screenless formula wheels"],buy:"https://ascher-racing.com/int/ascher-racing-mclaren-artura-ultimate/",notes:"Top of the McLaren Artura line. Identical components to the real Artura GT4 wheel, plus the 4-inch SimHub-compatible dashboard. Accessories: optional QR for Simucube 2/3, Asetek, MOZA, Simagic EVO, or VRS; optional Knob Kit Pro."},
  {id:293,brand:"Ascher Racing",model:"AR × Simucube Ultimate",section:"sim",subcat:"Ascher Racing",conn:"blue",dia:"300mm",shape:"Formula Closed",inputs:26,display:true,simhub:true,lights:true,price:"€1,499",pros:["Ascher Artura Ultimate hardware with official Simucube co-branding","4-inch dashboard with 21 RGB shift LEDs, full SimHub support","14 RGB push buttons, 4 thumb encoders, Gen6 dual clutch","SC3 QR Mounting Adapter included in the box","USB universal — any PC-connected wheelbase"],cons:["USB only — Simucube SC Pass-Through not supported","Currently listed as out of stock on Ascher website","3×50mm bolt pattern needs spacer QR for some wheelbases"],buy:"https://ascher-racing.com/int/shop/steering-wheels/ascher-racing-x-simucube-ultimate/",notes:"Co-branded version of the Artura Ultimate, launched October 14, 2025 alongside Ascher × Simucube collaboration announcement. Hardware identical to standard Artura Ultimate. Simucube Link QR optional add-on."},
  {id:294,brand:"Zen's Simwheels",model:"LMZ Evo",section:"preorder",subcat:"Zen's Simwheels",conn:"blue",dia:"298mm",shape:"LMP/Hypercar",inputs:25,display:true,simhub:true,lights:true,price:"From €1,229",releaseDate:"2026-Q2",pros:["Custom 4.3-inch 800×480 display at 60fps, full SimHub integration confirmed","18 telemetry LEDs on the display panel","8 RGB buttons, 5 RGB multi-position rotary switches, 2 thumb encoders, 2 FUNKY switches","4 magnetic N52 aluminium paddle shifters, single or dual clutch","Forged carbon main plate and paddles, full CNC 6061 aluminium housing","Glass screen plate, 50.8mm direct hub included (70mm adapter available)","Multi-link: center rotary can link to thumb encoders for expanded input count"],cons:["From €1,229 before clutch upgrade and encoder options","1,540g full option — heavier than most formula wheels","Preorder only, small Dutch manufacturer","298mm LMP/hypercar shape not for all drivers"],buy:"https://www.zenssimwheels.com/product-page/lmz-evo",notes:"Dutch manufacturer. LMH/LMDh hypercar-inspired wheel. Optional Elma thumb-encoders (4.5Ncm). QR-USB support via 4-pin JST 2.54 connector directly on PCB. Sim Racing Expo Charlotte showcase planned before release."},
"""

html = html.replace('\n];', '\n' + new_entries + '];', 1)

# ────────────────────────────────────────────────────────
# 6. UPDATE: last-updated date (header + meta-line)
# ────────────────────────────────────────────────────────
html = html.replace(
    'Updated April 25, 2026',
    'Updated May 1, 2026'
)
html = html.replace(
    'Last updated: April 25, 2026',
    'Last updated: May 1, 2026'
)

# ────────────────────────────────────────────────────────
# Sanity check before write
# ────────────────────────────────────────────────────────
if html == original:
    print("ERROR: no changes made — check find strings")
else:
    changed = sum(1 for a, b in zip(original.splitlines(), html.splitlines()) if a != b)
    print(f"Changes detected across ~{changed} lines")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done writing index.html")
