# Contributing

This is a pre-peer-review research packet. Contributions in any form are
welcome; what we most need is the kind of contribution that strengthens
the programme's empirical anchoring or sharpens the math discipline.

## What helps most

### Empirical replication

The single highest-impact contribution would be an external replication of
**any** of the empirical results in Notes B, C, D, or F using independent
data. The Closure-as-Distance methodology paper (Note C) lists pre-registered
external tests at the end; we will accept pull requests that add new
diagnostic-applied real-data analyses with frozen-script provenance.

### Math discipline review

The formal theorems in Paper I and the conditional propositions in Paper II
have been hardened through 5 rounds of codex (gpt-5.x) review. Independent
mathematicians who can read the τ-icosian-vs-spectral distinction (see Paper I
Appendix on $\tau$ conventions) and verify the structural claims under each
convention would be valuable.

### Limitations or scope issues

We list every disclosed limitation in `review/known_limitations.md`. If you
identify a limitation we have not disclosed, please open an issue.

## How to contribute

1. **Open an issue first** for substantive changes. Describe the claim you
   are concerned about, the data or argument that supports your view, and
   the proposed change.
2. **Pull requests welcome** for typo corrections, broken-citation fixes,
   reproducibility issues, and small wording tightenings. Larger changes
   should be discussed in issues first.
3. **Empirical contributions** should include the full freeze-script
   provenance: pre-registered thresholds, no retuning after seeing
   outcomes, CAD-D1–D5-v1 diagnostic computation before the main analysis.
4. **Negative results are welcome**. The programme explicitly commits to
   reporting honest negatives (see Note E, Note F). A pull request that
   adds a confirmed honest negative on an independent dataset is as
   valuable as a pull request adding a confirmed positive.

## Code style

- Python: standard library + numpy, scipy, matplotlib. Avoid heavy frameworks.
- Determinism: every sim demo is seeded at 42. Do not introduce
  uncontrolled randomness.
- Scripts must run under `python -m` from the repo root with `pip install
  -r repro/shared/requirements.txt`.

## Prose style

- Theorem / Conditional Proposition / Empirical Result / Empirical Proxy /
  Pre-registered Proposal: the five-class status taxonomy is enforced
  throughout.
- "Validated" → "operationalised and simulation-tested" or "empirically
  anchored to specific real data".
- "Rules out" → "argues against [X] as the sole explanation".
- "Iff" claims should be either proved or downgraded to "best matched by".

## Code of conduct

This is a research repository. Disagreement on substance is welcome.
Personal attacks, harassment, or ad-hominem arguments are not.

## Licence

By contributing, you agree that your contributions will be licensed under
the same terms as the repository: Apache-2.0 for code, CC BY 4.0 for prose.
