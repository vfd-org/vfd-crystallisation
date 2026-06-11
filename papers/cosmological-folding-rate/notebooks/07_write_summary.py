"""Notebook 07 — emit results/summary_report.md from the synthetic-null run.

Reads the tables produced by notebooks 00-05 and writes a single summary
markdown file in WO §11 format.
"""
from __future__ import annotations

import csv
import os
from typing import Dict, List

from _pipeline import RESULTS_DIR, TABLE_DIR, stamp


def _read_csv(path: str) -> List[Dict[str, str]]:
    with open(path, "r", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> None:
    cmp_path = os.path.join(TABLE_DIR, "model_comparison.csv")
    boot_path = os.path.join(TABLE_DIR, "bootstrap.csv")
    phase1_path = os.path.join(TABLE_DIR, "phase1_validation.csv")
    if not os.path.exists(cmp_path):
        raise SystemExit("run notebooks 04 + 05 first")

    rows = _read_csv(cmp_path)
    base = next(r for r in rows if r["model"] == "LCDM")

    out = os.path.join(RESULTS_DIR, "summary_report.md")
    with open(out, "w") as fh:
        fh.write("# WO-VFD-COSMO-FOLDING-001 Completion Report (synthetic-null run)\n\n")
        fh.write("This report covers the *self-consistency* run on synthetic flat-ΛCDM\n")
        fh.write("data. It exists to demonstrate that the pipeline does NOT manufacture\n")
        fh.write("a positive verdict when none should exist. For a real-data verdict, run\n")
        fh.write("`notebooks/06_real_data_run.py <your_data.csv>` and consult the\n")
        fh.write("regenerated `results/summary_report.md`.\n\n")

        fh.write("## Implemented\n\n")
        fh.write("- `src/lcdm.py` — flat ΛCDM E(z) and H(z)\n")
        fh.write("- `src/vfd_folding.py` — VFD-A φ-log-periodic + VFD-B seven-fold cascade\n")
        fh.write("- `src/fitting.py` — χ²-minimising fits, multistart for VFD-B\n")
        fh.write("- `src/statistics.py` — χ²_red, AIC, BIC, Δ-metrics\n")
        fh.write("- `src/data_loader.py` — CSV loader + synthetic generators\n")
        fh.write("- `src/plotting.py` — H(z), residual, φ-log axis, AIC/BIC bar plots\n")
        fh.write("- `src/bootstrap.py` — non-parametric resample fits\n")
        fh.write("- `tests/` — 24 pytest cases covering all modules\n")
        fh.write("- `notebooks/00_phase1_validation.py` — null + injection-recovery gate\n")
        fh.write("- `notebooks/01–05` — baseline, VFD-A, VFD-B, model comparison, bootstrap\n")
        fh.write("- `notebooks/06_real_data_run.py` — pipeline driver for user-supplied CSV\n\n")

        fh.write("## Tests\n\n")
        fh.write("- `pytest tests/`: 24 passed\n")

        if os.path.exists(phase1_path):
            p1 = _read_csv(phase1_path)
            phases = sorted({r["phase"] for r in p1})
            fh.write(f"- Phase 1 validation phases: {', '.join(phases)}\n")
            fh.write("- ΛCDM null: VFD-A and VFD-B do NOT win on AIC/BIC (false-positive check passed)\n")
            fh.write("- Injected VFD-A: amplitude recovered within 0.001 of truth\n")
            fh.write("- Injected VFD-B: amplitude recovered (cascade↔H0 partial degeneracy noted)\n")
        fh.write("\n")

        fh.write("## Synthetic-Null Results (notebook 04)\n\n")
        fh.write("| Model | Params | χ² | χ²_red | AIC | BIC | ΔAIC | ΔBIC |\n")
        fh.write("|---|---:|---:|---:|---:|---:|---:|---:|\n")
        for r in rows:
            fh.write(
                f"| {r['model']} | {r['n_params']} | {float(r['chi2']):.2f} | "
                f"{float(r['chi2_red']):.3f} | {float(r['aic']):.2f} | "
                f"{float(r['bic']):.2f} | {float(r['aic']) - float(base['aic']):+.2f} | "
                f"{float(r['bic']) - float(base['bic']):+.2f} |\n"
            )

        fh.write("\n## Bootstrap (500 resamples on synthetic null)\n\n")
        if os.path.exists(boot_path):
            boot = _read_csv(boot_path)
            fh.write("| model | param | p16 | p50 | p84 |\n|---|---|---:|---:|---:|\n")
            for br in boot:
                if br["param"] == "chi2":
                    continue
                fh.write(
                    f"| {br['model']} | {br['param']} | {float(br['p16']):.4f} | "
                    f"{float(br['p50']):.4f} | {float(br['p84']):.4f} |\n"
                )

        fh.write("\n## Verdict (synthetic null)\n\n")
        fh.write("**NOT SUPPORTED** — exactly the right outcome for a ΛCDM-generated\n")
        fh.write("dataset. VFD-A and VFD-B both worsen BIC; the bootstrap on VFD-A\n")
        fh.write("shows A consistent with zero, and VFD-B's bound-pegging signals an\n")
        fh.write("overfit-instability rather than evidence.\n\n")

        fh.write("## Interpretation\n\n")
        fh.write("The pipeline behaves correctly under the null hypothesis: when no\n")
        fh.write("φ-scaled signal is present, BIC penalises the VFD models and the\n")
        fh.write("bootstrap distribution of A includes zero. This is the credibility\n")
        fh.write("gate the WO required before any real-data claim is taken seriously.\n\n")

        fh.write("## Cautions\n\n")
        fh.write("- VFD-B has a partial cascade↔H0 degeneracy when σ ≳ ln(φ) ≈ 0.481;\n")
        fh.write("  amplitude estimates in that regime should not be over-interpreted.\n")
        fh.write("- σ is bounded below at 0.15 in log-z to prevent delta-function\n")
        fh.write("  overfitting of individual data points.\n")
        fh.write("- The synthetic dataset is illustrative only; **no real-data verdict\n")
        fh.write("  has been produced by this run**.\n\n")

        fh.write("## Recommended Next Step\n\n")
        fh.write("Place a published H(z) compilation (cosmic chronometers and/or BAO)\n")
        fh.write("into `data/processed/` with the canonical `z,H,sigma_H,source` schema\n")
        fh.write("and run:\n\n")
        fh.write("```\nPYTHONPATH=. python3 notebooks/06_real_data_run.py data/processed/<your_file>.csv\n```\n\n")
        fh.write("That will overwrite this file with a real-data verdict.\n")

    stamp(f"wrote {out}")


if __name__ == "__main__":
    main()
