**Referee Verdict**
No, not publication-ready yet on substantive-math/attribution scope. The paper is strong as a computational research note, but it repeatedly upgrades “template-residual signatures in a 2-second BETSE panel” into “morphogenetic basin / attractor” language. That is the main over-claim, especially because Paper 07 explicitly says the same 2-second BETSE substrate fails the closure-applicability diagnostic as “no emergence” / “target-only suffices” (`papers/07.../main.tex:157-158`).

**1. Claim Audit**
Line refs are to `papers/05-bioelectric-closure/main.tex`.

- “Which morphological attractor is the field heading toward” (`L33`, `L40`): not established. The paper shows lower residual against chosen voltage templates, not confirmed morphological attractor selection.
- `R_cl` five-term definition (`L60-80`): definition is clear, but “closed-form definitions are in docs/metric_definition.md” (`L80`) is not verifiable in this bundle; that file is absent.
- “Default weights … not fit to any dataset” (`L69`): important and plausible, but not proven by the manuscript. Needs a freeze/provenance statement or commit hash.
- Synthetic 81% vs 70% CV (`L138-151`): established only for the synthetic target-pull model. It does not support biological rescue/commitment, though `L155-158` correctly narrows the rescue interpretation.
- BETSE setup says “Conditions (4 total…20 runs)” (`L103`) but lists six conditions and later uses 30 runs. This is a hard internal inconsistency.
- Empirical-template LOO says “other 19 replicates” (`L128`), but the six-condition analysis uses 30 replicates and later correctly says “other 29” (`L414`).
- MW minimum p-value statement (`L132`) is correct for exact two-sided full separation at `n=5/5`, assuming no tie complications; but repeated `p=0.008` claims need the actual test table or correction discussion.
- K_env A/B result (`L162-180`) establishes differential residual shifts. It does not by itself establish a two-headed biological basin.
- “four-condition panel” (`L184`) conflicts with the “six-condition” table (`L187`) and five perturbation columns (`L205-211`).
- “Same signature within 10% magnitude” (`L233`, also table caption `L266-267`) is false for normal and failed templates: ratios are `0.67` and `1.95` (`L271-273`). Only the two-headed entry is within about 10%.
- Localized-depolarization claim (`L260`, `L349-362`): DiBAC A/P fluorescence ratio fails, but A-P voltage difference is rank 1 with `d=28.0`. Do not say closure “leads” over polarity scalars as a class.
- Sham calibration (`L283-297`) supports “not reducible to uniform mean shift alone” in this panel. It does not rule out all scalar or low-dimensional spatial baselines.
- Empirical templates (`L414-468`) support strong recovery for uniform depolarizers, but not general six-class basin identification: control/cl_env have zero recall and `na_mem_ant` is never predicted.
- LOO per-class caption says “one cross-mapping in each direction” (`L440`), but the table shows only `na_mem_glb -> k_env`; `k_env` has 5/5 correct (`L430`, `L433`).
- Leave-condition-out table (`L481-492`) omits a `na_mem_ant` prediction column even when `na_mem_ant` should be an available remaining template. The table is under-specified.
- Sensitivity section says “merged 3-class LOO” (`L499`) without defining the three classes; earlier merged analysis is 5-class (`L453-468`).
- Weight robustness (`L510-524`) does not include `na_mem_glb`, yet the abstract claims preservation “on every perturbed condition” (`L33`) and discussion says “four perturbed-condition signatures” (`L524`).
- Wet-lab preregistration (`L557-565`) is useful, but `t*` and the `<0.30` region need operational definitions in-paper. P5 is later declared underpowered and should be restated (`L583`), conflicting with the falsifier framing at `L47`.

**2. Internal Consistency**
Major conflicts: 4 vs 6 conditions (`L103`, `L184`, `L187`), 19 vs 29 LOO replicates (`L128`, `L414`), missing `na_mem_glb` in weight robustness (`L517-520`), missing `na_mem_ant` column in LCO (`L483-491`), and undefined merged 3-class sensitivity (`L499`). These must be fixed before review.

**3. External Programme Consistency**
Paper 03 frames SL-001 as the empirical realization of the Levin bridge and says `R_cl` operationalizes `C_phi^bio` (`papers/03.../main.tex:223-244`). Paper 05 instead says “independent of any meta-framework” (`L50`). That undersells the programme relation. Suggested replacement: “Operationally stand-alone; programme interpretation is conditional on H-RP-3 and the CAD applicability discipline.”

Paper 07 explicitly says “BETSE 2-sec bioelectric sims” fail as no-emergence / target-only suffices (`papers/07.../main.tex:157-158`) while Paper 05 says “basin-direction identification” no scalar can compete with (`L601`). This is the largest cross-paper conflict. Paper 05 should acknowledge: BETSE supports a template-residual engineering result; the wet-lab planarian test is the real CAD/Tier-A claim.

**4. Narrative Coherence**
The title says “In-Vivo Regeneration” (`L16`) but the paper has no in-vivo data. Use “for in-vivo regeneration” or “toward in-vivo regeneration.”

“real-physics voltage trajectories” (`L96`) is too strong. Use “biophysically parameterized BETSE trajectories.”

The paper should contain a short “Programme Position” box: SL-001 is the operational BETSE/wet-lab instantiation of Paper 03’s Levin bridge, not proof of the full closure framework.

**5. Tightness Edits**
- `L33`: “confirming basin-direction generalisation” -> “showing nearest-neighbour generalisation within this BETSE panel.”
- `L50`: replace meta-framework independence with conditional programme positioning.
- `L203`, `L267`: “within 10% on every template” -> “same sign pattern; two-headed residual within about 10%.”
- `L530`: “chemistry drives different morphological attractors” -> “perturbations produce different template-residual signatures.”
- `L601`: “no scalar baseline can compete with” -> “not represented by any single scalar baseline tested.”

**6. Surface Issues**
- Bibliography is broken in the release bundle: `\bibliography{refs}` (`L633`) but the file is `references.bib`.
- Referenced files `docs/metric_definition.md`, `docs/tier3_limits.md`, and `docs/wetlab_preregistration.md` are absent from this bundle (`L80`, `L551`, `L557`).
- Data/code commands only mention four conditions and omit `na_mem_ant`, `na_mem_glb` (`L615-619`).
- Mixed spelling/capitalization: localized/localised, depolarized/depolarised, K_env/`k_env`.

**7. Top Three Fixes**
1. Reconcile Paper 05 with Paper 07’s CAD verdict on 2-second BETSE (`L530-536`, `L601`; Paper 07 `L157-158`).
2. Fix condition-count, LOO/LCO, and weight-robustness inconsistencies (`L103`, `L128`, `L184`, `L481-492`, `L510-524`).
3. Add explicit programme positioning and companion citations to Paper 03 and Paper 07 (`L50`, `L555-565`).

**8. Programme-Strengthening Recommendations**
- Add a standard “status of evidence” label: synthetic demo / BETSE simulation / open-data real data / preregistered wet-lab prediction.
- Add a default-weight freeze ledger: weights, date, commit, and exactly which analyses used unchanged weights.
- Align all Solution Lab papers around CAD-D1-D5 language: when a substrate fails CAD, say so in the paper using it.
- Bundle reproducibility assets or remove claims that depend on absent docs/code.

**9. Publication Ready?**
No. It is close as a computational preprint, but publication-ready status requires narrowing “basin/attractor” language, fixing the internal inconsistencies, and explicitly aligning with Paper 07’s applicability diagnostic.

External check on `L552`: I found public planarian DiBAC protocol/article pages, not an obvious machine-readable time-series dataset in the quick search: [Oviedo et al. protocol](https://pmc.ncbi.nlm.nih.gov/articles/PMC10468776/) and [Durant et al. planarian bioelectric signals](https://pmc.ncbi.nlm.nih.gov/articles/PMC6401388/).
