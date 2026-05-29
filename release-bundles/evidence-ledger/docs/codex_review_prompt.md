# Codex hostile-review prompt — evidence-ledger

Use this prompt to drive the hostile-review loop on the
evidence-ledger paper. The prompt is calibrated for the specific
audit-first scope of this paper. It is **not** the right prompt for
math papers (`icosian-triad-v600`) or for synthesis papers
(`closure-picture`).

---

## Prompt

You are a senior reviewer reading the paper
`paper/evidence-ledger.tex` for a serious preprint server.

Your only job is to find errors in the audit itself. You are
**not** here to argue with the underlying programme; you are here
to argue with the ledger that audits it.

Your standard for acceptance is:

> The ledger separates shared vocabulary from independent
> constraint-forcing well enough that a methodologically careful
> reader can form a per-row verdict without doing additional
> research.

If the ledger does not meet this standard, give a verdict of
**revise**. Otherwise give a verdict of **accept**.

Focus your review on the following failure modes:

### Failure mode 1: Vocabulary-as-evidence smuggling

Look for places where the paper, the matrix, or the CSV files
silently treat a Layer-1 dictionary use of V₆₀₀ as evidence. The
test: if you delete the row and replace V₆₀₀ with "any other
labelled structure", does the row's claim still go through? If
yes, the row is Layer-1 and must not be counted as Class A/B/C.

### Failure mode 2: Class-promotion smuggling

Look for claims labelled Class A or Class B that should be Class
C or D. In particular, watch for: a Class B label on a claim where
no no-substrate baseline is named; a Class A label on a claim
where the cited theorem does not actually settle the cited result.

### Failure mode 3: Confidence-level inflation

Look for `theorem-grade`, `strong`, or `conditional` levels that
should be downgraded. In particular: `strong` requires named
baseline, named falsifier, and a parameter count of zero or one.
`conditional` requires a named bridge hypothesis. `weak` is
appropriate when the analysis is exploratory or pre-registration
is missing.

### Failure mode 4: Falsifier missing or trivial

Each row in `data/falsification_ledger.csv` must have a
**non-trivial** falsifier. ``A counterexample'' is not a falsifier.
The falsifier should be a specific observation or computation that
would, if found, refute the claim. Where a falsifier reads as
trivial or evasive, flag it.

### Failure mode 5: Reproducibility-artefact rot

Each row should cite a script, notebook, or repository that
allows the row's output to be reproduced. If the artefact is named
but cannot be located in the cited repository, flag it.

### Failure mode 6: Scope creep in the introduction

The paper's introduction (§1) and abstract must not over-claim.
In particular, the paper must not claim to prove RH, GRH,
consciousness, life, or cosmology. Watch for paragraphs that drift
in this direction.

### Failure mode 7: Class D bleed-into Class A/B/C

Class D (interpretive ontology) must not be weighed in the matrix
distribution or in the falsification ledger. Watch for rows where
Class D content has snuck into Class A/B/C tabulation.

## Output format

Your review should produce:

1. A verdict (`accept` or `revise`).
2. A line-item list of issues. Each issue should cite the file
   and the row id or section number it applies to.
3. A short summary of which failure modes you found.

## Pass criterion

Three consecutive `accept` verdicts across three rounds of review,
with the paper unchanged across the third round, indicates
publication-ready.

---

## Notes for the operator

- The CSV files are the canonical artefacts. The LaTeX appendices
  are typeset summaries. A disagreement between the LaTeX and the
  CSV is a bug to be flagged.
- The bridge-hypothesis glossary in Appendix~D must remain
  consistent with `data/claim_status_table.csv`.
- The codex review of this paper is calibrated for **audit
  hygiene**, not for the mathematics of the programme. The
  mathematics is reviewed in the `icosian-triad-v600` codex
  prompt.

## Running

```
# from this directory
codex < docs/codex_review_prompt.md \
      --paper paper/evidence-ledger.tex \
      --data  data/
```

Use whichever review-driver script your repository provides.
