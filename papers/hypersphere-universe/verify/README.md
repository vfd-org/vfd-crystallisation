# Numerical Verification Suite

This directory contains the verification script `verify_paper.py` that re-derives every numerical claim in `hypersphere-universe.tex` from scratch. No values are imported from the paper or from prior cascade work — every quantity is computed here.

## How to run

```bash
pip install -r requirements.txt
python verify_paper.py
```

Expected output: **77/77 tests passing**, no failures. Total runtime ~10 minutes (dominated by the 8640-dim eigendecomposition in the final test).

## What each test verifies

| # | Test | Paper claim | Section |
|---|------|-------------|---------|
| 1-5 | F1: Banach contraction | `r = 1 + 1/r → φ`, convergence rate `≤ 4/9`, `φ² = φ+1`, `ψ` Galois conjugate, `φψ = -1` | Theorem 4.1 |
| 6-8 | F4: Depth count | `N = 7 + 24² = 583`, 7 scalar shells, 576 tensor shells | Lemma 8.3 |
| 9-11 | C1: 24-cell construction | 24 unit-norm vertices, distance profile {1: 8, √2: 6, √3: 8, 2: 1} | §6.1 |
| 12-14 | H₄ rung: 600-cell | 120 unit-norm vertices, 24-cell ⊂ 600-cell | §5.1 |
| 15-18 | C2: 24-cell Laplacian | Spectrum {0:1, 4:4, 8:9, 10:8, 12:2}, low-band match to S³ Laplacian | Theorem 6.X |
| 19-22 | C3: 2I → A₅ action | 2I closure under quaternion multiplication, Schläfli compound 120 = 5×24, image of order 60, all even permutations | Theorems 6.X |
| 23-24 | C4: Moment tensor | M = r̂⊗r̂ has eigenvalues (0,0,0,1), traceless part has (-1/4, -1/4, -1/4, 3/4), trace = 1 | Theorem 6.X |
| 25-27 | F5: σ-orbit | E₈ = 240 roots = 120 + 120, orthogonal R⁴ factors, σ-orbit length = 2 | Conditional Theorem 8.6 |
| 28-31 | Λ derivation | `2·φ⁻⁵⁸³ = 2.892×10⁻¹²²`, within 1% of Planck 2018, within observation spread | Conditional Theorem 8.7, Numerical Fit 8.8 |
| 32-36 | Cosmological cross-checks | `Ω_Λ = 2/3 exactly`, `H₀ = 68.83 km/s/Mpc` (within Hubble-tension window), `H₀√Ω_Λ` at 0.81% of Planck, `H₀ t₀ = 0.936` (cascade Ω values), `t₀ = 13.30` Gyr | §8.7 |
| 37-38 | Sensitivity to N | N=583 unique within 1%, N=582 fails by 63%, N=584 fails by 38% | §9.2 |
| 39-40 | Search-space exhaustion | Exactly one (κ, N) in S = {1..8}×{1..1000} matches within 1%, and it's (2, 583) | Proposition 9.1 |
| 41-48 | 600-cell adjacency + dipole probe | Edge length 1/φ; degree 12; spectrum {12: 1, 6φ: 4, ...}; 4 off-Ramanujan adjacency eigenvalues; dipole correction δ matches Planck at +0.078% | §8.7, Lemmas `lem:dipole`, `lem:230-10` |
| 49-54 | E₈ extended operator search | Tests 10 candidate operators on 240-root E₈ system; all cascade-natural σ-twists give 230 on / 9 off (adjacency-level); robustness across n_off ∈ {8, 9, 10, 11} gives Λ gaps in [-0.08%, +0.24%] | Remark `rem:dipole-robust` |
| 55-59 | **Ihara-zero rigorous 230/10** | **EXACT verification**: 120 adjacency eigenvalues → 240 Ihara zeros → 230 on-circle + 10 off-circle (= 2 trivial + 8 dipole). The dipole correction formula `δ = (10/240)·(12-6φ)/12` is now fully derived from scratch | Lemma `lem:230-10` |
| 60-63 | **Full F = αR+βE-γQ on E₈ (validation WO)** | Construct closure operator with F8 coefficients; verify it respects substrate Ramanujan-defect decomposition (2 trivial + 8 dipole + 230 on-Ramanujan = 240). Independent validation of dipole correction via cascade closure operator | Remark `rem:F-validation` |
| 64-70 | **Rank-2 F operator on 600-cell** | Full rank-2 symmetric tensor field validation: 1200-dim state space (120 vertices × 10 Sym²(R⁴) components); F = αL⊗I + β div^T·div - γI; verify symmetric, verify substrate sector decomposition (10 + 40 + 1150 = 1200), verify off-Ramanujan ratio rank-invariance (5/120 = 50/1200 = 1/24) | Remark `rem:F-validation` (rank-2 extension) |
| 71-77 | **Rank-2 F on full E₈ (8640-dim, ~5 min)** | The strongest verification: 240 vertices × 36 (Sym²(R⁸)) = 8640-dim state space; full F = αR + βE - γQ with F8 coefficients; diagonalise 8640×8640 (LAPACK, ~250s); verify sector decomposition (72 + 288 + 8280 = 8640); verify off-Ramanujan ratio identical across all 4 operators built (5/120 = 50/1200 = 10/240 = 360/8640 = 1/24) | Remark `rem:F-validation` (full rank-2 E₈) |

## Output format

Each test prints a `[✓]` or `[✗]` line with the claim and the computed values. At the end, a summary lists pass/fail counts. If any test fails, the script exits with code 1.

## Reproducibility

- All numerical results are computed using `mpmath` at 50-digit precision for sensitive quantities (φ-powers, Λ evaluation, sensitivity sweeps).
- All polytope constructions (24-cell, 600-cell) use standard rational coordinates; no random sampling.
- The Friedmann integral uses `scipy.integrate.quad` with default tolerance.
- The 2I → A₅ action uses fixed coset representatives (sorted lexicographically) to ensure deterministic output.

## What does NOT pass and why

Currently 42/42 pass. Earlier development versions had failures from:

- **Unit conversion bug** (KMSMPC_TO_GEV off by 10×): the natural-units conversion is `1 km/s/Mpc = 2.13×10⁻⁴⁴ GeV`, not `2.13×10⁻⁴³`. (This was fixed; the paper's intermediate-step text in Appendix A.5 originally had the wrong constant but the final number was correct.)
- **Quaternion rounding tolerance**: 2I closure under multiplication needs `1e-12` distance tolerance because float quaternion products accumulate ~1e-15 noise per multiplication. Switched to nearest-vertex check.
- **Set iteration determinism**: 2I → S₅ permutation needs *fixed* coset representatives (sorted, not `next(iter(set))`) for consistent action computation.
- **Traceless vs full moment tensor**: paper's eigenvalues `(-1/4, -1/4, -1/4, 3/4)` are for the *traceless* part M₀ = M - (tr M/4)·I, not the full M (which has eigenvalues `(0, 0, 0, 1)`). Sim now checks both.
- **H₀·t₀ for cascade Ω-values**: For cascade Ω_m = 1/3, Ω_Λ = 2/3, the integral is `√(2/3)·arcsinh(√2) = 0.9358`, not the 0.951 value the paper originally had (which was using observed Planck Ω-values). Paper text was updated to match.

These were sim bugs and paper inconsistencies, not bugs in the underlying mathematics.

## Dependencies

```
numpy >= 1.20
scipy >= 1.7
mpmath >= 1.2
```

Pure Python; no compiled extensions needed.

## Reference implementations (existing scripts in the repo)

The verification herein is independent of, but cross-checks against, scripts in `papers/cascade-derivation/scripts/`:
- `base_permeability_lambda.py` — Λ evaluation
- `dual_600cell_factor2.py` — factor-2 σ-orbit
- `closure_depth_583.py` — rank-stratified depth
- `omega_lambda_cascade.py` — Ω_Λ derivation
- `lambda_independent_predictions.py` — cross-checks
- `continuum_limit_24cell.py` — L_24 spectrum
- `coset_action_2I_on_5_skeletons.py` — A₅ action
- `tensor_uplift_24cell.py` — moment tensor

If any sim test fails, cross-check with the corresponding cascade-derivation script.

## Citation

When citing this verification suite, reference:

> *Hyperspherical Closure Cosmology: A φ-Cascade Derivation of Λ.* Verification suite at `papers/hypersphere-universe/verify/verify_paper.py`.
