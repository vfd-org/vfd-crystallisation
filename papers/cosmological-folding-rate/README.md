# Cosmological Folding Rate (WO-VFD-COSMO-FOLDING-001)

Falsification-first test of whether cosmic expansion H(z) contains
statistically defensible φ-scaled or seven-fold-cascade residual
structure relative to ΛCDM.

This module is **exploratory**. It does not claim to derive cosmology
from VFD. It only asks: once flat ΛCDM has done its job, does what is
left over carry a φ-shaped rhythm strong enough to survive AIC/BIC
penalties and bootstrap resampling?

The hypothesis frame, models, and reporting rules follow
`WO-VFD-COSMO-FOLDING-001` (this README's source).

## Layout

```
papers/cosmological-folding-rate/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/                  # drop public H(z) compilations here
│   ├── processed/            # cleaned CSVs used by the pipeline
│   └── README.md             # documents formats + sources
├── src/
│   ├── constants.py
│   ├── data_loader.py
│   ├── lcdm.py
│   ├── vfd_folding.py
│   ├── fitting.py
│   ├── statistics.py
│   └── plotting.py
├── tests/                    # pytest
├── notebooks/                # runnable .py scripts (no kernel needed)
│   ├── 01_lcdm_baseline.py
│   ├── 02_phi_log_periodic_residuals.py
│   ├── 03_seven_fold_cascade_model.py
│   └── 04_model_comparison.py
└── results/
    ├── figures/
    ├── tables/
    └── summary_report.md
```

## Models tested

- **ΛCDM** — flat, with Ω_m, Ω_r, H0.
- **VFD-A** — `H_ΛCDM · (1 + A · sin(2π · ln(1+z)/ln φ + θ))`.
- **VFD-B** — `H_ΛCDM · (1 + A · C7(z))` with seven φ-spaced log-z
  Gaussian centres.

## Quickstart

```bash
cd papers/cosmological-folding-rate
pip install -r requirements.txt
PYTHONPATH=. pytest tests/             # run unit + integration tests
PYTHONPATH=. python notebooks/01_lcdm_baseline.py
PYTHONPATH=. python notebooks/02_phi_log_periodic_residuals.py
PYTHONPATH=. python notebooks/03_seven_fold_cascade_model.py
PYTHONPATH=. python notebooks/04_model_comparison.py
```

A bundled run script `run.sh` performs all of the above and writes the
verdict into `results/summary_report.md`.

## Verdict criteria

Outcomes are reported as one of:

```
SUPPORTED         BIC improvement > 10, stable under bootstrap, repeats across datasets
WEAKLY SUGGESTIVE χ²/AIC improve, BIC does not, parameters not robust enough
INCONCLUSIVE      small improvement comparable to overfit risk
NOT SUPPORTED     no improvement, or worse AIC/BIC
FAILED            implementation/data quality invalidates the test
```

## Honest framing

The question is not *"can we force a φ-pattern into cosmology?"* — that
is always trivially yes with enough parameters. The question is whether
the data actually wants the extra structure once parameter penalties are
applied. If it does not, the report says so.
