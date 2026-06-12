#!/usr/bin/env bash
#
# sync_to_sources.sh
# ==================
#
# Push refinement edits from this workspace BACK to source-of-truth
# locations. Use when refinement work in the workspace is ready to be
# merged into the original repos.
#
# Usage:
#   ./scripts/sync_to_sources.sh           # push all 10 papers
#   ./scripts/sync_to_sources.sh --dry-run # show what would be copied
#   ./scripts/sync_to_sources.sh --paper 02-life-as-closure   # push just one
#
# SAFETY: this overwrites the source-of-truth files. Make sure your
# workspace edits are intended and committed somewhere (git, backup, etc).
#
# Source locations (mirror of sync_from_sources.sh):
#   01-04  -- vfd-crystalisation-paper/papers/<slug>/
#   05-10  -- solution-lab/experiments/<slug>/paper/

set -e

DRY_RUN=false
ONLY_PAPER=""
for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=true ;;
        --paper) shift; ONLY_PAPER="$1" ;;
        *) ;;
    esac
done

BUNDLE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CRYST="$BUNDLE_ROOT/../../papers"
SL="$(cd "$BUNDLE_ROOT/../../../solution-lab/experiments" 2>/dev/null && pwd)"

if [ -z "$SL" ]; then
    echo "ERROR: solution-lab not found."
    exit 1
fi

# Reverse mapping
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

echo "PUSHING workspace edits to source-of-truth locations"
$DRY_RUN && echo "(DRY RUN — no changes will be made)"
echo

for entry in "${PAPERS[@]}"; do
    IFS=':' read -r ws src tex bib <<< "$entry"
    if [ -n "$ONLY_PAPER" ] && [ "$ws" != "$ONLY_PAPER" ]; then continue; fi
    source="$BUNDLE_ROOT/papers/$ws"
    if [ ! -d "$source" ]; then
        echo "[skip] workspace dir missing: $source"
        continue
    fi
    if [ ! -d "$src" ]; then
        echo "[skip] source dir missing: $src"
        continue
    fi
    echo "=== $ws -> $src ==="
    [ -f "$source/main.tex" ] && run cp "$source/main.tex" "$src/$tex"
    [ -f "$source/references.bib" ] && run cp "$source/references.bib" "$src/$bib"
done

echo
echo "Done."
