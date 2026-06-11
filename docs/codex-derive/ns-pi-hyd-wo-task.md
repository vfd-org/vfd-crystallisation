# Task: WO for NS Π_hyd integration lemma

## Goal

Discharge H_{NS} (the hydrodynamic-projection bridge) so
`papers/millennium-ns-formal/ns-formal.tex` can be promoted from
"conditional on H_NS + H_1 + H_{P6/P7}" to either fully
unconditional NS global regularity, or at minimum to "conditional
only on H_1' (cascade-internal closure-convergence hypothesis)."

The bridge lemma Π_hyd: given the cascade closure functional F on
the 600-cell substrate with bounded discrete spectrum (F4), and the
coarse-graining map c: cascade-discrete-fields → continuum velocity
u: R^3 × [0,T] → R^3, prove

  sup_{t ∈ [0,T]} ‖ω(c(Φ(t)))‖_{L^∞(R^3)} ≤ M(α, β, γ, ‖u_0‖)

uniformly in T, where Φ(t) is the cascade evolution.

By Beale-Kato-Majda, this implies global C^∞ regularity of the NS
solution u(x,t) with initial data u_0.

## What's known / available

- F4 (foundations.tex): cascade closure operator F has bounded
  discrete spectrum on H_4 substrate (600-cell); 9 eigenvalues
  {1, 12, 20, 12, 30, 12, 20, 12, 1} as conjugacy classes, eigenvalue
  multiset {0, 9, 12, 14, 15, ...} from the H_4 Laplacian.
- P6 Schläfli convergence: discrete cascade dynamics converges to
  a unique attractor on each rung.
- P7 hydrodynamic projection: c maps to fluid variables.
- BKM: continuum criterion ‖ω‖_∞ bounded → C^∞ regularity.

## What's needed

- B_NS_1: explicit form of c (cascade discrete → continuum NS variable
  map). Use multi-scale shell averaging on Z[φ]-scaled lattice.
- B_NS_2: explicit propagation theorem: discrete spectral bound (F4)
  → discrete vorticity bound on each scale → L^∞ vorticity bound
  via shell-summation.
- B_NS_3: Π_hyd integration lemma stated and (sketched) proved at
  Clay-bar grade.

## Constraints (no downgrades)

- Sim must use exact arithmetic where possible (cascade discrete
  spectrum is exact rational over Q(√5)).
- Continuum bounds use standard Sobolev / BKM analysis with
  explicit constants in terms of cascade parameters α, β, γ.
- Cite Lions, Ladyzhenskaya, Constantin-Foias for classical NS
  regularity background.

## Required output (Sections A-F per codex_derive template)
