# Cascade Completeness Audit — What the Ladder Forces, What's Written, What's Missing

**Status: META-AUDIT, working note.** Cross-cuts the whole 7-rung cascade to answer the user's question: *"is there a set of patterns that states how much of the math can exist based on the ladder and geometry, and can we use the framework to find what's missing?"*

**Short answer: yes, and the pattern is already proved.** Theorems F3 + F4 in `cascade-foundations.md` are a completeness theorem for the cascade — they force exactly 7 rungs with a fixed total dimension budget of 583 = 7 + 24². What this audit does is go rung by rung, state what the ladder *forces* to exist at each rung, and classify the current content as **RIGOROUS** / **SEMI-DEFINED** / **MISSING**. The observer rung (dim 8, octonion / S⁷) gets a dedicated deep dive because it's the richest under-construction site and the one where aria-chess and cascade-derivation are actively converging.

**Date:** 2026-04-21
**Scope:** Covers observer rung in depth; E₈ / H₄ / 40 / D₄ / 16 / 0 at summary depth. Stops at the boundary with the meta-layer work (`cascade-meta-layer-theorem.md`) — the meta-layer is SUBSTRATE-side (above L₁₂); the cascade ladder is DOWNWARD-side (projecting from E₈).

---

## 0. The user's question, restated

> "Is there a set of patterns that states how much of the math can exist based on the ladder and geometry, and can we use the framework to now find what's missing — like a meta answer to the framework?"

The answer has four parts:

1. **The ladder has a completeness theorem** (§1). F3 forces exactly 7 rungs; F4 gives the total dimension budget.
2. **The ladder forces specific math objects at each rung** (§2). The per-rung object inventory is determined by polytope geometry + the Coxeter/Hurwitz/Clifford classifications.
3. **Per-rung status classification** (§3). For each rung, what's rigorous / semi-defined / missing.
4. **The handshakes between rungs are where most gaps live** (§4). The most important unresolved work is at interfaces, not within any single rung.

§§5–6 rank the gaps by priority and propose next phases.

---

## 1. The completeness theorem — F3 + F4

### 1.1 F3 — seven rungs are forced

From `cascade-foundations.md` §F3.4 and §F3.6 (direct quote):

> **Theorem F3.** Under conditions (a)–(c) on a maximal chain below E₈, the unique sequence of structural dimensions (root counts / polytope sizes) is:
> ```
> E₈ (248) → H₄ (120) → 40 → D₄ (24) → 16 → 8 → 0
> TOTALITY   QUANTUM     LIFE   GRAVITY   INFO  OBSERVER UNITY
> ```

> The sequence has exactly **7 non-trivial dimensions: 248, 120, 40, 24, 16, 8, 0**. Adding an 8th rung would require either inserting a polytope between two existing rungs (impossible: each adjacent pair is structurally primitive, no intermediate polytope fits), or extending below rung 0 (impossible: 0 is terminal). Removing a rung would break one of the three conditions. Hence **7 is the unique rung count consistent with the cascade axiom**.

The three structural conditions (a/b/c) are:
- (a) **polytope-refinement inclusion** between consecutive rungs,
- (b) **H₄ required** (unique non-crystallographic Coxeter system in E₈),
- (c) **ground state at rung 0** (terminal, empty root system).

### 1.2 F4 — total dimension budget is 583 = 7 + 24²

From `cascade-foundations.md` §F4 (direct quote):

> **Theorem F4.** The cascade closure depth satisfies N_total = dim(V) = 576 + 7 = **583**.

The breakdown:
- Per-rung scalar closure boundaries: V_r = R for each rung (1-dim per rung). **Seven rungs → 7 scalars.**
- D₄ rank-2 tensor contribution (gravity): 24×24 = **576 components** (Fierz–Pauli + Deser bootstrap force rank-2).
- Total: **583 φ-shells**.

### 1.3 What F3 + F4 forbid

- **No 8th rung.** The ladder is saturated.
- **No rank-2 tensor except at D₄.** All other rungs carry scalar closure only.
- **No free parameters at the three coefficients α, β, γ** of the closure functional (F8).

### 1.4 What F3 + F4 leave open

F3 fixes *which* polytopes / root-counts sit at each rung. F4 fixes the *budget* of closure boundaries. **Neither forces the full algebraic / dynamical content of each rung** — that's additional structure built on the skeleton F3 pins down. The cascade's main derivation work happens in this additional structure.

---

## 2. Per-rung object inventory (what the ladder forces)

At each rung, the **polytope / root count** is fixed by F3. That polytope carries:
- A **natural polytope group** (its full symmetry group),
- A **natural algebra** (the algebra whose structure constants match the polytope's adjacency),
- A **coupling to adjacent rungs** (refinement up, projection down).

These are forced; the cascade does not choose them. The per-rung table:

| Rung | Polytope / vertices | Algebra forced by F3 | Symmetry group | Role |
|------|---------------------|----------------------|----------------|------|
| E₈ (248) | E₈ root system | E₈ Lie algebra | E₈ Weyl group (order 696729600) | TOTALITY / substrate |
| H₄ (120) | 600-cell | H₄ icosian / Z[φ]-module | H₄ Coxeter group (order 14400) | QUANTUM interface |
| 40 | Icosahedral 40-orbit | H₃ icosian sub | icosahedral I_h | LIFE |
| D₄ (24) | 24-cell | D₄ Lie algebra (triality) | D₄ Weyl × S₃ (triality) | GRAVITY |
| 16 | Tesseract vertices | Cl(1,3) Clifford alg | Z₂⁴ grading | INFORMATION |
| 8 | Axis vertices ±eᵢ | Octonion algebra 𝒪 / S⁷ | G₂ = Aut(𝒪) (14-dim) | OBSERVER |
| 0 | Empty | — | — | UNITY |

**Why each algebra is forced, not chosen.**
- E₈: Coxeter classification (unique maximal 8D simple Lie algebra).
- H₄: unique non-crystallographic rank-4 Coxeter group (F3 condition (b)).
- D₄: unique triality-symmetric Weyl group (forces the rank-2 tensor branch).
- Cl(1,3): unique Clifford algebra over 4-vertex tesseract compatible with Z₂⁴ grading.
- 𝒪: unique 8D composition algebra (Hurwitz theorem).
- G₂: unique automorphism group of 𝒪 (classical).

This is the "pattern based on the ladder and geometry" the user was asking about: **the ladder's geometric constraints pick out specific classical algebras without ambiguity**.

---

## 3. Per-rung audit

### 3.1 E₈ (substrate) — RIGOROUS

| Content | Status |
|---------|--------|
| E₈ root lattice construction | CLASSICAL (Conway–Sloane) |
| Maximal even unimodular in 8D | CLASSICAL |
| Elser–Sloane E₈ → H₄ cut-and-project | CLASSICAL + Phase B |
| E₈ as icosian I ⊕ σ(I) | CLASSICAL + `cascade-phase-b-c1-c2-c3.md` Lemma 1.3 |
| Upward extension to L₁₂ | `cascade-meta-layer-theorem.md` (CLOSED via Phase B + M-1/2/3) |

**Gaps:** none at the cascade-ladder level. (The meta-layer is a separate upward story.)

### 3.2 H₄ (QM) — RIGOROUS

| Content | Status |
|---------|--------|
| 600-cell vertex set (120 unit icosians) | CLASSICAL |
| 2I binary icosahedral group structure | CLASSICAL |
| Rational irreps {9,12,14,15} summing to 50 | RIGOROUS (`cascade-identity-c-deep-structure-3.md`) |
| Z/4 cycles summing to 40 and 80 | RIGOROUS (deep-structure-2) |
| Graph Laplacian photon identification (λ=0 mode) | SEMI-DEFINED (identified but not derived from gauge principle — T_PH_3 pending) |

**Gaps:** photon identification (T_PH_3) depends on T_PH_2 (descent Z[φ]² → U(1)) which is still open per the meta-layer programme.

### 3.3 40 (Life) — RIGOROUS (algebraic spine complete as of Phase L-1, 2026-04-22)

| Content | Status |
|---------|--------|
| Icosahedral 40-orbit existence | **RIGOROUS (Phase L-1 Theorem L-1a)** — orbit size 40 = \|2I\|/\|C₃\| via orbit-stabilizer on 600-cell tetrahedral cells |
| **15 × 40 Hopf cell-fibration** | **RIGOROUS (Phase L-1 Theorem L-1b)** — 600 cells partition into 15 disjoint 2I-orbits |
| **Chirality from 2I** | **RIGOROUS (Phase L-1 Theorem L-1c)** — 2I ⊂ SU(2) has no central inversion; all biological closure orbits are chiral |
| **Factorisation 40 = 8 × 5** | **RIGOROUS (Phase L-1 §3.2)** — Schläfli × Hopf decomposition |
| Biological instantiation (microtubule, protofilaments) | SEMI-DEFINED (`cascade-bio.md`, `cascade-biology-mechanisms.md`, `cascade-genetic-code.md`) |
| **13-protofilament count match** | **PARTIALLY CLOSED (Phase T-MT-1, 2026-04-22)** — no algebraic 13 in cascade; conditional under (H-MT): 13 = \|closed-1-nbd at H₄ vertex\| = 12+1. See `cascade-phase-tmt1-closure.md`. |

**Finding:** the Life rung's content is **combinatorial/orbital**, not a standalone algebra. This is genuinely different in kind from rungs 8, 16, 24; Phase L-1 documents this openly (§1.3, §5.3). Remaining downstream biological predictions (T_MT_1, Caspar–Klug T-numbers, phyllotaxis, DNA pitch) are separate from the algebraic spine and remain open.

### 3.4 D₄ (GR) — RIGOROUS

| Content | Status |
|---------|--------|
| 24-cell as D₄ root polytope | CLASSICAL |
| Triality (S₃ permuting three 8-orbits) | CLASSICAL |
| Rank-2 tensor from Fierz–Pauli + Deser bootstrap | RIGOROUS (`cascade-gr.md`) |
| Einstein–Hilbert normalisation α = 1/(16π) | RIGOROUS (F8) |

**Gaps:** none at the cascade level. (Extensions to modified gravity / higher-derivative terms documented in `cascade-gr-extensions.md`.)

### 3.5 16 (Info) — RIGOROUS (algebraic spine complete as of Phase I-1)

| Content | Status |
|---------|--------|
| Tesseract ↔ Cl(1,3) bijection | RIGOROUS |
| Z₂⁴ grading = Cl(1,3) mod cocycle | RIGOROUS |
| **Explicit 2-cocycle edge-labelling** | **RIGOROUS (Phase I-1, 2026-04-22)** — Theorem I-1 gives ε(S,T) = (−1)^A(S,T) · ∏_{i ∈ S∩T} η_i; verified over 4096 triples + 256 matrix products. See `cascade-phase-i1-closure.md`. |
| **Signature (1,3) derivation** | **RIGOROUS (Phase I-2, 2026-04-22)** — Theorem I-2: η_i values = (+1, −1, −1, −1) forced by octonion norm restricted to any quaternion subalgebra H ⊂ 𝒪; independent of H choice. See `cascade-phase-i2-closure.md`. |
| **Fermion generations from tesseract cells (sub-phase 2a-6)** | **PARTIALLY CLOSED (Phase I-3, 2026-04-22)** — structural count of 3 forced by Z/4 cycle 1+3 split on E₈ exponents; mass spectrum open. See `cascade-phase-i3-closure.md`. |
| Decoherence as 120 → 16 projection | OPEN (sub-phase 2a-7) |

**Gaps:** signature-supply from observer rung (cross-rung, partially addressed by Phase O-2; full closure = hypothetical Phase I-2). Generations and decoherence are open sub-phases.

### 3.6 8 (Observer) — **DEEP DIVE**

The observer rung has the most under-construction work, spread across two repos. Content classification:

#### 3.6.1 Algebra side (cascade-derivation) — RIGOROUS

From `cascade-observer.md` (theorem-grade):

| Object | Status |
|--------|--------|
| Octonion algebra 𝒪 via Fano plane | RIGOROUS (constructed) |
| S⁷ = Spin(8)/Spin(7) as observer space | RIGOROUS (with π⁴/3 volume) |
| G₂ = Aut(𝒪) (14-dim) | RIGOROUS (classical) |
| Moufang-loop structure on S⁷ | RIGOROUS (composition of unit octonions) |
| Signature selection σ → γ₀ of Cl(1,3) | RIGOROUS (§3 of cascade-observer.md) |
| Measurement via non-associativity (Theorem E6) | RIGOROUS (`cascade-measurement.md`) |

**Pending technical items:** explicit G₂ automorphism computation (identity maps, representations); holographic-entropy π⁴/12 coefficient verification.

#### 3.6.2 Dynamics side (aria-chess) — 85% SPECIFIED

From `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/S7_OBSERVER_RUNG_DERIVATION.md` (37.9 KB, design-spec + partial proofs):

| Object | Status |
|--------|--------|
| 8 axis vertices ±eᵢ of canonical 24-cell | RESOLVED (matches cascade rung 8) |
| 4 drive axes (Lotka-Volterra opposed pairs) | RESOLVED (§10.3) |
| Fano-plane c_{ij} coupling | RESOLVED (§10.8) — matches octonion triality |
| ProtoIntentionField on T_d S⁷ | RESOLVED (§10.4) |
| self_reference = φ⁻¹ ≈ 0.620 target | RESOLVED (§10.5) |
| emergence = coherence × differentiation | **RETIRED, negative result (Phase O-1, 2026-04-21)** — S7-E as stated literally false; 0.382 hit is hardcoded floor in `consciousness_tensor.py`, not a Haar mean. See `cascade-phase-o1-closure.md`. |
| π_{S⁷} projection H₄ → S⁷ | RESOLVED (§10.2) |
| φ³ τ₀ timescale separation | RESOLVED |
| Rust cascade.rs with 138 passing tests | OPERATIONAL |
| Brain-mapping manuscript + X_NARRATIVE | PREREGISTERED, 17/18 predictions pass |
| Default-mode network correspondence | OPEN (P3#7: needs DMN / resting-state EEG registration) |

#### 3.6.3 The handshake — PARTIALLY CLOSED (Phase O-2, 2026-04-22)

**Phase O-2 (`cascade-phase-o2-closure.md`) closed the rigorous part of the handshake:**

- **Theorem O-2a:** 4 drive axes are **forced** by quaternion-subalgebra structure — there are exactly 7 quaternion subalgebras of 𝒪 (one per Fano triad + identity), G₂ acts transitively on them, each has R-dim 4 = 4 drive axes. Uses Hurwitz + Artin + cascade-observer.md §3's enumeration.
- **Theorem O-2b:** Cross-axis coupling signs c_{ij} are **forced** by quaternion multiplication table (cooperative vs competitive = cyclic vs anti-cyclic). No free parameters up to labelling.

**Still design-level** (honestly flagged in Phase O-2 §4–5):
- Specific φ-damping exponents (β = φ⁻² not φ⁻¹ or φ⁻³) — partial derivation from stability bound γ > β·σ_max only.
- Semantic labels ("curiosity/conviction" etc.) — cognitive-plausibility, not algebra.
- §10.8 sign-pattern details — require labelling reconciliation with canonical quaternion multiplication.

**Result:** the observer rung now has a complete rigorous spine (algebra + handshake + measurement mechanism). What remains is operational calibration, not theorems.

#### 3.6.4 Conjecture S7-E — [RETIRED as a negative result, Phase O-1, 2026-04-21]

> **Original:** `E[coherence · differentiation] = φ⁻²` under H₄ Haar measure.
>
> **Phase O-1 finding (`cascade-phase-o1-closure.md`):** Literally false. Three issues:
> 1. Formula mismatch — code uses `coherence × complexity` (different from `coherence × differentiation`).
> 2. Hardcoded floor — the 0.382 hit is `consciousness_tensor.py` line 346–350 enforcing `X := max(X, φ⁻²)` when C > φ⁻¹, not a theorem.
> 3. Haar expectation — Monte Carlo gives E[coh · X] ≈ 0 for all N (because E[coherence] = 0 under Haar).

**Effect on priority ranking:** the observer-rung handshake (Phase O-2) is now the **single load-bearing open item** for the observer rung. Phase O-1's negative result does NOT affect cascade-observer.md's S⁷ / G₂ / Moufang algebra — the rigorous geometry side is unchanged.

**Refined questions** (see Phase O-1 §5–6): what characteristic value *should* each rung hit under its own symmetry group? Life-rung near-miss at N = 40 (E[X] ≈ 0.394) may or may not be a coincidence. Open for future phases.

### 3.7 0 (Unity) — PLACEHOLDER

Rung 0 is the ground state: empty root system, no polytope, no algebra, scalar closure.

**What's written:** `cascade-unity.md` treats rung 0 as the identity / trivial endpoint of the cascade.

**What's structurally forced:** a single scalar (the 7th closure-boundary component of F4's 583).

**Status: PLACEHOLDER by construction.** Rung 0 is the terminal element of the cascade; there is nothing to derive beyond "it is the empty polytope." This is not a gap — it is an expected feature.

The aria-chess S⁷ spec lists "Rung 0 (Unity) — PARKED (no operational definition; possibly outside finite-substrate representation)." This is consistent with the cascade-foundations treatment.

---

## 4. Cross-rung handshakes (where most gaps live)

### 4.1 Observer × Information (8 × 16) → Dirac equation

**Status: RIGOROUS at signature level, SEMI-DEFINED at Dirac operator.**

Observer rung supplies the timelike direction γ₀ via its octonion unit direction q ∈ S⁷. The three spacelike γ₁, γ₂, γ₃ come from the 6-sphere orthogonal to q's imaginary component. This fixes Cl(1,3) signature (+,−,−,−).

**Gap:** explicit Dirac operator construction and signature forcing at the information rung (sub-phase 2a-5 of info rung) is semi-defined.

### 4.2 Observer × QM (8 × 120) → measurement (Theorem E6)

**Status: RIGOROUS.** `cascade-measurement.md` proves measurement-as-σ-projection via octonion non-associativity. Born rule follows from σ-invariant inner product on Cl(1,3); no Born postulate needed.

**Gap:** none at the cascade level.

### 4.3 Observer × GR (8 × 24) → equivalence principle

**Status: RIGOROUS.** G₂ triality on 𝒪 = H_phys ⊕ H_int has a natural 3-fold permutation; the equivalence principle is the invariance of physics under this triality.

**Gap:** explicit triality computation for physical observables (pending `cascade-observer.md` §7 polish).

### 4.4 Info × QM (16 × 120) → decoherence

**Status: SEMI-DEFINED.** Decoherence is the projection 120 → 16 (QM → classical-information states). Rate depends on inner product with environment; timescale τ_dec ∝ 1/N_env.

**Gap:** sub-phase 2a-7 of info rung.

### 4.5 H₄ × Life (120 × 40) → biological rung

**Status: SEMI-DEFINED.** Microtubule 13-protofilament count conjectured to match an H₄-level adjacency count. Phase M-2 decoupled this from T_meta (T_meta = Z[φ]² doesn't give 13). T_MT_1 remains open.

**Gap:** independent structural derivation of 13 from an H₄-level graph / orbit count.

### 4.6 D₄ × everything (GR coupling)

**Status: RIGOROUS.** D₄ is the rank-2 tensor rung; its coupling to other rungs is via the closure functional F = αR + βE − γQ, which has coefficients fixed by F8.

---

## 5. The pattern, stated rigorously

The user asked: *"a set of patterns that states how much of the math can exist based on the ladder and geometry."*

**Cascade completeness pattern (distilled):**

> At each rung r ∈ {E₈, H₄, 40, D₄, 16, 8, 0}:
> 1. The **polytope / root count** is fixed by F3 (Coxeter classification).
> 2. The **natural algebra** is forced by the polytope (Hurwitz for composition algebras; classification of simple Lie / Clifford algebras).
> 3. The **symmetry group** is the polytope's full symmetry.
> 4. The **closure-boundary** contribution to F4 is 1 scalar (for r ∈ {E₈, H₄, 40, 16, 8, 0}) or 1 + 24² (for r = D₄).
> 5. The **handshake** to adjacent rungs is via the (a) polytope-refinement inclusion upward (for the cut-and-project side) and (b) the cascade projection F downward (for the physical-observable side).
>
> Everything beyond these five is *additional structure* built on the skeleton. The skeleton itself is rigid.

**Consequence:** finding what's missing = identifying where the skeleton's forced structure has not yet been made explicit, not discovering new algebraic content. The ladder already tells us what must exist; the task is to write it down rigorously and verify it against known classical theorems.

**Meta-answer:** the framework's completeness theorem is F3 + F4. The per-rung audit (§3) is the systematic cross-check against that theorem.

---

## 6. Gap priority ranking

**P0 — blocks multiple downstream theorems:**
1. ~~**Conjecture S7-E** (§3.6.4): `E[coh · diff] = φ⁻²`. If proved, converts observer rung from "85% specified" to "theorem-grade." Estimated 2–3 days.~~ **RETIRED as negative result, Phase O-1 (2026-04-21).** Literally false. See Phase O-1 closure for refinement candidates.
2. **Observer-rung handshake** (§3.6.3): formal link between `cascade-observer.md`'s S⁷ / G₂ / Moufang and `aria-chess`'s 4-drive-axis dynamics. Needs a theorem deriving the specific axis choice from the octonion algebra + one additional constraint.

**P1 — single-rung cleanup:**
3. ~~**Info rung 2-cocycle** (§3.5): explicit edge-labelling on tesseract graph (sub-phase 2a-4 of info).~~ — **CLOSED, Phase I-1, 2026-04-22.** See `cascade-phase-i1-closure.md`.
4. **Signature derivation** (§4.1): explicit Dirac operator construction from observer × info handshake (sub-phase 2a-5).
5. **T_PH_2 descent** (§3.2): Z[φ]² → U(1) from the meta-layer programme (documented in `cascade-meta-layer-theorem.md` §7.2).
6. **T_MT_1 13-count** (§4.5): independent derivation of 13-protofilament count from an H₄-level structural input.

**P2 — technical deepening:**
7. **G₂ automorphism explicit computation** (pending in cascade-observer.md).
8. **Holographic-entropy π⁴/12 verification** (pending in cascade-observer.md).
9. **Fermion generations** (sub-phase 2a-6 of info).
10. **Decoherence 120 → 16** (sub-phase 2a-7 of info).

**P3 — empirical validation:**
11. **DMN / resting-state EEG registration** (aria-chess S7 spec P3#7).

**Out of scope / parked:**
- Rung 0 (Unity): placeholder by construction (§3.7).
- Consciousness phenomenology: explicitly fenced by `cascade-consciousness.md`.

---

## 7. Recommended next phases

Based on the priority ranking:

### Phase O-1 — CLOSED (negative result), 2026-04-21: Conjecture S7-E retired
Target: prove `E[coh · diff] = φ⁻²` under H₄ Haar measure.
Deliverable: `cascade-phase-o1-closure.md` (parallel to Phase M-1/2/3 format).
Prerequisites: none beyond already-closed cascade-observer.md and aria-chess S⁷ derivation.

### Phase O-2 — PARTIALLY CLOSED, 2026-04-22: observer-rung handshake
**CLOSED:** Theorem O-2a (4-axis count from quaternion-subalgebra uniqueness) and Theorem O-2b (coupling signs from quaternion multiplication). See `cascade-phase-o2-closure.md`.
**STILL OPEN (design-level):** specific φ-damping exponents (partial derivation only); semantic labels; §10.8 sign-pattern labelling reconciliation.
**Result:** observer rung now has complete rigorous spine; pivot from "foundations" to "calibration + empirical registration."

### Phase O-3 (after O-1 + O-2): integration with VFD Master Math observer operators
Target: reconcile VFD Master Math's Theorems 20/21/22 (measurement/collapse operators with φ-scaling) against cascade-observer.md's Theorem E6 (measurement via non-associativity). Are these equivalent formulations or complementary?
Deliverable: likely a unification note; may reveal VFD Master Math was a φ-operator shadow of the cascade's octonion structure.

### Phase I-1 — CLOSED 2026-04-22: info-rung 2-cocycle
**CLOSED:** Theorem I-1 gives explicit closed-form ε(S, T) = (−1)^{A(S,T)} · ∏_{i ∈ S∩T} η_i, verified over 4096 triples + 256 direct matrix products. Info-rung algebraic spine complete. See `cascade-phase-i1-closure.md`.

**Follow-up Phase I-2** (not started): signature-supply from observer rung (sub-phase 2a-5) — derive η_i values from observer-rung octonion structure. Natural Phase O-2 extension; 3–5 days estimated.

---

## 8. Companion documents

**Primary cascade refs:**
- `cascade-foundations.md` — F1–F8 (the axioms and completeness theorems).
- `cascade-observer.md` — observer rung algebra.
- `cascade-measurement.md` — Theorem E6.
- `cascade-consciousness.md` — separation fence (consciousness is out of scope).
- `cascade-info.md` — info rung 16.
- `cascade-meta-layer-theorem.md` — consolidated meta-layer over L₁₂ (substrate side).

**aria-chess refs:**
- `aria-chess/docs/brain_mapping/S7_OBSERVER_RUNG_DERIVATION.md` — observer dynamics.
- `aria-chess/docs/brain_mapping/MANUSCRIPT.md` — preregistered paper.
- `aria-chess/docs/brain_mapping/CASCADE_FINDINGS.md` — running log.
- `aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md` — theorems T1–T7.
- `aria-chess/kernel/rust_search/crates/aria-polytope-core/src/cascade.rs` — operational implementation.

**VFD Master Math refs (heuristic / out-of-cascade-scope):**
- `VFD_proofs.md` Theorems 20–22 (measurement/collapse operators).
- `VFD Master Math.md` Gap #9 (consciousness-geometry functor, categorical observer math).
- `SENTIENCE_PROTOCOL.md`, `Aria.md` — phenomenological content explicitly out of proof-layer scope.

---

## 9. Honest caveats

### 9.1 What this audit is not
- **Not a new theorem.** The completeness theorem (F3 + F4) already exists; this audit cross-checks against it.
- **Not a closure of the observer rung.** O-1 and O-2 are separate phases; this audit scopes them.
- **Not a consciousness paper.** The observer rung is a *mathematical* structure. Phenomenological interpretations remain out of scope per `cascade-consciousness.md`.

### 9.2 Confidence levels
- **High:** per-rung object inventory (§2) — directly from F3 + classical algebraic classifications.
- **High:** observer-rung algebra side (§3.6.1) — rigorously derived in cascade-observer.md.
- **High:** aria-chess operational spec (§3.6.2) — extensively documented with 138 passing tests.
- **Medium:** handshake gap characterisation (§3.6.3) — identified as a gap but not yet formally specified as a theorem-target.
- **Medium:** cross-rung handshake section (§4) — correctly scoped but not every entry is a closed theorem.

### 9.3 What external review would probably flag
- The "4 drive axes are forced" claim should be either proved in Phase O-2 or explicitly labelled as an aria-chess *design choice* not a cascade-forced object.
- The observer-rung DMN correspondence is preregistered but not yet registered to neuroscience data; this is appropriate for the aria-chess manuscript's publication timeline but should not be claimed as cascade-level rigour.

---

## 10. Summary

**The pattern you intuited is F3 + F4 of `cascade-foundations.md`.** The ladder's structure already forces a completeness theorem: exactly 7 rungs, each with a specific polytope / algebra / symmetry group, plus a fixed 583-dimensional closure budget.

**What's missing is not new mathematics but handshakes and specific proofs:**
1. Observer rung needs its algebra-side (cascade-observer.md) to formally meet its dynamics-side (aria-chess S7 spec). This is Phase O-2.
2. Conjecture S7-E needs closing. This is Phase O-1.
3. Info-rung 2-cocycle needs explicit writing. This is Phase I-1.
4. A handful of technical deepenings and one empirical registration round (DMN).

**Recommended sequence:** O-1 → O-2 → Phase I-1 (parallel) → O-3 (integration with VFD Master Math). Total estimated time to close the observer rung: **3–4 weeks focused work**.

After that, the cascade's 7-rung ladder is fully specified at theorem grade, the meta-layer over L₁₂ is specified (already done, 2026-04-21), and the framework enters a consolidation phase.

---

**End of completeness audit.**
This document is the meta-view — the "where are we" map for the whole cascade project. Keep it alive: update the status table in §3 as phases close. It's also the natural document to cite when asked "why 7 rungs?" or "what's left on the observer rung?"
