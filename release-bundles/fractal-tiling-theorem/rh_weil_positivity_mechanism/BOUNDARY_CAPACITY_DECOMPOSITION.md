# Deliverable E — boundary-capacity decomposition

Source: `boundary_capacity_tests.py`,
`results/phase_5_boundary_capacity/boundary_capacity.json`.

## Theorem Target 2: `Q_Weil = H − R`, `H ⪰ R`

The decomposition is **canonical** — `H` and `R` are literally the explicit
formula's own terms, not invented after the fact:

```
H = ARCH + POLE   (archimedean / completed boundary CAPACITY)
R = PRIME          (prime residual LOAD)
Q_Weil = H − R
```

## Results (basis: 7 heights 12–40, σ=2)

| block | min eig | max eig | property |
|---|---|---|---|
| `H` capacity | +0.57 | +2.71 | **positive kernel (PSD)** |
| `R` load | −0.81 | +0.92 | **indefinite** |
| `Q = H − R` | ≈ 0 | — | PSD (capacity dominates load on this basis), at the edge |

## The two structural facts that matter

1. **The archimedean capacity `H` is a positive kernel.** This is the real reason
   positivity has any chance: the completion contributes a genuinely
   positive-definite form. (Consistent with the Weil/Barner theorem that the
   archimedean term is positive.)
2. **The prime side alone is not positive.** `R` is indefinite (it has negative
   eigenvalues), so:
   > *Can the prime/Euler-product side alone ever be positive?* **No.**
   Positivity **requires** the archimedean completion. The Euler product is not
   enough — the completed (adelic) object is essential (Deliverable G).

## RH as capacity dominance

```
RH   ⇔   H ⪰ R   for ALL admissible h
      ⇔   the positive boundary capacity dominates the prime load everywhere.
```

This is exactly VFD's "closure capacity vs prime pressure" — a faithful
re-description of Weil positivity. On the tested basis `H ⪰ R` holds and `Q` sits
at the positivity edge; the **universal** quantifier is RH and is not proved.

## Is this new structure or a relabelling?

It is **canonical and explanatory** (it correctly localises the positivity in the
archimedean block and the threat in the prime block), but it is **not a new
theorem**: `H ⪰ R ∀h` is the classical Weil positivity. VFD supplies the
capacity/pressure language; it does not supply the dominance proof.
