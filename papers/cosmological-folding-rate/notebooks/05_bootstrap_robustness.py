"""Notebook 05 — bootstrap robustness on the active dataset.

Resamples the data 500 times and reports the distribution of (A, θ) for
VFD-A and (A, z0, σ) for VFD-B.
"""
from __future__ import annotations

import os
import sys

from _pipeline import DATA_PROC_DIR, FIG_DIR, TABLE_DIR, stamp, write_csv
from src.bootstrap import bootstrap_fit, summarise
from src.data_loader import load_hz
from src.fitting import fit_vfd_phi_log, fit_vfd_seven_fold


def main() -> None:
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(DATA_PROC_DIR, "synthetic_lcdm.csv")
    if not os.path.exists(target):
        raise SystemExit(f"dataset not found: {target}")
    z, H, sH, _ = load_hz(target)
    stamp(f"bootstrapping on {target}, n={len(z)}")

    boot_a = bootstrap_fit(fit_vfd_phi_log, z, H, sH, n_boot=500, seed=1, track=("A", "theta"))
    boot_b = bootstrap_fit(fit_vfd_seven_fold, z, H, sH, n_boot=500, seed=2, track=("A", "z0", "sigma"))

    rows = []
    for model, boot in (("VFD-A", boot_a), ("VFD-B", boot_b)):
        for param, samples in boot.items():
            if param in ("failures",):
                continue
            s = summarise(samples)
            rows.append({"model": model, "param": param, **s})

    out = os.path.join(TABLE_DIR, "bootstrap.csv")
    write_csv(out, rows)
    stamp(f"wrote {out}")
    for r in rows:
        print(" ", r)


if __name__ == "__main__":
    main()
