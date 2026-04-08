# Exact Invariant Analysis — Honest Assessment

## Summary

15 candidate exact closure-class invariants were evaluated against the
observed proton-to-electron mass ratio mp/me = 1836.15267343.

## Key Finding

The observed ratio satisfies:

    mp/me ≈ phi^(14 + phi) = phi^(15.618...) = 1836.44

to 0.015% accuracy. This is a striking numerical relationship.

The exponent 14 + phi decomposes as:

    14 = prod(shells_p) - sum(shells_p) - 1 = 24 - 9 - 1
    phi = the golden ratio (from the manifold structure)

where the proton occupies shells {2, 3, 4}.

For the electron at shell {1}:

    C(electron) = prod - sum - 1 = 1 - 1 - 1 = -1

So C(proton) - C(electron) = 14 - (-1) = 15.

## The Cancellation Problem

If the mass invariant is defined as I(A) = phi^(C(A) + phi), then in the
ratio the +phi terms cancel:

    mp/me = phi^(C_p + phi) / phi^(C_e + phi) = phi^(C_p - C_e) = phi^15

phi^15 = 1364.0, which is 25.7% below the observed value.

The 0.015% accuracy of phi^(14+phi) arises only if:
- the invariant is phi^(C(A) + phi) evaluated ABSOLUTELY, not as a ratio
- a universal calibration constant Lambda maps both masses to the SAME
  reference, and the phi correction does NOT cancel

This means the mass law would be:

    m_k = Lambda * phi^(C(A_k) + phi)

with Lambda calibrated once (e.g., against the electron mass), and the
proton mass then PREDICTED as:

    m_p = m_e * phi^(C_p - C_e) * [phi^(C_p + phi) / phi^(C_e + phi)]
        = m_e * phi^15

This gives phi^15 = 1364, not 1836.

## Resolution: The Ratio Is Not a Pure Phi Power

The observed mp/me = 1836.15 is NOT a clean power of phi. Specifically:

    log_phi(1836.15) = 15.618

This is not an integer, not a half-integer, and not a simple phi-expression
when taken as a ratio exponent.

## What the Framework CAN Do

The framework produces:
1. The correct HIERARCHY (proton >> electron) from shell structure
2. The correct ORDER OF MAGNITUDE (~10^3) from phi-scaling
3. A structural exponent (C_p - C_e = 15) that is within ~25% of reality

## What the Framework CANNOT Yet Do

1. Derive the exact ratio without an adjustable exponent
2. Explain why the correction from phi^15 to 1836.15 has the specific
   value it does
3. Resolve the neutron-proton mass difference

## Assessment: OUTCOME B

A strong shortlist of structural invariant candidates exists, with exact
derivation still incomplete. The framework is structurally viable but not
yet sufficient for an exact ratio claim.

### Best candidates (ranked by structural quality):

1. **I06: Sum of phi^(n^2)** — gives 1415 (23% error). Structurally clean:
   each shell contributes phi^(n^2) to the closure energy. No fitted parameters.

2. **Combinatorial exponent phi^(prod-sum-1)** — gives phi^15 = 1364 (26% error)
   as a ratio, or phi^(14+phi) = 1836.4 (0.015% error) as an absolute.
   The absolute form is numerically excellent but the phi-in-exponent
   creates an interpretation problem for ratios.

3. **I09: Product of n*phi^n** — gives 1127 (39% error). Each shell
   contributes its index times its phi-weight multiplicatively.

## Recommendation for Paper II

1. Present the framework as a structural proposal that reproduces the
   correct hierarchy and order of magnitude from exact shell combinatorics.

2. Note the phi^(14+phi) = 1836.4 relationship as a numerically striking
   observation (0.015% accuracy) but DO NOT claim it as a derived result
   unless the absolute-vs-ratio interpretation issue is resolved.

3. Present I06 (sum of phi^(n^2)) and the combinatorial exponent C(A)
   as the strongest structural candidates.

4. Be explicit that the exact ratio derivation is incomplete and that
   the remaining ~25% discrepancy (for ratio-based invariants) represents
   missing structure — possibly inter-shell coupling, boundary effects,
   or a correction from the detailed closure dynamics.

5. Frame the paper as: "the framework identifies the structural origin
   of the mass hierarchy and constrains the ratio to the correct order
   of magnitude; an exact derivation remains an open problem."

## Evaluation Questions (Direct Answers)

1. **What distinguishes proton from electron?** Shell occupancy complexity:
   {2,3,4} vs {1}. The combinatorial invariant C = prod-sum-1 captures this.

2. **Can phi enter without being manually inserted?** Yes — it enters
   through the phi-structured manifold. The exponent is a pure integer
   derived from shell combinatorics.

3. **What drives the ratio?** Primarily shell depth (phi^n scaling) and
   composite multiplicity. The exponent C_p - C_e = 15 is combinatorial.

4. **Is there an exact candidate in the right range?** I06 gives 1415
   (right range, 23% error). phi^(14+phi) gives 1836.4 (0.015% error)
   but has an interpretation issue.

5. **What structure is missing?** The ~25% gap for ratio-based invariants
   likely reflects inter-shell coupling or detailed closure-cycle corrections
   not captured by the additive/multiplicative invariants tested.

6. **Neutron-proton splitting?** Cannot be addressed by the current
   invariant candidates — it requires phase-dependent or symmetry-class
   corrections not yet formalised.
