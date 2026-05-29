# Contributing

This is a pre-peer-review open research audit bundle. The most
useful engagement is **row-level**: a specific row of the matrix,
a specific column, a specific judgement you challenge.

## How to engage

### Row-level technical engagement (preferred)

Open an Issue with the label `row-XX` (where `XX` is the
`row_id` from `data/evidence_matrix.csv`). State which column you
disagree with and what you would replace it with.

Examples of useful issues:

- "row-10 (cosmological observables): the no-substrate-baseline
  column says 'ΛCDM (6-parameter fit)' but a 4-parameter EDE
  variant matches the same precision; the row should record this."
- "row-12 (α⁻¹ = 137 + π/87): confidence level says `conditional`;
  I argue it should be `weak` because the 6-hypothesis stack
  itself has not been shown to be minimal."
- "row-17 (ARIA 18/18): falsifier column says 'a new preregistered
  ARIA test fails'; this is correct but should also specify the
  effect-size threshold."

### Class-promotion / demotion arguments

If you believe a row should be promoted to a higher class (e.g.\
B → A) or demoted (e.g.\ A → B), open an Issue with the label
`reclassify`. Include the failure-mode reference (1–7) from the
codex review prompt.

### New-row proposals

If you believe the matrix is missing a claim that should be
audited, open an Issue with the label `new-row`. We will not add
rows that are not already supported by a public reproducibility
artefact.

### Audit-hygiene feedback

If the paper itself (rather than the matrix content) drifts from
its audit-first scope — over-claims, smuggles interpretation into
evidence, drops a falsifier — open an Issue with the label
`scope`.

## What we will not accept

- Claims that the audit ``proves'' the programme. The audit does
  not prove the programme; it makes the programme assessable at
  row-level granularity.
- Claims that the audit ``disproves'' the programme. The audit
  does not disprove the programme; specific rows survive or fail
  on their own terms.
- Reframes that drop Class D's flag and weigh interpretation as
  evidence.
- Reframes that drop named bridge hypotheses.

## Updating the ledger

The CSVs in `data/` are the canonical artefacts. Updates to a row
should be made in the CSV first; the LaTeX appendices are
regenerated from the CSV.

When a falsifier is attempted, update the `attempted` /
`date_attempted` / `attempt_artefact` / `outcome` columns in
`data/falsification_ledger.csv` and note the change in
`CHANGELOG.md`.

## Licence

CC BY 4.0. By contributing, you agree your contributions are
released under the same licence.
