# A falsifiable test for any candidate "RH object"

**Distilled 2026-06-03 from the honeycomb prototype.** Any geometry/operator
proposed as *the* Riemann object must pass all of the following. The `{3,3,5,3}`
hyperbolic honeycomb (built in `hyperbolic_600cell_honeycomb/`) is the **worked
exemplar**: it passes the *mechanism* tests (1–4, for its own zeta) and fails the
*arithmetic-lock* tests (5–8). The failing tests are the wall.

## The mechanism (honeycomb PASSES, for itself)
1. **Prime side.** Primitive closed geodesics / cycles exist.
   — honeycomb: `π_k` prime cycles, `π₃=15798,…`, growth `R^k/k`, `R=24.15`. ✓
2. **Spectral / line side.** A self-adjoint operator with real spectrum.
   — honeycomb: cell-adjacency Laplacian, real spectrum, gap `λ₁=1.58`. ✓
3. **One zeta, two faces.** Prime Euler product `=` spectral determinant.
   — honeycomb: Ihara duality verified to 0.01% (`u=0.02`). ✓
4. **Self-adjointness ⇒ zeros on a line.** Real spectrum ⇒ zeros on the critical line.
   — honeycomb: 447/452 on `Re(s)=3/2`, 0 violations; breaks if self-adjointness broken. ✓

## The arithmetic lock (honeycomb FAILS — the wall)
5. **Primes = rational primes.** The primitive cycles must be `2,3,5,7,…` with
   lengths `log p` (and prime-power weights matching the explicit formula).
   — honeycomb: cycles are golden-field geodesics, lengths NOT `{log p}`. ✗
6. **Spectrum = Riemann zeros.** The eigenvalues must be the `γ_n`, line `Re(s)=1/2`.
   — honeycomb: eigenvalues are its own, line `Re(s)=3/2`. ✗
7. **Cardinality = infinite.** Countably infinitely many zeros (transcendental ζ).
   — finite graphs give *rational* zetas (finitely many zeros). ✗ for any finite model.
8. **Field = ℚ.** Riemann ζ is over ℚ (rational primes), not a sibling field.
   — honeycomb / icosian machinery is over ℚ(√5). ✗ (sibling field).

## Where the object that passes 5–8 is believed to live
Not a classical manifold. The live candidates for the arithmetic lock are
**Deninger's arithmetic flow** (closed orbits = primes, length `log p`; zeros =
spectrum of a Frobenius flow) and **Connes' arithmetic site / adele class space**
(zeros = spectrum of the idele-class action — a *noncommutative* space). The gap is
therefore likely **classical → noncommutative geometry**, plus **finite → infinite**,
plus **ℚ(√5) → ℚ** — not merely a re-tuning of the honeycomb.

## What the exemplar proves (and doesn't)
- **Proves:** the RH-shaped architecture (prime side ⇄ one zeta ⇄ self-adjoint line)
  is *real and constructible* — a working prototype exists in a golden-field geometry.
- **Does not prove:** that the rational primes / Riemann zeros are *that* architecture.
  Passing 5–8 is the Riemann Hypothesis; no object here passes them.

**Use:** apply tests 1–8 to any future "RH geometry" candidate. Passing 1–4 means
"correct mechanism"; only passing 5–8 means "the Riemann object." Most candidates
will pass the first four and stop — exactly like the honeycomb.
