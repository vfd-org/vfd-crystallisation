# Preregistration: H₄ Geometric Fingerprint Falsification Battery

**Frozen:** 2026-04-24.
**Basis:** Codex design round + Claude Code consensus
(`review/consensus/1777044153_wo_h4_fingerprint_design.md`).
**Derivation behind predictions:**
`vfd-crystalisation-paper/papers/cascade-derivation/cascade-h4-oscillator-law.md`.

This document locks decision rules BEFORE any code runs on real data.
Any change to this document after first data-look invalidates the test
and requires a new preregistered document.

---

## Hypotheses

### H1 (Constant 1 — Coxeter 11:1 spectral ratio)
Subject-level γ-peak / θ-peak ratio clusters at the Coxeter exponent
ratio m₁₁/m₁ = 11.0, against broad biological null [4, 25].

### H4 (Constant 4 — 12-fold PAC phase preference)
θ-γ phase-amplitude coupling locks preferentially to the 12 icosahedral
vertex angles (harmonic 12 of the θ-phase circle), against uniform null.

### H2 (Constant 2 — paired 2-torus PCA)
Cortical state-trajectory PCA shows exactly two dominant paired modes
(PC1-PC2, PC3-PC4) with eigenvalue structure |log(λ₁/λ₂)| < ε,
|log(λ₃/λ₄)| < ε, log(λ₂/λ₃) > δ, against unpaired monotone decay null.

### H5 (Constant 5 — 120-fold PAC kernel symmetry)
Staged after H4. PAC kernel has peak rotational power at harmonic 120
(or 12) above nearby harmonics' baseline.

### H3 (Constant 3 — α criticality, REVISED)
α estimated identically across ≥ 4 datasets, ≥ 80 subjects total,
clusters at 2.85 ± 0.15 with tight dispersion.
**Current status: existing n=30 Sleep-EDFx gives 2.51, so default prior
is REJECT until contradicted.**

### H6 (Constant 6 — φ-scaled cross-scale slopes)
Deferred. Reopen only if H1+H2+H4 confirm.

---

## Preprocessing (frozen, identical across signatures)

- **Line-noise notch:** 50 Hz and harmonics (EU data) or 60 Hz (US data)
  via IIR notch, Q=30.
- **Bandpass:** 0.5 - 100 Hz (wide). Per-signature sub-band filters apply
  downstream.
- **Epoching:** 60-second non-overlapping epochs; reject epochs with
  peak-to-peak amplitude > 5·median (gross artefact).
- **Rereferencing:** common average (scalp EEG) or bipolar (ECoG) where
  montage-appropriate; no re-referencing for MEG.
- **Sampling rate:** preserve native sampling; do not downsample below
  250 Hz (Nyquist covers γ).

---

## H1 — Constant 1 test protocol (locked)

### Bands
- θ search range: [4.0, 8.0] Hz
- γ search range: [30.0, 100.0] Hz
- Excluded from γ search: [48, 52], [58, 62], [98, 102] Hz (line noise
  plus harmonic).

### Peak-picking algorithm
1. Per-channel Welch PSD on each 60-s epoch (4-s Hann window, 50% overlap).
2. Fit 1/f background via FOOOF (`fooof` Python package, default
   parameters) over [1, 120] Hz, exclude known peak regions.
3. Detrended spectrum = raw - 1/f fit.
4. In θ band: pick argmax of detrended spectrum. Require prominence
   > 1.5 × MAD(detrended). If no peak meets prominence, mark epoch as
   NO-θ-PEAK.
5. In γ band: same procedure. Exclude line-noise sub-bands.
6. **Do not search γ near 11·f_θ.** Search full γ band.
7. Epoch ratio r_{ch,ep} = f_γ / f_θ if both peaks detected, else NaN.

### Subject statistic
r_s = median over all (channel, epoch) pairs with both peaks detected,
provided subject has ≥ 5 valid (ch, ep) pairs. Subjects with < 5 pairs
are excluded.

### Group statistic
Group median m_r = median(r_s over subjects). Group 95% CI via bootstrap
(10,000 resamples).

### Decision rule
**PASS:** 95% bootstrap CI on m_r lies within [10.0, 12.0] AND matched-
spectrum null permutation test rejects uniform-null at Holm-corrected
α = 0.05 (corrected across 4 primary signatures C1, C2, C4, C5).
**FAIL:** CI outside [10.0, 12.0] or null test fails to reject.
**INCONCLUSIVE:** CI overlaps both [10, 12] and outside, or < 18
subjects qualify.

### Nulls
1. **Sanity control (non-inferential):** phase-shuffled surrogate of
   each epoch's Fourier phases. Must reproduce m_r to within 10% (proves
   peak picker is stable).
2. **Inferential null:** matched-spectrum 1/f noise generated per
   channel by sampling from the fitted 1/f model without the θ/γ peaks
   added. Ratio distribution under null should be uniform in
   log(γ band) / log(θ band) ≈ log(100/30)/log(8/4) ≈ 1.74 in natural
   coordinates; mean expected null ratio ≈ exp(mean log γ) / exp(mean log θ)
   ≈ 55/5.7 ≈ 9.6. H₁ requires observed to exceed null plus δ = 1.0.

### Sample size and power
Target ≥ 30 subjects per dataset. Primary datasets in order:
1. Sleep-EDFx wake (n ≥ 30)
2. ds004902 rest (n ≈ 10)
3. ds003708 ECoG rest (n = 1, 76 channels — treat as 76 "subjects"
   with Gelman-style multilevel correction)

Power calculation: N = ((z_{0.975} + z_{0.8}) σ_log / δ_log)² with
σ_log = 0.15, δ_log = 0.10 → N ≈ 18. Safety factor × 1.7 → 30.

### Datasets frozen for primary analysis
- `~/.aria/datasets/physionet_sleep_edfx/` — wake stage W only
- `~/.aria/datasets/openneuro_ds004902/` — eyes-closed rest
- `~/.aria/datasets/openneuro_ds003708/` — pre-stimulation rest window

### Datasets NOT used for primary (reserved for replication)
- `openneuro_ds005620` (propofol) — reserve
- `zenodo_dmt_eeg` — reserve
- `hcp_ptn1200` (MEG) — reserve for H2

---

## H4 — Constant 4 test protocol (locked)

### Measurement
Staged after H1. Preregistration of H4 details deferred to a later
document IF H1 passes; but high-level protocol is fixed now:

- Hilbert θ-phase, γ-amplitude envelope on the same epochs as H1.
- Primary 12-fold PLV: R₁₂ = |Σ A_γ(t) exp(i·12·φ_θ(t))| / Σ A_γ(t)
- Absolute-grid statistic: d₁₂ = min_k |wrap(μ − kπ/6)|,
  μ = arg Σ A_γ(t) exp(i φ_θ(t))
- Null: phase-shuffled θ-γ alignment; matched-spectrum simulated noise.

### Decision rule
R₁₂ significantly > null (Wilcoxon signed-rank, Holm-corrected).

---

## H2 — Constant 2 test protocol (locked)

### Measurement
- Primary dataset: ds003708 ECoG (76 channels) for pilot; HCP MEG for
  confirmation (deferred).
- Channel × time matrix X. Covariance C = X X^T / T.
- Eigenvalues λ₁ ≥ λ₂ ≥ …, compute:
  - D₁₂ = |log(λ₁/λ₂)|
  - D₃₄ = |log(λ₃/λ₄)|
  - G₂₃ = log(λ₂/λ₃)
  - T₂ = G₂₃ − D₁₂ − D₃₄

### Decision rule
PASS if D₁₂ < 0.1, D₃₄ < 0.1, G₂₃ > 0.5, AND T₂ significantly > null
(matched-spectrum channel-independent simulated noise).

---

## H5 — Constant 5 test protocol (locked)

Staged after H4. Same PAC pipeline with phase-bin resolution ≥ 240 bins.

S_h = P_h / median(P_j over j ∈ {h-5, ..., h+5} \ {h}).

Targets: h = 12 and h = 120, both preregistered.

---

## Multiple comparisons correction

Holm correction across the 4 primary signatures (C1, C2, C4, C5) at
family-wise α = 0.05. C3, C5 (h=120), C6 are secondary; corrected within
their own family at α = 0.05.

## Analysis freeze

Once data has been touched for any signature:
- No further changes to this document.
- No filter/band retuning.
- Any exploratory deviation from this protocol is reported as
  EXPLORATORY in the paper, not primary.

## Paper framing commitment

- Section 1: preregistration declared.
- Section 2: protocol (this document reproduced).
- Section 3: results (positive OR negative, per-hypothesis).
- Section 4: interpretation under full H₄ framework.
- Section 5: rescues considered and rejected / accepted (preregistered).

## Authors

- ARIA substrate + H₄-derivation: Claude Code + Codex pair (this session)
- Experimental implementation: Claude Code + Codex pair (next session)
- Data curation: pre-existing downloads under `~/.aria/datasets/`

---

**END OF PREREGISTRATION — FROZEN 2026-04-24.**
