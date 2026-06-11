# WO-PAPER-XXXVII — Neutrino Sector in H4

## Programme Position
The H4 mass assignment in Papers I–V uses eigenvalues {9,12,14,15} to cover 13 particles, but neutrinos are currently absent from the assignment. This paper identifies where the three neutrinos sit in the 600-cell spectrum, or establishes that they require an extension to the existing framework, and derives their mass ordering and absolute scale (if any can be derived).

## Scope
- Locate ν_e, ν_μ, ν_τ within the H4 eigenvalue structure — as sub-shells, missing-eigenvalue interpretations, or an extended spectrum requiring justification from F1–F8.
- Derive neutrino mass ordering (normal / inverted) or show the framework is agnostic.
- Derive the sum of neutrino masses Σm_ν if accessible, for comparison to cosmological bounds (<0.12 eV).
- State whether the Dirac vs Majorana nature is fixed by the cascade structure.
- Connect to PMNS mixing if mixing angles are derivable from cascade geometry.

## Inputs
- Prior papers: I–V (mass core, shell logic, particle assignment); III (600-cell spectrum eigenvalues); VI–XI (SM translation); XXII (integer selection, generations from Z_3 Hopf).
- Cascade foundations: F1–F3 (cascade structure), F4–F5 (rung-to-observable mappings), particularly what constrains admissible sectors within H4.
- External mathematics: H4 representation theory, sub-lattice / sub-shell decomposition, Clifford algebra irreps for fermion generations.

## Outputs
- Observable predictions: neutrino mass ordering; Σm_ν bound or value; PMNS mixing angles (θ_12, θ_23, θ_13, δ_CP) if derivable, with comparison to T2K / NOvA / JUNO data.
- Structural theorems: neutrino-sector placement theorem within the 600-cell; no-go results for any ordering excluded by the cascade.
- Additions to VFD Explorer library: `neutrino_sector.py`, `pmns_mixing.py` (if applicable).

## Key derivations needed
1. Identify candidate eigenvalue slots in H4 consistent with the existing {9,12,14,15} assignment plus the Z_3 generational action.
2. Show whether the candidate slots accommodate three nearly-massless states ordered normally or invertedly, or whether massless neutrinos require a distinct mechanism (e.g., vanishing projection onto the mass operator).
3. Derive mixing via basis rotation between the flavour basis (PMNS) and the mass basis, if the Z_3 Hopf action supplies the basis change.
4. Connect to Paper XXII's α⁻¹ derivation so that electroweak consistency is preserved.
5. State the falsifiable prediction: which ordering is excluded, what Σm_ν range the framework predicts, and how a measured lightest mass would support or reject the placement.

## Open questions / risks
- H4's eigenvalue structure may not naturally accommodate nearly-massless states; a small-parameter mechanism may be needed.
- Majorana vs Dirac may be left as an external input rather than derived.
- The PMNS matrix has complex phases (δ_CP) that may not fit cleanly into the Z_3 action.
- If neutrinos require a rung beyond H4 (e.g., a coupling to the information rung Cl(1,3) as a decoherence channel), the paper's scope expands.

## Dependencies
- Blocked by: XXXVI (cascade foundations).
- Blocks: XXXIX (W/Z/H derivation needs the full matter content), XLIV (information rung may couple to neutrino sector).

## Estimated scope
- Rigor level: substantive
- Page count: 22–35
- Review rounds expected: 3–5
