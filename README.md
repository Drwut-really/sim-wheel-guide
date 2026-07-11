# Sim Racing Wheel Guide

A self-contained, free catalog of sim racing steering wheels and rims. Browse it from any web browser on any device — phone, tablet, laptop, desktop. Each entry shows price, size, features, pros and cons, and a link to the manufacturer's own website.

**Live page:** http://www.simgear.online or the backup https://simracing-catalogue.mdw7wkp6fg.workers.dev/

---

## What's in the catalog

| Tab | Contents |
|-----|----------|
| **Sim Specific** | Wheels with electronics (buttons, displays, paddles) |
| **Standalone Rims** | Bare rims that pair with a button plate |
| **Preorders** | Upcoming wheels with confirmed release dates |

Current size: **270 wheels** across **35+ brands** (July 2026).

---

## Editorial rules

- **No referral or affiliate links.** Every buy link points to the manufacturer's own website. Reseller links aren't used. The only exception is products with no manufacturer site of their own.
- **No bias in link choice.** Every brand is linked the same way.
- **Pros and cons compare hardware specs only.** Bullets describe diameter, inputs, paddle type, materials, and displays. Brand reputation, customer service, and warranty experiences are not factored in.
- **Sources:** brand websites, sim racing review sites, authorized retailers. Aliexpress / eBay / Etsy are excluded unless the brand is Simjack or Simmson.

---

## Keeping it current

The catalog is reviewed and refreshed regularly — new wheels and rims are added, and prices are re-checked against manufacturer sites. Every change is validated with `validate.sh` before it is published.

---

## Repo structure

```
sim-wheel-guide/
├── index.html                 ← the catalog (one self-contained HTML file)
├── validate.sh                ← linter (acorn JS parse + field checks)
├── sync-public.sh             ← syncs public-safe files to the public branch
├── update_catalog_may2026.py  ← one-off catalog migration script (historical)
├── wheel_research_prompt.md   ← research prompt template
├── wrangler.jsonc             ← Cloudflare Workers config (auto-deploy on push)
├── _redirects                 ← Cloudflare URL redirects
├── CNAME                      ← custom domain for the live page
├── .env.example               ← template of environment variable names
├── README.md                  ← this file
└── research/                  ← audit-trail notes from past catalog expansions
```

---

## Validate the catalog

```bash
./validate.sh
```

Runs the acorn JS parser plus field/ID/style checks and prints section counts. Returns non-zero on any failure.

---

## Data schema (single wheel entry)

Each wheel is a JavaScript object in the `WHEELS` array inside `index.html`:

```js
{
  id: 261,
  brand: "Simucube",
  model: "Tahko GT-21",
  section: "sim",            // "sim" | "oval" | "preorder"
  subcat: "Simucube Brand",
  conn: "orange",            // see connection codes
  dia: "320mm",
  shape: "GT",
  inputs: 18,
  display: true,
  simhub: true,
  price: "$649–$699",
  pros: ["Native SC2 wireless", "Alcantara grip"],
  cons: ["28-input limit on Simucube wireless"],
  buy: "https://simucube.com/tahko/",
  notes: "First Simucube wireless wheel."
}
```

**Optional fields:** `bt` (boolean → 📶 BT badge), `adapter` (string → 🔌 chip), `lights` (boolean → 💡 RPM/FLAG badge), `releaseDate` (string, preorder only → 🗓 badge).

### Connection codes (`conn` field)

| Code | Meaning |
|------|---------|
| `orange` | Simucube native — SC Wireless (BLE) and SC Link / LightBridge |
| `blue` | USB cable — universal, full SimHub |
| `mixed` | USB + Bluetooth dual-mode (Cube Controls) |
| `wireless` | Proprietary wireless dongle (Heusinkveld One) |
| `gray` | Rim only — no electronics |
| `simagic` | Simagic base-locked (older FX / GT models) |

---

## Sharing

Free to share, fork, and modify. A link back to this repo when you republish is appreciated, not required.
