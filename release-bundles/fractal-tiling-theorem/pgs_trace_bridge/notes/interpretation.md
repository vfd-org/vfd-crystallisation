# Interpretation — WO-VFD-PGS-TRACE-BRIDGE-001

## What is real
- `E(n)=(τ(n)/2−1)log n` is exactly `0` on primes (`τ=2`) and `>0` on every composite
  (`τ≥3`). The "chamber" picture — zero boundary, positive interior — is **true by
  construction**, not an empirical discovery.
- Gap-chamber statistics (length, interior width, min/max/mean/sum E) compute cleanly.

## What does NOT hold (the honest core)
1. **Operator self-adjointness is tautological.** The chamber operator is a symmetric
   tridiagonal `T = diag(V) + offdiag(1)`. Any real symmetric matrix has real
   eigenvalues, so the "self-adjointness / real-spectrum" test passes for `V = E, H, τ,
   log, Λ` **and a random diagonal** (sym-error 0, all eigenvalues real, in every case).
   It therefore certifies nothing about `E(n)`. Self-adjointness here is a property of
   the *construction*, not the arithmetic.
2. **The σ-balance probe is tautological.** `R(σ)=|Φ(σ)−Φ(1−σ)|`, `Φ(σ)=Σ w(n)n^{−σ}`,
   gives `argmin σ = 0.5` and `R(0.5)=0` for **every** weight tested (`Z_E`, `e^{−H}`,
   `log`, `Λ`, `|μ|`, **random**). The reason is structural: a bare Dirichlet series has
   **no σ↔1−σ functional equation** (ζ(s) is *not* symmetric; only the completed ξ(s),
   with the archimedean Γ-factor, is). So `Φ(σ)` and `Φ(1−σ)` are unrelated numbers, and
   `|Φ(σ)−Φ(1−σ)|` is *defined* to vanish at the midpoint. The "preferred σ=1/2 axis" is
   an artifact of the metric, identical for arithmetic and random weights.
3. **Chamber interiors are not mirror-symmetric.** Normalised symmetry residual: real E
   `0.317` vs gap-local shuffle `0.363`. Real is marginally lower (more "symmetric"),
   but this is a weak **local-autocorrelation** effect — adjacent composites have
   correlated divisor counts, so the unshuffled field is locally smoother — not mirror
   symmetry about the gap centre, and it carries no critical-line structure.

## The lesson (where the real missing ingredient is)
The bridge fails not because `E(n)` is wrong but because **neither test contains an
involution / functional equation**. A genuine σ↔1−σ balance requires the *completed*
object (archimedean Γ-factor + functional equation), and a genuine self-adjoint
*spectrum-on-a-line* requires a substrate that forces the spectrum real — neither is
supplied by a diagonal potential or a raw Dirichlet sum. This is precisely the
archimedean-completion / geometric-substrate gap identified in
`WO-RH-ARITHMETIC-TRACE-FORM-SEARCH-001` (the canonical form is the adelic explicit-
formula trace; its positivity needs a geometric substrate the number field lacks).

So PGS feeds `WO-VFD-INVARIANT-TRACE-FORM-LAW-001` only as a **source-side diagnostic**:
the diagonal pressure field is real, but the *kernel/involution* — the hard part — is
not provided by `E(n)`.
