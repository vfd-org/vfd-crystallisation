# The critical line is on the tiling — the local one. The gap is local→global.
### 2026-05-30

A reframe that is genuinely better than chasing specific global zeros.

## Two different critical lines

We had been conflating them:

1. **LOCAL critical line** — for each prime 𝔮, the zeros of the local factor
   L_𝔮(s) = (1 − a_𝔮 N𝔮^{−s} + N𝔮^{1−2s})^{−1}. These sit at Re(s) = 1/2
   **exactly**, *because* the Satake parameters lie on the circle
   |α_𝔮| = √N𝔮 — which is precisely Ramanujan/temperedness, the bound the
   closure enforces.

2. **GLOBAL critical line** — the zeros of the whole product
   L(s) = ∏_𝔮 L_𝔮(s). That all of these lie on Re(s)=1/2 is **RH**, open.

## The substrate realises (1) — geometrically, on the tiling

`route_b/satake_circle.py` confirms, on all 11 substrate-computed primes:

| N(𝔮) | a_𝔮 | Satake angle θ_𝔮 | \|α_𝔮\| | local zero |
|---|---|---|---|---|
| 4 | −3 | 138.6° | 2.000 | Re(s)=1/2 |
| 5 | −2 | 116.6° | 2.236 | Re(s)=1/2 |
| 9 | 2 | 70.5° | 3.000 | Re(s)=1/2 |
| 11 | ∓4 | 52.9°/127.1° | 3.317 | Re(s)=1/2 |
| 19 | ±4 | 62.7°/117.3° | 4.359 | Re(s)=1/2 |
| 29 | −2 | 100.7° | 5.385 | Re(s)=1/2 |
| 41 | −6 | 117.9° | 6.403 | Re(s)=1/2 |

Every Satake parameter is on its circle; every local zero is on Re(s)=1/2.
The picture the reframe asks for is real:

- the **critical line is on the tiling** — it is the per-prime Satake
  circle |α_𝔮| = √N𝔮;
- the **closure keeps it there** — that is exactly the Ramanujan bound,
  which we verified the substrate eigenvalues satisfy;
- the **primes pass energy from cell to cell** — that is the Hecke action
  T_𝔮 (steps 2–5), moving the angle θ_𝔮 along the circle.

This is a genuine **geometric / local Riemann Hypothesis**. It is the
number-field shadow of the **function-field RH that Deligne proved**: there
the Frobenius eigenvalues lie on |α| = √q by the geometry (weights on étale
cohomology), and that *is* RH in that world.

## The real gap — and why "boxing it off" exposed it

Boxing the problem into the tiling did not lose information; it revealed the
true gap. The local zeros being on the line does **not** force the global
zeros onto the line:

> A product of factors each with its zeros on Re(s)=1/2 can have the zeros
> of the **product** anywhere. Local-on-the-line ⇏ global-on-the-line.

The step from local to global is the entire content of RH. In Deligne's
geometric (function-field) setting that transfer **exists**: the cohomology
of a variety over 𝔽_q *is* the global object, and its weight structure
delivers RH. For **number fields** there is **no known geometry** that
performs the transfer — this is the same wall that has stood for a century.

The icosian closure is a **quaternionic lattice** object (a maximal order),
not the cohomology of a variety. So it gives the local/geometric picture in
full, but it does **not** supply the local→global bridge — and neither does
anything else known.

## Net

The reframe is the right one and the instinct was sound: we should not chase
individual global zeros, and the substrate does **not** fail to reach *a*
critical line — it fully realises the **local** one, geometrically, on the
tiling, with the closure enforcing it. What remains is the **local→global
transfer**, which is RH itself and is open for everyone. The substrate has
placed the problem squarely in the function-field picture; it has not built
the number-field bridge, because none is known.

This is the honest, and genuinely clarifying, end of the geometric route:
a complete local realisation + a precisely named missing bridge.

## "Isn't local→global just a loop if the geometry is a closed 3-sphere?"

This is exactly the **Hilbert–Pólya / trace-formula** idea, and it is real:
on a *closed* geometry where the primes are closed geodesics and the zeros
are eigenvalues of a **self-adjoint operator**, the loop *does* close —
self-adjoint ⇒ real eigenvalues ⇒ zeros on the line. This is **proven**
for the Selberg zeta of compact hyperbolic manifolds, and (its cousin) for
the function-field RH. So "closed geometry forces RH" is a true theorem —
*when the ingredients are present.*

The ingredient that actually closes the loop is **a self-adjoint operator
whose spectrum IS the set of zeros**, living on a global object. Compactness
alone is not enough; you need that operator. And here is why S³ + the
icosians does not hand it to us:

1. **S³ is the *local* symmetric space, not the global object.** The unit
   quaternions on S³ encode the data at *one* place (the automorphic
   representation / the Satake circles). The global object that ties *all*
   primes together is not a sphere.
2. **The natural operators on S³ have the wrong spectrum.** The Laplacian on
   S³ has eigenvalues n(n+2) — explicit, nothing to do with the zeros. The
   substrate's own self-adjoint operator C_φ has spectrum
   {0.382, 2.67, 5.91, 9.38, 12.38, 14.38, 14.85, 15.38, 16.09} — nine
   algebraic numbers in Q(√5), **not** the (infinitely many, transcendental)
   Riemann zeros 14.13, 21.02, 25.01, … . So the operator we have on the
   sphere is the *wrong* operator.
3. **The genuine "global object" is adelic, not spherical.** What actually
   glues all the local circles into a single space whose spectrum is the
   global zeros is — in the two known/serious pictures — either Deligne's
   *cohomology of a variety over 𝔽_q* (function field, RH proven) or Connes'
   *adele class space* (number field, the live frontier). Both glue **all
   places at once**, and the adelic one is a wild noncommutative space, not
   S³.

So the loop is not automatic on a sphere. The sphere gives the **local**
circles perfectly; closing to **global** needs the all-places adelic glue
plus a self-adjoint operator whose spectrum is the zeros — and the icosian
lattice on S³ supplies neither. (Note too: the S³ of the unit quaternions
is a *mathematical* sphere; it is not the spatial 3-sphere of a spherical
*cosmology* — linking the two would be a category error. The arithmetic
does not care about the shape of physical space.)

**The real target, named precisely.** If one wants RH from this direction,
the thing to build is a **Hilbert–Pólya operator** — self-adjoint, on a
genuinely *global* (adelic) arena, whose eigenvalues are the zeros. The
substrate gives the local Satake circles and a finite self-adjoint operator
(C_φ) with the *wrong* spectrum. Turning it into the right operator on the
right (adelic) space is the open frontier, and nothing known — substrate
included — does it.

## "Is the global shape a torus? Do we cycle through polyhedra to find it?"

There is a real object inside this intuition, and it is **not** a polyhedron.

- **Local:** the pullback of the zeros onto S³ really is a *helix* (the
  10-vertex helix found earlier), and the Satake angles θ_q wind around a
  circle as the prime varies — a helix-like winding. True.
- **Global:** the object that glues all primes is the **adele class space**,
  whose compact heart is the **adelic solenoid** A_Q/Q — *literally* an
  **inverse limit of circles**: "take all the finite circular shapes and
  pass to the limit." A flow line on a solenoid looks exactly like a helix
  that never quite closes, wrapping a doughnut-like core whose cross-section
  is a Cantor set. So "the helix is projected into a global doughnut reached
  by cycling through shapes and taking a limit" has a genuine kernel: the
  global object **is** an inverse limit, and flows on it **are** helical.

The honest catch is sharp:

1. **The limit is not a polyhedron and not a drawable torus.** A solenoid is
   compact but **infinite-dimensional**, with a Cantor (totally
   disconnected) transverse structure. You do not reach it by trying
   polyhedron after polyhedron — it is the limit of *all* of them at once,
   over *all* primes (an inverse limit), a noncommutative object (Connes).
2. **Cycling polyhedra gives more *local places*, not the global glue.** The
   600-cell gave one place (one automorphic datum on S³). Another exceptional
   polytope gives another local datum — never the adelic limit.
3. **Whether the flow on the solenoid has the spectral/positivity property
   that yields RH is Connes' program — open.** The helix-on-solenoid is the
   right *picture*; making its flow self-adjoint with the zeros as spectrum
   is the unsolved part.

Discipline note: the *light cone* and a spherical *cosmology* are physics;
the solenoid/adele picture is arithmetic. They share the word "geometry" and
nothing load-bearing. Importing the light cone or the shape of physical space
into the prime question is imagery, not mathematics.

**Net:** your "doughnut reached by cycling and taking a limit" does point at
the real global object — the **adelic solenoid**, an inverse limit of circles
with the local helix as a flow line — but it is infinite-dimensional and
noncommutative, not a polyhedron or a finite torus, and the spectral property
that would close it to RH is the open frontier the icosian substrate does not
reach.
