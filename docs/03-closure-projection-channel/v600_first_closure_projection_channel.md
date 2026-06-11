# From Schläfli Decomposition to Spectral Bridge

*A First Explicit Closure-Projection Channel in V₆₀₀.*

**Lee Smart**
*Institute of Vibrational Field Dynamics*
[contact@vibrationalfielddynamics.org](mailto:contact@vibrationalfielddynamics.org) · [@vfd_org](https://x.com/vfd_org)
May 2026

> **Status:** Synthesis note / programme map. Not peer-reviewed.
>
> This note introduces no new load-bearing mathematical claim. It
> synthesises two previously published reproducible exact-arithmetic
> notes — the Schläfli decomposition of the 600-cell and the 24–600
> spectral bridge — and explains their combined role as a first
> local-to-global spectral channel in the V₆₀₀ programme. Both prior
> notes are self-contained and reproducible from public
> repositories; this note is a reader's map between them.

*(This Markdown rendering tracks the LaTeX note
`v600_first_closure_projection_channel.tex`, which is canonical.)*

## Abstract

The Schläfli decomposition of the 600-cell represents V₆₀₀ as the
binary icosahedral group 2I and partitions it into five right cosets
of the binary tetrahedral subgroup 2T, each carrying intrinsic
24-cell structure. The 24–600 spectral bridge then shows that the
local λ=12 eigenspaces of these five 24-cell sectors zero-extend
exactly into the global λ=12 eigenspace of the 600-cell Laplacian.
This note synthesises those two exact-arithmetic results and
explains their combined role as a first explicit local-to-global
spectral channel in the V₆₀₀ programme. No new physical claim is
made.

## 1. Why this synthesis note exists

Two reproducible exact-arithmetic notes have been published. Read
individually, each is narrow:

- the Schläfli note proves the five-sector finite geometry of the
  600-cell;
- the 24–600 spectral bridge proves a single λ=12 local-to-global
  spectral lift.

Read together, they exhibit a pattern: a local shell structure
inside the 600-cell does not merely sit inside the global geometry —
at a specific spectral value it couples *exactly* to a global
invariant sector. The pattern is short and precise enough to warrant
a brief synthesis.

This note is a map, not a new claim-heavy paper.

## 2. Artifact I: the five 24-cell cosets

The Schläfli note ([github.com/vfd-org/the-24-600-spectral-bridge](https://github.com/vfd-org/the-24-600-spectral-bridge), `docs/01-schlafli-decomposition/`) establishes, by exact ℚ(√5)
arithmetic:

- V₆₀₀ ≅ 2I, 2T ⊂ 2I, [2I : 2T] = 5;
- V₆₀₀ = C₀ ⊔ C₁ ⊔ C₂ ⊔ C₃ ⊔ C₄, with Cᵢ = 2T·gᵢ and |Cᵢ| = 24;
- each coset Cᵢ is an isometric copy of the 24-cell.

Two further structural facts:

- **Two distinct distance shells.** The shortest non-zero squared
  distance in V₆₀₀ is `d²₆₀₀ = (3 − √5)/2 ≈ 0.382` (the 600-cell
  edge); the shortest non-zero squared distance inside each coset
  is the next shell up, `d²₂₄ = 1`. The two graphs share *no* edges.
- **Coset action.** Right multiplication by 2I permutes the five
  cosets; the kernel is exactly {±1} ⊂ 2T and the image is
  A₅ = 2I/{±1} acting transitively on five points.

All three facts are certified by exact rational arithmetic.

## 3. Artifact II: the λ=12 spectral bridge

For each coset Cᵢ let `L_{Cᵢ}` be the local 24-cell shell Laplacian
(the unweighted combinatorial Laplacian of the `d²₂₄ = 1` graph on
Cᵢ), and let `L₆₀₀` be the global 600-cell shell Laplacian (the
unweighted combinatorial Laplacian of the `d²₆₀₀` graph on V₆₀₀).
The bridge note ([docs/02-spectral-bridge/](https://github.com/vfd-org/the-24-600-spectral-bridge/tree/main/docs/02-spectral-bridge)) establishes:

```
liftᵢ(E_{Cᵢ}(12)) ⊂ E₆₀₀(12)   for each i,
```

where liftᵢ: ℝ^Cᵢ → ℝ^V₆₀₀ is zero-extension and `E_X(λ)` is the
λ-eigenspace of `L_X`. Stacking across the five cosets,

```
E_lifted := ⊕ᵢ liftᵢ(E_{Cᵢ}(12)),   dim E_lifted = 10,   dim E₆₀₀(12) = 25.
```

Under the A₅ action (after verifying {±1} acts trivially on
E₆₀₀(12)):

```
E_lifted   ≅ 2·Y₅
E_residual ≅ 3·Y₅
E₆₀₀(12)   ≅ 5·Y₅
```

The bridge is also **selective**: λ=12 is the only eigenvalue of
`L_{Cᵢ}` that admits a full zero-extension. At λ=0 only the global
constant (the symmetric sum of the five coset indicators) survives;
at λ ∈ {4, 8, 10} these are not eigenvalues of `L₆₀₀` at all
(certified exactly), so the question is vacuous.

## 4. Why the bridge is non-trivial

Sections 2 and 3 use **different Laplacians on different graphs**.
The local Laplacian is built from the 24-cell edge graph on 24
vertices at squared distance `d²₂₄ = 1`. The global Laplacian is
built from the 600-cell edge graph on 120 vertices at squared
distance `d²₆₀₀ = (3 − √5)/2`. These are not subgraphs of each
other: no edge of `L_{Cᵢ}` is an edge of `L₆₀₀`, and conversely no
`L₆₀₀`-edge joins two members of the same coset.

For a function v supported on a single coset Cᵢ, the value
`(L₆₀₀ v)(u)` at u ∉ Cᵢ is in general non-zero — it is minus the
sum of v over the global neighbours of u that happen to lie in Cᵢ.
The zero-extension of v is therefore generically *not* a
`L₆₀₀`-eigenvector.

The content of the lift identity is that, on the local λ=12
eigenspace specifically, all such off-coset couplings cancel
**identically**: a finite-rank linear condition that turns out to
be satisfied at λ=12 and nowhere else in the local spectrum.

> **The bridge is not a restriction theorem. It is a cancellation
> theorem.**

Equivalently, the λ=12 lift is a finite-dimensional compatibility
condition between a local shell operator and a global shell
operator built from different distance shells.

## 5. Closure-projection channel: a careful definition

**Definition (Closure-projection channel, working).** A
*closure-projection channel* (in the sense of the present V₆₀₀
programme) is a reproducible local-to-global compatibility relation:
a class of modes defined on a local geometric sector projects,
lifts, or embeds exactly into a global invariant sector of a larger
geometry.

Specialised to the 24–600 case: *the local λ=12 eigenspaces on the
five 24-cell sectors of the 600-cell zero-extend exactly into the
global λ=12 eigenspace of `L₆₀₀`, and that lift is A₅-stable.*

The definition is **interpretive**. The formal mathematical content
is the combination of the two exact results cited in §2 and §3: the
five-coset partition and the λ=12 lift identity with its A₅
decomposition. The phrase *closure-projection channel* adds no new
theorem; it is a name for the pattern.

## 6. What is and is not established

**Established (by the two cited artifacts):**

- V₆₀₀ decomposes into five 24-cell cosets (exact).
- The induced coset action descends to A₅ (exact).
- Local 24-cell shell operators and the global 600-cell shell
  operator are distinct objects on different distance shells (exact).
- The local λ=12 eigenspaces zero-extend into the global λ=12
  sector (exact, ℚ-rational).
- The lifted subspace E_lifted is A₅-stable and decomposes as 2·Y₅
  (exact characters).

**Not established (in this note or in the two cited artifacts):**

- No derivation of particle masses, the Standard Model, or any
  specific physical observable.
- No derivation of quantum mechanics or General Relativity.
- No claim that λ=12 is physically realised, or that the 600-cell
  is a physical structure.
- No claim that all closure projection is explained by this example.
- No proof of the Riemann hypothesis or any number-theoretic
  statement.

The synthesis is mathematical and interpretive only.

## 7. Why this matters for the V₆₀₀ programme

The V₆₀₀ programme requires explicit mechanisms by which local
finite-geometric structures can participate in global invariant
sectors. The Schläfli decomposition supplies local sectors; the
spectral bridge supplies an exact compatibility channel. Together,
they provide a finite test case for the broader idea of *closure
projection*.

The next mathematical step is not to identify this channel with a
physical observable, but to formalise the general selection
principle: *given a local sector, a local operator, a global
operator, and a projection/lift map, when does a local eigenspace
contribute to a global invariant sector?* The λ=12 lift in the
24–600 case is one positive instance and one negative-control
template (at every other local eigenvalue) for that general question.

## 8. Reproducibility and dependency map

This synthesis note introduces no new computation, so it carries no
new formal certificate of its own.

| Artifact | Role | Reproducibility |
|---|---|---|
| Schläfli decomposition (Paper 1) | Five 24-cell cosets and A₅ coset action | exact ℚ(√5) certificate |
| 24–600 spectral bridge (Paper 2) | λ=12 local-to-global lift identity | exact ℚ-rational certificate |
| This synthesis note (Paper 3) | Combined interpretation | no new formal certificate |

All three live in the same repository:
<https://github.com/vfd-org/the-24-600-spectral-bridge>.
Run `pytest closure_transform_engine/tests/` from a clone to
re-assert every certificate-level claim of Papers 1 and 2.

Although named after the spectral-bridge artifact, this repository
now serves as the public V₆₀₀ foundation bundle for all three
notes:

- Paper 1 (Schläfli decomposition): `docs/01-schlafli-decomposition/`
- Paper 2 (spectral bridge): `docs/02-spectral-bridge/`
- Paper 3 (this synthesis): `docs/03-closure-projection-channel/`

---

The next paper in this programme will attempt to formalise the
*closure-projection channel* definition into a general selection
principle, but is out of scope here.
