# Evidence Ledger for the V₆₀₀ Closure Programme

**From Shared Vocabulary to Independent Constraint:
An Evidence Ledger for the V₆₀₀ Closure Programme**

This bundle is the programme-wide audit responding to the critique
that V₆₀₀ recurring across the VFD programme's papers might be
*recurrence by construction* rather than *independent constraint-
forcing*.

The audit does not introduce new mathematics. It separates the
programme's outputs into four evidence classes — exact mathematical
certificates (A), constrained physical derivations (B), data-facing
empirical analyses (C), and interpretive ontology (D) — and records,
per claim, the substrate's role, the free-parameter count, the
fixed inputs, the comparison target, the reproducibility artefact,
and the falsifier.

The result is one paper and three CSV files. The CSVs are the
canonical artefacts.

## What is in this bundle

```
paper/                          The audit paper itself
  evidence-ledger.tex
  evidence-ledger.pdf
  references.bib

data/                           Machine-readable canonical ledger
  evidence_matrix.csv           20 audited claims with full audit columns
  claim_status_table.csv        Per-claim bridge-hypothesis and verification status
  falsification_ledger.csv      Per-claim falsifier and attempt outcome

docs/
  codex_review_prompt.md        Hostile-review prompt for codex review

README.md                       This file
CHANGELOG.md
CITATION.cff
CONTRIBUTING.md
LICENSE                         CC BY 4.0 (prose)
.gitignore
```

## What the paper does

The paper takes the critique seriously and states it in full. Then
it builds the apparatus needed to assess it row by row:

1. A **dictionary / grammar / interpretation** distinction
   separating Layer-1 vocabulary uses of V₆₀₀ (no evidential
   weight) from Layer-2 constraint-forcing uses (audited) from
   Layer-3 interpretation (Class D, flagged).
2. A **four-class taxonomy** (A: exact / B: constrained
   derivation / C: data-facing / D: interpretation) with explicit
   critique-survival commentary per class.
3. A **formal criterion** for when V₆₀₀ or closure is doing
   independent constraint-forcing work.
4. A **20-row evidence matrix** populated with the programme's
   current claims.
5. A **claim-status table** recording bridge hypotheses per claim.
6. A **falsification ledger** recording, per claim, the falsifier
   and whether the falsifying observation has been attempted.

## Class distribution in the current matrix

| Class | Count | Confidence range |
|-------|-------|------------------|
| A — exact mathematical certificate     | 6 | theorem-grade |
| B — constrained physical derivation    | 7 | strong → conditional |
| C — data-facing empirical analysis     | 5 | strong → weak |
| D — interpretive ontology              | 2 | interpretive (flagged) |

## Reading order

- **If you only have ten minutes**, read §1 (the burden problem),
  the class summary box in §4, and Appendix A (the matrix).
- **If you have one hour**, add §5 (the formal criterion) and §8
  (the recurrence-by-construction critique met directly).
- **If you want to engage technically**, the CSVs in `data/` are
  the canonical artefacts. The paper is the typeset summary.

## What this bundle does *not* claim

- It does not claim that the programme is correct.
- It does not claim to prove RH or any of its generalisations.
- It does not claim independence of the bridge hypotheses listed
  in `data/claim_status_table.csv`.
- It does not weight Class D as evidence.

## Companion bundles

- [`vfd-org/icosian-triad-v600`](https://github.com/vfd-org/icosian-triad-v600)
  — the math anchor (Paper 1 + Paper 2 + 13 reproducible sims).
- [`vfd-org/closure-picture`](https://github.com/vfd-org/closure-picture)
  — the programme-wide synthesis (compendium, ~80 pages).
- This bundle (`evidence-ledger`) — the audit that lets the
  programme be assessed at row-level granularity.

## Status

Pre-peer-review open research preprint, v1.0.0-rc1, 2026-05-28.
Not independently validated.

## Engagement

See `CONTRIBUTING.md`. The most useful engagement is at the row
level of the evidence matrix: a specific row, a specific claim, a
specific column you challenge.

## Licence

Paper, prose, and CSVs: CC BY 4.0. See `LICENSE`.
