# The 24--600 Spectral Bridge

*A selective λ=12 eigenspace embedding from five 24-cell cosets into
the 600-cell.*

**Lee Smart**
*Institute of Vibrational Field Dynamics*
[contact@vibrationalfielddynamics.org](mailto:contact@vibrationalfielddynamics.org) · [@vfd_org](https://x.com/vfd_org)
May 2026

> **Status:** Reproducible mathematical note / exact computational
> certificate. Not peer-reviewed.
>
> **Reproducibility.** The formal claims of this note — the λ=12 lift
> identity (Theorem 1), the dim E₆₀₀(λ) entries for
> λ ∈ {0, 4, 8, 10, 12} used in the selectivity table (§4), the
> {±1}-triviality lemma (Lemma 3), the 2I-invariance of E_lift and
> E_residual (Lemma 3.5), the integer A₅ class characters (Theorem 4),
> and the A₅ irrep multiplicities (Corollary 5) — are all certified by
> exact rational arithmetic in the accompanying repository (integer
> Laplacians, ℚ-rational nullspace bases, exact zero residuals; A₅
> character projection uses exact ℚ(√5) character-table entries). The
> numerical quantities (floating-point lift residuals, max-residual
> column of the selectivity table) are cross-checks only.
> One-command reproduction is in §8.

*(This Markdown rendering tracks the LaTeX note `spectral_bridge_note.tex`,
which is canonical and includes the full proofs and bibliography.)*

## Abstract

The 600-cell is the regular 4-polytope whose 120 vertices form the
binary icosahedral group 2I. The binary tetrahedral group 2T ⊂ 2I has
index 5; its right cosets partition the 600-cell into five disjoint
copies of the 24-cell. Each coset carries a d=1 (nearest-neighbour)
graph isomorphic to the 24-cell edge graph (8-regular); on the full
vertex set the d=1 graph is the 600-cell edge graph (12-regular).

We prove that the 2-dimensional λ=12 eigenspace of each local 24-cell
Laplacian zero-extends into the 25-dimensional λ=12 eigenspace of the
full 600-cell Laplacian. The identity is established **exactly over ℚ**:
from the local ℚ-rational nullspace of each `L_C − 12I` (an integer
matrix), every zero-extended basis vector is verified to lie in the
kernel of `L₆₀₀ − 12I` by exact rational matrix multiplication. A
floating-point cross-check independently gives residual
‖L₆₀₀ v − 12 v‖ ≤ 6.2 × 10⁻¹⁵.

Among the five local 24-cell Laplacian eigenvalues {0, 4, 8, 10, 12},
λ=12 is the only one that gives a full zero-extension into a
corresponding global 600-cell eigenspace. The λ=0 case contributes
exactly one direction (the global constant, reconstructed from the
symmetric sum of the five coset indicators) of the 5-dimensional lift
image; the local eigenvalues λ ∈ {4, 8, 10} are not eigenvalues of
the 600-cell Laplacian at all, so the question is vacuous there.

Under the induced A₅ = 2I/{±1} action on the five cosets,
E₆₀₀(12) = E_lifted ⊕ E_residual with E_lifted ≅ 2·Y₅,
E_residual ≅ 3·Y₅, E₆₀₀(12) ≅ 5·Y₅, where Y₅ is the 5-dimensional
irreducible representation of A₅. The A₅ class characters are exact
integers, computed in ℚ.

## 1. Introduction

The 600-cell is the regular 4-polytope `{3,3,5}` with 120 vertices,
720 edges and icosahedral symmetry. Its vertex set is naturally
identified with the binary icosahedral group 2I ⊂ Sp(1). The 24-cell
is the regular 4-polytope `{3,4,3}` with 24 vertices, 96 edges and
F₄-symmetry; its vertex set is the binary tetrahedral group 2T.

It is classical that 2T has index 5 in 2I and that the five cosets of
2T in 2I form five inscribed 24-cells whose vertex sets partition the
600-cell (Coxeter; Conway–Sloane). A machine-verified treatment within
the present programme is in `papers/paper-xxxv/` of the VFD research
repository (Schläfli decomposition; A₅ origin of the coset action),
using the left-coset convention; this note uses the right-coset
convention, equivalent via the involution g ↦ g⁻¹.

The question this note answers is sharper: *does the spectral structure
of each local 24-cell graph embed exactly into the spectral structure
of the global 600-cell graph?* The answer is "yes, but only at λ=12 in
full". Full zero-extension to a global λ-eigenspace occurs only at
λ=12; at λ=0 exactly one symmetric combination (the sum of the five
coset indicators, equal to the global constant) lands in the global
eigenspace, while at every other tested λ the lift image intersects
the global eigenspace only at 0.

### Why the comparison is non-trivial

The local 24-cell Laplacian `L_C` and the global 600-cell Laplacian
`L₆₀₀` are built from *different* graphs: `L_C` uses the 24-cell edge
graph on the 24 vertices of a single coset (edges at squared distance
1), while `L₆₀₀` uses the 600-cell edge graph on all 120 vertices
(edges at squared distance (3−√5)/2 < 1). These graphs are not
subgraphs of one another; in fact *no* edge of `L_C` is an edge of
`L₆₀₀` (the local 24-cell edge length is the next distance shell up of
V₆₀₀). Consequently, for a function v supported on a coset C, the value
(L₆₀₀ v)(u) at a vertex u ∉ C is in general non-zero — it is minus the
sum of v over the global neighbours of u that happen to lie in C — so
the zero-extension of v is generically *not* a `L₆₀₀`-eigenvector. The
content of the lift theorem is that this off-coset coupling cancels
*identically* on the local λ=12 eigenspace — a finite-rank linear
condition that turns out to be satisfied — and the content of the
selectivity table is that no other local eigenspace satisfies it. That
is what makes λ=12 a genuine local-to-global bridge rather than a
trivial restriction-and-extension.

## 2. Construction

### 2.1 V₆₀₀ as 2I

Working in exact ℚ(√5) arithmetic, the 120 vertices of V₆₀₀ are:
8 vertices ±eᵢ (i = 0..3); 16 vertices (±1, ±1, ±1, ±1)/2; and 96
vertices: even permutations of (0, ±1/(2φ), ±1/2, ±φ/2), φ = (1+√5)/2.
These unit icosian quaternions form 2I under quaternion multiplication
(construction in package `vfd_v600`). Closure of the vertex set under
multiplication is exercised end-to-end by the A₅ certificate of §5
(which enumerates every h ∈ 2I and looks up vh ∈ 2I for every v ∈ 2I);
any non-closure would manifest as a missing index lookup and abort
the certificate.

### 2.2 V₂₄ as 2T = σ-fixed subset

The Galois twist σ: √5 ↦ −√5 acts component-wise on ℚ(√5). Its fixed
subset in V₆₀₀ is the 24-element binary tetrahedral group V₂₄ = 2T:
the 8 unit vectors ±eᵢ and the 16 half-integer vectors
(implemented in `vfd_v600.sigma`).

### 2.3 Right cosets of 2T in 2I and the A₅ action

**Convention.** We work with the *right cosets* 2T·v in 2I —
equivalently, the orbits of left multiplication by 2T on 2I. Left and
right cosets give different partitions of 2I (2T is not normal), but
both partition the 120-vertex set into five sets of 24, both contain
2T itself as the identity coset, and both produce isomorphic 24-cell
edge graphs on each block by isometry. The two conventions are related
by g ↦ g⁻¹, which is a bijection between left and right cosets fixing
the identity coset 2T.

**Cosets.** The five right cosets are: C₀ = 2T itself (the σ-fixed
orbit); C₁..C₄ = the four 2T-orbits on the 96 σ-mobile vertices. Each
|Cᵢ| = 24, and ⊔ Cᵢ = V₆₀₀.

**Action on cosets.** 2I acts on the five right cosets by right
multiplication: (2T·v)·g = 2T·(vg). The kernel of this *coset-level*
action contains {±1} because −1 ∈ 2T (so 2T·v·(−1) = 2T·(−v) = 2T·v).
By the parallel left-coset result in `papers/paper-xxxv/`, the kernel
is exactly {±1} and the image on five letters is exactly
A₅ = 2I/{±1}, acting transitively.

**Vertex action vs. coset action.** Right multiplication on *vertices*
of V₆₀₀ has trivial kernel. When we say "A₅ action" on a subspace
E ⊂ ℝ^V₆₀₀ below, we mean the action induced on E by right
multiplication of vertices, restricted to subspaces on which −1 acts
trivially (so the linear action descends through {±1} to A₅). Whether
−1 acts trivially on a given E is a fact specific to E; we prove it for
E = E₆₀₀(12) in §5 (Lemma 3).

| Object | \|V\| | \|E\| | Graph = shortest non-zero distance shell |
|---|---:|---:|---|
| V₆₀₀ | 120 | 720 | shortest-V₆₀₀ shell, squared distance (3−√5)/2, 12-regular |
| 2T-coset (any) | 24 | 96 | shortest intra-coset shell, squared distance 1, 8-regular |

The two distance shells are distinct: *no* pair within a single coset
has separation (3−√5)/2, and conversely no V₆₀₀-edge joins two
vertices of the same coset. Throughout this note, "d=1 graph" is
shorthand for "shell-1 (nearest-neighbour) graph at the shortest
non-zero distance of whichever vertex set we are working on"; the
squared distances are different for V₆₀₀ and a coset, as the table
makes explicit.

### 2.4 The two d=1 shells

There are 8 distinct non-zero squared distances between pairs in V₆₀₀.
The shortest is d²(V₆₀₀) = (3−√5)/2 ≈ 0.382, which defines the 600-cell
edge graph (12-regular, 720 edges). Inside each right coset Cᵢ the
shortest non-zero squared distance between members is the next shell
up: d²(C) = 1, which on Cᵢ realises the standard 24-cell edge graph
(8-regular, 96 edges). The two distances are distinct: *no* pair within
a single coset has separation d²(V₆₀₀).

### 2.5 Laplacians

We use the unweighted combinatorial Laplacian L = D − A. Both graphs
are regular with integer 0/1 adjacency and integer regular degree, so
the Laplacians are integer matrices. Numerical diagonalisation (with
the local spectrum cross-checked against `papers/paper-v/`, and every
integer-eigenvalue multiplicity additionally certified by exact
ℚ-rational sympy nullspace, via
`closure_transform_engine.keystone.exact_integer_spectrum_check`):

```
spec L_C   = {0¹, 4⁴, 8⁹, 10⁸, 12²}
spec L₆₀₀  = {0¹, (≈2.29)⁴, (≈5.53)⁹, 9¹⁶, 12²⁵, 14³⁶, (≈14.47)⁹, 15¹⁶, (≈15.71)⁴}
```

in multiset notation λ^m; the four non-integer eigenvalues take values
in ℚ(√5). In particular dim E₆₀₀(12) = 25, an exact rational-arithmetic
spectral fact, is used below.

## 3. The λ=12 lift identity

For a coset Cᵢ, define the zero-extension map
`liftᵢ: ℝ²⁴ → ℝ¹²⁰`, `(liftᵢ u)(v) = u(v)` if `v ∈ Cᵢ`, else 0.

**Theorem 1 (λ=12 lift identity).** For every coset Cᵢ,
`liftᵢ(E_{Cᵢ}(12)) ⊂ E₆₀₀(12)`.

*Proof by exact rational certificate.* `L_C − 12I` and `L₆₀₀ − 12I`
are integer matrices, and 12 is an integer eigenvalue, so `E_{Cᵢ}(12)
= ker(L_C − 12I)` is a ℚ-rational subspace. The repository produces a
checkable certificate consisting of: (i) the integer matrices; (ii) a
ℚ-rational basis {v₁, v₂} of each `E_{Cᵢ}(12)`, by exact Gaussian
elimination over ℚ; (iii) for each vₖ, the vector
`(L₆₀₀ − 12I)·liftᵢ(vₖ) ∈ ℚ¹²⁰`, computed by exact rational matrix
multiplication, with every one of its 120 coordinates equal to 0.
Item (iii) certifies `L₆₀₀·liftᵢ(vₖ) = 12·liftᵢ(vₖ)` in ℚ¹²⁰, for
both k=1,2 and all five cosets; no floating-point arithmetic enters.
Regenerated and re-checked by
`closure_transform_engine.keystone.exact_certify_lambda12_lift`. ∎

**Remark (floating-point cross-check).** Independent FP diagonalisation
of `L₆₀₀` and each `L_C` via `numpy.linalg.eigh`, zero-extension of
each E_{Cᵢ}(12) basis vector v, and evaluation of
‖L₆₀₀ v_lifted − 12 v_lifted‖ gives maximum residual ≤ 6.2 × 10⁻¹⁵
across all 10 lifted vectors — consistent with Theorem 1 at numerical
precision.

**Corollary 2.** Setting E_lifted := ⊕ᵢ liftᵢ(E_{Cᵢ}(12)), the five
lifted local eigenspaces have disjoint supports, so dim E_lifted = 10.
Since dim E₆₀₀(12) = 25, E_lifted ⊂ E₆₀₀(12) is proper.

## 4. Selectivity

For other eigenvalues λ of `L_C` the natural measure is the
*intersection dimension* s(λ) := dim( Im(lift)|_λ ∩ E₆₀₀(λ) ), where
Im(lift)|_λ = Σᵢ liftᵢ(E_{Cᵢ}(λ)) ⊂ ℝ¹²⁰. A "full" lift has s(λ) equal
to the total lift-image dimension; a generic eigenvalue has s(λ) = 0.

| local λ | lift-image dim | dim E₆₀₀(λ) | s(λ) | verdict |
|---:|---:|---:|---:|---|
| 0 | 5 | 1 | 1 | PARTIAL — only the global constant |
| 4 | 20 | 0 | 0 | E₆₀₀(λ) = {0} |
| 8 | 45 | 0 | 0 | E₆₀₀(λ) = {0} |
| 10 | 40 | 0 | 0 | E₆₀₀(λ) = {0} |
| **12** | **10** | **25** | **10** | **FULL** |

The PARTIAL row at λ=0 is the substantive control: E₆₀₀(0) is
1-dimensional (the global constant), and one might ask whether the lift
hits it. It does — but only through the symmetric combination:
**1**_{V₆₀₀} is the sum of the five coset indicators, each a local λ=0
eigenvector, so exactly one direction of the 5-dim lift image lands in
E₆₀₀(0). No single-coset λ=0 lift lies in E₆₀₀(0); only the
A₅-invariant combination does.

For λ ∈ {4, 8, 10} the control is weaker: these are simply not
eigenvalues of `L₆₀₀` at all, so E₆₀₀(λ) = {0} and s(λ) = 0 holds for
trivial dimensional reasons. We list these rows for completeness — and
the floating-point lift residuals at these λ (3.16 to 9.38, far above
machine precision) confirm the lifted vectors are nowhere near an
approximate λ-eigenfunction of `L₆₀₀` — but we do not claim they
constitute a strong falsification test in the way the λ=0 row does.

Hence among the five eigenvalues of `L_C`, only λ=12 satisfies the
lift identity in full; at λ=0 the lift is partial in the single
symmetry-forced way; and at the remaining λ the question is empty for
spectral reasons.

## 5. Direct-sum decomposition and A₅ structure

Inside E₆₀₀(12), the lifted subspace E_lifted (dim 10) has orthogonal
complement E_residual := E₆₀₀(12) ⊖ E_lifted, dim 15. E_residual
consists of the global λ=12 eigenvectors orthogonal to every
zero-extension of a local λ=12 eigenfunction.

### 5.1 Descent of right multiplication to A₅ on E₆₀₀(12)

For h ∈ 2I let P_h be the 120-permutation matrix from right
multiplication v ↦ vh. Right multiplication is an isometry of V₆₀₀, so
P_h commutes with `L₆₀₀` and restricts to a linear action on E₆₀₀(12).

**Lemma 3 ({±1} acts trivially on E₆₀₀(12)).** P₋₁ restricted to
E₆₀₀(12) is the identity.

*Proof by exact rational computation.* Compute the ℚ-rational nullspace
B_global ∈ ℚ^{120×25} of `L₆₀₀ − 12I` (an integer matrix). For each
column v, apply the integer permutation matrix P₋₁ exactly and verify
P₋₁ v − v = 0 ∈ ℚ¹²⁰ componentwise (no floating point). Every one of
the 25·120 = 3000 rational component checks returns 0. Hence
P₋₁ = Id on E₆₀₀(12). Reproduced by
`closure_transform_engine.keystone.exact_a5_characters`. ∎

By Lemma 3 the action of 2I on E₆₀₀(12) factors through A₅ = 2I/{±1}.
To restrict to E_lifted and E_residual we need 2I-invariance:

**Lemma 3.5 (E_lifted and E_residual are 2I-invariant).** For every
h ∈ 2I, P_h E_lifted = E_lifted and P_h E_residual = E_residual.

*Proof.* Right multiplication by h permutes the right cosets:
P_h sends Cᵢ bijectively to C_{σ_h(i)}, an isometry between two
metric copies of the 24-cell. It intertwines the local shell-1
Laplacians (L_{C_{σ_h(i)}}(P_h v) = P_h (L_{Cᵢ} v)), so P_h maps
E_{Cᵢ}(12) to E_{C_{σ_h(i)}}(12). By linearity of zero-extension,
P_h sends liftᵢ(E_{Cᵢ}(12)) to lift_{σ_h(i)}(E_{C_{σ_h(i)}}(12));
summing over i gives P_h E_lifted ⊆ E_lifted, and invertibility of
P_h gives equality. E_residual = E₆₀₀(12) ⊖ E_lifted, and P_h is
orthogonal (a permutation), so P_h preserves E_residual too.

Independent of this prose proof, the repository carries an exact
ℚ-rational certificate: for every h ∈ 2I and B ∈ {B_lifted,
B_residual}, sympy computes P_h B − B(BᵀB)⁻¹Bᵀ(P_h B) over ℚ and
verifies every component is exactly 0, certifying
P_h col(B) ⊆ col(B). Reproduced by the `lifted_2I_invariant` and
`residual_2I_invariant` fields of `exact_a5_characters`. ∎

By Lemmas 3–3.5 the A₅ action on E₆₀₀(12) restricts to each
summand.

### 5.2 Exact A₅ class characters

Using ℚ-rational bases of E_lifted, E_residual, E₆₀₀(12) (sympy
nullspace), we compute the trace of P_h on each subspace by exact
rational matrix multiplication for every h ∈ 2I, and average by A₅
conjugacy class. The five classes 1A, 2A, 3A, 5A, 5B are obtained by
explicit orbit enumeration: enumerate the 60 distinct 5-letter
permutations in the coset-action image, then partition into orbits
under conjugation. The cycle structures (1,1,1,1,1), (1,2,2), (1,1,3)
each give one class (sizes 1, 15, 20); the cycle structure (5) splits
into two A₅ orbits of size 12 each (5A and 5B). Sizes (1, 15, 20, 12,
12) match the standard A₅ character table.

**Theorem 4 (exact A₅ class characters).** The A₅ class characters of
E₆₀₀(12), E_lifted, E_residual are constant on each conjugacy class and
take exact integer values:

| subspace | 1A | 2A | 3A | 5A | 5B |
|---|---:|---:|---:|---:|---:|
| E₆₀₀(12) | 25 | 5 | −5 | 0 | 0 |
| E_lifted | 10 | 2 | −2 | 0 | 0 |
| E_residual | 15 | 3 | −3 | 0 | 0 |

Each entry is computed in ℚ (no floating point).

**Corollary 5 (A₅ irrep decomposition).** Projecting the exact
characters against the A₅ character table (one trivial, two 3-dim, one
4-dim, one 5-dim irrep, with Y₅ the 5-dim irrep):

```
E_lifted   ≅ 2·Y₅
E_residual ≅ 3·Y₅
E₆₀₀(12)   ≅ 5·Y₅
```

with all other irrep multiplicities exactly zero over ℚ.

The "15 = 3×5" is representation-theoretic — three copies of the 5-dim
A₅ irrep — *not* five cosets each contributing three local modes.

## 6. Interpretation and limits

This is a reproducible spectral-graph result in the 24-cell/600-cell
coset geometry. It does not by itself derive particle physics,
quantum mechanics, or cosmology.

Within the broader closure-geometry programme that motivated this
work, the result may be interpreted as one example of a
"closure-projection channel": a local shell structure lifting exactly
into a global invariant sector. That interpretation is provided here
only for context and is not load-bearing for any claim in this note.

## 7. What this does and does not claim

It claims: a reproducible, selective λ=12 spectral channel between the
five 24-cell cosets of the 600-cell and the global 25-dim λ=12 sector;
an exact direct-sum split 10 + 15 = 25; an A₅-equivariant decomposition
2·Y₅ + 3·Y₅ = 5·Y₅ with exact integer characters.

It does **not** claim to derive the Standard Model, particle masses,
cosmology, black holes, the Riemann hypothesis, or consciousness, and
it does not subsume or replace any other framework.

## 8. Reproducibility

**One-command reproduction** (from the repository root):

```bash
python closure_transform_engine/examples/run_wo008_keystone.py
pytest  closure_transform_engine/tests/test_wo008_keystone_artifact.py
```

The first command (a few minutes) builds the 600-cell from exact
ℚ(√5) icosian quaternions, runs all certificates, and writes the
frozen output artifacts; the second re-asserts every claim of this note
as a test.

**Environment.** Pinned in `requirements.txt` / `pyproject.toml`:
Python ≥ 3.8 (developed on 3.8.10), NumPy ≥ 1.20 (1.24.4), SymPy ≥ 1.12
(1.13.3), SciPy ≥ 1.7 (1.10.1). Formal certificates use only exact ℚ
arithmetic (SymPy `Rational`/`Matrix`); NumPy enters only the
floating-point cross-check.

**Dependency chain.** *The claims of this note do not require
rerunning Paper V or Paper XXXV.* Those upstream references justify
the broader programme context and provide an independent treatment of
the coset construction; the standalone bundle reconstructs from
scratch the objects needed for the certificates used here, so a
reader can verify every theorem of this note without access to the
main research repository.

**What the runner verifies:** Theorem 1 (ℚ-rational lift certificate);
the floating-point cross-check (max residual ≤ 10⁻¹⁰; observed ≈
6.2 × 10⁻¹⁵); every integer-eigenvalue multiplicity of `L_C` and
`L₆₀₀`; the intersection-dimension table of §4; Lemma 3 (−1 acts
trivially on E₆₀₀(12)); Theorem 4 (exact integer A₅ class characters)
and Corollary 5 (A₅ irrep multiplicities).

**Outputs** (under the docs outputs directory):
`wo008_summary.json`, `wo008_verdict_table.csv`,
`wo008_reproducibility_log.txt`.

---

### Summary

We isolated one concrete result from the broader closure-geometry
programme: a selective λ=12 spectral bridge between five 24-cell cosets
and the 600-cell. It is reproducible by one command, certified by exact
rational arithmetic, hostile to misclassification by the λ=0 control,
and structurally clean under the A₅ action that the geometry forces.
