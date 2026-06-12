# Note F — Dyadic Joint Meaning

## Abstract

Hyperscanning closure residual as a first-order empirical proxy for joint meaning. Formal $\delta_{AB} = |\mathcal{X}_{AB}|$ (Paper I §8 / Paper II §10) vs empirical $\widehat{\delta}_{AB}^{\mathrm{EEG}}$ (this note) are notationally distinct. Real-data results: ds007471 musical joint-action HONEST NEGATIVE (d_z=+0.23, p=0.43, CAD predicted FAIL a priori); ds006802 collaborative rule-learning EXPLORATORY MODERATE-POSITIVE TREND (d_z=+0.39, p=0.071, below preregistered confirming threshold). Conversational hyperscanning remains the appropriate next test.

## Files

- `note.pdf` — the compiled PDF (latest build).
- `source/main.tex` — LaTeX source.
- `source/references.bib` — bibliography.
- `figures/` — figures embedded in the paper.
- `repro/` — reproducibility scripts.

## Reproducibility

Scripts:

- `repro/synthetic_dyad_demo.py — synthetic dyad-level validation`
- `repro/run_ds007471.py — musical hyperscanning honest negative`
- `repro/run_ds006802.py — collaborative rule-learning exploratory`

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
