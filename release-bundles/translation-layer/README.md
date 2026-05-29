# The Translation Layer

**Polytope Overlap as the Empirical Grammar of the V₆₀₀ Substrate,
with Dictionary and Translation Rules**

This bundle is the paper that makes the "math as language" claim
concrete. It argues — and empirically exhibits — that the V₆₀₀
substrate has crossed the threshold from metaphor to formal
language: it has a typed dictionary, a decidable grammar driven by
polytope overlap, and translation rules into the interpretive
layer.

The grammar is not declarative. It is exhibited by the **closure
transformation engine**, a computational pipeline that returns
admissibility verdicts on proposed transformations. Three engine
results in particular pin the grammar down concretely:

1. The **Schläfli decomposition**:
   V₆₀₀ = C₀ ⊔ C₁ ⊔ C₂ ⊔ C₃ ⊔ C₄ into 5 cosets of 2T, each
   isomorphic to a 24-cell, with A₅ acting faithfully on the coset
   index. Five reproducible certificates.
2. The **λ=12 lift theorem**: every per-coset 24-cell λ=12
   eigenvector extends to a V₆₀₀ Laplacian λ=12 eigenvector. 10-dim
   lifted subspace inside 25-dim E₆₀₀(12). A positive grammar rule.
3. The **λ=12 uniqueness scan**: across the tested subgroups
   H ⊂ 2I and global eigenvalues λ', the full lift channel opens
   *only* at (H=2T, λ'=12). A negative grammar rule.

Positive + negative + syntactic structure = a working grammar.

## What is in this bundle

```
paper/                         The paper itself
  translation-layer.tex
  translation-layer.pdf
  references.bib

data/                          Machine-readable canonical artefacts
  dictionary.csv               14 typed substrate → referent entries
  grammar.csv                  15 grammar rules (12 transformation kinds + 3 derived)
  translation.csv              14 translation rows: dictionary + verdict + bridge → claim

docs/
  codex_review_prompt.md       Hostile-review prompt
  engine_pointer.md            Where to find the engine in tranformation-engine/

README.md                      This file
CHANGELOG.md
CITATION.cff
CONTRIBUTING.md
LICENSE                        CC BY 4.0 (paper, prose, CSVs)
.gitignore
```

## The empirical anchor

The grammar is reproducible from modules in the
[closure transformation engine](https://github.com/vfd-org/transformation-engine)
(see `docs/engine_pointer.md`). Specifically:

| Grammar result | Engine module |
|---|---|
| Schläfli decomposition | `closure_transform_engine.decomposition` |
| λ=12 lift theorem | `closure_transform_engine.keystone` |
| λ=12 uniqueness scan | `closure_transform_engine.physics.universality_lambda12` |
| Transformation taxonomy (12 kinds) | `closure_transform_engine.transformations.transformation_grammar` |
| Admissibility classes (5 classes) | `closure_transform_engine.physics.admissibility` |
| Transition rules | `closure_transform_engine.physics.transition_rules` |
| Physical-interpretation labels | `closure_transform_engine.physics.physical_interpretation` |
| Compositional reasoning | `closure_ai` (relational); `min_aria` (vector-state) |

## Reading order

- **If you only have ten minutes**, read §1 (the translation
  problem), the box at the end of §2 (the three layers), and the
  three grammar boxes in §5.
- **If you have one hour**, add §6 (translation rules with three
  worked examples) and §8 (compositionality via closure_ai /
  min_aria).
- **If you want to engage technically**, the CSVs in `data/` are
  canonical. The paper is a typeset summary.

## What this bundle does *not* claim

- It does not claim the language is correct as a physical theory.
- It does not derive RH, GRH, consciousness, or cosmology.
- It does not claim independence of the bridge hypotheses listed in
  §7. Each translation is conditional on a named bridge.
- It does not claim translation is invertible. Interpretation→
  substrate is open.

## Companion bundles

- [`vfd-org/icosian-triad-v600`](https://github.com/vfd-org/icosian-triad-v600)
  — the math anchor for the substrate.
- [`vfd-org/closure-picture`](https://github.com/vfd-org/closure-picture)
  — the programme-wide interpretive synthesis.
- `release-bundles/evidence-ledger` — the audit framework
  separating dictionary entries from constraint-forcing entries.
- This bundle — establishes that the substrate is a working formal
  language.

## Status

Pre-peer-review open research preprint, v1.0.0-rc1, 2026-05-29.
Not independently validated.

## Licence

Paper, prose, and CSVs: CC BY 4.0. See `LICENSE`.

## Engagement

See `CONTRIBUTING.md`. The most useful feedback is at the
row-level of any of the three CSVs (a specific dictionary entry, a
specific grammar rule, a specific translation).
