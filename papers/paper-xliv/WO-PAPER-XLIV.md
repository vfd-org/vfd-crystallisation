# WO-PAPER-XLIV — Information Rung and Decoherence as $H_4 \to \mathrm{Cl}(1,3)$ Coarsening

## Programme Position
This paper turns decoherence from an external interpretive add-on into an explicit cross-rung process. It is the information-theoretic counterpart to the observer / measurement line, explaining how $120 \to 16$ coarse-graining produces effectively classical Lorentzian information channels.

## Scope
- Define the information rung as a controlled coarsening map from $H_4$ structure to $\mathrm{Cl}(1,3)$ degrees of freedom.
- Show how decoherence appears as loss of fine $H_4$ phase / closure information under this cross-rung map.
- Connect this to the Born-rule and measurement papers so that decoherence, probability, and sector separation are mutually consistent.
- Identify whether the resulting reduced dynamics is Lindblad-like, only approximately CP, or structurally different.
- Produce at least one concrete reduced-state or entropy-growth calculation.

## Inputs
- Prior papers: XV–XXI (QM recovery from closure dynamics); XXVIII (shared (E,F,G) substrate); XXIX (observer localisation); XXX (Born rule from Kähler-uniqueness + Gleason); XXXI (measurement as sector separation); XXXIII (universal measurement principle); XXXV (synthesis); XXXVII if neutrino-sector structure informs $H_4$ state counting; XLII ($\delta U_{\mathrm{rel}}$ physical status).
- Cascade foundations: XXXVI / F1–F8 for the $E_8 \to H_4$ and downstream $\to 16$ mapping, including admissible projection / coarsening operators.
- External mathematics: Clifford algebra $\mathrm{Cl}(1,3)$, quantum channels, Stinespring / Kraus / Lindblad frameworks, relative entropy monotonicity, Petz recovery as a test of lost versus recoverable information.

## Outputs
- Observable predictions: decoherence-rate scaling laws or channel-structure constraints for specific experimental architectures if derivable; otherwise "none — structural paper."
- Structural theorems: cross-rung coarsening theorem $H_4 \to \mathrm{Cl}(1,3)$; decoherence-as-coarse-graining theorem; compatibility theorem with Born / Gleason uniqueness.
- Additions to VFD Explorer library: `h4_to_cl13_channel.py`, `decoherence_cross_rung.py`, `petz_recovery_test.py`.

## Key derivations needed
1. Define the coarsening functor / operator from $H_4$ state data to $\mathrm{Cl}(1,3)$ observables or channels.
2. Show which $H_4$ invariants survive the map and which are irretrievably discarded, linking the latter to decoherence.
3. Derive the reduced dynamics on the coarse-grained side and test whether it has Lindblad form, approximate Lindblad form, or a distinct VFD signature.
4. Connect the coarse-grained probabilities to Paper XXX's Kähler / Gleason derivation so the information rung does not conflict with Born recovery.
5. Use Petz-style recoverability criteria to characterise when cross-rung loss is effective decoherence versus merely hidden information.
6. Work at least one explicit toy model through the full $120 \to 16$ reduction.

## Open questions / risks
- The proposed $H_4 \to \mathrm{Cl}(1,3)$ map may be non-unique, undermining the information-rung claim.
- Complete positivity or semigroup structure may fail, making contact with standard decoherence theory awkward.
- The paper may end up highly structural with no direct measurable rates.
- If $\delta U_{\mathrm{rel}}$ is physical, it may contaminate the reduced dynamics and complicate interpretation.

## Dependencies
- Blocked by: XXXVI, XXXVII, XLII.
- Blocks: XLV.

## Estimated scope
- Rigor level: substantive
- Page count: 24–38
- Review rounds expected: 3–5
