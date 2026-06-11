# Post draft: Proton–electron mass ratio from the 600-cell spectrum

segment: physicists | status: verified

## BLOCKED — do these before posting
- [ ] No figure attached yet (figure_idea: 600-cell vertex graph render + its five-line integer spectrum, with the 15 eigenvalue highlighted feeding into the formula; predicted-vs-measured bar with 0.02% gap.)

## Lead post (figure attached: TODO)

```
The proton–electron mass ratio from one polytope's spectrum: φ^(1265/81) = 1835.8 vs measured 1836.15. The exponent's leading term is a 600-cell Laplacian eigenvalue.

1835.8 vs 1836.15267 (CODATA) — 0.02%.

No fitted parameters. Verify it yourself:
https://github.com/vfd-org/vfd-crystallisation
```

## Thread (one reply per block)

**2/**
```
What goes in (everything, numbered — judge for yourself):
1. The 600-cell: a single, classical 4D polytope (120 vertices, H4 symmetry)
2. Its graph Laplacian spectrum {0, 9, 12, 14, 15} — exact integers, verifiable by diagonalisation
3. The golden ratio φ as base (forced by H4/icosian structure, not chosen)
4. A stated counting rule for the exponent 1265/81 (the modelling input — see paper)
```

**3/**
```
How to kill it:
The exponent has no continuous freedom: 1265/81 is fixed by the counting rule and φ is fixed by H4. If the 600-cell Laplacian spectrum is not exactly {0,9,12,14,15}, or the counting rule cannot be stated without tuning, the claim dies.
```

**4/**
```
Run it (deps: numpy, scipy):
  cd papers/paper-xxii/scripts
  python3 run_600cell_spectral_verification.py
```

**5/**
```
Background / independent data: https://vibrationalfielddynamics.org/articles/paper-iv-pemr.html
```

**6/**
```
Full write-up: Paper IV (site entry point: /articles/paper-iv-pemr.html)
```

## Figure
TODO — idea: 600-cell vertex graph render + its five-line integer spectrum, with the 15 eigenvalue highlighted feeding into the formula; predicted-vs-measured bar with 0.02% gap.
