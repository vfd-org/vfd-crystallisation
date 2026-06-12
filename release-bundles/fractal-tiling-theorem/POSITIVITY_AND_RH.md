# Positivity, the Li criterion, and why the substrate stops at the coefficients
### 2026-05-30

This note answers the strategic question: now that the circle is closed
(the substrate genuinely computes the norm-31 newform), is there a route to
RH via *positivity* — the Li/Weil criterion — and does the substrate's own
positivity (the closure operator C_φ) help?

## The three routes, and the single wall

The substrate offers exactly three handles on the L-function, and all three
reach the same place and stop:

| Route | What it gives | Reaches the zeros? |
|---|---|---|
| Hecke multiplicativity tiling | finite primes → all coefficients | No |
| Admissibility + explicit formula | a genuine automorphic L-function | No |
| Positivity (C_φ / Weil–Li) | a finite positive operator + a real eigenform | No |

Every handle is **coefficient-side / geometry-side**. RH is **zero-side**.
That is the wall, and it is the same wall each time.

## Why positivity does not cross it

RH for L(f,s) is equivalent to the **Li criterion**:
```
λ_n = Σ_ρ [ 1 − (1 − 1/ρ)^n ] ≥ 0   for all n ≥ 1,
```
positivity of an explicit-formula functional on the **zeros** ρ.

The substrate has its own positivity, computed exactly in
`route_b/positivity_analysis.py`:
```
C_φ = (12 + φ⁻²) I − A_1   is positive definite on V_600;
smallest eigenvalue = φ⁻² = 0.381966 (the witness V_min, multiplicity 1);
9 distinct eigenvalues, all > 0.
```
But this is positivity of a **finite 120×120 operator** built from the
600-cell. The substrate's influence on L(f,s) factors as
```
C_φ ≥ 0  ──►  witness/eigenform exists  ──►  Hecke values a_𝔮
         ──►  Dirichlet series  ──►  analytic continuation  ──►  zeros  ──►  λ_n
```
C_φ ≥ 0 is used **only at the first arrow** (the eigenform exists). It does
not constrain the analytic continuation or the zero locations. There is no
theorem, and no plausible mechanism, by which positivity of the finite
operator C_φ implies λ_n ≥ 0. The two positivities are in different
categories:

- **C_φ ≥ 0** — finite-dimensional, algebraic (eigenvalues in Q(√5)
  determined by the 600-cell);
- **λ_n ≥ 0 (RH)** — analytic invariants of the zeros of L(f,s).

There is no arithmetic map from one to the other. Matching them would be
numerology, not a derivation.

## What computing λ_n would (and would not) show

Computing λ_n for L(f,s) is a well-defined numerical task — degree-4
gamma factor Γ_C(s)² gives a Bessel-K₀ approximate functional equation, the
a_𝔮 (which the substrate genuinely supplies) feed the Dirichlet
coefficients, and λ_n follows from the low zeros. If carried out, λ_n > 0
would be expected (this curve's L-function has its low zeros on the line,
as for every L-function checked to date).

But — and this is the load-bearing honest point — **λ_n > 0 would be a
property of L(f,s), not a substrate result.** It is evidence for RH-of-this-
L-function (i.e. GRH), exactly as open as before, and the substrate
contributes only the a_𝔮 that any computation of this newform would use.
The substrate's *distinctive* structure (C_φ positivity, σ-pairing) does
not appear in λ_n.

## Strategic conclusion

- **Extending the circle test is not progress toward RH.** The match is the
  confirmation of a theorem (icosian ring = maximal order ⇒ its Brandt
  action = this newform); more primes verify the code, not RH.
- **The "representative fractal" is real but boxes the wrong object.** Hecke
  multiplicativity + the A₅/P¹(F₃₁) fundamental domain box the *L-function*
  into finite data; the *zeros* are not finite-prime data, so RH is not
  boxed.
- **The positivity route hits the same wall.** Substrate positivity is
  coefficient-side; RH positivity is zero-side; no bridge.

**Net:** every substrate handle is coefficient-side and stops at the
eigenform. RH lives on the zero side, which no substrate structure reaches.
The honest standing of the programme at the RH question is: a *verified,
non-circular geometric realization of a genuine Hilbert newform* — a real
result — together with the clear finding that this realization does **not**
supply a route to RH. A genuinely different idea would have to act on the
zeros directly, and the substrate, as constructed, does not.
