# A native icosian realization of Hilbert modular forms over Q(√5)

Pre-peer-review preprint. Reproduction-and-map paper: the 600-cell /
icosian maximal order reproduces a family of cuspidal Hilbert modular
forms over Q(√5) via Brandt modules, verified out-of-sample against
point-counted elliptic curves and Dembélé's tables, with an explicitly
heuristic (non-load-bearing) outlook on the Riemann Hypothesis.

## Build
```
pdflatex icosian-realization && bibtex icosian-realization \
  && pdflatex icosian-realization && pdflatex icosian-realization
```

## What is claimed (and what is not)
- **Verified (reproducible):** the prime-level cuspidal-dimension
  sequence over Q(√5) for split levels 31–89 (7/7 vs Dembélé, incl. the
  59-vanishing and the 61 jump); the full Hecke eigenvalue sets of two
  rational eigenforms (levels 31, 41) out-of-sample, no fit; the
  genus-2 form at level 61, with real multiplication by Q(√5) **proved**
  from a single non-square discriminant (Prop. on RM).
- **Not claimed:** any new number theory (this is an independent
  implementation of the standard definite Brandt method, reproducing
  Dembélé 2005), and any progress on RH (the §8 outlook is heuristic).

## Reproducibility
The load-bearing scripts live in `../route_b/` and `../../icosian_brandt_build/`:
`ideal_classes.py`, `brandt_matrices.py`, `hecke_compare.py`,
`second_form_level41.py`, `genus2_form_level61.py`,
`multilevel_dimensions.py`, `point_count_target.py`, `no_fit_guard.py`.
Targets are computed independently (brute-force point counts) and read
only at comparison time.

## Review
Hardened against a hostile-referee codex review (two rounds); see the
session log. Status stamps (Verified / Open / Interpretation) are
in-text via colored boxes.
