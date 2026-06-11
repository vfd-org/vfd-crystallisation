**Claim Audit**

- Line 244: “A field state ... undergoes cascade closure ... if ... `lim R_k(\Phi_k(t))=0`.” This is a definition, not an existence theorem. It is acceptable only because lines 95-99 and 1188-1213 fence it as non-existence. However, the duplicate placeholder at lines 403-430 makes later references ambiguous.

- Lines 347-357: Hypotheses `\ref{hyp:ref-int}` and `\ref{hyp:monotone}` are stated, but `\pi^*_{k+1,k}` is type-inconsistent. Line 316 defines it as a pullback `\Phi_k -> \Phi_{k+1}`, while line 355 applies it to `\Phi_{k+1}`. The proposition depending on it is therefore not presently well-typed.

- Lines 359-364: “If the gradient flow of `R_N` has a fixed point ... then the projected states ... satisfy `R_k=0`.” The proof does not establish the stated claim as written. It silently needs a well-defined high-to-low projection/composite `\pi_{N,k}` and an induction from adjacent monotonicity. It also cites flow-intertwining too broadly: the local source proves this only in the mass-only case `\alpha=\beta=0`, not for the full residual.

- Lines 371-381: “This is exactly the flow-intertwining condition proved in Paper IV...” Over-claim. The cited source supports the mass-only finite-level construction; the paper must either restrict this sentence or leave it as a hypothesis.

- Lines 614-626: “visible states are residual-zero projections ... non-visible states are non-realised refinements.” This is explicitly interpretive and is fine as interpretation. It is not theorem-grade and should not be referenced as if numbered, because `interpretation` is unnumbered.

- Lines 684-694: “`C` implements the gradient flow toward a fixed point.” Not established. The ARIA sources support an observer-process / selector architecture, not equivalence with the cascade gradient flow in Definition 2.1. This should be “plays the role of” or “is modelled as”.

- Lines 727-732: “A 40ms primitive tick and `\lambda_\theta\simeq2.29` produce theta-band recurrence near 6 Hz.” Numerical claim lacks a displayed formula and the cited runtime source is not present locally. It cannot be verified from the repository as supplied.

- Lines 859-874: “18/18 ... 6/6 ... HCP ... `-11.58\sigma`.” The local ARIA chess source supports the 18/18 and 6/6 counts. The `-11.58\sigma` value is not a clustering result; the source associates it with degree homogeneity, while clustering is reported separately. Current wording misstates the metric.

- Lines 939-950: “b-anomaly closure kernel ... passive response layer.” The passive-response framing is correct and important. But primary b-anomaly fit claims cannot be locally verified: the repository contains secondary closure-kernel summaries, not the primary `BANOMALY-001` preprint.

- Lines 979-991: “exact rational matching of nine multiplicative chain coefficients ... thirteen mass correspondences.” Verified against the local Paper V Revisited source at the intended scope: numerical/rational correspondences, not a first-principles derivation of masses. The paper mostly preserves that limitation.

- Lines 1008-1018: `H_{\mathrm{Mill-Proj}}` is correctly stated as a hypothesis. This must remain so. The later Millennium table generally preserves delta/gamma/beta/coherence scope and does not claim Clay solutions.

- Lines 1048-1096: Millennium verdict table is mostly source-faithful. RH is delta-class with spec-to-zero conjectural; YM/NS are beta bridges; P vs NP is gamma; Poincare is coherence only. No upgrade to solved status found.

- Lines 1319-1392: The appendix reports audit-script outcomes. Since the review did not execute those scripts, these are repository-reported numerical claims, not independently checked computations. The honest negatives listed there are appropriate and should stay.

**Internal Consistency**

- Lines 202 and 403 duplicate `\label{sec:mechanism}`; lines 244 and 409 duplicate `\label{def:cascade-closure}`; lines 303 and 423 duplicate `\label{sec:rung-model}`. This is a serious LaTeX and logical defect: references may resolve to the TODO placeholder block, not the real definition.

- Lines 403-430 are an abandoned placeholder section inside the paper. It directly contradicts the polished sections around it and must be removed.

- Line 316 defines `\pi^*_{k+1,k}` low-to-high, but lines 355, 363, and 372 use it high-to-low. This is the main mathematical inconsistency.

- Line 642 and line 1222 reference `\ref{int:visible-non-visible}`, but the environment is defined with `\newtheorem*`, so it has no stable theorem number.

- Lines 1207 and 1231 use `\S\ref{def:cascade-closure}` and `\S\ref{hyp:mill-proj}` for a definition and hypothesis. Use `Definition~\ref{...}` and `Hypothesis~\ref{...}`.

- The claim ledger in Section 9 is mostly honest, but its references are compromised by the duplicate labels. That undermines the “not claimed” protection the section is supposed to provide.

**External Consistency**

- `CascadeClosureDynamics`: partially verified. Gradient flow and energy-dissipation material exist, but flow-intertwining is proved only in the mass-only case. Lines 371-381 overstate the imported scope.

- `CascadeRefinementSpaces`: verified for bonding maps/direct limits/refinement-space infrastructure. No major mismatch found.

- `CascadeCapstone`: verified. The four-phase/comonadic material is interpretive or conditional in the source, and the present paper mostly respects that.

- `CascadeAlgebraicSubstrate`: verified. The source explicitly treats `E_8 -> H_4` as projection, not inclusion. The present paper correctly says projection at line 491. Minor issue: the cited `prop:spectrum-P2` is a “Fact” in the source, not a proposition.

- `Cascade12D` / meta-layer sources: conditionally verified. The source depends on `H_min` and related hypotheses. The present table should cite these source hypothesis labels explicitly.

- Metric/hydrodynamic/phason projection sources: broadly verified as conditional finite/projection programs. The present table omits several source hypothesis labels, especially P5/P6 coordinate/separation/isotropy assumptions and hydrodynamic scaling hypotheses.

- ARIA chess source: verified as observer-process architecture / substrate witness, not consciousness proof. The paper correctly avoids a consciousness theorem, but lines 684-694 need weaker wording.

- ARIA six-module bundle: locally verified only as the in-repository bundle. The asserted upstream 88-module production architecture cannot be checked locally from this repository.

- b-anomaly: not locally verifiable at primary-source level. Only secondary closure-kernel claims are present.

- Millennium papers: verified at the stated conservative scope. No Clay solution claim found in this preprint.

**Tightness**

- Line 176: replace “positions them as case studies of a shared mechanism” with “positions them as case studies under a shared-mechanism hypothesis.”

- Lines 379-381: replace “known to hold for the P3/P4 finite-level construction” with “known in the mass-only P3/P4 finite-level construction; otherwise retained here as a hypothesis.”

- Lines 684-688: replace “implements the gradient flow” with “plays the role of a closure selector in the observer-process architecture.”

- Lines 727-732: either give the formula and source for the 6 Hz conversion, or demote to “is consistent with theta-band recurrence.”

- Lines 868-869: replace “clustering separates ARIA ... at `-11.58\sigma`” with “degree-homogeneity comparison places ARIA at `-11.58\sigma`, with the source’s node-count caveat.”

- Line 969: replace “jointly establish” with “jointly support, at substrate-witness scope.”

- Line 1258: replace “the mechanism is mathematically explicit” with “the response and residual components are mathematically explicit under the stated hypotheses.”

**Surface Issues**

- Remove the duplicate placeholder block at lines 403-430.

- Fix duplicate labels: `sec:mechanism`, `def:cascade-closure`, and `sec:rung-model`.

- Make `interpretation` numbered if it will be referenced, or stop referencing it numerically.

- Figure placeholder at lines 771-781 is not publication-ready.

- Bibliography path `\bibliography{references}` may fail if compiled from repo root rather than the paper directory.

- Several imported table entries need source hypothesis labels, not only paper names.

- “HCP clustering ... `-11.58\sigma`” is a metric-label error.

**Top Three Fixes**

1. Lines 403-430: delete the duplicate placeholder section and repair all affected references. This is the most immediate publication blocker.

2. Lines 316, 355-364, 371-381: repair the projection direction and proof of Proposition 3.3. As written, the statement is not well-typed and imports flow-intertwining beyond the source theorem.

3. Lines 684-694, 806-874, 939-950: harden ARIA and b-anomaly scope. ARIA is observer-process architecture, not consciousness proof or established gradient flow; the 88-module system is not locally verifiable; b-anomaly primary evidence is absent from this repo; and the HCP `-11.58\sigma` metric is mislabeled.
