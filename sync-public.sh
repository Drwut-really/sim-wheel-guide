#!/usr/bin/env bash
# sync-public.sh — Copies public-safe files from main to the public branch and
# pushes to GitHub (origin). Called automatically by update_wheels.sh after each
# cron run, or manually to force a sync.
#
# Usage:
#   bash sync-public.sh [push-url]
#   push-url: optional GitHub URL with PAT already injected. If omitted, uses
#             GITHUB_PERSONAL_ACCESS_TOKEN from ~/.claude/.env to build it.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Files and directories that are safe to publish
SAFE_FILES="index.html README.md validate.sh wheel_research_prompt.md wrangler.jsonc _redirects .env.example sync-public.sh update_catalog_may2026.py"

# Build push URL if not passed in
PUSH_URL="${1:-}"
if [[ -z "$PUSH_URL" ]]; then
    if [[ -f "$HOME/.claude/.env" ]]; then
        # shellcheck disable=SC1091
        source "$HOME/.claude/.env"
    fi
    if [[ -n "${GITHUB_PERSONAL_ACCESS_TOKEN:-}" ]]; then
        REMOTE_URL=$(git -C "$SCRIPT_DIR" config --get remote.origin.url)
        PUSH_URL="${REMOTE_URL/https:\/\//https:\/\/oauth2:${GITHUB_PERSONAL_ACCESS_TOKEN}@}"
    fi
fi

CURRENT=$(git -C "$SCRIPT_DIR" rev-parse --abbrev-ref HEAD)

# Stash any uncommitted changes so we can switch branches cleanly
STASHED=false
if ! git -C "$SCRIPT_DIR" diff --quiet || ! git -C "$SCRIPT_DIR" diff --cached --quiet; then
    git -C "$SCRIPT_DIR" stash push --include-untracked -m "sync-public: auto-stash"
    STASHED=true
fi

cleanup() {
    git -C "$SCRIPT_DIR" checkout "$CURRENT" 2>/dev/null || true
    if [[ "$STASHED" == "true" ]]; then
        git -C "$SCRIPT_DIR" stash pop 2>/dev/null || true
    fi
}
trap cleanup EXIT

# Switch to public branch
git -C "$SCRIPT_DIR" checkout public

# Pull updated safe files from main
# shellcheck disable=SC2086
git -C "$SCRIPT_DIR" checkout main -- $SAFE_FILES

# Sync research/ and docs/ directories if they exist on main
git -C "$SCRIPT_DIR" checkout main -- research/ 2>/dev/null || true
git -C "$SCRIPT_DIR" checkout main -- docs/ 2>/dev/null || true

# Commit if anything changed
git -C "$SCRIPT_DIR" add -A
if ! git -C "$SCRIPT_DIR" diff --cached --quiet; then
    SYNC_DATE=$(date -u '+%Y-%m-%d')
    git -C "$SCRIPT_DIR" commit -m "sync: update from main ${SYNC_DATE}"
fi

# Push to GitHub (public branch)
if [[ -n "$PUSH_URL" ]]; then
    git -C "$SCRIPT_DIR" push "$PUSH_URL" public
else
    git -C "$SCRIPT_DIR" push origin public
fi

echo "sync-public.sh: public branch updated and pushed."
