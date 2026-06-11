# Preregistration: Rung-Specific Observable Battery for Cortical Cascade Reading

**Frozen:** 2026-04-24, BEFORE data analysis.
**Context:** 4-lens H₄ test was negative; per cascade substrate-indexing
(P-A, G6.4, QMS-2 L40-YES), that's the *predicted* outcome if EEG reads
at a downstream rung rather than the H₄ substrate rung. This preregistration
tests which rung cortical EEG/ECoG actually reads at.

**Hypotheses (mutually exclusive to first order):**

### H-L40 (quaternion 1+3 split)
Per QMS-2 L40-YES, the biological rung preserves
H = span{1, e₁, e₂, e₃} ⊂ O, i.e. 1 scalar + 3 vector axes. Channel-PCA
of band-limited cortical activity should show:
- **S-dominance:** λ₁ / Σᵢ₌₁⁴ λᵢ ≥ 0.40 (scalar mode dominant among top 4).
- **V-equality:** std({λ₂, λ₃, λ₄}) / mean({λ₂, λ₃, λ₄}) ≤ 0.25 (3 vector
  axes approximately equal in power).
- **4-gap:** λ₄ / λ₅ ≥ 1.5 (gap after the 1+3 structure).

### H-Cl13 (Clifford 1+3+3+1)
Cl(1,3) has grades: scalar (1), vector (3), bivector (3), pseudoscalar (1)
= 8 components. PCA should show:
- **Blocks:** mean{λ₁}, mean{λ₂..₄}, mean{λ₅..₇}, mean{λ₈} form 4 distinct
  blocks with ratios close to [4, 3, 2, 1] by cascade-predicted weighting.
- **Within-block equality:** std within each block / mean within block
  ≤ 0.25.
- **8-gap:** λ₈ / λ₉ ≥ 1.5.

### H-S7 (S⁷ observer, 8-fold equal)
S⁷ ⊂ O has 8 axes (1 real + 7 imaginary unit octonions). If observer rung
is S⁷ and reads uniformly, PCA should show:
- **8-equal:** std({λ₁..₈}) / mean({λ₁..₈}) ≤ 0.25 (all 8 modes
  approximately equal).
- **8-gap:** λ₈ / λ₉ ≥ 1.5.

## Null (inferential)
Matched 1/f noise (same per-channel spectrum, independent across channels)
— gives approximately exponential eigenvalue decay with no gap structure.

## Decision rule per rung
- **PASS:** all 3 criteria of a rung satisfied in ≥ 50% of subjects AND
  matched-null does not.
- **FAIL:** any criterion violated in ≥ 50% of subjects OR null passes.

## Datasets (in order)
1. **ds003708 ECoG** — 76 channels, cleanest; primary test (n=1, channel-
   level statistics with time-window bootstrap).
2. **ds004902 scalp EEG** — 61 channels, n=20; cross-modality check.
3. **Sleep-EDFx** — 2 channels, insufficient for PCA; excluded.

## Multiple comparisons
3 rungs × 2 datasets × 3 frequency bands (α, β, γ) = 18 decisions.
Holm correction at family-wise α = 0.05.

## Frequency bands (pre-frozen)
- α = 8-13 Hz
- β = 13-30 Hz
- low-γ = 30-80 Hz (ECoG can resolve; scalp clipped at 50 Hz by
  Sleep-EDFx Nyquist but ds004902 at 500 Hz can see low-γ)

## Anti-tuning clauses
- No post-hoc band adjustments.
- No eigenvalue-index shifts (e.g. testing 2+3 instead of 1+3 because
  λ₁ alone doesn't dominate).
- ds003708 is one subject; channel-level statistics only, no population
  claim.

## Paper framing commitment
- PASS for any rung: report as "cortex reads at rung X."
- FAIL for all three: the cascade-reading framework is undermined, not
  just the naive H₄ mapping.
- Mixed results: report faithfully; no cherry-picking.

---

**FROZEN 2026-04-24, preregistered before any analysis.**
