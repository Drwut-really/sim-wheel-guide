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

Current size: **261 wheels** across **35+ brands** (May 2026).

---

## Editorial rules

- **No referral or affiliate links.** Every buy link points to the manufacturer's own website. Reseller links aren't used. The only exception is products with no manufacturer site of their own.
- **No bias in link choice.** Every brand is linked the same way.
- **Pros and cons compare hardware specs only.** Bullets describe diameter, inputs, paddle type, materials, and displays. Brand reputation, customer service, and warranty experiences are not factored in.
- **Sources:** brand websites, sim racing review sites, authorized retailers. Aliexpress / eBay / Etsy are excluded unless the brand is Simjack or Simmson.

---

## How auto-updates work

Twice a month (1st and 15th, 06:15 UTC), a Raspberry Pi runs Claude Code against the guide. Claude:

1. Searches the web for new wheels and rims across 12 targeted queries
2. Verifies current MSRP pricing on existing entries while visiting brand sites
3. Adds qualifying new entries to the HTML
4. Updates the `price` field on existing entries where MSRP has changed
5. Runs the validator (`validate.sh`)
6. Commits and pushes to GitHub (Cloudflare auto-deploys from `main`)
7. Posts a rich-embed changelog to Discord (added / removed / format changes / price moves ≥$150)

The validator must pass before anything is committed. If validation fails, the previous HTML is restored and the run aborts.

---

## Repo structure

```
sim-wheel-guide/
├── index.html                 ← the catalog (one self-contained HTML file)
├── update_wheels.sh           ← bi-weekly cron entry point (requires .env)
├── sync-public.sh             ← syncs public-safe files to the public branch
├── wheel_research_prompt.md   ← Claude Code prompt template
├── validate.sh                ← linter (acorn JS parse + field checks)
├── wrangler.jsonc             ← Cloudflare Workers config (auto-deploy on push)
├── _redirects                 ← Cloudflare URL redirects
├── .env.example               ← env var names required by update_wheels.sh
├── README.md                  ← this file
├── updater.log                ← run history (gitignored)
├── cron.log                   ← cron launch log (gitignored)
├── backups/                   ← bi-weekly HTML snapshots (gitignored)
└── research/                  ← audit trail JSONs from past expansions
```

---

## Commands reference

All commands assume you're in the project root (wherever you cloned the repo).

### Trigger an update manually

```bash
./update_wheels.sh
```

Runs the full pipeline: research → price check → validate → commit → push → Discord. Output streams to `updater.log`. Safe to run any time — backups roll the prior HTML to `backups/` before any edits.

### Validate the current HTML

```bash
./validate.sh
```

Runs the acorn JS parser plus field/ID/style checks. Prints section counts. Returns non-zero on any failure (which is what the cron uses to decide whether to restore the backup).

### See the latest cron run

```bash
tail -40 updater.log
tail -20 cron.log
```

### Check the cron schedule

```bash
crontab -l
```

Should show a line running `update_wheels.sh` at 06:15 UTC on the 1st and 15th of each month.

### Re-deploy without a content change

The Cloudflare Worker redeploys on every push to `main`. To force a redeploy without changing content, bump the meta-line timestamp in `index.html` and push.

### Restore from backup

```bash
cp backups/simracing-wheel-guide-YYYY-MM.html index.html
./validate.sh   # confirm the backup is still valid
git diff index.html
```

### Rotate the GitHub PAT

The PAT lives in `~/.claude/.env` (chmod 600). To rotate:

```bash
# Replace token; preserve env-var format
printf 'GITHUB_PERSONAL_ACCESS_TOKEN=%s\n' "<new_token>" > ~/.claude/.env
chmod 600 ~/.claude/.env
# Verify
source ~/.claude/.env && curl -s -H "Authorization: token $GITHUB_PERSONAL_ACCESS_TOKEN" \
  https://api.github.com/repos/Drwut-really/sim-wheel-guide | grep full_name
```

The same token is consumed by the GitHub MCP server via `~/.claude/mcp-github-wrapper.sh`, so no other config needs updating.

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
