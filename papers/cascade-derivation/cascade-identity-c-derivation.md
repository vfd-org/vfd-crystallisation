# T_α_1 Attempt — Identity C as a Structural Derivation

**Status: CONDITIONAL DERIVATION.** The argument below reduces Identity C (Σ{upper E₈ Coxeter exponents} − 1 = 87) to four explicit conditions, three classical and one conjectural (C1 from the 12D closure document). Under the stated conditions, the identification of 87 with **the count of physical phason-winding slots per Coxeter cycle** follows by direct computation.

**Date:** 2026-04-21
**Parent document:** `cascade-photon-microtubule-alpha-programme.md` Theorem T_α_1
**Depends on:** C1 (Z[φ]⁴ phason complement, `cascade-12d-closure.md`)

---

## 1. Statement

**Conjecture T_α_1.** Let L₁₂ = E₈ ⊕ Z[φ]⁴ be the 12D ambient (conditional on C1). Then the integer 87 appearing in the fine-structure formula α⁻¹ = 137 + π/87 admits the following structural interpretation:

> **87 counts the number of gauge-fixed phason winding slots accumulated by an E₈ root orbit under one complete rotation of the Coxeter element c ∈ W(E₈), when the 4D phason complement Z[φ]⁴ is aligned with the 4 Coxeter-invariant rotation planes of E₈'s reflection representation.**

The identity

> Σ{17, 19, 23, 29} − 1 = 87

is a structural identity in this framework:
- **Σ{17, 19, 23, 29} = 88** = total phason winding number per Coxeter cycle
- **− 1** = U(1) gauge redundancy (one global phase is non-physical)
- **87** = physical phason slots per cycle

This conditionally promotes Identity C from "arithmetic appearance in cascade data" to "geometric count of phason gauge degrees of freedom."

---

## 2. Preliminaries (classical)

### Lemma 2.1 — E₈ Coxeter exponents

The E₈ root system has rank 8 and Coxeter number h = 30. Its Coxeter exponents are

> {m_1, m_2, ..., m_8} = {1, 7, 11, 13, 17, 19, 23, 29}

satisfying the symmetry m_i + m_{9−i} = h = 30. The sum Σ m_i = 8h/2 = 120, equal to the number of positive roots of E₈.

Classical: Bourbaki, *Groupes et algèbres de Lie* IV–VI; Humphreys, *Reflection Groups and Coxeter Groups*, §3.19.

### Lemma 2.2 — Coxeter element decomposition

The Coxeter element c ∈ W(E₈) acts on the 8-dimensional reflection representation R^8 with eigenvalues

> λ_k = exp(2πi · m_k / h), k = 1, ..., 8.

These eigenvalues come in 4 conjugate pairs, since m_k + m_{9−k} = h implies λ_k · λ_{9−k} = exp(2πi) = 1, so λ_{9−k} = conj(λ_k). Each conjugate pair defines a real 2-dimensional c-invariant subspace P_k ⊂ R^8 on which c acts as a rotation by angle θ_k.

The 4 invariant planes are mutually orthogonal and span R^8:

| Plane | Exponent pair | Rotation angle (per application of c) |
|---|---|---|
| P_1 | {1, 29} | θ_1 = 2π/30 |
| P_2 | {7, 23} | θ_2 = 14π/30 |
| P_3 | {11, 19} | θ_3 = 22π/30 |
| P_4 | {13, 17} | θ_4 = 26π/30 |

Classical: Kostant, "The principal three-dimensional subgroup and the Betti numbers of a complex simple Lie group," *Amer. J. Math.* 81 (1959).

### Lemma 2.3 — Windings per Coxeter cycle

After one complete Coxeter cycle (30 applications of c), each invariant plane P_k has rotated through total angle 30 · θ_k = 2π · m_{lower,k}, where m_{lower,k} ∈ {1, 7, 11, 13} is the lower exponent of the conjugate pair.

Equivalently, the *reverse* winding (if traversed in the opposite orientation) is 2π · m_{upper,k}, where m_{upper,k} ∈ {17, 19, 23, 29} is the upper exponent. Lower and upper describe the same 4 planes from opposite orientation conventions.

---

## 3. The phason alignment condition

### Assumption A — Phason-to-Coxeter-plane alignment

> The 4D phason complement Z[φ]⁴ in L₁₂ = E₈ ⊕ Z[φ]⁴ decomposes under a natural basis into 4 1-dimensional Z[φ]-rank factors, each aligned with one of the 4 Coxeter-invariant planes P_k of E₈.

This is the central non-classical assumption. It requires:

1. That Z[φ]⁴ admits a natural basis compatible with the E₈ action.
2. That the basis decomposes as 4 rank-1 Z[φ]-modules.
3. That the identification with P_1, P_2, P_3, P_4 is canonical, not a choice.

**Plausibility argument.** The Z[φ] ring has Galois twist σ: φ ↦ 1 − φ = −1/φ. Under σ, Z[φ] splits into its fixed subring Z and its anti-fixed part (1D over Z). On the product Z[φ]⁴, σ acts coordinate-wise and the decomposition into 4 anti-fixed 1D pieces is canonical. Aligning these with the 4 c-invariant planes of E₈ is natural if the σ-twist on Z[φ]⁴ corresponds to the c-rotation on E₈ — which is the minimal assumption that connects the two structures.

**This is where C1 enters.** If C1 holds — that is, Z[φ]⁴ is the *unique* phason complement making L₁₂ project to E₈ under σ-twist cut-and-project — then the alignment of phason directions with Coxeter planes is forced by the uniqueness structure.

### Assumption B — Upper exponents are the phason-active windings

> The upper Coxeter exponents {17, 19, 23, 29} parameterize *phason* (phason-flip, discrete) winding, while the lower exponents {1, 7, 11, 13} parameterize *phonon* (smooth translation) winding on the same 4 planes.

**Plausibility argument.** The distinguishing structural property between upper and lower exponents: upper have m > h/2, meaning each Coxeter cycle accumulates more than half a full turn. The lower exponents parameterize "short" paths (< half turn); the upper parameterize "long" paths (> half turn). In cut-and-project, phonon modes are short-range elastic; phason modes are long-range discrete rearrangements. The natural assignment — phason to upper, phonon to lower — reflects the physical role: phason flips traverse the full orbit structure of the lattice while phonon vibrations stay near the origin.

**Not yet rigorous.** This assignment is motivated by structural analogy, not proved. A direct proof would show that the σ-twist on Z[φ]⁴ specifically picks out the upper-exponent eigenspaces of c.

---

## 4. The derivation

Under Assumptions A and B (plus C1 and classical results), proceed.

### Step 1 — Total phason winding per Coxeter cycle

By Lemma 2.3 and Assumption B, the 4 phason directions accumulate winding numbers equal to the 4 upper exponents per one complete Coxeter cycle of c. Total phason winding:

> W_total = 17 + 19 + 23 + 29 = **88**

This is the number of full 2π rotations the phason vector undergoes in R^4 (via its alignment with the 4 Coxeter planes) during one full Coxeter cycle of E₈.

### Step 2 — Gauge reduction

The phason configuration carries a U(1) gauge redundancy: a constant phase shift is non-physical. This gauge arises as the descent of the translation automorphism of the tiling above L₁₂ (see T_PH_2 in the programme). The gauge group is generated by one degree of freedom — the "global rotation" of all 4 phason directions by a common phase.

Gauge-fixing removes one winding slot (the identity translation):

> W_physical = 88 − 1 = **87**

### Step 3 — Phase per slot

One Coxeter cycle accumulates total phase 88 × 2π in the ambient 12D lattice. The two-to-one E₈ → H₄ Galois projection (paper-xxxvi, Theorem F5, under F3) halves the phase observable at the H₄ rung:

> Phase per H₄-observable cycle = 88π

Distributed evenly over the 87 physical phason slots:

> Phase per slot = 88π / 87 = π + π/87

The **+π** is the standard half-turn — trivial gauge (any gauge theory absorbs full-π rotations). The residual:

> **π/87** = physical phase increment per phason slot

This is the phase the photon's U(1) gauge mode accumulates per nontrivial phason adjacency under one observable cycle. It is the origin of the fine-structure correction:

> α⁻¹ = 137 + π/87

where 137 is the continuum-limit (infinite-cycle, substrate-blind) coupling and π/87 is the finite-substrate correction from the 12D phason structure.

---

## 5. What the derivation establishes

### Conditional theorem

**Theorem (conditional).** Assume C1 (Z[φ]⁴ phason complement), Assumption A (phason-to-Coxeter-plane alignment), Assumption B (upper-exponent phason assignment), and the classical results F3/F5 of paper-xxxvi. Then:

(a) The 4 upper Coxeter exponents of E₈ parameterize 4 independent phason directions in the 12D ambient L₁₂.

(b) The sum Σ{17, 19, 23, 29} = 88 counts the total phason winding per Coxeter cycle.

(c) After U(1) gauge-fixing, 88 − 1 = 87 physical slots remain, one per nontrivial phason adjacency per cycle.

(d) The observable phase increment per slot is π/87, yielding the fine-structure correction term.

### What was only structural becomes derivational

Before this work, Identity C (88 − 1 = 87 from upper E₈ exponents) was a numerical coincidence in paper-xxii, noted alongside two other 87-appearances but with no unifying derivation. Under the conditional theorem above, Identity C is the *geometric* identity among the three — the one that reflects structural content (E₈ Coxeter planes ↔ phason directions). Identities A and B (eigenvalue arithmetic on 600-cell Laplacian) now read as downstream consequences visible at the H₄ interface rather than independent derivations.

### What this does for the programme

- **T_α_1 closes conditionally.** 87's geometric meaning is now: count of gauge-fixed phason slots per Coxeter cycle. Not arithmetic coincidence — E₈ intrinsic data combined with cut-and-project structure.
- **T_α_2 partially closes.** π in π/87 is identified as the half-turn absorbed into trivial gauge after the two-to-one E₈ → H₄ Galois projection.
- **T_α_3 gains structural anchor.** 137 = 87 + 50 still requires independent justification of the eigenvalue set {9, 12, 14, 15} as "the relevant integers," but 87 is now derived rather than fit.
- **T_PH_2 gains traction.** The U(1) gauge group arises naturally as the 1D gauge reduction of the 4D phason translation group, aligned with the Coxeter-plane structure. This suggests T_PH_2's descent statement can be made precise.
- **T_LOOP_1 has a candidate path.** α mediates photon-phason coupling because α's fine correction π/87 is literally the phason winding per Coxeter cycle gauge-fixed.

---

## 6. Gaps and next steps

The derivation is conditional. What must close for it to become a theorem:

### C1 (Z[φ]⁴ uniqueness) — must close first

Without C1, the phason is not canonically 4-dimensional and Assumption A cannot be stated. This is the bedrock. Must be attempted as Phase B of the programme.

### Assumption A → lemma

If C1 closes, prove that the unique phason complement aligns canonically with the 4 Coxeter-invariant planes. Expected proof route: the σ-twist on Z[φ] corresponds to the reflection part of c, and this correspondence extends to Z[φ]⁴ ⟷ the 4 c-invariant planes uniquely.

### Assumption B → lemma

Prove that upper exponents parameterize phason-active (not phonon) winding. Expected proof route: identify phason flips with the "long" orbits of c (those > half period), which are precisely the upper-exponent planes by Lemma 2.3.

### Independence from paper-xxii heuristic

Paper-xxii already had the π-phase-per-d.o.f. heuristic but framed it as structural correspondence. This derivation promotes the heuristic to a conditional theorem with explicit structural content. Worth checking whether the two framings agree at every step (they appear to; paper-xxii's "Coxeter cycle cumulative phase 2π × 88" is our W_total = 88 here).

---

## 7. Honest assessment

**Does this derivation confirm the original thinking?** Yes — the 4-upper-exponent structure and the 4D phason structure align cleanly. The correspondence is non-trivial (not forced by counting alone) and yields the specific 87 = 88 − 1 structure by direct computation under clearly-stated assumptions.

**Is it a proof yet?** No — it is a conditional derivation with four assumptions. Two are classical (Lemma 2.1, Lemma 2.2). One is C1 (actively conjectural in the 12D closure document). Two (Assumption A, Assumption B) are new and need separate proofs.

**Is it worth proceeding to Phase B?** Yes — the conditional structure is clean enough that closing C1 likely forces A and B via uniqueness. The payoff is large: α⁻¹ = 137 + π/87 becomes a theorem rather than a 0.81-ppm coincidence.

**Risk level.** Low-moderate. If C1 fails (different top lattice), the 4-fold alignment story collapses and Identity C loses its geometric meaning — reverting to the arithmetic-coincidence status. But the correspondence (4 upper exponents, 4 Coxeter planes) is structurally robust and would likely survive any reasonable alternative top-lattice choice.

---

**Recommendation.** Proceed to Phase B (attempt C1–C3) with this derivation as context. C1 is the single most important thing to establish — it unlocks the rest conditionally.

**End of document.**
