# Paper 5 — Math Catalogue (D/L/IT/F entries)

This is the synthesis paper. It IMPORTS theorems from Papers 1–4
without re-proof. Catalogue entries are organised as:
- **D** definitions (introduced or re-stated here),
- **L** lemmas (load-bearing, proved here OR cited),
- **IT** imported theorems (citation-only restatements of foundation
  results — the heart of the paper),
- **F** named future builds (out of scope; explicit unmet
  prerequisites).

No new theorem-grade physical claim is asserted by Paper 5; the
synthesis adds only the structural-spine identification.

## Layer discipline

- **Layer 1 (Theorem-grade):** D1, L1, L2, IT1, IT2, IT3, IT4a
  (Layer-1 trace identities + admissibility from Paper 4), S1, N1.
  The only NEW Layer-1 content is the structural-spine definition
  (D1) and the synthesis proposition (S1) that IT1–IT3 and IT4a
  factor through it.
- **Scope-limiting remarks:** R1 (synthesis is structural, not a
  unification theorem in physics).
- **Layer 2 (Observation):** IT4-Obs (Layer-2 numerical match imported
  unchanged from Paper 4 §5; uses external cosmology benchmarks NOT
  in Σ_{V_600}).
- **Layer 3 (Hypothesis, NOT claimed):** IT4-H1 (Layer-3 coupling
  hypothesis imported unchanged from Paper 4 H1; invokes physical
  observables NOT in Σ_{V_600}).
- **F (Future builds, OUT of scope):** F1 CMB-bulk projection bridge;
  F2 cosmic dipole / 1+k/2 ladder audit; F3 pre-registered
  prediction manifest.

## Definitions

- **D1.** Structural spine (label `def:spine`, §2).
  Σ_{V_600} := (G = 2I = V_600, T_τ-cycles, K-multiset
  {72:1, 0:1, 52:5, 20:5}, H = Dic_5, V_24 = Fix_σ(V_600), right
  cosets R = {Hg : g ∈ 2I}, σ (the K/Q Galois twist √5 ↔ −√5
  acting on the icosian quaternion algebra and restricted to V_600),
  τ_σ involution, K-saturated algebra A_K). Every component is
  imported from a foundation paper (citation in Table 2.1); none
  is introduced or re-proved here.
  *Status:* explicit definition recording the load-bearing finite
  data shared by Papers 1–4.

## Lemmas

- **L1.** V_24 / Dic_5 distinction (label `lem:V24Dic5`, §2.1).
  Fix_σ(V_600) = V_24 has 24 vertices; Dic_5 has 20 vertices; they
  are distinct subsets of V_600. The intersection
  |gH ∩ V_24| = 4 per coset is the Bekenstein incidence content of
  Paper 1, NOT a new claim of Paper 5.
  *Status:* citation (Paper 1). `verify.py` cross-checks
  |Dic_5| = 20, |V_24| = 24, Dic_5 ≠ V_24, |Dic_5 ∩ V_24| = 4.

- **L2.** Cross-cutting phase-independence (label `lem:phaseind`,
  §2.2).
  The theorem-grade identities and properties imported in
  IT1–IT4a — namely the |gH ∩ V_24| = 4 incidence count (IT1), the
  σ-pair-energy spectrum 24·δ_0 + 96·δ_{5/2} (IT2), the (P1)–(P4)
  involution properties of τ_σ (IT3), and the trace identities
  tr(I_C + P_72) = 13 + tr(I_C - P_0) = 11 plus K-saturated
  admissibility (IT4a) — are independent of which τ_σ phase lift
  (out of the 32 canonical lifts) is chosen. The explicit phase-0
  vertex map of IT3 is, by construction, phase-specific as a
  120-vertex map; phase-independence is a statement about the
  structural identities/properties, NOT about the explicit lift.
  *Status:* citation (Papers 3 + 4). `verify.py` cross-checks all
  32 phase combinations: cycle-level permutations all pointwise
  fix Ĥ and Ĉ.

## Imported theorems (citation only)

- **IT1.** Bekenstein 1/4 incidence (Paper 1, §3).
  For every coset gDic_5 of the bulk subgroup,
  |gDic_5 ∩ V_24| = 4. The structural ratio S/A = 4/16 = 1/4
  matches the Bekenstein–Hawking entropy coefficient.
  Uses (V_600, Dic_5, V_24) from Σ_{V_600}.
  *Status:* citation. `verify.py` re-runs the count for both left
  and right cosets.

- **IT2.** Hawking quantum E_q = 5/2 + first-law identity (Paper 2,
  §4).
  Every σ-mobile vertex has |v - σ(v)|_E^2 = 5/2; the spectrum is
  24·δ_0 + 96·δ_{5/2}. Per non-bulk coset T_casc · S = E/4 with
  A=16, S=4, E=40, T_casc=5/2 — T_casc is the finite cascade
  temperature parameter of Paper 2, NOT calibrated to a physical
  Hawking temperature. Uses (V_600, V_24, σ, Dic_5) from
  Σ_{V_600}.
  *Status:* citation. `verify.py` re-runs |v - σ(v)|_E^2 over all
  120 vertices.

- **IT3.** τ_σ involution (Paper 3, §5).
  Explicit involution τ_σ : V_600 → V_600 satisfying (P1) involution,
  (P2) fixes Dic_5 pointwise, (P3) swaps K=52 ↔ K=20 cycle classes
  within each non-bulk right coset, (P4) commutes with T_τ. Plus
  antipodal compatibility. Z_2^5 = 32 phase ambiguity; phase-0 lift
  explicit on 120 vertices. Uses (V_600, T_τ, K-multiset, Dic_5,
  R, σ) from Σ_{V_600} and produces τ_σ.
  *Status:* citation. `verify.py` re-runs (P1)–(P4) and antipodal
  compatibility on the canonical phase-0 lift.

- **IT4a.** Operator-trace identities + K-saturated admissibility
  (Paper 4, §4 — Layer 1 only).
  tr(I_C + P_72) = 13, tr(I_C - P_0) = 11 on C_Q ≅ Q^{12}. Within
  A_K the only rank-1 projector corrections to I_C are ±P_72 and
  ±P_0. Uses (V_600, T_τ, K-multiset, A_K) from Σ_{V_600}; THIS
  is the part of Paper 4 that factors through Σ_{V_600} (S1).
  *Status:* citation. `verify.py` re-runs the trace identities.

- **IT4-Obs.** Layer-2 numerical observation (Paper 4, §5 —
  observational only, NOT a theorem).
  13/12 × 67.36 = 72.97 km/s/Mpc vs SH0ES 73.04±1.04 (≈0.06σ);
  11/12 × 0.832 = 0.763 vs KiDS multi-probe 0.766(+0.020/-0.014)
  (≈0.24σ directional residual). Carried across unchanged from
  Paper 4. Uses external cosmology benchmarks NOT in Σ_{V_600};
  hence does NOT factor through Σ_{V_600}.
  *Status:* observational pass-through.

- **IT4-H1.** Cycle-mode coupling hypothesis (Paper 4, §6, H1 —
  hypothesis, NOT a theorem).
  Γ : {scale-rate, clustering-amplitude} → A_K with H_0 ↔ +P_72,
  S_8 ↔ -P_0. The synthesis carries this forward AS a hypothesis;
  we do NOT promote it to a theorem here. Uses external physical
  observables NOT in Σ_{V_600}; hence does NOT factor through
  Σ_{V_600}.
  *Status:* hypothesis pass-through.

## Synthesis proposition

- **S1.** Common factorisation through Σ_{V_600} (label
  `prop:synthesis`, §7).
  Each of IT1, IT2, IT3 (structural-property package only), and
  IT4a is a statement about Σ_{V_600}: IT1 uses (V_600, Dic_5,
  V_24); IT2 uses (V_600, V_24, σ, Dic_5); IT3 uses (V_600, T_τ,
  K-multiset, Dic_5, R, σ, τ_σ); IT4a uses (V_600, T_τ,
  K-multiset, A_K). None of these four Layer-1 statements uses any
  datum outside Σ_{V_600}. CAVEAT: Paper 3's explicit phase-0
  vertex map (the 120-vertex realisation of τ_σ) additionally
  requires the icosian trace metric and base-point/ordering
  conventions of `vfd_v600.icosian.build_vertices()` as auxiliary
  data; those conventions are NOT part of Σ_{V_600}, but the
  (P1)–(P4) + antipodal structural-property package does not need
  them. The factorisation does NOT extend to IT4-Obs (Layer 2:
  external cosmology benchmarks) or IT4-H1 (Layer 3: coupling
  hypothesis tying trace ratios to those observables); both invoke
  data and physical hypotheses outside Σ_{V_600}.
  *Status:* proved by inspection of the four cited papers (no new
  derivation).

- **R1.** What the synthesis does and does not say (label
  `rem:synth`, §7).
  S1 is a structural observation, NOT a unification theorem in
  physics. It does not derive black-hole thermodynamics, Hawking
  radiation, or cosmological tensions from the shared structure;
  whether the shared dependence has physical content is a separate
  question this paper does not address.
  *Status:* explicit scope-limiting remark.

## Named future builds (OUT of scope)

- **F1.** CMB-bulk projection bridge (§8).
  A possible map Θ : (F^B_t, π_C, calibration) → T : S^2 → R_+
  from a candidate bulk-supported sector of states (with
  σ-invariance to be proved by the bridge, NOT assumed; and NOT
  identified with V_24 — bulk Dic_5 has 20 elements, V_24 has 24;
  the two are distinct, see L1) to an observed CMB temperature
  field. Open builds in `docs/closure-cosmogenesis.md`: residual
  support ρ^B_t = 0 conditional, coarse-graining π_C weights open,
  temperature calibration unspecified. NOT a claim of Paper 5.
  Source language identifying the 20-vertex bulk with the 24-vertex
  σ-fixed sublattice is a known conflation that this paper
  explicitly disowns (see L1 / `lem:V24Dic5`).

- **F2.** Cosmic dipole / 1+k/2 ladder audit (§8).
  Repository scripts catalogue cascade-resolution rung predictions
  vs survey dipole-axis measurements. Currently exploratory and
  partly fitted (`papers/cosmological-folding-rate/dynamics/preregister_k.py`
  admits the k-rule is a working hypothesis). A separate audit with
  frozen survey inclusion, uncertainties, k-assignment, and null
  model is needed before any such claim is defensible. NOT a claim
  of Paper 5.

- **F3.** Pre-registered prediction manifest (§8).
  A locked, timestamped prediction manifest with formula, value,
  uncertainty window, and source commit per observable would convert
  Hypothesis Γ (Paper 4) into a falsifiable programme. The present
  scripts (preregister_k.py, cmb_mapping.py, the legacy
  UNIFIED_RESULT.md) are not in that form. NOT a claim of Paper 5.

## Numerical / computational results

- **N1.** Synthesis verification certificate (label `app:verify`,
  Appendix A).
  `verify.py` computes Σ_{V_600} from `vfd_v600.group.build_state()`
  and asserts the listed headline cross-checks: state size,
  K-multiset, |Dic_5|=20, |V_24|=24, Dic_5≠V_24, |Dic_5∩V_24|=4,
  Dic_5 non-normal in 2I, left cosets NOT whole-cycle carriers
  (regression vs right cosets), Bekenstein |gH∩V_24|=4 for both
  coset families, σ-pair energy = 5/2 on all 96 mobile vertices
  and 0 on all 24 σ-fixed vertices, τ_σ canonical-lift
  (P1)–(P4)+antipodal, trace ratios 13/12 and 11/12, and
  phase-independence on all 32 τ_σ phase combinations.
  *Status:* exits 0 iff every assertion holds.

## Verification entry points

- `papers/v600-unified/verify.py` — primary cross-check certificate
  (re-runs each foundation paper's headline number from the shared
  exact `vfd_v600` infrastructure).
- `papers/v600-programme/tests/` — 39 shared tests covering V_600,
  Dic_5, V_24, σ, τ_σ, operator traces, symmetry.
- Each foundation paper's own `verify.py` (Paper 1: bekenstein-
  incidence, Paper 2: v600-hawking-quantum, Paper 3: tau-sigma-
  construction, Paper 4: v600-cosmic-tensions).

## Out-of-scope (reserved for future programme work)

- Quantitative CMB ℓ-spectrum, recombination model, Planck-continuum
  recovery (F1 territory).
- Cosmological perturbation theory in V_600 (Tier-2).
- Quantum gravity ontology — no claim made.
- Cascade-unit ↔ Mpc calibration (Tier-2).
- Promotion of Hypothesis Γ (Paper 4 H1) to a theorem (would likely
  require an H_4-representation derivation of the coupling rule;
  out of scope here).
