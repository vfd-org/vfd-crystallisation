# The 24--600 Spectral Bridge

*A reproducible λ=12 eigenspace channel between five 24-cell cosets and
the 600-cell.*

> **Status:** Reproducible mathematical note / exact computational
> certificate. Not peer-reviewed. All formal claims are certified over
> the rationals (ℚ); floating-point computation is an independent
> cross-check only. A self-contained public bundle of this artifact is
> at `release-bundles/the-24-600-spectral-bridge/`.

---

## What is this?

A reproducible geometry result involving the 600-cell, five 24-cell
cosets, and a selective λ=12 spectral channel.

Concretely:

> The 600-cell partitions into five 24-cell right cosets of
> 2T ≤ 2I.  On each coset, the local nearest-neighbour ("d=1") graph
> is the 24-cell edge graph (8-regular).  The 2-dimensional λ=12
> eigenspace of each local Laplacian lifts by zero-extension into the
> 25-dimensional λ=12 eigenspace of the full 600-cell Laplacian.
>
> The identity holds **exactly over ℚ** (verified by exact ℚ-rational
> sympy nullspace computation; independently cross-checked
> numerically with residual ‖L₆₀₀ v − 12 v‖ ≤ 6.2 × 10⁻¹⁵).
>
> The lift is **selective** for λ=12.  At λ ∈ {4, 8, 10} the
> intersection of the lift image with the global λ-eigenspace is
> empty.  At λ = 0 only the symmetric combination of the five coset
> indicators (= the global constant) survives — a 1-dimensional
> intersection inside a 5-dimensional lift image.

The five local lifts span a 10-dimensional subspace E_lifted; its
orthogonal complement inside the full 25-dimensional λ=12 sector is a
15-dimensional inter-coset operator subspace E_residual.  Under the
induced action of A₅ = 2I/{±1} on the five cosets,

```text
E_lifted   ≅ 2·Y₅
E_residual ≅ 3·Y₅
E600(12)   ≅ 5·Y₅
```

where Y₅ is the 5-dimensional irreducible representation of A₅.

## Why does it matter?

It shows a non-obvious local/global relation in closed geometry:

```text
local 24-cell shell modes  →  global 600-cell spectral modes
```

The lift is exact, fully numerically reproducible, and selective: it
holds at λ=12 and fails at every other Laplacian eigenvalue of the
local 24-cell graph.

This is a demonstration of closure / invariant machinery on a fixed
finite vertex set.  It is **not** a claim about particle physics,
cosmology, or consciousness.

## How do I run it?

From the repository root:

```bash
python closure_transform_engine/examples/run_wo008_keystone.py
```

The runner constructs the 600-cell from exact icosian quaternions (no
floating-point in the vertex set), builds the d=1 graphs, diagonalises
the Laplacians, performs the zero-extension lift, and decomposes
E_lifted / E_residual under A₅.

To re-run the unit tests:

```bash
pytest closure_transform_engine/tests/test_wo008_keystone_artifact.py
```

## What should I see?

Expected console summary:

```text
λ=12 lift residual: ~6.16e-15  (numerical cross-check)
exact ℚ-rational certificate: YES (0 nonzero off-coset components)
selectivity:  λ=0 PARTIAL (intersection 1/5)
              λ=4,8,10 EMPTY (intersection 0)
              λ=12 FULL (intersection 10/10)
E_lifted:   10D  ≅ 2·Y₅
E_residual: 15D  ≅ 3·Y₅
E600(12):   25D  ≅ 5·Y₅
Verdict: SELECTIVE_SPECTRAL_BRIDGE
```

The runner also writes three machine-readable artifacts under
`docs/keystone_24_600/outputs/`:

- `wo008_summary.json` — full structured result.
- `wo008_verdict_table.csv` — one row per tested λ with verdict.
- `wo008_reproducibility_log.txt` — the runner's console log.

## What this artifact does and does not claim

It claims:

- A reproducible, selective λ=12 spectral channel between the five
  24-cell cosets of the 600-cell and the global λ=12 eigenspace.
- An exact decomposition `E600(12) = E_lifted ⊕ E_residual` of
  dimensions 10 and 15.
- An A₅-equivariant representation splitting `2·Y₅ + 3·Y₅ = 5·Y₅`.

It does **not** claim:

- to derive the Standard Model, particle masses, or any specific
  physical interpretation;
- to prove anything about cosmology, black holes, the Riemann
  hypothesis, or consciousness;
- to subsume or replace any other framework.

## Provenance

The result rests on existing, audited components:

- `papers/v600-programme/lib/vfd_v600/` — exact Q(√5) icosian arithmetic,
  the 120-vertex V₆₀₀ vertex set, the σ-Galois-twist 24-cell V₂₄, and
  the V₂₄ left-action used here to obtain the five-coset partition.
- `closure_transform_engine/keystone.py` — the d=1 graph construction,
  Laplacian eigenspace lift, residual computation, and A₅ character
  decomposition specific to this artifact.

The technical write-up is in [`spectral_bridge_note.md`](spectral_bridge_note.md)
(and identical LaTeX in `spectral_bridge_note.tex`).
