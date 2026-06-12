# Paper I — Existence as Closure

## Abstract

Formal foundation: distinction, relation, closure operator $C_\varphi = L_{V_{600}} + \varphi^{-2} I$ on the 600-cell substrate, σ-twist τ, bounded reference frames, per-frame zero-line $\Sigma_\mathcal{I}$, joint frames, complexity hierarchy, recursion-depth bound. Includes the τ-conventions appendix (τ_ico vs τ_spec) and the 10-paper programme map.

## Files

- `paper.pdf` — the compiled PDF (latest build).
- `source/main.tex` — LaTeX source.
- `source/references.bib` — bibliography.
- `figures/` — figures embedded in the paper.
- `repro/` — reproducibility scripts.

## Reproducibility

Scripts:

- `repro/closure_demo.py — D1–D8 substrate facts on V_600`
- `repro/rung_tower_demo.py — C1 cascade rung tower (E_8, H_4, D_4), standalone reproducibility artifact`

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
