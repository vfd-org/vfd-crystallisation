# Known Limitations

Honestly disclosed limitations of the Existence / Life / Closure
Programme as of v1.0.0-rc1 (2026-05-22). Reviewers should treat every
item below as a known gap. Future work targets are listed in
[`../01-falsifiers-and-roadmap.md`](../01-falsifiers-and-roadmap.md).

## Status

- **Pre-peer-review.** This is a release candidate, not a peer-reviewed publication. All papers and notes are open research notes prepared for external review.
- **Multi-round codex-hardened, single-author.** The papers have undergone 5 rounds of codex review iteration; no independent peer review has occurred.

## Formal-core limitations

- **$\tau_{\mathrm{ico}}$ vs $\tau_{\mathrm{spec}}$ basis bridge is unresolved.** Paper I distinguishes the two conventions (Appendix on $\tau$ conventions) but the icosian-to-spectral basis-change for the 96 Type-C vertices of $V_{600}$ has not been implemented numerically. The structural claim (involutivity + commutation + non-trivial fixed subspace) is convention-independent; the specific dimension (94 vs 116) is not. See `papers/I-existence-as-closure/repro/closure_demo.py` D8 for the honest sim-vs-theorem gap report.
- **$C = \mathrm{Fix}(\tau)$ is a definitional stipulation, not a derived theorem.** Paper I's universal closure structure $C$ is defined as $\mathrm{Fix}(\tau)$ rather than derived as the unique maximal $\Cph$-invariant subspace. Demo D7 verifies the operator-invariance content (that $\Cph$ leaves $\mathrm{Fix}(\tau)$ invariant); the maximality interpretation is the framework's choice.
- **Pointwise-fixed vs invariant-subspace semantics are separated.** Paper I states the Algebraic Existence theorem in pointwise form, then notes that the VFD instantiation on $V_{600}$ uses the weaker invariant-subspace form because $\mathrm{Fix}(\Cph) = \{0\}$ on $V_{600}$ (eigenvalues bounded below by $\varphi^{-2} \neq 1$). The two semantics are not interchanged.

## Empirical-proxy limitations

- **Empirical proxies are not the formal operator.** Note C states this explicitly: closure-as-distance is a measurable first-order proxy for distance-to-closure-stable-reference, not the formal closure operator $\Cph$.
- **CAD-D1–D5 thresholds are empirical, not universal constants.** Paper Note C labels them "CAD-D1–D5-v1 empirical thresholds"; CAD-v1.5 recalibration on a larger unpaired-design cohort set is open work.
- **Unpaired-design threshold calibration is unresolved.** The unpaired-design extension of CAD-D1–D5 inherits paired-design thresholds; per-design recalibration on $\geq 10$ between-group substrates is open.
- **FTD vs healthy is a transparently characterised false positive.** Note C reports FTD-on-`ds004504` as predicted-PASS / observed-FAIL. The diagnostic predicts PASS based on the multi-feature criteria; the empirical result is null because the per-feature shifts are directionally coherent but at magnitudes comparable to within-cohort variance. The supplementary $D_6$ criterion catches FTD but creates a false negative on anxiety.
- **Mood `ds004315` is a diagnostic false negative / CAD-v1.5 calibration addendum.** Under unpaired-design CAD-D1–D5-v1 thresholds, mood predicts FAIL; the observed PASS at $d = +0.70$ is recorded as a calibration addendum, not included in the main 15/16 ledger.

## Per-Note limitations

### Note B (Cortical Phase Closure)

- **Source localisation uses sLORETA with ad-hoc identity noise covariance.** Empty-room-noise covariance and non-template anatomy would be the next steps. The strongest interpretation of the source-space result is that it argues against scalp-electrode volume conduction as the sole explanation; source leakage and template-anatomy effects remain.
- **Clinical cohort is small.** $n = 7$ for `ds004541`. The in-sample $d_z = 1.98$ and the cross-validated LOSO $d_z = 1.16$ both fall within the power curve's lower bound. A larger independent clinical cohort would strengthen the cross-cohort claim.

### Note C (Closure-as-Distance)

- **One confirmed strict-CAD-PASS empirical substrate so far.** Source-localised propofol EEG (Note B) is the empirical anchor; the trait-anxiety substrate (Note D) is PASS-leaning under strict thresholds. More strict-PASS empirical substrates would strengthen the predictive licence claim.
- **RNN training rows show calibration-boundary behaviour.** CAD-D5 FAIL is correctly predicted; raw effect size exceeds simple baselines, but across-fold feature-set Jaccard does not. The classification is MATCH-on-stability-claim with a calibration-boundary note on raw effect size.

### Note D (Trauma / Cortical Closure)

- **No clinical PTSD-cohort EEG yet.** The empirical anchor is trait anxiety (`ds007609`, $n = 24$), not a PTSD diagnostic cohort. PTSD pre/post-therapy longitudinal EEG remains the gold-standard external validation.
- **Mood cohort is acute, not chronic.** `ds004315` is an acute mood induction, not a clinical chronic-trauma cohort. Reported as cross-application validation, not as trauma replication.

### Note E (FlowIndex)

- **No real-data PASS yet.** The synthetic-implementation validation $5/5$ PASS shows the metric behaves as designed; both completed real-data substrates (MOBA-gaming `ds005520`, table-tennis `ds004505`) returned diagnostic-correctly-predicted FAILs. The metric has not been empirically demonstrated to PASS on a real-data substrate satisfying multi-channel integrative-organisation conditions. Music-performance and esports-professional EEG remain the pre-registered next experiments.

### Note F (Dyadic Joint Meaning)

- **No confirmed PASS hyperscanning substrate yet.** The completed musical hyperscanning result on `ds007471` is an honest negative (CAD predicted FAIL). The `ds006802` collaborative-rule-learning trend is below preregistered confirming-evidence threshold. A genuine-dialogue conversational hyperscanning cohort with content-meaningfulness ratings remains the appropriate next test.
- **Formal vs empirical $\delta_{AB}$ are distinct.** The formal $\delta_{AB} = |\mathcal{X}_{AB}|$ of Paper II is an orbit count; the empirical $\widehat{\delta}_{AB}^{\mathrm{EEG}}$ of Note F is an L²-norm proxy. The empirical proxy licenses inference about the formal object only when the substrate passes CAD-D1–D5.

### Note A (Bioelectric Closure)

- **BETSE 2-second simulation is Tier C under CAD.** Note C's diagnostic classifies the 2-second BETSE substrate as not closure-applicable in the strict sense; the closure-residual reading is operationally useful but not closure-necessary on this substrate. The wet-lab DiBAC4(3) planarian test (pre-registered, not yet performed) is where the closure interpretation can become load-bearing.
- **Scalar baselines beat closure features on raw "did the perturbation happen?" detection** for uniform depolarisations; closure's contribution is the differential template-residual signature, not bulk perturbation detection.

## Consciousness / phenomenology

- **The Access Principle (P-A) is conjectural.** Paper III's consciousness bridge is conditional on P-A. The framework does not assert P-A; it states the conditional consequence.
- **P-A-spectral (qualia identification) is a strictly stronger conjecture than P-A.** Paper II §11 qualia identification requires both P-A and P-A-spectral; either alone is insufficient.
- **No phenomenological measurement.** The framework supplies structural correlates; no part of the framework measures phenomenology directly.
- **ARIA-chess is a constructed witness, not a proof of consciousness.** Paper III is explicit that ARIA-chess satisfies the structural conditions for a bounded reference frame; whether it has owned experience requires P-A.

## Withheld

- **Extension IV (Cosmic Self-Pruning and Frame Recurrence) is withheld from the primary review packet.** It is a speculative structural extension and is not load-bearing for the core existence, life, measurement, or consciousness-bridge claims. The PDF is not committed to this repository by default; reviewers wishing to read it should contact the author.

## Honest summary

The programme has structural strength and one strong cortical empirical
anchor (Note B). It has scope-conditioned measurement methodology
(Note C). It has not yet demonstrated:

- a strict-CAD-PASS independent cortical empirical substrate beyond anaesthesia;
- a confirmed flow-on-real-data PASS;
- a confirmed conversational-hyperscanning joint-meaning PASS;
- a clinical PTSD-cohort EEG test;
- a wet-lab planarian DiBAC4 regeneration test;
- a TMS-EEG perturbational-complexity consciousness-level test.

Each of these is named as a pre-registered next experiment. Reviewers
should treat them as commitments to test, not as evidence.
