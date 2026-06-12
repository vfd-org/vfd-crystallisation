Publication-ready? **No.** The `ds007471` honest-negative core is defensible and valuable, but the manuscript currently overclaims around the diagnostic, has internal contradictions after adding `ds006802`, and contains several fix-before-release data/count/notation issues.

Line references: P10 = [Paper 10 main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/10-hyperscanning-joint-meaning/main.tex>), P02 = [Paper 02 main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/02-life-as-closure/main.tex>), P07 = [Paper 07 main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex>).

**1. Claim Audit**
- P10:33,38: The Life-as-Closure joint-meaning framing matches P02:703-711 and P02:731, but P02 defines formal `\delta_{AB}` as an orbit-count/generative-excess object, while P10 reuses `\delta_{AB}` for an empirical L2 residual. The proxy claim is acceptable only if notation is separated, e.g. `\widehat{\delta}_{AB}^{\mathrm{EEG}}`.
- P10:43,63: “Positive `\delta_{AB}` indicates closure structure not reducible…” is not established by the formula alone. It requires comparable normalization of `R_A`, `R_B`, `R_J`, a null model for channel-count effects, and a proof that joint concatenation does not inflate norms mechanically. “Zero indicates additive composition” is especially too strong for a nonlinear norm.
- P10:56: `O_J = O_A \oplus O_B` conflicts with P10:38 `O_A \times O_B` and P02:695 `O_A \cup O_B`. This needs an explicit formal-to-empirical mapping.
- P10:65: Default-weight transfer is asserted, not demonstrated in the manuscript. Worse, H4 is defined here as default-weight robustness, but P10:95 reports H4 as “cross-cohort replication.”
- P10:69: The diagnostic is described as computed on “the per-pair signed-delta of `\delta_{AB}`,” but P07:66-75 defines D1-D5 on a feature-delta matrix. A scalar `\delta_{AB}` cannot yield D2/D3 feature counts. Say it is computed on the underlying per-feature signed deltas used to form the dyadic residual.
- P10:78,94,99,168: H3 fails the revised `>1.5` threshold at `d_z=1.25`. P10:168 says the revised threshold is “still met,” which is simply false.
- P10:103-109: The `ds006802` statistics may be useful, but the diagnostic itself predicts FAIL at P10:107. Therefore this cannot support the conclusion that the diagnostic predicts semantic substrates pass. It is exploratory trend evidence, not a diagnostic PASS.
- P10:107: “Statistically unreachable at n=24” is false. `>=80%` agreement is 20/24, which is reachable; it is just a strict and likely underpowered threshold.
- P10:113-115: Trial counts conflict. P10:33 says `13` pairs and `520` trials. P10:113 says `40 + 40` trials per pair, which would be `1040` trials for 13 pairs. P10:115 says `37+32` markers per pair, which is `69`, not `80` or `40`.
- P10:117-123: The `ds007471` numerical result matches P02:731 and P07:254. But “Empirical `d_z=+0.23` confirms the predicted FAIL” should be “is consistent with the predicted FAIL.” A null does not prove the diagnostic mechanism.
- P10:129: The claim that musical joint-action is structurally single-channel and that all correlations are driven by one beat/tempo mechanism is not established. Also, it says single-channel structure fails D5, but the reported musical diagnostic fails D2/D3, with D5 not reported in P07:201.
- P10:131,145,179: Dialogue PASS is a preregistered prediction, not established evidence. P10:179 overclaims: “substrates with multi-channel semantic content produce the signal” is not supported by a below-threshold `ds006802` trend.

**2. Internal Consistency**
- P10:48 says one real-data cohort; P10:101-123 reports two; P10:166 says “only real-data test” is musical joint-action. This must be reconciled.
- H4 is inconsistent: default-weight robustness at P10:79/65, cross-cohort synthetic replication at P10:95.
- H3 threshold language is inconsistent and mathematically wrong at P10:168.
- Diagnostic computation alternates between scalar `\delta_{AB}` and feature-matrix D1-D5.
- Trial/pair counts for `ds007471` are inconsistent across abstract, methods, and marker description.

**3. External Programme Consistency**
- P02 supports the broad joint-meaning framing, but formal `\delta_{AB}` is not the same object as P10’s L2 proxy. Tighten notation.
- P07 supports D1-D5 and the `ds007471` FAIL numbers, but P10 overstates what FAIL means. P07:44 and P07:49 say the proxy is not expected to dominate baselines outside regime, not that no detectable shift should occur.
- P07 reports musical hyperscanning FAIL on D2/D3; P10’s D5 explanation does not match.
- `ds006802` is not in the P01/P02/P07 programme summaries. If retained, mark it as a new exploratory addendum, not part of the validated 14/15 CAD accounting.

**4. Narrative Coherence**
The honest-negative framing is coherent with Papers 07 and 09. The main narrative problem is that the paper drifts from “methodology-boundary success” into “semantic substrates produce the signal.” Keep Round 1 focused: `ds007471` is a diagnostic-predicted FAIL, and that is the contribution.

Tighten P10:135 because Paper 02 explicitly lists music ensemble as a possible joint-meaning case under P-A at P02:717. Say this EEG musical-joint-action contrast is the wrong substrate for this proxy, not that music is the wrong substrate for joint meaning.

**5. Tightness Edits**
- P10:43: replace “Positive `\delta_{AB}` indicates…” with “When D1-D5 passes and null calibration excludes channel-count inflation, positive `\widehat{\delta}_{AB}` is interpreted as…”
- P10:69: replace “not expected to show a detectable shift” with “not licensed to dominate or to carry the joint-meaning interpretation.”
- P10:105: replace “Direction strongly positive” with “Directionally positive.”
- P10:107: replace “statistically unreachable” with “over-strict and likely underpowered at n=24.”
- P10:123: replace “confirms the predicted FAIL” with “is consistent with the predicted FAIL.”
- P10:179: replace “semantic content produce the signal” with “semantic multi-channel dialogue remains the hypothesised confirming class.”

**6. Surface Issues**
- P10:182 uses `\bibliography{refs}`, but the local file is `references.bib`; source build will fail unless a hidden `refs.bib` exists.
- P10:113-115 trial arithmetic must be corrected before release.
- P10:168 says a threshold is met when it is not.
- “BIOSEMI” should likely be “BioSemi.”
- Use one spelling convention: “pre-registered” vs “preregistered.”
- Add a dated download/log note for the `sub-05` 404 at P10:113.

**7. Top Three Fixes**
1. Fix scope contradictions around one vs two real-data substrates: P10:48,101-123,166,179. For Round 1, I would demote `ds006802` to exploratory appendix or remove it.
2. Separate formal `\delta_{AB}` from empirical residual proxy, and define the normalization/null model for `R_A`, `R_B`, `R_J`: P10:43,56-63.
3. Repair preregistration and diagnostic language: H3 fail, H4 mismatch, scalar-vs-feature D1-D5, and “confirms FAIL” overclaim: P10:69,78,94-95,121-123,168.

**8. Programme-Strengthening Recommendations**
- Adopt a programme-wide convention: formal objects keep bare symbols; empirical proxies get hats and version tags.
- Add a small “claim ledger” table to each Solution Lab paper: formal object, empirical proxy, diagnostic status, preregistered thresholds, real-data status.
- Reuse the exact Paper 07 diagnostic-boundary boilerplate across Papers 08-10.
- Update Paper 01/Paper 02/Paper 07 only after deciding whether `ds006802` is part of the official SL-007 evidence record.
- Add a `ds007471` extraction appendix with pair IDs, downloaded/missing subjects, trial counts, marker counts, and condition counts.

**9. Publication Ready?**
**No.** The central honest-negative result can become publication-ready, and it is worth preserving. But the manuscript currently needs revision because the notation, preregistration accounting, diagnostic interpretation, and `ds007471` trial counts are not tight enough for the ten-paper programme’s standards.

I also spot-checked the live “open-data ceiling” claim. OpenNeuro is indeed an open repository, and the Drijvers/Holler conversational dual-EEG resource appears adjacent but not a simple fully open confirming dataset. Still, “exhaustive search confirms no dataset” needs a dated search appendix, not just prose. Sources: [OpenNeuro](https://openneuro.org/), [MPI Drijvers/Holler protocol page](https://www.mpi.nl/publications/item3513124/studying-naturalistic-human-communication-using-dual-eeg-and-audio-visual).
