# (1 ± 1/12) modifications of H_0 and σ_8 — paper scope

**Working title:** *Operator-trace derivation of the (1 ± 1/12) Hubble and σ_8 modifications from the K-class structure of the 600-cell.*

**One-sentence pitch:** The H_0 tension closes at ≈ 0.06σ and the σ_8/S_8 tension lands within the published weak-lensing uncertainty via two rank-one K-class projector corrections to the identity on the 12-dimensional rational T_τ-cycle space of V_600 — Ĥ = I_C + P_72 (max-K bulk anchor) and Ĉ = I_C − P_0 (trivial-K bulk zero-mode) — whose trace ratios 13/12 and 11/12 are the only K-saturated rank-one diagonal projector corrections compatible with the K-multiset {72:1, 0:1, 52:5, 20:5}.

## Why this paper, why now

Paper 4 in the V_600 programme. Inherits V_600 + Dic_5 + V₂₄ from Paper 1 and τ_σ from Paper 3. Combines the H_0 and σ_8 results into a single paper because they share the same machinery, with opposite signs.

This is a tightly-scoped paper: it reports two parameter-free benchmark matches under an explicit, separately stated coupling hypothesis. It does NOT claim to resolve cosmological tensions; the credibility-bar discipline applies hardest here. The paper survives or dies on three pillars:

1. The operator-trace formalism is rigorously stated.
2. The K-saturated admissibility theorem (rank-one projector corrections classified inside A_K) is correctly stated with explicit hypotheses and a clean idempotent-coefficient proof.
3. The empirical match is honestly reported with directional σ-tension and the coupling rule is explicitly flagged as a Layer-3 hypothesis.

## What's IN scope

1. **Setup (cite Papers 1 + 3).** V_600, T_τ-cycle space C ≅ ℂ^12, K-class projectors P_K (rank m_K), Dic_5 ⊂ 2I, τ_σ involution.
2. **Operator-trace formalism.** ΛCDM-baseline = I_12; modifications as rank-1 corrections P_K with K ∈ {0, 72}.
3. **K-saturated admissibility theorem.** Given the K-multiset {72:1, 0:1, 52:5, 20:5}, the only rank-one K-saturated diagonal projector corrections to I_C are ±P_72 and ±P_0. (Hypotheses — diagonal in the cycle basis and K-class-saturated — are stated explicitly; we do NOT claim that arbitrary rank-1 operators or arbitrary τ_σ-invariant rank-1 operators are excluded.)
4. **Sign assignment (Layer-3 hypothesis, NOT theorem).** H_0 ↔ +P_72 (scale-setting / max-K-coupling); S_8 ↔ −P_0 (clustering / trivial-K-exclusion). Stated as a coupling hypothesis (H1) in §6, not as a derivation.
5. **Modification factors.** tr(I_C + P_72)/12 = 13/12 ≈ 1.0833. tr(I_C − P_0)/12 = 11/12 ≈ 0.9167.
6. **Empirical comparison (Layer 2).** H_0 Planck (67.36) × 13/12 = 72.97 km/s/Mpc vs SH0ES (73.04 ± 1.04): ≈0.06σ residual. S_8 Planck (0.832) × 11/12 = 0.763 vs KiDS-1000 multi-probe (0.766 +0.020/−0.014): directional residual ≈0.24σ using the lower KiDS error (predicted value below central). S_8 ≡ σ_8 √(Ω_m/0.3) is used since published weak-lensing intervals are reported as S_8.
7. **Scope.** The trace identity is unconditional Layer-1 mathematics; the coupling rule is Layer-3 hypothesis. We do NOT include pre-registered predictions for DESI/Euclid/eROSITA in this paper — those would require Hypothesis H1 to be promoted to a derivation, which is out of scope here.

## What's explicitly OUT of scope

1. **CMB acoustic peaks**, recombination physics, full ΛCDM 6-parameter derivation. Paper 5.
2. **BH thermodynamics, Hawking spectrum.** Papers 1 + 2.
3. **τ_σ construction.** Paper 3.
4. **Cosmic dipole 1+k/2 ladder.** Mentioned as related but reserved for Paper 5 synthesis.
5. **Ontology / metaphysics.** No claim about V_600 being THE substrate; the paper claims a numerical match.
6. **Cascade-unit ↔ physical-unit calibration.** Tier-2.
7. **Cosmological perturbation theory in V_600.** Tier-2.

## Section structure (target ~16 pages)

1. **Introduction** (1.5pp). H_0 and σ_8 tensions; what's known; what this paper does (two ratios).
2. **V_600 cycle structure and the K-multiset** (2pp). Cycle space C ≅ ℂ^12, K-class projectors, Dic_5 / τ_σ recap (cite Papers 1 + 3).
3. **The operator-trace formalism** (2pp). Definition of Ĥ, Ĉ as bounded self-adjoint operators on C; ΛCDM baseline = I_12.
4. **K-saturated admissibility theorem: rank-one K-class projector corrections** (2.5pp). Given the K-multiset, only ±P_72 and ±P_0 are admissible among K-saturated diagonal projector corrections. Proof with admissibility hypotheses stated first (diagonal in cycle basis; K-saturated). Phase-independence lemma covering all 32 τ_σ lifts from Paper 3.
5. **Sign assignment (Layer-3 hypothesis)** (1.5pp). H_0 ↔ +P_72, S_8 ↔ −P_0. Stated as a coupling hypothesis (H1), not a derivation.
6. **Modification factors and empirical match** (2pp). 13/12, 11/12, S_8 directional residual tabulated.
7. **Scope and what is NOT claimed** (1pp). Load-bearing honest section.
8. **Conclusion** (0.5pp).
9. **Appendix.** Verification scripts (`verify.py`).

## The undismissable spine

> We define two operators on the 12-dimensional rational T_τ-cycle space C_Q ≅ Q^{12} of the 600-cell: Ĥ = I_C + P_72 and Ĉ = I_C − P_0, where P_K is the diagonal rank-m_K projector onto the K-class cycles. Given the K-multiset {72:1, 0:1, 52:5, 20:5}, we prove that ±P_72 and ±P_0 are the only rank-one K-class projector corrections to I_C; arbitrary rank-one subprojectors are outside the admissible K-saturated diagonal operator algebra. The trace ratios tr(Ĥ)/12 = 13/12 and tr(Ĉ)/12 = 11/12 are exact rationals. As a numerical observation: 13/12 × H_0(Planck 2018) = 72.97 km/s/Mpc compared to SH0ES 2022's 73.04 ± 1.04 (≈0.06σ residual), and 11/12 × S_8(Planck 2018) = 0.763 compared to KiDS-1000 multi-probe 0.766(+0.020/−0.014) (≈0.24σ residual using the directional KiDS lower error; S_8 is used rather than bare σ_8 since published weak-lensing intervals are reported as S_8). The coupling rule (H_0 ↔ +P_72 max-K-coupling, S_8 ↔ −P_0 trivial-K-exclusion) is an explicit Layer-3 hypothesis, NOT a theorem. The trace identity is unconditional Layer-1 mathematics.

The reviewer reads: operator-trace identity, finite-group forcing argument, empirical match within 1σ, honestly stated interpretive content. No "we solved cosmology."

## Risk register

| Hook | Mitigation |
|---|---|
| "The coupling rule is hand-picked to fit the data." | §4 classifies rank-one corrections inside the K-saturated diagonal projector algebra A_K — the only rank-one elements are ±P_72, ±P_0. §5 states the sign assignment H_0 ↔ +P_72, S_8 ↔ −P_0 as an explicit Layer-3 hypothesis (H1), not as a derivation. |
| "Why I_C as baseline?" | §3 defines the baseline as the K-blind uniform cycle weighting — unit weight on every T_τ cycle. Once that operational definition is taken, I_C is unique by definition; this is a baseline choice, NOT a τ_σ-uniqueness theorem. |
| "What's the dynamical equation?" | §3 acknowledges: this paper presents observable-level ratios, not a Friedmann analog. Tier-2 work. |
| "Two benchmark matches from one hypothesis is too good." | The paper presents Layer 1 (theorem) + Layer 2 (observation) + Layer 3 (hypothesis) explicitly; Layer 3 is falsifiable by future H_0 / S_8 measurements. The numerical match alone does not constitute a derivation. |
| "Empirical match assumes specific Planck / SH0ES / KiDS values." | §6 tabulates Planck 2018, SH0ES 2022, KiDS-1000 multi-probe values with full asymmetric uncertainties and pinned bibliography (references.bib). |
| "Why not some other rank ≥ 2 correction?" | §4 ablation shows rank-5 corrections (P_52, P_20) give trace ratios 17/12 and 7/12, far outside the cited H_0 / S_8 bands. Within the rank-1 pair, trace data alone do NOT distinguish P_72 from P_0 — that is the content of Hypothesis H1. |

## Files inherited

- `papers/cosmological-folding-rate/dynamics/od1_operator_derivation.py` — legacy K-projector trace script (now softened; see header note).
- `papers/cosmological-folding-rate/dynamics/OD1_STATUS.md` — legacy status note documenting that mode-counting alone did not close (cited in §6 mode-count caveat).
- `papers/cosmological-folding-rate/dynamics/od1_cycle_spectrum.py` — orthonormal mode-count source for the older 17/12 number (cited in §6 mode-count caveat).
- `papers/v600-programme/lib/vfd_v600/operators.py` — shared library implementation of P_K, Ĥ, Ĉ, trace_ratio (Phase 0).

## Open scoping questions

1. **Combine H_0 and S_8** into one paper, or split? Current scope = combined. Rationale: same machinery (rank-one K-class projectors in A_K), opposite signs, mutually reinforcing. Split = two narrower papers.
2. **Engagement with mainstream tension-resolution proposals.** Brief comparison to early-dark-energy, modified gravity, sterile neutrinos — or hold to pure math + measurement? (Currently held; Paper 5 territory.)
3. **Length: 14pp vs 18pp.** 18 gives room for full perturbation-theory caveats; 14 is tighter and more focused.
