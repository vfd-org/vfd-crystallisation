**Publication Verdict**
No. The empirical numbers mostly match the companion papers, especially SL-002, but Paper 03 is not publication-ready on substantive-math and attribution scope. The main problem is overclaiming: operational proxies are repeatedly described as validation of operator-level propositions, and model demonstrations are treated as stronger evidence than they establish.

**1. Claim Audit**
- “Frame-local subjective time” claims subjective time equals frame-local ticks per substrate tick ([03:L150](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:150>)). Not proved. This is an interpretive hypothesis, not a derived proposition. Needs an additional bridge from tick-count to reported temporal phenomenology.

- “Bioelectric closure bridge” claims `C_phi^bio` satisfies closure axioms and therefore admits `Sigma_I^bio` etc. ([03:L198](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:198>)). Proof only shows symmetry by definition and positivity of a shifted Laplacian. It does not prove contraction for `C` itself; contraction belongs to an update such as `I - lambda C` with step-size assumptions. It also does not prove non-trivial `Fix(tau^bio)` for arbitrary allowed involutions.

- “Equation R_cl ... was validated” ([03:L234](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:234>)). Overclaim. SL-001 explicitly says “We have not shown biological validation” ([05:L532](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/05-bioelectric-closure/main.tex:532>)) and “No biological data” ([05:L596](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/05-bioelectric-closure/main.tex:596>)). Say “operationalised and simulation-tested,” not validated.

- “CEMI field as spectral signature of closure” says EM spectral peaks occur at `omega_k = c mu_k` ([03:L278](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:278>)). Not established. The demo code itself notes the real symmetric first-order dynamic is overdamped relaxation, not oscillation. The proof needs a physical time generator, oscillator model, or explicit EM transfer function.

- “R_phase ... operational form ... validated” ([03:L308](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:308>)). Overclaim and partially inconsistent with SL-002. SL-002 says the synthetic-anchored residual does “not strongly capture the empirical regime” ([06:L78](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/06-cortical-phase-closure/main.tex:78>)); the real anchor is the 9-D calibrated displacement proxy, not the closure operator ([06:L331](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/06-cortical-phase-closure/main.tex:331>)).

- SL-002 headline numbers match: 14/14, `t=7.11`, `d_z=1.90` ([03:L313](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:313>)); source `t=9.72`, `d_z=2.60` ([03:L314](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:314>)); cross-cohort `7/7`, `t=5.25`, `d_z=1.98` ([03:L315](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:315>)). But “on `\geq 35` subjects” is wrong ([03:L320](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:320>)): unique human subjects are 14 + 7 = 21; source and LOSO are reanalyses of the same 14.

- “volume conduction ruled out” ([03:L314](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:314>)) is too strong. SL-002’s own limitations include template anatomy and ad-hoc identity noise covariance ([06:L347](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/06-cortical-phase-closure/main.tex:347>)). Use “argues against volume conduction as the sole explanation.”

- ARIA theorem 17/18 and 18/18 ([03:L353](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:353>)) is imported, not proved here. Fine if labelled “reported in SmartAriaChess2026,” but theorem styling overstates what this paper establishes.

- Closure-cost argument says off-`Sigma` content “decays” from eigenvalue lower bound ([03:L425](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:425>)). This again needs the explicit dynamical map and step-size assumptions. A positive definite `C` does not by itself define decay under repeated application.

- Sleep proposition ([03:L435](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:435>)) is speculative. “Sleep deprivation causes a monotonic decline in `dim Sigma`” is not derived and should be a prediction, not a conditional proposition with proof force.

- Anaesthesia proposition ([03:L449](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:449>)) is plausible but underproved. SL-002 supports a state-displacement signature, not dose-response threshold crossing. B3 constructs a threshold by choosing the update step near criticality; that does not establish clinical abruptness.

- Numerical demos B1-B3 ([03:L553](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:553>)) are useful demonstrations, not grounding proofs. B1 is narrow and valid for the constructed symmetric graph. B2 does not prove spectral peak claims. B3 is a toy perturbation model.

**2. Internal Consistency**
- `C_phi` is alternately treated as the update operator ([03:L122](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:122>)) and as a generator inside `I - lambda C` ([03:L515](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:515>)). Pick one convention and propagate it.

- `Sigma_I` is sometimes a subset of `Fix(tau)` and sometimes effectively identified with it. The phrase “encoding `Fix(tau^bio)=Sigma_I^bio`” ([03:L234](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:234>)) conflicts with the core definition `Sigma_I := Fix(tau_I)` and inclusion into global `Fix(tau)`.

- H-RP-1 maps `H_4` to V1-V4 ([03:L95](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:95>)), but SL-002 and CEMI claims use whole-cortex EEG/source ROIs. Add a whole-cortex extension hypothesis or widen H-RP-1.

- “These four hypotheses are the only added commitments” ([03:L111](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:111>)) is false as written. The paper also assumes EM observability, physical tick scaling, thermodynamic cost, pharmacological Laplacian modelling, and CAD applicability.

**3. External Consistency**
- Core-paper imports mostly match: closure operator, 94-dimensional `Fix(tau)`, bounded frames, and P-A are aligned with Paper 01. But Paper 01’s per-frame theorem is conditional on symmetry-stability and gives a well-defined subspace, not automatic non-trivial phenomenology.

- SL-001 is underspecified in Paper 03 as simulation-only. Paper 05 is careful that BETSE is not biological validation ([05:L532](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/05-bioelectric-closure/main.tex:532>), [05:L596](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/05-bioelectric-closure/main.tex:596>)); Paper 03 should mirror that language.

- SL-002 is over-attributed. Paper 06 explicitly says the feature vector is “not the closure operator” ([06:L335](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/06-cortical-phase-closure/main.tex:335>)). Paper 03 should call it a first-order proxy and empirical anchor.

- CAD is not integrated deeply enough. Paper 07 says the diagnostic is part of the method, not optional ([07:L44](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:44>)), and that broader biological substrates remain external-validation targets ([07:L368](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/07-closure-cross-substrate/main.tex:368>)). Paper 03 should make every empirical bridge explicitly CAD-scoped.

**4. Narrative Coherence**
The paper mostly fits the programme, but it reads as if Paper 03 itself validates the neuroscience bridge. The stronger ten-paper narrative is: Paper 03 supplies the conditional operator bridge; Paper 06 supplies the real-data cortical proxy; Paper 07 supplies applicability boundaries; Papers 08-10 test downstream reuse. Sentences to tighten:

- “six independent EEG drug/sleep regime tests” ([03:L52](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:52>)) conflicts with “single deterministic trajectory at seed 42” and “not part of the 18 preregistered predictions” ([03:L374](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:374>)).

- “direct neuroscience counterparts” ([03:L415](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:415>)) should become “proxy-level neuroscience counterparts under SL-002/CAD.”

- “why biological systems specifically require sleep” ([03:L421](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:421>)) is broader than the programme’s bounded-conditional discipline.

**5. Tightness Edits**
- [03:L234](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:234>): replace “was validated” with “was operationalised and simulation-tested.”
- [03:L314](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:314>): replace “volume conduction ruled out” with “volume conduction is unlikely to be the sole driver.”
- [03:L320](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:320>): replace “on `\geq 35` subjects” with “on 21 unique subjects, with additional source-space and LOSO reanalyses.”
- [03:L445](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:445>): replace “Any physical realisation ... must” with “The model predicts that persistent biological realisations should.”
- [03:L460](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:460>): replace “is a consequence” with “is a model-level consequence, given the perturbation hypothesis.”

**6. Surface Issues**
- Broken/stale path: `papers/processing-to-point-of-view/repro/bridges_demo.py` should be `papers/03-processing-to-point-of-view/repro/bridges_demo.py` ([03:L553](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:553>)).
- Citation keys in Paper 03 references are present; I found no missing citation keys.
- Define `sigma-fixed` locally when moving to `tau^bio` and `tau^cortex`; the notation shifts too freely.
- Standardise “anaesthetic/anesthetic” in prose and variable labels.
- Avoid theorem environment for imported empirical result unless the paper provides the proof or validation artifact locally.

**7. Top Three Fixes**
1. Recast `R_cl` and `R_phase` as operational proxies, not validations of the operator propositions. This affects [03:L234](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:234>), [03:L308](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:308>), and [03:L320](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/existence-programme/papers/03-processing-to-point-of-view/main.tex:320>).
2. Repair the operator math: distinguish `C` from `I - lambda C`, state step-size/contraction hypotheses, and add non-trivial fixed-subspace assumptions. This affects the Levin bridge, CEMI bridge, thermodynamics, sleep, and anaesthesia claims.
3. Add CAD as a formal scope gate for every empirical bridge. Paper 07’s diagnostic should be part of Paper 03’s bridge logic, not only mentioned after SL-002.

**8. Programme-Strengthening Recommendations**
- Add a “structural claim -> operational proxy -> empirical anchor -> CAD status” table covering `R_cl`, `R_phase`, SL-002, SL-005, SL-006, and SL-007.
- Standardise programme-wide language: “operator-level proposition,” “first-order empirical proxy,” “real-data anchor,” “simulation demonstration,” and “P-A-conditional phenomenological reading.”
- Make Paper 03 the explicit handoff point: Paper 03 defines the neuroscience bridge, Paper 06 validates the cortical proxy, Paper 07 scopes applicability, Papers 08-10 reuse the proxy under CAD.
- Add a short “what would upgrade this bridge” paragraph: dose-response anaesthesia, TMS-EEG perturbational response, sleep-stage source EEG, and planarian wet-lab voltage imaging.

**9. Publication Ready?**
No. The paper is close in framing but not yet acceptable as the neuroscience companion because it overstates proof and validation. The SL-002 anchor is strong as a real-data cortical-state proxy; it does not yet prove the CEMI bridge or anaesthetic threshold mechanism. The needed revision is not cosmetic: tighten the mathematical hypotheses, downgrade proxy-validation language, correct the subject-count claim, and make CAD the formal empirical boundary.
