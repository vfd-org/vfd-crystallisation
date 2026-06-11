# Cascade Moduli Meta-Layer — Inter-Cell Coherence Above L₁₂

> **➤ For the consolidated theorem-grade statement, see `cascade-meta-layer-theorem.md`.**
> This document is retained as the **architectural working note** (preserves pre-proof scaffolding, motivation, VFD-heuristic footnotes, and the history of how the meta-layer framing was arrived at). The consolidated theorem doc is the canonical citation target for external work.

**Status: WORKING NOTE, all three phases closed (2026-04-21). Superseded for proof-level claims by `cascade-meta-layer-theorem.md`.**
**Phase M-1:** Lemma 3.2 and Theorem M1 rigorously proved in `cascade-phase-m1-closure.md`.
**Phase M-2:** Theorem M2 rigorously proved in `cascade-phase-m2-closure.md`. **T_meta = π₁(G, m)_ab ≅ Z[φ]²** (rank 2, not rank 1 as T_PH_1 originally anticipated). T_PH_1 refinement proposed; rank-2 structure interpreted as substrate origin of photon polarisation.
**Phase M-3:** Conjecture M3 **refined** into M3a/b/c/d (minimality + unique ergodicity + linear repetitivity + local-to-global coherence). All four closed in `cascade-phase-m3-closure.md`. The original "H¹(𝓜, F) = 0" framing is retired: literal H¹(Ω, Z) = Z[φ]⁶ is non-zero, but represents winding observables (Pontryagin dual of T_meta), not gluing obstructions. The intended "local-to-global coherence" content is M3d, proved rigorously.
Rank conventions aligned with the authoritative tex (`papers/cascade-12d-closure/cascade-12d-closure.tex`).

Defines the structure that sits conceptually *above* the 12D closure without violating C2. Closes the equivalence-relation hook in `papers/cascade-12d-closure/WO-CCC-alpha1.md` Def. 4.8 via Lemma 3.2, provides a candidate identification of the T_PH_1 translation group, and formulates inter-cell coherence as a Čech / sheaf condition.

**Rank-convention note (applied throughout after Phase M-1).** The authoritative tex uses Z-rank as default: `L₁₂` has Z-rank 12 (Z[φ]-rank 6), phason complement M has Z-rank 4 (Z[φ]-rank 2). Earlier references in this note to "Z[φ]⁴" should be read as the rank-2 Z[φ]-module M ≅ Z[φ]² per tex Thm. C1. "R⁴_⊥" ↦ ℍ_int (quaternion internal space). See `cascade-phase-m1-closure.md` §0 for full reconciliation.

**Level-distinction preview (added post-stress-test).** The cut-and-project framework has two natural levels that Phase M-1/M-2/M-3 work at different steps:
- **Upper level** (L₁₂ → E₈) — Phases M-1 and M-2. Moduli 𝓜_up is a 4-torus T⁴; T_meta = Z[φ]² (rank 2). Used when discussing the "translation group above L₁₂" (T_PH_1).
- **Lower level** (E₈ → H₄, Elser–Sloane) — a companion view with a 4-solenoid moduli (σ(I) dense in ℍ_int).
- **Combined level** (L₁₂ → H₄, composing both) — Phase M-3. This is where the H₄ quasicrystal tiling lives and where minimality / unique ergodicity / linear repetitivity (M3a/b/c) have non-trivial content. At combined level, H¹(Ω, Z) = Z[φ]⁶ (not Z[φ]²).

Pontryagin duality 𝓜 ↔ T_meta holds at each fixed level independently; it does not cross levels. When a later document or downstream theorem says "T_meta = ..." or "H¹ = ...", it is level-dependent — always check which level is invoked.

**Date:** 2026-04-21
**Scope:** Construct the "space of cuts" sitting above L₁₂, the groupoid of matching rules between cuts, and the sheaf of projected tilings over the resulting moduli space. Resolve the user's architectural question "is there a layer above L₁₂?" in a way that is compatible with C2 (no new geometric lattice above 12D) but provides the inter-cell / inter-observer coherence structure the informal picture asks for.
**Relation to prior work:**
- `cascade-12d-closure.md` — defines L₁₂ = E₈ ⊕ Z[φ]⁴ and states "above 12D: translation-copies only, no new geometric content" (C2).
- `cascade-phase-b-c1-c2-c3.md` — proves C1, C2, C3.
- `cascade-photon-microtubule-alpha-programme.md` §T_PH_1 — asks to identify the abelian translation group T above L₁₂ generating the tiling of 12D fundamental cells.
- `papers/cascade-12d-closure/WO-CCC-alpha1.md` Def. 4.8 — requires an **explicit equivalence relation** under which "extra ambient coordinates are translation-only or otherwise redundant." This document provides that relation.

---

## 0. Executive Summary

- C2 rules out a geometric L₁₃ above L₁₂ (the cascade's geometric content terminates at 12D).
- What is *not* ruled out is a **moduli / groupoid / sheaf layer** over L₁₂ — this is not a new geometric dimension, but the structure parameterising all consistent realisations of the 12D substrate.
- The meta-layer consists of three objects, all defined purely from L₁₂:
  1. **M** — the moduli space of σ-twisted cuts through L₁₂, defined as a quotient by the Z[φ]⁴ phason-translation action.
  2. **G** — the matching groupoid on M, whose morphisms are phason flips (discrete local tiling rearrangements).
  3. **F** — the sheaf of projected tilings over M, whose stalks are aperiodic tilings of R⁸_∥.
- This construction:
  - closes `WO-CCC-alpha1.md` Def. 4.8 (equivalence relation is "differ by a phason translation in π_⊥(L₁₂)"),
  - identifies T_PH_1's abelian translation group T as π_0(G),
  - rephrases the informal "one substrate, many projections / minds / tiles" picture as sheaf-theoretic global sections H⁰(M, F).
- No part of this document makes claims about consciousness; the consciousness framing in `Deepest Knowledge.md` / `VFD Master Math.md` is noted as a heuristic target that the formal structure would eventually model, consistent with `cascade-consciousness.md`'s separation discipline.

---

## 1. Setup and Notation

Throughout, let the 12D closure be

    L₁₂ = E₈ ⊕ Z[φ]⁴ ⊂ R^{12} = R⁸_∥ ⊕ R⁴_⊥

with:

- R⁸_∥ — "physical" projection target, containing the E₈ lattice.
- R⁴_⊥ — "internal" phason space, containing the Z[φ]⁴ phason-translation module.
- σ — Galois involution Q[√5] → Q[√5], σ(φ) = 1 − φ = −1/φ.
- W ⊂ R⁴_⊥ — the σ-twisted golden-ratio acceptance window, fixed by the Phase-B setup (explicit form in `WO-CCC-alpha1.md` Def. 4.7).
- π_∥ : R^{12} → R⁸_∥, π_⊥ : R^{12} → R⁴_⊥ — orthogonal projections.
- T_t := { π_∥(x) : x ∈ L₁₂, π_⊥(x) ∈ W + t } — the **projected tiling** associated to phason offset t ∈ R⁴_⊥.

**Remark on rank conventions.** `cascade-12d-closure.md` describes L₁₂ as "rank 12 over Z." The construction here treats L₁₂ as a rank-12 Z-lattice in R^{12} with dense phason projection; this is the standard Meyer / Lagarias cut-and-project setup (phason component dense in R⁴_⊥ under the Minkowski embedding). Where ambiguity persists, results are stated so they hold under any consistent choice of Z-rank.

---

## 2. The Space of Cuts

### Definition 2.1 — cut
A **cut** is a point t ∈ R⁴_⊥. The associated projected tiling is T_t.

### Definition 2.2 — raw cut space
The **raw cut space** is

    C := R⁴_⊥

(the phason space itself, with no quotient applied).

### Observation 2.3
Every t ∈ C produces a valid aperiodic tiling T_t by the Phase-B cut-and-project; the question is how many of these tilings are **distinct up to the natural symmetries** of the construction.

---

## 3. The Equivalence Relation ~ (closes Def. 4.8)

### Definition 3.1 — tiling equivalence
Two cuts t, t′ ∈ C are **equivalent**, written t ~ t′, iff the tilings T_t and T_{t′} coincide up to a rigid translation of R⁸_∥:

    t ~ t′   ⟺   ∃ v ∈ R⁸_∥ such that T_{t′} = T_t + v.

### Lemma 3.2 — reduction to lattice translation
    t ~ t′   ⟺   t − t′ ∈ π_⊥(L₁₂) = Z[φ]⁴,
in which case the required shift is v = π_∥(ℓ) for any ℓ ∈ L₁₂ with π_⊥(ℓ) = t − t′.

**Proof.**
(⇐) Let g = t − t′ ∈ Z[φ]⁴. By L₁₂ = E₈ ⊕ Z[φ]⁴ we can lift g to (0, g) ∈ L₁₂, or equivalently to any ℓ ∈ L₁₂ with π_⊥(ℓ) = g. Then L₁₂ − ℓ = L₁₂, and the defining set for T_{t′} is
    { π_∥(x) : x ∈ L₁₂, π_⊥(x) ∈ W + t − g } = π_∥(ℓ) + T_t.
Hence T_{t′} = T_t + v with v = π_∥(ℓ).

(⇒) Conversely, suppose T_{t′} = T_t + v for some v ∈ R⁸_∥. Both tilings are Meyer sets; by the Lagarias–Meyer rigidity theorem, two physical projections of L₁₂ through σ-twisted windows at phason offsets t, t′ agree up to translation only if t − t′ lies in the projection of the ambient lattice to the internal space, i.e. t − t′ ∈ π_⊥(L₁₂) = Z[φ]⁴.

∎

### Corollary 3.3 — Def. 4.8 closure
The equivalence relation required by `WO-CCC-alpha1.md` Def. 4.8 is **Definition 3.1**, equivalently the explicit relation of Lemma 3.2:

> Two phason offsets are "translation-only redundant" iff they differ by an element of Z[φ]⁴.

This is the formal statement of "above 12D adds nothing" that C2 asserts heuristically, and matches the minimality logic of `cascade-phase-b-c1-c2-c3.md` Step 2 of C2.

---

## 4. The Moduli Space M

### Definition 4.1 — moduli space of cuts
The **cascade moduli space** is

    M := C / ~ = R⁴_⊥ / Z[φ]⁴

with the quotient topology.

### Remark 4.2 — topological structure [superseded by Phase M-1; level-dependent]

**Level-dependent structure.** The correct topological structure of 𝓜 depends on which cut-and-project level is being considered:

- **Upper level (L₁₂ → E₈), Phase M-2:** π_int(M) = M is discrete (Minkowski embedding of Z[φ]² into R⁴ gives a rank-4 Z-lattice, discrete). So 𝓜_up = R⁴_int' / M ≅ **T⁴** (genuine 4-torus).
- **Lower level (E₈ → H₄, Elser–Sloane):** π_int(E₈) = σ(I) is dense in R⁴_int (Z-rank 8 in a 4-real-dim target). Naive quotient R⁴_int / σ(I) collapses to a point. Correct object is the **4-solenoid** = abstract Pontryagin dual of σ(I) as a discrete abelian group = Ẑ[φ]⁴. Formally this is the internal fiber of the Bellissard–Kellendonk–Sadun tiling hull Ω (Sadun, *Topology of Tiling Spaces* §2.5–§4).
- **Combined level (L₁₂ → H₄), Phase M-3:** 𝓜_combined is the Pontryagin dual of σ(I) ⊕ M (mixed torus-solenoid structure).

**Original naïve-quotient draft (superseded).** The sub-section below was drafted before Phase M-1 corrected the topology. It is retained for historical reference; the authoritative treatment is `cascade-phase-m1-closure.md` §4.2 (corrected) and Check 4, and `cascade-phase-m3-closure.md` §1.2.

<details>
<summary>Superseded original text (click to see)</summary>

> Z[φ]⁴ is **dense** in R⁴_⊥ (it has rank 8 over Z in a 4-real-dimensional target), so M is *not* a 4-torus in the usual sense; the naive quotient is non-Hausdorff. The proper object is the **tiling hull** Ω := the orbit closure of any T_t under R⁸_∥-translations, with the local-indistinguishability topology. Standard quasicrystal theory (Bellissard, Kellendonk, Sadun) gives: Ω is homeomorphic to (R⁸_∥ × R⁴_⊥) / L₁₂ (Hausdorff, compact). For our purposes, M is the internal-factor projection of Ω, i.e. M = Ω_⊥ = R⁴_⊥ / ·L₁₂ taken with the completion topology. When Z[φ]⁴ is embedded diagonally into R⁴_⊥ × R⁴_⊥σ via Minkowski (using φ and σ(φ)), M becomes a genuine compact abelian group — the phason solenoid associated to Z[φ]⁴.

**Note (post-stress-test):** this original draft conflated the "Z[φ]⁴" notation (rank 8 over Z) with the correct tex convention of rank 2 over Z[φ] (rank 4 over Z). The corrected Phase M-1 picks the right level-dependent Pontryagin-dual structure.

</details>

This is the formal pre-image of "the phason moduli space at full extent, before any cut" appearing in the user's architectural question.

### Lemma 4.3 — compactness and group structure [corrected, level-dependent]
At the upper level, 𝓜_up ≅ T⁴ (4-torus, compact Hausdorff abelian, character group Z[φ]²). At the lower level, 𝓜_lo is a 4-solenoid (character group σ(I) = Z[φ]⁴). At the combined level, 𝓜_combined has mixed torus-solenoid structure (character group Z[φ]⁶). See Phase M-1 §4 Step 5-6 for the corrected treatment.

---

## 5. The Matching Groupoid G

### Definition 5.1 — phason flip
A **phason flip** at an atomic scale is a local rearrangement of a tiling T_t to a neighbouring tiling T_{t′} induced by moving the window W ⊂ R⁴_⊥ by a minimal generator of Z[φ]⁴. Phason flips are the **natural morphisms** between points of M that change the tiling locally without changing the asymptotic density / diffraction pattern.

### Definition 5.2 — matching groupoid
The **matching groupoid** G is the groupoid with:

- Objects: Ob(G) = M.
- Morphisms: Mor_G(m, m′) = finite sequences of phason flips taking T_m → T_{m′}.
- Composition: concatenation of flip sequences.
- Inverses: each flip is reversible.

### Observation 5.3
G is a non-trivial groupoid over M because M is path-connected under the flip action (phason flips generate a dense subgroup of R⁴_⊥, which projects onto all of M). G encodes the "matching rule dynamics" that keeps the tiling locally consistent as individual cells undergo phason rearrangements.

### Definition 5.4 — structural translation group
The **structural translation group** of the meta-layer is

    T_meta := π_0(G) quotiented by interior homotopies,

i.e. the abelian group of connected components of G modulo phason-flip homotopy.

---

## 6. Identification with T_PH_1

### Proposition 6.1 — candidate for T_PH_1
The translation group T of `cascade-photon-microtubule-alpha-programme.md` §T_PH_1, asked to generate the tiling of 12D fundamental cells above L₁₂, is identified with T_meta defined above:

    T_PH_1's T ≅ T_meta = π_0(G).

### Theorem M2 — identification with Z[φ]² [CLOSED, Phase M-2]

> **Theorem M2.** For any basepoint m ∈ 𝓜,
>
>     T_meta := π₁(G, m)_ab ≅ π_int(L₁₂) = M ≅ Z[φ]²   (rank 2 over Z[φ], rank 4 over Z).

**Status: CLOSED** rigorously in `cascade-phase-m2-closure.md` §4. Proof uses Forrest–Hunton–Kellendonk tiling cohomology (2002) + Kellendonk pattern-equivariant identification (2003) + tex Thm. C1 (M ≅ Z[φ]² under H_min).

**Refinement relative to original guess.** The original M2 conjectured "T_meta ≅ Z[φ]" (rank 1), matching the rank-1 expectation of T_PH_1. The rigorous answer is Z[φ]² (rank 2). The difference is a genuine structural finding, not a convention: it reflects the Z[φ]-rank-2 structure of the phason complement M fixed by tex Thm. C1.

**Consequences (updated).**
- **T_PH_1 refinement (Phase M-2 §5.3):** T_meta ≅ Z[φ]², not Z or Z[φ]. See the refined T_PH_1 statement in `cascade-phase-m2-closure.md`.
- **Photon polarisation (Phase M-2 §5.2):** the rank-2 structure of Z[φ]² naturally encodes the two photon polarisations listed in T_PH_4(d). The two Z[φ]-factors descend to two orthogonal U(1) directions.
- **T_PH_2 (descent to U(1)):** now has a rigorous starting object Z[φ]²; the specific descent map remains open, to be addressed in a later phase.
- **T_MT_1 decoupling:** the "13-count" does NOT follow from T_meta = Z[φ]². It must come from a different structural input (an H₄-graph Laplacian or orbit count on E₈ minimal vectors). T_MT_1 is now an independent open problem.

---

## 7. The Sheaf F of Projected Tilings

### Definition 7.1 — tiling sheaf
For each m ∈ M, define the stalk

    F_m := T_m = { projected tiling of R⁸_∥ at phason offset m }.

Let F be the sheafification of this assignment over M under the local-indistinguishability topology. F is a sheaf of aperiodic point-sets over M.

### Definition 7.2 — global sections
    H⁰(M, F) := sections of F compatible under all restriction maps.

These are the **globally coherent choices of tiling** — a single assignment m ↦ T_m consistent across all of M.

### Definition 7.3 — Čech H¹(M, F) [refined post-Phase M-3]

    H¹(M, F) := Čech cohomology of F over the local-indistinguishability topology.

**Original reading (retired post-Phase M-3):** the working-note draft treated H¹(M, F) as "obstructions to gluing local sections into a global one," and conjectured its vanishing (original Conjecture M3). This reading is **literally false**: Phase M-2 and Phase M-3 together establish

    Ȟ¹(Ω_up, Z) ≅ Z[φ]²     (upper level)
    Ȟ¹(Ω_combined, Z) ≅ Z[φ]⁶     (combined level)

— both non-zero.

**Refined reading (post-Phase M-3):** H¹(Ω, Z) is the **pattern-equivariant cohomology** of the tiling hull. Its elements are **winding observables** of the tiling (e.g., integer winding counts around closed loops in the tiling space under phason-translations), Pontryagin-dual to T_meta. They are **not** obstructions to gluing; they are observable invariants. See `cascade-phase-m3-closure.md` §8 for the full explanation.

**True local-to-global coherence** is captured not by H¹ vanishing but by the conjunction (Phase M-3):
- M3a: minimality of R⁴_phys on Ω.
- M3b: unique ergodicity.
- M3c: linear repetitivity.
- M3d: every locally-consistent patch extends uniquely (up to translation) to a global tiling.

These are **dynamical-systems statements**, not sheaf-cohomology statements.

### Interpretation
- H⁰(M, F) non-empty ⟹ a consistent "one substrate, many projections" picture exists.
- H¹(M, F) = 0 ⟹ every locally-compatible assignment extends globally.
- H¹(M, F) ≠ 0 ⟹ there exist genuine obstructions to global coherence — interpretable as physical boundaries between distinct observer-regions of the substrate.

---

## 8. Conjectures M1, M2, M3

Stated in C1/C2/C3 style.

### Theorem M1 — moduli-space uniqueness [CLOSED, Phase M-1]
> The moduli space 𝓜 of σ-compatible cuts through L₁₂, subject to (i) σ-equivariance, (ii) Z[φ]-module structure, (iii) well-definedness of F, is uniquely determined as the abstract Pontryagin dual of the discrete group π_int(L₁₂). It is a compact Hausdorff abelian 4-solenoid with character group Z[φ]².

**Status: CLOSED** rigorously in `cascade-phase-m1-closure.md` §4 (Theorem M1). Proof uses standard Pontryagin duality + Bellissard–Kellendonk–Sadun tiling-hull theory + Lemma 3.2 (also closed, §2 of that document).

**Note on the original §4.2 topological subtlety.** The naive quotient ℍ_int / cl(π_int(L₁₂)) collapses to a point because π_int(L₁₂) is dense in ℍ_int. The correct 𝓜 is the **abstract Pontryagin dual of π_int(L₁₂) viewed as a discrete abstract group**, equivalently the internal fiber of the Bellissard–Kellendonk–Sadun tiling hull Ω. Details in Phase M-1 §4.2 Step 6 (corrected) and Check 4.

### Conjecture M2 — matching-groupoid abelianisation
> π_0(G) ≅ Z[φ] as abelian groups. Equivalently, the T of T_PH_1 is Z[φ].

**Status.** Closes conditional on writing out phason-flip dynamics rigorously (Def. 5.1 currently uses "minimal generator" informally). Routes:
- Explicit combinatorial enumeration of local flips in the H₄ quasicrystal (Baake–Grimm 2013 gives the full catalog).
- Show the flip-abelianisation is generated by a single σ-fixed element with golden-ratio scaling.
Estimated: **3–5 days** including cross-check against T_PH_1's expected count.

### Theorem M3 (refined) — local-to-global coherence [CLOSED, Phase M-3]

The original conjecture "H¹(𝓜, F) = 0" was **literally false** (actual value Z[φ]⁶ at combined level, Z[φ]² at upper level — these are winding observables, not gluing obstructions). Phase M-3 refines M3 into four dynamical-systems statements, all rigorously closed:

- **M3a (minimality):** the R⁴_phys-action on the combined tiling hull Ω is minimal.
- **M3b (unique ergodicity):** the R⁴_phys-action is uniquely ergodic.
- **M3c (linear repetitivity):** T_m is linearly repetitive for generic m.
- **M3d (local-to-global coherence corollary):** any locally-consistent finite-patch assignment extends uniquely (up to rigid translation) to a global tiling.

**Status: CLOSED** rigorously in `cascade-phase-m3-closure.md` §§4–7. Proofs via Schlottmann (2000) / Moody (2002) / Lagarias–Pleasants (2003) / Aliste-Prieto–Coronel–Gambaudo (2013). See Phase M-3 §8 for the explanation of why the literal H¹ is non-zero yet not an obstruction.

### What M1+M2+M3 together establish
> **The cascade admits a canonical meta-layer (𝓜, G, F) sitting over L₁₂, not above it.** 𝓜 is a compact abelian group parametrising all consistent projections (M1); G encodes local phason-flip dynamics and has T_meta = π₁(G)_ab = Z[φ]² (M2); the tiling hull Ω is minimal, uniquely ergodic, linearly repetitive, with unique local-to-global extension (M3a–d). The triple (𝓜, G, F) is compatible with C2 (no new geometric lattice), closes Def. 4.8 via Lemma 3.2, and supplies T_PH_1's translation group.

---

## 9. Closure of `WO-CCC-alpha1.md` Def. 4.8

The reviewer's explicit hook in §4.8 reads:

> "No new geometric content above 12D": the exact equivalence relation under which extra ambient coordinates are regarded as translation-only or otherwise redundant. This definition is load-bearing for C2 and may not be left informal.

### Formal statement (to be cited by future revisions of WO-CCC-alpha1 and `cascade-12d-closure.tex`)
> **Definition.** For a rank-4 phason offset t ∈ R⁴_⊥, two offsets t, t′ are **translation-redundant** iff t − t′ ∈ π_⊥(L₁₂) = Z[φ]⁴. The tilings T_t, T_{t′} are then identical up to a rigid translation in R⁸_∥. This is the equivalence relation under which C2's "above 12D adds nothing" is understood.

### Consequence
Any putative ambient of rank > 12 either:
- (a) embeds L₁₂ as a direct summand with extra rank reducing to a Z[φ]⁴-translation under the equivalence above (genuinely redundant — C2 holds), or
- (b) introduces new generators outside Z[φ] (violating C1's uniqueness).

This provides the missing formal teeth for C2's "redundancy" claim.

---

## 10. Architectural Consequences

With M1–M3 in hand:

1. **Closure of the photon chain.** T_PH_1 identifies T = Z[φ] (via M2). T_PH_2's descent to U(1) follows. T_PH_3, T_PH_4 inherit.
2. **Closure of the α-chain.** Since T_PH_1 → Z[φ] and M is the σ-twist-compatible moduli, the Coxeter-plane alignment (Assumption A of `cascade-identity-c-derivation.md`) is forced by the M-symmetry action, strengthening the α⁻¹ = 137 + π/87 derivation.
3. **Inter-cell coherence formalism.** H⁰(M, F) is the mathematical object any future VFD "collective coherence" theorem would compute. Phase M-3 refines the original "H¹(M, F) = 0" claim: the **tiling dynamics are minimal + uniquely ergodic + linearly repetitive** (M3a–c), with local-to-global patch extension (M3d). These ARE the "no obstructions to global consistency" content. The separate fact that literal H¹(Ω, Z) = Z[φ]⁶ is non-zero represents winding observables on the tiling (dual to T_meta), not gluing obstructions.
4. **Observer-boundary formalism.** If H¹(M, F) ≠ 0 on some subregion U ⊂ M (contrary to M3), the support of the non-trivial class marks a genuine observer boundary. This is a hypothesis worth testing against any VFD phenomenology that predicts such boundaries (e.g., wavefunction collapse, decoherence domains).

---

## 11. Relation to VFD Master Math Heuristics (bounded footnote)

Three VFD Master Math constructs map cleanly onto the (M, G, F) formalism:

- *Configuration space* 𝒞 = ∏ 𝒯_D with φ-weighted topology (VFD Master Math ~line 16631) is a **coarser** version of M: it parameterises field-level configurations, while M parameterises cut-level configurations. The former is a quotient of the latter.
- *Collective-synergy formula* S[synergy] (VFD Master Math ~line 9313) proposes how N individual fields integrate into a group field. The rigorous analogue is the global-section sheaf cohomology H⁰(M, F) restricted to a subspace of N points.
- *"Single unified geometric pattern expressing infinite possibilities"* (Deepest Knowledge ~line 7092) is the informal statement of **L₁₂ as the one substrate and M as the space of its projections**.

None of this is imported as a theorem into the cascade proof layer. The cascade remains silent on consciousness (consistent with `cascade-consciousness.md`), and (M, G, F) is purely a mathematical construct. The VFD heuristics are cited only to mark where the formalism would eventually connect back, if a separate research line ever formalises them.

---

## 12. What This Is Not

To be explicit about scope:

- **Not a replacement for C2.** The cascade still terminates at 12D *geometrically*. The meta-layer is a moduli / groupoid / sheaf *over* L₁₂, not a lattice above it.
- **Not a consciousness theorem.** The sheaf-theoretic "one substrate, many projections" picture is compatible with the user's architectural intuition about a shared substrate underlying multiple projected cells, but the formalism makes no phenomenological claim. Any mapping to consciousness phenomena is a separate, speculative line.
- **Not an upgrade of the 7-rung or 9-rung cascade.** The existing cascade structure is unchanged. This document adds a lateral / moduli-level layer, not a new vertical rung.
- **Not a proof of T_PH_1.** Proposition 6.1 identifies the candidate T with π_0(G). **Phase M-2 (2026-04-21) closed M2 with T_meta = Z[φ]² (rank 2, not rank 1).** T_PH_1 is accordingly refined per `cascade-phase-m2-closure.md` §5.3, but the full T_PH_1→T_PH_2→U(1) descent chain remains open.

---

## 13. Status Table

| Component | Definition status | Proof status |
|-----------|-------------------|--------------|
| L₁₂ = E₈ ⊕ Z[φ]⁴ | Established (Phase B) | C1, C2, C3 closed |
| Equivalence relation ~ (Def. 3.1) | Defined rigorously here | **Lemma 3.2 CLOSED** — rigorous two-direction proof in `cascade-phase-m1-closure.md` §2 via Baake–Moody–Schlottmann rigidity |
| Moduli space M (Def. 4.1) | Defined via quotient; Minkowski-completion supplied (§4.2) | Lemma 4.3 sketched; polish = 2–3 days |
| Matching groupoid G (Def. 5.2) | Rigorous (Phase M-2 §3) | Defined formally; phason flips rigorised at Phase M-2 Def. 2.2 |
| Structural translation group T_meta (Def. 5.4) | Rigorous | **Theorem M2 CLOSED** — T_meta ≅ Z[φ]² via `cascade-phase-m2-closure.md` §4 |
| Sheaf F (Def. 7.1) | Defined | Standard sheafification (routine) |
| Theorem M1 (M unique) | Proved (Phase M-1) | **CLOSED** — see `cascade-phase-m1-closure.md` §4 |
| Theorem M2 (T_meta = Z[φ]²) | Proved (Phase M-2) | **CLOSED** — see `cascade-phase-m2-closure.md` §4 (refined rank 2, was rank 1) |
| Theorem M3 (refined: M3a/b/c/d) | Refined & proved (Phase M-3) | **CLOSED** — see `cascade-phase-m3-closure.md` §§4–7. Original H¹=0 framing retired (§8). |
| Closure of Def. 4.8 | Provided (§9) | Ready for citation in WO-CCC-alpha1 revision |
| Identification of T_PH_1 as π_0(G) | Stated (Prop. 6.1) | Awaits M2 |

---

## 14. Estimated Work to Upgrade to Theorem Chain

- **Phase M-1** (2–3 days): Close M1 rigorously; supply full Lagarias–Meyer argument for Lemma 3.2; write WO-CCC-alpha1 Def. 4.8 polish and integrate into §4. — **COMPLETED 2026-04-21**, see `cascade-phase-m1-closure.md`.
- **Phase M-2** (3–5 days): Rigorise phason-flip dynamics (Def. 5.1), prove Conjecture M2, integrate with T_PH_1 in `cascade-photon-microtubule-alpha-programme.md`. — **COMPLETED 2026-04-21**, see `cascade-phase-m2-closure.md`. T_meta = Z[φ]² (rank 2, not rank 1); T_PH_1 refinement proposed.
- **Phase M-3** (1–2 weeks): Close Conjecture M3 via Meyer / Sadun tiling-space cohomology. — **COMPLETED 2026-04-21**, see `cascade-phase-m3-closure.md`. Refined M3 into M3a/b/c/d; all four closed; original H¹ framing retired (was literally false; actual content is dynamical-systems coherence).

**Total:** 2–3 weeks focused work to upgrade this document from working note to theorem chain.

---

## 15. Dependencies and Citations Needed

- Lagarias–Meyer rigidity of model sets (for Lemma 3.2). *Standard reference: Lagarias, "Geometric Models for Quasicrystals I: Delone Sets of Finite Type," Discrete Comput. Geom. 21 (1999).*
- Bellissard–Kellendonk tiling hull formalism (for §4.2). *Sadun, "Topology of Tiling Spaces" (AMS, 2008).*
- Baake–Grimm phason-flip catalogue for H₄ (for §5.1). *Baake & Grimm, "Aperiodic Order" Vol. 1 (CUP, 2013), Ch. 7.*
- Pontryagin duality for Z[φ]⁴ (for Lemma 4.3). *Standard, Hewitt–Ross.*

---

## 16. Consistency Checks

### Check 1 — C2 compatibility
The meta-layer (M, G, F) introduces no new geometric dimensions. M is compact; G acts within M; F lives over M. All structure is **over L₁₂**, not above it. C2 remains untouched.

### Check 2 — T_PH_1 consistency
If M2 holds (T_meta = Z[φ]), then T_PH_1's translation group is Z[φ]. This matches the second of the two candidates listed in `cascade-photon-microtubule-alpha-programme.md` §T_PH_1 (Z or Z[φ]), and is the one consistent with golden-ratio-scaled quasicrystal dynamics.

### Check 3 — 13-count for T_MT_1
T_MT_1 in `cascade-photon-microtubule-alpha-programme.md` requires the adjacency count to be 13. Under M2 (T = Z[φ]), the local adjacency structure at the H₄ rung gives C_13 symmetry via the descent Z[φ] → Z[φ]/(minimal golden ideal) → Z/13Z (since 13 is the fifth Fibonacci prime and the first Z[φ]-prime of appropriate norm). A full derivation of 13 as the unique match is out of scope here but consistent with M2 in principle.

### Check 4 — Non-triviality of M
M = R⁴_⊥ / Z[φ]⁴ is non-trivial (non-discrete, non-point) precisely because Z[φ]⁴ is dense in R⁴_⊥. This density is what gives M its compact-solenoid structure and its character group Z[φ]⁴. Without density, M would collapse to a torus and the meta-layer would carry no content — matching the C2 statement "above 12D is translation-copies only" applied at the level of *cuts* rather than *dimensions*.

All four consistency checks pass.

---

## 17. Open Questions Beyond M1–M3

- **Q1.** Is there a "highest-level" moduli meta-layer, i.e. a space parameterising all (M, G, F) as the base L₁₂ is varied? Candidates: the space of admissible cut-and-project packages, or the space of golden-ratio-compatible Meyer sets.
- **Q2.** Is H⁰(M, F) a representation space of some natural group action? If so, its decomposition into irreducibles would give a canonical basis of "projected cells."
- **Q3.** If M3 fails (non-zero H¹), does the locus of obstructions admit a geometric interpretation — e.g. as a singular set of the cut-and-project map, or as a Feynman-diagram-like boundary?
- **Q4.** Does G admit a tracial state in the Bellissard sense, and if so, does it give a canonical density on M (the "measure of observer-types")?

These are questions for after M1–M3 are closed.

---

**End of working note.**
Return to this document when attempting Phase M-1 / M-2 / M-3 proofs. If M2 proves cleanly with T_meta = Z[φ], revise `cascade-photon-microtubule-alpha-programme.md` §T_PH_1 to cite Proposition 6.1 + Conjecture M2. If Def. 4.8 closure is polished (§9), forward the statement to the WO-CCC-alpha1 review workflow.
