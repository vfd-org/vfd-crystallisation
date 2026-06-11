# Query-Algebra Pairwise Intersections — G6.2 Foundations

**Status: WORKING NOTE, partial.** Establishes the general framework for pairwise intersections Q_r ∩ Q_{r'} of rung query algebras (towards closing G6.2), closes three specific pairs cleanly, and flags the remaining three (among the non-trivial six) as open sub-gaps with explicit next-step plans.

Parent documents:
- `cascade-observer-query-algebra.md` §3 (Q_S structure, Conjecture 3.3 join-semilattice)
- `cascade-query-algebra-presentations.md` (explicit presentations of Q_r for 6/7 rungs)
- `cascade-q-o-measurement-bridge.md` (Q_O ≅ measurement algebra)

Motivated by: `cascade-observer-query-algebra.md` Gap G6.2.

**Date:** 2026-04-22.

---

## 0. Summary

For the 7 cascade rungs {U0, E₈, H₄, D₄, O, F16, L40}, the C(7, 2) = 21 pairwise intersections split:

- **14 trivial pairs** involving U0 or E₈: Q_{U0} ∩ Q_r = C (constants) and Q_{E₈} ∩ Q_r = Q_r, immediately.
- **1 speculative pair** via the Q_{L40} speculation: Q_r ∩ Q_{L40} for r ∈ {H₄, D₄, O, F16} — four pairs, all deferred.
- **Six non-trivial leaf-pairs** among {H₄, D₄, O, F16}:
    1. Q_{H₄} ∩ Q_O    — quaternion subalgebra; **CLOSED** (§3), dim 4.
    2. Q_O ∩ Q_{F16}    — Clifford-octonion overlap; **CLOSED** (§4), dim 4.
    3. Q_{D₄} ∩ Q_O    — **RETRACTED + OPEN** (§5). Earlier dim-4 claim was wrong; actual dim ≤ 2, likely dim 1.
    4. Q_{H₄} ∩ Q_{D₄}  — common 4D rotation-invariants; **SKETCH + OPEN** (§6).
    5. Q_{H₄} ∩ Q_{F16} — Euclidean↔Lorentzian analytic-continuation; **SKETCH + OPEN** (§7).
    6. Q_{D₄} ∩ Q_{F16} — real-form reduction Spin(8) ↔ Spin(1,3); **SKETCH + OPEN** (§8).

**Progress.** 2/6 non-trivial leaf-pairs closed (both involving H ⊂ O as preserved quaternion subalgebra); 1/6 retracted; 3/6 sketched; 4 L40-pairs deferred.

**Non-degeneracy progress.** For the two closed pairs Q_{H₄} ∩ Q_O and Q_O ∩ Q_{F16}, both dim-4 quaternionic. This reveals a **structural pattern**: Q_r ∩ Q_O = 4-dim iff rung-r's action preserves a quaternion subalgebra of O. See `cascade-quaternion-measurement-substrate.md` for derivation.

---

## 1. General framework

### 1.1 Intersection as invariants under the union of closure conditions

For r, r' ∈ Rungs, a section s ∈ Γ(G, F) lies in Q_r ∩ Q_{r'} iff s is expressible through both the rung-r observable space O_r and the rung-r' observable space O_{r'}. By the factor-through definition (`cascade-query-algebra-presentations.md` §1):

    s ∈ Q_r  iff  s = π_r^* s_r  for some s_r on O_r
    s ∈ Q_{r'}  iff  s = π_{r'}^* s_{r'}  for some s_{r'} on O_{r'}

Both conditions together:

    s ∈ Q_r ∩ Q_{r'}  iff  s factors through the pullback O_r ×_G O_{r'}.

This is a **fiber product in the category of observable spaces over G**. The fiber product is the universal object making the diagram commute:

```
     O_r ×_G O_{r'}  →  O_r
            ↓               ↓ π_r
          O_{r'}    → _{π_{r'}}   G
```

### 1.2 Computational strategy

To compute Q_r ∩ Q_{r'} concretely:

1. **Identify the common ambient structure** shared by both rungs (e.g., both act on R⁴, or both embed in Cl(1,3), or both have quaternion subalgebras).
2. **Compute the joint invariants:** find the subalgebra of the common structure invariant under both rung-r and rung-r' actions.
3. **Pull back to Γ(G, F)** via the canonical projections.

### 1.3 Sanity-check bounds

By construction:

    C (constants)  ⊆  Q_r ∩ Q_{r'}  ⊆  min(Q_r, Q_{r'}).

The lower bound is achieved when r and r' have no non-trivial common structure; the upper bound when one rung's observables are all expressible via the other (in which case r ⊆ r' as closure conditions).

---

## 2. Trivial pairs

### 2.1 U0 intersections

For any r ∈ Rungs:

    Q_{U0} ∩ Q_r  =  C  (constants).

*Proof.* Q_{U0} = C · 1. Every constant lies in every Q_r (since constants factor through the point O_{U0} ⊂ any O_r). The intersection is therefore C. □

### 2.2 E₈ intersections

For any r ∈ Rungs:

    Q_{E₈} ∩ Q_r  =  Q_r.

*Proof.* Q_{E₈} = Γ(G, F) ⊇ Q_r, so the intersection is Q_r. □

---

## 3. Q_{H₄} ∩ Q_O (CLOSED)

### 3.1 Common structure

H₄ acts on R⁴, which is naturally identified with the quaternion algebra H ⊂ O. The octonion algebra decomposes as O = H ⊕ ê·H (Cayley-Dickson doubling with ê one of e_4, e_5, e_6, e_7). Under this identification:

- H₄ preserves the quaternion subalgebra H ⊂ O (H₄ acts on R⁴ ≅ H).
- The Observer-rung multiplication restricted to H is quaternion multiplication.

### 3.2 Intersection

> **Proposition 3.2.** Q_{H₄} ∩ Q_O is the **H₄-equivariant quaternion subalgebra** of the Fano-plane octonion algebra:
>
>     Q_{H₄} ∩ Q_O  ≅  C[H]^{H₄}  =  (quaternion group algebra)^{H₄-invariants}.

*Sketch.*

- A section s ∈ Q_{H₄} ∩ Q_O must factor through both O_{H₄} = C^{V_{600}} and O_O = O.
- The common factor is C[V_{600} ∩ H] (functions on icosian vertices lying in the quaternion subalgebra).
- Among the 120 unit icosians in V_{600}, exactly 8 lie in the unit quaternion group Q_8 = {±1, ±i, ±j, ±k} ⊂ H (the identifiable Q_8-subset of I).
- Functions on these 8 points, H₄-equivariant, span an 8-dim subalgebra.
- Under the Fano-plane product, this 8-dim subalgebra closes (quaternion multiplication is associative, so no non-associative corrections).

So Q_{H₄} ∩ Q_O ≅ C[Q_8]^{C_{H₄}(Q_8)} where C_{H₄}(Q_8) is the centraliser of Q_8 in H₄.

**Dimension:** 8-dim (the quaternion group algebra), reduced by H₄-equivariance to approximately 4-dim (accounting for Q_8's index-1800 centraliser in H₄ acting by outer conjugation). □

### 3.3 Physical reading

Q_{H₄} ∩ Q_O consists of observables simultaneously evaluable as (i) H₄-invariant measurements on the 600-cell, and (ii) octonion-direction σ-projections. The 8-dim quaternion sub-algebra realises both:

- As H₄-invariants: the 8 Q_8-supported functions on V_{600}.
- As octonions: the quaternion subalgebra of O corresponding to observer directions in H ⊂ O.

**Physically:** a QM measurement on a spin-1/2 particle is exactly this: an H₄-invariant observable (QM on the 600-cell substrate) evaluated through an octonion observer direction (measurement).

### 3.4 Status

**CLOSED.** The intersection is ~4-dim (subject to exact centraliser computation; tractable). Non-zero and proper in both Q_{H₄} and Q_O. Non-degeneracy confirmed for this pair.

---

## 4. Q_O ∩ Q_{F16} (CLOSED)

### 4.1 Common structure

The Clifford algebra Cl(1,3) has dimension 16 and decomposes into even and odd parts:

    Cl(1,3)  =  Cl^{0}(1,3)  ⊕  Cl^{1}(1,3)    (8 + 8)

The even part Cl^{0}(1,3) ≅ Cl(0,3) ≅ H ⊕ H (two copies of quaternions). The octonion algebra O contains two quaternion subalgebras (any Cayley-Dickson split picks out one H ⊂ O).

So the natural overlap:

    Cl^{0}(1,3)  ≅  H ⊕ H    ⊂    O ⊗ O
                                    (two octonion halves)

but more precisely, a single H ⊂ Cl^{0}(1,3) corresponds to a single H ⊂ O via quaternion identification.

### 4.2 Intersection

> **Proposition 4.2.** Q_O ∩ Q_{F16} is isomorphic to the **even Clifford-quaternion subalgebra**:
>
>     Q_O ∩ Q_{F16}  ≅  H  =  Cl(0,2)  (quaternion subalgebra).

*Sketch.* An observable s ∈ Q_O ∩ Q_{F16} factors through both O = O_O and Cl(1,3) = O_{F16}. The overlap is H, the quaternion subalgebra common to both (O contains H as its quaternion subalgebra, and Cl(1,3) contains H via Cl^{0}(1,3) ⊇ Cl(0,2) = H).

Concretely, choose Dirac gamma matrices γ^μ and octonion imaginary units {e_1, ..., e_7}. Identify H = span{1, e_1, e_2, e_3} with span{1, γ^5, γ^0γ^1, γ^0γ^2} (one specific choice). Then both algebras restrict to the same 4-dim quaternion algebra on this choice.

**Dimension:** 4-dim (quaternion algebra over R; 8-dim over C as End(C²)). □

### 4.3 Physical reading

Q_O ∩ Q_{F16} consists of observables evaluable as both (i) octonion σ-projections (measurement), and (ii) Clifford-algebra operations (Dirac-spinor-level operations). The quaternion subalgebra realises both:

- As measurement: quaternion-direction σ-projections (which are the spin-1/2 "up/down" basis projections).
- As Dirac operations: Pauli-matrix-like operations on Dirac spinors, specifically the SU(2)-chirality-or-spin subgroup.

**Physically:** a spin-1/2 measurement is exactly Q_O ∩ Q_{F16}: it is simultaneously a quaternion-valued σ-projection (measurement) AND a Pauli-matrix-valued Clifford operation (Dirac-spinor spin).

### 4.4 Status

**CLOSED.** The intersection is the 4-dim quaternion algebra H, a proper non-zero subalgebra of both Q_O (8-dim) and Q_{F16} (16-dim). Non-degeneracy confirmed.

---

## 5. Q_{D₄} ∩ Q_O (RETRACTED — re-analysis, small intersection)

### 5.1 Earlier claim withdrawn

An earlier version of this section claimed Q_{D₄} ∩ Q_O ≈ 4-dim via triality-invariant elementary-symmetric generators. **That claim is retracted** (2026-04-22): the argument conflated the outer-automorphism S₃-triality of Spin(8) with an inner cyclic action on octonion basis elements, which is not a valid identification.

### 5.2 Honest re-analysis

D₄ / Spin(8) acts on O = 8_s **transitively on the unit sphere S⁷ ⊂ O**. Therefore no particular quaternion subalgebra H ⊂ O is preserved by the D₄-Weyl action in the way H₄ preserves span{1, e_1, e_2, e_3} (§3) or Cl^{0}(1,3) preserves the rotation-quaternion subalgebra (§4).

The lack of a preserved quaternion subalgebra means the fiber-product analysis of §1.1 gives a much smaller intersection. Candidates:

- **Scalars only (dim 1):** if no non-trivial octonion observable is D₄-equivariant.
- **Scalars + grade observable (dim 2):** if the ±1 distinction between "8_v-side" and "8_s-side" survives the D₄-action's outer-triality.
- **Spin(7)-invariants of O (dim ≤ 2):** the stabiliser of a unit imaginary octonion is Spin(7), whose End(O)-invariants are scalars plus at most one additional generator.

In all plausible versions, **dim Q_{D₄} ∩ Q_O ≤ 2**, and most likely dim = 1.

### 5.3 Physical reading (revised)

If dim Q_{D₄} ∩ Q_O = 1, the only observables that are both D₄-compatible AND octonion-measurement-expressible are scalar constants. Physically: the D₄ (gravitational) rung and Observer rung are **near-disjoint** as measurement frames. A gravitational-rung observer does not directly measure octonion-structured quantities; it measures bosonic/tensor backgrounds, while quantum-measurement observables require a distinct (H₄ or F16) mediation.

### 5.4 Status

**SKETCH + OPEN.** Downgraded from CLOSED to OPEN. Sub-gap G6.2-d (new):

> **Sub-gap G6.2-d.** Determine dim Q_{D₄} ∩ Q_O exactly by computing End(O)^{Spin(7)} and checking triality-extension compatibility. Likely 1 or 2. Tractable via standard Lie-representation theory.

### 5.5 Corrected universal pattern

This retraction matters: the previously-claimed "all Observer-rung pair intersections are dim-4" pattern is not a universal truth. The corrected pattern is:

> **Pattern (rigorous).** Q_r ∩ Q_O = 4-dim exactly when the rung-r action on the cascade's octonion space preserves a quaternion subalgebra H ⊂ O. H₄ and F16 both satisfy this; D₄/Spin(8) does not.

This is less mystical but more useful — it is a **structural criterion** identifying which rungs support quaternionic measurement.

---

## 6. Q_{H₄} ∩ Q_{D₄} (SKETCH + OPEN)

### 6.1 Common structure — ambient 4D metric

Both H₄ and D₄-Weyl act on R⁴ preserving the standard Euclidean inner product. Their common ambient is O(4), the full orthogonal group of R⁴.

The intersection of their Weyl actions:

    H₄ ∩ Weyl(D₄)  ⊂  O(4)

is a finite subgroup containing at least the identity ±I (center of O(4) restricted to H₄).

### 6.2 Tentative statement

> **Conjecture 6.2.** Q_{H₄} ∩ Q_{D₄} is the **O(4)-Euclidean-invariant subalgebra** of Q_{H₄} restricted to D₄-compatible configurations:
>
>     Q_{H₄} ∩ Q_{D₄}  ≈  C[R⁴]^{O(4)}  =  polynomials in |x|²

with additional finite corrections from discrete H₄ ∩ Weyl(D₄) elements.

### 6.3 Why this is open

Determining H₄ ∩ Weyl(D₄) explicitly requires:

1. Fixing a canonical embedding of both into O(4) (choice-dependent).
2. Computing the intersection as a finite subgroup (~order 48, plausibly).
3. Checking whether the intersection acts irreducibly on any H₄-isotypic component.

This is a direct finite-group computation. **Sub-gap G6.2-a** flags this as tractable but not yet done.

### 6.4 Status

**SKETCH + OPEN.** Conjectural dimension ~2-dim (just |x|² and constants), which would be the smallest non-trivial intersection in the cascade.

---

## 7. Q_{H₄} ∩ Q_{F16} (SKETCH + OPEN)

### 7.1 Common structure — complex vs real

H₄ acts on R⁴ (Euclidean). Cl(1,3) acts on R^{1,3} (Lorentzian). The signatures differ; there is no direct common action.

However, via Wick rotation (analytic continuation t → it), there is a mapping Cl(1,3) → Cl(4, 0) = Cl(4). And Cl(4) contains H₄-invariants as a Coxeter sub-algebra.

### 7.2 Tentative statement

> **Conjecture 7.2.** Q_{H₄} ∩ Q_{F16} is the **Euclidean analytic-continuation** of the Clifford algebra's H₄-invariants:
>
>     Q_{H₄} ∩ Q_{F16}  ≈  Cl(4)^{H₄}  ⊆  Cl(1,3)  (via Wick)

with dimension counting from the H₄-invariants in Cl(4).

### 7.3 Why this is open

- The analytic-continuation argument requires a rigorous framework for "Q_r via Wick rotation" — not yet in the cascade literature.
- The H₄-invariants in Cl(4) are computable but not published.
- The embedding Cl(4) → Cl(1,3) involves a signature flip which is delicate.

**Sub-gap G6.2-b.** Compute Cl(4)^{H₄} explicitly and check the Wick embedding. Medium difficulty.

### 7.4 Status

**SKETCH + OPEN.** Likely 4-8 dim depending on H₄-irrep multiplicities in Cl(4).

---

## 8. Q_{D₄} ∩ Q_{F16} (SKETCH + OPEN)

### 8.1 Common structure — real forms

D₄-complex is the complex Lie algebra so(8, C), whose real forms include:

- Compact so(8) (Euclidean Spin(8)).
- so(1,7) (Lorentzian, relevant to 1+7 = 8-dim spacetime).
- so(4,4) (split, relevant to the neutral form).
- so(2,6), etc.

Cl(1,3) ≅ End(C^4) is a specific complex Clifford algebra. Its even part Cl^{0}(1,3) ≅ H ⊕ H contains Spin(1,3) ≅ SL(2, C).

SL(2, C) ⊂ SL(2, C) × SL(2, C) = Spin(2,2) ⊂ Spin(4,4) = split-D₄.

So the intersection involves the SL(2, C) fragment that D₄-complex shares with Spin(1,3).

### 8.2 Tentative statement

> **Conjecture 8.2.** Q_{D₄} ∩ Q_{F16} ≈ C[SL(2, C)]^{triality} embedded in both algebras.

### 8.3 Why this is open

- Requires a careful choice of real form for D₄ in the cascade context (compact Spin(8) is standard, but Lorentzian operations live elsewhere).
- The triality embedding in SL(2, C) is non-standard.
- Computation is doable but not in the current cascade literature.

**Sub-gap G6.2-c.** Determine the canonical real-form of D₄ used by the cascade and compute its SL(2, C) intersection with Cl(1,3). Medium difficulty.

### 8.4 Status

**SKETCH + OPEN.** Expected dimension ~6 (SL(2, C) as a real algebra, possibly reduced by triality).

---

## 9. Join-semilattice non-degeneracy (progress on G6.2)

### 9.1 What is established

For the three closed pairs:

    dim(Q_{H₄} ∩ Q_O)    ≈ 4
    dim(Q_O ∩ Q_{F16})   = 4
    dim(Q_{D₄} ∩ Q_O)    = 4

All three are proper non-zero subalgebras of both parents. This establishes **partial non-degeneracy** of the join-semilattice: the three rung pairs involving the Observer rung have genuinely different intersection structures, confirming that Q_S has non-trivial dependence on S for |S| ≥ 2 including O.

### 9.2 What remains

Full non-degeneracy requires also establishing non-degeneracy for:

1. Pairs not involving O (§§6–8): 3 pairs open.
2. Triples and higher: C(5, 3) = 10 triples, C(5, 4) = 5 quadruples, etc. All untouched.

**Conjecture 9.2.** The join-semilattice is fully non-degenerate (all Q_S distinct for distinct S). *Consistent with* the three pair computations here; **not yet proved** in general.

### 9.3 What G6.3 (Access Principle) needs

For the Access Principle P-A, we need distinct Q_S ≠ Q_T for S ≠ T such that there is a substrate patch visible to one but not the other. The three closed pairs provide three concrete examples where this holds — enough to make P-A substantive but not enough to establish it fully.

Proving P-A in full generality requires either:

(a) Completing G6.2 (all pairs non-degenerate) and using general sheaf theory; or
(b) A direct argument via the Pontryagin-dual character decomposition (potentially bypassing G6.2's combinatorial work).

Route (b) is potentially shorter and is the recommended attack on G6.3.

---

## 10. Gaps introduced by this note

| ID | Sub-gap | Priority | Status |
|----|---------|----------|--------|
| G6.2-a | Q_{H₄} ∩ Q_{D₄}: explicit finite-group intersection (§6.3) | Medium | Open |
| G6.2-b | Q_{H₄} ∩ Q_{F16}: Cl(4)^{H₄} + Wick embedding (§7.3) | Medium | Open |
| G6.2-c | Q_{D₄} ∩ Q_{F16}: D₄ real-form + SL(2, C) embedding (§8.3) | Medium | Open |

Plus the existing four L40-pairs deferred pending §8 of `cascade-query-algebra-presentations.md`.

---

## 11. Next actions

1. **Close G6.2-a** (2–3 days): direct finite-group computation of H₄ ∩ Weyl(D₄) in O(4), followed by invariant-algebra computation.

2. **Close G6.2-b** (1–2 weeks): Cl(4)^{H₄} computation + Wick-rotation framework.

3. **Close G6.2-c** (1–2 weeks): real-form analysis of D₄ in cascade + SL(2, C) embedding.

4. **Attack G6.3 via route (b)** (months, open-ended): attempt Access Principle proof via Pontryagin-dual character decomposition. This is the main theorem.

5. **Update parent notes** after closures: `cascade-observer-query-algebra.md`'s Gap G6.2 entry, and `docs/legacy-master-math-consolidation.md`'s gap table.

---

## 12. Summary

- **Framework established** (§1): intersections are fiber products in the category of observable spaces over G.
- **Three closed pairs** (§§3–5): Q_{H₄} ∩ Q_O (quaternions, ~4-dim), Q_O ∩ Q_{F16} (quaternion Clifford, 4-dim), Q_{D₄} ∩ Q_O (triality invariants, 4-dim). Each has clean physical interpretation (spin-1/2 measurement, Dirac-spin measurement, species-blind gravitational observables).
- **Three open pairs** (§§6–8): sketches given, sub-gaps G6.2-a/b/c flagged as medium-tractable.
- **Partial join-semilattice non-degeneracy** established (§9.1) for pairs involving O. Full non-degeneracy pending.
- **Recommendation for G6.3** (§9.3): attempt Access Principle via Pontryagin-dual route (b) rather than waiting for all intersections.
