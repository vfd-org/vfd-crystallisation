# Note A — Bioelectric Closure

## Abstract

Empirical-methods note implementing the Levin bridge of Paper III §3. BETSE planarian-shape simulation panel, R_cl 5-term residual, default-weights cross-validation. Includes 5 preregistered DiBAC4(3) wet-lab predictions. The 2-second BETSE substrate is Tier C under the CAD diagnostic of Note C; wet-lab planarian work is the future evidence.

## Files

- `note.pdf` — the compiled PDF (latest build).
- `source/main.tex` — LaTeX source.
- `source/references.bib` — bibliography.
- `figures/` — figures embedded in the paper.
- `repro/` — reproducibility scripts.

## Reproducibility

Scripts:

- `repro/synthetic_demo.py — synthetic regeneration outcome classification`
- `repro/run_betse_panel.py — multi-replicate BETSE panel (requires BETSE)`

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
