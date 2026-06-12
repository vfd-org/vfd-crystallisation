# Deliverable A — VFD ↔ standard-mathematics translation table

Every VFD term is mapped to an accepted mathematical object. The table is
meaningful without any VFD belief-language; the right column is what the code
actually computes.

| VFD term | Standard mathematical equivalent | Where it appears here |
|---|---|---|
| prime irreducible | Euler-product atom / prime generator of the multiplicative semigroup | `ζ(s)=∏_p(1−p^{−s})^{−1}` |
| resonance frequency | `log p` (the phase weight of `p^{−s}=p^{−σ}e^{−it log p}`) | `prime_resonance_field.py` |
| prime residual | arithmetic side of the explicit formula `Σ_p Σ_k (log p) p^{−kσ}…` | `weil_wall.py` PRIME(h) |
| closure boundary | functional equation `ξ(s)=ξ(1−s)`; archimedean Γ-factor + conductor | `weil_wall.py` ARCH(h) |
| mirror involution `Θ` | `s ↦ 1−s`; fixed axis `Re(s)=1/2` | `leakage_functionals.py` L3 |
| boundary capacity | archimedean completion (gamma factor) `Γ_ℝ(s)=π^{−s/2}Γ(s/2)` | `weil_wall.py` archimedean term |
| closure energy | positive quadratic form / norm `Q(x)=|Ax|²`, or Weil functional | `closure_form_candidates.py` D1, D2 |
| resonance operator `R` | self-adjoint Hecke/Brandt operator `B(P)` | sibling `brandt_matrices.py` |
| stable mode | eigenmode / spectral state (real eigenvalue) | Hecke eigenvalue `a_P` |
| leakage | failure of self-adjointness / nonzero boundary defect `R−R^*` | `closure_form_candidates.py` D3 |
| off-axis instability | non-self-adjointness / failure of Weil positivity | the wall |
| self-dual closure axis | critical line `Re(s)=1/2` | throughout |
| arithmetic energy | **mathematical** energy: norm / quadratic form / spectral weight — **not joules** | `arithmetic_energy.py` |

**Discipline honoured.** No entry requires VFD belief-language; each is a
standard object a number theorist would recognise. "Energy" is used only as a
positive quadratic form / norm / spectral weight, never as physical energy.

**Key non-trivial identifications produced by this programme (not just renaming):**
- the VFD "closure energy whose positivity = closure" is *precisely* the **Weil
  functional** `W(h)=ARCH(h)−PRIME(h)` (a theorem), and `W(h)≥0 ∀h ⇔ RH`;
- the VFD "resonance operator with real spectrum" is *realised* by the
  **self-adjoint icosian Brandt operators** `B(P)` (finite, exact), whose
  eigenvalues are the Hecke `a_P` — built parameter-free from geometry;
- the VFD "irreducible emitters with log-frequency" is *exactly* the explicit
  formula: the prime fluctuation `(ψ(x)−x)/√x` has its spectral peaks at the
  zeta zeros `γ_n` (verified, `prime_resonance_field.py` B2).
