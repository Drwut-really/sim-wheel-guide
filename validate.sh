#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# SC2 Wheel Guide — Validation Script
# Run this before committing any HTML changes.
# ─────────────────────────────────────────────────────────────────────────────

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export HTML_FILE="$SCRIPT_DIR/index.html"

if [[ ! -f "$HTML_FILE" ]]; then
    echo "❌ HTML file not found: $HTML_FILE"
    exit 1
fi

echo "🔍 Validating $HTML_FILE ..."
echo ""

# Check for acorn
if ! command -v node &>/dev/null; then
    echo "❌ Node.js not found — install with: sudo apt-get install -y nodejs"
    exit 1
fi

if ! npm list -g acorn &>/dev/null && ! node -e "require('acorn')" 2>/dev/null; then
    echo "📦 Installing acorn JS parser globally..."
    npm install -g acorn
fi

# Ensure node can resolve globally-installed acorn (matters when node was installed
# via prebuilt binary into ~/.local rather than via apt — npm root -g points at
# ~/.local/lib/node_modules but node's default require path doesn't include it).
if command -v npm &>/dev/null; then
    export NODE_PATH="$(npm root -g):${NODE_PATH:-}"
fi

# Run the validation
node << 'NODE_EOF'
const fs = require('fs');
const path = require('path');

let acorn;
try {
    acorn = require('acorn');
} catch (e) {
    // Try global install path
    const globalPath = require('child_process').execSync('npm root -g').toString().trim();
    acorn = require(path.join(globalPath, 'acorn'));
}

const html = fs.readFileSync(process.env.HTML_FILE || './index.html', 'utf8');

let errors = 0;
let warnings = 0;

// 1. Extract and parse JS
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) {
    console.log('❌ No <script> block found');
    process.exit(1);
}

try {
    acorn.parse(scriptMatch[1], { ecmaVersion: 2020 });
    console.log('✅ JS syntax valid');
} catch (e) {
    console.log('❌ JS SYNTAX ERROR:', e.message);
    errors++;
}

// 2. Extract WHEELS array and validate fields
const wheelsMatch = scriptMatch[1].match(/const WHEELS = \[([\s\S]*?)\];\s*\nlet currentTab/);
if (!wheelsMatch) {
    console.log('❌ Could not extract WHEELS array');
    process.exit(1);
}

let WHEELS;
try {
    eval('WHEELS = [' + wheelsMatch[1] + ']');
} catch (e) {
    console.log('❌ WHEELS array eval failed:', e.message);
    process.exit(1);
}

const required = ['id', 'brand', 'model', 'section', 'subcat', 'conn', 'dia', 'shape',
                  'inputs', 'display', 'simhub', 'price', 'pros', 'cons', 'buy', 'notes'];
// Optional fields (validated only if present): bt (boolean), adapter (non-empty string)
let fieldErrors = 0;
WHEELS.forEach(w => {
    required.forEach(f => {
        if (w[f] === undefined) {
            console.log('  ❌ id:' + w.id + ' missing field: ' + f);
            fieldErrors++;
        }
    });
    if (!Array.isArray(w.pros) || !Array.isArray(w.cons)) {
        console.log('  ❌ id:' + w.id + ' pros/cons must be arrays');
        fieldErrors++;
    }
    if (w.bt !== undefined && typeof w.bt !== 'boolean') {
        console.log('  ❌ id:' + w.id + ' optional field bt must be boolean');
        fieldErrors++;
    }
    if (w.adapter !== undefined && (typeof w.adapter !== 'string' || w.adapter.trim() === '')) {
        console.log('  ❌ id:' + w.id + ' optional field adapter must be a non-empty string');
        fieldErrors++;
    }
    if (w.lights !== undefined && typeof w.lights !== 'boolean') {
        console.log('  ❌ id:' + w.id + ' optional field lights must be boolean');
        fieldErrors++;
    }
    if (w.releaseDate !== undefined && (typeof w.releaseDate !== 'string' || w.releaseDate.trim() === '')) {
        console.log('  ❌ id:' + w.id + ' optional field releaseDate must be a non-empty string');
        fieldErrors++;
    }
    if (w.isNew !== undefined && typeof w.isNew !== 'boolean') {
        console.log('  ❌ id:' + w.id + ' optional field isNew must be boolean');
        fieldErrors++;
    }
    // Preorder admission rule: must have a working buy URL or a releaseDate
    if (w.section === 'preorder' && (!w.buy || w.buy.trim() === '') && !w.releaseDate) {
        console.log('  ❌ id:' + w.id + ' preorder entry must have either a buy URL or a releaseDate');
        fieldErrors++;
    }
});

if (fieldErrors === 0) {
    console.log('✅ All ' + WHEELS.length + ' entries pass field validation');
} else {
    errors += fieldErrors;
}

// 3. Section counts
const sections = {};
WHEELS.forEach(w => sections[w.section] = (sections[w.section] || 0) + 1);
console.log('📊 Sections: ' + JSON.stringify(sections));

// 4. Check for duplicate IDs
const ids = WHEELS.map(w => w.id);
const dupes = ids.filter((id, i) => ids.indexOf(id) !== i);
if (dupes.length > 0) {
    console.log('❌ Duplicate IDs found: ' + dupes.join(', '));
    errors++;
} else {
    console.log('✅ All IDs unique');
}

// 5. HTML structural checks
const openScript = (html.match(/<script>/g) || []).length;
const closeScript = (html.match(/<\/script>/g) || []).length;
if (openScript !== closeScript) {
    console.log('❌ Mismatched script tags: ' + openScript + ' open, ' + closeScript + ' close');
    errors++;
}

// 6. Duplicate style attributes (regression check)
if (/style="[^"]*"[^>]*\sstyle="/.test(html)) {
    console.log('❌ Duplicate style attribute found on same element');
    errors++;
} else {
    console.log('✅ No duplicate style attributes');
}

// 7. Required element IDs exist
['cnt-sim', 'cnt-oval', 'cnt-preorder', 'cnt-new', 'btn-display', 'btn-simhub', 'btn-lights',
 'search', 'cards', 'count', 'subcats', 'preorder-warning', 'new-info', 'meta-line'].forEach(id => {
    if (!html.includes('id="' + id + '"')) {
        console.log('❌ Missing element id: ' + id);
        errors++;
    }
});

// 8. File stats
console.log('');
console.log('📦 File: ' + (html.length / 1024).toFixed(1) + ' KB, ' + WHEELS.length + ' wheels');

console.log('');
if (errors === 0) {
    console.log('✅ ALL CHECKS PASSED — file is valid');
    process.exit(0);
} else {
    console.log('❌ ' + errors + ' error(s) found — DO NOT save until fixed');
    process.exit(1);
}
NODE_EOF
