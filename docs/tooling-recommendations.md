# Tooling Recommendations

Tools that would help Claude assist with sim-wheel-guide work but aren't installed yet. Review and install manually as needed. RPi5 / Debian 13 / aarch64.

_Last refreshed: 2026-04-25_

## Already installed

| Tool | Path | Used for |
|---|---|---|
| `curl` | `/usr/bin/curl` | URL probing, Discord webhook posts, CF deploy checks |
| `wget` | `/usr/bin/wget` | File downloads |
| `jq` | `/usr/bin/jq` | JSON parsing (lychee output, audit results) |
| `lychee` | `~/.local/bin/lychee` | Bulk URL link-checker (`buy:` URLs across catalog) |
| `node` | `~/.local/bin/node` | v20.18.1 — runs validate.sh's acorn parse |
| `npm` | `~/.local/bin/npm` | acorn install |
| `acorn` | `~/.local/bin/acorn` | 8.16.0 — JS syntax validation in validate.sh |
| `python3` | `/usr/bin/python3` | bulk-edit scripts, local test server |
| `git` | `/usr/bin/git` | version control |
| `gh` | `/usr/bin/gh` | GitHub CLI (auth as Drwut-really) |

## High-impact install candidates

### 1. chromium-browser (headless mode) — biggest win

Lets Claude actually render the page's JS and verify filter buttons / preorder badges / Simucube tag merges work — instead of just curl-grepping HTML structure.

```bash
sudo apt update && sudo apt install -y chromium-browser
# verify
chromium-browser --version
# usage during a smoke test
chromium-browser --headless --disable-gpu --screenshot=/tmp/page.png http://localhost:8000/
chromium-browser --headless --disable-gpu --dump-dom http://localhost:8000/ > /tmp/dom.html
```

### 2. playwright (Python flavor) — programmable browser

Click filter buttons, assert post-click DOM state, take comparison screenshots, run cross-browser. Best fit for catalog interactivity tests.

```bash
pip3 install --user playwright
~/.local/bin/playwright install chromium
# verify
~/.local/bin/playwright --version
# example: see tests/smoke.py once installed (a tiny script can click each filter button and assert visible card count)
```

### 3. html-tidy — strict HTML validator

Catches duplicate-`style=` attributes, missing close tags, malformed markup. We currently catch some of this via ad-hoc grep in validate.sh; tidy is more thorough.

```bash
sudo apt install -y tidy
# usage
tidy -q -e index.html      # warnings to stderr; pipe-friendly
tidy -q -e index.html 2>&1 | head -20
```

## Medium-impact

### 4. htmlq — `jq` for HTML

CSS-selector queries against HTML files. No more brittle regex.

```bash
# No apt package on Debian 13. Install via prebuilt binary:
mkdir -p ~/.local/bin
curl -L https://github.com/mgdm/htmlq/releases/latest/download/htmlq-aarch64-unknown-linux-gnu.tar.gz \
  | tar -xz -C ~/.local/bin htmlq
chmod +x ~/.local/bin/htmlq
# verify
htmlq --version
# usage
htmlq '.filter-btn' --text < index.html
htmlq 'div.legend-item strong' --text < index.html
```

### 5. httpie — friendlier curl

Cleaner JSON output for API-style probing. Useful when WebFetch isn't available.

```bash
sudo apt install -y httpie
# verify
http --version
# usage
http GET https://simracing-catalogue.mdw7wkp6fg.workers.dev/
```

### 6. w3m / lynx — text-mode browsers

Marginal value for this site since the catalog is JS-driven (no JS in lynx/w3m), but useful for sanity-rendering markdown content and previewing static HTML.

```bash
sudo apt install -y w3m lynx
```

## Low-impact / skip for now

### 7. lighthouse — Google web auditor

Performance / accessibility / SEO audit. Heavy install (Node + headless Chromium); questionable ROI for an internal LAN catalog. Revisit if we ever go public-facing.

```bash
# only if we ever want it:
npm install -g lighthouse
# requires global Chromium, increases attack surface for a tool we'd run rarely
```

### 8. vnu — W3C HTML validator

Java jar, strict W3C compliance. Heavy install relative to signal for this project.

```bash
# only if we ever want it:
# download jar from https://github.com/validator/validator/releases
# requires JRE
```

## Recurring habit

At the start of any non-trivial sim-wheel-guide session, scan `~/.local/bin /usr/local/bin /usr/bin` for newly installed tools the user may have added between sessions:

```bash
for t in chromium-browser playwright tidy htmlq httpie http; do
  command -v "$t" >/dev/null 2>&1 && echo "[ok] $t -> $(command -v "$t")" || echo "[--] $t missing"
done
```

If anything new shows up, refresh awareness — don't blindly reinstall.
