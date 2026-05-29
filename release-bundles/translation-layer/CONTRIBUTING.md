# Contributing

This bundle is pre-peer-review open research. The most useful
engagement is **row-level** at any of the three canonical CSVs in
`data/`.

## How to engage

### Dictionary feedback

Open an issue with the label `dict-DXX` (where `DXX` is the
`entry_id` from `data/dictionary.csv`).

Examples of useful issues:
- "D08 (lambda_12 lift channel): the cognitive referent
  'coherence channel' is too strong without H-CortexClosure cited
  alongside H-ModeUnique."
- "D14 (min_aria 7-dim state vector): the `evidential_status`
  says `conditional`; I argue it should be `weak` because the
  agent has not been replicated by an independent group."

### Grammar feedback

Open an issue with the label `gram-GXX` (where `GXX` is the
`rule_id` from `data/grammar.csv`).

Examples:
- "G15 (lambda_12 uniqueness scan): the `default_admissibility_class`
  says `EXACT for (2T 12); BROKEN or smaller for all other tested
  pairs`. The phrase 'all other tested pairs' is empirical on a
  finite test set; the row should explicitly name the test set."
- "G04 (SPECTRAL_PROJECTION): the `default_admissibility_class`
  says `BROKEN otherwise`. I argue it should be `APPROXIMATE` at
  some threshold, not `BROKEN`."

### Translation feedback

Open an issue with the label `trans-TXX` (where `TXX` is the
`translation_id` from `data/translation.csv`).

Examples:
- "T04 (closed → stable observable): the `audit_caveat` is
  correct but the `interpretive_claim` should explicitly name the
  domain (which class of observable)."
- "T11 (V_24 → fundamental sector): the bridge hypothesis
  H-FundamentalSector is not defined in the paper. Add a
  definition."

### Engine-pointer feedback

If a function cited in `docs/engine_pointer.md` does not exist in
`tranformation-engine/closure_transform_engine`, open an issue
with the label `engine-pointer`. Drift in pointers is the main
maintenance task on this bundle.

### Audit-hygiene feedback

If the paper itself drifts from its language argument (e.g.\
promotes a Layer-1 dictionary entry to a Layer-3 interpretive
claim without going through a Layer-2 grammar verdict), open an
issue with the label `scope`.

## What we will not accept

- Claims that the substrate's status as a formal language settles
  any physical, biological, or cognitive question.
- Claims that drop the "candidate identification" caveat on a
  translation.
- Marketing reframes that drop the named bridge hypotheses.
- Reframes that promote the λ=12 uniqueness scan to theorem-grade
  without independently completing the subgroup test set.

## Updating the CSVs

CSVs in `data/` are canonical. Update CSV first, regenerate the
LaTeX appendix tables, then bump `CHANGELOG.md`.

## Licence

CC BY 4.0. By contributing, you agree your contributions are
released under the same licence.
