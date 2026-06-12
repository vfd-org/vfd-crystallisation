**Verdict**

Publication-ready on empirical-proxy framing: close. Publication-ready on substantive math/attribution scope: **no**.

The main blocker is the RNN/ledger logic. The 16-case arithmetic is internally countable, but the paper counts the RNN rows as `MATCH` even though they satisfy the paper’s own falsifier for a CAD-FAIL substrate whose closure statistic dominates baselines by `>=3x`. That needs to be resolved before publication.

**1. Claim Audit**

- “closure-as-distance … empirical first-order proxy … not … the formal closure operator” [L33](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:33>), repeated at [L44](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:44>) and [L342](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:342>): established by framing, not proof. This is appropriately bounded.

- “all nine paired-design tested substrates … 12/12 … 15 of 16” [L33](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:33>): arithmetic is consistent only under the paper’s current inclusion rule: 3 Tier A + 4 Tier B + 2 Tier C + 3 controls + 4 post-draft rows = 16, with one FTD miss. But it depends on excluding mood as CAD-v1.5 addendum [L216](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:216>) and counting RNN rows as matches.

- “PASS-leaning” rule [L75](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:75>): anxiety is applied consistently as PASS-leaning; AF is correctly FAIL because `D5=1.00` exceeds tolerance. The rule itself is empirical and post-calibrated, not theorem-grade.

- “predicted closure-over-single-axis advantage scales as sqrt(k_eff)” and source EEG “matches this prediction” [L95](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:95>): not established as written. The cited comparison is `d_z=2.07` vs best-single `d_z=2.11`, i.e. no effect-size advantage. The actual supported claim is stability/Jaccard advantage, not effect-size advantage.

- EEG anchor numbers [L124](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:124>): established internally as reported. The 5.5x attribution is clarified at [L126](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:126>) and [L368](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:368>): it is full-feature in-sample source closure `2.58/0.47`, not LOSO two-feature closure.

- RNN rows [L139](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:139>), [L144](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:144>): the data show CAD-FAIL but raw closure/baseline dominance of `5.3x` and about `9.7x`. That contradicts the falsifier at [L359](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:359>) unless “dominates” is redefined to require feature-set stability too.

- FTD explanation [L262-L270](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:262>): plausible as a boundary case, but the sentence “diagnostic correctly identifies this as the open calibration question” [L270](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:270>) is too strong. The diagnostic predicted PASS and was wrong; the post-hoc analysis identifies the calibration issue.

**2. Internal Consistency**

- [L52](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:52>) says “eight-substrate paired-design validation”; table and abstract say nine paired substrates. Fix to nine.

- [L40](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:40>) says “only one cleanly satisfies” while Table has three Tier A paired rows. Say “one substrate family: anaesthesia EEG.”

- Unpaired notation at [L81-L85](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:81>) reuses `j` as subject index after using it as feature index. Use `i` for target subjects and `j` for features.

- The table caption claims RNN classification matches “single-feature wins for stability” [L174](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:174>), but the table does not report RNN Jaccard or single-feature stability evidence.

**3. External Consistency**

- SL-002 anaesthesia numbers match Paper 06: `14/14`, `t=7.11`, `d_z=1.90`, source `t=9.72`, `d_z=2.60`, clinical `7/7`, `d_z=1.98` are consistent with Paper 06 [L33](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/06-cortical-phase-closure/main.tex:33>).

- Paper 06 still says the methodology paper reports `14/15` and `11 paired-design substrates` [L337](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/06-cortical-phase-closure/main.tex:337>). That is stale relative to Paper 07’s `15/16`.

- Paper 06 also attributes `~5.5x` to the LOSO two-feature result [L331](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/06-cortical-phase-closure/main.tex:331>), while Paper 07 now clarifies `5.5x` is full-feature in-sample. Update Paper 06 or cite `~4.4x` for `2.07/0.47`.

- Life-as-Closure dyscoherence is accurately matched: Paper 02 defines `D_I(v)=||v-P_Sigma(v)||` [L430-L435](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/02-life-as-closure/main.tex:430>). Paper 07 should say “closure-stable subspace,” not “self-model subspace,” unless that phrase is deliberately imported.

- The music/joint-meaning scope is accurate: Paper 02 lists music ensemble as a joint-meaning case [L716-L718](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/02-life-as-closure/main.tex:716>) and separately records ds007471 as honest negative [L735-L739](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/02-life-as-closure/main.tex:735>).

**4. Narrative Coherence**

The paper mostly now speaks the programme’s disciplined language: proxy, applicability diagnostic, scoped empirical bridge, no direct validation of formal operator. The remaining narrative problem is over-universal wording.

- [L272](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:272>) says “methodology and discovery procedure are universal”; this conflicts with the bounded framing at [L341](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:341>). Use “transferred across the tested EEG cases without retuning.”

- [L277](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:277>) says “Closure-as-distance measures basin transitions…” Better: “In the present validation set, closure-as-distance detects basin-transition structure…”

**5. Tightness Edits**

- [L95](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:95>): replace “matches this prediction” with “does not show an effect-size advantage over the best single feature; its advantage here is stable feature discovery.”

- [L174](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:174>): replace RNN `MATCH` language with “CAD-v1.5 calibration mismatch on raw effect size; interpretive FAIL on multi-channel license.”

- [L359](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:359>): either keep the falsifier and stop counting RNN as MATCH, or add stability to the falsifier.

**6. Surface Issues**

- Broken LaTeX: `\\S\ref{sec:results}` at [L33](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:33>) should be `\S\ref{sec:results}`.

- Undefined table footnote: `PASS$^{*}$` at [L182](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:182>) has no `*` note.

- Missing bibliography keys: Paper 07 cites `SolutionLab005` [L216](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:216>) and `SmartLifeAsClosure` [L224](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:224>), but `references.bib` has no entries for them.

- “D5 may exceed by <=0.10 in standardised units” [L75](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:75>): D5 is a fraction, not a standardised unit.

**7. Top Three Fixes**

1. Fix the RNN/falsifier/ledger contradiction at [L139](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:139>), [L174](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:174>), [L359](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:359>). This is the publication blocker.

2. Recast the `sqrt(k_eff)` claim at [L95](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:95>) as heuristic, since the source-EEG comparison does not show the claimed effect-size advantage.

3. Qualify the `15/16` headline wherever it appears: “main ledger excluding CAD-v1.5 addenda such as mood; RNN raw-effect dominance treated as calibration-boundary.” See [L33](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:33>), [L213-L216](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:213>), [L368](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:368>).

**8. Programme-Strengthening Recommendations**

- Add a shared programme convention for empirical ledgers: core ledger, calibration-boundary addenda, exploratory addenda, and excluded known false negatives should be named identically across Papers 02, 06, 07, 08, and 10.

- Create a small cross-paper “current empirical record” table and reuse it verbatim. Paper 06 is currently stale relative to Paper 07.

- Standardise proxy notation: formal `D_I`, formal `delta_AB`, empirical `CCR`, empirical `\widehat{\delta}_{AB}^{EEG}`, and Paper 07’s `closure-as-distance` should be visibly separated in every paper.

- Add a programme-wide rule that “PASS” means either effect-size threshold or statistical significance, not both ambiguously. Anxiety is `d=+0.79` but `p=0.07`; that is fine if PASS is effect-threshold PASS, but the rule should be explicit.

**9. Publication Ready?**

**No.** The paper is close, and the Round-5 fixes have improved the empirical-proxy discipline. But the RNN rows currently make the central `15/16` claim too brittle: under the stated falsifier, they are not clean MATCH rows. Fix that accounting and the `sqrt(k_eff)` overclaim, then the paper can plausibly be publication-ready on substantive scope.
