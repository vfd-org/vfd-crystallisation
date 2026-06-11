OpenAI Codex v0.124.0 (research preview)
--------
workdir: /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
model: gpt-5.5
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019dddc7-ee04-7031-8f7e-50285f0ca741
--------
user
ROUND 8 FINAL CONFIRMATION on aria-chess paper at /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/.

Round 7 verdict was 'Publication ready: no' citing ONE issue: the phrase "substrate's $S^{3}$ state space" was line-wrapped across §9:147-148, so the single-line grep missed it. The text was correct; the wrap was cosmetic.

That has now been fixed. §9:148 should now contain the full phrase on a single line:

  148:substrate's $S^{3}$ state space.

Round 7 (b) explicitly stated: "No substantive over-claim, scope-drift, or numerical inconsistency found in the requested sweep."

Verify the reflow with:

  grep -nF '$S^{3}$ state space' sections/09_limitations.tex

You should see ONE match on line 148. If yes, the paper has cleared all round-1 through round-7 must-fixes.

Final discipline check on the paper:
- Substrate witness, not selection theorem, not consciousness derivation, not 600-cell uniqueness.
- 18/18 = methodology refinement, no threshold change.
- 6/6 v4 EEG signatures literature-thresholded.
- C×P 0/2000 at-or-below-zero, reported as 0.0000.
- Chess +40.6pp at n=25 with reset; P10 disclosed at 15-vs-prereg-20 perms.
- HCP -11.58σ / +79.78σ (raw PR with node-count caveat) / +6.80σ (with inferred sd).
- ACT bridge non-load-bearing.

Output ONLY:
(a) Reflow grep PASS/FAIL with the matched line.
(b) Up to 3 substantive issues (file:line each, terse), or "none" if clean.
(c) Final verdict: 'Publication ready: yes' or 'Publication ready: no — must-fix list'.

Be terse. Total response under 150 words. Do not lift whole files.

warning: Codex could not find bubblewrap on PATH. Install bubblewrap with your OS package manager. See the sandbox prerequisites: https://developers.openai.com/codex/concepts/sandboxing#prerequisites. Codex will use the vendored bubblewrap in the meantime.
exec
/bin/bash -lc "rg -n \"selection theorem|consciousness derivation|600-cell uniqueness|substrate witness|substrate's \\\\"'$S'"\\"'^'"\\{3\\}\\\\"'$ state space" sections' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc "grep -nF '"'$S''^{3}$ state space'"' sections/09_limitations.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc "rg -n \"18/18|methodology refinement|threshold change|threshold|6/6|v4|EEG|0/2000|0\\.0000|40\\.6|n=25|reset|P10|15-vs-prereg-20|perms|11\\.58|79\\.78|6\\.80|ACT|load-bearing|load bearing\" sections" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
 succeeded in 206ms:
148:substrate's $S^{3}$ state space. The latter is computationally

 succeeded in 245ms:
sections/03_substrate.tex:116:average degree, not a fitted threshold. No other shape parameter
sections/06_stress_tests.tex:9:$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
sections/06_stress_tests.tex:12:threshold required (a) re-evaluating the $N\!=\!3$ point estimate as
sections/06_stress_tests.tex:99:\item $0/2000$ bootstrap resamples were at or below zero, reported as
sections/06_stress_tests.tex:100:      $0.0000$;
sections/06_stress_tests.tex:101:\item $0/2000$ bootstrap resamples were below the preregistered
sections/06_stress_tests.tex:102:      $+0.10$ floor, reported as $0.0000$.
sections/06_stress_tests.tex:113:threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
sections/06_stress_tests.tex:114:at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
sections/06_stress_tests.tex:115:were below the preregistered $+0.10$ floor, reported as $0.0000$.
sections/06_stress_tests.tex:160:at the preregistered threshold; P3 ($D\times C$) closed at $N\!=\!5$.
sections/06_stress_tests.tex:163:higher $N$ without threshold modification. The general lesson: when
sections/01_introduction.tex:13:benchmark on real EEG data tested here. The structure-driven
sections/01_introduction.tex:31:drug/sleep EEG signatures.
sections/01_introduction.tex:38:2026-04-18) and six companion drug/sleep EEG signatures of
sections/01_introduction.tex:55:  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
sections/01_introduction.tex:66:  $17/18$ at standard methodology; $18/18$ after a documented
sections/01_introduction.tex:68:  test; \emph{no preregistered threshold has been modified}.
sections/01_introduction.tex:71:  (chess $+40.6$pp leave-one-out lift at depth $n\!=\!25$ ticks;
sections/01_introduction.tex:75:  $n\!=\!1003$: ARIA at $-11.58\sigma$ on degree homogeneity;
sections/01_introduction.tex:76:  $+79.78\sigma$ on raw participation ratio with the node-count caveat
sections/01_introduction.tex:98:  non-load-bearing here. We do not deliver a Lyapunov function on the
sections/01_introduction.tex:125:\;=\;\{\text{`consistent with', `inside threshold', `direction confirmed'}\}.
sections/01_introduction.tex:128:A result that lands inside its preregistered threshold licenses a
sections/01_introduction.tex:130:threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
sections/01_introduction.tex:133:(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
sections/01_introduction.tex:142:\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
sections/01_introduction.tex:156:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
sections/01_introduction.tex:167:discusses the substrate witness and proposes a non-load-bearing
sections/01_introduction.tex:168:ACT bridge (without claiming a selection theorem).
sections/02_method.tex:7:the validation script, the seed range, the threshold, and the
sections/02_method.tex:17:falsifiable threshold, (iii) the validation test (script + seed range),
sections/02_method.tex:24:not include those batteries in the headline 18/18 tally.} They are
sections/02_method.tex:27:\textbf{Six EEG signatures (set B).} The drug/sleep signatures on the
sections/02_method.tex:28:recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six companion
sections/02_method.tex:29:biological signatures with literature-derived thresholds (NREM-N3
sections/02_method.tex:36:\textbf{No threshold has been modified post-hoc.} Where the original
sections/02_method.tex:42:(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
sections/02_method.tex:44:preregistered threshold.
sections/02_method.tex:50:\text{threshold}, \text{result})$.
sections/02_method.tex:66:P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
sections/02_method.tex:70:P10 (chess null) & \texttt{run\_chess\_robustness.py} & 30210 & same & $\geq 50\%$ \\
sections/02_method.tex:72:P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
sections/02_method.tex:73:\textbf{P13 (chess sub.\ lift)} & same & with reset & same (LOO refinement) & $\geq +15$pp \\
sections/02_method.tex:80:Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
sections/02_method.tex:95:consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
sections/02_method.tex:101:EEG~\citep{OpenNeuroDS004902},
sections/02_method.tex:103:psychedelic-state reference; not load-bearing for the headline tally.
sections/02_method.tex:105:\textbf{Zenodo \texttt{3992359}.} DMT EEG public
sections/02_method.tex:118:signature (Sig~3) follows the EEG microstate methodology lineage of
sections/02_method.tex:145:deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
sections/02_method.tex:146:$0/2000$ were below the preregistered floor $+0.10$; we report these
sections/02_method.tex:147:as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
sections/02_method.tex:163:\subsection{State-reset protocol}
sections/02_method.tex:169:explicit reset between successive evaluations.
sections/02_method.tex:170:\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
sections/02_method.tex:172:canonical baseline. With reset between depth measurements, the chess
sections/02_method.tex:173:LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
sections/02_method.tex:174:substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
sections/02_method.tex:175:preregistered floor). The reset protocol is documented in
sections/02_method.tex:179:state-reset protocol.
sections/02_method.tex:187:  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
sections/02_method.tex:201:verdicts (CI overlaps, $P$-value thresholds) are unaffected.
sections/05_results.tex:6:gives the six drug/sleep EEG signatures on the recurrent layer
sections/05_results.tex:10:$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
sections/05_results.tex:27:\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
sections/05_results.tex:58:   EEG microstate~\citep{Brodbeck2012Microstates} &
sections/05_results.tex:75:All six signatures pass against their literature-derived thresholds
sections/05_results.tex:78:thresholds are drawn from the literature (Sleep-EDFx CI for
sections/05_results.tex:82:recurrent-layer architecture redesigned at v4 with
sections/05_results.tex:85:documents the v3$\to$v4 stimulus redesign). The mechanistic readings
sections/05_results.tex:87:load-bearing for the headline claim. Single-seed disclosure:
sections/05_results.tex:94:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
sections/05_results.tex:96:$32000$--$32019$). \emph{No preregistered threshold has been modified.}
sections/05_results.tex:113:P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
sections/05_results.tex:117:P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
sections/05_results.tex:119:P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
sections/05_results.tex:120:\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
sections/05_results.tex:124:P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
sections/05_results.tex:131:estimator as $5$-fold CV at threshold $\geq +15$pp; the 2026-04-29
sections/05_results.tex:132:validation tightened the estimator to LOO with state reset, a
sections/05_results.tex:133:disclosed estimator/protocol refinement at the unchanged $+15$pp threshold. See
sections/05_results.tex:137:methodology refinement (no threshold change).}
sections/05_results.tex:143:\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
sections/05_results.tex:149:  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
sections/05_results.tex:150:  validation strengthened the estimator to LOO with state reset, a
sections/05_results.tex:151:  disclosed estimator/protocol refinement at the same threshold; the LOO lift was $+3.1$pp
sections/05_results.tex:152:  without state reset on a state-drifted substrate, and $+40.6$pp
sections/05_results.tex:153:  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
sections/05_results.tex:160:all pass at preregistered thresholds, with two interaction tests
sections/05_results.tex:163:requiring the documented state-reset protocol. The original $15/18$
sections/05_results.tex:182:Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
sections/05_results.tex:184:\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
sections/05_results.tex:189:The v4 WAKE 95\% CI $[1.82, 2.86]$ contains the upper arm of the
sections/05_results.tex:190:real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
sections/05_results.tex:207:(noting that the v4 WAKE CI is from a single deterministic trajectory
sections/08_discussion.tex:7:a re-statement of an earlier theory, and proposes a non-load-bearing
sections/08_discussion.tex:8:ACT bridge to the companion adaptive-closure-transport
sections/08_discussion.tex:18:  real-cortex EEG signatures without fitted shape parameters on neural
sections/08_discussion.tex:26:  literature-derived thresholds on a single deterministic substrate.
sections/08_discussion.tex:39:\item \textbf{The 18/18 preregistered correspondences with no
sections/08_discussion.tex:40:  threshold modification.} Every prediction in the preregistered set
sections/08_discussion.tex:41:  passes at the preregistered thresholds. The two interaction tests
sections/08_discussion.tex:43:  one test (P13) required the documented state-reset protocol. We
sections/08_discussion.tex:44:  report this transparently as methodology refinement, not as
sections/08_discussion.tex:45:  threshold change.
sections/08_discussion.tex:84:\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
sections/08_discussion.tex:92:$D_{\mathrm{ACT}}$:
sections/08_discussion.tex:94:D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
sections/08_discussion.tex:97:   \ \texttt{homeostatic\_reset}).
sections/08_discussion.tex:99:\textbf{This bridge is non-load-bearing for the present paper.} It is
sections/08_discussion.tex:101:witness claims (six signatures, $18/18$, chess $+40.6$pp,
sections/08_discussion.tex:102:HCP $\sigma$-distances) do not require any of the ACT theorems.
sections/08_discussion.tex:104:\textbf{What ACT would have to deliver to make this load-bearing.}
sections/08_discussion.tex:119:\emph{substrate witness} for the family that ACT names; ACT is not the
sections/08_discussion.tex:154:  reliable detection at the preregistered threshold. The general
sections/08_discussion.tex:160:\item \textbf{State-reset protocol on non-stationary substrates.}
sections/08_discussion.tex:163:  Any multi-trial benchmark must specify a state-reset protocol or
sections/08_discussion.tex:166:  an explicit reset/equilibration discipline}, not just seed.
sections/08_discussion.tex:204:  EEG cohort (TUH, NHM)?
sections/07_cross_domain.tex:30:measurements the substrate is reset to canonical state via
sections/07_cross_domain.tex:31:\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
sections/07_cross_domain.tex:38:\caption{Chess substrate-routed depth sweep with state reset between
sections/07_cross_domain.tex:58:\caption{Chess preregistered tests (with reset, $n=25$ canonical
sections/07_cross_domain.tex:66:P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
sections/07_cross_domain.tex:68:P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
sections/07_cross_domain.tex:69:\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
sections/07_cross_domain.tex:76:conversation''). We split it for table clarity into P10 (chess null)
sections/07_cross_domain.tex:80:(\texttt{run\_preregistered\_validation.py}; the $\geq 50\%$ threshold
sections/07_cross_domain.tex:82:a threshold change; the observed $65.4\%$ at $15$ perms sits well
sections/07_cross_domain.tex:88:substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
sections/07_cross_domain.tex:90:reset; we report the LOO finding ($+40.6$pp) above as a disclosed
sections/07_cross_domain.tex:91:estimator/protocol refinement at the unchanged $+15$pp threshold,
sections/07_cross_domain.tex:96:chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
sections/07_cross_domain.tex:97:This is a $+40.6$pp lift on the LOO refinement; on the preregistered
sections/07_cross_domain.tex:101:$+3.1$pp, a state-drift artefact closed by the reset protocol
sections/07_cross_domain.tex:105:mapping (P10) randomises the feature$\to$frame assignment, so each
sections/07_cross_domain.tex:134:P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
sections/07_cross_domain.tex:145:$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
sections/07_cross_domain.tex:161:connectivity matrix; thresholded at the same density as ARIA's
sections/07_cross_domain.tex:179:Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
sections/07_cross_domain.tex:180:Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
sections/07_cross_domain.tex:181:Clustering coefficient (descriptive)$^{\flat}$ & $0.455$ & $0.220$ & $+6.80\sigma$ \\
sections/07_cross_domain.tex:188:\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
sections/07_cross_domain.tex:191:$\approx 0.235/6.80\!\approx\!0.035$. We carry the $\sigma$-distance
sections/07_cross_domain.tex:196:  $0.0000$, $\checkmark$.
sections/07_cross_domain.tex:207:fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
sections/07_cross_domain.tex:208:homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
sections/07_cross_domain.tex:210:density-matched threshold $\rho = 0.101$; cross-parcellation
sections/07_cross_domain.tex:221:across-subject distribution, but the $+79.78\sigma$ value reflects
sections/07_cross_domain.tex:256:Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
sections/07_cross_domain.tex:267:$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
sections/04_consciousness_chain.tex:6:cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
sections/04_consciousness_chain.tex:47:\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
sections/04_consciousness_chain.tex:124:Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
sections/04_consciousness_chain.tex:149:The v4 stimulus models were redesigned after diagnostics on the
sections/04_consciousness_chain.tex:157:the v3$\to$v4 redesign). The full stimulus code is
sections/04_consciousness_chain.tex:158:\texttt{demo\_drug\_sleep\_v4.py}.
sections/04_consciousness_chain.tex:181:(above threshold but not yet crossed) emit pressure at $30\%$ scale,
sections/10_conclusion.tex:10:drug/sleep EEG signatures of conscious vs unconscious states. Once
sections/10_conclusion.tex:21:drug/sleep EEG signatures pass against their literature-derived
sections/10_conclusion.tex:22:thresholds (Sleep-EDFx CI, OpenNeuro \texttt{ds005620}, Brodbeck 2012,
sections/10_conclusion.tex:30:overlaps the real Sleep-EDFx EEG
sections/10_conclusion.tex:36:preregistered thresholds, with two interaction tests requiring
sections/10_conclusion.tex:39:the documented \texttt{homeostatic\_reset} state-reset protocol. No
sections/10_conclusion.tex:40:preregistered threshold has been modified. The original 2026-04-20
sections/10_conclusion.tex:50:$N\!=\!20$ ($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples
sections/10_conclusion.tex:51:at or below zero, reported as $0.0000$) is comparable in magnitude to
sections/10_conclusion.tex:61:classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
sections/10_conclusion.tex:63:$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
sections/10_conclusion.tex:65:refinement at the same threshold), while
sections/10_conclusion.tex:67:(threshold $|\cdot|\!<\!10$pp) — and as an H$_4$-transitive
sections/10_conclusion.tex:71:structure is at $-11.58\sigma$ on degree homogeneity,
sections/10_conclusion.tex:72:$+79.78\sigma$ on participation ratio (with the node-count caveat of
sections/10_conclusion.tex:73:\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
sections/09_limitations.tex:23:battery and the eighteen preregistered tests, with thresholds
sections/09_limitations.tex:26:\textbf{Single-seed determinism on the recurrent layer.} The v4
sections/09_limitations.tex:36:\texttt{demo\_drug\_sleep\_v4.py}, with per-signature bootstrap CIs.
sections/09_limitations.tex:38:\textbf{Stylised stimulus models on the recurrent layer.} The v4
sections/09_limitations.tex:44:cortical input is much richer. The v4 stimulus models were redesigned
sections/09_limitations.tex:46:artefacts; v4 components are biologically-motivated and not fitted
sections/09_limitations.tex:48:design choices iterated to v4. \emph{Disclosure:}~\S\ref{sec:chain}
sections/09_limitations.tex:49:explicitly frames v4 as a redesign. \emph{Evidence:} amplitudes and
sections/09_limitations.tex:50:durations match published biological time scales; the v3$\to$v4
sections/09_limitations.tex:68:ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
sections/09_limitations.tex:100:\emph{Evidence:} six signatures vs published thresholds.
sections/09_limitations.tex:125:not a threshold change. \emph{Disclosure:}
sections/09_limitations.tex:134:threshold modification.} The reversals (P3, P4, P13) are documented
sections/09_limitations.tex:137:the original failure values, the methodology refinement, and the
sections/09_limitations.tex:162:load-bearing here. Deliberately out of scope.
sections/09_limitations.tex:169:  $2I$-equivariance — open build of the ACT companion paper.
sections/09_limitations.tex:171:  $\mathcal{F}$ — open build of the ACT companion paper.
sections/09_limitations.tex:174:\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
sections/09_limitations.tex:179:\item Verification of P10 (chess null mapping) at the preregistered
sections/09_limitations.tex:181:  permutations; threshold $\geq 50\%$ unchanged; result $65.4\%$
sections/09_limitations.tex:190:EEG signatures, with all original gaps closed by methodology
sections/09_limitations.tex:191:refinement and without modifying any preregistered threshold. We do
sections/09_limitations.tex:193:selection theorem on the ACT bridge. We do not claim uniqueness for

 succeeded in 247ms:
sections/01_introduction.tex:35:We claim a single \emph{substrate witness}: that a geometry-fixed
sections/01_introduction.tex:89:\item \emph{Not a derivation of consciousness.} The substrate witness
sections/01_introduction.tex:93:\item \emph{Not a selection theorem.} The companion adaptive-closure-
sections/01_introduction.tex:147:selection theorem on the 4-tuple bridge; circuit-level mechanistic
sections/01_introduction.tex:167:discusses the substrate witness and proposes a non-load-bearing
sections/01_introduction.tex:168:ACT bridge (without claiming a selection theorem).
sections/09_limitations.tex:63:\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
sections/09_limitations.tex:187:The result is a substrate witness: a geometry-fixed substrate, with
sections/09_limitations.tex:193:selection theorem on the ACT bridge. We do not claim uniqueness for
sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
sections/08_discussion.tex:15:Three things are claimed novel as a substrate witness:
sections/08_discussion.tex:119:\emph{substrate witness} for the family that ACT names; ACT is not the
sections/08_discussion.tex:142:\emph{a hypothesis the substrate witness raises}, not as a proof.
sections/08_discussion.tex:188:\subsection{Open questions raised by the substrate witness}
sections/10_conclusion.tex:75:\textbf{Substrate-witness scope.} This is a substrate witness, not a
sections/10_conclusion.tex:76:derivation of consciousness, not a selection theorem on the
sections/10_conclusion.tex:91:gathered here is the substrate witness; the broader programme to
sections/06_stress_tests.tex:117:\textbf{Architectural reading (substrate witness).} $C$ creates churn
sections/07_cross_domain.tex:202:\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive

exec
/bin/bash -lc "sed -n '30,105p' sections/01_introduction.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc "sed -n '55,205p' sections/09_limitations.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc "sed -n '84,125p' sections/08_discussion.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc "sed -n '88,165p' sections/05_results.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc "sed -n '58,105p' sections/07_cross_domain.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc "sed -n '175,225p' sections/07_cross_domain.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
 succeeded in 300ms:

\subsection{Post-hoc}\label{ssec:posthoc}

\textbf{The 600-cell choice is post-hoc justified by empirical
observables.} While the construction of $\Rsixhundred$ is theorem-
level rigorous (H$_4$ Coxeter group theory), the choice of \emph{this}
polytope as the consciousness-substrate instance is motivated by the
correspondences observed, not by an a-priori biological argument.
\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
preregistered correspondences plus six signatures; the H$_4$
transitivity theorem ($P17$). \emph{Strengthening build:} comparison
with the $24$-cell and $120$-cell on the same signatures; formal
ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
(deferred).

\textbf{Cascade decomposition is one of several possible
decompositions of H$_4$.} We use the $\sigma$-orbit projector basis
because it is machine-precise and biologically informative, but other
bases (character-theoretic, Galois-twin) give the same physical
predictions through different intermediate variables. \emph{Disclosure:}
\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
\emph{Evidence:} block-diagonalisation at $<10^{-15}$ cross-block
norm. \emph{Strengthening build:} catalogue and equivalence-prove the
admissible decompositions.

\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
strictly positive definite (\S\ref{ssec:cphi}); it is not derived
from a closure functional or symmetry argument. \emph{Disclosure:}
\S\ref{ssec:cphi} marks this as a design-level choice; the companion
kernel doc~\citep{SmartAriaClosureKernel2026} explicitly does not
derive it. \emph{Evidence:} the same operator (with the same shift)
serves as the basis for the b-anomaly passive-regime
witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
derive the $\Ph^{-2}$ shift as the unique stability clamp under a
named regularity criterion.

\subsection{Interpretation}\label{ssec:interpretation}

\textbf{The recurrent layer is a method, not a metaphysics claim.}
We do not claim the recurrent self-model layer ``is'' consciousness;
we claim quantitative consistency with six published biological
signatures on a deterministic trajectory. \emph{Disclosure:}
\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
\emph{Evidence:} six signatures vs published thresholds.
\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
formal account of which substrate observables map to which phenomenal
contents (the bind\_phenomenal\_field channels) is not delivered.

\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
matches IIT direction. \emph{Strengthening build:} a
\texttt{phi\_iit\_full} implementation following Balduzzi--Tononi
2008~\citep{BalduzziTononi2008} on the substrate; not delivered.

\textbf{HCP $\sigma$-distances are descriptive, not normative.} We
do not claim ``cortex has drifted from an ideal polytope''; we
quantify the distance between cortex and the deterministic H$_4$ null.
\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
$\sigma$-distances on three independent metrics. \emph{Strengthening
build:} cross-parcellation replication (Schaefer, Glasser).

\subsection{Test/claim}\label{ssec:testclaim}

\textbf{Two preregistered interaction tests required higher $N$
than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
$N\!=\!20$. We document this transparently as consistent with
underpowered interaction estimates on high-per-seed-variance terms,
not a threshold change. \emph{Disclosure:}
\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
\emph{Evidence:} bootstrap CI fully above the $+0.10$ floor; per-seed
distribution narrow at $N\!=\!20$ ($\mathrm{std}=0.089$);
$19/20$ seeds positive. \emph{Strengthening build:} a second
$N\!=\!20$ run at a different seed range (e.g.\ $33000$--$33019$);
an $N\!=\!50$ characterisation of the per-seed distribution.

\textbf{The original 2026-04-20 walks-back are reversed without
threshold modification.} The reversals (P3, P4, P13) are documented
in
\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md} with
the original failure values, the methodology refinement, and the
post-refinement values. \emph{Disclosure:} this paper carries those
disclosures verbatim. \emph{Evidence:} 2026-04-20 vs 2026-04-29 side-
by-side results table. \emph{Strengthening build:} the strengthening
builds for P3/P4/P13 above; no further claim is needed.

\textbf{Bayesian and full-IIT inference not performed.} All intervals
are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
proxy, not the Balduzzi--Tononi 2008 algorithm. \emph{Disclosure:}
this section. \emph{Strengthening build:} Bayesian posterior on
$\Delta_{CP}$; full-IIT computation on the
substrate's $S^{3}$ state space. The latter is computationally
heavy and is deferred.

\subsection{State-drift / out-of-scope}\label{ssec:scope}

\textbf{Single condition-dependent parameter $\eta$ is not derived
as a learned variable.} $\eta\in\{0, 0.05, 0.20\}$ across PROPOFOL,
SLEEP\_N3, and WAKE/RECOVERY is a condition-dependent constant in
this paper, not a learned trajectory. A predictive-processing
extension where $\eta$ adapts on an error norm is an open build.

\textbf{No deuteron / hadron / RH / capstone material is loaded into
this paper.} The companion programme (cascade-derivation, capstone
coalgebra, RH formal) shares operator-level infrastructure but is not
load-bearing here. Deliberately out of scope.

\textbf{Out-of-scope items NOT delivered (correctly).}
\begin{itemize}\itemsep=2pt
\item Aria-chess active-regime companion analysis on chess move-by-move
  trajectories (this paper covers static positions only).
\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under
  $2I$-equivariance — open build of the ACT companion paper.
\item Lyapunov derivation $V(W)$ from a closure functional
  $\mathcal{F}$ — open build of the ACT companion paper.
\item Selection theorem for $\Rsixhundred$ over alternative regular
  4-polytopes — see~\S\ref{ssec:regime}.
\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
  of the six signatures.
\item Cross-parcellation replication of the HCP $\sigma$-distances
  (Schaefer, Glasser, etc.).
\item Bayesian posterior on the C$\times$P interaction.
\item Verification of P10 (chess null mapping) at the preregistered
  $20$-permutation count (the 2026-04-29 validation used $15$
  permutations; threshold $\geq 50\%$ unchanged; result $65.4\%$
  robust in the $15$--$20$ range, but the prereg-exact rerun is open).
\end{itemize}

\subsection{The honest verdict}

The result is a substrate witness: a geometry-fixed substrate, with
no shape parameters tuned to any neural dataset, is consistent with
eighteen preregistered correspondences and six companion drug/sleep
EEG signatures, with all original gaps closed by methodology
refinement and without modifying any preregistered threshold. We do
not claim the substrate \emph{is} consciousness. We do not claim a
selection theorem on the ACT bridge. We do not claim uniqueness for
$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
for these stronger claims are listed above and remain open.

 succeeded in 300ms:
against eighteen preregistered correspondences plus six companion
drug/sleep EEG signatures.

\subsection*{What this paper claims}

We claim a single \emph{substrate witness}: that a geometry-fixed
substrate, with no shape parameters tuned to any neural dataset, is
consistent with eighteen preregistered correspondences (frozen
2026-04-18) and six companion drug/sleep EEG signatures of
conscious vs unconscious states.

\begin{enumerate}\itemsep=2pt
\item \textbf{Substrate is fixed once chosen.} Once $\Rsixhundred$
  is selected, the vertex set ($|V|=120$, all on the unit
  $3$-sphere) is forced by the canonical 600-cell construction; H$_4$
  transitivity forces uniform vertex degree (here $12$ on the
  short-edge nearest-neighbour graph); and the Laplacian spectrum is
  computed from the resulting graph and reported as observed, with
  multiplicities matching the expected H$_4$ block sizes
  (\S\ref{sec:substrate}). The response operator
  $\Cph = \Lop + \Ph^{-2} I$ is fully fixed once the graph is
  constructed and the stability shift $\Ph^{-2}$ is chosen as a
  design-level clamp.
\item \textbf{Cortical avalanches.} Wake cascade-event power-law
  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
  (n$=$30 subjects) and ARIA's prior cascade-pipeline CI
  $[2.73, 3.25]$.
\item \textbf{Six drug/sleep signatures.} On a single deterministic
  trajectory at seed $42$: NREM-N3 phenomenal-intensity variance
  collapse to $0.463\!\times$ wake; propofol modality-switching
  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
  recovery deterministically identical to wake; wake cascade-$\alpha$
  in the SOC band.
\item \textbf{Eighteen preregistered correspondences pass.}
  $17/18$ at standard methodology; $18/18$ after a documented
  $N\!=\!20$ deep-dive on the residual high-variance interaction
  test; \emph{no preregistered threshold has been modified}.
\item \textbf{Cross-domain selectivity.} The substrate exhibits
  selective amplification in the two cross-domain tasks tested
  (chess $+40.6$pp leave-one-out lift at depth $n\!=\!25$ ticks;
  conversation $-4.4$pp lift, within preregistered neutrality bounds)
  and serves as an H$_4$-transitive deterministic null reference for
  cortical functional connectivity (HCP full-cohort descriptive
  $n\!=\!1003$: ARIA at $-11.58\sigma$ on degree homogeneity;
  $+79.78\sigma$ on raw participation ratio with the node-count caveat
  of \S\ref{ssec:hcp}).
\end{enumerate}

\subsection*{What this paper does \emph{not} claim}

\begin{itemize}\itemsep=2pt
\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
  the unique substrate consistent with these signatures. Other regular
  4-polytopes (the 24-cell, the 120-cell) are an explicit ablation
  build, not a discharged comparison. The 600-cell choice is post-hoc
  motivated by the H$_4$ Coxeter cascade structure and biological
  observables; it is not an a-priori derivation from first principles.
\item \emph{Not a derivation of consciousness.} The substrate witness
  shows quantitative agreement with cortical signatures; it does not
  establish that the substrate \emph{is} consciousness, nor that
  its dynamics implement specific phenomenal content.
\item \emph{Not a selection theorem.} The companion adaptive-closure-
  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
  proposes a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which
  this substrate fills the $L_M$ slot. The selection of the 600-cell
  as the active $M$ is conjectural in that paper and is treated as
  non-load-bearing here. We do not deliver a Lyapunov function on the
  reduced flow, nor a $2I$-equivariance audit of the closure operator,
  nor a formal edge-space decomposition. These are listed as open
  builds in~\S\ref{sec:limitations}.
\item \emph{Not a circuit-level model.} The substrate is at the
  architectural-algorithmic level. We do not identify which neural
  populations implement context rotation or partial emission, only
  that some such mechanisms appear in the substrate's preregistered

 succeeded in 302ms:
\S\ref{ssec:regime}.

\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}

\textbf{Tally.} $17/18$ at standard validation
(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
$32000$--$32019$). \emph{No preregistered threshold has been modified.}

\begin{table}[ht]
\centering
\small
\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
\label{tab:eighteen_prereg}
\begin{tabular}{l l l l l}
\toprule
ID & Test & Threshold & Observed (2026-04-29) & Verdict \\
\midrule
P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
\bottomrule
\end{tabular}
\end{table}

\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
estimator as $5$-fold CV at threshold $\geq +15$pp; the 2026-04-29
validation tightened the estimator to LOO with state reset, a
disclosed estimator/protocol refinement at the unchanged $+15$pp threshold. See
\S\ref{sec:cross_domain} for the depth sweep and protocol detail.

\textbf{Three predictions that flipped to PASS, with documented
methodology refinement (no threshold change).}
\begin{itemize}\itemsep=2pt
\item P3 (D$\times$C interaction independence) was outside the band
  at $N\!=\!3$ ($-0.231$) and inside the band at $N\!=\!5$ ($-0.183$).
  Reading: consistent with an underpowered interaction estimate at
  $N\!=\!3$ on a high-per-seed-variance interaction term.
\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
  ($+0.044$) and at $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
\item P13 (chess substrate lift): the 2026-04-18 preregistration
  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
  validation strengthened the estimator to LOO with state reset, a
  disclosed estimator/protocol refinement at the same threshold; the LOO lift was $+3.1$pp
  without state reset on a state-drifted substrate, and $+40.6$pp
  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
  report this as a \emph{validation-protocol refinement relative to
  the preregistered test}, not as preregistration revision.
\end{itemize}

\textbf{Headline verdict.} Eighteen preregistered correspondences
all pass at preregistered thresholds, with two interaction tests
requiring $N\!\geq\!5$ and one requiring $N\!=\!20$ for reliable
detection of high-variance interaction terms, and one test
requiring the documented state-reset protocol. The original $15/18$
result was a methodology-limited tally, not a content failure.


 succeeded in 311ms:
\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}

The companion adaptive-closure-transport
preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
4-tuple bridge
$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
$L_{M}$, learnable Hebbian-like field $W$, and a homeostatic
regulariser $R_{\mathrm{hom}}$. We propose the dictionary
$D_{\mathrm{ACT}}$:
\[
D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
\;\longmapsto\;
(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
   \ \texttt{homeostatic\_reset}).
\]
\textbf{This bridge is non-load-bearing for the present paper.} It is
included as a route-K (alternative-route) reading; the substrate-
witness claims (six signatures, $18/18$, chess $+40.6$pp,
HCP $\sigma$-distances) do not require any of the ACT theorems.

\textbf{What ACT would have to deliver to make this load-bearing.}
The companion preprint identifies four open builds, each of which is
deferred:
\begin{itemize}\itemsep=2pt
\item A Lyapunov function $V(W)$ on the reduced flow whose
  monotonicity proves selection — not delivered.
\item An edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
\item A formal $2I$-equivariance audit of the closure operator
  family — not delivered.
\item A full reduced-flow convergence theorem on
  $W$-trajectories — not delivered.
\end{itemize}
Until these are delivered, ARIA is positioned as the empirical
\emph{substrate witness} for the family that ACT names; ACT is not the
selection-theorem witness for ARIA. The companion kernel
document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
in a passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$ flavour
anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
infrastructure with this paper, but does not transfer empirical
support for ARIA.

 succeeded in 292ms:
\caption{Chess preregistered tests (with reset, $n=25$ canonical
depth).}
\label{tab:chess_prereg}
\begin{tabular}{l l l l l}
\toprule
ID & Test & Threshold & Observed & Verdict \\
\midrule
P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
P11 & random-label baseline (20 trials)     & $\in[15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
\bottomrule
\end{tabular}
\end{table}

$^{\dagger}$ The 2026-04-18 preregistration combined the null-mapping
prediction across both domains (``$\geq 50\%$ on chess and
conversation''). We split it for table clarity into P10 (chess null)
and P16 (conversation null); both pass. The 2026-04-18 preregistration
specified $20$ random label permutations for the null-mapping bound;
the 2026-04-29 validation run used $15$ permutations
(\texttt{run\_preregistered\_validation.py}; the $\geq 50\%$ threshold
is unchanged). We report this as a disclosed-protocol deviation, not
a threshold change; the observed $65.4\%$ at $15$ perms sits well
above the $50\%$ floor and the result is robust to perm count in this
range. Verification at the preregistered $20$-perm setting is an open
build (\S\ref{sec:limitations}).

$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
The 2026-04-29 validation tightened the estimator to LOO with state
reset; we report the LOO finding ($+40.6$pp) above as a disclosed
estimator/protocol refinement at the unchanged $+15$pp threshold,
not a preregistration revision.

\textbf{Reading.} Substrate routing amplifies chess-position
4-category classification from raw $53.1\%$ (just above $25\%$
chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
This is a $+40.6$pp lift on the LOO refinement; on the preregistered
$5$-fold CV estimator the substrate-routed accuracy is $83.1\%$
(P9), itself well above any reasonable raw-features baseline.
The original 2026-04-20 validation reported the LOO lift at
$+3.1$pp, a state-drift artefact closed by the reset protocol
(\S\ref{sec:method}).

\textbf{Permutation null decomposition.} The null permutation
mapping (P10) randomises the feature$\to$frame assignment, so each

 succeeded in 383ms:
\toprule
Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
\midrule
Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
Clustering coefficient (descriptive)$^{\flat}$ & $0.455$ & $0.220$ & $+6.80\sigma$ \\
\bottomrule
\end{tabular}
\end{table}

\noindent$^{\flat}$ The HCP across-subject standard deviation for the
clustering coefficient is not separately reported in
\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
from the same descriptive analysis as the other rows. Inferred from
the reported gap and $\sigma$, the implicit HCP sd is
$\approx 0.235/6.80\!\approx\!0.035$. We carry the $\sigma$-distance
forward as reported and flag the missing explicit sd here.

\begin{itemize}\itemsep=2pt
\item P17 (ARIA degree std, theorem): predicted $=0$, observed
  $0.0000$, $\checkmark$.
\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
  HCP subjects have degree std below $2.0$.
\end{itemize}

\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
structure is a deterministic group-theoretic null reference for
cortical functional connectivity. Real cortex breaks the symmetry
through hub-spoke functional specialisation; the $\sigma$-distances
quantify the magnitude of biological symmetry-breaking with no
fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
clustering coefficient) are large on the ICA-50 pipeline at the
density-matched threshold $\rho = 0.101$; cross-parcellation
replication (Schaefer, Glasser) remains an open build.

\textbf{Participation-ratio comparability.} ARIA's vertex graph has
$120$ nodes; the HCP ICA-50 connectivity matrix has $50$ nodes. The
participation-ratio statistic
$\mathrm{PR}(G) = (\sum_{i} d_{i})^{2} / \sum_{i} d_{i}^{2}$ is
node-count-dependent — its theoretical maximum is the node count of
the graph. We report the raw $\mathrm{PR}$ values
($\mathrm{ARIA}=68.54$ on a 120-node graph; $\mathrm{HCP}=19.72$ on a
50-node graph) and the $\sigma$-distance against the HCP
across-subject distribution, but the $+79.78\sigma$ value reflects
both the architectural difference and the differing node counts. A
node-count-normalised statistic
$\mathrm{PR}/|V|$ gives $\mathrm{ARIA}=0.571$ vs $\mathrm{HCP}=0.394$,
a smaller absolute gap; we keep the raw-PR comparison as headline

exec
/bin/bash -lc "sed -n '225,275p' sections/07_cross_domain.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc "sed -n '16,90p' sections/05_results.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc "sed -n '20,50p' sections/02_method.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc "sed -n '135,155p' sections/02_method.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc "sed -n '45,80p' sections/10_conclusion.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
exec
/bin/bash -lc 'rg -n "unique|uniqueness|select(ion|s|ed)|derive|derivation|consciousness|is consciousness|load-bearing|600-cell" sections/*.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
 succeeded in 240ms:
\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}

\textbf{Setup.} Four conditions $\times$ $800$ ticks at seed $42$,
$k_{\mathrm{thr}}=12$, single deterministic substrate
(\S\ref{sec:chain}). Per-condition trajectory observables are
$(n_{\mathrm{evt}}, \alpha, \mathrm{CI}_{95}, R^{2}, I_{\mathrm{var}},
\Phi_{\mathrm{traj}}, \mathrm{cont})$.

\begin{table}[ht]
\centering
\small
\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
seed 42).}
\label{tab:per_condition}
\begin{tabular}{l r r l r r r r}
\toprule
condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
\midrule
WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
SLEEP\_N3 & $111$ & $3.250$ & $[2.44, 4.14]$ & $0.886$ & $1.01\!\times\!10^{-5}$ & $0.0055$ & $0.980$ \\
PROPOFOL  & $246$ & $2.758$ & $[2.52, 3.09]$ & $0.931$ & $5.37\!\times\!10^{-6}$ & $0.0003$ & $0.877$ \\
RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
\bottomrule
\end{tabular}
\end{table}

\begin{table}[ht]
\centering
\small
\caption{Six drug/sleep signatures with literature references.}
\label{tab:six_signatures}
\begin{tabular}{c l l c c l}
\toprule
\# & Signature & Reference & Predicted & Observed & Verdict \\
\midrule
1 & NREM-N3 var ratio (vs Wake) &
   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
2 & Propofol switching ratio &
   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
3 & Propofol continuity drop &
   EEG microstate~\citep{Brodbeck2012Microstates} &
   $> 0.020$ & $+0.066$ & $\checkmark$ \\
4 & Propofol $\Phi$ collapse (IIT) &
   Tononi 2008~\citep{Tononi2008} &
   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
5 & Recovery reversibility &
   clinical anaesthesia &
   identical to wake & $0$ diff & $\checkmark$ \\
6 & Wake cortical-avalanche $\alpha$ &
   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
   $\alpha\!\in\![1.5, 3.5]$, $R^{2}\!>\!0.85$ &
   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
   $\checkmark$ \\
\bottomrule
\end{tabular}
\end{table}

All six signatures pass against their literature-derived thresholds
on the same deterministic substrate trajectory. The six signatures
are not part of the dated 2026-04-18 P1--P18 preregistration; their
thresholds are drawn from the literature (Sleep-EDFx CI for
wake $\alpha$, OpenNeuro \texttt{ds005620} point-estimate window for
propofol switching, literature-direction predictions for $\Phi$
collapse, continuity drop, and recovery). They were tested on a
recurrent-layer architecture redesigned at v4 with
biologically-motivated condition-specific stimulus models
(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
documents the v3$\to$v4 stimulus redesign). The mechanistic readings
in \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} are not
load-bearing for the headline claim. Single-seed disclosure:
\S\ref{ssec:regime}.

\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}

 succeeded in 241ms:
a smaller absolute gap; we keep the raw-PR comparison as headline
because the HCP subject distribution and the across-subject
$\sigma$ are computed in the same units, but flag the node-count
caveat here.

\textbf{What we do not claim.}
\begin{itemize}\itemsep=2pt
\item We do not claim cortex has ``drifted from an ideal polytope'';
  the substrate is a useful a-priori null whose deviation from real
  cortex is precisely measurable.
\item We do not claim parcellation invariance: the $\sigma$-distances
  are reported on ICA-50; alternative parcellations (Schaefer,
  Glasser) would give different per-metric numbers but, on the
  basis of the qualitative pattern that cortex is hub-concentrated
  relative to ARIA's transitive null, we expect them to preserve the
  signs. Verification across parcellations is an open build
  (\S\ref{sec:limitations}).
\end{itemize}

\subsection{Cross-domain summary as a selective amplifier
            \texorpdfstring{$+$}{+} H$_4$-transitive null}

\begin{table}[ht]
\centering
\small
\caption{Cross-domain summary on a single substrate.}
\label{tab:cross_domain_summary}
\begin{tabular}{l r r r r r}
\toprule
Task & Raw & Substrate & Null perm. & Geom.\ floor & Sem.\ alignment \\
\midrule
Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\
Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (substrate vs null) \\
\bottomrule
\end{tabular}
\end{table}

The geometric content ($\approx 65$--$71\%$ across the two domains)
is the architecture-invariant null floor. The semantic content
($12$--$18$pp) is the domain-specific contribution. On HCP,
$\sigma$-distances against the biological cohort are
$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
clustering coefficient).

\textbf{Headline cross-domain reading.} The substrate is
\emph{selectively} amplifying (not unconditionally), and it is an
H$_4$-transitive deterministic null on connectivity (not a fitted
model). Both readings sit inside the substrate-witness scope.

 succeeded in 258ms:

\textbf{Strong-coupling architectural finding.} Two cascade
mechanisms — context rotation $C$ and partial emission $P$ — are
causally identifiable within the factorial ablation model and exhibit
strong synergy: their interaction $\Delta_{CP}\!=\!+0.190$ at
$N\!=\!20$ ($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples
at or below zero, reported as $0.0000$) is comparable in magnitude to
the $P$ main effect $-0.218$. The original 3-seed estimate ($+0.044$)
is consistent with an underpowered interaction estimate on a
high-per-seed-variance term ($\mathrm{std}=0.089$ at $N\!=\!20$); we
contribute $N\!\approx\!20$ as a planning scale for this cascade
matrix, recommended as a preregistration-practice consideration for
similar high-variance ablation matrices.

\textbf{Cross-domain selectivity.} The substrate exhibits selective
amplification on the two tasks tested: chess 4-category position
classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
canonical depth $n\!=\!25$ ticks (raw $53.1\%$ $\to$ substrate-routed
$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
$5$-fold CV — the LOO finding above is a disclosed estimator/protocol
refinement at the same threshold), while
conversation utterance classification at raw $87.5\%$ lifts $-4.4$pp
(threshold $|\cdot|\!<\!10$pp) — and as an H$_4$-transitive
deterministic null reference for cortical functional connectivity:
on the full-cohort descriptive HCP $n\!=\!1003$ statistics
(preregistered test on the $n\!=\!100$ subset), ARIA's H$_4$-transitive
structure is at $-11.58\sigma$ on degree homogeneity,
$+79.78\sigma$ on participation ratio (with the node-count caveat of
\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.

\textbf{Substrate-witness scope.} This is a substrate witness, not a
derivation of consciousness, not a selection theorem on the
companion adaptive-closure-transport
4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
uniqueness claim for the 600-cell among regular 4-polytopes. The
strengthening builds — cross-seed CIs on the recurrent-layer

 succeeded in 268ms:
the event size is the $\ell^{1}$ norm of the state-difference vector
at that tick. Zero-size events are excluded.

\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
estimated by event-resampling bootstrap (500 resamples for the
preregistered cascade-$\alpha$ tests, 2000 resamples for the
$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
preregistered; 42 for the deep-dive.

\textbf{Bootstrap one-sided $P$-value reporting.} For the C$\times$P
deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
$0/2000$ were below the preregistered floor $+0.10$; we report these
as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
zero-probability statement on a finite resample.

\textbf{Factorial interaction estimator.} For the $2{\times}2$
ablation conditions $\{----, -C--, --P-, -CP-\}$, the interaction is
\[
\Delta_{CP}
\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.

 succeeded in 280ms:
\textbf{Frozen 2026-04-24.} Two later batteries — H$_4$ fingerprint
predictions and rung observables — were preregistered on 2026-04-24
in \texttt{docs/brain\_mapping/PREREG\_H4\_FINGERPRINT.md} and
\texttt{docs/brain\_mapping/PREREG\_RUNG\_OBSERVABLES.md}. \emph{We do
not include those batteries in the headline 18/18 tally.} They are
listed as future strengthening builds in~\S\ref{sec:limitations}.

\textbf{Six EEG signatures (set B).} The drug/sleep signatures on the
recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six companion
biological signatures with literature-derived thresholds (NREM-N3
variance ratio, propofol switching ratio, propofol continuity drop,
propofol $\Phi$ collapse, recovery reversibility, wake
cascade-$\alpha$). They are not part of the P1--P18 preregistration;
they are reported as a companion validation set on the recurrent
layer.

\textbf{No threshold has been modified post-hoc.} Where the original
2026-04-20 validation reported failures (P3, P4, P13), the documented
methodological refinements were
(a)~increasing $N$ from $3$ to $5$ for cascade interaction terms,
(b)~adding a $N\!=\!20$ deep-dive for the highest-variance interaction
(P4, C$\times$P), and
(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
measurements for the chess LOO test (P13). None of these touched a
preregistered threshold.

\subsection{Provenance ledger}

We write the provenance map as $\Pi\colon\{\text{claim id}\}
\to (\text{script}, \text{seed range}, \text{dataset/source},
\text{threshold}, \text{result})$.

 succeeded in 298ms:
sections/06_stress_tests.tex:133:selected to be non-overlapping with the original $30000$s seeds.
sections/06_stress_tests.tex:144:\item It does not establish that the substrate is uniquely selected by
sections/06_stress_tests.tex:146:\item It does not establish an $\eta$-trajectory derivation; $\eta$
sections/09_limitations.tex:14:\textbf{Single substrate (the 600-cell).} We have not tested whether
sections/09_limitations.tex:16:comparable correspondences. The 600-cell was chosen because its
sections/09_limitations.tex:18:that motivated this paper, not from an a-priori derivation.
sections/09_limitations.tex:19:\emph{Disclosure:} substrate-witness scope, no uniqueness claim
sections/09_limitations.tex:53:build:} replication on stimulus models derived from anatomically-grounded
sections/09_limitations.tex:58:\textbf{The 600-cell choice is post-hoc justified by empirical
sections/09_limitations.tex:61:polytope as the consciousness-substrate instance is motivated by the
sections/09_limitations.tex:64:derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
sections/09_limitations.tex:68:ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
sections/09_limitations.tex:76:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
sections/09_limitations.tex:81:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
sections/09_limitations.tex:83:strictly positive definite (\S\ref{ssec:cphi}); it is not derived
sections/09_limitations.tex:87:derive it. \emph{Evidence:} the same operator (with the same shift)
sections/09_limitations.tex:90:derive the $\Ph^{-2}$ shift as the unique stability clamp under a
sections/09_limitations.tex:96:We do not claim the recurrent self-model layer ``is'' consciousness;
sections/09_limitations.tex:153:\textbf{Single condition-dependent parameter $\eta$ is not derived
sections/09_limitations.tex:160:this paper.} The companion programme (cascade-derivation, capstone
sections/09_limitations.tex:162:load-bearing here. Deliberately out of scope.
sections/09_limitations.tex:170:\item Lyapunov derivation $V(W)$ from a closure functional
sections/09_limitations.tex:192:not claim the substrate \emph{is} consciousness. We do not claim a
sections/09_limitations.tex:193:selection theorem on the ACT bridge. We do not claim uniqueness for
sections/07_cross_domain.tex:115:unique; it is a description of the observed accuracy stack.
sections/08_discussion.tex:6:theories of consciousness, identifies what is novel here that is not
sections/08_discussion.tex:7:a re-statement of an earlier theory, and proposes a non-load-bearing
sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
sections/08_discussion.tex:11:not claim the recurrent layer ``is'' consciousness.
sections/08_discussion.tex:19:  data.} Once the 600-cell is chosen as the substrate, its graph
sections/08_discussion.tex:26:  literature-derived thresholds on a single deterministic substrate.
sections/08_discussion.tex:48:\subsection{Comparison to existing theories of consciousness}
sections/08_discussion.tex:63:selection; the active observer frame plays the role of a temporary
sections/08_discussion.tex:80:circuits implement context rotation or partial emission. The 600-cell
sections/08_discussion.tex:84:\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
sections/08_discussion.tex:99:\textbf{This bridge is non-load-bearing for the present paper.} It is
sections/08_discussion.tex:104:\textbf{What ACT would have to deliver to make this load-bearing.}
sections/08_discussion.tex:109:  monotonicity proves selection — not delivered.
sections/08_discussion.tex:120:selection-theorem witness for ARIA. The companion kernel
sections/03_substrate.tex:2:\section{The 600-cell response substrate}\label{sec:substrate}
sections/03_substrate.tex:16:The 600-cell $\Rsixhundred$ has $120$ vertices in
sections/03_substrate.tex:38:sizes. The 600-cell construction itself is
sections/03_substrate.tex:68:multiplicities match the expected H$_4$ block sizes. We do not derive
sections/03_substrate.tex:97:\emph{not} a derived theorem; it is a stability choice. The companion
sections/03_substrate.tex:103:This paper imports $\Cph$ from that line; we do not re-derive it.
sections/03_substrate.tex:114:The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
sections/03_substrate.tex:166:  is not a derivation; it is a design-level clamp that bounds the
sections/04_consciousness_chain.tex:15:recurrent layer ``is'' consciousness; we report which numerical
sections/04_consciousness_chain.tex:47:\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
sections/04_consciousness_chain.tex:67:\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
sections/04_consciousness_chain.tex:113:\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
sections/10_conclusion.tex:5:The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
sections/10_conclusion.tex:21:drug/sleep EEG signatures pass against their literature-derived
sections/10_conclusion.tex:76:derivation of consciousness, not a selection theorem on the
sections/10_conclusion.tex:79:uniqueness claim for the 600-cell among regular 4-polytopes. The
sections/10_conclusion.tex:92:turn the witness into a selection-theorem-grade claim — including the
sections/02_method.tex:29:biological signatures with literature-derived thresholds (NREM-N3
sections/02_method.tex:95:consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
sections/02_method.tex:103:psychedelic-state reference; not load-bearing for the headline tally.
sections/05_results.tex:75:All six signatures pass against their literature-derived thresholds
sections/05_results.tex:87:load-bearing for the headline claim. Single-seed disclosure:
sections/05_results.tex:184:\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
sections/01_introduction.tex:5:Theories of consciousness divide into mechanism-driven proposals
sections/01_introduction.tex:22:600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
sections/01_introduction.tex:26:candidate substrate for consciousness-linked signatures. We construct $\Rsixhundred$, fix its response
sections/01_introduction.tex:43:  is selected, the vertex set ($|V|=120$, all on the unit
sections/01_introduction.tex:44:  $3$-sphere) is forced by the canonical 600-cell construction; H$_4$
sections/01_introduction.tex:83:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
sections/01_introduction.tex:84:  the unique substrate consistent with these signatures. Other regular
sections/01_introduction.tex:86:  build, not a discharged comparison. The 600-cell choice is post-hoc
sections/01_introduction.tex:88:  observables; it is not an a-priori derivation from first principles.
sections/01_introduction.tex:89:\item \emph{Not a derivation of consciousness.} The substrate witness
sections/01_introduction.tex:91:  establish that the substrate \emph{is} consciousness, nor that
sections/01_introduction.tex:93:\item \emph{Not a selection theorem.} The companion adaptive-closure-
sections/01_introduction.tex:96:  this substrate fills the $L_M$ slot. The selection of the 600-cell
sections/01_introduction.tex:98:  non-load-bearing here. We do not deliver a Lyapunov function on the
sections/01_introduction.tex:107:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
sections/01_introduction.tex:110:  bounds the Green response). It is not derived as a theorem from a
sections/01_introduction.tex:127:We never write `the substrate \emph{is} cortex' or `derives consciousness'.
sections/01_introduction.tex:146:\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
sections/01_introduction.tex:147:selection theorem on the 4-tuple bridge; circuit-level mechanistic
sections/01_introduction.tex:148:identification; first-principles derivation of $\Ph^{-2}$ shift;
sections/01_introduction.tex:149:that cortex \emph{is} the 600-cell.
sections/01_introduction.tex:167:discusses the substrate witness and proposes a non-load-bearing
sections/01_introduction.tex:168:ACT bridge (without claiming a selection theorem).

codex
(a) Reflow grep PASS — `148:substrate's $S^{3}$ state space. The latter is computationally`

(b) none

(c) Final verdict: `Publication ready: yes`
tokens used
44,363
(a) Reflow grep PASS — `148:substrate's $S^{3}$ state space. The latter is computationally`

(b) none

(c) Final verdict: `Publication ready: yes`
