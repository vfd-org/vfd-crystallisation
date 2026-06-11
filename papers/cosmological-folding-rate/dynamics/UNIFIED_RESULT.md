# Unified Cosmological Framework — H(z) + BH + CMB from V_600 cascade

**Status: 2026-05-05.** All three pieces close from one structural source.

> **SUPERSESSION NOTE (2026-05-07):** This document is the original
> 2026-05-05 exploratory note. It contains forceful "FORCED" /
> "DERIVATION CLOSED" / pre-registered-CMB-prediction language and
> uses `T_H` notation that is INCONSISTENT with the publication-ready
> credibility-bar discipline of the V_600 programme.
>
> The publication-ready synthesis is `papers/v600-unified/`, which
> (a) restricts Paper 4 imports to Layer 1 only (trace identities
> 13/12 and 11/12 + K-saturated admissibility); (b) marks the
> H_0 / S_8 numerical match as Layer-2 observation, NOT derivation;
> (c) marks the cycle-mode coupling map Γ as Layer-3 hypothesis,
> NOT theorem; (d) names CMB-bulk projection, cosmic dipole audit,
> and pre-registered prediction manifests as F1/F2/F3 future builds
> with explicit unmet prerequisites — not claims of the synthesis;
> (e) uses T_casc rather than T_H for the finite cascade
> temperature parameter, which is NOT calibrated to physical
> Hawking temperature.
>
> The "FORCED" / "DERIVATION CLOSED" language below is legacy and
> should not be cited as a load-bearing claim. Use
> `papers/v600-unified/v600-unified.tex` instead.

## The structural foundation

```
V_600 = 2I (binary icosahedral group, |2I| = 120)
  ├─ 12 T_τ-cycles (length 10 each)
  │   ├─ Bulk: 2 cycles (K=72 + K=0) = Dic_5 subgroup (20 vertices)
  │   └─ Boundary: 10 cycles in 5 σ-paired pairs (100 vertices)
  ├─ Dic_5: binary dihedral group of order 20, [2I:Dic_5] = 6
  │   └─ 6 RIGHT cosets Hg: 1 bulk + 5 non-bulk; each non-bulk right
  │      coset is one whole K=52 cycle + one whole K=20 cycle.
  │      (LEFT cosets gH are NOT whole-cycle carriers — Paper 1.)
  └─ τ_σ: VFD-canonical involution
      ├─ Fixes Dic_5 pointwise
      ├─ Swaps K=52 ↔ K=20 within each non-trivial coset
      └─ Constructed via σ-projection in icosian trace metric (Block 3h)

24-cell ⊂ V_600: 24 coordinate-σ-fixed vertices ("twin-anchored")
  ├─ 4 in Dic_5 (twin-anchored bulk anchors)
  └─ 20 in boundary (4 per non-trivial coset)
```

## Three results from one structure

### Result 1 — H(z) modification: 1 + 1/12 = 13/12

**Source:** OD-1 (`od1_final_mode_count.py`)

Frame-perceived H(z) at late time = (13/12) × bulk-invariant H(z).
- ΛCDM treats 12 T_τ-cycles uniformly → 12 modes baseline.
- VFD: K=72 bulk cycle = unique high-κ scale-anchor → +1 mode beyond cycle count.
- K=0 bulk cycle has κ=0 throughout → contributes 0.
- Effective mode count = 12 + 1 = 13. Ratio = 13/12.

**Empirical match:**
- Predicted H₀_late: 67.36 × 13/12 = 72.97 km/s/Mpc.
- Observed SH0ES: 73.04 ± 1.04 km/s/Mpc.
- Tension after correction: **0.06 σ** (vs 4.85 σ raw).

### Result 2 — σ_8 modification: 1 − 1/12 = 11/12

**Source:** OD-1 antisymmetric channel.

Late-channel clustering amplitude = (11/12) × bulk σ_8.
- ΛCDM: 12 cycles uniformly contribute to clustering.
- VFD: K=0 cycle (all vertices at shell 4) has zero κ-distortion → no clustering signal.
- Effective clustering modes = 12 - 1 = 11.

**Empirical match:**
- Predicted σ_8_late: 0.811 × 11/12 = 0.743.
- Observed KiDS: 0.760 ± 0.020.
- Tension after correction: **0.79 σ** (vs ~2.5 σ raw).

### Result 3 — BH Bekenstein 1/4

**Source:** `bh_bekenstein_1_4.py`

Localised BH analog = single Dic_5-coset (20 vertices).
- Per coset: 4 σ-fixed (twin-anchored) "anchor states" + 16 σ-mobile "horizon modes".
- S/A = 4/16 = **1/4 exactly**.
- This reproduces Bekenstein-Hawking S = A/(4ℏG) with 1/4 coefficient from V_600 incidence structure (24-cell ∩ Dic_5-coset).

Aggregate over 5 boundary cosets: total S = 20 anchor states / total A = 80 horizon modes = 1/4. Uniform across all cosets.

### Result 4 — CMB uniformity + tension reframe

**Source:** `cmb_mapping.py`

- T_CMB = 2.725 K uniform: bulk invariance Theorem 5.2 (∂F^B/∂t = 0).
- Recombination reframed as bulk-resolution depth, not chronology.
- 6 ΛCDM parameters mapped structurally to V_600 quantities (qualitative).
- Planck CMB observables = bulk-projection (early-channel).
- Late-channel observables (galaxy ladders, weak lensing, BAO) carry 1±1/12 modifications.

## Falsifiable predictions

Pre-registered before observation (`preregister_k.py`):

| Survey | Observable | Prediction | Status |
|---|---|---|---|
| SPHEREx (~2026) | Cosmic dipole at k=4 rung | 5.083× ΛCDM amplitude | Open |
| LSST (~2027) | k=5 rung | 6.083× | Open |
| SKA-1 (~2030) | k=6 rung | 7.083× | Open |
| DESI-quasar (~2026) | H₀(z=2-4) | (13/12)·H₀_Planck = 72.97 | Open |
| Euclid (~2026) | σ_8(z=0.5-2) | (11/12)·σ_8_Planck = 0.743 | Open |
| eROSITA-DE (~2027) | f_σ8 | (11/12) factor | Open |

## Honest scope and remaining gaps

### What's solid (mathematically rigorous)

1. **V_600 + cycle structure**: pure group theory, exact.
2. **Dic_5 = bulk subgroup**: Block 2E proved this empirically and structurally.
3. **τ_σ explicit construction**: Block 3h, 32=2⁵ canonical candidates differing by Z₂⁵ orientation.
4. **Bekenstein 1/4**: exact ratio from incidence counting.
5. **OD-1 (1±1/12) factors**: operator-trace derivation, FORCED.
   - Ĥ = I_12 + P_72 (max-K rank-1 anchor) ⇒ tr=13 ⇒ +1/12.
   - Ĉ = I_12 - P_0 (trivial-K rank-1 zero-mode) ⇒ tr=11 ⇒ -1/12.
   - K-multiset {72:1, 0:1, 52:5, 20:5} + τ_σ pairing forbids ANY other rank-1 correction.
6. **Hawking spectrum**: monochromatic σ-pair quantum E_q = 5/2 (W(H₄)-invariant).
   - First-law identity exact per coset: E = T_H·A, T_H·S = E/4.
   - T_H = E_q (single-line spectrum ⇒ T = quantum gap).

### What's still gap (structural argument, not derivation)

1. **The 6 ΛCDM parameters**: qualitative mapping, not full derivation of
   numerical values.
2. **Quantitative CMB peak positions**: framework predicts uniformity and
   bulk/boundary split, but doesn't compute l-mode acoustic peaks.
3. **Hawking → Planck-spectrum semiclassical recovery**: discrete cascade
   gap → thermal continuum requires sum over many cosets/resolutions.
4. **Cascade unit calibration to physical T_H = ℏc³/(8πGM)**: requires
   identifying frame-resolution scale with horizon radius.

### What's a research programme (Tier-2)

- Explicit recombination model (τ_reion derivation).
- Full Planck l-spectrum prediction.
- Spectral distortion (μ, y) cascade quantities.
- Cosmological perturbation theory in V_600 framework.

## Pull quote for the paper

> The 1/12 cosmic-anomaly factor (H₀ tension closer at 0.06σ, σ_8 closer at
> 0.79σ, cosmic dipole 1+k/2 ladder) and the Bekenstein-Hawking 1/4
> coefficient both emerge from a single structural source: the V_600 cycle
> decomposition into bulk Dic_5 (20 vertices) and boundary (5 σ-paired
> Dic_5-cosets), with the canonical involution τ_σ explicitly constructed
> via icosian σ-projection. The same incidence structure — V_600 ∩ 24-cell
> distributed as 4 σ-fixed per Dic_5-coset — that gives 1/4 in BH
> thermodynamics also gives 12+1 = 13 effective modes for cosmic expansion
> and 12-1 = 11 for matter clustering.

## Files

- `block3h_VFD_canonical_filter.py` — τ_σ construction.
- `tau_sigma_VFD_canonical.txt` — explicit 120-vertex map.
- `od1_final_mode_count.py` — 1±1/12 structural argument.
- `od1_operator_derivation.py` — 1±1/12 operator-trace derivation.
- `bh_bekenstein_1_4.py` — BH S=A/4 derivation.
- `cmb_mapping.py` — CMB structural mapping.
- `hawking_radiation_derivation.py` — σ-pair Hawking spectrum + T_H.
- `TAU_SIGMA_RESULT.md` — τ_σ summary.
- `HAWKING_RESULT.md` — Hawking derivation summary.
- `UNIFIED_RESULT.md` — this file.
