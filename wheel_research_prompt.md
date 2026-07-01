# Wheel Guide Update — Research Prompt

You are updating a sim racing wheel reference catalog (all brands, all connection types).

**Today's timestamp:** {{TIMESTAMP}}
**HTML file to update:** {{HTML_FILE}}

Read `CLAUDE.md` in the same directory first — it contains the full project context, current wheel count, conventions, and the wheel data format.

---

## Step 1 — Web Research

Run these searches. For each, look for products NEW since the guide's "Last updated" timestamp:

1. "new Simucube 2 compatible steering wheel {{YEAR}}"
2. "new sim racing wheel release {{YEAR}} direct drive"
3. "sim racing wheel new SimHub display {{YEAR}}"
4. "new round oval steering wheel 320mm 325mm sim racing {{YEAR}}"
5. "Cube Controls GSI Ascher SRB new wheel {{YEAR}}"
6. "sim racing wheel 1 inch dish oval NASCAR 14 inch 15 inch {{YEAR}}"
7. "BavarianSimTec Conspit P1Sim Rexing Heusinkveld new wheel {{YEAR}}"
8. "MOZA new steering wheel {{YEAR}}"
9. "Asetek new steering wheel {{YEAR}}"
10. "sim racing wheel Bluetooth wireless {{YEAR}}"
11. "sim racing wheel preorder group buy release date {{YEAR}}"
12. "limited edition sim racing steering wheel {{YEAR}}"

For each result, note: brand, model name, price, diameter, connection type, whether it has a display, whether it supports SimHub, and a buy link.

---

## Step 2 — Read the existing HTML

Read `{{HTML_FILE}}` and identify all existing wheel IDs and models. Don't add duplicates.

---

## Step 2.5 — MSRP Price Verification

While you are already on brand websites from Step 1, check the current retail prices for **existing entries** from those same brands. You do not need to visit every brand — only the ones you already browsed during Step 1 research.

For each existing wheel entry whose price has changed from what is listed in the guide:
1. Update its `price` field to the current value
2. Record the change for the summary report

**Threshold for reporting:** Only flag changes ≥ $150 USD (or equivalent in local currency) in the final summary. Smaller corrections should still be made silently.

**Format for price field:** Keep the same style already used in the entry (e.g. `"$649"`, `"$649–$699"`, `"€599"`).

---

## Step 3 — Identify genuinely new wheels

Include any wheel that is:
- Released or announced AFTER the "Last updated" timestamp in the guide
- NOT already in the file
- A sim racing wheel from any brand — Simucube native, USB cable, USB+Bluetooth, brand-specific wireless, or paired with an adapter for cross-base use

**Sources:**
- ✅ Brand websites, sim racing review sites, authorized retailers
- ❌ Aliexpress / eBay / Etsy — UNLESS the brand is specifically Simjack or Simmson
- ✅ Off-brand / unique products are OK if genuinely interesting

**Dish rule for oval tab:** Round wheels 315mm+ with dish ≤1 inch (25mm).

**Bluetooth tag:** If a wheel supports Bluetooth, set `bt:true` (adds 📶 BT badge).

**Connection codes (`conn` field):**
- `orange` = SC Wireless (BLE via SC2/Link Hub)
- `blue` = USB cable
- `purple` = SC Link / LightBridge
- `mixed` = USB + Bluetooth dual-mode (Cube Controls)
- `wireless` = Proprietary wireless dongle (Heusinkveld One)
- `gray` = Rim only

---

## Step 4 — Preorders (HARD dates only)

Search for upcoming wheels with CONFIRMED, SPECIFIC dates only:
- A specific month + year (e.g. "May 2026", "Q2 2026 with confirmed shipping")
- A specific event anchor (e.g. "Charlotte Sim Racing Expo May 2026")
- An active preorder page with a confirmed ship date

EXCLUDE: "coming soon", "summer 2026", "TBD", "sometime next year".

Add qualifying preorders to `section:"preorder"` with IDs starting at 300+.

---

## Step 5 — Update the HTML

### Wheel entry format (single line per wheel):

```js
{id:NEW_ID,brand:"Brand",model:"Model Name",section:"sc2",subcat:"Brand",conn:"blue",isNew:true,dia:"300mm",shape:"Formula",inputs:18,display:false,simhub:true,bt:false,price:"$699",pros:["Pro 1","Pro 2"],cons:["Con 1"],buy:"https://url.com",notes:"Key note"}
```

Required fields: `id, brand, model, section, subcat, conn, dia, shape, inputs, display, simhub, price, pros, cons, buy, notes`. Optional: `bt`, `lights`, `adapter`, `releaseDate`.

**IMPORTANT — `isNew:true` is required on every new entry you add this run.** Existing entries should not carry `isNew:true`; clear it from any that still have it so newly added entries are the only ones flagged. Do NOT add `isNew:true` to existing entries. Do NOT add a date or emoji to the model name — the `isNew:true` flag is how new entries are surfaced in the 🆕 New tab.

Insert new wheels into the `WHEELS` array, just BEFORE the `];` that comes before `let currentTab`.

Use IDs:
- Regular wheels: next available after the highest existing ID
- Preorders: 300+

### Update both date stamps

There are two date strings in the file — update **both** to today's date (format: `Month D, YYYY`, e.g. `June 1, 2026`):

1. **header-sub div** (near the top of the `<body>`):
   ```html
   <div class="header-sub">Released + upcoming · Updated {{TIMESTAMP}}</div>
   ```
2. **meta-line JS** (near the bottom of the `<script>` block):
   ```js
   ... + ' brands · Last updated: {{TIMESTAMP}}';
   ```

Update both stamps yourself so the file stays consistent when previewed locally.

---

## Step 6 — Validate

After editing, run:
```bash
./validate.sh
```

The HTML must pass JS syntax check, field validation, and structural checks BEFORE saving as the final version.

If validation fails:
- Common issues: missing comma between entries (especially when a `// comment` is between them), double commas `},,`, duplicate style attributes
- See `CLAUDE.md` "Common Bugs From Past Sessions"

---

## Step 7 — Report

Output:
- How many new wheels added (or "none found this time")
- Names of new wheels
- Any preorders found with hard dates
- Any notable trends or brand news
- Any significant price changes found (≥$150 USD)

---

## Step 8 — Structured Summary (REQUIRED)

After your narrative report, output this exact block so the update can be parsed into a changelog summary:

```
=== WHEEL UPDATE SUMMARY START ===
WHEELS_ADDED_COUNT: <integer>
WHEELS_ADDED_NAMES: <pipe-separated list, e.g. "Brand Model A | Brand Model B", or "none">
WHEELS_REMOVED_COUNT: <integer>
WHEELS_REMOVED_NAMES: <pipe-separated list, or "none">
PRICES_UPDATED_COUNT: <integer>
MINOR_PRICE_CHANGES: <pipe-separated list of "Brand Model $OLD→$NEW" for changes <$150, or "none">
MAJOR_PRICE_CHANGES: <pipe-separated list of "Brand Model $OLD→$NEW (±$DIFF)" for changes ≥$150, or "none">
PREORDERS_FOUND_COUNT: <integer>
PREORDER_NAMES: <pipe-separated list of "Brand Model (Release: DATE)", or "none">
FORMAT_CHANGES: <one-line description of any schema/structure/CSS changes, or "none">
NOTABLE_TRENDS: <one-line note on brand news or industry shifts, or "none">
=== WHEEL UPDATE SUMMARY END ===
```

Rules:
- Do not omit or reorder any of the eleven key lines
- Use whole dollar values for USD (e.g. `$699→$449 (-$250)`)
- `WHEELS_REMOVED_*` will almost always be `0` / `none` (the workflow does not normally delete entries — only flag if you removed a preorder that shipped without a real product page, or a vaporware entry)
- `FORMAT_CHANGES` should only be non-`none` if you altered the schema, the CSS, or added/removed a section/tab — do NOT list routine field updates here
- `NOTABLE_TRENDS` is optional color (e.g. "Three brands released wireless variants this cycle") — keep to one line

---

## Rules

- Do NOT remove existing entries
- You MAY update the `price` field on existing entries when the current retail price has changed (Step 2.5)
- Do NOT change any other field on existing entries (model, specs, pros, cons, buy URL, etc.)
- Do NOT change CSS or JS logic
- Only add wheels you can verify are genuinely new
- Every new entry MUST have `isNew:true` — no exceptions
- Do NOT add `isNew:true` to any entry that already existed before this run
- Do NOT put a date, 🆕, or any other marker in the model name
- HTML must remain valid and self-contained
- Always run validate.sh before declaring done
