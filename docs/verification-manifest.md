# Verification Manifest

**Date:** 2026-06-13
**Purpose:** the exact, reproducible record behind the book's "every checkable claim has code" promise — every suite, its command, and its expected pass count. Source for the book's verification appendix.

## How to run

All commands run from the repository root with stock Python 3 plus NumPy (SciPy and SymPy needed only where noted). Every suite is deterministic (fixed seeds) and prints a `SUMMARY: N PASS, 0 FAIL` line; any other output is a failure of the claim it tests, and we ask to be told about it.

```
python3 scripts/verify_rendering_layer.py        # expect 21 PASS
python3 scripts/verify_rung_dimension_ladder.py  # expect 25 PASS
python3 scripts/verify_ladder_completion.py      # expect 29 PASS
python3 scripts/verify_narrative_closure.py      # expect 28 PASS
python3 scripts/verify_gap_strengthening.py      # expect 22 PASS
python3 scripts/verify_gr_closure.py             # expect 39 PASS
python3 scripts/verify_residual_closure.py       # expect 24 PASS  (SciPy, SymPy)
python3 scripts/verify_crystal_forcing.py        # expect 17 PASS
python3 scripts/verify_boundary_green_function.py    # Newtonian 1/r witness
python3 scripts/verify_lemma_2p5_boundary_connectivity.py
```

**Total: 205 itemised checks across the eight core suites**, each engineered with a falsifiable null (a wrong-by-construction control that the test must reject), plus the two witness scripts.

## What each suite carries

| Suite | Checks | Verifies | Book chapters |
|---|---|---|---|
| `verify_crystal_forcing.py` | 17 | the crystal is forced (2I unique perfect/maximal, McKay = affine E8 computed from the multiplication table); the graph reconstructs its own geometry from bare adjacency; non-abelian gauge consistency forces a Lie algebra | Ch3, Ch4, Ch9 |
| `verify_rendering_layer.py` | 21 | spectral dimension 3 (square multiplicities, Weyl count, exact dispersion); canonical kernel; quaternionic frames/chart; inner clock reversal ⟹ second-order time | Ch4, Ch5, Ch6, Ch7 |
| `verify_rung_dimension_ladder.py` | 25 | intertwiner theorem (eigenspaces = sampled harmonics); design cutoffs; arenas only 3D + 7D | Ch9, Ch10 |
| `verify_ladder_completion.py` | 29 | octonionic S⁷ frames/kernel; folded sector; aliasing tables | Ch10 |
| `verify_narrative_closure.py` | 28 | the ten geometry→reality gap closures (first pass) | Ch6, Ch11, Ch12 |
| `verify_gap_strengthening.py` | 22 | hardened re-tests of the same closures with genuine nulls (post-hostile-review) | Ch12 |
| `verify_gr_closure.py` | 39 | the gravity chain: stress tensor, Fierz–Pauli uniqueness, trace reversal/factor 2, light bending ×2, GW, Schrödinger envelope, equivalence principle, Maxwell | Ch9 |
| `verify_residual_closure.py` | 24 | residual upgrades: in-house bootstrap, beyond-Gaussian effective action, explicit-rate continuum control, conditional G, gauge-group structure (G₂ → su(3) etc.) | Ch9, Ch12 |

Supporting witnesses: `verify_boundary_green_function.py` (discrete 1/r, fit R² = 0.9966), `verify_lemma_2p5_boundary_connectivity.py` (boundary graph 10-regular, connected, λ₂ = 1.77), `verify_hadron_radii.py`, `verify_kappa_descent.py`, `verify_084473_derivation.py`.

## Data and environment

- The only data file the core suites need is `scripts/600cell_data.npz` (vertices, adjacency, Laplacian, eigenvalues of the 600-cell), bundled in-repo. Everything else is computed from it or from first principles (the octonions are built by Cayley–Dickson doubling inside the scripts).
- Verified against: Python 3.8, NumPy 1.24, SciPy/SymPy as packaged; runtimes from seconds to ~3 minutes per suite on a laptop.
- The derivation documents these suites verify: `docs/why-this-crystal.md`, `docs/rendering-layer.md`, `docs/rung-dimension-ladder.md`, `docs/narrative-gap-closure.md`, `docs/kappa-derivation-math.md`, `docs/gr-closure-derivation.md`, `docs/residual-closure-derivation.md`, `docs/gauge-group-from-arenas.md`, with the consolidated claim table in `docs/claim-status-ledger.md`.
- Formal write-ups: Paper LIII (`papers/paper-liii/`, the gravity chain), Paper XL (`papers/paper-xl/`, the remaining continuum-geometry programme), and the per-topic papers indexed in `papers/`.

## Honesty notes for the appendix

- A passing suite verifies the *mathematical chain*, not the physical interpretation; the claim–status ledger grades each claim separately (THEOREM / DERIVED-EFF / CONDITIONAL / WITNESSED / TIE / OPEN).
- The failed earlier construction of the gravity tensor action is deliberately preserved (`docs/kappa-derivation-math.md` §6.7) as the record of what did not work and why.
- Pass counts above are the expected values at the commit this manifest was written; `git log --oneline -1` identifies the current state.
