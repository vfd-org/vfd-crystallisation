# Changelog

## [1.0.0-rc1] — 2026-05-30

Initial public release.

### Paper

**Title:** *The Gradient Bridge: Closing the substrate's continuous
coverage gap.*

**Main observations:**

1. The |L_sub| topology in the critical strip is left/right
   asymmetric about Re(s) = 1/2 due to the functional equation
   ζ(s) ↔ ζ(1−s).
2. Vertical gradient (along Im) dominates horizontal (along Re)
   by factor ~2.7 — horizontal-stripe topology.
3. The witness axis is the meeting line of two structurally
   different regimes; zeros sit at the intersection.

**Cascade coverage estimates:**

- V_600: ~65% combined coverage of gradient regions
- E_8: ~77%
- E_8 × E_8: ~91%
- L_∞ (infinite cascade): 100%

**Main conjecture:** Cascade-Completeness Conjecture — finite
cascade level N forces RH structurally. The minimum N is unknown.

### Sims

- `sim_strip_sweep.py` — basic 41×81 strip sweep (Re ∈ [0.05,
  0.95], Im ∈ [-50, 50])
- `sim_gradient_regions.py` — high-res near γ_1, γ_5, γ_10
- `sim_full_strip_topology.py` — full 33×91 topology map +
  gradient field + valley trace
- `sim_cascade_coverage.py` — discrete-to-continuous coverage
  estimate for 8 cascade levels

### Outputs

7 generated plots including the full strip heatmap (showing
zero locus on Re=1/2), gradient magnitude field, valley trace,
cascade coverage growth curve, and three region zooms.

### Scope discipline

- Pre-peer-review preprint footer enforced
- No RH proof claimed
- Computational evidence at finite resolution (Δ Re ~0.025)
- Cascade-completeness is conjecture, not theorem
- Coverage metric is heuristic, not analytical
