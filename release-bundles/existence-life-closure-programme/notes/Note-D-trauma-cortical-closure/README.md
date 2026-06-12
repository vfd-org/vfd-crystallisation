# Note D — Trauma / Cortical Closure

## Abstract

Cortical closure residual (CCR) as a first-order proxy for chronic functional dyscoherence. Real-data anchors: ds007609 trait anxiety (n=24, d=+0.79); ds004315 mood manipulation (n=50, d=+0.70). Cross-cohort replication is acute mood, NOT trauma; PTSD pre/post-therapy longitudinal EEG remains the gold-standard external validation. Dementia null on ds004504 scopes the framework: CCR tracks functional dyscoherence, not structural neurodegeneration.

## Files

- `note.pdf` — the compiled PDF (latest build).
- `source/main.tex` — LaTeX source.
- `source/references.bib` — bibliography.
- `figures/` — figures embedded in the paper.
- `repro/` — reproducibility scripts.

## Reproducibility

Scripts:

- `repro/run_ds007609.py — trait-anxiety headline analysis`
- `repro/run_ds004315.py — mood manipulation cross-application`
- `repro/synthetic_trauma_eeg.py — synthetic-data demo`

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
