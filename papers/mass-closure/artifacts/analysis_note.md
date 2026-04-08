# Minimal Model Analysis Note

## Results Summary

The minimal deterministic model was evaluated across 540 candidate states,
3 energy laws, 3 frequency laws, 3 amplitude laws, and 3 phase laws.

### Best result (optimal k = 5.73)

| Quantity | Predicted | Observed | Error |
|----------|-----------|----------|-------|
| mp/me | 1825.33 | 1836.15 | 0.59% |
| mn/mp | 1.000 | 1.00138 | 0.14% (trivial — see note) |

The mn/mp ratio of exactly 1.0 is a limitation: in the current model the
neutron and proton have identical energy because the torsional offset phases
do not affect the energy functional. The neutron-proton mass difference
requires either a phase-dependent energy term or a separate neutral-sector
correction. This is identified as the primary target for the next model iteration.

### Best result (structural k = phi^2 + 3 ≈ 5.618)

| Quantity | Predicted | Observed | Error |
|----------|-----------|----------|-------|
| mp/me | 1557.14 | 1836.15 | 15.2% |

The structural value produces the correct order of magnitude and correct
hierarchy but is 15% low. This suggests the clean phi-derived exponent is
close to but not exactly the right value.

## Analysis Questions

### 1. Which frequency law best preserves the observed hierarchy?

**Linear** (omega_n = n) performs best overall. Phi-scaled and closure-corrected
laws overshoot the ratio slightly. This is because linear frequencies weight
higher shells proportionally to their index, while phi-scaled frequencies
grow too fast and produce excessive high-shell energy.

### 2. Does phi-scaling help or hurt mp/me?

Phi-scaling in the **energy** functional is essential — the k ≈ 5.7 exponent
in phi^{kn} is what generates the ~1800x ratio from only 3 shells of difference.
Phi-scaling in the **frequency** law is less helpful and can overshoot.

### 3. Are the current particle-class assignments defensible?

**Yes, provisionally.** The electron at shell 1 (minimal) and proton at shells
2,3,4 (composite) produce the correct hierarchy. The assignment is rule-based:
leptons are minimal-shell, baryons are multi-shell composite starting at shell 2.

### 4. How should the neutron be modelled?

The current model cannot distinguish neutron from proton energetically because
the torsional phase offset does not enter the energy functional. Options:
- **Phase-dependent energy correction**: add a term coupling phase to energy
- **Symmetry-class energy shift**: assign a small energy offset to the neutral sector
- **Composite sub-structure correction**: model the neutron as proton + additional
  internal mode

The first option is most natural within the current framework.

### 5. Which term in the stability functional dominates?

The **closure defect D** dominates for states with non-zero phases. For
exact-closure states (all phases = 0), D = 0 and the spectral variance V
becomes the deciding factor. The torsion penalty T is small but nonzero
for all multi-shell states.

### 6. Does the energy functional need revision?

The functional E = sum a^2 * phi^{kn} * omega_n works well for the mp/me ratio.
The exponent k ≈ 5.7 is the key parameter. For the neutron-proton difference,
the energy functional needs a phase-coupling term.

## Go/No-Go Assessment

**GO — with caveats.**

The paper is now strong enough to proceed as a structural proposal because:
1. The hierarchy is reproduced (proton > electron by ~1800x)
2. The best model achieves 0.59% accuracy on mp/me
3. The model is deterministic and fully reproducible
4. The particle assignments are rule-based, not reverse-fit

Caveats:
- The optimal k = 5.73 is not a clean phi-derived value
- The structural k = phi^2 + 3 gives 15% error
- The neutron-proton difference is not yet resolved
- The model remains phenomenological — the exponent k is not derived

The paper should present both the structural and optimal k values honestly,
noting that the structural value produces the correct order of magnitude
while the numerical optimum achieves sub-1% agreement.
