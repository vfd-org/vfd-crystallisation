# Web page copy — The 24--600 Spectral Bridge

## Hero

**The 24--600 Spectral Bridge**

A reproducible λ=12 eigenspace channel between five 24-cell cosets
and the 600-cell.

## 1. The result

The 600-cell — the regular 4-polytope with 120 vertices — splits
under its icosian/quaternion structure into five disjoint 24-cells.
On each 24-cell coset, the d=1 nearest-neighbour Laplacian has a
2-dimensional λ=12 eigenspace.  Each of those local eigenspaces
zero-extends *exactly* into the 25-dimensional λ=12 eigenspace of the
full 600-cell.

The lift residual:

    ‖L₆₀₀ v − 12 v‖ ≈ 6.2 × 10⁻¹⁵.

Ten dimensions worth of local 24-cell modes embed into a 25-dimensional
global spectral channel.  No floating-point in the vertex set; all
distances and group operations are exact in Q(√5).

## 2. Why λ=12 matters

The local 24-cell Laplacian has five distinct eigenvalues:
0, 4, 8, 10, 12.  Of those, **only λ=12 admits the zero-extension
lift**.  Every other eigenspace fails the lift by orders of magnitude.

This is what makes the result a *bridge* rather than a generic
sub-structure inheritance: the channel is opened by one specific
spectral resonance, not by accident.

## 3. Negative controls

| local λ | dim per coset | lift residual            | verdict   |
|---------|----------------|--------------------------|-----------|
|   0     | 1              | 1.34 × 10¹              | NEGATIVE  |
|   4     | 4              | 9.38 × 10⁰              | NEGATIVE  |
|   8     | 9              | 5.29 × 10⁰              | NEGATIVE  |
|  10     | 8              | 3.16 × 10⁰              | NEGATIVE  |
|  12     | 2              | 6.16 × 10⁻¹⁵           | POSITIVE  |

The controls foreground that we are presenting a *real* selectivity
result, not a generic eigenspace inclusion.

## 4. A₅ representation split

Right-multiplication by 2I on the 600-cell descends through Z(2I)
to a faithful A₅ action on the five cosets.  The full 25-dimensional
λ=12 sector decomposes under A₅ as

    E_lifted   ≅ 2·Y₅,
    E_residual ≅ 3·Y₅,
    E₆₀₀(12)   ≅ 5·Y₅,

where Y₅ is the 5-dimensional irreducible representation of A₅.
The character orthogonality check matches to ~10⁻¹⁵.

## 5. Reproduce it

```bash
python closure_transform_engine/examples/run_wo008_keystone.py
```

Outputs are written to `docs/keystone_24_600/outputs/` as JSON, CSV,
and a plain-text log.  Unit tests at
`closure_transform_engine/tests/` lock the dimensions, residuals, and
representation strings.

## 6. What this does and does not claim

It claims:

- a reproducible, selective λ=12 spectral channel between the five
  24-cell cosets of the 600-cell and the global 25-dim λ=12 sector;
- a clean direct-sum split of dimensions 10 + 15 = 25;
- an A₅-equivariant decomposition `2·Y₅ + 3·Y₅ = 5·Y₅`.

It does **not** claim:

- to derive the Standard Model, particle masses, or any specific
  physical interpretation;
- to prove anything about cosmology, black holes, the Riemann
  hypothesis, or consciousness;
- to subsume or replace any other framework.

This is a narrow, inspectable, reproducible geometry result.
