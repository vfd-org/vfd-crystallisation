# Deliverable F — kernel positivity report

Source: `kernel_positivity_search.py`,
`results/phase_4_factorisation_kernel/kernel.json`.

## Theorem Target 3: `Q_Weil[h] = ⟨h, K h⟩`, `K ⪰ 0`

Discretised on the test-function basis, `Q_Weil[c] = cᵀ K c` with `K = Q = H − R`,
i.e. the canonical decomposition `K = K_arch − K_prime`.

## Results (basis: 8 heights 12–42, σ=2)

| kernel block | min eig | property |
|---|---|---|
| `K_arch` (archimedean) | +0.49 | Hermitian, **PSD — positive kernel** |
| `K_prime` (prime) | −0.66 (max +0.68) | Hermitian, **indefinite** |
| `K = K_arch − K_prime` | ≈ 0 | Hermitian, PSD on basis (edge) |

Hermitian symmetry `K(x,y)=conj(K(y,x))` holds for both blocks (Test 5 setup
valid).

## What the candidate kernel is

`K` is **exactly the Weil kernel** — the integral kernel of the explicit-formula
quadratic form, with the archimedean part `K_arch` carrying the positivity and
the prime part `K_prime` threatening it. It is **not a new kernel**.

## Is `K ⪰ 0` equivalent to RH?

**Yes.** On finite bases `K` is PSD (at the edge); and the off-line teeth
(Deliverable D) show `K` develops a negative eigenvalue **iff** a zero leaves the
critical line. So `K ⪰ 0` on the full admissible space `⇔` RH — the universal
quantifier, unproved.

## Conclusion (Test 7 — existing-math reduction)

The kernel search produces the Weil kernel itself. Its positivity is RH; there is
no new positive kernel that sidesteps the universal quantifier. This is a clean
**reduction to Weil positivity**, stated honestly.
