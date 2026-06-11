# WO-PAPER-XXXIX — W, Z, and Higgs from Closure Geometry

## Programme Position
This paper supplies the missing mechanism behind the already-published electroweak numerology, especially $\sin^2\theta_W = 3/8$. It must show how W, Z, and Higgs observables arise from closure geometry rather than being only interpreted after the fact.

## Scope
- Derive electroweak symmetry breaking analogues from sector separation / closure geometry rather than assuming the standard Higgs mechanism verbatim.
- Produce $m_W$, $m_Z$, and $m_H$ from cascade-fixed quantities with no new free parameters.
- Reinterpret the Weinberg angle as a closure-geometry invariant and connect it to the spectral bridge integer structure.
- Clarify whether the Higgs is a genuine scalar excitation, a closure modulus, or an effective bound-state descriptor in VFD language.
- State which electroweak observables are in scope now and which are deferred, especially widths and couplings.

## Inputs
- Prior papers: VI–XI (SM interpretation and Weinberg-angle discussion); XII–XIV (closure dynamics); XXII (spectral bridge and $\sin^2\theta_W = 3/8$); XXXI (measurement as dynamical sector separation); XXXIII (universal measurement principle); XXXV (synthesis).
- Cascade foundations: the full cascade normalisation and integer-selection statements from F1–F8, especially the rung where electroweak sector data are anchored.
- External mathematics: spontaneous-symmetry-breaking geometry, constrained Hessian analysis, mass-matrix diagonalisation, gauge-boson mixing formalism, effective-field-theory matching if needed.

## Outputs
- Observable predictions: $m_W$, $m_Z$, $m_H$, $\sin^2\theta_W$, and if feasible $\Gamma_W$, $\Gamma_Z$; target comparison to PDG world averages with ppm-to-$10^{-4}$ ambition for angle-level quantities and realistic sub-percent ambition for masses unless the derivation is stronger.
- Structural theorems: closure-mass theorem for vector bosons; scalar-mode theorem identifying the Higgs analogue; invariant-angle theorem connecting electroweak mixing to cascade spectral geometry.
- Additions to VFD Explorer library: `ew_closure_geometry.py`, `wzh_mass_predict.py`, `weinberg_invariant.py`.

## Key derivations needed
1. Write the effective closure operator whose small fluctuations produce a neutral/charged vector-boson mass matrix and a scalar mode.
2. Derive the mixing angle from geometry, showing why $\sin^2\theta_W = 3/8$ is an intrinsic invariant rather than an inserted GUT-style relation.
3. Compute the vector-boson eigenmasses after sector separation, including the analogue of the $W^3/B$ mixing construction in VFD notation.
4. Identify the Higgs-like mode as a radial, modulus, or closure-defect excitation and derive its mass scale from the same structure.
5. Demonstrate compatibility with the $\alpha^{-1} = 137 + \pi/87$ bridge so electroweak masses and couplings are not overconstrained inconsistently.
6. Compare the resulting observables to PDG values and state precisely what deviations would falsify the mechanism.

## Open questions / risks
- The framework may recover the angle but not the actual mass scales without an extra normalisation input.
- The Higgs sector could emerge only as an effective parameterisation, not a true derived excitation.
- There is a real danger of circularity if the same empirical quantities used in coupling matching are reused as "predictions."
- Precision electroweak observables may reveal that the geometric mechanism is too coarse.

## Dependencies
- Blocked by: XXXVI, XXXVII, XXXVIII.
- Blocks: XLII.

## Estimated scope
- Rigor level: substantive
- Page count: 28–42
- Review rounds expected: 3–5
