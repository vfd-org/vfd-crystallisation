# E10 = E8++ : the Z-native hyperbolic over-extension + its baby-RH

The hyperbolic relative of E8. E8 tiles flat R^8 (a lattice, no gap); its
over-extension **E10 = E8++** is Lorentzian, signature **(9,1)**, a hyperbolic
Kac-Moody group acting on **H^9**, with lattice **II_{9,1}** (even unimodular,
over Z). E10's Weyl chamber is the **M-theory cosmological billiard**
(Damour-Henneaux-Nicolai). Unlike the {3,3,5,3} honeycomb (over Q(sqrt5)), E10 is
**Z-native** -- the right field family for Riemann.

## Built & verified (`build_e10_baby_rh.py`)
- Gram signature (9,1) = hyperbolic H^9. ✓
- 10 reflection generators satisfy the **E10 Coxeter relations** (adjacent order 3,
  else 2) -> genuinely E10. ✓
- 750-point orbit patch (seed = timelike fundamental weight, B=-84); exponential
  shells `1,3,5,9,14,24,36,55,81,118,167,236` = negative curvature.
- **Baby-RH on H^9** (critical line Re(s)=4, lambda=s(8-s)): 289 tempered zeros on
  Re(s)=4, 461 exceptional (real), **0 violations** -> holds. Break self-adjointness
  -> 726/750 off-line. Self-adjointness IS the mechanism, over Z.

## What it tells us (the significant part)
The baby-RH mechanism fires **identically** over Z (E10) as over Q(sqrt5) (honeycomb).
So the **field was never the obstruction** and neither was the geometry: the
self-adjoint -> on-line engine is universal. Switching to the Z-native lattice does
**not** cross the wall -- E10's geodesics/spectrum are its own, not the primes/zeros.
The missing piece is confirmed to be *specifically* the arithmetic-spectral lock
(Gate 6 / Connes-Weil positivity), not field, geometry, or mechanism.

Honest scope: finite discrete model; E10's own spectrum, NOT the Riemann zeros.
Output: `results/e10_baby_rh.json`.
