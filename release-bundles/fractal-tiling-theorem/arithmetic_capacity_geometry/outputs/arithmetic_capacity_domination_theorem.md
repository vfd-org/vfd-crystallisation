# Theorem candidate — Arithmetic Capacity Domination (= Weil positivity)

**Setup.** Let `H∞` be the completed adelic witness Hilbert space (functions on the idele
class space of ℚ). Let `H = A∞ + P` be the positive capacity operator (archimedean local
factor `+` pole). Let `R` be the finite-prime reflection operator (Euler-product /
prime-power trace). Let `K = H^{−1/2} R H^{−1/2}`.

**Theorem candidate.** If
1. `H = A∞ + P` is positive and self-adjoint on `H∞`,
2. `R` is `H`-bounded,
3. `K = H^{−1/2} R H^{−1/2}` extends to a bounded operator on `H∞`,
4. no norm escapes through the adelic-boundary channels (decay / compactness control),
5. **`‖K‖ ≤ 1`** (equivalently `R ≤ H` as forms, equivalently `Q_W = H − R ≥ 0`),

then the Weil positivity criterion holds, and **RH follows**.

**What is unresolved.** Conditions 1–4 are the analytic *setup* (a rigorous infinite
witness space with controlled operators); **condition 5 is the heart and is exactly Weil
positivity** — equivalent in difficulty to RH itself. No finite computation establishes it
(the near-null margin closes only in the limit). The standard route to *force* condition 5
is a **geometric substrate** (intersection/Hodge-index positivity), which exists and proves
the analogue in the **function-field** case (Weil's theorem) but is **not available over
Spec ℤ** — supplying it is the **Connes–Consani arithmetic site**, i.e. RH's open heart.

> This theorem candidate does **not** prove RH; it isolates the exact unresolved condition
> (5 + the setup 1–4), which is RH-equivalent.
