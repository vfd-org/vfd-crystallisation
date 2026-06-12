# The three mirrors and where they agree (map)

All three are order-2 involutions (mirrors). They live on linked spaces; the common arena
is the spectral / L-function picture. Computed by three_mirrors_map.py.

| mirror | involution | fixed locus | computed |
|---|---|---|---|
| **M1 τ_FE** (analytic) | s ↔ 1−s  (t↔1/t, u↔−u) | critical line Re(s)=1/2 | the FE axis (witness axis) |
| **M2 σ** (Galois/arithmetic) | √5 ↔ −√5  (φ↔φ̄) | rational/integer part | 600-cell spectrum: **94 σ-fixed** (integer eigs = 1+16+25+36+16), **26 σ-paired** (φ-irrational 6φ/4φ ↔ 6−6φ/4−4φ = 13+13) |
| **M3 JL/curvature** (geometric) | compact spherical ↔ hyperbolic | same L-function both sides | norm-31 a_P are **integers** (σ-fixed) and JL-matched |

## Agreements
- **τ ∩ σ** (ESTABLISHED — per-observer-zero-line): the σ-fixed (rational, 94/120) modes lie
  on Fix(τ) = the critical line. `Σ_𝓘 ⊂ Fix(τ)`, proven modulo Galois for the 94; the 26
  σ-paired modes are the conditional residue (H_attr closure-flow suppression).
- **σ ∩ JL**: the cusp form's `a_P` are integers ⇒ σ-fixed (Galois-rational), AND JL-matched
  (icosian compact ↔ hyperbolic). Rational + doubly-realised.
- **τ ∩ JL**: both realisations share ONE completed L-function ⇒ one functional equation ⇒
  one critical line.
- **TRIPLE (M1∩M2∩M3)**: the locus that is FE-self-dual + Galois-rational + JL-doubly-realised.
  The **norm-31 Hilbert cusp form sits exactly here**: integer (σ-fixed) `a_P`, Ramanujan
  `|a_P|≤2√N(P)` (FE/critical-line consistent), JL-matched. A concrete witness at the
  triple-fixed point.

## Reading
The three mirrors are one ladder of ℤ/2 involutions whose **common fixed locus is "the
rational, self-dual, doubly-realised spectrum"** — exactly where RH lives. They agree
**provably on the 94 σ-fixed integer modes** (which sit on Fix(τ)); the **26 σ-paired modes
are the open residue**. The agreement is a MAP, not a proof of RH: RH is the statement that
the σ-paired residue *also* lies on Fix(τ), and that is precisely the part the three mirrors
do NOT pin down together.
