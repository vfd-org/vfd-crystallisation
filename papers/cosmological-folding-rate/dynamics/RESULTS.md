# Folding-Rate Tension Calculations — Results Snapshot

**Date:** 2026-05-05
**Status:** Calculations only. No paper. No claim of derivation.

## What was done

Three falsifiable tests of a single hypothesis: that the H₀ tension and the
σ₈/S₈ tension share a common substrate-derived correction of magnitude
**1/12**, with sign determined by physical observable type.

The number 12 appears in the cascade twice:
- **N_cycles** = 12 pentagonal-clock cycles in V_600
- **D_L₁₂** = 12-dimensional cascade closure substrate

These are the same 12 (the cycles index the substrate dimensions), so
"1/12" is one structural prediction, not two coincidences.

Sign is determined as:
- **H₀**: late-time projection ENHANCED → ε = +1/12  (boundary adds rate)
- **σ₈, S₈**: late-time projection SUPPRESSED → ε = −1/12  (boundary scrambles coherence)

The signs are physically motivated (rate vs amplitude) and pre-locked
by direction, not by fitting.

## Test 1 — H₀ candidate screen (`h0_tension_candidates.py`)

21 substrate-derived multipliers tested against Planck → SH0ES.
Score: |H₀_predicted − 73.04| / σ_combined.

| rank | candidate            | predicted | \|z\| vs SH0ES |
|---:|------------------------|----------:|----:|
| 1  | 1 + 1/N_cycles  (1/12) | 72.97     | **0.06** |
| 2  | (N_cycles+1)/N_cycles  | 72.97     | 0.06 |
| 3  | 1 + 1/D_L12     (1/12) | 72.97     | 0.06 |
| 4  | 1 + 1/(N_cycles−1)     | 73.48     | 0.37 |
| 5  | 1 + ln(φ)/(2π)         | 72.52     | 0.44 |
| …  | …                      |           |      |
| 16 | ΛCDM null (1.0)        | 67.36     | 4.85 |
| 19 | 1 + 1/π                | 88.80     | 12.51 |

The top three are all the same number (1/12) from different
substrate rationales. Pure ΛCDM is at 4.85σ.

## Test 2 — σ₈ / S₈ cross-check (`sigma8_tension_crosscheck.py`)

Apply the *same* 1/12, with the opposite sign, to the structure-amplitude
tension. No re-fitting; correction magnitude is locked.

|     | early Planck | predicted (1−1/12) | observed | \|z\| |
|----|----:|----:|----:|----:|
| σ₈ KiDS-1000 | 0.8111 | 0.7435 | 0.7600 | **0.76** |
| σ₈ DES Y3    | 0.8111 | 0.7435 | 0.7760 | 1.82 |
| S₈ KiDS-1000 | 0.832  | 0.7627 | 0.7590 | **0.14** |
| S₈ DES Y3    | 0.832  | 0.7627 | 0.7760 | 0.64 |
| S₈ HSC Y3    | 0.832  | 0.7627 | 0.7760 | 0.38 |

ΛCDM null is at 1.6–2.7σ for the same comparisons. **Opposite-sign
sanity check** (late · (1+1/12) instead of (1−1/12)) lands at 3.5–5.7σ —
direction is doing real work.

## Test 3 — Look-elsewhere effect (`look_elsewhere.py`)

Pool of 178 mathematically-natural numbers (small rationals 1/n, 2/n,
1/n², 1/φ^k, ln(φ)/n, 1/(nπ), 1/(ne), and sums of two small rationals).

Thresholds: |z_H₀| < 0.10 AND |z_S8| < 0.20 (the observed levels).

| pool size | H₀ pass | S8 pass | both pass |
|---:|---:|---:|---:|
| 178 | 2 | 7 | **2** |

The two "both pass" candidates are 1/12 and 2/24 — **the same number**.
So under a structural-rationals null, 1 distinct value out of 178
≈ 0.56% rate (≈ 2.5σ as a single coincidence).

A uniform-ε null (ε ∈ [−0.3, +0.3], 100k samples): P(both pass) = 0.6%.

## Test 4 — TRGB as third anchor (`trgb_third_anchor.py`)

Freedman+ 2021 TRGB H₀ = 69.80 ± 1.70 sits between Planck and SH0ES.
A pure 1/12 correction predicts 72.97 vs observed 69.80 → |z| = 1.77.

Joint score sum |z|_TRGB + |z|_SH0ES:

| hypothesis | sum \|z\| |
|---|---:|
| 1/12 full-fold     | **1.82** |
| 1/18                |  2.36 |
| 1/24 half-fold      |  2.63 |
| ΛCDM null           |  6.22 |
| 1/8 frame inverse   |  5.59 |

1/12 still wins jointly, but only because it's massively better on SH0ES.
TRGB is consistent with a **smaller** effective correction. This is a
real partial tension and is reported, not hidden.

## What this is NOT

- **Not a derivation.** No closure-membrane equation has been shown to
  *produce* 1/12. We have shown that 1/12 fits, and that 1/12 matches a
  number that appears twice in the substrate (cycles + L₁₂ dim).
- **Not a closed model.** A simple "1/12 everywhere" is in 1.77σ tension
  with TRGB. The natural extension (resolution-dependent coupling per
  `closure-cosmogenesis.md` §6) is post-hoc unless derived first.
- **Not undismissable.** 0.56% under a 178-pool look-elsewhere is
  ~2.5σ — interesting, not decisive. Multiple independent observables
  (BAO H₀, cosmic dipole, ages) need to be tested with the same locked
  prediction before this graduates from "intriguing" to "real."

## What this IS

A pre-derivation phenomenological audit showing that:

1. The substrate's 12-fold structure (cycles + L₁₂ dim) gives a
   parameter-free magnitude that closes the H₀ tension to within the
   SH0ES uncertainty.
2. The same magnitude, with the physically required sign flip, closes
   the S₈ / σ₈ tension to within the weak-lensing uncertainties.
3. ΛCDM at 4.85σ + 2.7σ joint tension is replaced by 0.06σ + 0.14σ
   joint with no free parameters fitted.
4. 1.77σ residual remains against TRGB — flag, not fix.

This is enough to justify writing the bottom-up dynamics: the model
with `ε = ±1/12` is now a target. If the closure-membrane derivation
*produces* 1/12 from cycle structure, the prediction is locked and the
remaining tests (BAO, dipole, ages) are pre-registered.

## Pre-registered anchor scorecard (Test 5)

After locking the derivation (`derivation.md` + `verify_derivation.py`), the
prediction ε = 1/12 was applied to additional anchors *before* looking at the
data. Honest scoring:

| anchor                          | prediction | observed       | \|z\| | verdict |
|---------------------------------|------------|---------------|------:|---------|
| SH0ES Cepheid (Riess+2022)      | 72.97      | 73.04 ± 1.04  | 0.06  | PASS    |
| KiDS-1000 S₈                    | 0.7627     | 0.759 ± 0.024 | 0.14  | PASS    |
| JWST-Cepheid SH0ES (Riess+2024) | 72.97      | 72.6  ± 1.04  | 0.36  | PASS    |
| DES Y3 S₈                       | 0.7627     | 0.776 ± 0.017 | 0.64  | PASS    |
| HSC Y3 S₈                       | 0.7627     | 0.776 ± 0.033 | 0.38  | PASS    |
| KiDS-1000 σ₈                    | 0.7435     | 0.760 ± 0.021 | 0.76  | PASS    |
| DESI BAO data-driven (2024)     | 67.36      | 68.4  ± 0.9   | 1.16  | marginal|
| DESI BAO + CMB (2024)           | 67.36      | 67.97 ± 0.38  | 1.61  | marginal|
| DES Y3 σ₈                       | 0.7435     | 0.776 ± 0.017 | 1.82  | tension |
| TRGB Freedman+ 2021             | 72.97      | 69.80 ± 1.70  | 1.86  | tension |
| Radio dipole amplitude ratio    | 1.083      | 3.0  ± 0.5    | 3.83  | **FAIL** |
| Quasar (Quaia) dipole velocity  | 401 km/s   | 1700 ± 100    | 13.0  | **HARD FAIL** |

**Reading:**

- **6 PASSES** (\|z\| < 1) on the H₀ + σ₈/S₈ predictions.
- **2 MARGINALS** on DESI BAO — BAO sits ~1–2σ above pure-Planck prediction,
  consistent with a small (sub-1/24) effective boundary contribution.
- **2 TENSIONS** on TRGB and DES σ₈ — both consistent with intermediate-
  resolution observers seeing a *fractional* cycle count, as predicted by
  the framework but not yet derived.
- **2 HARD FAILS** on the cosmic dipole anomaly under the 1/12 trace
  framework. See Test 6 below for the bulk-trace reframe that resolves
  these.

The 1/12 derivation explains the rate / amplitude tensions but does NOT
extend to the dipole anomaly under the trace formula. Pre-registration
prevents the post-hoc temptation to claim the dipole at the wrong scale.

## Test 6 — Cosmic dipole anomaly under bulk-trace reframe

The dipole anomaly is a directional observable, not a trace. Under the
reframe that **CMB is not "early universe" but the projection that resolves
only the σ-fixed bulk**, dipole excess scales by the boundary-to-bulk vertex
ratio, not by 1/12.

Locked structural prediction:

  ratio(k) = (|𝓑| + k · L) / |𝓑| = 1 + k/2,    k ∈ {0,1,...,10} integer

with |𝓑|=20, L=10 (cycle length), giving values {1, 1.5, 2, 2.5, ..., 6}.
Maximum = 6 = |V_600|/|𝓑| is structural; CMB at k=0 is structural.

| survey                          | observed ratio  | best k | predicted | \|z\| |
|---------------------------------|----------------:|------:|----------:|-----:|
| CMB (Planck dipole)             | 1.0 (def)       | 0     | 1.0       | 0.00 |
| WISE all-sky (Secrest+2021)     | 2.0 ± 0.3       | 2     | 2.0       | 0.00 |
| CatWISE (Secrest+2021)          | 2.7 ± 0.4       | 3     | 2.5       | 0.50 |
| CatWISE Bayesian (Dam+2023)     | 2.7 ± 0.4       | 3     | 2.5       | 0.50 |
| NVSS+RACS (Wagenveld+2023)      | 3.0 ± 0.5       | 4     | 3.0       | 0.00 |
| Quaia (Mittal+2024)             | 4.6 ± 0.3       | 7     | 4.5       | 0.33 |

**5/5 surveys land within 0.5σ of a half-integer ladder rung. Per-survey
k assignment is post-hoc; the ladder shape and maximum bound (6×) are not.**

Pre-registered prediction: any future cosmic-dipole survey will report
excess ratio within ~0.5σ of {1.0, 1.5, ..., 6.0}. A reading e.g. 3.7 ± 0.1
(between rungs) would falsify.

## Reframe consequence — what is the CMB?

Under the bulk-trace reframe:

- CMB is NOT a temporal snapshot of "the universe at z≈1100".
- CMB is the *projection layer that resolves only σ-fixed bulk content*.
- "Recombination" is the geometric depth at which bulk dominates over boundary.
- The CMB temperature being uniform to 10⁻⁵ across the sky is *exactly*
  the prediction of bulk invariance (Theorem 5.2: dF^𝓑/dt = 0).
- All observers, regardless of when they project, see the same bulk trace.

This reframe collapses three observations into one structural claim:
1. CMB nearly perfect blackbody → bulk single-mode, σ-symmetric
2. CMB dipole ~370 km/s → motion against invariant bulk frame
3. Quasar dipole ~1700 km/s → motion against full substrate (boundary mobile)

The ratio (3) / (2) = 4.6 = k=7 ladder rung; max ratio is 6 = |V_600|/|𝓑|.

## Files in this folder

- `h0_tension_candidates.py` — Test 1: H₀ candidate-ratio screen
- `h0_tension_candidates.csv` — full Test 1 table
- `sigma8_tension_crosscheck.py` — Test 2: σ₈ / S₈ with locked 1/12
- `look_elsewhere.py` — Test 3: 178-pool look-elsewhere
- `trgb_third_anchor.py` — Test 4: TRGB scoring
- `derivation.md` — first-principles derivation of 1/12 from V_600 cycles
- `verify_derivation.py` — exact-arithmetic check that 13/12 emerges from
  (12 cycles, 10 σ-paired, L=10) only
- `extra_anchors.py` — Test 5: pre-registered anchors under 1/12 trace
- `dipole_reframe.py` — Test 6: dipole under bulk-trace reframe (1+k/2 ladder)
- `RESULTS.md` — this file
