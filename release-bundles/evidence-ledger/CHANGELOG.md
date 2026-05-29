# Changelog

All notable changes to this audit bundle are documented here.

## [1.0.0-rc1] — 2026-05-28

Initial public release.

### Paper

- **Title:** *From Shared Vocabulary to Independent Constraint:
  An Evidence Ledger for the V₆₀₀ Closure Programme.*
- **Sections:**
  - §1 The burden problem
  - §2 What is not being claimed
  - §3 Dictionary, grammar, interpretation
  - §4 The four claim classes (A: exact / B: constrained
    derivation / C: data-facing / D: interpretation)
  - §5 When is the substrate doing work? — a formal criterion
  - §6 Reading the evidence matrix
  - §7 The shape of the matrix
  - §8 Comparison to other geometric programmes
  - §9 The recurrence-by-construction critique, met directly
  - §10 Open gaps
  - §11 What this audit changes
  - §12 Conclusion
  - Appendix A — evidence matrix
  - Appendix B — claim-status table
  - Appendix C — falsification ledger
  - Appendix D — glossary of bridge hypotheses

### Data (canonical artefacts)

- `data/evidence_matrix.csv` — 20 audited claims, 16 columns.
- `data/claim_status_table.csv` — bridge-hypothesis and
  verification status per claim.
- `data/falsification_ledger.csv` — falsifier, attempt outcome
  and notes per claim.

### Docs

- `docs/codex_review_prompt.md` — hostile-review prompt
  specifically for the audit (failure modes 1–7).

### Scope discipline

- Pre-peer-review open research preprint; not independently
  validated.
- No claim of RH / GRH / consciousness / cosmology settlement.
- Class D entries are flagged and excluded from the falsification
  ledger.
- Each Class B and Class C row records a named falsifier and a
  named bridge hypothesis (Appendix~D).
