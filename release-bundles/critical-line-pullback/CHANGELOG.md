# Changelog

## [1.0.0-rc1] — 2026-05-29

Initial public release.

### Paper

**Title:** *The Critical Line, Pulled Back to V₆₀₀: Four empirical
findings on the substrate image of ζ(s)'s non-trivial zeros.*

**Findings (load-bearing):**

1. Substrate L-function L_sub(s) = ζ_K(s)·ζ_K(s−1)·C_2(s)
   vanishes at every one of the first ten Riemann zeta zeros to
   numerical precision (|L_sub| < 2·10⁻¹¹).
2. Eichler–Brandt formula r(p) = 8(1+p²) verified exactly at
   coordinate bound K=4 for all five odd inert primes p ≤ 23
   tested, plus the Jacobi anomaly r(2)=24.
3. Clean closed 10-vertex icosian rotation orbit visible as
   discrete helix on S³.
4. Coordinate-Galois σ does NOT preserve V₆₀₀ as a set; 96 of
   120 vertices map to odd-permutation positions outside V₆₀₀.
   The "94+13+13" decomposition referenced in the icosian-triad
   paper requires a different involution τ. Open follow-on
   pinned down precisely.

### Sims

- `sims/sim_critical_line_pullback.py` (v1) — initial probe;
  stereographic V₆₀₀ + truncated-Dirichlet L-function partial
  sum.
- `sims/sim_v2.py` (v2) — main probe; analytic L_sub via
  mpmath, evaluation at Riemann zeros, clean 10-vertex helix,
  Eichler–Brandt verification at K=4.
- `sims/sim_v3_sigma_exact.py` (v3) — exact-arithmetic σ
  diagnostic; surfaces Finding 4.

### Data

- `data/v2/l_substrate_at_riemann_zeros.csv` — load-bearing
  table for Finding 1.
- `data/v2/eichler_brandt_table.csv` — Finding 2.
- `data/v2/helix_orbit.csv` — Finding 3.
- `data/v3/sigma_decomposition.csv` — Finding 4 diagnostic.

### Plots

- `outputs/v2/02_l_spiral_riemann_marked.png` — main figure
  (substrate L-spiral with first 10 Riemann zeros marked).
- `outputs/v2/01_clean_helix.png` — Finding 3 (the helix).

### Scope discipline

- Pre-peer-review preprint footer enforced.
- No claim of RH or GRH settlement.
- Finding 1 is empirical confirmation of a published one-way
  identity, not a closure of the RH bridge.
- Finding 4 is honest: it surfaces a mismatch between
  expectations and direct computation, and pins it down to a
  precise open question.
