# Going Public — Pre-flight Checklist

This catalog repo is currently **private**. The live page on Cloudflare is already publicly viewable; the source repo just isn't. Follow this checklist before flipping the GitHub repo to public visibility.

> ⚠️ **DO NOT run any step here until the user explicitly says "go public."** Treat this as a procedural reference.

---

## Step 1 — Full backup FIRST (before any cleanup)

```bash
DATE=$(date +%Y-%m-%d)
mkdir -p /mnt/internal_ssd/backups
cd /mnt/internal_ssd/Projects
zip -r "/mnt/internal_ssd/backups/sim-wheel-guide-${DATE}-pre-public-backup.zip" \
    sim-wheel-guide-creation/
echo "Backup written to /mnt/internal_ssd/backups/sim-wheel-guide-${DATE}-pre-public-backup.zip"
```

Store this zip somewhere safe (external drive, encrypted cloud, etc.). It captures the full pre-cleanup state including .git/ history, untracked files, and anything we end up scrubbing later.

---

## Step 2 — Inventory of files needing scrub or move

| File | Issue | Action |
|---|---|---|
| `update_wheels.sh` | Hardcoded PandaSpec Discord webhook URL | Move webhook to `.env` (gitignored); reference via `${DISCORD_WEBHOOK}` env var |
| `CLAUDE.md` | Same webhook + Pi local IP + user hardware setup + "About This User" section | Either scrub personal sections OR replace with a public-safe `CLAUDE.md` and gitignore the local copy |
| `PROJECT_STATE.md` | Pi paths (`/home/pi/...`), absolute dev folder paths (`/mnt/internal_ssd/Projects/`), LAN IP `10.0.5.241` | Generic-ize paths; remove LAN IP |
| `SETUP.md` | Pi-5-specific deployment specifics, sudoers tweaks, etc. | Either scrub or move to a `private/` folder that's gitignored |
| `wheel_research_prompt.md` | Internal prompt template | KEEP (a prompt is fine to publish; might rate-limit if scrapers spam, but minor) |

---

## Step 3 — Reorganize the research folder

Going public means human-made research and AI-generated research should be visually separated. AI artifacts go in a sub-folder; the parent stays for human notes.

```bash
cd /mnt/internal_ssd/Projects/sim-wheel-guide-creation/research
mkdir -p ai
git mv \
    2026-04-25_sweep_rewrites.json \
    description_cleanup.json \
    missing_sim_objects.json \
    missing_sim_wheels_findings.md \
    research_accessories.md \
    research_moza_simagic_asetek.md \
    research_simline.md \
    research_simracingcoach_and_missing.md \
    standalone_rims_findings.md \
    standalone_rims_objects.json \
    url_match_report.md \
    ai/
```

Going-forward convention:
- **`research/`** (parent) — human-made research, market analysis, personal notes
- **`research/ai/`** — AI-generated agent outputs (sweep rewrites, deep-research findings, batch JSONs)

---

## Step 4 — Update `.gitignore`

Add (alongside what's already there):

```gitignore
# Secrets
.env
.env.*
!.env.example

# Personal Claude config (if anything stored in-repo)
.claude/
*.local

# Backup zips (in case anyone runs the backup script in-tree)
*.zip
sim-wheel-guide-*.zip

# Private folder (if Step 2 moves SETUP.md there)
private/
```

---

## Step 5 — Webhook secret rotation (CRITICAL)

The PandaSpec Discord webhook URL is hardcoded in `update_wheels.sh` and `CLAUDE.md` in the **current repo history**. **Removing it from `main` does NOT remove it from `git log`.** If the repo is flipped public, the webhook is exposed.

Two options:

**Option A — Recommended: rotate the webhook**
1. In Discord → Server Settings → Integrations → Webhooks → find the wheel-guide webhook → "Copy Webhook URL" gives you the URL; click "..." → "Delete Webhook"
2. Create a new webhook with the same name (record the new URL)
3. Update `.env` (gitignored) with the new URL
4. Old webhook URL is dead even if leaked

**Option B — Rewrite git history**
Use `git filter-repo` (or BFG) to scrub the webhook from history before flipping public.
```bash
pip install git-filter-repo
cd sim-wheel-guide-creation
git filter-repo --replace-text <(echo 'https://discord.com/api/webhooks/[REDACTED]==>$REDACTED_WEBHOOK')
# Force-push history rewrite
git push --force origin main
```
Heavier; only do if rotation isn't an option.

**Both options should be combined.** Rotate the webhook AND scrub history. Belt-and-suspenders.

---

## Step 6 — Public-safe `CLAUDE.md`

The current `CLAUDE.md` has:
- "About This User" section (preferences, sim time, primary sim)
- Hardware Setup table (specific gear, Link Hub ownership, devices)
- Hardcoded webhooks
- Pi-specific paths

For a public repo, choose one:

**Option A — Sanitize in place** (simpler):
Remove the "About This User" + "Hardware Setup" + webhook sections; keep the schema, conventions, brand notes, validation rules. The user-specific stuff lives in the user's auto-memory anyway.

**Option B — Two CLAUDE.md files**:
- `CLAUDE.public.md` — sanitized, checked into the repo
- `CLAUDE.md` — kept locally, gitignored
- Symlink locally so Claude Code still auto-loads the personal one

---

## Step 7 — License

Add a `LICENSE` file. Reasonable options:
- **MIT** — permissive, code-style; fine for the HTML+JS catalog
- **CC-BY-4.0** — better for the dataset itself (the wheel info); requires attribution
- **MIT for code + CC-BY for data** — split via a NOTICE file

The footer note already says "free to share, fork, and modify; link back appreciated" — that aligns with MIT or CC-BY.

---

## Step 8 — Final pre-flight commit

```bash
git add -A
git commit -m "Public-readiness pass: webhook to .env, research/ai split, .gitignore, scrubbed personal info"
git push origin main
```

---

## Step 9 — Flip repo visibility

```bash
gh repo edit Drwut-really/sim-wheel-guide --visibility public --accept-visibility-change-consequences
```

---

## Step 10 — Post-flip verification

- Browse the public repo URL from a **logged-out browser tab** — confirm no webhooks or personal info visible
- Search the repo for `discord.com/api/webhooks` — should return zero matches in current code
- Check `git log --all -p | grep -F 'discord.com/api/webhooks'` — should be zero matches if Step 5 ran
- Confirm `.env.example` is committed (showing what env vars are needed) but `.env` is not
- Verify the live Cloudflare deploy still works: `curl -sI https://simracing-catalogue.mdw7wkp6fg.workers.dev/`
- Test a fresh clone in a tmp directory and verify it works without `.env`:
  ```bash
  cd /tmp && git clone https://github.com/Drwut-really/sim-wheel-guide test && cd test && ls -la
  ```

---

## Step 11 — Optional polish before announcing

- Badges in README (build / link-check / live status)
- A `CONTRIBUTING.md` if you want PRs from the public
- A `SECURITY.md` with how to report secret leaks
- GitHub Actions for `validate.sh` on every PR

---

## Decision flag

This checklist sits in the repo. **The actual decision to go public is the user's** — Claude shouldn't autonomously execute these steps. When the user says "let's go public," start at Step 1 and don't skip the backup.
