**1. Claim Audit**

- Line 150, eigenvalue proposition: established only by import from Paper II, not by the displayed proof. Acceptable if Paper II is treated as a premise.
- Line 177, uniqueness theorem: the proof establishes only the scoped eleven-polytope uniqueness stated in line 190. It does not support any broader uniqueness of the 600-cell substrate.
- Line 243, RD4 theorem: the first-passage ratio `RD4 = 15` is established. Its use as a mass coefficient is not established; the paper correctly admits this at lines 268 and 310.
- Line 318, proton corollary: the numerical exponent follows from the ansatz and anchors. It does not establish a physical derivation of the proton mass.
- Lines 354-358, alpha: the formula gives the quoted numerical match. The paper is right to call this an engineered arithmetic coincidence, not a derivation.
- Lines 41, 410, 433, 578, 595, 664, “all ten chain ratios forward-traceable”: overclaim. The script verifies nine non-trivial rational coefficient identities. The neutron entry is not a ratio; it is an additive phenomenological reclassification.
- Line 438, Higgs derivation: the arithmetic identity using `RD4` is verified. The claim that this is “not just algebraic match” is not established.
- Lines 439-440, muon/tau: the stated coefficients are exact arithmetic identities, but the proof does not show that those substrate expressions are forced rather than selected.
- Line 441, strange: the shared denominator is not proved structural. This still depends on the open shell-5 boundary convention acknowledged at lines 460 and 654.
- Lines 428, 442, 446, neutron EM splitting: not established. The written mass-level formula has the wrong physical behavior as stated: subtracting a positive EM correction from the proton cannot produce the heavier neutron. It also does not match the script-level `sin^2 theta` implementation cleanly.
- Lines 468-492, mass table: the numerical correspondence is conditional on assignments, anchors, alpha, and the mass ansatz. It is not a theorem-level prediction.
- Lines 675-677, null test: not established by the local script. `run_null_hypothesis.py` samples nine chain ratios and compares framework `sin^2 theta` values, not thirteen fractions evaluated as mass predictions against the observed spectrum.

**2. Internal Consistency**

- Line 652 directly contradicts the new framing: it says several entries are “explicit reverse identifications,” while lines 41, 433, 578, 595, and 664 say the reverse flag is retired.
- Line 451 says nine non-trivial coefficients; line 410/table framing repeatedly says ten chain ratios. This should be stated as “nine coefficients plus one neutron reclassification.”
- Line 595 puts a positive claim, “All ten chain ratios are forward-traceable,” under “What this paper does not claim.”
- Lines 428, 442, and 446 disagree about the neutron correction’s mathematical form and status. The table/text should distinguish mass correction from `sin^2 theta` correction.
- Line 574 says shell 1 is covered by the same `c/b=1/6` single-step argument, but the displayed dual-population table supports shells 2 and 3. Shell 1 is a convention unless separately proved.
- Line 540 says the neutral `Z` uses `{2,3,4}` as a model choice, while rule R5 at line 513 says charged bosons/scalars include shell 1. This exception should be part of the rules, not buried in the assignment table.
- Line 109 says all witnesses share the “same shell decomposition.” That is too strong: the mass paper uses the six BFS shells and dual populations, while closure-kernel/ARIA material uses a different shell/coarse-graining language.
- Table `tab:chain` uses `N_8`, `N_9`, and `N_{11}` without defining them.

**3. External Consistency**

- Paper II / cascade substrate: locally verified. It supports the spectrum, narrow uniqueness, dual populations, RD4 first-passage value, and Hopf-cycle facts, with the same caveat that mass identification remains model-level.
- Closure-kernel / ARIA witness: locally verified in the release bundle only with caveats. The 18/18 claim is after documented P4/P13 refinements; the standard tally is 17/18. The six active-regime signatures are single-seed and explicitly scoped as witness evidence, not substrate uniqueness.
- B-anomaly: the primary cited `vfd-b-anomaly` paper is not present locally in this repo. I can verify only a secondary closure-kernel summary: five datasets have `A>0` and negative effective `Delta C9`, while AIC discrimination is inconclusive. The paper should not imply the primary source has been locally checked unless it is actually included.
- Selection-layer / ACT / transport-law: locally verified, but the present text overstates alignment. Those papers present a candidate dynamical framing on the same operator family; they explicitly do not verify full coupled transport/selection dynamics. Line 99 should not say they “supply the dynamical layer” without qualification.

**4. Tightness**

- Line 41: replace “closed forward derivation of all ten chain ratios” with “exact primitive decompositions for nine non-anchor chain coefficients, plus a separate neutron EM-splitting reclassification.”
- Line 438: replace “not just algebraic match” with “an algebraic decomposition reusing the independently imported `RD4` value.”
- Line 441: replace “not coincidence forced by open search” with “a proposed structural regularity; no exclusion of post-hoc selection is proved here.”
- Line 446: replace “standard EM correction” with “a phenomenological EM-inspired correction; the correction form is not derived from the 600-cell.”
- Line 99: replace “supply the dynamical layer” with “supply a proposed dynamical framing on the same operator family.”

**5. Surface Issues**

- Line 602 gives the wrong script path: it says `papers/paper-v/scripts/`; the relevant scripts are under `papers/paper-v-revisited/scripts/`.
- `N_8`, `N_9`, and `N_{11}` are undefined in Table `tab:chain`.
- The neutron formula needs unambiguous parentheses and must match the script.
- “10 chain ratios” is used where the table contains anchors, nine multiplicative coefficients, and one additive neutron correction.
- The long `tabular` in Table `tab:chain` is likely to overrun page width; use `tabularx` or paragraph columns.
- Line 568 says the exact forms come from “standard H4 spectral analysis,” but the actual import is via the 2I character-table computation in Paper II.

**6. Top Three Fixes**

1. Fix the chain claim at lines 41, 410, 433, 442, 446, 451, 578, 595, and 664. The current “10/10 forward derivation” language is not supported. State nine verified coefficient identities plus one phenomenological neutron correction.

2. Repair the neutron entry at lines 428, 442, and 446. As written, the mass-level EM-splitting formula has the wrong sign/behavior and does not cleanly match the script. This is the most serious mathematical defect in the new table framing.

3. Qualify the three-witness framing at lines 109, 123, 128, and 131. The closure-kernel and selection-layer papers support a shared-substrate narrative only with caveats; the b-anomaly primary paper is not locally verifiable; and “same shell decomposition” is too strong.
