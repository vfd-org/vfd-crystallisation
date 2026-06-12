#!/usr/bin/env bash
#
# build_all_papers.sh
# ===================
#
# Compile all 10 papers in the unified refinement workspace.
# Requires `tectonic` on PATH.
#
# Usage:
#   ./scripts/build_all_papers.sh                       # build all 10
#   ./scripts/build_all_papers.sh --paper 02-life       # build just one
#   ./scripts/build_all_papers.sh --check               # report status without recompiling

set -e

ONLY_PAPER=""
CHECK_ONLY=false
for arg in "$@"; do
    case "$arg" in
        --paper) shift; ONLY_PAPER="$1" ;;
        --check) CHECK_ONLY=true ;;
        *) ;;
    esac
done

BUNDLE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PAPERS_DIR="$BUNDLE_ROOT/papers"

if [ ! -d "$PAPERS_DIR" ]; then
    echo "ERROR: papers/ directory not found"; exit 1
fi

declare -i ok=0 fail=0
for paper_dir in "$PAPERS_DIR"/*/; do
    paper=$(basename "$paper_dir")
    if [ -n "$ONLY_PAPER" ] && [[ "$paper" != *"$ONLY_PAPER"* ]]; then continue; fi
    if [ ! -f "$paper_dir/main.tex" ]; then
        echo "[skip] $paper (no main.tex)"; continue
    fi

    echo "=== $paper ==="
    if $CHECK_ONLY; then
        if [ -f "$paper_dir/main.pdf" ]; then
            pages=$(python3 -c "
import re, zlib
with open('$paper_dir/main.pdf','rb') as f: data = f.read()
found = 0
for m in re.finditer(rb'stream\s*\n(.+?)\nendstream', data, re.DOTALL):
    try:
        decomp = zlib.decompress(m.group(1))
        found += len(re.findall(rb'/Type\s*/Page(?!s)', decomp))
    except: pass
found += len(re.findall(rb'/Type\s*/Page(?!s)', data))
print(found)
" 2>/dev/null || echo "?")
            echo "  PDF present: $pages pages"
            ok=$((ok+1))
        else
            echo "  [no PDF yet]"
            fail=$((fail+1))
        fi
    else
        (cd "$paper_dir" && tectonic main.tex 2>&1 | grep -E "Writing|error:" | head -3) && {
            ok=$((ok+1))
        } || {
            fail=$((fail+1))
        }
    fi
    echo
done

echo "============================================"
echo "Summary: $ok OK / $fail failed"
echo "============================================"
exit $((fail > 0 ? 1 : 0))
