# Changelog

## [1.0.0-rc1] — 2026-05-29

Initial public release.

### Paper

**Title:** *The Translation Layer: Polytope Overlap as the
Empirical Grammar of the V₆₀₀ Substrate, with Dictionary and
Translation Rules.*

**Sections:**

- §1 The translation problem
- §2 Three layers (dictionary, grammar, interpretation)
- §3 The closure transformation engine
- §4 The dictionary
- §5 Polytope overlap as grammar
  - §5.1 Schläfli decomposition (5 engine certificates)
  - §5.2 λ=12 lift theorem
  - §5.3 λ=12 uniqueness scan (negative rule)
  - §5.4 Transformation kinds as legal moves (12 kinds)
  - §5.5 Admissibility classes as well-formedness (5 classes)
  - §5.6 Transition rules as composition
- §6 Translation rules with three worked examples
- §7 Expressive scope: what the substrate can and cannot say
- §8 Compositionality via closure_ai and min_aria
- §9 Comparison to other mathematical languages
- §10 Open translation problems
- §11 Conclusion
- Appendix A — dictionary table
- Appendix B — grammar table
- Appendix C — translation table
- Appendix D — engine reproducibility map

### Data (canonical artefacts)

- `data/dictionary.csv` — 14 typed substrate→referent entries
- `data/grammar.csv` — 15 grammar rules (12 transformation kinds +
  3 derived: Schläfli decomposition, λ=12 lift, λ=12 uniqueness
  scan)
- `data/translation.csv` — 14 worked translations

### Docs

- `docs/codex_review_prompt.md` — hostile-review prompt with 7
  language-argument failure modes
- `docs/engine_pointer.md` — module-by-module pointer to the
  engine in `tranformation-engine/`

### Scope discipline

- Pre-peer-review open research preprint; not independently
  validated.
- No claim of physical, biological, or cognitive derivation.
- All Layer-3 translations conditional on named bridge hypotheses.
- λ=12 uniqueness scan is empirical-on-test-set, not
  theorem-grade.

### Companion bundles

This bundle complements:

- `vfd-org/icosian-triad-v600` (math anchor for substrate)
- `vfd-org/closure-picture` (programme-wide interpretive synthesis)
- `release-bundles/evidence-ledger` (audit framework)
