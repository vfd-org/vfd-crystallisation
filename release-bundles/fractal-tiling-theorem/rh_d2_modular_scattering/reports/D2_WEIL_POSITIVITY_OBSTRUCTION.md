# WS-E/F — d=2 Weil positivity (gated) and the obstruction

**Engine.** The Weil explicit formula for ζ, on an even test-function basis
`h_k(r) = e^{−w²r²/2} cos(a_k r)` (w=0.12, a_k = 0,1,2,3,4), with

```
Σ_ρ h(γ) = [h(i/2)+h(−i/2)]  −  2 Σ_n Λ(n)/√n · g(log n)  +  [(1/2π)∫h(r)Re ψ(¼+ir/2)dr − g(0)log π]
            └─── pole ───┘        └────── prime ──────┘        └────────── archimedean ──────────┘
```

## Validation gate (non-negotiable)

Single-function gate (a=0): zero-side `Σ_γ h(γ) = 0.11630` vs `pole − prime + arch =
0.11630`, **rel.err 9×10⁻¹⁶**. The explicit-formula machinery is correct and
non-circular (primes + archimedean only; zeros appear *only* in the gate). An earlier
run with w=0.6 failed because the test functions vanished at the zeros (γ≥14) — fixed
by widening (small w). **[VERIFIED]**

## Positivity of the 5×5 Weil Gram form

| form | min eigenvalue | PSD? |
|---|---|---|
| zero side (validation) | +0.0000 | PSD |
| **COMPLETE** (pole − prime + arch) | **+0.0000** | **PSD** |
| drop archimedean (pole − prime) | +0.5324 | PSD |
| prime only (−prime) | **−34.6** | **NOT PSD** |

## Findings (honest)

1. **The completed Weil form is PSD and equals the zero side** (gate-validated). The
   form genuinely reflects the on-line zeros.
2. **The prime term alone is strongly indefinite** (min eig −34.6). The completion
   (pole + archimedean) is *required* to reach positivity — the bare prime "emissions"
   cannot make a positive form; the boundary/completion terms must close it.
3. **Apportionment is basis-dependent.** In this cos-Gaussian basis the pole term
   already lifts the form positive and the archimedean term sets the *marginal* edge
   (complete min eig ≈ 0). In the route_b autocorrelation basis the archimedean
   integral itself carried positivity (dropping it broke PSD). The **basis-independent**
   facts are the robust ones: prime-only indefinite; completed form PSD; positivity is
   marginal.

## The obstruction (= the wall)

PSD on a finite basis **reflects** zeros-on-line; it does **not force** it. The
statement "the completed Weil form is PSD for *all* test functions" **is** Weil
positivity **is** RH. No finite computation crosses it. This reaches the **same wall**
as the validated route_b operator program (Connes/Weil positivity, gated on ζ to 0.01%,
knife-edge as the cutoff grows) — now in the explicit d=2 modular frame. **[OPEN]**
