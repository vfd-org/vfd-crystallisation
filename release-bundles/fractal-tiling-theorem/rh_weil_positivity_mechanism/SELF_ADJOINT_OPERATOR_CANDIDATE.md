# Deliverable H — self-adjoint operator candidate

Source: `operator_candidate_tests.py`,
`results/phase_4_factorisation_kernel/operator.json`.

## Theorem Target 4: `Q_Weil[h] = ⟨h, K h⟩`, `K = K*`, `K ⪰ 0`

### Domain
The admissible test-function cone (finite model: span of even Gaussians at
heights `t_a`).

### Action
`K` is the Weil Gram operator: `(K c)_a = Σ_b Q_{ab} c_b`, `Q = H − R` from the
explicit formula.

### Tests (basis: 6 heights 12–40, σ=2)

| property | result |
|---|---|
| symmetric `⟨f,Kg⟩=⟨Kf,g⟩` | **yes** |
| positive `⟨h,Kh⟩≥0` on 200 random `h` | **yes** |
| spectrum | `[0.05, 2.31]` (PSD) |

### Is `K` new?

**No.** `K` is the Weil functional represented as an operator. Its
self-adjointness is automatic (the Gram is symmetric); its positivity on the full
admissible class is RH.

### What theorem would make `K ⪰ 0` universal?

Exactly RH. Equivalently: a **canonical self-adjoint operator whose spectrum is
the zero ordinates `γ_n`**, arising from the archimedean–adelic completion (not
from the assumed zeros). That operator is the Hilbert–Pólya object and is open.

## Honest status

We have a self-adjoint, positive (on tested bases) operator `K` — but it is the
Weil functional in operator clothing, and its universal positivity is RH. No
canonical zero-spectrum operator is constructed. This satisfies the WO's pass
condition (a precise operator candidate is defined) while making clear it is not
a route through the wall.
