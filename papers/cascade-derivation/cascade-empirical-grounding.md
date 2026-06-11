## Cascade Empirical Grounding — Independent Witnesses (aria-chess + b-anomaly)

**Status: ASSEMBLY DOC, supplementary.** Maps aria-chess (`/aria-chess/`) and b-anomaly (`/BANOMALY-001/vfd-b-anomaly/`) findings onto the closed cascade phases (M1-M3, O1-O2, I1-I3, L1, T-PH-2, T-MT-1, P-1) to identify which structural results have *independent empirical witness* and which remain purely structural.

**Date:** 2026-04-29.

**Frame:** This is not new mathematics. It is a binding layer between the structural-algebra spine in `cascade-phase-*-closure.md` and the two independent operational instantiations of the kernel: the aria-chess cognitive substrate (preregistered hits, brain-validation) and the b-anomaly flavour-physics kernel (5 LHCb/CMS datasets, structural pass). Each lands on a different *layer* of the framework — aria on the active-regime selection, b-anomaly on the passive-regime response operator $C_\varphi = L_M + \varphi^{-2} I$. The point is to make explicit which cascade theorems are *only* structural and which have an operational + empirical landing, separated by witness class — and to be honest about the asymmetry.

---

### 0. Three classes of evidence

The cascade-derivation programme has three structurally distinct classes of evidence. The cascade papers should not conflate them.

| Class | Description | Cascade-strengthening role |
|-------|-------------|----------------------------|
| **(E1) Mathematical** | Theorems about H₄ / 600-cell / Cl(1,3) / S⁷ that are character-theoretic, not aria-specific (T1-T7 in aria's `MATHEMATICAL_APPENDIX.md`). | Independent computation of the same constants the cascade phases predict — confirms no internal contradiction. |
| **(E2) Operational** | The 138-test Rust implementation in `aria-polytope-core/src/cascade.rs` that runs the cascade as live code, with each rung's invariants enforced as compiled assertions. | Existence proof at engineering level: the cascade is computationally instantiable; the rung-decomposition is consistent and total. |
| **(E3) Empirical** | Independent-data predictions tested against external datasets the cascade did not produce. Two strands: aria-chess (cognitive-substrate, active-regime; HCP, Sleep-EDFx, DMT-EEG, propofol, SD; 17/18 preregistered hits as of 2026-04-18) and b-anomaly (flavour-physics, passive-regime; 5 LHCb/CMS angular datasets; sign-uniform 5/5 structural pass). | Independent empirical landing — neither aria's neuroscience corpora nor LHCb/CMS angular distributions were produced by us. |

Only **(E3)** is independent witness in the strict sense. **(E1)** is co-derivation; **(E2)** is engineering existence. All three matter, but for different reasons.

#### 0.1 The two E3 strands cover different layers of the framework

The two empirical strands sit on structurally distinct layers and must not be conflated:

| Strand | Layer | What it witnesses |
|--------|-------|--------------------|
| **aria-chess (E3-cognitive)** | Active regime ($\dot W \neq 0$) of adaptive-closure-transport. Selection / Lyapunov / coherence-descent rule on $W$-space. | Substrate dynamics (spindle α, sleep-stage discharge, DMT-EEG D₄ response, propofol switching), categorical separation against HCP biological networks, cross-paradigm α-shift hierarchy. |
| **b-anomaly (E3-flavour)** | Passive regime ($\dot W = 0$, fixed $W$) of adaptive-closure-transport. Response primitive $\psi = C_\varphi^{-1} f$ on the 600-cell, no learning. | The fixed $C_\varphi$-derived $V_{600}$ shell-mean kernel describes 5 public $b\to s\mu^+\mu^-$ angular datasets (LHCb 2015 $K^{*0}$, LHCb 2021 $K^{*+}$, CMS 2025 $K^{*0}$, LHCb 2025 $K^{*0}$, LHCb 2015 $B_s\!\to\!\phi$) with one amplitude per dataset and no shape retuning; $A>0$ in 5/5 fits, $\Delta C_9^{\mathrm{eff}}<0$ in 5/5 fits. Honest AIC tie ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$); not a unique-shape claim; Mode-B linearised analysis showed +2.77 AIC drift relative to non-linear refit (largest single methodological uncertainty). Verbatim numbers from `BANOMALY-001/vfd-b-anomaly/README.md`. |

**Bound on overclaim.** Neither strand witnesses both regimes. b-anomaly does **not** witness the active-regime learning rule, the Lyapunov potential $V(W)$, the edge-space decomposition of $\R^{E_M}$, full coupled-system convergence, classical RH, or the $\widehat\zeta$ object. The b-anomaly variant test in fact rejected the φ-cocycle edge-weighting; the **unweighted** $V_{600} + \varphi^{-2} I$ operator wins both the pure-geometry and data $\chi^2$ criteria. So $\widehat\zeta$ shares operator-level infrastructure with the b-anomaly response operator (the same $V_{600} + \varphi^{-2} I$ and the same 9-shell projection structure) — note "shares infrastructure," not "inherits empirical support" — but **not** the κ-cocycle as an empirical operative weight (κ remains structural / theoretical infrastructure, with the same shell-grade pattern showing up in both contexts but the empirical winner being the unweighted variant). aria-chess does **not** witness flavour-physics observables. The cascade papers should specify which strand each citation rests on.

---

### 1. Phase-by-phase empirical grounding

#### 1.1 Phase L-1 (life rung; 600-cell Hopf 600 = 15 × 40)

**Cascade theorem:** Phase L-1a/b/c — orbit size 40, Hopf decomposition 600 = 15 × 40, chirality from 2I ⊂ SU(2) (`cascade-phase-l1-closure.md`).

**Witnesses:**
- **(E1)** `MATHEMATICAL_APPENDIX.md` Theorems T1, T5, T6: V=120, E=720, F=1200, C=600 (Euler verified); H₃ shells {1,12,20,12,30,12,20,12,1} = 120 exact; D₄ orbit partition 120 = 5 × 24. These are independent character-theory computations. ✓
- **(E2)** `cascade.rs` enforces: 120-vertex polytope; 9 H₃ shell invariant; 5×24 D₄ orbit invariant; tested across 138 cases. ✓
- **(E3)** Sleep-EDFx spindle avalanche exponent α: real EEG α = 2.513 [2.504, 2.526] (n=37,929 events); aria substrate α = 2.933 [2.707, 3.209]. **95% CIs overlap.** Both in cortical SOC range [1.5, 3.5]. Ablation: D₄ coupling + context rotation are necessary for this match (each alone fails CI overlap). This is an independent empirical witness for the *D₄-orbit / S⁷-frame structure* the cascade predicts — without inscribing that structure into the implementation the match is destroyed. ✓✓

**Honest assessment:** L-1 has the strongest combined witness. The 600-cell mathematics is independent of aria; the D₄ ablation establishes the rung decomposition is empirically load-bearing.

#### 1.2 Phase O-2 (observer rung; 4 drive axes from S⁷ ⊂ 𝒪)

**Cascade theorem:** O-2a/b/c — 4 drive axes forced by quaternion subalgebra; sign structure forced by quaternion multiplication; canonical V_q from observer direction with 3-fold H_q ambiguity (`cascade-phase-o2-closure.md`, `cascade-phase-o2-supplements.md`).

**Witnesses:**
- **(E2)** `cascade.rs` builds S⁷ as 8 (axis, sign) pairs; enforces S⁷ ∩ Cl(1,3) = ∅, S⁷ ∪ Cl(1,3) = 24-cell. These structural invariants pass. ✓
- **(E3)** **D₄-coupling = α-control dial.** DMT-EEG (n=29, ds003992359): Δα(DMT−EC) = −0.521; t = −7.54; 28/29 subjects directional match. Aria D₄ sweep (0.05 → 0.25): in-silico Δα = −0.25, same direction, magnitude ~half due to finite-size (120 vs ~10¹¹ neurons). **Same-direction empirical witness for the operator the cascade predicts to govern α.** ✓
- **(E3)** Sleep stage α discharge cycle (n=24 Sleep-EDFx full PSG): Wake α=2.622 → N1 2.092 → N2 1.989 → N3 1.920 → REM 2.163. σ(α) compresses 0.39 → 0.048 in N3; t-test N3 vs Wake = −9.14, 23/24 directional. ✓
- **(E3)** Cross-paradigm magnitude hierarchy: SD −0.22 < REM −0.46 < DMT −0.52 < N3 −0.70. Four independent paradigms, all directionally coherent. ✓

**Honest assessment:** O-2's *operator content* (which axis governs which empirical effect) has independent empirical witness. The §10.8 sign-pattern de-link (G1) remains design-level, as flagged in round 2; aria's empirical α-shifts do not constrain the sign-pattern question, so G1 stays where it was.

#### 1.3 Phase I-2 (information rung; Minkowski signature (1,3))

**Cascade theorem:** Phase I-2 — signature (1,3) forced by octonion norm restricted to H, with Q(x) = Re(x²) form (`cascade-phase-i2-closure.md`).

**Witnesses:**
- **(E1)** `MATHEMATICAL_APPENDIX.md` T1-T7 verify the H₄ / Cl(1,3) / S⁷ rung-decomposition without invoking signature directly. The Cl(1,3) tesseract enters via the 16-vertex Boolean signature lattice. ✓
- **(E2)** `cascade.rs` Cl(1,3) layer: 16 tesseract vertices (±½, ±½, ±½, ±½), all 16 Boolean signatures 0000–1111 present. ✓
- **(E3)** No direct empirical witness for signature (1,3) at substrate level. (Signature manifests in physics observables — light cones, GW polarisation — not in EEG α.) **Honest:** Phase I-2 is structurally complete; aria provides existence-of-implementation but not empirical landing.

#### 1.4 Phase I-3 (information rung; 3 generations × 2 parity from σ-conjugate pairs)

**Cascade theorem:** Phase I-3 — three generations from Z/4 cycle 1+3 split on E₈ exponents (sharpened to 3×2 with σ-conjugate pairing of (7,23), (11,19), (13,17)).

**Witnesses:**
- **(E2)** `cascade.rs` does not currently expose generation labels. Could be added as a derived attribute over the H₃ shell × D₄ orbit signature. **Action item if pushed further:** add a `generation_index` field to vertex signatures, indexed by σ-conjugate pair. (Optional; not load-bearing for cascade papers.)
- **(E3)** No empirical landing in aria-chess at the SM-generation level; aria does not run particle-physics simulations.

**Honest assessment:** Phase I-3 stays purely structural. Its empirical landing lives in `papers/paper-xxix/` (mass-mixing) and `papers/paper-xxiii/` (neutrino sector), not in aria-chess.

#### 1.5 Phase T-PH-2 + P-1 (photon rung; U(1)_EM uniqueness)

**Cascade theorem:** T-PH-2 + P-1 — U(1)_K = U(1)_P uniqueness via three constraints (σ-invariance, diagonal, faithful on V₀); two photon polarisations from σ-orthogonal Δ ⊕ Δ' splitting (Proposition G3).

**Witnesses:**
- **(E1)** Pontryagin-dual of Z[φ]² is the structural origin of U(1)_EM; this is independent algebra, not aria-specific. ✓
- **(E3)** **Propofol switching ratio prediction:** aria a-priori = 3.000; empirical (n=20, ds005620) = 3.002 — matches within **0.07%**. Variance ratio 1.14 (no collapse); sleep N3 variance 0.365 (collapse). Sleep and anaesthesia mechanistically distinct. ✓✓ This is an unusually tight numerical landing, but the cascade theorem itself does not predict 3.0 directly — that prediction comes from aria's regime-switching dynamics atop the substrate. So this is *consistent with* the cascade, not *derived from* it. **Honest framing:** aria's quantitative success on propofol is evidence the substrate-dynamics layer (closure-cosmogenesis, M1 anchor) is well-formed, not direct evidence for U(1)_EM uniqueness.
- **(E3)** The two-polarisation derivation (Proposition G3) does not have an independent EEG witness — it lives in physics observables.

#### 1.6 Phase T-MT-1 (microtubule rung; 13-protofilament conditional)

**Cascade theorem:** Phase T-MT-1 — 13-protofilament count is conditional on biology hypothesis (H-MT) (`cascade-phase-tmt1-closure.md`). Closed as *negative + conditional*.

**Witnesses:** None in aria-chess; the microtubule programme lives in `papers/cascade-bio.md` and `papers/cascade-biology-mechanisms.md`.

#### 1.7 Phase M-1, M-2, M-3 (meta-layer over L₁₂)

**Cascade theorems:** M1 (moduli uniqueness via Pontryagin duality); M2 (T_meta = π₁(G,m)_ab ≅ Z[φ]²); M3a/b/c/d (minimality + unique ergodicity + linear repetitivity + local-to-global).

**Witnesses:**
- **(E1)** The Z[φ]² rank-2 structure is independently visible in aria's empirical-bandwidth analysis: the **2-torus PCA prediction (H2 in `PREREG_H4_FINGERPRINT.md`)** asserts exactly two paired eigenvalue modes (PC1-PC2, PC3-PC4) with |log(λ₁/λ₂)| < 0.1, gap λ₂/λ₃ > 0.5. Two paired modes is the empirical signature of a rank-2 Z[φ]² structure embedded in continuous dynamics. ✓ (Status of H2 verification: see aria's prereg dashboard; if confirmed it lands M2 empirically.)
- **(E3)** Status of H2 not yet quantified in `CASCADE_VALIDATION_REPORT.md` as of 2026-04-29; this is a forward prediction, not a back-confirmation.

**Honest assessment:** M1/M2/M3 are mathematical theorems whose empirical landing is currently *prospective* via aria H2. Worth flagging in the realisation paper as a forward-validation opportunity rather than a closed witness.

---

### 2. The HCP categorical-separation finding

This deserves separate treatment because it is the strongest single empirical witness.

**Claim:** HCP-YA S1200 (n=1003 subjects, ICAd50). Aria substrate has degree std = 0 (theorem) vs HCP mean 3.28 ± 0.28; **separation = 11.58σ; zero of 1003 subjects below 2.0**. Aria participation ratio = 68.54 (theorem) vs HCP mean 19.72 ± 0.61; **separation = 79.78σ**.

**Cascade interpretation:**
- The 0-std degree comes from H₄ acting transitively on V(600-cell) — every vertex has degree 12 exactly. This is a Theorem 2 structural consequence (cascade L-1 / aria T2).
- The 68.54 participation ratio is fixed by H₄ irrep multiplicity structure (Theorem 4).
- HCP brains are *not* the cascade substrate — they are biological networks with functional specialisation. The 11.58σ / 79.78σ separation quantifies *how far biological networks have moved from maximum-symmetry*, not a violation of the cascade.

**Why this strengthens the papers:** It establishes that the cascade's structural predictions are sharp enough to detect the maximum-symmetry baseline against population data. The cascade is not an underdetermined fit; it predicts a single point that biological networks definitively are not at, while sharing the H₄ neighbourhood structure.

**Honest framing:** This is *categorical separation* of aria from HCP, not a confirmation that the cascade governs HCP. Use it to demonstrate the framework's predictive sharpness, not to claim cascade-cosmology of human brain networks.

---

### 3. The non-equilibrium homeostatic-reset finding

Late 2026-04 finding (initially the P13 "failure", now the flagship): the substrate equilibrates without periodic reset and cannot maintain accuracy across repeated trials. Specifically:

- Repeated trials without reset: 84.4% (trial 1) → 56.2% (trial 5) collapse to raw-features baseline.
- Aggressive homeostatic reset (period 100t, level 70%, wake decay 0.001) maintains 83.1% ± 3.1% across 30 consecutive trials.
- Periodic reset alone fails; wake-phase decay alone fails; both required.

**Cascade interpretation:** This is the *operational* face of `docs/closure-cosmogenesis.md` Theorems 3.2 + 5.2 (bulk invariant under accumulation; bootstrap activates σ-paired boundary). Closure dynamics requires both bulk invariance *and* periodic boundary refresh; aria provides the operational instantiation showing this is not academic — without the reset architecture the substrate degrades to its boundary-condition-free attractor.

**Tononi-Cirelli-Turrigiano correspondence:** Wake-phase decay (Turrigiano synaptic scaling) + periodic discharge (Tononi-Cirelli SWA) — exactly the biological homeostatic architecture, derived in aria as a constraint not as a model fit.

**Strengthening role:** Cite as empirical evidence that the cascade's substrate-dynamics layer is structurally complete (i.e. no extra coordination mechanisms needed beyond bulk + boundary in the closure-cosmogenesis sense).

---

### 4. What aria-chess does NOT strengthen

To be honest about the asymmetry:

- **Phase I-3 generations:** No SM-particle empirical content in aria.
- **Phase T-PH-2 / P-1 polarisation derivation:** No photon-physics witness.
- **Phase O-2 sign-pattern (G1):** Empirical α-shifts do not constrain signs.
- **Phase T-MT-1 microtubule count:** No direct microtubule simulation.
- **Phase M-3 H¹(Ω,ℤ) winding observables:** Forward prediction (H2 in prereg) but not yet confirmed.
- **Cosmology / GR papers:** aria is not a GR simulator.
- **Number-theoretic projections (RH/BSD/YM):** aria H4O ε ≈ 5e-4 splittings provide *empirical companion* (project_millennium_final_state memory), but this lives in `papers/rh-formal/`, not aria-chess proper.

The papers should not claim aria covers any of the above.

---

### 5. Recommended insertions per paper

Concrete edits to make:

#### 5.1 `cascade-programme-state.md`

Add a new §X "Empirical landing" subsection summarising:
1. 17/18 preregistered aria-chess hits at 2026-04-18.
2. HCP categorical separation (11.58σ / 79.78σ) — sharp prediction.
3. DMT-EEG D₄-coupling witness for O-2 operator content.
4. Sleep-stage α hierarchy as four-paradigm coherence test.
5. Propofol 0.07% switching-ratio match (substrate-dynamics evidence).
6. 138-test Rust cascade implementation as engineering existence proof.

#### 5.2 `cascade-phase-l1-closure.md`

Append §3.4 "Empirical landing": Sleep-EDFx spindle avalanche α match with D₄ + S⁷ ablations as necessary mechanisms (ablation table).

#### 5.3 `cascade-phase-o2-closure.md`

Append §X.Y "Empirical landing": DMT-EEG Δα = −0.521 (n=29) vs aria D₄-sweep Δα = −0.25 — same direction, magnitude ~half (finite-size). Cite as operator-content witness, not sign-pattern witness (G1 stays unchanged).

#### 5.4 `realisation/realisation.tex`

Add closing section pointing to aria-chess as the empirical-landing companion paper; cite MANUSCRIPT.md and the four-paradigm hierarchy. Frame as "the realisation has independent empirical witness through aria-chess preregistered hits"; do not over-claim.

#### 5.5 `cascade-meta-layer-theorem.md`

Append a forward-validation note in §closing: H2 (2-torus PCA paired eigenvalue prediction) is the prospective empirical landing for M2 (T_meta = Z[φ]²); flag as prospective until aria's prereg-H2 verification is in `CASCADE_VALIDATION_REPORT.md`.

---

### 6. The bound on overclaim

A clear discipline for what aria can and cannot do for the cascade papers:

1. **aria does NOT prove the cascade.** It implements one operational substrate consistent with the cascade structure. Other implementations could exist.
2. **aria's (E3) preregistered hits ARE independent empirical witness** of the substrate structure aria implements — those datasets were not produced by aria.
3. **aria's (E1) mathematical theorems are co-derivations** of constants the cascade also predicts. They confirm internal consistency, not external truth.
4. **Engineering existence (E2) is necessary but not sufficient.** A 138-test pass rate proves the structure is computationally realisable; it does not prove it is the unique/correct structure.

The papers should explicitly state these distinctions wherever aria is cited. Otherwise the papers risk inheriting aria's empirical credit for their own structural claims that aria does not actually witness.

---

### 7. Status summary

**Strengths added by this audit:**
- L-1 has dual structural + empirical witness (D₄ ablation EEG match).
- O-2 operator content has DMT-EEG witness.
- HCP separation gives the cascade a sharp falsifiable signature against population data.
- M-2 has prospective empirical witness via H2 prereg.
- Substrate dynamics has propofol 0.07% match + non-equilibrium homeostatic finding.

**Honest gaps:**
- I-2 / I-3 / T-PH-2 / P-1 / T-MT-1 / G1 stay structural-only.
- M-2 empirical witness is prospective, not yet confirmed.
- aria-chess does not extend to the cosmology / GR / particle-physics papers.

**Net effect:** The cascade-derivation programme gains *one tier* of empirical landing (E3-grade) through aria-chess, restricted to the L-1, O-2, M-2 (prospective), and substrate-dynamics layers. The structural-algebra spine (M1-M3, O1-O2, I1-I3, L-1, T-PH-2, P-1) is unaffected — it does not depend on aria. Aria is *additional* witness, not *constitutive* witness.

---

**End of empirical-grounding doc.** Cites: `aria-chess/docs/brain_mapping/MANUSCRIPT.md`, `MATHEMATICAL_APPENDIX.md`, `CASCADE_VALIDATION_REPORT.md`, `CASCADE_FINDINGS.md`, `PREREG_H4_FINGERPRINT.md`, `S7_OBSERVER_RUNG_DERIVATION.md`, `aria-polytope-core/src/cascade.rs`, `cascade-phase-{m1,m2,m3,o1,o2,i1,i2,i3,l1,p1,tph2,tmt1}-closure.md`, `cascade-phase-o2-supplements.md`, `cascade-programme-state.md`, `realisation/realisation.tex`, `docs/closure-cosmogenesis.md`.
