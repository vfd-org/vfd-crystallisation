**Claim Audit**

Round 1 fixes mostly landed. Hypothesis 3.1 is now flow-intertwining, Proposition 3.1 uses it directly, Definition 2.1 is explicitly conditional, the E8 action overclaim is removed, the brain/EEG and SmartV scope rows are softened. Two fixes are incomplete: the shell/spectrum ledger row is not actually supported by Appendix A as written, and the finite-level import still overstates what the source proves for this paper’s \(R_k\).

- `R_k : \Phi_k \to [0,\infty)` and closure compatibility, lines 192-198: stated as a new residual functional, but the imported source at lines 200-204 proves results for a quadratic closure functional \(F_n=\alpha R_n+\beta E_n-\gamma Q_n\), not this non-negative \(R_k\). The import does not establish the construction of the present \(R_k\) without an identification lemma.

- “existence of a gradient flow, energy descent, and refinement compatibility”, lines 200-204: overbroad. `CascadeClosureDynamics` supports finite-dimensional flow existence and energy descent for \(F_n\), and mass-only refinement/flow intertwining. It does not give full refinement compatibility for arbitrary closure dynamics.

- Definition 2.1, lines 228-235: acceptable as a definition, not a theorem. Still under-specified: no topology/metric for convergence, no global product functional \(R\), and “gradient flow of \(R\) under \(\pi\)” is informal.

- Remark 2.3, lines 247-261: Round 1 fix landed. It correctly says conditional propagation, not existence.

- Hypothesis 3.1, lines 274-287: Round 1 fix landed. The mass-only source attribution is accurate. Minor issue: say “negative gradient flow” if descent is meant.

- Proposition 3.1, lines 295-306: proof sketch at 308-325 establishes the claim under global Hypotheses 3.1 and 3.2. If the phrase “at which Hypothesis 3.1 applies” is intended to allow partial/local assumptions, the statement is too strong: fixed-point propagation only passes through contiguous adjacent flow-intertwining steps.

- Carrier facts, lines 357-378: E8 projection wording is now source-faithful. But the shell/spectrum paragraph has three errors: “shell decomposition” is Euclidean/conjugacy shell, not graph-distance shell; the Laplacian has five integer eigenvalues including \(0\), not four; and \(\sigma:\varphi\leftrightarrow1/\varphi\) is wrong.

- \(\|\Cphi^{-1}\|=\varphi^2\), lines 382-391 and 546-548: established, conditional on the unweighted connected finite graph Laplacian with zero bottom eigenvalue. This claim is fine.

- ARIA empirical witness, lines 456-465: locally verified, but the text should say “18/18 after documented methodology refinement,” not just “18/18 at unchanged thresholds.”

- \(b\to s\mu^+\mu^-\) witness, lines 490-502: verified in the sibling `BANOMALY-001/vfd-b-anomaly` repo. The “AIC parity, not preference” boundary is correct.

**Internal Consistency**

- Lines 360-367 conflict with local substrate terminology. The sequence \((1,12,20,12,30,12,20,12,1)\) is the Euclidean/conjugacy shell sequence. The graph BFS shell sequence is \((1,12,32,42,32,1)\). Edit “shell decomposition” to “Euclidean distance/conjugacy-shell decomposition.”

- Line 364 has the wrong Galois action. Use \(\sigma(\varphi)=1-\varphi=-1/\varphi\), not \(1/\varphi\).

- Lines 362-366 omit the zero eigenvalue while counting the \(94/120\) fixed sector that includes it. Say “five integer eigenvalues \(\{0,9,12,14,15\}\), four nonzero.”

- Lines 367, 540-542 cite Appendix A for shell sizes and spectrum. Appendix A only states the \(94/26\) split and honest negative; Appendix E states shell sizes. The full nine-eigenvalue list is not in the appendix text.

- All explicit `\ref` targets in the file resolve. The A/E/F appendix subheads are unnumbered textual labels, not LaTeX reference targets; acceptable but brittle.

- Appendix runtime mapping, lines 656-673 and table 687-707, makes concrete upstream `ariaChessRepo` module claims while admitting no commit pin. The local `ariaChessRepo` directory is not present, so those module-level claims are not locally verifiable.

**External Consistency**

- `CascadeClosureDynamics`: verified for gradient operator, finite-dimensional flow existence, energy dissipation, coercive Euler contraction, and mass-only flow intertwining. Not verified for the present paper’s general \(R_k\), arbitrary-rung convergence, or full non-mass refinement compatibility.

- `CascadeRefinementSpaces`: verified for finite-level Hilbert spaces, bonding maps, contractions, and stated intertwinings.

- `CascadeAlgSubstrate`: verified for \(E_8\to H_4\) minimal-shell projection, \(V_{600}\cong2I\), Euclidean shell sizes, Laplacian spectrum, and \(94/26\) integer/irrational split. It contradicts the paper’s \(\sigma:\varphi\leftrightarrow1/\varphi\) notation.

- `AriaClosureKernel`: verified for \(\Cphi\), \(\|\Cphi^{-1}\|=\varphi^2\), unweighted correlation \(0.976\), weighted variants underperforming, and multi-source max-min \(\sim10^{-15}\).

- `SmartARIAChess`: verified for the ARIA empirical numbers, with the methodology-refinement caveat above.

- `SmartBAnomaly`: verified locally in sibling repo, not inside this repo. It supports five datasets, sign uniformity, one amplitude per dataset, and AIC indistinguishability.

- `SmartV`, `SmartVRev`: local files exist and contain the spectral mass-projection context. Current paper cites them only as out-of-scope context; that is acceptable.

**Tightness**

- Lines 148-153: “we offer a single named mechanism” is stronger than the math. Edit: “we define a candidate mechanism for systems satisfying the stated closure and projection hypotheses.”

- Lines 200-204: replace “construction of \(R_k\)” with “finite-dimensional closure-flow infrastructure for the source’s \(F_n\), used here as background.”

- Lines 456-465: add “after documented methodology refinement” and the HCP node-count caveat.

- Lines 481-485: “The shared layer is not the material; it is the process” is interpretive, not established. Edit: “The proposed common layer is process-level rather than material-level.”

- Lines 575-578: “mathematically explicit” is too strong until \(R_k\) is tied to the imported finite-level functional. Edit: “partly explicit, conditional on the stated residual and projection hypotheses.”

**Surface Issues**

- Line 364: wrong Galois conjugation sign.
- Lines 360 and 626: “shell sizes” should specify Euclidean/H3/conjugacy shells, not graph shells.
- Lines 362-366: missing zero eigenvalue.
- Lines 540-542: ledger cites the wrong appendix support.
- Lines 613-634: Appendix subsections jump A, E, F. Explain legacy audit lettering or renumber.
- Line 44: `Lee Smart\\Institute...` compiles, but `\\ Institute` is cleaner.
- No missing `\ref` labels found. No obvious undefined macros in the target file.

**Top Three Fixes**

1. Fix the \(R_k\) import gap at lines 192-204 and 228-235. Either define \(R_k\) as the imported \(F_n\)/residual component with hypotheses, or stop saying the source constructs this paper’s \(R_k\).

2. Correct the carrier paragraph at lines 360-367 and ledger row 540-542: Euclidean shells, five integer eigenvalues including zero, and \(\sigma(\varphi)=1-\varphi\).

3. Pin or remove unverifiable upstream runtime claims at lines 656-673 and 687-707, and qualify the ARIA empirical line 456-465 with the methodology-refinement and node-count caveats.
