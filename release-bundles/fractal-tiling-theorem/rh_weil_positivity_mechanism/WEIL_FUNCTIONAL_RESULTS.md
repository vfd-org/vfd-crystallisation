# Deliverable C — Weil functional results

Source: `weil_functional_harness.py`, `results/phase_2_weil_harness/harness.json`.

## Consistency: formula side = zero side

For even Gaussian test functions (σ=2) at heights `[14,21,25,30,33]`, the
formula-side Gram `ARCH+POLE−PRIME` matches the zero-side Gram `Σ_ρ h(γ_ρ)`:

```
max|Q_formula − Q_zero| / max|Q_zero| = 5.6e-16   (machine precision)
```

Convergence check (independence confirmed): at nz=20 zeros / P=100 primes the
agreement is 6.6e-10, tightening to 3e-16 by nz=40 / P=500 — i.e. the explicit
formula converges fast for smooth test functions, and the two sides are genuinely
independent computations. The harness is therefore trustworthy.

## The Gram and its split

```
Q = H − R   (Weil Gram = boundary capacity − prime residual)

Q = H − R  : min eigenvalue ≈ 0      → PSD, and at the EDGE of positivity
H = ARCH+POLE : min eigenvalue 0.57–0.66 → a POSITIVE kernel
R = PRIME      : min eig −0.81, max +0.92 → INDEFINITE (negative directions)
```

## Reading

- The Weil functional is reproduced exactly from the prime + archimedean side
  (no zeros) — the construction is sound and non-circular.
- The **archimedean boundary capacity `H` is positive**; the **prime residual `R`
  is indefinite**. Positivity of `Q` is therefore a genuine contest between a
  positive capacity and an indefinite prime load.
- The on-line Gram sits at the **edge** of PSD (min eig ≈ 0) — the form is
  *tight*, not comfortably positive. This is the critical-line signature, and it
  is what makes the off-line teeth (Deliverable D) sharp rather than washed out.

This is a stronger, more RH-sensitive regime than a wide-test-function scalar
evaluation (which is archimedean-dominated): here the quadratic form is working
at its positivity boundary.
