# The d=2 geometry, defined

The object the whole WO points at is a single, classical, completely well-defined
surface: the **modular orbifold**. Every line below is verified in
`../src/modular_scattering.py` and the definition run; none of it is conjectural.

## Definition

**The geometry is the quotient orbifold**

```
X  =  PSL(2,Z) \ H²
```

built from three pieces:

### 1. The space — the hyperbolic plane
```
H²  =  { z = x + iy  :  y > 0 },     ds² = (dx² + dy²) / y²
```
the upper half-plane with the hyperbolic metric, **constant curvature −1**. (This is
the d=2 case; "d" is the real dimension, and the Selberg line sits at Re(s)=(d−1)/2=½.)

### 2. The group — the modular group
```
PSL(2,Z)  =  ⟨ S, T ⟩,     S: z ↦ −1/z,   T: z ↦ z + 1
            with relations  S² = 1,  (ST)³ = 1     [VERIFIED: S²=−I, (ST)³=−I in SL₂]
```
acting by Möbius transformations z ↦ (az+b)/(cz+d). It is the **(2,3,∞) triangle
group** — one order-2 generator, one order-3 element, one parabolic (cusp) direction.

### 3. The quotient — the modular surface
Identify points of H² that differ by a modular transformation. The result X is a
**hyperbolic orbifold** with:

| feature | location | data |
|---|---|---|
| **fundamental domain** | `F = { \|Re z\| ≤ ½, \|z\| ≥ 1 }` | hyperbolic **area = π/3** [VERIFIED] |
| **order-2 cone point** | `z = i` | fixed by S; cone angle π [VERIFIED S(i)=i] |
| **order-3 cone point** | `z = ρ = e^{2πi/3} = (−1+i√3)/2` | fixed by ST; cone angle 2π/3 [VERIFIED ST(ρ)=ρ] |
| **cusp** | `z → i∞` | one parabolic point (the funnel) |

(Gauss–Bonnet check: area = −2π·χ_orb with χ_orb = −1/6 ⟹ area = π/3. ✓)

So **X is a sphere with one cusp (a funnel out to infinity) and two cone points** (a
sharp π corner at i and a sharper 2π/3 corner at ρ). That funnel in the poster is the
**cusp** — a consequence of the SL(2,ℤ) identification, *not* a pentagon gap.

## Analytic structure — why ζ lives here

On X put the **hyperbolic Laplacian** `Δ = −y²(∂ₓₓ + ∂_yy)`. Its spectrum has two parts:

- **Discrete** — the **Maass cusp forms**, eigenvalues `¼ + r²` (first r ≈ 9.534). These
  are the genuine self-adjoint bound states; they are **not** the Riemann zeros.
- **Continuous** — the **Eisenstein series** E(z,s), parametrised on the line Re(s)=½,
  with scattering coefficient (the constant term of E):
  ```
  φ(s) = ξ(2s − 1) / ξ(2s),     ξ(s) = π^{−s/2} Γ(s/2) ζ(s)
  ```
  **unitary on Re(s)=½** ( |φ(½+it)| = 1 [VERIFIED] ), and **its poles — the scattering
  resonances — are the Riemann zeros**, at s = ρ_ζ/2 = ¼ + iγ/2 ( |φ| spikes ~10⁶ there
  [VERIFIED] ).

## In one sentence

> **The geometry is the modular orbifold X = PSL(2,ℤ)\H²**: the hyperbolic plane folded
> by the modular group into a finite-area (π/3) surface with one cusp and two cone
> points (orders 2, 3). It is the **d=2 arithmetic surface** whose Selberg line is
> Riemann's line Re(s)=½, and the **Riemann zeros are the resonances of its Eisenstein
> scattering channel** φ(s)=ξ(2s−1)/ξ(2s). Proving those resonances lie on the line is
> Weil positivity = RH = the open wall.

Status: this is **standard, classical mathematics** (the modular curve / modular
orbifold, one of the most-studied objects in number theory). Defining it is exact and
non-speculative; the only open thing is the positivity wall, which is RH for everyone.
