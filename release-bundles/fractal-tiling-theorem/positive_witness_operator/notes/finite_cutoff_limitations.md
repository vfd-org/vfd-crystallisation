# Finite-cutoff limitations

- The Weil form is computed on a 12-function Gaussian basis (centres 14+4k), primes
  ≤2000, r-grid ±150. `min eig = +0.00004` is a **finite-cutoff** number; the lowest
  eigenvalues collapse to 0 as the cutoff grows (NULLMODE-FACTOR: λ₀~N⁻⁴,
  basis-dependent). **Finite PSD ≠ infinite PSD.**
- The explicit-formula balance (3.7e-10) used σ=0.3 (so the test function's transform
  overlaps the first ~9 zeros) and 40 zeros / primes ≤3000; it is truncation-limited,
  not exact. (σ=1 is ill-conditioned: ZeroSide underflows and the identity demands
  ~40-digit cancellation — the identity still holds, the *float computation* doesn't.)
- The scale generator is a finite-difference `D` on a bounded interval with boundary
  effects; its spectrum approximates the unbounded operator only in the bulk.
- None of these limitations are hidden; all are the standard finite-truncation caveats,
  and none of them can be removed by more computation — the limit is RH.
