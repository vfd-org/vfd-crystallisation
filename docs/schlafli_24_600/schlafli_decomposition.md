# The Schläfli Decomposition of the 600-cell

*Five 24-cell Cosets and the Induced A₅ Action.*

**Lee Smart**
*Institute of Vibrational Field Dynamics*
[contact@vibrationalfielddynamics.org](mailto:contact@vibrationalfielddynamics.org) · [@vfd_org](https://x.com/vfd_org)
May 2026

> **Status:** Reproducible mathematical note / exact computational
> certificate. Not peer-reviewed.
>
> **Reproducibility.** The formal claims of this note — construction
> of V₆₀₀ as 2I, identification of the σ-fixed subset as 2T, the
> partition of V₆₀₀ into five right cosets of 2T, verification that
> each coset carries the intrinsic 24-cell distance structure, and
> the induced action of 2I on the five cosets descending through
> {±1} to a transitive A₅ on five points — are all certified by
> exact ℚ(√5) arithmetic in the accompanying repository. No
> floating-point computation enters any formal certificate.
> One-command reproduction is in §8.

*(This Markdown rendering tracks the LaTeX note
`schlafli_decomposition.tex`, which is canonical and includes the
full proofs and bibliography.)*

## Abstract

The 600-cell vertex set is represented exactly as the 120 unit
icosian quaternions, i.e. the binary icosahedral group 2I. The
24-cell vertex set is represented as the 24-element binary
tetrahedral group 2T, characterised as the σ-fixed subset of 2I
under the Galois twist σ: √5 ↦ −√5. We prove that 2T has index 5 in
2I, that its five right cosets partition V₆₀₀ into five disjoint
24-element subsets, that each subset carries the intrinsic 24-cell
distance structure (an 8-regular graph at squared distance 1, 96
edges), and that right multiplication by 2I induces a transitive
action on the five cosets with kernel exactly {±1}, so the image is
A₅ = 2I/{±1} acting on five points. Each claim is certified by
exact ℚ(√5) arithmetic.

## 1. Introduction

The 600-cell is the regular 4-polytope `{3,3,5}` with 120 vertices.
The 24-cell is the regular 4-polytope `{3,4,3}` with 24 vertices.
Classically (Coxeter; Conway–Sloane) the vertex set of the 600-cell
can be identified with the binary icosahedral group 2I, the vertex
set of the 24-cell with the binary tetrahedral group 2T, and 2T sits
inside 2I as a subgroup of index 5. Its cosets therefore give five
copies of the 24-cell whose union is V₆₀₀ — a finite-geometric
decomposition that we make explicit, exact, and reproducible here.

This note supplies the finite-geometric substrate used by the
24–600 spectral bridge note. That later result assumes five disjoint
24-cell coset sectors inside V₆₀₀ and proves that the local λ=12
Laplacian eigenspaces zero-extend exactly into the global λ=12
eigenspace. Here we prove and certify the underlying coset
decomposition independently of any spectral claim.

Because 2T is not normal in 2I, left and right cosets give
different partitions of V₆₀₀; we fix the right-coset convention
2T·g throughout, matching the spectral bridge.

No physical claim is made. Within the broader closure-geometry
programme that motivated this work, the decomposition is one of the
finite geometric structures used downstream; in the present note it
is a self-contained finite-group / finite-geometry result.

## 2. Exact construction of V₆₀₀ as 2I

We work in ℚ(√5), represented as ordered pairs (a, b) ↦ a + b√5 with
a, b ∈ ℚ. Set φ = (1 + √5)/2. Define V₆₀₀ ⊂ ℚ(√5)⁴ as the
120-element set:

- 8 vertices ±eᵢ (i = 0, …, 3);
- 16 vertices (±1, ±1, ±1, ±1)/2;
- 96 vertices: even permutations of (0, ±1/(2φ), ±1/2, ±φ/2).

This vertex set is the standard *icosian model* of the 600-cell
vertex set; under quaternion multiplication it is the binary
icosahedral group 2I in its classical presentation (Coxeter;
Conway–Sloane). Theorem 1 verifies, by exact arithmetic, that the
explicit 120-element model above does satisfy the group axioms on
this set; the identification with the abstract 2I is the classical
reference, not a consequence of the certificate alone.

**Theorem 1 (Exact group structure of the icosian model).** The 120
vectors above are pairwise distinct; each has squared ℚ(√5)-norm
exactly 1; the set contains the identity quaternion (1, 0, 0, 0); it
is closed under quaternion multiplication; the conjugate of every
element (= its inverse, since norms are 1) is again in V₆₀₀. Hence
V₆₀₀, equipped with quaternion multiplication, is a finite group of
order 120. By Coxeter / Conway–Sloane this is the standard icosian
model of 2I.

*Proof.* `certify_v600_construction` in
`closure_transform_engine.decomposition` runs the four exact checks:
distinctness on ℚ(√5) keys, unit norm componentwise, 120² = 14 400
products `u·v` lying in the key set, and 120 conjugates inverse-check.
No floating-point. ∎

## 3. The σ-fixed 24-cell as 2T

Let σ: ℚ(√5) → ℚ(√5) be the Galois twist √5 ↦ −√5, extended
componentwise to ℚ(√5)⁴. Define V₂₄ := {v ∈ V₆₀₀ : σ(v) = v}. This
fixed subset consists exactly of the 8 unit vectors ±eᵢ and the 16
half-integer vectors (±1, ±1, ±1, ±1)/2 — the vectors with no √5
component.

**Theorem 2 (Exact subgroup structure of the σ-fixed set).** |V₂₄| =
24. The set V₂₄ ⊂ V₆₀₀ is closed under quaternion multiplication,
contains the identity, and contains the inverse of each of its
elements. Hence V₂₄ is a subgroup of V₆₀₀ of order 24, and the index
of V₂₄ in V₆₀₀ is |V₆₀₀| / |V₂₄| = 120 / 24 = 5. The 24-element
set — the eight units ±eᵢ together with the sixteen half-integer
vectors (±1, ±1, ±1, ±1)/2 — is the standard Hurwitz-unit model of
the binary tetrahedral group 2T (Coxeter; Conway–Sloane); the
certificate verifies that this explicit model satisfies the
subgroup axioms inside V₆₀₀.

*Proof.* `certify_v24_subgroup` computes the fixed set, verifies its
size is 24, runs 24² = 576 products `u·v` for u, v ∈ V₂₄ and checks
each lies in V₂₄, verifies that the identity is fixed, and verifies
that the conjugate of every fixed element is fixed. ∎

## 4. The five right cosets

**Convention.** We work with right cosets 2T·g of 2T in 2I.
Equivalently, for v ∈ V₆₀₀ the orbit 2T·v = {h·v : h ∈ 2T} is the
right coset containing v. 2T is not normal in 2I; left and right
cosets give different partitions of 2I, related by the inversion map
g ↦ g⁻¹ which exchanges the two families and fixes the identity
coset 2T. We use right cosets to match the 24–600 spectral bridge.

**Cosets.** Label them C₀, C₁, C₂, C₃, C₄ with C₀ = V₂₄ itself. The
remaining four cosets C₁..C₄ are the four V₂₄-orbits on the 96
σ-mobile vertices.

**Theorem 3 (Schläfli decomposition).** The five right cosets of 2T
in 2I partition V₆₀₀:

```
V₆₀₀ = C₀ ⊔ C₁ ⊔ C₂ ⊔ C₃ ⊔ C₄,   |Cᵢ| = 24 for each i,
```

C₀ = 2T, and C₁ ∪ C₂ ∪ C₃ ∪ C₄ is exactly the set of 96 σ-mobile
vertices. In particular, every vertex of V₆₀₀ belongs to exactly one
coset.

*Proof.* `right_cosets` + `certify_right_cosets` compute the five
orbits, verify there are exactly 5 of size 24, pairwise disjoint,
union equals V₆₀₀, C₀ = V₂₄, and C₁ ∪ … ∪ C₄ equals the σ-mobile
complement. Each check is an exact set operation on vertex
indices. ∎

## 5. Each coset carries the 24-cell structure

For pairs u, v ∈ V₆₀₀ define the squared ℚ(√5)-distance
d²(u, v) = |u − v|² ∈ ℚ(√5). There are 8 distinct non-zero values of
d² on V₆₀₀. The shortest is

```
d²(V₆₀₀) = (3 − √5)/2 ≈ 0.382,
```

which defines the 600-cell edge graph (12-regular, 720 edges).
Inside each coset Cᵢ the shortest non-zero d² between members is the
next shell up: d²(24) = 1.

**Theorem 4 (Each coset is a 24-cell).** For each i, Cᵢ = 2T·gᵢ is
isometric to 2T as a metric subspace of S³. In particular, the
shortest non-zero squared distance between members of Cᵢ is exactly
1, and the graph on Cᵢ whose edges are the pairs at d² = 1 is the
standard 24-cell edge graph (24 vertices, 96 edges, 8-regular).
Furthermore, no pair of vertices within a single coset is joined by
a V₆₀₀-edge: every count of intra-coset pairs at separation
(3 − √5)/2 is zero.

*Proof.* For any unit quaternion g ∈ 2I, right multiplication
v ↦ v·g is a Euclidean isometry of ℝ⁴ restricted to S³, since
|v₁g − v₂g| = |(v₁ − v₂)g| = |v₁ − v₂| (because |g| = 1). Hence
the map 2T → 2T·gᵢ, h ↦ h·gᵢ, is an isometric bijection; the
intrinsic metric on Cᵢ = 2T·gᵢ is the metric on 2T pulled across.
Since the standard Hurwitz-unit model of 2T has shortest non-zero
squared distance 1 and its d²=1 graph is the 24-cell edge graph
(Coxeter; Conway–Sloane), each coset Cᵢ inherits exactly that
structure. The repository (`certify_each_coset_is_24cell`) also
verifies, as a numerical check on the explicit coordinates, that
the minimum non-zero d² is exactly 1, the directed d²=1 pair count
is 192 (96 undirected edges), every vertex has exactly 8 such
neighbours inside the coset, and the count of intra-coset pairs at
the V₆₀₀-shell distance (3 − √5)/2 is 0. ∎

**Remark.** Theorem 4 says each coset is an isometric copy of the
24-cell, but the 24-cell edges live at the *next* V₆₀₀-distance
shell, not at the shortest one. Equivalently, the five 24-cells are
*not* induced subgraphs of the 600-cell edge graph: every 600-cell
edge runs between two different cosets, and every intra-coset
24-cell edge runs at a strictly longer distance than a 600-cell
edge. This separation is the structural feature that the 24–600
spectral bridge then exploits to compare local and global
Laplacians.

## 6. Induced action on the five cosets

Right multiplication by g ∈ 2I permutes the right cosets:
(2T·v)·g = 2T·(vg). This well-defined map 2I → Sym{C₀, …, C₄} is the
focus of this section.

**Theorem 5 (A₅ coset action).** The induced map
2I → Sym{C₀, …, C₄}:

1. is transitive on the five cosets;
2. has image of size 60 (exactly 60 distinct coset-level
   permutations arise from the 120 elements of 2I);
3. has kernel exactly {+1, −1}, the centre of 2I;
4. lands entirely in the alternating group: every element of the
   image is an even permutation;
5. has image equal to A₅ ⊂ S₅, with conjugacy-class sizes
   (1, 15, 20, 12, 12) matching the standard A₅ character table.

Equivalently, the coset action factors through the surjection
2I ↠ 2I/{±1} = I ≅ A₅.

*Proof.* `certify_a5_coset_action` enumerates all 120 vertex
permutations P_h, reads off the induced coset permutation π(h) ∈ S₅,
and computes: (i) |{π(h) : h ∈ 2I}| = 60 exactly; (ii) the kernel
contains exactly the identity and its negative; (iii) every element
of the image is even; (iv) conjugacy-class sizes match (1, 15, 20,
12, 12). Transitivity follows from the orbit of C₀, which covers
all five cosets. All 60 image permutations are verified even, so
the image lies inside A₅ ⊂ S₅; since |A₅| = 60 and the image has 60
elements, the image equals all of A₅. ∎

## 7. Relationship to the 24–600 spectral bridge

This note proves the finite-geometric decomposition used by the
24–600 spectral bridge. The spectral bridge then asks a further
question: whether local eigenspaces of the 24-cell shell Laplacians
zero-extend into eigenspaces of the global 600-cell Laplacian. That
later note proves the λ=12 local eigenspaces do exactly this, and
no other local eigenvalue admits a non-trivial lift. That spectral
result is independent and is not reproved here; the two artifacts
can be read in either order, but the finite-geometric decomposition
certified in this note is logically prior.

Spectral bridge repository:
<https://github.com/vfd-org/the-24-600-spectral-bridge>

## 8. Reproducibility

**One-command reproduction** (from the repository root):

```bash
python closure_transform_engine/examples/run_wo007_schlafli_decomposition.py
pytest  closure_transform_engine/tests/test_wo007_schlafli_decomposition.py
```

The first command (under a minute) builds V₆₀₀ from exact ℚ(√5)
icosian quaternions, runs every certificate, and writes the frozen
output artifacts; the second re-asserts the certificate-level claims
as a test.

**Environment.** Pinned in `requirements.txt` / `pyproject.toml`:
Python ≥ 3.8 (developed on 3.8.10), NumPy ≥ 1.20 (1.24.4), SymPy ≥
1.12 (1.13.3). All formal certificates use exact arithmetic via
`vfd_v600` (ℚ(√5)-rational pairs) and integer set operations on
vertex indices; NumPy and SymPy enter only auxiliary computations
and never a formal claim. The reproducibility log records UTC
timestamp, elapsed time, Python and dependency versions, platform,
commit hash, and per-certificate pass/fail states.

**Dependency chain.** The claims of this note do not require any
external repository. A reader can verify every theorem by running
the two commands above. The vendored `vfd_v600` package supplies
exact ℚ(√5) icosian arithmetic; it is the only dependency beyond
the standard scientific Python stack.

**What the runner verifies:**

- Theorem 1 — V₆₀₀ = 2I: 120 distinct unit-norm vertices, closure
  under multiplication, identity and inverses present.
- Theorem 2 — V₂₄ = 2T: 24 σ-fixed vertices, subgroup property,
  index 5 in 2I.
- Theorem 3 — Schläfli decomposition: 5 right cosets, sizes 24,
  disjoint, cover V₆₀₀, C₀ = 2T.
- Theorem 4 — each coset is a 24-cell: shortest intra-coset d² = 1,
  8-regular, 96 edges, no intra-coset V₆₀₀-edge.
- Theorem 5 — A₅ coset action: 60 distinct perms, kernel = {±1},
  image even with classes (1, 15, 20, 12, 12), hence A₅.

**Outputs** (under the docs outputs directory):

- `wo007_summary.json` — full structured certificate result.
- `wo007_cosets.json` — the 5 coset vertex-index lists.
- `wo007_coset_action_table.csv` — for each h ∈ 2I, the induced
  coset permutation, cycle structure, identity flag, parity.
- `wo007_distance_shells.csv` — the 8 non-zero V₆₀₀ distance shells
  and pair counts.
- `wo007_reproducibility_log.txt` — run UTC timestamp, environment,
  commit hash, and per-certificate pass/fail states.

---

### Summary

We publish a reproducible exact-arithmetic certificate that the
600-cell vertex set, represented as the binary icosahedral group 2I,
decomposes into five right cosets of the binary tetrahedral subgroup
2T. Each coset carries the intrinsic 24-cell distance structure, and
the induced action on the five cosets factors through A₅ = 2I/{±1}.
This supplies the finite-geometric foundation for the later 24–600
spectral bridge.
