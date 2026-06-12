# Tier-2: the adelic scaling operator — finite part verified, rest open
### 2026-05-30 · `route_b/adelic_scaling.py`

Question: does the cascade's adelic limit carry a ℂ-class scaling operator?

**Honest decomposition** of the adelic scaling operator:
- **finite places** = the Hecke algebra = the local scaling operators T_𝔮;
- **archimedean place** = the Mellin / dilation continuum (spectrum = the
  critical line).

## What is computable (verified)
The 2×2 Hecke operators on the Brandt module, built from the substrate's own
quaternion action:
```
T_(2)=[[2,3],[5,0]]  T_(√5)=[[3,3],[5,1]]  T_(3)=[[7,3],[5,5]]  T_(11)=[[6,6],[10,2]]
```
- **They commute exactly:** max ‖[T_a,T_b]‖ = 0 → a **commutative scaling
  algebra** (a torus of commuting local scalings).
- **Joint spectrum** = Eisenstein (N𝔮+1) ⊕ cuspidal (a_𝔮), with every
  cuspidal eigenvalue **unitary/Satake** (|a_𝔮| < 2√N𝔮).

So **the adelic limit DOES carry a ℂ-class (β=2, unitary) scaling structure
at the finite places** — exactly the side the Jacquet–Langlands trace and
the Katz–Sarnak bulk pointed to.

## What remains open (reduces to Tier-3, not fabricated)
- The **archimedean** scaling (Mellin/dilation, spectrum = critical line)
  combined with the finite Hecke data is **Connes' adele-class scaling
  action**. The zeros are its **absorption spectrum**.
- Realising the zeros as a **self-adjoint discrete point spectrum** =
  Connes' **Weil positivity** (computed *positive* for this L-function,
  `CONNES_POSITIVITY.md`) holding for **all** test functions = **RH**. Same
  open wall.

## Verdict
Tier-2 resolves the **finite / ℂ-class half**: the substrate's adelic limit
genuinely carries a commutative, unitary (ℂ-class) scaling algebra (verified).
The **archimedean dilation + self-adjoint realisation of the zeros** is not
separable from Tier-3 and remains open. We built and verified what is
buildable; we did not invent the operator.

## Net effect on the operator search (maximally sharpened)
The missing operator is now pinned as far as honestly possible:
- **class:** ℂ / unitary / β=2 (not the substrate's ℍ/β=4);
- **finite-place part:** the verified commutative Hecke (scaling) algebra;
- **what's missing:** the **archimedean dilation** glued to it, with a
  **self-adjoint** realisation making the zeros a discrete spectrum — i.e.
  Connes' Weil positivity for all test functions. That last step is RH.
