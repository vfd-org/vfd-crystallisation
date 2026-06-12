# Processing to Point of View --- bridges numerical demonstrations

`bridges_demo.py` grounds the operator-level bridges to mainstream
consciousness science.

## Running

```bash
python bridges_demo.py                # all three demos
python bridges_demo.py --demo 1       # only B1 (Levin)
python bridges_demo.py --no-figures
```

Outputs in `output/`: 3 PNG figures + `bridges_demo_results.json`.

## What each demo verifies

| ID | Demo | Paper grounds | Verified |
|----|------|--------------|----------|
| B1 | Levin bridge --- cell-cluster bioelectric closure | Cond. Prop. 4.5 | tau^bio is involution; tau^bio commutes with C^bio (to 1e-15); lambda_min(C) = mu^bio; dim Sigma^bio = n/2; off-Sigma decay rate matches (1 - lam * mu_perp)^t prediction |
| B2 | CEMI spectral signature | Cond. Prop. 5.5 | dipole observable's spectral content concentrated on excited eigenmodes (concentration ratio > 3) |
| B3 | Sleep / anaesthesia perturbation | Cond. Props 7.2, 7.3 | eigenspectrum shifts continuously with drug concentration; criticality detected at alpha* where stability margin crosses 0; effective dim Sigma drops past threshold |

## Substrate facts

- **B1 cell-cluster**: 60 cells, explicit bilateral symmetry (left-right swap),
  random within-side connectivity + 8 cross-bridges. tau^bio is the swap
  permutation, which commutes exactly with C^bio.
- **B2 cortex**: 60 cortical units with random local connectivity (p_local = 0.18)
  and weighted edges (gamma-rhythm-like).
- **B3 cortex with pharmacology**: same cortex; alpha parameter scales the
  Laplacian eigenvalues (modelling inhibitory potentiation).

## What B1 actually shows

The bridge proposition (Cond. Prop. 4.5) states that C^bio = L^bio + mu^bio I
satisfies the closure-operator axioms (sigma-equivariance, contraction off
Sigma, locality) on any cell-cluster substrate with a discrete symmetry. B1
instantiates a small substrate, builds C^bio and tau^bio, and shows:

- The operator axioms hold numerically (commutator within 1e-15).
- The predicted decay rate matches measured decay to 4+ decimal places.
- The Sigma^bio dimension matches the predicted n/2 (bilateral symmetry).

This is the empirical content of the Levin bridge: the closure-operator
framework applies cleanly to a bioelectric substrate with the right symmetry.

## What B2 actually shows

The CEMI bridge claims that the spectral content of the cortical EM field
is determined by the closure operator's eigenstructure on Sigma. B2 constructs
the dipole observable E(t) = sum_i F_i(t) d_i for random positions d_i, runs
the closure dynamic with a source that excites three specific eigenmodes, and
verifies that the projection of the substrate state onto the excited modes
is much larger than the average projection onto non-excited modes.

This is the operator-level evidence: the EM field is structurally determined
by which eigenmodes the closure dynamic activates.

## What B3 actually shows

The anaesthesia proposition (Cond. Prop. 7.3) says drug concentration shifts
the eigenspectrum continuously and crosses a threshold at which the closure
dynamic's stability is broken. B3 sweeps the perturbation strength alpha,
tracks lambda_max(C_modified), and identifies the critical alpha at which
1 - lam * lambda_max crosses zero. Below: full dim Sigma. Above: dim Sigma
drops as fast modes become inaccessible.

## Dependencies

```
numpy
matplotlib
```

Seed fixed at 42.
