# Cosmic Self-Pruning + Frame Recurrence --- numerical demonstrations

`cosmic_demo.py` grounds the structural claims of the cosmic / structural
extension paper. Each demo (C1--C5) maps to a load-bearing theorem.

## Running

```bash
python cosmic_demo.py                # run all five demos
python cosmic_demo.py --demo 1       # only C1 (cascade rung tower)
python cosmic_demo.py --no-figures   # numerics only
```

Outputs in `output/`: 4 PNG figures + `cosmic_demo_results.json`.

## What each demo verifies

| ID | Demo | Paper grounds | Verified |
|----|------|--------------|----------|
| C1 | Cascade rung tower (E_8, H_4 = V_600, D_4 = 24-cell) | Thm 19.1 | each rung has non-trivial Sigma; tau commutes with C; lambda_min(C) > 0 |
| C2 | Hierarchical time-scaling | Thm 19.2 | per-rung tick rates differ |
| C3 | Pruning operator idempotence | Def 18.1, Prop 18.2 | $\|P \circ P - P\| < 10^{-10}$; self-adjoint; rank = dim Sigma |
| C4 | Non-periodic recurrence under time-dependent C | Thm 18.4 | no two phases coincide; constant-C trajectory converges (Option A); time-varying does not |
| C5 | Frame destruction four conditions | Thm 16.2 | each pathway independently collapses dim Sigma |

## Substrate facts confirmed

- **E_8**: 240 root vectors in R^8, uniform degree 56 (each root has 56 nearest neighbours)
- **H_4 = V_600**: 120 vertices, uniform degree 12, edge length 1/phi
- **D_4 = 24-cell**: 24 vertices, uniform degree 8, edge length 1
- All three rungs admit a positive-definite C_phi and a non-trivial spectral tau

## What C1 shows about CP-rung-9.3

The open task CP-rung-9.3 asks to verify sigma-fix dimensions at each cascade
rung. C1 instantiates this for E_8, H_4, and D_4 using the spectral-tau
construction. The reported dim Sigma values (for the spectral tau choice that
negates the top eigenvalue cluster):

- E_8:      dim Sigma = (n - top cluster size)
- H_4=V600: dim Sigma = 116
- D_4=24c:  dim Sigma = (n - top cluster size)

The exact icosian sigma-fix dims (94 for H_4 etc) require the full icosian
arithmetic construction; the spectral demonstrations show the structural
mechanism holds at each rung.

## Dependencies

```
numpy
matplotlib
```

Seed fixed at 42; results reproducible bit-for-bit.
