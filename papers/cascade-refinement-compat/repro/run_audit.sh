#!/usr/bin/env bash
# cascade-refinement-compat audit
#
# Re-runs the load-bearing exploration script and diffs against frozen
# expected outputs.

set -euo pipefail

REPRO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PAPER_DIR="$(cd "$REPRO_DIR/.." && pwd)"
REPO_ROOT="$(cd "$PAPER_DIR/../.." && pwd)"
OUT_DIR="$REPRO_DIR/output"
EXPECTED_DIR="$REPRO_DIR/expected_outputs"

mkdir -p "$OUT_DIR"

REFRESH=0
if [[ "${1:-}" == "--refresh-expected" ]]; then
  REFRESH=1
  echo "[mode] --refresh-expected: will overwrite frozen reference outputs."
  echo ""
fi

echo "[run] explore_defect.py (Schur-complement halving on Towers I and II)"
( cd "$REPO_ROOT" && python3 papers/cascade-refinement-compat/scripts/explore_defect.py ) \
    > "$OUT_DIR/explore_defect.txt" 2>&1
echo "[run]   ok"

echo ""
echo "[diff] comparing live output against frozen expected_outputs/"

if [[ "$REFRESH" -eq 1 ]]; then
  mkdir -p "$EXPECTED_DIR"
  cp "$OUT_DIR/explore_defect.txt" "$EXPECTED_DIR/"
  echo "[diff] expected_outputs/ refreshed."
  echo ""
  echo "REFINEMENT COMPAT AUDIT REFRESHED"
  exit 0
fi

if [[ ! -f "$EXPECTED_DIR/explore_defect.txt" ]]; then
  echo "[diff] expected_outputs/explore_defect.txt missing."
  echo "[diff] run 'bash run_audit.sh --refresh-expected' once to seed it."
  exit 2
fi

if diff -q "$EXPECTED_DIR/explore_defect.txt" "$OUT_DIR/explore_defect.txt" > /dev/null 2>&1; then
  echo "[diff]   explore_defect.txt: OK"
  echo ""
  echo "REFINEMENT COMPAT AUDIT PASSED"
  exit 0
else
  echo "[diff]   explore_defect.txt: MISMATCH"
  echo "[diff]   show with: diff $EXPECTED_DIR/explore_defect.txt $OUT_DIR/explore_defect.txt"
  echo ""
  echo "REFINEMENT COMPAT AUDIT FAILED"
  exit 1
fi
