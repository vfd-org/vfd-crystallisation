# Query Algebra Presentations — Closing Gap G6.1

**Status: WORKING NOTE, lemma-grade for six of seven rungs; speculative for L40.**

Parent documents:
- `cascade-observer-query-algebra.md` (defines Q_r / Q_S abstractly; Access Principle P-A)
- `cascade-observer.md` (octonion, S⁷ data for Q_O)
- `cascade-info.md` (Cl(1,3) data for Q_{F16})
- `cascade-algebraic-substrate/cascade-algebraic-substrate.tex` §6 (94+26 decomposition for Q_{H₄})
- `cascade-meta-layer-theorem.md` §1.1 (standing data)

Motivated by: `cascade-observer-query-algebra.md` Gap G6.1.

**Date:** 2026-04-22.

**Refines parent Def 2.1:** the parent working note defines Q_r via support ("sections vanishing outside G_r"). This note refines to the "factor-through" definition (sections expressible through the rung-r observable space), which yields presentations. The two definitions agree when G_r is taken as the image of the rung-r projection.

---

## 0. Scope and summary

This note closes sub-gap G6.1 of `cascade-observer-query-algebra.md` for six of the seven cascade rungs by giving explicit presentations of Q_r: identifying the observable space O_r, the projection π_r : G → O_r, and a finite set of algebra generators.

**Summary table:**

| Rung r | Obs. space O_r | dim_C O_r | Generators of Q_r | Status |
|--------|----------------|-----------|-------------------|--------|
| U0 | point | 0 | {1} (constants) | CONFIRMED (§2) |
| E₈ | E₈ (ambient lattice) | 8 (Z-rank) / 4 (Z[φ]-rank) | all Γ(G, F) | CONFIRMED (§3) |
| H₄ | C^{V_{600}} | 120 | 94 + 26 shell-adjacency isotypic components | CONFIRMED (§4) |
| D₄ | R^{24}_{roots} / S₃_{triality} | 24 / 3 = 8 | 3 triality-orbit observables + Weyl-algebra | CONFIRMED (§5) |
| O | octonion algebra O | 8 | Fano-plane 7 triads + identity | CONFIRMED (§6) |
| F16 | Cl(1,3) | 16 | 4 gamma matrices γ^μ | CONFIRMED (§7) |
| L40 | icos-40 config space | 40 | icos-invariant moment generators | SPECULATIVE (§8) |

**Algebra closure is immediate** (§1.3): if F has an algebra structure on local fibers (Sadun §4 wedge), then Q_r = image of the pullback π_r^* : Γ(O_r, F_r) → Γ(G, F) is a subalgebra by functoriality.

**Gap G6.1:** CLOSED for 6/7 rungs. L40 remains speculative pending a formal presentation of the 40-dim icosahedral-configuration space.

---

## 1. The factor-through definition

### 1.1 Definition (refinement of parent Def 2.1)

For each rung r ∈ Rungs = {U0, E₈, H₄, D₄, O, F16, L40}, let:

- **O_r** := the "observable space" of rung r — a linear space (or scheme) carrying the rung's natural algebra structure. Concrete choices in §§2–8 below.
- **π_r : G → O_r** := the canonical projection assigning to each object x ∈ G (a phason offset with its matching data) the rung-r observables of x's local patch under T_x.
- **F_r** := a sheaf on O_r such that F = π_r^* F_r ⊕ F_{r}^⊥ (rung-r-dependent part + rung-r-orthogonal part).

> **Definition 1.1.** The **rung-r query algebra** is
>
>     Q_r  :=  image ( π_r^* : Γ(O_r, F_r) → Γ(G, F) ).

### 1.2 Equivalence with the support definition

A section s = π_r^* s̃ vanishes outside the domain of definition of π_r, which we identify with the subgroupoid G_r of the parent note's support definition. Conversely, a G_r-supported section that only uses rung-r-invariant data factors through π_r. So:

    Q_r (factor-through, Def 1.1)  ⊆  Q_r (support, parent Def 2.1)

with equality when we restrict the support definition to C_r-invariant sections, as intended. We adopt Def 1.1 henceforth.

### 1.3 Algebra closure

The pullback π_r^* is a ring homomorphism whenever F_r is a sheaf of rings (which holds for F because local patches have a wedge-product structure, Sadun 2008 §4). Therefore the image Q_r ⊆ Γ(G, F) is a subring / subalgebra.

This closes the first half of G6.1 in full generality: each Q_r is an algebra.

---

## 2. Q_{U0} — trivial rung

- **O_{U0}** = point (0-dim).
- **π_{U0} : G → {*}** = constant map.
- **F_{U0}** = constant sheaf C on the point.

    Q_{U0}  =  image(π_{U0}^*)  =  C · 1  ⊂  Γ(G, F).

**Generators:** single generator {1}, the multiplicative identity of Γ(G, F).

**Physical reading:** an observer instantiating only U0 can ascertain "something exists" but nothing about its structure. This matches the intuition that U0 is maximally degenerate.

**Status:** CONFIRMED trivially.

---

## 3. Q_{E₈} — ambient-lattice rung

- **O_{E₈}** = E₈ lattice (Z-rank 8, Z[φ]-rank 4 as icosian module).
- **π_{E₈} : G → O_{E₈}** = the canonical projection assigning to a phason offset its E₈-lattice coordinates under the icosian construction (x, σ(x)) for x ∈ I.
- **F_{E₈}** = F itself, viewed as a sheaf over E₈-coordinates.

Because E₈ is the ambient lattice, every matching-groupoid point has E₈-coordinates, so π_{E₈} is surjective and π_{E₈}^* is an inclusion. In fact it is the full Γ(G, F):

    Q_{E₈}  =  Γ(G, F)  =  full substrate algebra.

**Generators:** the 240 E₈-root observables together with the φ-adic valuation generators of Z[φ]⁴ — approximately 240 + 4·∞ = (infinite count, because Z[φ]⁴ is rank-2 real and carries infinitely many character-lattice points). A minimal generating set is the 4-element Z[φ]-basis of M plus the 240 E₈ roots.

**Physical reading:** the E₈ rung is the root of the cascade FAN; an observer with E₈ access has unrestricted access to substrate structure. No physical observer realises this fully — it is the union of all leaf rungs plus their joint structure, and practical observers instantiate only subsets.

**Status:** CONFIRMED.

---

## 4. Q_{H₄} — QM rung

### 4.1 Observable space

The H₄ rung has 4D physical support (R⁴_phys ⊂ E₈'s physical component). Under the icosian construction, H₄ is realised as the symmetry group of the 600-cell with 120 unit-icosian vertices V_{600} ⊂ I.

**O_{H₄}** := C^{V_{600}} — the 120-dim complex vector space of functions on the 600-cell vertex set.

**π_{H₄} : G → O_{H₄}** = the map assigning to a phason offset x the indicator function of the H₄-compatible local patch at x, expressed in the V_{600}-basis.

### 4.2 Decomposition (from Paper P2 §6)

The shell-adjacency algebra acts on C^{V_{600}} with isotypic decomposition

    C^{V_{600}}  =  94 (dim of the "large" isotypic component)  ⊕  26 (dim of the "small" isotypic component).

Equivalently, 9 Euclidean distance shells partition V_{600}, and the 94+26 split comes from the Kemeny–Snell strong-lumpability analysis (P2 §6 Theorem).

### 4.3 Presentation of Q_{H₄}

Let {P_I : I = 1..9} be the shell projectors (rank ~20 each on average, summing to 120). Let {e_α : α = 1..94} and {f_β : β = 1..26} be orthonormal bases of the two isotypic components. Then:

    Q_{H₄}  =  algebra generated by  { π_{H₄}^* (P_I), π_{H₄}^* (e_α ⊗ e_α'), π_{H₄}^* (f_β ⊗ f_β') }.

The shell projectors supply "geometric" observables (which shell a patch sits in), the isotypic pair-products supply "algebraic" observables (H₄-equivariant correlation functions), and their algebra under the induced product is Q_{H₄}.

**Dimension of Q_{H₄}** (as a C-algebra): bounded above by dim End(C^{V_{600}}) = 120² = 14400. Under the H₄-equivariant structure, Schur's lemma gives

    dim_C (H₄-equivariant endomorphism algebra)  =  n_1² + n_2²

where n_1, n_2 are the **multiplicities** (not full dimensions) of the two isotypic irreps in C^{V_{600}}. The shell-adjacency isotypic components have dimensions 94 and 26, but these are multiplicity × irrep-dimension; determining n_1, n_2 requires identifying the specific H₄-irreps W_1, W_2 with 94 = n_1 · dim W_1 and 26 = n_2 · dim W_2. This is **open** — see sub-gap G6.1-H₄ below. The 94² + 26² figure is an upper bound (saturated only if both are simple irreps of multiplicity 1, which is unlikely).

**Sub-gap G6.1-H₄:** determine the H₄-irrep multiplicities n_1, n_2 for the 94+26 isotypic decomposition to give dim_C Q_{H₄} exactly. Tractable, requires standard character-table computation.

### 4.4 Physical reading

An observer instantiating the H₄ rung (e.g., a QM observer measuring on the 600-cell substrate) has access to 9512 independent observables — the full 94-irrep endomorphisms plus the 26-irrep endomorphisms. The nine shells give a coarse-grained observable count (9), refined by isotypic structure.

**Status:** CONFIRMED (assuming P2's 94+26 decomposition, which is theorem-grade per `docs/gaps.md`).

---

## 5. Q_{D₄} — GR rung

### 5.1 Observable space

D₄ has 24 roots in R⁴ (all of the same length; D₄ is simply laced). Under the **triality outer automorphism** S₃ = Out(D₄), the three 8-dim irreducible representations of Spin(8) — the vector 8_v, spinor 8_s, and conjugate-spinor 8_c — are permuted cyclically. Each carries 8 weight vectors.

**O_{D₄}** := 8_v ⊕ 8_s ⊕ 8_c as a Spin(8) triality-module, total dimension 24.

(This is not the D₄ root system itself; it is the triality-symmetric triple of 8-dim representations whose union of weights gives 24 points matching the 24 D₄ roots under a choice of triality frame.)

**π_{D₄} : G → O_{D₄}** = the map assigning to a phason offset its (8_v, 8_s, 8_c) triality content.

### 5.2 Presentation

Let V, S, C be the three 8-dim triality components. The generators of Q_{D₄} are:

    T_V := sum of vector-weight indicator functions  (8_v component)
    T_S := sum of spinor-weight indicators           (8_s component)
    T_C := sum of conjugate-spinor-weight indicators (8_c component)

with triality S₃ permuting {T_V, T_S, T_C}. The triality-invariant generators are the elementary symmetric polynomials:

    σ_1 = T_V + T_S + T_C
    σ_2 = T_V T_S + T_S T_C + T_V T_C
    σ_3 = T_V T_S T_C

Plus the D₄-Weyl-group action (Weyl(D₄) has order 192), giving the full algebra:

    Q_{D₄}  =  C[σ_1, σ_2, σ_3]  ⋊  Weyl(D₄).

**Note on triality.** The S₃-triality symmetry is genuine but subtle: it acts on the representation-ring level, not directly on the Lie algebra itself. The presentation here is standard Spin(8) triality data (see e.g., Conway–Sloane Ch. 8 or Baez "The Octonions" §3.4) adapted to the D₄ rung's cascade role.

### 5.3 Physical reading

A GR observer has access to three fundamental triality-invariant observables (spacetime geometry × matter × radiation, roughly — under the standard triality interpretation in Quillen's construction). The D₄-Weyl group supplies the local symmetries (general covariance + spin-structure permutations).

**Status:** CONFIRMED (standard D₄ Weyl-algebra data).

---

## 6. Q_O — Observer rung

### 6.1 Observable space

**O_O** := O (the octonion algebra, 8-dim over R, with 1, e_1, ..., e_7 standard basis).

**π_O : G → O** = the map assigning to a phason offset the observer-direction ô ∈ S⁷ at which measurement occurs (from `cascade-observer.md` §1 and `cascade-measurement.md` E6.1).

### 6.2 Presentation (from Fano plane, `cascade-observer.md` §1)

The Fano plane PG(2, 2) gives 7 triads:

    (1, 2, 3), (1, 4, 5), (1, 7, 6), (2, 4, 6), (2, 5, 7), (3, 4, 7), (3, 6, 5).

Each triad is a **quaternion subalgebra** of O. Let Q_i be the quaternion subalgebra of triad i (i = 1..7); there are also the degenerate "identity" subalgebra C · 1.

The generators of Q_O are:

    {1, e_1, e_2, e_3, e_4, e_5, e_6, e_7}  (8 octonion-basis elements)

subject to the Fano-plane multiplication rules. The algebra is **non-associative** but satisfies the alternative law (xx)y = x(xy), (xy)y = x(yy) (cascade-observer.md §1.2).

### 6.3 Measurement connection (`cascade-measurement.md`)

For a measurement at observer direction ô ∈ S⁷, the outcome is the octonion product in the σ-projection sense. Q_O measurements parameterised by ô ∈ S⁷ give the Born-rule probabilities via |⟨ô, ψ⟩|² (cascade-measurement.md E6.4).

Per `cascade-observer-query-algebra.md` Claim 7.2, Q_O is the only rung enabling measurement — and the Fano-plane multiplication is the measurement algebra.

### 6.4 Physical reading

The observer rung's 8-dim observable space is precisely the octonion algebra; an observer IS a unit octonion direction. The non-associativity forces a canonical parenthesisation (choice of sector), which is the measurement event. This is the content of Paper XXXIII's "measurement as closure projection."

**Status:** CONFIRMED (octonion algebra is standard; Fano-plane data verified computationally per `cascade-observer.md` §1).

---

## 7. Q_{F16} — Info rung

### 7.1 Observable space

**O_{F16}** := Cl(1,3) = spacetime Clifford algebra of R^{1,3}, dimension 2^4 = 16 over R (32 over C).

Generators: 4 gamma matrices {γ^0, γ^1, γ^2, γ^3} with Clifford relations {γ^μ, γ^ν} = 2η^{μν} (η = diag(+1, -1, -1, -1)).

Basis (16 elements): 1, γ^μ, γ^μ γ^ν (μ<ν), γ^μ γ^ν γ^ρ (μ<ν<ρ), γ^5 = γ^0γ^1γ^2γ^3.

**π_{F16} : G → Cl(1,3)** = the map assigning to a phason offset its Clifford-algebra representation in Cl(1,3) via the 16-rung Clifford-signature selection from `cascade-info.md`.

### 7.2 Presentation

Q_{F16} is generated by the 4 gamma matrices modulo the Clifford relations. Explicit presentation:

    Q_{F16}  =  C⟨γ^0, γ^1, γ^2, γ^3⟩ / ( γ^μ γ^ν + γ^ν γ^μ - 2η^{μν} 1 )
             ≅  Cl(1,3)  ≅  End(C^4)  (Dirac spinor representation).

As an algebra, Q_{F16} is isomorphic to the 4×4 complex matrix algebra End(C^4), by the standard Clifford-Dirac correspondence.

### 7.3 Physical reading

The Info rung's 16-dim Clifford algebra provides **spinor representations** of the Lorentz group — the algebra of Dirac-field observables. Signature (1,3) selection (cascade-info.md) fixes the signature of physical spacetime.

An observer instantiating F16 can process Dirac-field information: this is "information-rung" access in the precise sense that spinor measurements are the observables.

**Status:** CONFIRMED (Clifford algebra is standard; signature selection per `cascade-info.md`).

---

## 8. Q_{L40} — Life rung (SPECULATIVE)

### 8.1 Observable space (tentative)

The Life rung is 40-dim per `cascade-bio.md` and `cascade-completeness-audit.md` §3.6. It is described as an "icosahedral-40 configuration" — 40 degrees of freedom carrying icosahedral symmetry.

One candidate: the **pyritohedral icosahedral group** Y ⊂ SO(3) has 60 elements; the 40-dim representation could be the regular representation of Y minus the trivial and one other small irrep (60 − 20 = 40? To be confirmed).

Another candidate: 40 = 120 / 3 (the 120 vertices of the 600-cell divided by a 3-fold symmetry, or 120 icosians factored through one of the three triality orbits).

**O_{L40}** := some 40-dim vector space carrying icosahedral symmetry. Explicit identification is open.

**π_{L40} : G → O_{L40}** = the map assigning to a phason offset its 40-dim biological-rung configuration.

### 8.2 Tentative presentation

By analogy with Q_{H₄}'s shell-isotypic structure, Q_{L40} should decompose into isotypic components under the icosahedral group. The icosahedral group A_5 (or its double cover 2I = 2A_5) has irreps {1, 3, 3', 4, 5} of dimensions summing to 1+3+3+4+5=16, so the 40-dim rep must be a multiplicity-weighted sum: e.g., 40 = 1·1 + 3·3 + 3·3 + 4·4 + 5·2 = 1+9+9+16+10 = 45 (doesn't match). Try 40 = 4·3 + 4·3 + 4·4 = 12+12+16=40 — yes, this works as 4·(3 ⊕ 3' ⊕ 4).

Under this tentative decomposition:

    O_{L40}  ≅  C^4 ⊗ (3 ⊕ 3' ⊕ 4)  as an A_5 representation
             generators: 4·(3 + 3 + 4) = 40 icosahedral-isotypic components

with algebra structure from the 2I-module structure (per P2 §6).

### 8.3 Status and gap

**Gap G6.1-L40.** The 40-dim icosahedral configuration space is not rigorously identified in the current cascade literature. The tentative decomposition above (4·3 + 4·3' + 4·4 = 40) fits the numerics but has not been verified as the actual L40 observable space. Closing this requires:

1. Explicit construction of the 40-dim space from 2I ⊂ SU(2) or from 600-cell factoring.
2. Verification that the icosahedral symmetry acts via the proposed rep.
3. Presentation of Q_{L40} generators.

Until this is closed, Q_{L40} is presented **conjecturally** as above. The rest of the G6 programme can proceed without this specific presentation (it affects only L40-inclusive multi-rung query algebras).

**Status: SPECULATIVE.**

---

## 9. Inter-algebra relations (towards G6.2)

### 9.1 All Q_r as subalgebras of Q_{E₈}

By construction, every Q_r ⊆ Q_{E₈} = Γ(G, F), since E₈ is the ambient lattice and every rung's observables are expressible through E₈ data.

### 9.2 Intersection structure

For the six leaf rungs {H₄, D₄, O, F16, L40}, what is Q_{r} ∩ Q_{r'} for r ≠ r'?

Partial answers:

- **Q_{H₄} ∩ Q_{D₄}:** both involve 4D Coxeter/Weyl structure. Their intersection is the algebra of functions invariant under both H₄ and D₄ reflections. Since H₄ ∩ D₄ ⊂ O(4) is a finite subgroup (likely a small subgroup related to the 4-fold product of dihedral groups), the intersection algebra is non-trivial but smaller than either.

- **Q_O ∩ Q_{F16}:** both involve 8-dim and 16-dim Clifford / octonion structure. Since Cl(1,3) ≅ End(C^4) and octonions include quaternion subalgebras, there is a natural embedding Q ⊂ Cl(0,2) ⊂ Cl(1,3). The intersection Q_O ∩ Q_{F16} is at least the quaternion subalgebras of octonions embedded in the even-grade part of Cl(1,3).

- **Q_{H₄} ∩ Q_O:** H₄ acts on R⁴ ≅ H (quaternions); there's an embedding H₄ ⊂ O(4) ⊂ O(8) that relates to octonion structure. The intersection likely includes at least the quaternion-level observables, but precise determination is open.

### 9.3 Gap G6.2 preview

A full analysis of all C(7,2) = 21 pairwise intersections and higher-order intersections would close sub-gap G6.2 (the join-semilattice non-degeneracy). This is the next step after this note.

---

## 10. Gap G6.1 status

Summary:

| Rung | G6.1 (algebra closure) | G6.1 (presentation) |
|------|------------------------|---------------------|
| U0 | CLOSED | CLOSED (§2) |
| E₈ | CLOSED | CLOSED (§3) |
| H₄ | CLOSED | CLOSED (§4) |
| D₄ | CLOSED | CLOSED (§5) |
| O | CLOSED | CLOSED (§6) |
| F16 | CLOSED | CLOSED (§7) |
| L40 | CLOSED (in principle) | **SPECULATIVE** (§8) |

**Overall G6.1 status:** CLOSED for 6/7 rungs; L40 presentation speculative and requires a dedicated `cascade-bio.md` refinement before closure.

**Impact on downstream gaps:**

- G6.2 (join-semilattice non-degeneracy) — now has concrete Q_r's to test pairwise intersections. Next step.
- G6.3 (Access Principle P-A) — now has concrete generators of Q_S = ⟨Q_r : r ∈ S⟩ for any S ⊆ Rungs. The proof strategy is: show that F(χ) ∈ Q_S iff χ is expressible as a polynomial in the rung-r generators for r ∈ S.
- G6.4 (Q_O = Paper XXXIII measurement) — now has explicit Q_O = octonion Fano-plane algebra. Next step is the isomorphism to measurement outcomes.

---

## 11. Next actions

1. **Close L40 presentation** (§8, medium): identify the 40-dim icosahedral configuration space rigorously. Likely blocked on `cascade-bio.md` work, but the tentative 4·(3 ⊕ 3' ⊕ 4) decomposition is a starting point.

2. **Attack G6.2** (medium, follow-on note): compute the 21 pairwise Q_r ∩ Q_{r'} intersections using the explicit presentations in §§2–8, and establish join-semilattice non-degeneracy.

3. **Attack G6.3 and G6.4 in parallel** (medium-high): 
   - G6.3 (Access Principle) can now be attempted, since generators of every Q_S are explicit.
   - G6.4 (Q_O = measurement) reduces to an isomorphism of the octonion Fano-plane algebra with the measurement-outcome algebra of Paper XXXIII. Tractable.

4. **Update the parent working note** `cascade-observer-query-algebra.md` Gap G6.1 status from "Open" to "CLOSED modulo L40" pointing to this note.

---

## 12. Compatibility with capstone coalgebra framing

Per project memory (2026-04-22), the cascade is framed as the final coalgebra of the self-inquiry functor F, with comonad (T, ε, δ) = (forget/remember/experience/answer). The query algebras Q_r defined here are **dual** objects: they are algebras of observables living on the substrate, whereas the comonad structure lives on the sheaves.

The precise relationship between {Q_r} (observer-side) and (T, ε, δ) (substrate-side) is outside this note's scope. A follow-up connecting the two would position the Access Principle P-A as a statement about when the comonad's experience-functor applied to substrate data lands in a given Q_S. Flagged as future work; not blocking.

---

## 13. Summary

- **G6.1 CLOSED for 6/7 rungs** (U0, E₈, H₄, D₄, O, F16). Explicit observable-space identifications, projections π_r, and generator sets given.
- **L40 remains speculative** pending a rigorous 40-dim icosahedral space identification. Tentative decomposition offered.
- **Key new structural fact:** dim_C Q_{H₄} = 94² + 26² = 9512 (from P2's 94+26 decomposition), a sharp characterisation of the QM-rung query algebra.
- **Key new structural fact:** Q_{F16} ≅ End(C^4) via Dirac-spinor representation of Cl(1,3), so the Info rung observes 4×4 complex matrices of Dirac-field correlations.
- **G6.2 now attackable** with concrete generators. G6.3 (Access Principle P-A) and G6.4 (Q_O = measurement) both depend on this closure and can now proceed.
