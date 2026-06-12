Line refs are to `papers/07-closure-cross-substrate/main.tex` unless prefixed.

**1. Claim Audit**

- “Closure-as-distance” as an L2 norm proxy is established as a definition by lines 58-62. The paper correctly says it is not the closure operator itself at lines 33, 44, 340.
- “Dominates scalar single-axis baselines iff...” at lines 33, 40, 49, 237, 366 is not established. It is contradicted by RNN rows where CAD fails but closure beats the stated baseline: single-objective RNN `d_z=3.40` vs `0.64` at line 139; multi-objective RNN `3.99` vs `0.41` at line 144.
- “A substrate passes iff all five criteria are satisfied” at line 75 is contradicted by trait anxiety: table reports `D2=0`, `D3=0.64`, but classifies PASS at lines 200 and 207.
- “14/15 correctly classified” at lines 33, 174, 211-213 is not cleanly established. The table contains more rows than the accounting admits, anxiety is only PASS by post-hoc “PASS-leaning,” and the mood case at line 316 is included later but absent from the classification ledger.
- Source EEG anchor is broadly consistent with SL-002 for the original in-sample results: Paper06 lines 33, 225-263. But Paper07’s LOSO line 124 has incompatible `d_z=2.07`, `t=7.00`, `p=3.1e-6`; for `n=14`, these numbers cannot all be true.
- Sensor EEG line 129 has a similar internal mismatch: `d_z=1.43` would imply `t≈5.35`, not `6.83`; the reported `p=1.3e-4` also does not match `t=6.83`, df=13.
- Clinical `ds004541` line 132 matches Paper06’s headline `7/7`, `d_z=1.98` claim, but Paper07’s primary LOSO result is `6/7`, `d_z=1.16`; this is fine if clearly marked as a new stricter reanalysis.
- Constraint-manifold “tight iff” and `sqrt(k_eff)` advantage at line 95 are not proved. Worse, the cited empirical comparison is `2.07` vs best single feature `2.11`, so the predicted effect-size advantage is absent; only stability improves.
- Negative controls at lines 164-167 support rejection, but high `D4` values in the table for noise rows show that `D4` alone cannot mean “mechanism complementarity.”
- BETSE claim at line 158 overstates the companion paper. Paper05 argues for a narrow basin-direction advantage, not “structurally inappropriate”; see Paper05 lines 33, 391-409, 601.
- FTD false positive is honestly reported at lines 203, 260-268. The characterization is useful, but line 268 overstates: the diagnostic did not “correctly identify” the issue; the post-hoc boundary analysis did.
- Two-statistic section lines 306-334 is valuable but under-integrated. Mood `ds004315` appears at line 316 without entering the 14/15 accounting or citations; Paper08 treats mood as a diagnostic false negative at Paper08 lines 124-130 and 195.

**2. Internal Consistency**

- Main conflict: all-five gate at line 75 vs PASS-leaning anxiety at lines 200, 207.
- Accounting conflict: “8 original + 3 controls = 11” at line 174, but the table lists 9 original paired rows plus 3 controls.
- Falsifier conflict: line 357 says failed diagnostic plus `>=3x` closure dominance means diagnostic is too conservative; RNN rows already satisfy this at lines 139 and 144.
- Notation issue: unpaired `\delta_j` at lines 81-84 uses `j` as target subject while also saying `j=1,...,n_tgt`; this should be a subject-indexed vector, not a feature-indexed scalar.
- “One empirically-confirmed Tier A substrate” at line 352 conflicts with “trait-anxiety ... second confirming PASS” at line 33 unless Tier A is reserved for paired designs.

**3. External Consistency**

- SL-002: mostly consistent. Paper06 supports the original `14/14`, `d_z=1.90`, source `d_z=2.60`, clinical `7/7`, `d_z=1.98` claims.
- Life as Closure: dyscoherence definition matches Paper02 lines 430-435. But Paper07 cites `SmartExistenceClosure` at line 222 where it should cite `SmartLifeClosure`.
- SL-005/Paper08: anxiety result matches Paper08 lines 98-106 and 150. But Paper08 adds mood manipulation as a false negative for the diagnostic at lines 124-130 and 195, which undermines Paper07’s “false negatives: 0” at line 215.
- SL-007/Paper10: musical hyperscanning numbers match Paper10 lines 117-123. But the sentence at line 229 should not imply musical joint-action is not joint meaning in general; Paper02 explicitly lists music ensemble as a joint-meaning example at Paper02 lines 716-718. The correct scope is this dataset/proxy/contrast.
- SL-001/Paper05: Paper07’s dismissal of 2-second BETSE at line 158 conflicts with Paper05’s own claim of a narrow but real basin-direction contribution.

**4. Narrative Coherence**

The paper’s best programme role is as the boundary-methods paper: “when is an L2 closure proxy licensed?” That coheres well with Papers06, 08, and 10. The weak spots are vocabulary drift and ledger drift. Use the programme discipline explicitly: proxy not operator, empirical bridge scoped by CAD, phenomenological readings conditional on P-A, and cosmic claims absent.

Specific tightening:
- Line 229: replace “musical joint-action does not satisfy joint-meaning’s multi-channel condition” with “this musical synchronisation contrast does not license the dyadic L2 proxy.”
- Line 230: replace “scopes Life as Closure’s implicit claim” with “scopes this paper’s cortical proxy for dyscoherence.”
- Line 270/366: “transfers universally” is too strong; say “has transferred in the tested EEG cases, while feature subsets remain substrate-specific.”

**5. Tightness Edits**

- Lines 33/40/237: replace “if and only if” / “exactly when” with “in the present validation set, is best predicted by.”
- Line 75: add “strict CAD-v1 pass” and keep PASS-leaning cases out of the main accuracy count.
- Line 139/144: either report best-single-feature baselines or stop saying Tier B empirically does not dominate baselines.
- Line 268: “The FTD miss exposes an unpaired-design calibration gap” instead of “the diagnostic correctly identifies this.”
- Line 332: replace `n >= 80` expectation with “a larger cohort may test whether Hotelling’s T2 crosses significance.”

**6. Surface Issues**

- `\bibliography{refs}` at line 371 is broken in this bundle; file is `references.bib`.
- Table line 182 has `PASS$^{*}$` but no `*` footnote.
- `\subsubsection*` with `\label{sec:ftd-boundary}` at line 258 will not create a reliable numbered reference. Use unstarred heading or `\phantomsection`.
- Mood `ds004315` at line 316 lacks setup, citation, and accounting.
- Several numerical triplets need recomputation: lines 124 and 129 especially.
- The title says “Validated Across Paired and Unpaired Substrates” at line 16; given unpaired recalibration failures, “Tested Across...” is safer.

**7. Top Three Fixes**

1. Fix the diagnostic ledger: strict CAD-v1 vs PASS-leaning, table row count, mood inclusion, and false-negative count. Lines 75, 174, 200, 207, 211-216, 316, 354.
2. Remove the iff/exactly/universal language and reconcile RNN dominance with the core claim and falsifier. Lines 33, 40, 49, 139, 144, 237, 357, 366.
3. Align cross-paper attributions: cite Life as Closure correctly, soften BETSE dismissal, and scope musical/dementia statements to this proxy. Lines 158, 222, 229-230.

**8. Programme-Strengthening Recommendations**

- Make Paper07 the canonical versioned CAD ledger: substrate, design, prediction timestamp, strict CAD result, empirical metric, companion paper, classification.
- Add a shared cross-paper wording block: “first-order empirical proxy, not operator; licensed by CAD; P-A only for phenomenological readings.”
- Split paired CAD-v1 and unpaired CAD-v1 clearly. The current unpaired cases are calibration data, not a mature validation set.
- Add a companion-paper concordance table linking Paper07 rows to Papers05, 06, 08, and 10.
- Distinguish “method transfer” from “minimal feature transfer” throughout.

**9. Publication Ready?**

No. The core methodological idea is promising, and the FTD false positive is usefully characterized, but the paper is not publication-ready on substantive math/attribution scope until the CAD accounting, numerical inconsistencies, RNN contradiction, and companion-paper alignment are fixed. Overclaiming is currently the main risk.
