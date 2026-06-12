# The negative hyperbolic object: the {3,3,5,3} honeycomb of H⁴

A built, verified patch of the regular honeycomb that fills **hyperbolic** 4-space
with **600-cells** — the "negative" dual fabric to the spherical 600-cell.

## What it is
The 600-cell `{3,3,5}` is spherical (it tiles `S³`). It does **not** tile flat `R⁴`.
It fills 4-space only in the **hyperbolic** honeycomb `{3,3,5,3}` (3 600-cells around
each face) — a regular tessellation of `H⁴`. This is the concrete "negative hyperbolic
object" that completes the fabric the spherical cells cannot tile alone.

## What `build_h4_honeycomb.py` does (and verifies)
1. Builds the Schläfli/Gram matrix of `[3,3,5,3]` — **signature (4,1)** (Lorentzian = `H⁴`). ✓
2. Builds the 5 reflection generators `s_i = I − 2 e_i e_iᵀ M` in `O(4,1)`.
3. **Verifies the Coxeter relations**: `s_i²=1`, consecutive orders `[3,3,5,3]`,
   non-adjacent reflections commute → the group is genuinely `[3,3,5,3]`. ✓
4. Seeds at a **600-cell cell-centre** (fixed point of the finite `[3,3,5]` subgroup;
   `B(p,p)=−0.079 < 0` → a proper point of `H⁴`).
5. BFS the orbit → an "onion" of shells of 600-cells; projects to the **Poincaré ball**;
   saves `results/honeycomb_patch.json`.

## Result (this run)
452 600-cell centres, shells growing `1,1,1,2,4,5,8,12,19,29,44,67,102,156`
— **exponential** (~1.52/shell), radii `0.755 → 0.983` toward the `H⁴` boundary.
Exponential shell growth **is** the signature of negative curvature, so the build
confirms its own hyperbolicity.

## Honest scope
- The `{3,3,5,3}` honeycomb is a **known** regular hyperbolic honeycomb (Coxeter);
  we *constructed and verified* a finite patch — real, reproducible geometry, not new.
- `H⁴` is **Euclidean anti-de Sitter (AdS)**; this connects to the programme's `S³`/
  hypersphere substrate and to holographic (AdS/CFT) field theory — a real framework.
- **Boundary:** this is *geometry*. That the fabric *generates physical wave fields* is
  the interpretive layer (the human seat), not established here; and this is the
  geometry/cosmology side of VFD — separate from the icosian-arithmetic / RH work.

Reproduce: `python3 build_h4_honeycomb.py`.

## Baby-RH demonstration (`baby_rh_eigenvalues.py`)
A finite self-adjoint operator built from the honeycomb (452-cell adjacency
Laplacian, `<deg>≈14`) has real spectrum; mapped to the H^4 Selberg plane
(`λ = s(3−s)`, critical line `Re(s)=3/2`):
- **447 tempered zeros exactly on `Re(s)=3/2`**, 5 exceptional on the real axis
  (spectral gap `λ₁=1.58`), **0 violations** — baby RH holds.
- Breaking self-adjointness (antisymmetric part) sends **422/452** eigenvalues
  complex → zeros off the line. Self-adjointness IS the mechanism.

Honest scope: a finite discrete MODEL of the mechanism (not the true continuous
Selberg spectrum, and these are the honeycomb's eigenvalues, NOT the Riemann
zeros). It demonstrates "lossless self-adjoint engine ⟹ zeros on a line" firing
on a real golden-field hyperbolic object — the mechanism the true RH object would
need; attaching it to the actual zeros is Hilbert–Pólya (the wall).
Output: `results/baby_rh_spectrum.json`.

## Prime geodesics — the prime side (`prime_geodesics.py`)
The closed geodesics of the honeycomb = prime cycles of the cell graph.
Non-backtracking (Ihara) spectrum, Perron `R=24.15`:
- **Prime geodesic length spectrum** `π_k` (number of prime closed geodesics of
  length k): `π₃=15,798`, `π₄=162,418`, … `π₁₄≈1.6×10¹⁸`, growing like **`R^k/k`** —
  the graph **prime geodesic theorem** (analogue of primes `~ x/log x`).
- **Ihara duality VERIFIED**: prime-geodesic Euler product `∏(1−u^k)^{−π_k}` equals
  the spectral determinant `1/[(1−u²)^{m−n} det(I−Au+Qu²)]` to 0.01% at `u=0.02`.
  Prime side (geodesics) **==** line/spectral side (eigenvalues): one zeta, two faces
  — the prime↔zero duality realised geometrically, the twin of the explicit formula.

Honest scope: the cell graph is a finite nearest-neighbour proxy; the Ihara analysis
is exact *for this graph*, and these are the honeycomb's own geodesics/eigenvalues,
NOT the Riemann primes/zeros. It demonstrates the structure; attaching it to ζ is the wall.
Output: `results/prime_geodesics.json`.
