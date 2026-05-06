# cascade-refinement-compat — repro

Self-contained reproduction bundle for the load-bearing computations
in `cascade-refinement-compat.tex`.

## Quick start

From this directory:

```bash
bash run_audit.sh
```

Wallclock: ~1 second on a laptop. A clean run prints
`REFINEMENT COMPAT AUDIT PASSED` and confirms that the live output of
`explore_defect.py` matches the frozen reference output in
`expected_outputs/`.

## Requirements

Python 3.8+ with `numpy`. The script also uses the standard-library
`fractions.Fraction` for exact rational arithmetic, so all results
are reproducible to symbolic precision.

## What is reproduced

`explore_defect.py` constructs two finite refinement towers
explicitly and verifies, to exact rational precision:

1. **Tower I** — single edge `(u, v)` refined by inserting one
   midpoint `m`. Confirms:
   - source's coboundary refinement relation
     `p^1 d_1 = (1/2) d_0 p^0` holds;
   - strict refinement-compatibility `p^0 A_1 = A_0 p^0` **fails**,
     with explicit defect `D_0` matrix (paper §6.1);
   - **Schur-complement halving**: the Schur complement of
     `A_1^vertex` w.r.t. the (boundary, interior) partition equals
     `(1/2) A_0^vertex` exactly (Theorem 2.1);
   - operational verification of `p^0 A_1 H_1 e_k = (1/2) A_0 e_k`
     for both boundary basis states.

2. **Tower II** — triangle (3-cycle) refined by inserting one
   midpoint per edge. Same five facts verified at the larger scale.

## What is *not* reproduced here

The paper makes no empirical claims. The numerical witness is purely
linear algebra over `Fraction`s; there are no fitted parameters, no
random seeds, and no external data. The reproducibility story is
fully self-contained.

## Files

- `README.md` — this file.
- `run_audit.sh` — single-command audit wrapper.
- `expected_outputs/explore_defect.txt` — frozen reference output.
- `output/` — created by `run_audit.sh`; gitignored.

## To regenerate frozen outputs (rare)

If `explore_defect.py` is intentionally modified:

```bash
bash run_audit.sh --refresh-expected
```

Otherwise leave them alone — they are a frozen reference for
reviewers.
