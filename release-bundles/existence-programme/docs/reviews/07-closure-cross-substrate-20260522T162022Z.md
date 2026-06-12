Line refs are to `papers/07-closure-cross-substrate/main.tex`.

**Bottom Line**
No, not publication-ready yet. Round 4 resolves the narrow anxiety-rule blocker: the PASS-leaning rule at line 75 now does classify anxiety as PASS-leaning. It also removes the old hard “iff” language and updates the conclusion to `15/16`. But the paper still has substantive ledger, attribution, and claim-tightness problems.

**1. Claim Audit**
- Line 33: “measurable approximation to the closure operator” is still too strong. The paper defines an `L^2` empirical proxy, not an approximation to `C_\varphi` itself. Use “proxy for distance to a closure-stable reference basin.”
- Line 33: “all eight tested substrates” conflicts with the table arithmetic immediately given: `3 Tier A + 4 Tier B + 2 Tier C = 9`, plus 3 controls = 12.
- Line 33: “Tier B substrates ... empirically do not dominate single-axis baselines” is false for the RNN rows: closure dominates baseline at lines 139 and 144.
- Line 40: “nine tested substrates” is correct; it conflicts with lines 33, 52, and 355 saying “eight.”
- Line 42: SL-002 numbers match Paper 06: sensor `14/14`, `t=7.11`, `d_z=1.90`; source `t=9.72`, `d_z=2.60`; clinical `7/7`, `d_z=1.98`; LOSO `d_z=2.07` matches Paper 06’s companion-methodology statement.
- Line 49: boxed core claim is mostly acceptable as an empirical calibration claim, but still needs RNN-qualified wording because CAD-FAIL RNN cases dominate raw simple baselines.
- Line 75: PASS-leaning rule now does classify anxiety as PASS-leaning. Round-3 blocker resolved in the rule itself.
- Line 75 vs line 214: unresolved contradiction. Line 75 says cardiac AF does *not* satisfy PASS-leaning; line 214 says the strict audit gives cardiac AF `PASS_LEANING`.
- Line 87: `D_6` is useful, but “too strict” is only established in this small current cohort set, not generally.
- Line 95: “tightest” is safer than “iff,” but still not proved. The centroid approximation needs manifold radius/curvature/metric assumptions.
- Line 95: `sqrt(k_eff)` effect-size advantage is not established by the cited source EEG result: closure `d_z=2.07` is slightly below best single feature `d_z=2.11`; the observed advantage is stability, not effect size.
- Lines 99-111: power curve supports “minimum `n=7` at source-EEG anaesthesia effect strength,” not a general cohort-size rule. Line 111 correctly qualifies this.
- Line 126 vs line 368: `5.5x` dominance uses full-feature in-sample closure `2.58 / 0.47`, not LOSO `2.07 / 0.47`. The conclusion currently attaches `5.5x` to the LOSO/two-feature result.
- Lines 139, 144, 174, 211, 359: RNN rows still create a claim problem. The paper says CAD-FAIL + closure dominance by `>=3x` means the diagnostic is too conservative, but the RNN rows do exactly that and are counted as MATCH.
- Line 158: BETSE is overcompressed and partly inconsistent with Paper 05. Paper 05 says target-only recovers “most” structural claims and raw 6-class LOO is `0.43`, merged 5-class `0.63`; Paper 07 says “all structural claims” and “80% ... six-class accuracy.”
- Line 207/254: anxiety should be called strict-fail on `D_2` but within the new tolerance, not simply “marginal” on `D_2/D_3`.
- Line 216: mood accounting is honest, but `SolutionLab005` is missing from this paper’s bibliography.
- Line 262: “15-case classification record” is stale; the table ledger is 16 cases.
- Line 270: “the diagnostic correctly identifies this as the open calibration question” overstates. The diagnostic predicted FTD PASS; the post-hoc boundary analysis identifies the failure mode.
- Line 272: “methodology and discovery procedure are universal” is too strong from one anxiety transfer test. Say “transferred in the tested EEG applications without retuning.”
- Line 334: `n >= 80` per arm for Hotelling significance is not derived in text.
- Line 368: `15/16` is now corrected, but the same sentence overstates anxiety as clean “PASS” rather than PASS-leaning.

**2. Internal Consistency**
- Row-count conflict remains: lines 33/52/355 say eight original paired substrates; lines 40/174/211 imply nine non-control paired rows and 12 paired rows including controls.
- Strict/PASS-leaning split is inconsistent: line 75 excludes cardiac AF; line 214 includes it.
- RNN rows are simultaneously “MATCH,” “CAD-FAIL,” and raw effect-size dominance cases. The paper needs separate columns for effect-size dominance, stability dominance, and interpretation license.
- Table line 182 has `PASS^{*}` but no `*` footnote.
- Line 308 says four post-draft real-data EEG cohorts plus SL-002, but Table 2 includes mood and excludes musical hyperscanning; call these “four cortical real-data cohorts,” not the same four Table 1 rows.

**3. External Consistency**
- Paper 06: SL-002 and `ds004541` numerical claims match.
- Paper 08: anxiety `d=+0.79`, `t=1.93`, `p=0.07` matches; mood `ds004315` `d=+0.70`, `p=0.018` matches. But Paper 08 treats mood as a diagnostic false negative, while Paper 07 excludes it from the main ledger. That convention must be stated programme-wide.
- Paper 10: musical `ds007471` numbers match. But Paper 10 now also reports `ds006802` collaborative learning as a moderate-positive trend with diagnostic FAIL; Paper 07 should say whether `ds006802` is excluded from the CAD ledger and why.
- Paper 05: Paper 07 undersells and overstates BETSE at once. Match Paper 05’s wording: operationally useful but not closure-necessary on the 2-second substrate.
- Paper 01 still has old `14/15` programme-ledger language at several places; Paper 07 now says `15/16`. The programme map needs synchronization.

**4. Narrative Coherence**
The paper’s role is coherent: it should be the canonical CAD boundary paper for Papers 06, 08, 09, and 10. The narrative weakens when it slides from “proxy licensed by CAD” into “closure measures basin transitions” at lines 277 and 368. Use “closure-as-distance is supported as a proxy for...” instead.

**5. Tightness Edits**
- Line 33: “measurable proxy for distance to a closure-stable reference basin.”
- Line 33: “Tier B substrates expose CAD-v1 calibration boundaries; some dominate simple baselines but not the licensed multi-channel interpretation.”
- Line 75/214: make cardiac AF status consistent.
- Line 95: “expected to be most useful when...”; move `sqrt(k_eff)` to conjecture unless derived.
- Line 158: “target-only recovers most structural claims; closure is operationally useful but not closure-necessary in this 2-second regime.”
- Line 262: “16-case classification record.”
- Line 368: “anxiety PASS-leaning / empirical PASS.”

**6. Surface Issues**
- Missing bibliography keys: `SmartLifeAsClosure`, `SolutionLab005`.
- `src/strict_vs_passleaning_audit.py` is referenced, but I do not see it in this release bundle.
- `\subsubsection*{...}\label{sec:ftd-boundary}` may not create a reliable hyperlink target; use `\phantomsection` or an unstarred heading.
- Lines 81-84: unpaired notation uses `\delta_j` for target subjects while `j` elsewhere denotes feature index. Use subject index `i`.
- `PASS^{*}` lacks a footnote.
- `ds004504` should be consistently `\texttt{ds004504}`.

**7. Top Three Fixes**
1. Fix the CAD ledger and strict/PASS-leaning accounting: lines 33, 52, 75, 174, 211-216, 262, 355.
2. Resolve the RNN contradiction with the core claim and falsifier: lines 139, 144, 174, 211, 359.
3. Tighten theoretical overclaims: line 95 `sqrt(k_eff)` / “tightest,” line 277 “measures,” line 368 `5.5x` attached to LOSO.

**8. Programme-Strengthening Recommendations**
- Make Paper 07 the canonical ledger with columns: substrate, companion paper, design, strict CAD verdict, PASS-leaning verdict, empirical effect, stability result, ledger status.
- Split paired CAD-v1 validation from unpaired CAD-v1.5 calibration evidence.
- Add explicit ledger status for mood `ds004315` and collaborative learning `ds006802`.
- Standardize the programme sentence: “empirical proxy, not operator; licensed by CAD-D1--D5-v1; phenomenological readings conditional on P-A.”

**9. Publication Ready?**
No. Round-3 anxiety and conclusion blockers are partly resolved, and the constraint-manifold “iff” is softened. But the ledger is still internally inconsistent, RNN cases still contradict the stated diagnostic/falsifier logic, and several companion-paper attributions need tightening before publication.
