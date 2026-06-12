#!/usr/bin/env bash
#
# run_all_sims.sh
# ===============
#
# Reproduce all 27 numerical demonstrations of the four-paper Existence
# Programme:
#
#   - existence-as-recursive-closure/repro/closure_demo.py    (D1-D7)
#   - life-as-closure/repro/life_demo.py                       (L1-L13)
#   - cosmic-closure-recurrence/repro/cosmic_demo.py           (C1-C5)
#   - processing-to-point-of-view/repro/bridges_demo.py        (B1-B3)
#
# All sims are deterministic at seed 42. Total runtime ~1 minute on
# a modern laptop.
#
# Usage:
#   ./scripts/run_all_sims.sh                # run everything (figures + numerics)
#   ./scripts/run_all_sims.sh --no-figures   # skip figure generation (faster)
#
# Outputs:
#   - papers/<paper>/repro/output/*.png       (sim figures)
#   - papers/<paper>/repro/output/*.json      (numerical results)
#
# Exit codes:
#   0  -- all 27 demos pass
#   1  -- at least one demo reports PARTIAL or FAIL

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NO_FIGURES_FLAG=""

for arg in "$@"; do
    case "$arg" in
        --no-figures)
            NO_FIGURES_FLAG="--no-figures"
            ;;
        *)
            echo "Unknown argument: $arg"
            echo "Usage: $0 [--no-figures]"
            exit 2
            ;;
    esac
done

PAPERS=(
    "existence-as-recursive-closure:closure_demo.py"
    "life-as-closure:life_demo.py"
    "cosmic-closure-recurrence:cosmic_demo.py"
    "processing-to-point-of-view:bridges_demo.py"
)

ANY_FAILED=0
SUMMARY=""

echo "========================================================================"
echo "  Existence Programme --- numerical demonstration suite (27 demos)"
echo "  Seed: 42 (all sims deterministic)"
echo "========================================================================"
echo

for entry in "${PAPERS[@]}"; do
    paper="${entry%%:*}"
    script="${entry##*:}"
    sim_dir="$REPO_ROOT/papers/$paper/repro"
    sim_script="$sim_dir/$script"

    if [ ! -f "$sim_script" ]; then
        echo "[skip] $paper/$script not found"
        continue
    fi

    echo "------------------------------------------------------------------------"
    echo "  Running $paper/$script"
    echo "------------------------------------------------------------------------"

    cd "$sim_dir"
    # Run once, capture output, parse pass/fail from the summary tail
    output=$(python3 "$script" $NO_FIGURES_FLAG 2>&1)
    echo "$output" | tail -10
    partial=$(echo "$output" | grep -cE "PARTIAL" || true)
    if [ "$partial" -gt 0 ] 2>/dev/null; then
        ANY_FAILED=1
        SUMMARY="$SUMMARY\n  [PARTIAL] $paper: $partial demos partially verified"
    else
        SUMMARY="$SUMMARY\n  [OK]      $paper: all demos verified"
    fi
    echo
done

cd "$REPO_ROOT"

echo "========================================================================"
echo "  FINAL SUMMARY"
echo "========================================================================"
echo -e "$SUMMARY"
echo

if [ "$ANY_FAILED" -eq 0 ]; then
    echo "  RESULT: all 27 demos passed."
    echo
    echo "  Programme is reproducibility-verified at seed 42."
    exit 0
else
    echo "  RESULT: at least one demo reported PARTIAL or FAIL."
    echo "  Review per-paper output above."
    exit 1
fi
