# WO-VFD-RH-POSITIVE-ADELIC-WITNESS-OPERATOR-001

Builds and tests the finite-cutoff **positive witness scaffold** at the centre of the
Adelic Triskelion — `PW=(H,D,J,Q,T,Ξ)`. **STRONG PASS as a proof-facing scaffold; NOT
a proof of RH.**

- **H,J,D:** witness space L²(log-scale); involution `J` (u↔−u, J²=I); scale generator
  `D=−i d/du` Hermitian, real spectrum, `JDJ=−D`.
- **Ξ (completed kernel):** Gaussian→½π^{−s/2}Γ(s/2) (4.7e-13), theta self-duality
  (1.4e-21), FE residual Ξ passes (2.5e-21); raw ζ + fake kernels fail.
- **T (explicit formula):** Riemann–Weil balance **residual 3.7e-10**.
- **Q (Weil positivity):** `D=A+P−R` min eig **+0.00004** (PSD with near-null mode).
- **Null discrimination:** positivity rejects no-archimedean (−5.0), fake-Γ (−0.11),
  random Hermitian (−4.0); the explicit-formula balance rejects shuffled primes (2424);
  the FE residual rejects raw ζ / fake completions. (Different nulls fail different
  tests — collectively discriminated.)
- **Hilbert–Pólya:** the positive self-adjoint operator is **not exhibited** (no
  non-fitted A_N) — the open problem.

**The wall:** finite PSD only *with* a near-null mode (`λ_min→0⁺`); infinite-limit
positivity for all admissible test functions = RH. This is the Weil/Connes criterion
(KNOWN) re-encoded — not new, not a proof. See `notes/`. Run: `python3
src/run_positive_witness.py`. LOCAL.
