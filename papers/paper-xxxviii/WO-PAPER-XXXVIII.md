# WO-PAPER-XXXVIII — Individual Quark Masses from the Cascade

## Programme Position
The mass core already succeeds for composites, but the programme still lacks a clean derivation of the six individual quark masses. This paper determines whether confinement-compatible constituent structure can be reconciled with PDG quark mass conventions without breaking the zero-parameter framework.

## Scope
- Define how confined quark degrees of freedom are represented within the existing spectral/closure scheme.
- Derive masses for `u,d,s,c,b,t` in a way that distinguishes pole, constituent, and $\overline{\mathrm{MS}}$ notions rather than conflating them.
- Explain why hadron-level successes in Papers I–V and XXXII do or do not lift to quark-level observables.
- State the renormalisation-scale convention explicitly and map VFD quantities to PDG reporting standards.
- Test whether the same integer-selection/cascade machinery suffices or whether an extra confinement-to-parton matching layer is required.

## Inputs
- Prior papers: I–V (mass-core equations and particle eigenvalue assignments); VI–XI (SM interpretation, confinement analogy, translation dictionary); XXII (spectral bridge and integer selection); XXXII (hadron charge radii / coherence lengths); XXXV (synthesis and catalogue).
- Cascade foundations: all rung-map and selection-rule components needed to identify quark-sector states, especially the `H4 → 40 → D4` reduction and coupling-matched normalisation.
- External mathematics: renormalisation-group running for quark masses, constituent-versus-current mass matching, spectral perturbation methods, heavy-quark effective theory conventions for `c,b,t`.

## Outputs
- Observable predictions: $m_u(2\,\mathrm{GeV})$, $m_d(2\,\mathrm{GeV})$, $m_s(2\,\mathrm{GeV})$, $m_c(m_c)$, $m_b(m_b)$, and either $m_t(m_t)$ or pole-mass equivalent; target agreement against PDG central values within the smallest defensible error bands the method supports.
- Structural theorems: confinement-compatible quark-state assignment theorem; mapping theorem from VFD mass eigenvalues to PDG running-mass conventions.
- Additions to VFD Explorer library: `quark_mass_map.py`, `rg_match_quarks.py`, `constituent_current_bridge.py`.

## Key derivations needed
1. Identify the quark-sector eigenmodes in the cascade and show why they were invisible or only composite-accessible in the published mass core.
2. Derive a mass functional that survives confinement, specifying whether it is a bare spectral value, a closure-renormalised value, or a coherence-length inverse.
3. Construct the dictionary between VFD internal mass values and PDG running masses, including scale choice and scheme conversion.
4. Show how colour/confinement structure from Papers VI–XI modifies or protects the individual-mass assignment.
5. Treat the top quark separately, since its weak decay precedes hadronisation and may be the cleanest test of the framework.
6. Check consistency against hadron masses already fitted in Papers I–V, so the quark-level derivation does not spoil earlier composite success.

## Open questions / risks
- Current-quark masses are scheme-dependent; a theory that naturally produces constituent-like masses may not map cleanly to PDG $\overline{\mathrm{MS}}$ values.
- The light-quark sector may be underdetermined because confinement smears the very notion of an isolated mass eigenvalue.
- Any mismatch between individual quark masses and previously successful hadron fits will be highly visible.
- The top sector could work while the light sector fails, leaving only a partial success.

## Dependencies
- Blocked by: XXXVI.
- Blocks: XXXIX.

## Estimated scope
- Rigor level: substantive
- Page count: 25–40
- Review rounds expected: 3–5
