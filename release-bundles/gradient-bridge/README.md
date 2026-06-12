# The Gradient Bridge

**Closing the substrate's continuous coverage gap: gradient regions
of L_sub in the critical strip and their cascade-level coverage**

This bundle extends the V₆₀₀ closure programme by mapping the
continuous gradient regions of |L_sub(s)| in the critical strip
0 < Re(s) < 1 — the analytical landscape *between* the substrate's
discrete particles.

## The gap we're closing

The substrate captures **discrete** structure:
- 120 V_600 vertices in S³
- 9 distinct C_φ eigenvalues
- γ_n discrete points on the witness axis

What's missing is the **continuous** gradient field of |L_sub|
covering the open critical strip *away from* the axis. This
in-between region carries the analytical content that determines
whether off-axis zeros are possible — which is RH.

## What the sims found

### Sim 1: full critical-strip topology

Computed |L_sub(s)| on a 33×91 grid covering Re ∈ [0.1, 0.9],
Im ∈ [10, 55]. Three structural observations:

1. **Left/right asymmetry around Re=1/2.** ζ(s−1) dominates the
   left, ζ(s) oscillation dominates the right. The functional
   equation creates this asymmetry; the witness axis is the
   meeting line.

2. **Horizontal-stripe topology.** Vertical gradient (along Im)
   dominates horizontal (along Re) by factor ~2.7. |L_sub|
   oscillates rapidly with Im at fixed Re.

3. **Zeros are at the meeting line, not at a simple valley.**
   The zeros aren't where |L_sub| is uniformly small; they're
   where both factor regimes can simultaneously produce zero.

### Sim 2: gradient regions near known zeros

High-resolution probes near γ_1, γ_5, γ_10. Gradient flow lines
from off-axis starting points do NOT trivially converge to the
axis — the topology is more complex. But the deep minima (the
actual zeros) are all on Re=1/2.

### Sim 3: cascade coverage

Estimated coverage of the gradient regions at each cascade level:

| Level | Vertices | Combined Coverage |
|---|---|---|
| Pentagon | 5 | 41% |
| Icosahedron | 12 | 44% |
| Dodecahedron | 20 | 48% |
| 24-cell | 24 | 46% |
| **V_600** | **120** | **65%** |
| E_8 | 240 | 77% |
| E_8 × E_8 | 480 | 91% |
| L_∞ | ∞ | 100% |

Each cascade level adds particles and covers more of the gradient
regions. Full coverage requires the infinite-cascade limit.

## What this implies for RH

**Cascade-Completeness Conjecture (Conjecture 1):** If some
finite cascade level N covers the gradient regions densely
enough to structurally forbid off-axis zeros, then RH holds.

We do NOT prove this conjecture for any finite N. We observe
the structural ingredients:

- The witness axis Re=1/2 sits at the unique meeting line of
  asymmetric L-function factors.
- Each cascade level adds more particles, covering more of the
  off-axis topology.
- At V_600 alone (~65% coverage), substantial gradient gaps
  remain. At E_8×E_8 (~91%), the gap is smaller. At L_∞, the
  substrate becomes the continuum.

The minimum N for which the structural forcing is rigorous is
unknown. This is the substrate's most refined formulation of
what RH asks.

## Bundle contents

```
gradient-bridge/
  paper/
    gradient-bridge.tex
    gradient-bridge.pdf       ← compiled with topology + cascade plots
  sims/
    sim_strip_sweep.py        ← basic strip sweep
    sim_gradient_regions.py   ← high-res near zeros
    sim_full_strip_topology.py ← complete topology map
    sim_cascade_coverage.py   ← cascade level coverage
  outputs/                    ← 7 generated plots
  data/                       ← raw measurement CSVs
  README.md
  CHANGELOG.md
  LICENSE
```

## Position in the programme

```
icosian-triad-v600         → substrate, C_φ, L-function identity
closure-picture            → programme-wide interpretive synthesis
critical-line-pullback     → 8 findings on critical-line embedding
translation-engine-v2      → operational engine (v0.6, 7 admissibility)
observer-attractor-theorem → Witness Invariant Theorem (W = V_min)
rh-witness-resonance       → RH as substrate spectral completeness
gradient-bridge            → THIS BUNDLE: continuous gradient regions
                             + cascade extension
```

The arc: substrate → interpretation → findings → engine → witness
identification → RH reformulation → gradient regions.

## What is computational evidence

- |L_sub| topology in the strip has the observed asymmetry,
  stripes, and meeting-line structure
- Cascade vertex count grows in a way that progressively covers
  the gradient regions
- At V_600 alone, ~65% combined coverage; substrate captures the
  witness axis but not the off-axis topology directly

## What is conjecture

- Cascade-Completeness Conjecture: some finite N forces RH
- The minimum such N

## What is not proved

- RH itself
- GRH for L(s, χ_5)
- Any direct relation between cascade-coverage percentages and
  analytical content of RH (the coverage metric is heuristic)

## Status

Pre-peer-review open research preprint. **No RH proof claimed.**
The bundle provides computational evidence and structural
framework only.

## Licence

Paper and prose: CC BY 4.0.
