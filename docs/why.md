# `vfd why <prediction_id>`

Explain a prediction: method, dependencies, current primitive
values, experimental comparison, and co-dependents.

## What it does

Given a registered prediction id, the walker reads the registry,
follows the dependency graph, resolves the current runtime value of
each primitive, and prints a human-readable trace.

Use it when:

- A reader asks "how did you get 0.8412?"
- You change a primitive and want to see the immediate effect on a
  specific prediction.
- You're writing a paper and need the derivation chain for the
  methodology section.

## Example

```
$ vfd why proton_charge_radius

Prediction:   Proton charge radius r_p
Paper:        WO-PROTON-RADIUS
Method:       r_p = Tr(L(P_3)) × λ̄_p = 4 × λ̄_p

Depends on:
  shell:proton
    description:   Canonical proton shell support {2, 3, 4}
    current value: (2, 3, 4)
    source:        vfd_core.shells.assignment.SHELL_ASSIGNMENTS
  constant:LBAR_P
    description:   Reduced Compton wavelength of the proton (fm)
    current value: 0.2103089102724652
    source:        vfd_core.constants.LBAR_P

Result:
  VFD value:    0.8412356410898608 fm
  Experimental: 0.8409 ± 0.0004 fm  (source: PDG 2022)
  Rel. error:   0.0399%
  σ-margin:     0.84
  Status:       PASS (tolerance 0.1%)

Co-dependents (other predictions sharing a primitive):
  - G_E_proton_at_Q2_0p05
  - G_E_proton_at_Q2_0p1
  - G_E_slope_radius_consistency
  - deuteron_charge_radius
  - kaon_charge_radius
  - pion_charge_radius
  - proton_electron_mass_ratio
  - proton_magnetic_radius
```

## Notes

- **Current primitive values** are resolved at call time, not
  pre-computed. If you've patched a constant in your session, `vfd
  why` reflects the patched value.
- **Shell primitives** dereference the specific particle rather than
  dumping the whole `SHELL_ASSIGNMENTS` map.
- **Derived primitives** (eigenvalue multiplicities from the
  600-cell, Hopf-fiber structure, etc.) show `<derived / external>`
  — they aren't single attributes on a module, they come out of a
  computation.
- **Co-dependents** are other predictions that share *any* primitive
  with the target. This answers "who else moves if this primitive
  moves?" without needing a separate perturbation run.
