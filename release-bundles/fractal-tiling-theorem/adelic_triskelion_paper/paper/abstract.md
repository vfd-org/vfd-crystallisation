# Abstract

We consolidate a sequence of computational and structural tests leading to the **Adelic
Triskelion**, a *tested normal-form representation* of the completed-zeta architecture.
The finite-arithmetic arm reconstructs the Euler product `ζ(s)=∏_p(1−p^{−s})^{−1}`; the
archimedean arm reconstructs the completion factor `½π^{−s/2}Γ(s/2)` through the
Gaussian/Mellin transform; the scale-action arm reconstructs Jacobi theta self-duality
`θ(t)=t^{−1/2}θ(1/t)` and hence the functional equation `ξ(s)=ξ(1−s)`. A constructed
centre `W = Centre(F,A∞,S)` yields a finite positive-witness form
`Q_W = A∞ + P_F − R_S`, and the positivity problem is reformulated as a **capacity
contraction** `Q_W = H^{1/2}(I−K)H^{1/2}` with `H=A∞+P_F`, `K=H^{−1/2}R_S H^{−1/2}`, so
that positivity ⟺ `‖K‖ ≤ 1`.

Finite-cutoff experiments show `‖K_N‖ < 1` approaching 1 **from below** (0.99958 → 0.99981
over basis sizes 8–24), with a **stable, non-escaping, low-spectral-edge near-null mode**
and a capacity ratio `R/(A∞+P) → 0.9998`. Discriminating null models fail (removing the
archimedean arm destroys positive-definiteness; a wrong Γ-factor pushes `‖K‖` above 1; a
wrong reflection axis breaks the functional-equation residual). This is **consistent with
RH but does not prove it**: the gap `1−‖K_N‖` shrinks only in a basis-resolution-dependent
way, the positivity is marginal and gapless, and no finite computation decides the limit.

**This work does not prove the Riemann Hypothesis.** The remaining obligation is an
infinite-dimensional operator theorem — construct the full adelic witness space and prove
the limiting capacity-normalised reflection operator `K` satisfies `‖K‖ ≤ 1` for all
admissible test functions. That theorem is RH-equivalent (Weil's criterion). The
components are classical (Riemann; Tate; Weil; Connes); the contribution is the *tested
normal form*, the *elimination of false routes*, the *constructed capacity centre*, and
the *precise isolation of the remaining wall*.
