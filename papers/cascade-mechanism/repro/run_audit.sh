#!/usr/bin/env bash
# cascade-mechanism repro audit
#
# Re-runs both load-bearing scripts (Appendix A and Appendix E of the
# paper) from a clean working tree, captures their output, and diffs
# against the frozen reference outputs in expected_outputs/.
#
# Usage:
#   bash run_audit.sh                # standard audit (diff against frozen refs)
#   bash run_audit.sh --refresh-expected   # regenerate expected_outputs/ from
#                                          # current run; do this only when the
#                                          # underlying scripts have changed in
#                                          # an intended, reviewed way.

set -euo pipefail

REPRO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$REPRO_DIR/../../.." && pwd)"
OUT_DIR="$REPRO_DIR/output"
EXPECTED_DIR="$REPRO_DIR/expected_outputs"

mkdir -p "$OUT_DIR"

REFRESH=0
if [[ "${1:-}" == "--refresh-expected" ]]; then
  REFRESH=1
  echo "[mode] --refresh-expected: will overwrite frozen reference outputs."
  echo "[mode] only do this when the scripts have changed in a reviewed way."
  echo ""
fi

run_one () {
  local label="$1"
  local script="$2"
  local outfile="$3"

  echo "[run] $label"
  echo "[run]   script: $script"
  echo "[run]   output: $outfile"
  ( cd "$REPO_ROOT" && python3 "$script" ) > "$outfile" 2>&1
  echo "[run]   ok"
}

# Appendix A — σ-attractor spectrum
run_one \
  "Appendix A: sigma-attractor spectrum" \
  "papers/cascade-derivation/scripts/test_sigma_attractor_spectrum.py" \
  "$OUT_DIR/appendix_A_sigma_attractor.txt"

# Appendix E — closure kernel
run_one \
  "Appendix E: closure kernel" \
  "papers/aria-closure-kernel/repro/verify_kernel.py" \
  "$OUT_DIR/appendix_E_closure_kernel.txt"

# verify_kernel.py also writes papers/aria-closure-kernel/repro/results.json
# Copy that into our output/ so the bundle is self-contained.
cp "$REPO_ROOT/papers/aria-closure-kernel/repro/results.json" \
   "$OUT_DIR/appendix_E_closure_kernel_results.json"

echo ""
echo "[diff] comparing live output against frozen expected_outputs/"

if [[ "$REFRESH" -eq 1 ]]; then
  mkdir -p "$EXPECTED_DIR"
  cp "$OUT_DIR/appendix_A_sigma_attractor.txt"          "$EXPECTED_DIR/"
  cp "$OUT_DIR/appendix_E_closure_kernel.txt"            "$EXPECTED_DIR/"
  cp "$OUT_DIR/appendix_E_closure_kernel_results.json"   "$EXPECTED_DIR/"
  echo "[diff] expected_outputs/ refreshed from this run."
  echo ""
  echo "AUDIT REFRESHED — frozen reference outputs now match the latest run."
  exit 0
fi

if [[ ! -d "$EXPECTED_DIR" ]] || [[ -z "$(ls -A "$EXPECTED_DIR" 2>/dev/null)" ]]; then
  echo "[diff] expected_outputs/ is empty."
  echo "[diff] run 'bash run_audit.sh --refresh-expected' once to seed it."
  exit 2
fi

DIFF_FAILED=0

diff_one () {
  local name="$1"
  local live="$OUT_DIR/$name"
  local expected="$EXPECTED_DIR/$name"
  if [[ ! -f "$expected" ]]; then
    echo "[diff]   $name: expected file missing in expected_outputs/"
    DIFF_FAILED=1
    return
  fi
  if diff -q "$expected" "$live" > /dev/null 2>&1; then
    echo "[diff]   $name: OK"
  else
    echo "[diff]   $name: MISMATCH"
    echo "[diff]     show with: diff $expected $live"
    DIFF_FAILED=1
  fi
}

diff_one "appendix_A_sigma_attractor.txt"
diff_one "appendix_E_closure_kernel.txt"
diff_one "appendix_E_closure_kernel_results.json"

echo ""
if [[ "$DIFF_FAILED" -eq 1 ]]; then
  echo "AUDIT FAILED — see [diff] lines above for which file mismatched."
  echo "If the divergence is a known/intended change, re-seed with:"
  echo "  bash run_audit.sh --refresh-expected"
  exit 1
fi

echo "AUDIT PASSED — both scripts reproduce frozen reference outputs."
