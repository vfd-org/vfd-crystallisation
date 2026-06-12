# Deliverable C — matrix-model results

Source: `matrix_model_experiments.py`, `results/beta_baseline/beta_baseline.json`.

## Phase 1 — the harness distinguishes the three classes

Nearest-neighbour spacing distribution (NNSD) after unfolding to mean spacing 1,
L1-distance to the Wigner surmises, and the small-`s` repulsion exponent.

| ensemble | best-fit β | dist to β=1 | dist to β=2 | dist to β=4 | repulsion `s^?` |
|---|---|---|---|---|---|
| GOE | **1** | 0.084 | 0.269 | 0.527 | 0.90 |
| GUE | **2** | 0.215 | 0.058 | 0.281 | 1.57 |
| GSE | **4** | 0.476 | 0.262 | 0.078 | 3.89 |
| **zeta zeros** (300) | **2** | 0.385 | 0.244 | 0.264 | 2.75 |

The harness cleanly separates GOE/GUE/GSE (each matches its own class by a wide
margin) and classifies the **Riemann zeros as β=2 (GUE)** — the standard
Montgomery–Odlyzko fact, reproduced here from `mpmath.zetazero` with von-Mangoldt
unfolding. So Test 4 (β-transition) and Test 7 (robustness) have a trustworthy
yardstick.

## Phase 3/4 — do projections move β=4 toward β=2?

On a true GSE matrix (`results/projection_candidates/`):

| projection | result | reading |
|---|---|---|
| GSE baseline | β=4 | control |
| B3 drop Kramers pairs | β=4 | removing the 2× degeneracy ≠ GUE |
| B4 half-spectrum | β=4 | decimation changes density, not class |
| B1 complex restriction | β=2 | **circular**: this *builds* a GUE matrix |

**Pass/fail (WO Deliverable C):** the only projection that yields β=2 statistics
does so by construction (it extracts a complex Hermitian matrix), i.e. by
arbitrary/post-hoc selection — the explicit **fail condition**. No projection
moves GSE *spacing* to GUE *spacing* for a structurally-explainable,
non-circular reason. GSE and GUE are distinct universality classes.

## Honest conclusion

At the **spacing/universality** level the β=4→β=2 transition is **not** achievable
by a canonical projection — and, crucially, the icosian substrate does not even
present GSE spacing (`BETA_CLASS_AUDIT.md`: 9 distinct eigenvalues / 120). The
real content is at the **symmetry-class** level (complexification), treated next.
