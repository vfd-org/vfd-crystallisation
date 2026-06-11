**1. Claim Audit**

- “$L(\Theta_\Icos,s)=\zetaK(s)\zetaK(s-1)$ exactly” (line 47): supported by the local triad paper. This is verified there as Theorem `euler-bridge`. Claim is at the right strength.

- “$\zeta$ appears as one of its four factors” (line 48): correct, since $\zeta_K(s)=\zeta(s)L(s,\chi_5)$. No issue.

- “Hecke parameters are $a_q=N(q)+1$, which violate Ramanujan… therefore not a positivity-valid $L$-function, and is not where a Weil witness can live” (lines 49-51): over-strong. The Ramanujan failure is correct for treating these as unitary cuspidal GL(2)-type Satake parameters. But an Eisenstein product still has an explicit formula. Say it is not valid for the cuspidal Satake-angle residual used below, not that no Weil witness can live there.

- “Brandt eigenvalues… geometric and parameter-free… no point-counting and no fitting” (lines 53-57): supported for the Brandt construction path. Missing scope: level is the ideal $\mathfrak p_{31}=(5\varphi-2)$, and `geometric_aP.py` supplies only the cached finite prime set $N(\mathfrak q)\le150$ for the witness run.

- “These $a_q$ satisfy Ramanujan; this cuspidal face is positivity-valid” (line 58): under-justified as written. The local Brandt paper says Ramanujan is observed in computed values and follows globally only through the Hilbert modular/Jacquet-Langlands identification, not from finite self-adjoint Brandt matrices alone.

- Weil formula and criterion (lines 61-72): standard in spirit, but too schematic. “positive type” is undefined, the transform convention is unclear, and line 65 uses $\widehat h(\rho)$ while `weil_wall.py` computes sums of $h(\gamma)$ for zeros $\rho=1/2+i\gamma$. Needs a precise normalization and a citation to Weil.

- Proposition 2.1 (lines 74-78): mostly matches `weil_wall.py`: PRIME uses geometric Brandt coefficients, ARCH uses gamma factor/conductor, no zero data enters construction. But it is not proved in the note; it is asserted from code. Hidden inputs are the chosen level-31 Hilbert newform, conductor `775`, gamma type `[0,1,0,1]`, and the finite cache $N(\mathfrak q)\le150$.

- “Every ingredient… comes from the geometry” (lines 81-84): over-claim. PRIME comes from geometry; ARCH comes from the automorphic completion data. Unless the paper proves conductor/gamma factor as part of the same object, this must be weakened.

- Computed Result “calibration on $\zeta$” (lines 90-95): numerical values match `weil_wall.py`. But “identical machinery” is too strong: the zeta gate uses a different prime residual, pole term, and gamma factor. “Calibrates” should be “validates”; the code does not fit constants.

- Computed Result “positivity on every test” (lines 97-100): matches `weil_wall.py` for Gaussian tests $\sigma=3,4,5,6$ with $W=1.4047,3.6961,6.3931,9.4125$. The phrase is acceptable only because line 98 says “tried”; line 131 later drops that qualification.

- Computed Result “control has teeth” (lines 102-107): the 32 Ramanujan violations match the script. The conclusion “exactly what the witness requires” is too strong. The control only shows the Eisenstein bookkeeping coefficients are invalid for this cuspidal Satake-angle residual.

- Universal quantifier remark (lines 112-116): mostly correct and important. It correctly says this is GRH for the cuspidal L-function, not classical RH. The same precision is not preserved elsewhere.

- Archimedean-dominated remark (lines 119-125): honest and matches code. It should add that the PRIME term is truncated to the cached Brandt range and that no sharp test family is supplied.

- Conclusion/localization (lines 128-139): contains the main over-claim. “The gap between the constructed object and the Riemann Hypothesis is exactly one named inequality” (lines 134-135) conflates classical RH with GRH for the separate cuspidal L-function. Classical $\zeta$ sits in the Eisenstein face; the witness lives on the cuspidal face. This sentence must be rewritten.

**2. Internal Consistency**

- “RH” shifts meaning. Lines 36 and 135 read as classical RH; lines 69 and 113 mean RH/GRH for the chosen cuspidal L-function. Use “classical RH” only for $\zeta$, and “GRH for the cuspidal level-31 L-function” for the Brandt witness.

- $\sigma$ denotes Galois symmetry at line 28 and Gaussian test width at lines 93, 99, 121. Rename the test parameter, e.g. $\sigma_h$.

- “positive type” and “positivity-valid” are not defined. The second term is especially dangerous because it is doing real argumentative work.

- No `\ref` or `\eqref` occurs in this file, so there are no broken cross-references. The labels are unused. The bibliography item `Weil` is unused despite Weil’s criterion being invoked.

**3. External Consistency**

- `IcosianTriad`: verified locally. The triad paper states the exact identity at lines 734-743 and the four-factor decomposition at lines 770-777. It also explicitly says it does not address RH/GRH at lines 790-802.

- `BrandtCuspidal`: verified locally, with qualifications. The Brandt paper supports parameter-free construction and point-count comparison at lines 79-99, level-31 details at lines 267-282, and self-adjoint Brandt operators at lines 246-255. It also warns that finite Brandt data supply coefficients, not analytic positivity, at lines 511-521.

- `weil_wall.py` / `geometric_aP.py`: the manuscript’s numbers match the scripts. `geometric_aP.py` builds $N(\mathfrak q)\le150$ data; `weil_wall.py` hardcodes the level-31 completion data and tests only $\sigma=3,4,5,6$. The script itself states the archimedean-dominated caveat.

- There are no “Paper XVIII” or “Paper XXIX” style citations in this draft.

**4. Tightness**

- Lines 50-51: replace “not a positivity-valid $L$-function” with “not admissible as the unitary cuspidal Satake input used in the witness below.”

- Lines 75-78: add “for the finite prime cache used in the computation” and specify $N(\mathfrak q)\le150$.

- Lines 91-94: replace “calibrates” with “validates the implementation of the normalizations.”

- Lines 105-106: replace “exactly what the witness requires” with “the input required for this cuspidal Satake residual.”

- Lines 122-123: replace “consistent with RH” with “consistent with GRH for this cuspidal L-function.”

- Lines 134-136: replace with: “The localization is not a reduction of classical RH; after choosing the cuspidal Brandt face, the remaining wall is GRH for that cuspidal L-function.”

**5. Surface Issues**

- Line 48: write `L(s,\chi_5)`, not `L(\chi_5)`.

- Line 54: “level of norm 31” should specify the ideal $\mathfrak p_{31}=(5\varphi-2)$.

- Lines 61-70: define the admissible test class and Fourier convention.

- Line 65: likely should be phrased in terms of $h(\gamma)$ or carefully define evaluating $\widehat h$ at zeros.

- Line 67: add `\cite{Weil}`.

- Use $\mathfrak q$ rather than bare `$q$` for prime ideals.

**6. Top Three Fixes**

1. Fix the RH/GRH conflation, especially lines 122 and 134-136. The paper must not say the gap to classical RH is one cuspidal positivity inequality.

2. Scope Proposition 2.1 and the computed results to the actual finite computation: Gaussian tests $\sigma=3,\dots,6$, Brandt cache $N(\mathfrak q)\le150$, hardcoded conductor/gamma data, no tail bound.

3. Define and weaken the “positivity-valid” Eisenstein discussion at lines 50-51 and 103-106. The Eisenstein face fails the cuspidal Ramanujan/Satake-angle model; it is not thereby disqualified from all explicit-formula positivity language.
