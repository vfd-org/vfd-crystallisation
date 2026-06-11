#!/usr/bin/env bash
# Full pipeline runner for WO-VFD-COSMO-FOLDING-001.
#
# usage:
#   ./run.sh                                # synthetic-null run
#   ./run.sh data/processed/your_file.csv   # real-data run

set -euo pipefail
cd "$(dirname "$0")"
export PYTHONPATH=.

echo "==> pytest"
python3 -m pytest tests/ -q

echo "==> phase 1 validation"
python3 notebooks/00_phase1_validation.py

echo "==> notebook 01: ΛCDM baseline"
python3 notebooks/01_lcdm_baseline.py

echo "==> notebook 02: VFD-A φ-log-periodic"
python3 notebooks/02_phi_log_periodic_residuals.py

echo "==> notebook 03: VFD-B seven-fold"
python3 notebooks/03_seven_fold_cascade_model.py

echo "==> notebook 04: model comparison"
python3 notebooks/04_model_comparison.py

if [ "$#" -ge 1 ]; then
  DATA="$1"
  echo "==> notebook 06: real-data run on ${DATA}"
  python3 notebooks/06_real_data_run.py "$DATA"
else
  echo "==> notebook 05: bootstrap on synthetic null"
  python3 notebooks/05_bootstrap_robustness.py
  echo "==> writing synthetic-null summary report"
  python3 notebooks/07_write_summary.py
fi
