**1. Claim Audit**

- “cascade-closure event … occurs … when … flows … converge … to a limit point” (l.301-327). This is a definition, not a theorem. Coherent, but it defines occurrence rather than proves any occurrence or selection mechanism.

- “Conditional closure-residual compositionality” (l.399-409). The proof at l.413-430 establishes the stated residual-zero and fixed-point propagation under the two hypotheses. However, under the standing assumptions \(R_k\in C^1\) and \(R_k:\Phi_k\to[0,\infty)\) (l.205, l.218-225), \(R_k(\phi)=0\) already makes \(\phi\) a global minimum, hence \(\nabla R_k(\phi)=0\) on a smooth manifold without boundary. Then fixed-point invariance follows from residual-zero alone. If boundary/constrained/nonsmooth cases are intended, they must be stated.

- “Convergence propagation under flow intertwining” (l.432-445). The proof at l.447-456 establishes exactly the stated convergence from a projected top-rung initial datum. It does not establish zero residual, fixed-point status, or occurrence of Definition 3.1 unless combined with extra hypotheses. Also \(\phi_k^\star\) is used at l.444 without being redefined inside the corollary.

- “\(\Vsub\) … uniform vertex degree \(12\)” (l.501-508). Supported by the local closure-kernel results, not proved in this paper. Acceptable as imported/numerical, but it should be labelled consistently as reproduced computation.

- “Euclidean shell sizes … \((1,12,20,12,30,12,20,12,1)\)” (l.511-517). Verified in `CascadeAlgSubstrate`; the extension from identity shells to arbitrary source vertices is a valid inference from the group/left-translation structure, but it is not the literal theorem statement cited.

- “The graph Laplacian \(L\) has nine distinct eigenvalues … split \(94/120\), \(26/120\)” (l.518-525). Verified as an imported character-table fact plus numerical reproduction. The manuscript correctly avoids presenting this as a fresh proof.

- “\(\|\Cphi^{-1}\|=\varphi^2\) exactly” (l.551-556). The analytic proof works if \(L_M\) is the connected unweighted graph Laplacian: \(\lambda_{\min}(L_M)=0\), so \(\lambda_{\min}(L_M+\varphi^{-2}I)=\varphi^{-2}\). Wording should distinguish “numerically reproduced” from “proved exactly.”

- “per-vertex correlation … uniform across the 120 source-vertex sweeps” (l.557-562). Supported by `results.json`; correctly called a numerical diagnostic, not a convergence theorem.

- “\(17/18\) … and \(18/18\) after documented methodology refinement” (l.639-642, repeated l.759-761 and l.863-866). The cited ARIA paper supports the numbers, but the present manuscript omits a material caveat from that source: P10 was validated with 15 permutations rather than the preregistered 20, with the prereg-exact rerun left open. This is an over-clean import.

- “HCP … ARIA at \(-11.58\sigma\) … clustering \(+6.80\sigma\)” (l.644-648, l.869-873). Verified in the ARIA paper. The node-count caveat is included; this is acceptable as an imported descriptive statistic.

- “\(b\to s\mu^+\mu^-\) … AIC-inconclusive … \(w_{\mathrm{FREE\_C9}}=0.652\), \(w_{\mathrm{VFD}}=0.348\)” (l.682-689, l.762-764). Verified in the sibling `BANOMALY-001/vfd-b-anomaly` checkout, not inside this repository. The caveat is correctly stated.

**2. Internal Consistency**

- All `\ref`/`\eqref` targets used in the manuscript are defined. All cited bibliography keys used in this file are present in `references.bib`.

- The relation between “zero residual” and “flow invariance” is internally under-explained. With \(R_k\ge0\) and \(C^1\) on a smooth manifold (l.205, l.218-225), clause (2) of Definition 3.1 (l.319-321) follows from clause (1) (l.318), unless boundary/constrained dynamics are intended.

- The paper repeatedly calls this “state selection” (e.g. l.52-55, l.809-815), but the formal result begins with a top-rung fixed point already supplied (l.401-404). The mathematics propagates compatibility; it does not select the fixed point.

- The `CascadeRefinementSpaces` description at l.271-277 is imprecise: `thm:commute` is not a commutation theorem “between the specific maps \(p^0\) and \(p^1\).” It is a set of refinement-Coxeter, refinement-\(\sigma\), and restricted Coxeter-\(\sigma\) intertwining identities for those source maps.

**3. External Consistency**

- `CascadeClosureDynamics` claims at l.234-260 and l.737 are verified: the cited source contains `thm:gradient-operator`, `prop:energy-dissipation`, `thm:coercive-contraction`, `prop:adjoint-refinement`, `def:refinement-compat`, `thm:flow-exists`, and mass-only `thm:flow-intertwining`. The target correctly notes that full flow-intertwining is not imported outside the mass-only case.

- `CascadeRefinementSpaces` claims at l.264-286 and l.738-740 are mostly verified. The source defines \(p^0,p^1\) and proves contraction/bonding properties. But the target’s shorthand “existence of downward bonding maps” for `thm:bonding` is loose; the theorem proves contractions after the maps are defined.

- `CascadeAlgSubstrate` claims at l.501-541 and l.741-749 are verified: \(E_8\to H_4\) projection, icosian closure, shell-class theorem, and character-table spectrum are present. The source itself treats the spectrum as imported character-table data, which the target correctly preserves.

- `AriaClosureKernel` supports the degree, shell, spectrum, norm, correlation, and weighted-variant negative claims at l.507, l.551-562, and l.849-859.

- `SmartARIAChess` supports the broad ARIA numbers, but the import is incomplete because the P10 prereg-exact caveat is not carried over.

- `SmartBAnomaly` is not a paper inside this repository. A sibling checkout exists at the pinned commit and supports the AIC/sign-uniformity claims, but repository-local verification is not possible from this repo alone. The manuscript admits this at l.699-706.

**4. Tightness**

- l.52-55: “state selection … until … fixed point is selected” is too strong. Suggested edit: “a formal compatibility template for propagating a supplied closure-compatible fixed point through a projection stack.”

- l.70-73: “mathematical payload … definition plus conditional propagation lemma” is accurate and should control the title/closing language.

- l.344-355: good caveat; keep it.

- l.551-552: “Direct computation … gives … exactly” mixes numeric and analytic claims. Suggested edit: “Direct computation reproduces the value; exactness follows analytically from…”

- l.914-919: “immutable working-tree snapshot” is stronger than a directory snapshot without an internal checksum or git commit. Suggested edit: “frozen working-tree snapshot.”

**5. Surface Issues**

- l.57: awkward grammar: “model that this paper is proposed as…” Suggested edit: “model for which this paper is proposed as…”

- l.271-277: rewrite the `thm:commute` description; current wording misdescribes the source theorem.

- l.432-445: define \(\phi_k^\star:=\pi^\sharp_{N,k}\phi_N^\star\) inside the corollary.

- l.897: “six `.py` modules” ignores `__init__.py`; harmless, but say “six substantive modules” if precision matters.

- No undefined macros or unresolved local references found by static extraction. I did not run LaTeX because this environment is read-only and compilation would write aux files.

**6. Top Three Fixes**

1. Fix the core mathematical framing: the paper proves propagation from an already supplied top fixed point, not state selection. Either add a nontrivial instance satisfying Definition 3.1 or downgrade “state-selection mechanism” throughout, especially l.52-55 and l.809-815.

2. Clarify zero-residual versus fixed-point invariance. Under l.205 and l.218-225, clause (2) and part of Proposition 3.4 are redundant unless boundary/constrained/nonsmooth cases are intended. State the intended analytic setting.

3. Carry over the missing ARIA caveat. The imported “18/18” claim at l.639-648, l.759-761, and l.863-866 should mention the P10 15-vs-20 permutation prereg-exact rerun issue from the cited ARIA paper.
