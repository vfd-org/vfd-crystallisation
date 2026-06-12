# Note C — Closure-as-Distance

## Abstract

Empirical-methods methodology note. Defines closure-as-distance as a measurable first-order proxy for distance-to-closure-stable-reference. Introduces the CAD-D1–D5-v1 applicability diagnostic (anisotropy, multi-feature consistency, subject-level coherence, mechanism complementarity, feature minimality). 15/16 substrates correctly classified; FTD false positive transparently disclosed. RNN training rows are CAD-FAIL calibration-boundary cases.

## Files

- `note.pdf` — the compiled PDF (latest build).
- `source/main.tex` — LaTeX source.
- `source/references.bib` — bibliography.
- `figures/` — figures embedded in the paper.
- `repro/` — reproducibility scripts.

## Reproducibility

Scripts:

- `repro/strict_vs_passleaning_audit.py — strict-PASS vs PASS-leaning classification audit`
- `repro/run_ds004504.py — Alzheimer's / FTD diagnostic check`
- `repro/synthetic_controls.py — negative-control validation`

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
