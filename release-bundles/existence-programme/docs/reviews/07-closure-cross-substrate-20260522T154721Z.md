Line refs are to [Paper 07 main.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex) unless prefixed.

**Round 2 Status**
2.1 iff -> best-predicted-by: partly resolved. Lines 33, 40, 238 are mostly softened, but the boxed core claim still says “when, and only when” at L49, and the RNN/falsifier contradiction remains at L139, L144, L358.

2.2 strict-PASS vs PASS-leaning: not resolved. L75 defines PASS-leaning as four of five criteria with one near miss; trait anxiety fails two criteria, with `D2=0` and `D3=0.64`, yet is counted as PASS/PASS-leaning at L200, L207. L214’s strict audit also conflicts with the table.

2.3 headline triples: mostly resolved. Source `d_z=2.07`, `t=7.76`, `p=3.1e-6` at L124 and sensor `d_z=1.43`, `t=5.35`, `p=1.3e-4` at L129 are arithmetically coherent. The row-count part of 2.3 is still unresolved: L174/L211 say `8 + 3 = 11`, but the table lists 12 paired rows if read literally.

2.4 mood ledger: not resolved. Mood `ds004315` appears in the two-statistic table at L317 and in false-negative discussion at L216, but is absent from the 14/15 ledger and has no setup/citation in Paper 07.

**1. Claim Audit**
- “Closure-as-distance” as an L2 proxy, L33 and L58-L62: established as a definition. The paper correctly says it is not the full closure operator at L33, L44, L341.
- “Measurable approximation to the closure operator,” L33: acceptable only as a modelling bridge. It is not proved from the formal closure operator.
- “Best predicted to dominate scalar single-axis baselines,” L33/L40/L238: plausible as an empirical calibration claim, but not fully established because the RNN CAD-FAIL rows dominate the stated baselines at L139 and L144.
- “when, and only when,” L49: not established and contradicted by the RNN rows. This Round 1 blocker remains.
- “All eight tested substrates correctly; with controls 11/11,” L33/L174/L211: not cleanly established. The table’s paired rows do not match the stated accounting.
- “14 of 15,” L33/L174/L213: not yet honest enough. It depends on inclusive PASS-leaning treatment and excludes the mood false negative despite later mentioning it.
- Diagnostic thresholds D1-D5, L68-L77: defined, but empirical and post-hoc-calibrated. “A priori” is justified for the post-draft runs if logs exist, not for the original calibration set.
- PASS-leaning definition, L75: internally valid in isolation, but not applied consistently to trait anxiety or cardiac AF.
- Unpaired extension, L81-L85: under-specified and notation-confused. `\delta_j` is indexed as if `j` were a target subject while also using feature notation.
- D6, L87: useful as an exploratory criterion, but the “too strict” conclusion rests on very few cohorts.
- Constraint-manifold “tight iff,” L95: not proved. Centroid approximation tightness needs manifold-radius/curvature/metric assumptions. Effective rank alone is not sufficient.
- `sqrt(k_eff)` advantage, L95: not established by the cited source result because closure `d_z=2.07` is slightly below best single feature `d_z=2.11`; only stability improves.
- Power curve, L99-L111: supports “at source-EEG effect strength,” not a general minimum `n`.
- Source EEG result, L120-L126: numerically coherent after repair and broadly supported by Paper 06 L331. But “dominates baselines” should distinguish source baseline, sensor baseline, full feature space, and LOSO subset.
- Sensor EEG, L129: repaired triple is coherent. Jaccard `0.64` is below the discovery-stability threshold used elsewhere, so it should be called weaker/boundary.
- Clinical `ds004541`, L132: matches Paper 06’s in-sample `7/7`, `d_z=1.98`, and honestly reports LOSO `6/7`, `d_z=1.16`.
- RNN claims, L139/L144: empirical numbers are clear, but they contradict the claim that CAD-FAIL substrates do not dominate scalar baselines. Calling them Tier B is fine; using them as MATCH requires a better matched-complexity baseline.
- BETSE, L158: overstates relative to Paper 05. Paper 05 claims a narrow basin-direction contribution, not that the regime is wholly “structurally inappropriate.”
- Negative controls, L164-L166: support rejection. But high D4 values in noise rows show D4 cannot itself be read as “mechanism complementarity.”
- FTD reconciliation, L261-L269: valuable and honest as a false positive, but L269 overstates. The diagnostic did not identify the failure mode; post-hoc boundary analysis did.
- Feature-transfer, L271 and L367: “methodology and discovery procedure transfer universally” is too strong. The fixed subset fails on anxiety (`d=0.22`), so the supported claim is “pipeline reused without retuning; feature subsets are substrate-specific.”
- External validations, L283-L303: properly not used as evidence, but “pre-registered” should be reserved for timestamped external preregistration or cited local prereg docs.
- Two-statistic section, L307-L335: promising, but under-methoded. Mood appears without ledger/citation, anaesthesia `d_z=2.16` is not reconciled with L124, and `n>=80` at L333 needs an explicit power calculation.

**2. Internal Consistency**
- L49 conflicts with L139/L144 and L358.
- L75 conflicts with L200/L207 and L214.
- L33 says Tier B substrates “do not dominate” baselines; L139/L144 say both RNN rows do.
- L174/L211 say 11 paired cases; the table visually presents 12 paired rows.
- L214’s “cardiac AF PASS_LEANING” conflicts with table L188, where AF fails both D1 and D5.
- L216 says false negatives are zero, while mood is acknowledged as a possible D6/diagnostic false negative and appears at L317.
- L353 says one confirmed Tier A substrate; L33 calls trait anxiety a second confirming PASS. Clarify strict Tier A vs unpaired PASS-leaning.

**3. External Consistency**
- Paper 06: original SL-002 numbers match Paper 06 L33 and L225-L263; Paper 06 L331 supports the LOSO `d_z=2.07`, Jaccard `1.00` cross-validated cousin. Good.
- Paper 08: anxiety `d=+0.79`, `t=1.93`, `p=0.07` matches Paper 08 L100-L102. But Paper 08 calls it PASS-leaning/boundary and reports mood `ds004315` as a diagnostic false negative at L126-L130 and L195. Paper 07 must sync.
- Paper 10: musical `ds007471` numbers match Paper 10 L117-L123. Paper 07’s scope correction at L230 is good. L255 should use the same narrower wording: this contrast/proxy fails, not music or joint meaning generally.
- Paper 02: dyscoherence definition at L223 matches Paper 02 L432-L435. Music ensemble is explicitly listed as a joint-meaning case in Paper 02 L719, so Paper 07 is right to avoid generalising the musical null.
- Paper 05: Paper 07 undersells SL-001. Paper 05 L530-L536 and L601 claim a limited basin-direction advantage; Paper 07 L158 should not dismiss the whole framework for BETSE.
- Bibliography: L223 cites `SmartLifeAsClosure`, but Paper 07’s `references.bib` lacks that key. The cite-key repair is incomplete.

**4. Narrative Coherence**
The paper’s best role in the programme is as the versioned CAD boundary paper: it tells Papers 06, 08, 09, and 10 when an L2 empirical proxy is licensed. That framing coheres with the programme. The narrative breaks when it tries to be both a strict diagnostic validation and an inclusive boundary ledger. The programme would read as one body of work if this paper separated: strict paired CAD-v1 validation, unpaired CAD-v1 boundary tests, and exploratory two-statistic extensions.

**5. Tightness Edits**
- L49: replace with “Closure-as-distance is best predicted to be useful when the substrate’s transition is distributed across multiple complementary causal channels.”
- L33: replace “Tier B substrates ... do not dominate” with “Tier B substrates expose calibration boundaries; some dominate simple baselines but not matched structural baselines.”
- L75: define strict PASS, PASS-leaning, and inclusive PASS in separate terms.
- L95: replace “tight iff” with “expected to be most accurate when.”
- L158: replace “structurally inappropriate” with “not a clean CAD-v1 test of emergent multistability over this 2-second regime.”
- L207: replace “D2/D3 marginal” with “D3 marginal; D2 strict-fail but treated as unpaired-design boundary.”
- L269: replace “the diagnostic correctly identifies” with “the boundary analysis identifies.”
- L333: replace the `n>=80` expectation with “a larger cohort should test whether Hotelling’s T2 crosses significance.”
- L367: replace “transfers universally” with “has transferred across the tested EEG applications without parameter retuning.”

**6. Surface Issues**
- Missing `SmartLifeAsClosure` bibliography key.
- `PASS$^{*}$` at L182 has no `*` footnote.
- `\subsubsection*` plus `\label{sec:ftd-boundary}` at L259 will not give a reliable numbered reference; use `\phantomsection` or an unstarred heading.
- Unpaired delta notation at L81-L84 should be subject-indexed vector notation.
- Mood `ds004315` at L317 needs setup, citation, and ledger decision.
- “Scalar baseline” is used for a seven-dimensional baseline vector at L126.
- Repository org is inconsistent across the programme (`vfd-aria` here, `vfd-org` elsewhere).
- Data sources for climate/PhysioNet/RNN scripts need clearer citations or artifact pointers.

**7. Top Three Fixes**
1. Fix the CAD ledger: L75, L174, L200, L207, L211-L217, L214, L317. Separate strict PASS, PASS-leaning, false positives, false negatives, and out-of-ledger exploratory cases.
2. Remove the remaining iff/universal language and reconcile RNN dominance with the core claim and falsifier: L33, L49, L139, L144, L358, L367.
3. Align companion-paper attribution: add `SmartLifeAsClosure`, soften BETSE at L158, sync Paper 08 mood/anxiety status, and keep musical-joint-action scoped to this dataset/proxy/contrast.

**8. Programme-Strengthening Recommendations**
- Make Paper 07 the canonical CAD ledger with columns for substrate, design, prediction timestamp, strict verdict, inclusive verdict, empirical effect, p-value, companion paper, and status.
- Split paired CAD-v1 from unpaired CAD-v1.x. The unpaired cases should be calibration evidence, not counted as equally mature validation.
- Add a companion concordance table linking each row to Papers 05, 06, 08, and 10.
- Standardise the programme sentence: “empirical proxy, not operator; licensed by CAD; phenomenological readings conditional on P-A.”
- Require every empirical PASS to state both effect-size threshold status and significance status.

**9. Publication Ready?**
No. The source/sensor headline triples are repaired, and the FTD discussion is useful, but the paper is not publication-ready on substantive math/attribution scope until the CAD ledger, PASS-leaning rules, RNN contradiction, mood accounting, and companion-paper alignment are fixed.
