# WO-PAPER-XLI — Schwarzschild Analogue on the Event Poset

## Programme Position
This paper is the first concrete solution paper in the GR branch of the programme. It tests whether the event-poset and metric machinery can produce a recognisable static, spherically symmetric gravitational field rather than only kinematic scaffolding.

## Scope
- Construct the VFD analogue of a static, spherically symmetric vacuum solution on the event poset.
- Show how the solution reduces to a Schwarzschild-like metric in the continuum regime identified in Paper XL.
- Derive the weak-field observables needed to compare against standard GR: redshift, null deflection, perihelion precession, and horizon condition if present.
- Clarify whether the "mass parameter" is a closure / observer invariant or an emergent coarse-grained descriptor.
- State precisely what is exact, approximate, or only asymptotic in the construction.

## Inputs
- Prior papers: XXIII–XXVII (metric candidates, curvature, field-equation analogues); XXVIII (shared substrate); XXIX (localised probe observers / LMC theorem); XXXIII (measurement principle); XXXV (synthesis); XL (continuum theorems).
- Cascade foundations: downstream discrete-geometric portions of F1–F8 relevant to the `D4 → 16 → 8 → 0` gravitational branch.
- External mathematics: static spherically symmetric ansatz methods, geodesic equations, weak-field / post-Newtonian expansion, redshift and lensing formulae, discrete elliptic boundary-value methods if the solution is first built on the poset.

## Outputs
- Observable predictions: weak-field coefficients equivalent to $\beta$ and $\gamma$, light-deflection coefficient, perihelion-precession coefficient, and redshift law; target agreement with GR values to the highest order actually derived. If a horizon analogue exists, specify the $r_s$ relation.
- Structural theorems: existence of a static spherically symmetric event-poset solution; continuum Schwarzschild-analogue theorem under the assumptions of Paper XL.
- Additions to VFD Explorer library: `schwarzschild_poset.py`, `weak_field_observables.py`, `null_geodesic_vfd.py`.

## Key derivations needed
1. Formulate the symmetry-reduced event-poset ansatz corresponding to spherical symmetry and time independence.
2. Solve the VFD field-equation analogue in this ansatz, either exactly on the poset or asymptotically after refinement.
3. Extract the effective metric functions and compare them term-by-term to Schwarzschild in the large-scale limit.
4. Derive timelike and null geodesic observables: redshift, bending, perihelion shift, and any innermost stable orbit analogue.
5. Determine whether the horizon condition is topological, metric, or merely approximate in the discrete setting.
6. State the falsifiable deviations from GR, if any, at post-Newtonian order.

## Open questions / risks
- Static spherical symmetry may be difficult to define non-arbitrarily on the event poset before taking the continuum limit.
- The solution could reproduce Newtonian gravity but fail at the first post-Newtonian correction.
- Horizon language may be too smooth-manifold dependent for the discrete setting.
- If Paper XL only yields weak continuum control, the Schwarzschild analogue may remain formally suggestive rather than rigorous.

## Dependencies
- Blocked by: XL.
- Blocks: none.

## Estimated scope
- Rigor level: substantive
- Page count: 24–36
- Review rounds expected: 3–5
