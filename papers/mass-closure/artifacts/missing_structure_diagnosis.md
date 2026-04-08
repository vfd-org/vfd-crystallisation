# Missing Structure Diagnosis

## Summary

The correction beyond phi^15 CANNOT be derived from the current formalism.
phi^(1/phi) does NOT emerge from any currently defined operator.

## The 14/15 tension is a bookkeeping artifact.
The ratio is phi^15 regardless of absolute calibration.

## Missing structures (in priority order):

### MS1: Manifold metric / Laplacian eigenvalues
**Why needed:** The energy functional E[Psi] depends on how the phi-manifold weights different shells. Without an explicit metric, the energy scaling exponent k is a free parameter.

**Gap:** The paper defines the shell hierarchy phi^{-n} but does not define the inner product or Laplacian on the manifold. The Laplacian eigenvalues would determine k.

**Fix:** Define the natural Riemannian metric on the phi-structured manifold and compute its Laplacian spectrum. The energy functional then follows from the quadratic form.

### MS2: Linearized closure operator / Jacobian of C
**Why needed:** The spectral radius of the linearized C at fixed points is a legitimate class invariant that could provide the correction factor.

**Gap:** The closure operator C is defined but its derivative (Jacobian DC) is not computed. The spectral properties of DC at closure-fixed-points are unknown.

**Fix:** Compute the Jacobian of C at each closure-class representative and extract the spectral radius.

### MS3: Boundary-aware closure operator
**Why needed:** Shell 1 (electron) is the boundary; shells 2+ are interior. The current operator treats them equally.

**Gap:** No formal distinction between boundary and interior shells in the closure operator or stability functional.

**Fix:** Introduce boundary-shell weights in the closure operator, justified by the shell's coupling to the exterior.

### MS4: Energy normalization convention (sum vs average vs weighted)
**Why needed:** The energy is currently a sum over shells. Whether mass scales with total content or average density is undetermined.

**Gap:** The energy functional's normalization is a convention, not derived from the manifold structure.

**Fix:** Derive the normalization from the manifold's volume element or from the closure-cycle integral.

