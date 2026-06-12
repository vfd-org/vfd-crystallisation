# Note E — FlowIndex (Flow Cortical Closure)

## Abstract

Composite cortical closure index for flow states, operationalising the four-condition flow claim of Paper II §13.3. Synthetic-implementation validation 5/5. NO REAL-DATA PASS YET. Two completed open-data applications returned diagnostic-correctly-predicted FAILs: ds005520 MOBA gaming (FAIL on D_5; FlowIndex d_z=-0.26 confirmed FAIL); ds004505 table tennis (FAIL on D_5; FlowIndex d_z=+0.06 confirmed FAIL). Music-performance and esports-professional EEG remain the appropriate next experiments.

## Files

- `note.pdf` — the compiled PDF (latest build).
- `source/main.tex` — LaTeX source.
- `source/references.bib` — bibliography.
- `figures/` — figures embedded in the paper.
- `repro/` — reproducibility scripts.

## Reproducibility

Scripts:

- `repro/synthetic_flow_demo.py — FlowIndex synthetic validation (5/5)`
- `repro/run_ds005520.py — MOBA gaming diagnostic-predicted FAIL`
- `repro/run_ds004505.py — table tennis diagnostic-predicted FAIL`

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
