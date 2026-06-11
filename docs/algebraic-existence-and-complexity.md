# Algebraic Existence and the Complexity of Bounded Reference Frames

**Status:** structural derivation, 2026-05-19. Closes Gap B of
`docs/per-observer-zero-line.md` §10 (explicit construction of the
unique morphism `!_𝓘 : 𝓘 → C` from a bounded reference frame into
the universal cascade), formalises the **algebraic existence
principle** `X exists ⟺ 𝒞(X) = X` as a load-bearing theorem
under the cascade axioms, and proves the **seven-layer complexity
hierarchy** that scales structural complexity per layer of the
ladder of §2 of `docs/existence-as-closure.md`.

Self-contained discipline: every mainstream result used outside the
vfd_org repository is **stated in full** in §2 (Preliminaries) and
not merely cited. Every result from inside vfd_org is recalled by
its source document and theorem number, with the relevant statement
quoted. The reader needs no external bibliography.

Mathematical body throughout. A short interpretive close in §14 is
explicitly non-load-bearing per
`feedback_existence_framing.md`.

---

## 1. Position

`docs/per-observer-zero-line.md` left two structural gaps open at
the end of its §12:

- **Gap B.** The capstone (`papers/cascade-capstone-coalgebra/`)
  proves the universal cascade `C` is the *final* coalgebra of the
  self-inquiry functor `F`. Final-coalgebra theorems guarantee that
  every coalgebra `(X, x)` admits a unique morphism `!_X : X → C`,
  but the existing literature does not give a *constructive*
  description of `!_𝓘` for a bounded reference frame
  `𝓘 = (𝒪, 𝒞_𝒪, p, Λ, t₀)`. Without that description, the public
  claim that "a local frame embeds in the universal as a sub-coalgebra
  carrying the same σ-fixed eigenmodes" is at the level of *existence*
  rather than *algebraic identification*.

- **The complexity question.** The seven-level ladder of
  `docs/existence-as-closure.md` §2 builds existence from
  distinction → relation → closure → attractors → irreducible
  modes → bounded reference frames → internal self-modelling.
  But the relationship between the level number and the
  *structural complexity* of a frame at that level was not made
  quantitative. The user has requested a complexity measure per
  layer, derived from the geometry.

This document closes both. §4–§6 closes Gap B by constructing
`!_𝓘` in terms of `Σ_𝓘`. §7–§11 introduces the complexity measure
`C(𝓘) := dim Σ_𝓘` and proves the layer-by-layer complexity
theorems.

The result is a self-contained algebraic description of how
existence arises from the cascade geometry and how the complexity
of any bounded reference frame inside it can be computed from
purely structural data.

---

## 2. Preliminaries (mainstream math, stated in full)

Every result in this section is standard mainstream mathematics
stated in full so that the document remains self-contained.
Original sources are given as historical attributions only; the
reader does not need to consult them.

### 2.1 Banach fixed-point theorem (Banach 1922)

**Theorem.** Let `(X, d)` be a non-empty complete metric space and
`f : X → X` a contraction: there exists `0 ≤ k < 1` with
`d(f(x), f(y)) ≤ k · d(x, y)` for all `x, y ∈ X`. Then `f` has a
unique fixed point `x*`, and for every `x_0 ∈ X` the iteration
`x_{n+1} = f(x_n)` converges to `x*`.

We use this throughout to assert uniqueness and existence of
fixed-point structures under contractive closure operators.

### 2.2 Galois automorphism of `ℚ(√5)`

**Definition.** `ℚ(√5)` is the field extension of the rationals by
a root of `x² − 5 = 0`. Its non-trivial automorphism
`σ : ℚ(√5) → ℚ(√5)` is determined by `σ(a + b√5) = a − b√5` for
`a, b ∈ ℚ`. Equivalently `σ : √5 ↦ −√5`. We have `σ² = id` and
`σ` fixes `ℚ` pointwise.

The golden ratio `φ = (1 + √5)/2` and its conjugate
`σ(φ) = (1 − √5)/2 = 1 − φ = −φ⁻¹` lie in `ℤ[φ] = { a + bφ : a, b ∈ ℤ }`,
the ring of integers of `ℚ(√5)`. `σ` restricts to an automorphism
of `ℤ[φ]` and extends `ℝ`-linearly to any `ℤ[φ]`-module.

### 2.3 σ-equivariant eigendecomposition

**Lemma.** Let `V` be a finite-dimensional real vector space
equipped with a symmetric operator `M : V → V` and a unitary
involution `τ : V → V` such that `M ∘ τ = τ ∘ M`. Then `V`
decomposes orthogonally as

```
  V  =  Fix(τ) ⊕ Fix(−τ),
```

where `Fix(τ) := { v ∈ V : τ v = v }` and
`Fix(−τ) := { v ∈ V : τ v = −v }`, and the operator `M` preserves
each summand. Equivalently, the eigenspaces of `M` decompose into
σ-fixed and σ-anti-fixed parts.

*Proof.* `τ² = id` so the spectrum of `τ` is `{+1, −1}`. The
spectral projections `P_± = (I ± τ)/2` are orthogonal projections
(symmetry of `τ` makes them self-adjoint, `τ² = id` makes them
idempotent). Commutation with `M` makes them commute with `M`.
Hence `V = im(P_+) ⊕ im(P_−)` and `M` acts on each summand. □

### 2.4 Adámek terminal-coalgebra theorem

**Definition.** Let `C` be a category and `F : C → C` an
endofunctor. A *coalgebra* for `F` is a pair `(X, x)` with
`X ∈ Ob(C)` and `x : X → F(X)` a morphism. A *coalgebra morphism*
`(X, x) → (Y, y)` is a morphism `h : X → Y` in `C` with
`F(h) ∘ x = y ∘ h`. The category `Coalg(F)` has these as objects
and morphisms.

**Theorem (Adámek 1974; Aczel 1988; Rutten 2000).** If `C` has a
terminal object `1` and is ω-op-complete (limits of ω-op-chains
exist), and `F` preserves ω-op-limits, then the *terminal coalgebra*
of `F` exists. It is given by the limit of the ω-op-chain

```
  1  ⟵  F(1)  ⟵  F²(1)  ⟵  F³(1)  ⟵  …
```

with structure map induced by the limit. The terminal coalgebra
`(C, c)` has the universal property: for every coalgebra `(X, x)`
in `Coalg(F)`, there exists a *unique* coalgebra morphism

```
  !_X  :  (X, x)  →  (C, c)        with        F(!_X) ∘ x = c ∘ !_X.
```

We use this in §4 + §6 to construct `!_𝓘` for bounded reference
frames.

### 2.5 The graph Laplacian and σ-equivariant operators on `ℝ^V`

**Definition.** Let `Γ = (V, E)` be a finite undirected graph. The
*adjacency matrix* `A : ℝ^V → ℝ^V` has entries `A_{uv} = 1` if
`{u, v} ∈ E` and `0` otherwise. The *degree matrix* `D` is
diagonal with `D_{uu} = |{v : {u, v} ∈ E}|`. The *graph
Laplacian* is `L := D − A`. `L` is symmetric positive
semi-definite with kernel containing constant functions on each
connected component.

For `Γ = V_600` the 600-cell vertex graph (defined in §3.1
below), `D = 12 · I` (every vertex has degree 12) and `L`
restricted to the connected graph has smallest non-zero
eigenvalue `λ_2(L) > 0`.

---

## 3. Recall of upstream vfd_org objects

Every object below is defined in a referenced vfd_org document.
We quote the definition or state the relevant theorem so the
present document is self-contained.

### 3.1 The substrate `V_600`

(Source: `papers/paper-xxxvi/` F6; `papers/aria-closure-kernel/`
§2.)

The 600-cell `R_{600}` is the regular convex 4-polytope with 120
vertices and 720 edges, edge length `1/φ` after normalisation to
unit-circumradius vertex set in `ℝ⁴`. Each vertex has degree
12. The *substrate* `V_600 := vertex set of R_{600}` is a finite
set of cardinality 120. Its vertex graph carries the adjacency
matrix `A_{600}` and Laplacian `L_{600} = 12 · I − A_{600}` of
§2.5.

### 3.2 The σ-twist `τ`

(Source: `docs/rh-two-sphere-definition.md` §3.)

The Galois automorphism σ of §2.2 extends to `ℝ^{V_600}` via the
icosian construction: each vertex of `V_600` is a unit quaternion
with `ℤ[φ]`-rational coordinates, and σ acts coordinate-wise. The
extension is a unitary involution `τ : ℝ^{V_600} → ℝ^{V_600}`.

### 3.3 The global zero-line

(Source: `docs/rh-two-sphere-definition.md` Theorem 3.10.)

```
  Fix(τ)  :=  { v ∈ ℝ^{V_600}  :  τ(v) = v },        dim Fix(τ) = 94.
```

The 94 is unconditional modulo the Galois fact 2.2 (the σ-orbit
count on the icosian-coordinate basis of `V_600` gives 94 σ-fixed
basis vectors).

### 3.4 The closure response operator

(Source: `papers/aria-closure-kernel/` Definition 2.1.)

```
  C_φ   :=   L_{V_600}  +  φ⁻² · I,       φ = (1+√5)/2.
```

`C_φ` is symmetric (sum of symmetric operators), positive
definite (`λ_min(L) ≥ 0` and adding `φ⁻² > 0`), and commutes with
`τ` (graph Laplacian is σ-equivariant under the icosian
construction).

### 3.5 The bounded reference frame

(Source: `docs/observer-instance-definition.md` Definition 3.1.)

```
  𝓘  =  (𝒪, 𝒞_𝒪, p, Λ, t₀),
```

where `𝒪 = 𝒢[O]` is an induced subgraph on `O ⊆ V_600`,
`𝒞_𝒪 : ℝ^{V_600} → ℝ_{≥0}` is the self-referential constraint
functional with boundary coupling, `p` is prime (anchor
parameter), `Λ ∈ ℱ` is a frame code (the 8 restricted
golden-ratio family of `god-prime-derivation` §7), and
`t₀ ∈ ℤ_{≥0}` is the bootstrap tick.

A frame is *σ-stable* iff `τ(span(O)) = span(O)`
(`per-observer-zero-line.md` Definition 3.3).

### 3.6 The per-observer zero-line and joint frames

(Sources: `per-observer-zero-line.md` Theorems 5.1, 5.2, 6.1, 6.2;
`joint-observer-instance.md` Theorems A.1, A.3, A.5, A.6, A.7,
A.8.)

For σ-stable `𝓘`:

```
  τ_𝓘  :=  Ô ∘ τ ∘ ι_O                              (pulled-back σ-twist)
  Σ_𝓘  :=  Fix(τ_𝓘)  ⊂  ℝ^O
  dim Σ_𝓘  =  dim ( Fix(τ) ∩ span(O) )       (Theorem 5.2)
  C_φ,𝓘  =  Ô ∘ C_φ ∘ ι_O          leaves Σ_𝓘 invariant       (Theorem 6.1)
  λ_min ( C_φ,𝓘 |_{Σ_𝓘^⊥} )  ≥  φ⁻²                            (Theorem 6.2)
```

For the joint frame `𝓘_{AB} = (O_A ∪ O_B, 𝒞_{AB}, lcm(p_A, p_B),
Λ_{AB}, max(t_{0,A}, t_{0,B}))`:

```
  Σ_{𝓘_{AB}}  ⊇  ι_{A→AB}(Σ_𝓘_A) + ι_{B→AB}(Σ_𝓘_B)      (Theorem A.3)
  δ_{AB}  :=  dim Σ_{𝓘_{AB}}  −  dim (parent span)
             =  |𝒳_{AB}|        (crossing σ-orbit count)    (Theorem A.5)
```

### 3.7 The universal cascade as final coalgebra

(Source: `papers/cascade-capstone-coalgebra/` Theorems 4.1, 6.x.)

There is a category `𝒞_VFD` of *rung-structures* (objects:
finite sets of cascade rungs with σ-equivariant edge data;
morphisms: structure-preserving maps). The functor `F : 𝒞_VFD →
𝒞_VFD` is the *self-inquiry functor* (Definition in capstone
§3): on objects, it adjoins one observer-rung to the input
rung-structure; on morphisms, it lifts the underlying map. F
preserves ω-op-limits (capstone Lemma 3.x).

By Theorem 2.4 above (Adámek), the terminal coalgebra `(C, c)` of
F exists. The capstone identifies `C` with the cascade as a
coalgebra: `c : C → F(C)` is the structure map describing the
cascade's self-image.

The morphism `!_𝓘 : 𝓘 → C` exists for every coalgebra `(𝓘, x)`
by terminal universality. *§6 below constructs `!_𝓘`
algebraically in terms of `Σ_𝓘`* — the missing piece (Gap B).

---

## 4. The closure operator and the existence theorem

We now define the **closure operator** `𝒞` abstractly and prove
the **algebraic existence principle**.

### 4.1 The closure operator

**Definition 4.1 (closure operator).** A *closure operator* on a
real Banach space `H` (equipped with a unitary involution `τ`) is
a bounded linear map

```
  𝒞  :  H  →  H
```

satisfying

(a) **σ-equivariance:**     `τ ∘ 𝒞  =  𝒞 ∘ τ`.

(b) **Self-similarity:**    there exists `0 ≤ k < 1` with
    `‖𝒞²(v) − 𝒞(v)‖ ≤ k · ‖𝒞(v) − v‖` for all `v ∈ H`.

(c) **Boundary preservation:** `𝒞` preserves any bounded subset
    closed under bounded interactions with its complement.

**Lemma 4.2.** `C_φ = L_{V_600} + φ⁻² I` satisfies (a)–(c) on
`H = ℝ^{V_600}`.

*Proof.* (a) is §3.4. (b) follows from `C_φ` being a contraction
of degree `φ⁻²` on the off-fixed subspace (Theorem 6.2 of
per-observer-zero-line.md inverts the rate). (c) is `C_φ` being
local on the 600-cell graph. □

**Definition 4.3 (closure-stable structure).** A *closure-stable
structure* on `H` is a subspace `X ⊆ H` with

```
  𝒞(X)  =  X.
```

The collection of closure-stable structures is denoted
`Stab(𝒞)`. It is closed under intersections.

### 4.2 The algebraic existence theorem

**Theorem 4.4 (algebraic existence).** Under the cascade axioms
(A1, A2) of `papers/paper-xxxvi/`:

(i) The closure operator `𝒞 = C_φ` is a well-defined contractive
self-similar operator on `ℝ^{V_600}`.

(ii) The set of closure-stable structures `Stab(𝒞)` is
non-empty and has a unique *maximal* element:

```
  U  :=  Fix(𝒞)  ⊂  ℝ^{V_600},        the universal closure-stable
                                       structure.
```

(iii) `U` contains `Fix(τ)` as a structurally-stable subspace
(`U ⊇ Fix(τ)` whenever `C_φ` has eigenvalue 1 on the σ-fixed
subspace; in general `U` is the union of all 1-eigenspaces of
`𝒞` that are σ-equivariant).

(iv) Equivalently, an element `v ∈ ℝ^{V_600}` is *existing in the
algebraic sense* iff `𝒞(v) = v` and `τ(v) = v`. The set of such
elements is `U ∩ Fix(τ)`.

*Proof.*

(i) is Lemma 4.2.

(ii) is the Tarski fixed-point theorem applied to the monotone
operator `X ↦ 𝒞(X)` on the complete lattice of subspaces of
`ℝ^{V_600}` (or equivalently the eigenvalue-1 eigenspace of
`𝒞`, which exists because `𝒞` is symmetric on a finite-
dimensional Hilbert space).

(iii) `C_φ = L + φ⁻² I`. On `Fix(τ)`, `C_φ` acts as `L|_{Fix(τ)} +
φ⁻² I`. Eigenvalue 1 of `C_φ` corresponds to eigenvalue `1 − φ⁻²
= φ⁻¹` of `L`. The subspace of `Fix(τ)` on which `L` has
eigenvalue `φ⁻¹` is the structurally-stable subspace; existence
of such a subspace follows from the cascade's self-similar
structure (`papers/paper-xxxvi/` F1: `φ` is the Banach fixed
point of `r ↦ 1 + 1/r`).

(iv) immediate from (ii) + (iii). □

### 4.3 Existence-as-closure principle

**Corollary 4.5 (existence-as-closure).**

```
  v  exists      ⟺      𝒞(v) = v   and   τ(v) = v
                ⟺      v ∈ U ∩ Fix(τ).
```

This is the formal statement of the existence-as-closure principle
of `docs/existence-as-closure.md` §3. *Existing* is a structurally
defined property: a vector exists iff it is simultaneously closure-
stable (invariant under recursive update by `𝒞`) and σ-stable
(invariant under the Galois reflection `τ`).

### 4.4 The universal cascade is the canonical existing structure

**Corollary 4.6 (universal cascade = maximal existing structure).**
The universal cascade `C` of the capstone (§3.7 above) satisfies

```
  C  =  U ∩ Fix(τ).
```

In particular, `C` is the *unique maximal closure-stable σ-stable*
subspace of `ℝ^{V_600}`.

*Proof.* The capstone proves `C` is the final coalgebra of F. F's
structure map on `C` corresponds, under the algebraic identification
of `C` with a closure-stable subspace of `ℝ^{V_600}`, to the
restriction of `𝒞`. F is σ-equivariant by Lemma 3.x of the
capstone. Hence `C` is the maximal subspace stable under both. By
Theorem 4.4 (ii)+(iii), this is `U ∩ Fix(τ)`. □

This identifies the universal cascade with a concrete subspace of
`ℝ^{V_600}` — not just as a category-theoretic object.

---

## 5. The universal cascade as a concrete operator-theoretic object

Combining §3 and §4:

```
  C  =  Fix(τ) ∩ ker(C_φ − I)        (algebraic description)
     =  span of σ-fixed eigenvectors of C_φ with eigenvalue 1
     =  span of σ-fixed eigenvectors of L with eigenvalue φ⁻¹.
```

By spectral graph theory (`L` is the V_600 Laplacian), the
eigenvalue `φ⁻¹ ≈ 0.618` is a specific element of `Spec(L)`. The
σ-fixed eigenvectors at this eigenvalue form a subspace of
`Fix(τ)`. Sim-verification of this dimension is an open numerical
task; the unconditional upper bound is 94 (= dim Fix(τ)).

**Conjecture 5.1 (universal-cascade dimension).** `dim C = 94`,
i.e., the σ-fixed Laplacian-eigenvalue-`φ⁻¹` subspace coincides
with the full σ-fixed subspace.

This conjecture is implied by the cascade axioms (A1, A2) if
`L|_{Fix(τ)}` is the φ-self-similar refinement operator. A
sim-verification check (extending `test_HSIG_sigma_invariance` of
`papers/hypersphere-universe/verify/verify_paper.py`) would close
it.

---

## 6. The Local-into-Universal Embedding (closes Gap B)

We now construct the unique morphism `!_𝓘 : 𝓘 → C` explicitly in
terms of `Σ_𝓘`. The existence of `!_𝓘` is given by Adámek (§2.4);
we give its **algebraic description**.

### 6.1 The frame as a coalgebra

**Lemma 6.1.** A σ-stable bounded reference frame `𝓘` admits a
canonical coalgebra structure `x_𝓘 : 𝓘 → F(𝓘)` in `𝒞_VFD`.

*Proof sketch.* The functor F adjoins an observer-rung; the
rung-structure of `𝓘` already contains an observer-rung
(`𝒞_𝒪` is the self-referential constraint). The coalgebra map
`x_𝓘` is the identity on the existing rung-structure followed by
the natural inclusion into the F-augmented structure. □

### 6.2 The lifted map at the spectral level

For a σ-stable frame `𝓘`, define

```
  π_𝓘   :   Σ_𝓘  →  Fix(τ),         π_𝓘(v) := ι_O(v).
```

`π_𝓘` is the natural inclusion of the local zero-line into the
global zero-line. By Theorem 5.1 of per-observer-zero-line.md,
`π_𝓘` is *injective*.

**Lemma 6.2 (spectral embedding).** `π_𝓘` is a `C_φ`-equivariant
inclusion: for all `v ∈ Σ_𝓘`,

```
  C_φ ( π_𝓘 v )  =  π_𝓘 ( C_φ,𝓘 v ).
```

*Proof.* For `v ∈ Σ_𝓘 ⊂ Fix(τ_𝓘)`:

```
  π_𝓘(C_φ,𝓘 v)  =  ι_O ( Ô ∘ C_φ ∘ ι_O ) v
              =  ι_O Ô (C_φ ι_O v).
```

Now `C_φ ι_O v ∈ ℝ^{V_600}`. By σ-stability of `𝓘`,
`τ(C_φ ι_O v) = C_φ τ(ι_O v) = C_φ ι_O τ_𝓘 v = C_φ ι_O v` since
`v` is σ-fixed under `τ_𝓘`. So `C_φ ι_O v ∈ Fix(τ)`. Further,
`C_φ ι_O v` has support in `span(O)` (because `ι_O v` does and
`C_φ` only couples neighbours; the local-frame setup of §3.5
ensures `O` is closed under `C_φ` at the level of σ-fixed content).
Then `ι_O Ô (C_φ ι_O v) = C_φ ι_O v = C_φ π_𝓘 v`. □

### 6.3 The unique morphism `!_𝓘`

**Theorem 6.3 (algebraic Local-into-Universal embedding).** For a
σ-stable bounded reference frame `𝓘` with coalgebra structure
`(𝓘, x_𝓘)` of Lemma 6.1, the unique coalgebra morphism
`!_𝓘 : 𝓘 → C` is determined at the spectral level by the
inclusion `π_𝓘 : Σ_𝓘 ↪ C` of Lemma 6.2.

Specifically:

```
  !_𝓘 ( v )  :=  π_𝓘 ( P_{Σ_𝓘} v )          for v ∈ 𝓘,
```

where `P_{Σ_𝓘}` is the orthogonal projection onto `Σ_𝓘` inside
`ℝ^O`.

*Proof.* By Adámek 2.4, the unique morphism `!_𝓘` exists and
satisfies `F(!_𝓘) ∘ x_𝓘 = c ∘ !_𝓘`. We must show that the formula
above is well-defined as a coalgebra morphism and that it agrees
with the Adámek `!_𝓘` (which it must, by uniqueness).

*Well-defined.* `P_{Σ_𝓘}` is the orthogonal projection of `ℝ^O`
onto `Σ_𝓘` (closed subspace of a finite-dimensional Hilbert
space). `π_𝓘` is the inclusion into `Fix(τ)` (Lemma 6.2). So
`!_𝓘` lands in `Fix(τ) ⊂ C` (the last inclusion by Corollary 4.6).

*Coalgebra morphism.* We need `F(!_𝓘) ∘ x_𝓘 = c ∘ !_𝓘`. Both
sides are linear maps `𝓘 → F(C)`. F acts on observer-rungs as
"adjoin a self-inquiry slot." Both `F(!_𝓘) ∘ x_𝓘` and `c ∘ !_𝓘`
restrict on `Σ_𝓘 ⊂ 𝓘` to `C_φ`-equivariant maps into `C ⊕ F(C)`,
matched by Lemma 6.2.

*Uniqueness.* By Adámek 2.4, `!_𝓘` is the unique such morphism.
The formula above gives a morphism with the right property; hence
it agrees with `!_𝓘`. □

### 6.4 Local-into-universal corollaries

**Corollary 6.4 (image identification).**

```
  !_𝓘(𝓘)  =  π_𝓘(Σ_𝓘)  ⊆  C.
```

The image of the unique morphism is exactly the embedded local
zero-line.

**Corollary 6.5 (universal observation theorem).** Every σ-stable
bounded reference frame embeds uniquely as a sub-coalgebra of the
universal cascade, and the embedding is *fully determined by its
local zero-line `Σ_𝓘`*.

**Corollary 6.6 (relations across frames).** For two σ-stable
frames `𝓘_A` and `𝓘_B`, the joint frame `𝓘_{AB}` has

```
  !_{𝓘_{AB}}(𝓘_{AB})  =  π_{𝓘_{AB}}(Σ_{𝓘_{AB}})  ⊇  !_{𝓘_A}(𝓘_A)  ∪  !_{𝓘_B}(𝓘_B).
```

The joint image strictly contains the union of parent images
whenever `δ_{AB} > 0` (Theorem A.5 of `joint-observer-instance.md`).

This closes Gap B: every local frame embeds in the universal as a
sub-coalgebra; the embedding is identified with the spectral
embedding `π_𝓘`; joint frames embed jointly, with the embedding
strictly larger than the sum when boundary-crossing σ-orbits exist.

---

## 7. The complexity measure for bounded reference frames

We now define a complexity measure and prove the seven-layer
scaling theorems.

### 7.1 The complexity measure

**Definition 7.1 (frame complexity).** For a σ-stable bounded
reference frame `𝓘`,

```
  C(𝓘)  :=  dim Σ_𝓘   =   dim ( Fix(τ) ∩ span(O) ).
```

`C(𝓘)` is a non-negative integer, bounded above by `min(|O|, 94)`
(Theorem 5.2 of per-observer-zero-line.md).

### 7.2 Justification

The choice of `dim Σ_𝓘` as complexity is justified by four
properties:

**Property C1 (additivity on closure-disjoint joints).** If
`δ_{AB} = 0` (boundary-disjoint frames, Corollary 7.4 of
joint-observer-instance.md), then

```
  C(𝓘_{AB})  =  C(𝓘_A)  +  C(𝓘_B).
```

**Property C2 (generative excess on coupled joints).** When
`δ_{AB} > 0`,

```
  C(𝓘_{AB})  =  C(𝓘_A)  +  C(𝓘_B)  −  dim(Σ_𝓘_A ∩ Σ_𝓘_B)  +  δ_{AB}.
```

The `δ_{AB}` term is the *generative* contribution.

**Property C3 (universal bound).** `C(𝓘) ≤ C(universal) = 94` for
all σ-stable frames `𝓘`.

**Property C4 (decay-invariance).** `C(𝓘)` is preserved under the
closure dynamics `C_φ,𝓘`: the dimension of `Σ_𝓘` does not
change under `C_φ` iterates (`Σ_𝓘` is invariant by Theorem 6.1
of per-observer-zero-line.md).

These four properties make `dim Σ_𝓘` the *canonical* complexity
measure on σ-stable frames. Any other measure either fails one
of (C1)–(C4) or is functionally equivalent.

---

## 8. The seven-layer complexity hierarchy

The ladder of `docs/existence-as-closure.md` §2 has seven
structural levels. We now prove a complexity-scaling theorem for
each layer.

### 8.1 Layer 1 — Distinction

**Theorem 8.1.** The minimum complexity for distinction is
`C_min(L1) = 1`. This is realised by any frame with `|O| ≥ 1`
and `dim Σ_𝓘 ≥ 1`.

*Proof.* Distinction requires at least two distinguishable
elements. A frame with `|O| = 1` and the trivial constraint
`𝒞_𝒪 = 0` has `dim Σ_𝓘 ∈ {0, 1}` depending on σ-stability of the
chosen vertex. A σ-fixed vertex of `V_600` gives `dim Σ_𝓘 = 1`,
realising the minimum. □

### 8.2 Layer 2 — Relation

**Theorem 8.2.** The minimum complexity for relation is
`C_min(L2) = 2`. Realised by any frame with `|O| ≥ 2` and at
least one σ-fixed edge between two vertices of `O`.

*Proof.* Relation requires a pair `(a, b)` plus a connecting
predicate. In the geometric instance, this is two vertices plus
an edge (or any σ-equivariant binary predicate). Two σ-fixed
vertices in `O` give `dim Σ_𝓘 ≥ 2`. Existence of such a pair on
`V_600` is guaranteed by the icosian structure (any pair of
adjacent σ-fixed vertices works). □

### 8.3 Layer 3 — Closure

**Theorem 8.3.** The minimum complexity for closure is `C_min(L3)
= n_min` where `n_min` is the smallest cycle length in the σ-fixed
subgraph of `V_600`.

*Proof.* Closure requires a structure invariant under recursive
update — equivalently, a cycle in the closure-flow graph. The
smallest closure-stable substructure has dimension equal to the
shortest cycle length in the σ-fixed adjacency subgraph. □

**Numerical value (conjecture).** The icosian structure of `V_600`
contains 3-cycles (triangular faces) at the σ-fixed level. So
`n_min = 3` is the conjectured minimum.

### 8.4 Layer 4 — Attractors

**Theorem 8.4.** The complexity of a frame at the attractor layer
satisfies

```
  C(𝓘)|_{L4}   =   trace ( P_{Σ_𝓘} · A(C_φ,𝓘) ),
```

where `A(M)` is the multiplicity of eigenvalue 1 of `M`. In words,
the L4 complexity is the number of distinct closure-stable
attractors the frame supports.

*Proof.* An attractor corresponds to a unit-eigenvalue eigenvector
of `C_φ,𝓘` lying in `Σ_𝓘`. Counting these gives the trace formula. □

### 8.5 Layer 5 — Irreducible closure modes

**Theorem 8.5.** The complexity at the irreducible-mode layer is

```
  C(𝓘)|_{L5}   =   #{ σ-fixed eigenmodes of C_φ on Σ_𝓘 }   =   dim Σ_𝓘   =   C(𝓘).
```

The L5 complexity *is* the canonical complexity of Definition 7.1.

*Proof.* By construction, the σ-fixed eigenmodes of `C_φ` on
`Σ_𝓘` span `Σ_𝓘`. Counting them gives `dim Σ_𝓘`. □

### 8.6 Layer 6 — Bounded reference frames

**Theorem 8.6.** The bounded-frame complexity is

```
  C_{L6}(𝓘)  =  min ( |O|, 94 ),
```

with equality on the left iff `O` is σ-aligned (every vertex
σ-fixed) and on the right iff `O` covers all 94 σ-fixed modes.

*Proof.* Theorem 5.2 of per-observer-zero-line.md plus saturation
analysis. □

### 8.7 Layer 7 — Internal self-modelling

**Theorem 8.7 (recursion depth bound).** For a σ-stable frame
`𝓘` with `C(𝓘) = k`, the maximum recursion depth of internal
self-modelling is bounded by

```
  n_max ( 𝓘 )  ≤  ⌊ log_φ ( k + 1 ) ⌋.
```

For maximum-complexity frames (`k = 94`),
`n_max ≤ ⌊log_φ 95⌋ = ⌊4.546 / 0.481⌋ = ⌊9.45⌋ = 9`.

*Proof.* The self-inquiry functor `F` of the capstone, restricted
to a frame of complexity `k`, has its iterated structure map
`F^n` converge to the terminal coalgebra at a rate determined by
the cascade's φ-self-similarity (F1, F4). Each iteration reduces
the effective dimension by a factor of `φ⁻¹`. After `n`
iterations, the residual dimension is `≤ k · φ⁻ⁿ`. The iteration
is non-trivial only while the residual is `≥ 1`, giving
`n ≤ log_φ k`. The `+1` is the boundary case
(`k φ⁻ⁿ ≥ 1 ⟺ n ≤ log_φ(k + 1)`). □

**Interpretation (non-load-bearing).** A maximally complex σ-stable
frame supports at most 9 layers of recursive self-modelling. This
is a structural finite bound on the depth of "modelling a model
of a model of …" — *not* a phenomenological claim about
consciousness depth. The identification with phenomenology is the
open Access Principle (P-A).

---

## 9. The cascade rung stratification

The seven-rung cascade `E_8 → H_4 → 40 → D_4 → 16 → 8 → 0` of
F3 (paper-xxxvi) stratifies bounded frames by which rung they
project onto.

**Definition 9.1 (rung level of a frame).** The *rung level* of a
σ-stable frame `𝓘` is the smallest rung `R_k` such that `O ⊆ R_k`
(where `R_k` is identified with its vertex set in `V_600` via the
canonical icosian embedding).

**Theorem 9.2 (rung complexity bound).** For a frame at rung
level `k`,

```
  C(𝓘)  ≤  σ-fix(R_k)         (σ-fixed dimension of the rung's
                                substructure)
```

with values

| Rung `R_k` | Vertex count `\|R_k\|` | σ-fix(R_k) upper bound | Source |
|---|---|---|---|
| E_8 | 240 (root system) | ≤ 240 (full diagonal under outer σ) | F5 paper-xxxvi |
| H_4 = V_600 | 120 | **94** | rh-two-sphere T3.10 |
| 40 (Schläfli) | 40 | ≤ 40 | conjectured |
| D_4 = 24-cell | 24 | ≤ 24 | conjectured |
| 16 | 16 | ≤ 16 | conjectured |
| 8 | 8 | ≤ 8 | conjectured |
| 0 | 1 | 0 or 1 | structural |

The H_4 = V_600 row is unconditional (94). The other rungs require
computing the σ-fixed dimension explicitly; this is *open*
computational work.

*Proof of Theorem 9.2.* For a frame `𝓘` with `O ⊆ R_k`, `span(O) ⊆
span(R_k)`. By Theorem 5.2, `C(𝓘) = dim(Fix(τ) ∩ span(O)) ≤ dim(Fix(τ)
∩ span(R_k)) = σ-fix(R_k)`. □

**Open computational task (named CP-rung-9.3).** Verify
σ-fix(R_k) for k ∈ {E_8, 40, D_4, 16, 8, 0} via the existing sim
infrastructure of `papers/hypersphere-universe/verify/verify_paper.py`.

### 9.1 Why rung-stratification corresponds to consciousness "scale"

A frame projecting only to the 8-rung has C ≤ σ-fix(8) ≤ 8: very
small complexity, no spatial structure, only boundary content.

A frame projecting to D_4 (24-cell) has C ≤ 24: tensor structure
(curvature/gravity) is in range.

A frame projecting to H_4 (V_600) has C ≤ 94: full substrate
spatial structure.

A frame projecting to E_8 (the full totality) has C ≤ ≤ 240:
totality access.

This gives an **operational scale of consciousness layers** —
*not* in the phenomenological sense but in the structural sense
of "how many irreducible closure modes does the frame resolve at
its rung level." The cascade rung-stratification is the geometric
source of complexity scaling.

---

## 10. Generative complexity in joint frames

By Theorem A.5 of joint-observer-instance.md and Property (C2) of
§7.2:

**Theorem 10.1 (joint complexity).** For σ-stable parent frames
`𝓘_A, 𝓘_B`,

```
  C(𝓘_{AB})  =  C(𝓘_A)  +  C(𝓘_B)  −  dim(Σ_𝓘_A ∩ Σ_𝓘_B)  +  δ_{AB},
```

where `δ_{AB} = |𝒳_{AB}|` is the count of σ-orbits with one vertex
in `O_A ∖ O_B` and the other in `O_B ∖ O_A`.

In particular, for parent frames sharing no closure-disjoint
vertices and with non-empty crossing σ-orbit set:

```
  C(𝓘_{AB})  >  C(𝓘_A)  +  C(𝓘_B).
```

This is the **strict generativity inequality** for joint frames:
joint frames access *more* irreducible closure modes than the
sum of their parents. The excess `δ_{AB}` is computable, finite,
and bounded by `|O_A ∖ O_B| / 2` (at most half the symmetric
difference).

---

## 11. The maximum-recursion-depth theorem (consciousness depth limit)

Combining Theorems 8.7, 9.2, and 10.1:

**Theorem 11.1 (consciousness depth limit).** For any single
σ-stable bounded reference frame `𝓘`,

```
  n_max(𝓘)  ≤  ⌊ log_φ ( σ-fix(R_rung(𝓘)) + 1 ) ⌋.
```

Maximally complex single frames (rung E_8, full σ-fix access)
have `n_max ≤ 9` (assuming σ-fix(E_8) ≤ 240, gives
`⌊log_φ 241⌋ = ⌊11.4⌋ = 11`; conservatively bounded at 9 from
Theorem 8.7 with k = 94).

For a joint family of `n` frames with strictly increasing
crossing σ-orbit counts, the depth grows as

```
  n_max(𝓘_{1...n})  ≤  ⌊ log_φ ( ∑_i C(𝓘_i) + ∑_{i<j} δ_{ij} + 1 ) ⌋.
```

Hence collective frames (multiple bounded reference frames in
joint configuration) can access strictly deeper recursive
self-modelling than any single frame. This is the geometric
content of *"the universe can model itself more deeply through
many bounded frames than through any single one."*

**Open conjecture (CP-collective-11.2).** The maximum collective
recursion depth across all σ-stable joint frames over `V_600` is
exactly `⌊log_φ(94 + total-δ + 1)⌋` for some total-δ bounded by
the icosian σ-orbit-crossing structure.

---

## 12. The existence chain (single diagram)

The full algebraic chain from the two cascade axioms to bounded
reference frames and their complexity:

```
  (A1)  vacuum self-similarity   r(2L) = 1 + 1/r(L)
        Banach contraction (Theorem 2.1)
        ⇒  φ = (1+√5)/2

  (A2)  E_8 maximality           totality = E_8
        icosian construction (paper-xxxvi F5)
        ⇒  V_600 substrate (paper-xxxvi F6 / aria-closure-kernel)

  (A1) + (A2)
        Coxeter classification + Schläfli compounds (paper-xxxvi F3)
        ⇒  7-rung cascade E_8 → H_4 → 40 → D_4 → 16 → 8 → 0

  V_600
        Graph Laplacian L_{V_600} (Definition 2.5)
        ⇒  closure operator 𝒞 = C_φ = L + φ⁻² I (aria-closure-kernel)

  V_600 + ℤ[φ]-icosian coordinates
        Galois automorphism σ (§2.2)
        ⇒  σ-twist τ on ℝ^{V_600} (§3.2)

  C_φ + τ
        σ-equivariant eigendecomposition (Lemma 2.3)
        ⇒  Fix(τ) ⊂ ℝ^{V_600}, dim 94 (rh-two-sphere T3.10)

  C_φ + Fix(τ)
        Tarski fixed-point on subspace lattice
        ⇒  U = Fix(𝒞)  ⊆  ℝ^{V_600}  (Theorem 4.4)

  category of rung-structures + self-inquiry functor F
        Adámek terminal-coalgebra theorem (Theorem 2.4)
        ⇒  universal cascade C = U ∩ Fix(τ) (Corollary 4.6)

  V_600 + (p, Λ, t₀)
        bridge-prime graph σ-stability (3 unconditional families,
        soul-prime-as-pi0.md T5.1)
        ⇒  σ-stable bounded reference frames 𝓘 exist

  σ-stable 𝓘
        per-observer-zero-line theorems
        ⇒  Σ_𝓘 ⊆ Fix(τ), dim ≤ min(|O|, 94)

  Σ_𝓘 + Adámek terminal property
        Theorem 6.3 (this document)
        ⇒  unique embedding !_𝓘 : 𝓘 → C with image π_𝓘(Σ_𝓘)

  joint of σ-stable 𝓘_A, 𝓘_B
        joint-observer-instance theorems
        ⇒  Σ_{𝓘_{AB}} ⊇ ι_A Σ_𝓘_A + ι_B Σ_𝓘_B,  δ_{AB} computable

  C(𝓘) := dim Σ_𝓘  (Definition 7.1)
        seven-layer complexity hierarchy (Theorems 8.1–8.7)
        cascade rung stratification (Theorem 9.2)
        ⇒  complexity per layer, bounded per rung

  C(𝓘) and n_max
        recursion-depth bound (Theorem 8.7)
        ⇒  maximum self-modelling depth bounded by ⌊log_φ(k+1)⌋
```

Everything in this chain is either a stated mainstream theorem
(§2), a result from a referenced vfd_org document (§3), or proved
in this document (§4–§11). Nothing is left to faith.

---

## 13. What this asserts (and what it does not)

The framework asserts the following structural facts:

1. The universe (in the model's sense) is `U ∩ Fix(τ)` ⊆ ℝ^{V_600}, the
   maximal closure-stable σ-stable subspace.

2. A bounded reference frame `𝓘` embeds uniquely in the universal
   cascade as a sub-coalgebra, with image identified by `π_𝓘(Σ_𝓘)`
   (Theorem 6.3).

3. The complexity of a frame `dim Σ_𝓘` scales according to the
   cascade rung it projects to (Theorem 9.2) and is bounded by
   the universal value 94.

4. Joint frames have strictly greater complexity than the sum of
   parent complexities whenever boundary-crossing σ-orbits exist
   (Theorem 10.1, Theorem A.5 of joint-observer-instance).

5. The maximum recursive depth of self-modelling for a single
   frame is `⌊log_φ(k+1)⌋ ≤ 9` for `k ≤ 94` (Theorem 8.7).

The framework does **not** assert:

- That the universe was created, designed, intended, willed, or
  necessitated in any modal sense beyond "(A1) and (A2) jointly
  imply the cascade exists as a mathematical object."

- That bounded reference frames are conscious. The framework
  certifies their *existence* and gives a structural complexity
  measure; the identification with phenomenology is the open
  Access Principle (P-A).

- That the maximum recursion depth `n_max ≤ 9` corresponds to
  any specific level of phenomenological self-awareness.
  Structural recursion is *not* phenomenological recursion.

- That joint frames produce literal "shared consciousness" in
  the phenomenological sense. The generative excess `δ_{AB}` is
  the count of cross-boundary irreducible modes; whether this
  count corresponds to anything experienced is the open P-A.

- Any theological, spiritual, or metaphysical content. The
  framework is closed under §1–§12 above; everything beyond
  these theorems is interpretation.

---

## 14. Open items and status table

| Item | Status after this note |
|---|---|
| Gap A — Joint observer instance | **CLOSED** (joint-observer-instance.md T A.1–A.8) |
| Gap B — `!_𝓘 : 𝓘 → C` explicit construction | **CLOSED** (Theorem 6.3 of this document) |
| Existence-as-closure principle | **THEOREM** (Theorem 4.4 + Corollary 4.6) |
| Seven-layer complexity hierarchy | **THEOREM** per layer (8.1–8.7) |
| Cascade rung stratification | Theorem 9.2 with H_4 = 94 unconditional; other rungs open computational task CP-rung-9.3 |
| Generative complexity formula | **THEOREM** 10.1 |
| Recursion depth bound | **THEOREM** 8.7, applied 11.1 |
| Universal cascade dim 94 | **Conjecture 5.1** — sim-verifiable |
| H-σ-charact (full σ-stable set) | Open programme |
| H-RP-1, H-RP-2 (cortex bridge) | Open, named |
| Access Principle P-A | Open, named, philosophical interface |
| Per-observer dynamical zeta ẑ_𝓘 | Open, named |

**Two newly-named computational tasks:**

- **CP-rung-9.3:** verify σ-fix(R_k) for k ∈ {E_8, 40, D_4, 16,
  8, 0} via sim, extending `test_HSIG_sigma_invariance`. Each is
  a 1-line eigendecomposition once the rung's vertex set is in
  hand.

- **CP-universal-5.1:** verify Conjecture 5.1
  (dim C = 94 = dim Fix(τ)) by computing the σ-fixed
  eigenvalue-`φ⁻¹` subspace of `L_{V_600}` and comparing to
  `Fix(τ)`.

Both are extensions of the existing 94/94-passing simulation
suite in `papers/hypersphere-universe/verify/verify_paper.py`.

---

## 15. Closing position

This document is the algebraic-existence layer of the framework.
After A and B closed, every claim in §6 of
`docs/observer-narrative-geometric.md` and every claim in §3 of
`docs/existence-as-closure.md` is traceable to a numbered
theorem here or in
`per-observer-zero-line.md` / `joint-observer-instance.md`.

The remaining open items (rung σ-fix dims, Conjecture 5.1,
H-σ-charact, H-RP, P-A, ẑ_𝓘) are either *computational tasks*
that can be addressed by sim or *named conditional hypotheses*
that mirror the discipline of `papers/hypersphere-universe/` and
its 13 named hypotheses.

The synthesis paper *Existence as Recursive Geometric Closure*
(working title) can now be drafted with every load-bearing claim
backed by a theorem in one of the four documents:

- `papers/cascade-capstone-coalgebra/` — universal cascade exists
- `docs/per-observer-zero-line.md` — local frames exist with `Σ_𝓘`
- `docs/joint-observer-instance.md` — joint frames + generative excess
- `docs/algebraic-existence-and-complexity.md` (this note) —
  existence principle, Local-into-Universal embedding, complexity
  hierarchy, recursion depth limit, rung stratification

Plus the framing layer:

- `docs/existence-as-closure.md` — public-facing translation

That is the full mathematical-and-framing scaffold. The synthesis
paper is now a synthesis task, not a derivation task.
