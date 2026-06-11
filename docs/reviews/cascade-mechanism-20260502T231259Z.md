**1. Claim Audit**

- “prove a conditional residual-compositionality proposition” (l.61-62; claim at l.345-358). Established, but only in the narrow sense stated: residual-zero and fixed-point propagation downward from an already-given top fixed point. The proof at l.362-378 is valid under Hypotheses 3.1 and 3.2. It does not prove existence, convergence from data, or occurrence of a cascade event; the paper correctly says this at l.381-400.

- “flow intertwining implies operator intertwining … in the sense of [source] `def:refinement-compat`” (l.331-337). Over-strong. Differentiating a nonlinear residual flow gives vector-field/generator compatibility, not the bounded linear operator intertwining of the cited definition unless the residual gradients are linear operators. Add that extra hypothesis or rephrase.

- “if some intermediate step lacks flow intertwining…” inside the proposition statement (l.353-358). This discusses a case outside the proposition’s hypotheses. Move it to the following remark or state a separate partial-propagation lemma.

- “$\Vsub$ … 120 vertices … degree 12 … shell sequence … nine distinct eigenvalues … $94/26$ split” (l.417-435). Supported by the cited algebraic-substrate source and local result files. Caveat: the spectrum is an imported character-table computation in the source, not a new theorem of this paper.

- “$\|\Cphi^{-1}\|=\pphi^2$ exactly” (l.67-68; l.461-464; l.627-629). Established, provided $L_M$ is the unweighted graph Laplacian. The analytic argument from $\lambda_{\min}(L_M)=0$ and the shift by $\pphi^{-2}$ is sufficient.

- “per-vertex correlation … uniform across all 120 vertices” (l.465-467; l.724-726). Supported by existing `results.json`; I did not rerun the script because `verify_kernel.py` writes `results.json` and this workspace is read-only.

- “$\sigma$-fixed eigenvectors do not preferentially localise on $2T$” (l.480-483; l.711-714). Supported as a numerical diagnostic by the local script. Wording should be “eigenspaces/modes” rather than “eigenvectors” if counting multiplicities.

- “ARIA … $18/18$ … six drug/sleep EEG signatures … $-11.58\sigma$” (l.531-541; l.732-741). Verified against `papers/aria-chess-paper/paper/main.tex` and sections. The methodology-refinement and single-seed caveats are present.

- “$b\to s\mu^+\mu^-$ … sign-uniform … AIC-inconclusive” (l.569-576; l.636-638). Supported by the sibling `../BANOMALY-001/vfd-b-anomaly` checkout, but not by a paper inside this repository. The current wording is appropriately caveated.

- “runtime module mapping … audited 2026-05-02 … locked branch” (l.762-779; table l.793-813). File names exist in the sibling `../aria-chess/v4_locked_2026-04-29/` directory. However, `../aria-chess` is not a git checkout, so neither branch identity nor commit identity is locally verifiable. This is not publication-grade provenance.

**2. Internal Consistency**

- All `\ref` labels and citation keys exist. Static scan found no missing labels or missing `.bib` keys.

- The Appendix A/E/F cross-references are broken semantically. Labels placed after `\subsection*` at l.704, l.720, and l.732 will not produce distinct reference numbers; `Appendix~\ref{app:fsa-E}` will likely print the parent appendix section number, not “E”. Fix by citing “Appendix~\ref{app:field-signature-audit}, entry E” or by making A/E/F actual numbered/custom-refstepped entries.

- “finite-dimensional smooth (or Hilbert) manifold” (l.202-203) is ambiguous. A Hilbert manifold is usually not finite-dimensional. Say either “finite-dimensional smooth manifold with a chosen Riemannian metric” or explicitly allow Hilbert manifolds while retaining flow existence as a hypothesis.

- The source asymmetry between $F_n$ and this paper’s $R_k$ is mostly fixed. The remaining weak point is l.331-337, where nonlinear residual-flow compatibility is still blurred with linear operator compatibility.

**3. External Consistency**

- `CascadeClosureDynamics` (l.214-222, l.326-337, l.612-614): verified locally. It proves gradient operator, flow existence, energy dissipation, coercive contraction, and mass-only flow intertwining for its quadratic $F_n$. It does not prove arbitrary residual-flow intertwining for this paper’s $R_k$.

- `CascadeRefinementSpaces` (l.227-230, l.615-617): verified locally for finite-level Hilbert spaces, bonding maps, and commuting identities.

- `CascadeAlgSubstrate` (l.417-451, l.618-620): verified locally for $E_8\to H_4$ projection, $V_{600}\cong 2I$, shell-class decomposition, icosian closure, and the $94/26$ split. The spectrum depends on imported $2I$ character-table data, as the source says.

- `AriaClosureKernel` (l.767): verified locally for the unweighted $\Cphi$ kernel, operator norm, correlation values, and weighted-variant negative result.

- `SmartARIAChess` (l.493, l.532-541, l.633-635, l.767-768): verified locally for the empirical numbers and caveats.

- `ariaChessRepo` (l.545-547, l.762-779): module files exist in the sibling directory, but no git commit can be verified. The branch-pin caveat is honest but not sufficient for publication.

- `SmartBAnomaly` (l.569-583, l.636-638): not in this repository. Sibling checkout supports the stated AIC/sign-uniformity claims. If repository-local verification is required, this remains external.

- `SmartV`, `SmartVRev` (l.674-675): local files exist; current paper uses them only as out-of-scope context. No load-bearing inconsistency found.

**4. Tightness**

- l.119-124: “neither supplies a mechanism” is too broad. Edit: “the projection postulate specifies the update rule, not a substrate-level selection mechanism.”

- l.166: “ours is one further example” overstates physical establishment. Edit: “ours is proposed as a further substrate-geometry parametrisation.”

- l.331-337: replace with “flow intertwining differentiates to vector-field compatibility; in the linear finite-level setting this reduces to operator intertwining.”

- l.491-498: “The mechanism admits a computational implementation” is stronger than the ARIA evidence. Edit: “The observer-process architecture admits an implementation-level mapping.”

- l.567-578: “couples to an external observable” is a little strong. Edit: “has been used as a fixed-kernel structural witness against an external observable.”

**5. Surface Issues**

- l.432: “counting eigenvectors with multiplicity” should be “counting eigenvalue multiplicities” or “counting eigenspace dimensions.”

- l.465: “continuum Green response” is not defined in this paper. Give the formula or point to the closure-kernel paper.

- l.494 and l.512: inconsistent slash style: “realisation / mapping”, “closure / crystallisation”. Use either spaced prose or compact slashes consistently.

- l.704, l.720, l.732: `\subsection*` plus `\label` is not enough for meaningful `\ref` output.

- `references.bib` l.162-168 uses document-local `\ref{sec:aria}` and `\ref{app:aria-runtime-map}` inside a bibliography note. It may compile here, but it is bad bibliographic hygiene and non-portable.

**6. Top Three Fixes**

1. Fix Appendix A/E/F references (l.704, l.720, l.732 and all uses such as l.435, l.461, l.533, l.623). Current refs will not identify entries A/E/F as the prose implies.

2. Repair the flow-to-operator statement (l.331-337). The current sentence still conflates nonlinear residual-flow generator compatibility with the linear operator-intertwining definition imported from `CascadeClosureDynamics`.

3. Pin `ariaChessRepo` to a real commit hash and URL before publication (l.762-779; table l.793-813; `.bib` l.162-168). A branch/directory name is not stable evidence.

Publication ready: No.
