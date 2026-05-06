# FIELD-SIGNATURE AUDIT — cascade-mechanism paper

**Date:** 2026-05-02
**Purpose:** Before drafting `cascade-mechanism.tex`, re-run the load-bearing
sims that the paper rests on. The data — not the narrative — decides
whether each section is data-supported, conditional, or out-of-scope.

This audit is the empirical anchor for the eventual `.tex` paper. Every
load-bearing data claim in the paper must point back to one row of this
audit (or a comparable re-runnable sim).

---

## Verdict: GO

All five load-bearing sims passed at the precision claimed in the source
papers. The data also surfaced three honest-negatives that constrain the
paper's scope — these are not failures, they are the system telling us
where the conditional boundaries genuinely sit.

---

## Audit results

### A. σ-attractor spectrum (RH + Millennium scaffolding)

**Script:** `papers/cascade-derivation/scripts/test_sigma_attractor_spectrum.py`
**Status:** GREEN (Q1) + HONEST-NEGATIVE (Q2)

- Q1 σ-fixed fraction: **94/120 = 78.3%** (target ≥ 50% — passed by ≈1.6×).
  σ-fixed eigenvalues are the **five integer eigenvalues**
  λ ∈ {0, 9, 12, 14, 15} (fixed under σ(φ) = 1−φ = −1/φ);
  σ-paired are the four irrational eigenvalues in Q(√5).
- Q2 2T-localisation: **0.200 vs baseline 0.200 (target ≥ 1.5× baseline) —
  MISSED**. σ-fixed eigvecs do NOT preferentially localise on the binary
  tetrahedral subgroup 2T.

**What this tells the paper.** The 78.3/21.7 spectral split is unconditional
and is the principal RH-projection-class witness on V_600. The 2T-localisation
hypothesis is empirically unsupported, so the paper must NOT use 2T
concentration as an additional witness — only the spectral count survives.
The sim itself flags: "conversion to a critical-line Mellin-shadow zero
claim requires the additional spectral-mode → Mellin-zero correspondence
(Conjecture conj:spec_to_zero in rh-formal), which is not established by
this script." This anchors the WO §8 verdict-discipline language ("RH
stays conditional on `H_{sigma-fix}`").

### B. Mass-spectrum chain forward derivations (Paper V Revisited)

**Script:** `papers/paper-v/scripts/run_chain_forward_derivations_v2.py`
**Status:** GREEN — 9/9 forward at exact rational precision

| Coefficient | Expression | Value |
|---|---|---|
| Z = 87 | `3 (λ_5 + λ_7) = 3 (14 + 15)` | 87 ✓ |
| charm = 5/6 | `1 - R_I` | 5/6 ✓ |
| W = 5/2 | `N/2` | 5/2 ✓ |
| down = 2 | `R_D(3)` | 2 ✓ |
| bottom = 43/6 | `V_3/6 + R_I` | 43/6 ✓ |
| Higgs = 39/2 | `(R_D(4) + R_D(3) V_1) / R_D(3)` | 39/2 ✓ |
| muon = 8/3 | `V_2 / V_1` | 8/3 ✓ |
| tau = 23/8 | `(λ_5 + λ_3) / (λ_3 - V_5)` | 23/8 ✓ |
| strange = 9/8 | `λ_3 / (λ_3 - V_5)` | 9/8 ✓ |

Plus structural EM-splitting reclassification of neutron via
forward-traceable α correspondence. **What this tells the paper.** The
spectral-mass projection class (Section 7 case-study row) has 9 exact
forward identities + 1 sin²θ-level neutron correction — not theorem-grade
across the board, but the load-bearing factual core is unconditional.

### C. YM Build B_YM_P8 — Der(O) and stab(e_1)

**Script:** `papers/millennium-ym/scripts/verify_der_O_su3_stabilizer.py`
**Status:** GREEN — exact rational arithmetic; no prior g₂/su(3) assumption

- `dim Der(𝕆) = 14` (g₂, classical Schafer-Jacobson). Confirmed by
  rank(A) = 7 ⇒ dim = 21 - 7 = 14.
- `dim stab_{Der(𝕆)}(e_1) = 8` (su(3), classical). Confirmed by
  rank = 13 ⇒ dim = 21 - 13 = 8.

**What this tells the paper.** The YM projection-class substrate
(octonion derivation algebra) is unconditional at the algebra-dimension
level. The remaining mass-gap claim depends on `H_{OS-lift}`, which the
paper must keep flagged. WO §8 verdict-table already encodes this.

### D. Pentagonal-clock B5/B6 — order-10 cycle structure on 2I

**Script:** `papers/cascade-derivation/scripts/derive_pentagonal_clock_B5_B6.py`
**Status:** GREEN

- B5: order-10 class canonical (24 elements = 2 conjugacy classes of 12);
  τ⁵ = -1 confirmed.
- B6: left-mult clock T_τ decomposes 2I into 12 cycles of length 10.
  Fix(T^n) = ∅ for 1 ≤ n < 10; Fix(T^10) = 2I (all 120).
- Unweighted Artin-Mazur zeta: ζ_T(z) = (1 - z^10)^{-12}. Exact.

**What this tells the paper.** The pentagonal-clock cycle structure
K = {72, 0, 52, 20} is well-defined and B5–B6 fixtures hold at the
group-theoretic level. WO §8 cites this for the RH `ẑ(z)` Mellin object.

### E. Closure kernel passive-regime witness (b-anomaly substrate)

**Script:** `papers/aria-closure-kernel/repro/verify_kernel.py`
**Status:** GREEN + HONEST-NEGATIVE on weighting

- Euclidean / conjugacy shell sizes match expected `[1, 12, 20, 12, 30, 12, 20, 12, 1]` exactly.
- `‖C_φ⁻¹‖ ≈ 2.618034`, matching `φ²` to machine precision (analytic identity from `λ_min(L_M)=0` plus the `φ⁻²` shift).
- Per-vertex correlation **uniform across the 120 source-vertex sweeps** (max-min ≈ 2e-15);
  this is a numerical diagnostic, not a discrete-to-continuum convergence theorem.
- **UNWEIGHTED variant wins** at per-vertex correlation 0.976, beating
  PHI_GEOMETRIC (0.888) and PHI_ARITHMETIC (0.884). **The two tested φ-cocycle
  weighted variants UNDERPERFORM the unweighted operator — consistent with the
  project_banomaly_kernel_alignment memory.**

**What this tells the paper.** The passive-regime b-anomaly witness rests
on the UNWEIGHTED kernel `C_φ = L + φ⁻²I`. The paper must NOT claim
weighted variants and must NOT claim model selection (the b-anomaly fit
is an AIC tie, not a preference). This is exactly what WO §6 / §7 already
encode.

### F. ARIA observer-process witness

**Source:** `papers/aria-chess-paper/paper/main.tex`.
**Status:** GREEN — 17/18 standard validation; 18/18 after methodology
refinement; 6/6 EEG signatures; HCP degree-homogeneity at −11.58σ
(clustering separately +6.80σ)

- **17/18 preregistered cortical correspondences** under standard
  validation; **18/18 after the documented methodology refinement**,
  all at unchanged thresholds (lines 51, 95).
- **6/6 drug/sleep EEG signatures** on a single deterministic
  recurrent-layer trajectory at seed 42 (lines 100, 127): propofol
  modality-switching drop, propofol continuity drop +0.066, etc.
- **HCP brain functional connectivity** degree-homogeneity (degree
  standard-deviation): ARIA at **−11.58σ** vs HCP baseline (line 163),
  establishing substrate distinguishability. The
  clustering-coefficient comparison is reported separately in the
  source as a **+6.80σ** result; the −11.58σ figure must not be
  conflated with clustering.

**What this tells the paper.** The observer-process architecture-level
mapping §5 has a **substrate-witness** (not consciousness-derivation)
anchor that the data already carries. The paper treats this as an
imported empirical fact, scoped to substrate-witness only — no
consciousness, qualia, or implementation-level claim is built on it.
The paper's claim-boundary discipline is calibrated against this
exact scope.

---

## Honest-negatives the paper must respect

The data refuses to support these claims, and the paper must NOT make them:

1. **σ-fixed spectral subspace has average 2T-mass at baseline** (basis-invariant
   projector trace ratio); the 78.3% σ-fixed split is the only spectral RH witness.
   No 2T concentration claim allowed.
2. **φ-cocycle weighted kernel variants LOSE to UNWEIGHTED.** Use
   `C_φ = L + φ⁻²I` only. No weighted-substrate selection claim.
3. **Spectral-mode → Mellin-zero is conjectural** (conj:spec_to_zero in
   rh-formal). RH-related claims stay under `H_{sigma-fix}`. No
   unconditional zero-location claim.

---

## Implication for paper structure

Every WO §6.1–§6.7 (ARIA observer-process), §7 (case studies), and §8
(Millennium scaffolding) entry is data-supported at the substrate /
finite-spectral / algebra-dimension / cycle-structure / shell level.
Every conditional boundary in WO §8 verdict-discipline is exactly where
the data also says "conjectural." The data calibration matches the WO
scope discipline 1:1 — go.

The eventual `.tex` paper should reproduce this audit table verbatim as
an appendix (call it `app:field-signature-audit`) so reviewers can
re-run the full empirical anchor in one pass.

## Re-run command (for reviewers / future self)

```bash
cd /path/to/vfd-crystalisation-paper
python3 papers/cascade-derivation/scripts/test_sigma_attractor_spectrum.py
python3 papers/paper-v/scripts/run_chain_forward_derivations_v2.py
python3 papers/millennium-ym/scripts/verify_der_O_su3_stabilizer.py
python3 papers/cascade-derivation/scripts/derive_pentagonal_clock_B5_B6.py
python3 papers/aria-closure-kernel/repro/verify_kernel.py
```

ARIA witnesses (E and F) are documented in
`papers/aria-chess-paper/paper/main.tex`; the upstream re-run lives in
the `aria-chess` repo cited as `@misc{ariaChessRepo}`.
