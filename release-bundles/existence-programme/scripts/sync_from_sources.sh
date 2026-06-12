#!/usr/bin/env bash
#
# sync_from_sources.sh
# ====================
#
# Pull fresh paper sources from their authoritative locations into this
# refinement workspace.
#
# Source locations:
#   01-04  -- vfd-crystalisation-paper/papers/<slug>/
#   05-10  -- solution-lab/experiments/<slug>/paper/
#
# Use this when:
#   - Source-of-truth has changed and you want the latest in the workspace
#   - You want to compare workspace edits against source state
#
# Usage:
#   ./scripts/sync_from_sources.sh           # pull all 10 papers
#   ./scripts/sync_from_sources.sh --dry-run # show what would be copied

set -e

DRY_RUN=false
for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=true ;;
        *) echo "Unknown arg: $arg"; exit 2 ;;
    esac
done

# Resolve paths
BUNDLE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CRYST="$BUNDLE_ROOT/../../papers"
SL="$(cd "$BUNDLE_ROOT/../../../solution-lab/experiments" 2>/dev/null && pwd)"

if [ -z "$SL" ]; then
    echo "ERROR: solution-lab not found. Expected at:"
    echo "  $BUNDLE_ROOT/../../../solution-lab/"
    echo "Adjust the SL path in this script if your repo layout differs."
    exit 1
fi

echo "Source paths:"
echo "  vfd-crystalisation-paper papers: $CRYST"
echo "  solution-lab experiments:        $SL"
echo

# Mapping: workspace_dir : source_dir : tex_name : bib_name
PAPERS=(
    "01-existence-as-closure:$CRYST/existence-as-recursive-closure:main.tex:references.bib"
    "02-life-as-closure:$CRYST/life-as-closure:main.tex:references.bib"
    "03-processing-to-point-of-view:$CRYST/processing-to-point-of-view:main.tex:references.bib"
    "04-cosmic-closure-recurrence:$CRYST/cosmic-closure-recurrence:main.tex:references.bib"
    "05-bioelectric-closure:$SL/001-vfd-bioelectric-closure/paper:paper.tex:refs.bib"
    "06-cortical-phase-closure:$SL/002-vfd-cortical-phase-closure/paper:paper.tex:refs.bib"
    "07-closure-cross-substrate:$SL/closure_cross_substrate/paper:main.tex:refs.bib"
    "08-trauma-cortical-closure:$SL/005-vfd-trauma-cortical-closure/paper:main.tex:refs.bib"
    "09-flow-cortical-closure:$SL/006-vfd-flow-cortical-closure/paper:main.tex:refs.bib"
    "10-hyperscanning-joint-meaning:$SL/007-vfd-hyperscanning-joint-meaning/paper:main.tex:refs.bib"
)

run() {
    if $DRY_RUN; then
        echo "  [dry-run] $*"
    else
        "$@"
    fi
}

for entry in "${PAPERS[@]}"; do
    IFS=':' read -r ws src tex bib <<< "$entry"
    target="$BUNDLE_ROOT/papers/$ws"
    if [ ! -d "$src" ]; then
        echo "[skip] source missing: $src"
        continue
    fi
    echo "=== $ws ==="
    run mkdir -p "$target"
    [ -f "$src/$tex" ] && run cp "$src/$tex" "$target/main.tex"
    [ -f "$src/$bib" ] && run cp "$src/$bib" "$target/references.bib"
    if [ -f "$src/${tex%.tex}.pdf" ]; then
        run cp "$src/${tex%.tex}.pdf" "$target/main.pdf"
    elif [ -f "$src/main.pdf" ]; then
        run cp "$src/main.pdf" "$target/main.pdf"
    fi
    [ -d "$src/figures" ] && run cp -r "$src/figures" "$target/"
    # For existence-programme papers, also sync repro/
    [ -d "$src/repro" ] && run cp -r "$src/repro" "$target/"
done

echo
echo "Done."
