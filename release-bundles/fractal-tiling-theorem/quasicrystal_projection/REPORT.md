# Quasicrystal-projection diagnostic — report

WO-RH-HYPERBOLIC-QUASICRYSTAL-PROJECTION-001, first build (§7). Diagnostic, not a proof.

## Result: do primes look more quasicrystalline than random?  YES — weakly.
Diffraction concentration (1 = flat/random, high = sharp Bragg peaks):

| point set | concentration |
|---|---|
| lattice (periodic) | ~467 |
| quasicrystal (Penrose/Fibonacci) | ~158 |
| **LOG-PRIMES** | **~6** |
| random (Poisson) | ~2 |

Ordering: **lattice > quasicrystal > log-primes > random.** The log-primes are ~3x
more spectrally concentrated than random — genuinely *more ordered* — but ~26x less
than a clean quasicrystal. So primes are a **weak / "limit" quasicrystal**: detectably
non-random, but far from crystalline.

## Where the primes' order lives: the zeros
The log-prime (von Mangoldt) diffraction `Σ Λ(n) n^{-1/2} cos(t log n)` peaks at the
**Riemann zeros** `γ_n` (clear at `γ₁=14.13`; more resolve as the prime range grows —
0→2→4 zeros for X = 1k→20k→200k). This is **Dyson's 1D quasicrystal**: the zeros are
the diffraction spectrum of the primes (and vice-versa) — the explicit-formula duality.

## Verdict (honest)
- **Weak pass.** Primes are more quasicrystalline than random, and their spectral
  order *is* the zeros — confirmed diagnostically.
- **But this is the diffraction/explicit-formula duality, which we already have** — NOT
  the positivity. The quasicrystal framing gives the *spectrum*, not the proof that it
  lies on the line (Weil positivity = RH). Same wall.
- Track B (hyperbolic-boundary / E10 quasicrystal, Boyle-Kulp arXiv:2408.15316) would
  add visualization, not positivity — so it is *intuition-grade*, not RH-bearing.

Scripts: `diffraction_diagnostic.py`. Builds on `../hyperbolic_600cell_honeycomb/`,
`../rh_address_lock/`, `../RH_OBJECT_TEST.md`.

## Coxeter-plane star projections (`coxeter_star_projection.py`)
Built the canonical Petrie/Coxeter-plane projections of the exceptional root systems:
E6 (72 roots, 12-fold), E7 (126, 18-fold), **E8 (240, 30-fold — the iconic mandala)**.
Output: `coxeter_stars.png`, `coxeter_star_coords.json`. These are the real, canonical
"star" geometries — the visible symmetric skin of the FINITE reflection groups.

E10 caveat: E10 is infinite-dimensional / hyperbolic, with INFINITE Coxeter number — so
it has **no finite Coxeter-plane star**. One can only build a *constructed* slice/boundary
projection of a finite patch of its real roots (star-like but aperiodic, growing without
bound) — non-canonical, visualization-grade. Honest scope: all of this is the Coxeter
*symmetry skin* (the bulk reflection structure projected) — it gives structure/symmetry,
NOT the positivity. Visualization, not RH progress.
