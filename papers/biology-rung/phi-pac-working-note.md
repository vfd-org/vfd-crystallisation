# Working Note: π/15 Phason Tick → Phase-Amplitude Coupling

**Status:** Exploratory hypothesis — pre-preregistration
**Date opened:** 2026-04-23
**Classification:** Cross-rung bridge (Life rung → adult-brain dynamics)
**Related programmes:**
- `aria-chess/docs/brain_mapping/` (mature: 15/18 preregistered hits)
- `papers/cascade-derivation/cascade-pentagonal-coxeter-bridge.md` (π/15 origin)
- `papers/paper-v/derivations/LAMBDA_15_PROOF.md` (600-cell eigenvalue λ=15)

---

## 1. The framework side (what we already know)

The number **15** and the phase quantum **π/15** appear in four independent
structural roles in the cascade / substrate architecture:

1. **600-cell Laplacian integer eigenvalue λ = 15** (multiplicity 16),
   a member of the mass-sector set **{9, 12, 14, 15}**.
2. **π/15 as the Coxeter phason tick**: all four H₄ rotation angles are integer
   multiples of π/15, i.e. {1, 7, 11, 13}·π/15. Equivalently,
   15 = h/2 where h = 30 is E₈'s Coxeter number.
3. **4π/15 ≈ 48°**: the σ-conjugate inter-spiral phase offset (corrects the
   legacy π/5 = 3π/15 intuition by a factor 5/4; G3 closed).
4. **Load-bearing in α⁻¹**: 3(14+15) = 87 gives one of three independent derivations
   of the 87 in α⁻¹ = 137 + π/87.

Summary claim: **π/15 is the framework's smallest phase quantum**, and the integer
set {9, 12, 14, 15} organises observable modes. If any dynamical system inherits
closure-geometric constraints, these numbers should appear as structural signatures
in its phase observables.

---

## 2. The neuroscience side (what the literature already contains)

Targeted web search (2026-04-23) for where 15, 0.15, π/15, and 4π/15 actually
appear in the neuroscience literature:

### 2.1 Cross-frequency n:m phase-phase coupling (strongest hook)

**Belluscio et al. 2012** (*J. Neuroscience* 32(2): 423–435) reported that
hippocampal theta/gamma coupling has *discrete* n:m peaks:

| Gamma band | Frequency | n:m ratio peak |
|---|---|---|
| Slow γ_S | 30–50 Hz | **m ≈ 4–6** (peak ~5) |
| Mid γ_M  | 50–90 Hz | **m ≈ 7–11** (peak ~9) |
| Fast γ_F | 90–150 Hz | **m ≈ 12–20** (peak region includes 15) |

The framework's mass-sector integers {9, 12, 14, 15} overlap the m = 9 (slow/mid
peak) and m = 12–15 (fast peak) regions directly. Not a fit to a single number
— a fit to the *set*.

Caveat: Scheffer-Teixeira & Tort (2016) reanalysis raised concerns about phase-phase
coupling artefacts from waveform asymmetry. The PAC (phase-amplitude) evidence is
more robust than phase-phase.

### 2.2 Sensorimotor beta at ~15 Hz

Low-beta (14–20 Hz) over sensorimotor cortex is a canonical band, functionally
distinct from high-beta (>24 Hz). **15 Hz sits near the centre of low-beta**,
consistent with a preferred resonance rather than a diffuse band.

### 2.3 Modulation Index (MI) and phase-bin resolution

- **Tort MI** (2010) uses KL-divergence from uniform across a histogram of
  phase-binned amplitudes. Standard choice: **18 bins** (20° each).
- **π/15 rad = 12°** corresponds to **30 bins per cycle** — a finer, framework-native
  alternative. Not currently a standard choice in the literature.
- Typical significant MI values for real data are ~10⁻⁴ to ~10⁻¹;
  MI ≈ 0.15 would be very strong coupling.

### 2.4 What does NOT appear in literature

- No canonical IIT Φ = 0.15 value (Φ is not reliably computable at brain scale).
- No "π/15 rad" or "4π/15" as named phase values in EEG/MEG literature.
- No standard PAC analysis using a 30-bin (π/15) histogram.

So the user's recollection of "0.15 from neuroscience" is most likely
**low-beta 15 Hz** (if about frequency) or **Belluscio m=15 fast-gamma peak**
(if about cross-frequency ratio). The cleanest framework hook is (2.1).

---

## 3. The bridge hypothesis

**H_PAC:** If adult-brain oscillatory dynamics inherit closure-geometric
constraints from the Life rung of the cascade, then observables that depend on
*phase quantisation* should preferentially lock to integer multiples of π/15,
and cross-frequency n:m ratios should cluster on the integer set {9, 12, 14, 15}
(with the set {5, 7, 11, 13} as the conjugate-spiral partner set from the
4π/15 = {8}·π/30 offset analysis).

This is a **distributional prediction** (the *set* shows up as discrete peaks),
not a point prediction on any single frequency.

---

## 4. Three specific preregistrable predictions

### P1 — Fast-gamma n:m peak at 15

**Test:** Replicate Belluscio-style n:m phase-phase analysis on CA1 theta /
fast-gamma (90–150 Hz), using surrogate-safe methodology (Scheffer-Teixeira &
Tort 2016 precautions). Predict a peak at **m = 15 ± 1**, with secondary
peaks at m = 12 and m = 14.

**Falsifier:** Flat distribution across 12–20, or a single dominant peak at
some non-cascade integer (e.g., m = 10, 16, 18).

**Effect size to beat:** Belluscio's reported m = 12–20 envelope has no internal
structure reported. A framework hit requires *resolvable peaks on {12, 14, 15}*
above the envelope baseline.

### P2 — Low-beta preferred frequency at 15 Hz

**Test:** In large resting-state MEG/EEG datasets (e.g. HCP, Cam-CAN),
fit a mixture of Gaussians to the low-beta (12–20 Hz) peak power spectrum per
subject. Predict the population-level central frequency at **15.0 ± 0.3 Hz**,
not e.g. 16 Hz or 17 Hz.

**Falsifier:** Central frequency reliably ≠ 15 Hz, or no unimodal peak at all.

**Pre-existing constraint:** The framework does not predict 15 Hz uniquely
*against* all other cascade-consistent frequencies. This is a *weak* test;
P1 and P3 are stronger.

### P3 — π/15 phase-bin quantisation in PAC

**Test:** Compute PAC modulation index for theta-gamma and alpha-gamma coupling
using two bin widths: the conventional 20° (18 bins) and the framework-native
12° (30 bins, = π/15). Ask: does the phase of peak gamma amplitude cluster on
integer multiples of π/15 across subjects, more than on multiples of π/9 (20°)?

Operational form: take the preferred-phase distribution across a large subject
pool, fit it against two uniform-multiple-of-π/N null models (N = 9 vs. N = 15),
and compare log-likelihoods.

**Falsifier:** No preference for π/15 over π/9 (or over continuous distribution).

### Bonus — {5, 7, 11, 13} conjugate-spiral signature

If the σ-conjugate H₄-plane structure is real, the "other" integer set
**{5, 7, 11, 13}** (from the upper π/15 coefficients) should appear as a
*secondary* mode, perhaps in contraction-phase dynamics (desynchronisation,
post-movement beta rebound, sleep-wake transitions). Untested, speculative.

---

## 5. What this working note is NOT

- Not a claim that the brain IS a 600-cell. Cascade predicts phase-quantum
  structure *on whatever dynamics inhabit* the Life-rung substrate; it does
  not specify the biophysical implementation.
- Not a replacement for the mature aria-chess brain-mapping thread. This is
  a *new* predictable signature to add to that preregistration pipeline, not
  a parallel programme.
- Not compatible with the legacy "π/5 = 3π/15" intuition. Any prediction
  derived from π/5 (e.g., 5-fold n:m peaks without a 4π/15 conjugate
  structure) is superseded by the G3 correction.

---

## 6. Next steps (not started)

1. Circulate to aria-chess/docs/brain_mapping/ maintainers — decide if P1–P3
   belong in that preregistration register or here.
2. For P1: identify a public dataset (Buzsáki Lab CRCNS hc-3 is canonical)
   and draft the analysis pipeline.
3. For P2: pull Cam-CAN / HCP-MEG peak-frequency distributions already in
   the literature; may not need new analysis.
4. For P3: requires new analysis — no standard toolbox ships with π/15 binning.

---

## 7. References (preliminary)

- Belluscio et al. (2012), *J. Neurosci.* 32(2):423–435.
  Cross-frequency phase-phase coupling, hippocampus.
- Scheffer-Teixeira & Tort (2016), *eLife* 5:e20515.
  Critique; waveform-asymmetry caveat.
- Tort et al. (2010), *J. Neurophysiol.* 104:1195–1210.
  Modulation Index, KL definition.
- Spitzer & Haegens (2017), *eNeuro* 4(4).
  Low-beta endogenous reactivation.
- Engel & Fries (2010), *Curr. Opin. Neurobiol.* 20:156–165.
  Beta oscillations as status quo.
