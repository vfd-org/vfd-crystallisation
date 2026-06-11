**1. Claim Audit**

- “A cascade closure is a triple … such that the gradient flow of \(R\) … converges to a fixed point … and \(R_k(\phi_k^\ast)=0\)” (`cascade-mechanism.tex:235-241`). This is a definition, not a theorem. It is acceptable as stipulated terminology, but the paper has not defined a global \(R\) or a global gradient flow on the tower; only the family \(R_k\) is defined. Add the ambient product space / compatibility structure or say “the family of negative-gradient flows”.

- “Imported finite-dimensional closure-flow infrastructure” for \(F_n=\alpha R_n+\beta E_n-\gamma Q_n\) (`200-215`). Verified locally in `cascade-closure-dynamics`. The rewritten caveat is correct: that source does not prove results for the arbitrary residual \(R_k\) used here.

- Hypothesis 3.1 (`281-294`) is properly marked as a hypothesis. The “negative-gradient flow” wording has landed. The cited source only proves mass-block intertwining; this paper correctly does not import that as a general theorem.

- Proposition 3.1 (`302-317`). The proof establishes the stated conditional claim under Hypotheses 3.1 and 3.2. It does not establish convergence, existence of a closure point, or applicability of the hypotheses to the carrier. The partial-hypothesis caveat in part (2), `310-315`, is mathematically reasonable but belongs in a remark, because it is not a second proved assertion unless all lower-step hypotheses are restated precisely.

- “\(V_{600}\) is canonically isomorphic to the binary icosahedral group \(2I\)” and the shell/eigenvalue data (`368-393`). Verified against the algebraic-substrate paper and the local spectrum script. The Round 2 corrections landed: five integer eigenvalues including \(0\), Euclidean/conjugacy shells, and \(\sigma(\phi)=1-\phi=-1/\phi\). One weakness remains: “Cayley graph … on a generating icosahedral conjugacy class” (`371-372`) is not explicitly proved in the cited passage; it is inferable from the nearest-neighbour shell and connectedness, but should be stated as such or cited directly.

- “\(\|\Cphi^{-1}\|_2=\phi^2\)” (`397-404`). Established, assuming the unweighted connected Laplacian with lowest eigenvalue \(0\). The local `results.json` agrees numerically. This is one of the cleanest claims in the paper.

- “Per-vertex correlation … uniform across all vertices” (`407-409`). Supported as a numerical claim for the unweighted operator, but only as a finite-carrier computation. Keep “empirical/computational” language.

- ARIA empirical witness claims (`471-480`). Verified in the ARIA chess paper. The Round 2 caveats landed in the main text: documented methodology refinement and the HCP node-count caveat are present. Appendix F does not carry the node-count caveat (`668`), so the caveat is not propagated consistently.

- “B-anomaly … sign-uniform structural witness” (`506-518`). Verified in the sibling `BANOMALY-001/vfd-b-anomaly` source. The statement that the primary fit is not rerun here is important and correct. “AIC parity, not AIC preference” (`511`) is slightly too soft: the source reports no decisive VFD preference and a mild FREE_C9 weight advantage. Say “AIC-inconclusive, with mild FREE_C9 weight.”

**2. Internal Consistency**

- The Round 2 fixes mostly landed: \(R_k\) import boundary (`200-215`), carrier spectrum/shell corrections (`371-379`, `637-653`), ARIA caveat in the main text (`473-480`), Hypothesis 3.1 wording (`284`), Proposition 3.1 partial-step clarification (`310-315`), and appendix lettering explanation (`629-633`).

- “Compositionality lemma” (`78`) conflicts with the labelled environment, which is Proposition 3.1. Use “proposition” consistently.

- `\Phi_k` is called a “state space” in the definition (`187-198`), but line `196` says the functional measures failure of `\Phi_k` to be closure-compatible. That should be the state \(\phi_k\), field configuration, or projection, not the state space itself.

- “If each adjacent projection is closure-compatible” (`273-276`) uses terminology not formally defined there. The proposition actually assumes monotonicity and flow intertwining. Replace the informal phrase with the formal hypotheses.

- Appendix A in the TeX is updated, but `papers/cascade-mechanism/FIELD_SIGNATURE_AUDIT.md` still contains the stale “four integer eigenvalues” wording. Since line `629` points readers to that file, this is a real consistency problem.

- Appendix F repeats “ARIA at \(-11.58\sigma\)” (`668`) without the node-count caveat present in the main text. That weakens the Round 2 fix.

**3. External Consistency**

- `CascadeClosureDynamics` claims are verified: finite-dimensional \(F_n\), gradient flow, dissipation, coercive contraction, and mass-only refinement compatibility exist there. The present paper correctly refrains from importing arbitrary-\(R_k\) theorems.

- `CascadeRefinementSpaces` imports are verified: bonding maps and Coxeter/\(\sigma\) intertwinings are present.

- `CascadeAlgSubstrate` imports are verified for \(E_8\to H_4\), \(V_{600}\cong 2I\), shell/conjugacy structure, spectrum, and 94/26 rational/irrational split. The “generating conjugacy class” phrase needs either a direct citation or a proof sentence.

- `AriaClosureKernel` supports the \(C_\phi\) operator norm and correlation claims. I verified the existing local result data; I did not rerun the script because the workspace is read-only and the script writes outputs.

- `SmartARIAChess` supports 18/18 after methodology refinement, six drug/sleep signatures, and HCP \(-11.58\sigma\) with the 120-vs-50 node-count caveat. The main text reflects this; Appendix F does not.

- `SmartBAnomaly` supports the sign-uniformity and unweighted-kernel witness framing, with the explicit limitation that AIC does not prefer VFD. The paper’s “not re-executed here” caveat is necessary and correct.

**4. Tightness**

- `177-181`: Replace “The four terms describe the same physical event” with “Within this vocabulary, the four terms name complementary aspects of the same proposed event-type.”

- `273-276`: Replace “if each adjacent projection is closure-compatible” with “if each adjacent projection satisfies the monotonicity and flow-intertwining hypotheses below.”

- `417-419`: Replace “sets the relaxation scale” with “sets an operator response scale.” The paper has not derived a dynamical relaxation time.

- `493-501`: Replace “brain-wave signatures are biological telemetry” with “brain-wave signatures are treated here as candidate biological telemetry.”

- `511`: Replace “AIC parity, not AIC preference” with “AIC-inconclusive, with mild FREE_C9 weight; not a VFD preference.”

- `568-570`: The ledger row is too compressed. Add “single deterministic seed, documented methodology refinement, and HCP node-count caveat.”

**5. Surface Issues**

- `78`: “lemma” should be “proposition.”

- `196`: `\Phi_k` is the wrong object for “failure”; use \(\phi_k\) or “configuration”.

- `556-558`, `629-633`: “Appendix A/E/F” are unnumbered lettered entries inside one appendix, not labelled subsections. Add labels for A/E/F or call them “Appendix entries A/E/F”.

- `637-641` vs `FIELD_SIGNATURE_AUDIT.md`: TeX says five integer eigenvalues including \(0\); the audit markdown still says four. Update the markdown or stop citing it as the detailed audit.

- `668`: Appendix F omits the HCP node-count caveat.

- `697-701`: The paper admits no pinned commit hash for `ariaChessRepo`. That is acceptable as a draft caveat, but not publication-ready evidence.

**6. Top Three Fixes**

1. Fix the formal object of the cascade flow: define the global residual/flow structure or rewrite Definition 3.1 and Proposition 3.1 in terms of the family \(\{R_k\}\) and its rungwise flows (`235-241`, `281-317`).

2. Propagate empirical caveats everywhere the empirical claims are repeated: Appendix F needs the ARIA node-count caveat (`668`), and the ledger should include methodology refinement, single-seed status, and node-count caveat (`568-570`).

3. Make the cited evidence auditable: pin the ARIA runtime repository commit (`697-701`) and update the stale `FIELD_SIGNATURE_AUDIT.md` spectral wording referenced by the appendix (`629`, `637-641`).
