# Note B — Cortical Phase Closure

## Abstract

Strongest current empirical cortical anchor. OpenNeuro ds005620 propofol (n=14, 14/14 positive, t=7.11, d_z=1.90); sLORETA source-localised replication (14/14, t=9.72, d_z=2.60); cross-cohort ds004541 (7/7, t=5.25, d_z=1.98 in-sample; d_z=1.16 LOSO). 9-feature closure feature vector over multi-band cortical phase graphs. Scope note: does NOT claim to detect consciousness directly.

## Files

- `note.pdf` — the compiled PDF (latest build).
- `source/main.tex` — LaTeX source.
- `source/references.bib` — bibliography.
- `figures/` — figures embedded in the paper.
- `repro/` — reproducibility scripts.

## Reproducibility

Scripts:

- `repro/run_ds005620.py — propofol headline analysis`
- `repro/run_ds004541.py — clinical anaesthesia replication`
- `repro/synthetic_pipeline_demo.py — feature-vector computation smoke`

Run smoke tests at seed 42:

```bash
python repro/<script>.py
```

For real-data analyses, see `../../repro/shared/data_access.md`.

## Status

This document is part of the Existence / Life / Closure Programme
review packet (v1.0.0-rc1, pre-peer-review). Conventions:

- Theorem / Conditional Proposition / Empirical Result / Empirical Proxy / Pre-registered Proposal taxonomy.
- Two τ conventions (τ_ico vs τ_spec) documented in Paper I appendix.
- CAD-D1–D5-v1 applicability diagnostic from Note C scopes empirical proxies.

## Citation

See `../../CITATION.cff` for citation metadata.

## Licence

- Prose / figures: CC BY 4.0.
- Code in `repro/`: Apache-2.0.
