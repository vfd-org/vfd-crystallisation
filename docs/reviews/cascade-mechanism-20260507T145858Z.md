Line refs below are to `papers/cascade-mechanism/cascade-mechanism.tex`.

**Claim Audit**

- L357 Definition: the cascade-closure event is stipulative. No proof issue.
- L386 Remark: clause (1) implies clause (2) is correct only under the stated finite-dimensional, boundaryless, unconstrained \(C^1\), \(R_k\ge0\) assumptions. The text states this adequately.
- L487 Proposition: proof establishes residual-zero and fixed-point propagation, conditional on both flow intertwining and monotonicity. No overclaim.
- L520 Corollary: proof establishes convergence only from a projected top-rung initial datum. It does not establish convergence of independently evolved lower-rung data. The text mostly preserves this.
- L627 API inheritance: acceptable only when the successor paper uses the projected initial tower. Add that phrase explicitly.
- L641-L652 vs L716-L724: main mathematical mismatch. The worked invocation first identifies \(R_k\) with P4’s full curvature residual on \(X_n=X_n^0\oplus X_n^1\), but the compat paper only proves O3 for the scaled scalar vertex-sector residual \(\widetilde R_n\) in the abstract pure-midpoint model. The O3 “closed” status does not apply to the P4 residual just identified unless the paper explicitly switches models.
- L660-L676 O1: spectral convergence for \(e^{-tA_N}\) is fine in finite-dimensional positive-semidefinite form. The nontrivial physical selection remains undisarged; the text says so.
- L677-L698 O2: correct. P4’s flow-intertwining theorem is mass-only and does not discharge curvature-flow O2.
- L804-L816 \(\|\Cphi^{-1}\|=\varphi^2\): proof by connected graph Laplacian bottom eigenvalue is valid.
- L777-L784 spectrum split: locally numerically supported and imported from P2 character-table material; not independently proved here. The paper states that.
- L897-L919 ARIA witness: imported and caveated; no cascade-event claim. Acceptable.
- L951-L976 b-anomaly witness: correctly scoped as external, commit-pinned, not locally re-executed.

**Internal Consistency**

- Stale compat section references: L99-L100, L130-L131, L721, L731-L732, L1010, L1075-L1077 cite `CascadeRefinementCompat` §1.5. In the current compat source, the L1-L3 scope gap is in `sec:scope-and-gap`, numerically §1.1, not §1.5.
- Wrong P4 label: L292, L1013, L1345 cite `prop:adjoint-refinement`; current P4 has `prop:mass-refinement`. I found no `prop:adjoint-refinement`.
- P4 parameter wording is stale: L306-L312 says P4 sets up \(\alpha,\beta,\gamma>0\) globally. Current P4 defines \(\alpha,\beta\ge0,\gamma>0\), with \(\alpha,\beta,\gamma>0\) only as the default working regime and \(\alpha=\beta=0\) explicitly named mass-only.
- All `\ref` and `\eqref` targets in this file resolve by static scan. Citation keys are present in `references.bib`.

**External Consistency**

- P3: `thm:bonding`, `thm:commute`, and `prop:adjoints` exist. But `thm:bonding` proves contraction of already-defined bonding maps; L327 should not say the maps are “constructed” by that theorem alone.
- P4: `thm:gradient-operator`, `prop:energy-dissipation`, `thm:coercive-contraction`, `thm:flow-exists`, and `thm:flow-intertwining` exist and have the stated scope. The mass-only restriction is verified. Replace `prop:adjoint-refinement` with `prop:mass-refinement`.
- Compat: verifies exactly what this paper now says in substance: O3 closed only in the abstract scalar pure-midpoint model; O2 as stated remains false; L1 and L3 are open; L2 is P3 `prop:adjoints`. The only stale part is section numbering and the residual/model mismatch noted above.
- P2/algebraic substrate: cited `thm:pi-H`, `thm:icosian-closure`, `thm:shell-class`, spectrum fact, and 94/26 split are present. Spectrum depends on imported \(2I\) character-table data, as this paper acknowledges.
- ARIA/closure-kernel sources: the cited numerical claims are present in local sources or frozen expected outputs. ARIA full validation is not re-executed here.
- b-anomaly: not in this repository. Only the secondary closure-kernel summary can be locally checked; the paper correctly says the primary fit is external.

**Tightness**

- L87: replace “the obligations discharge as follows” with “the obligation status is as follows.” O2 and nontrivial O1 are not discharged.
- L713: replace “in the imported P3/P4 finite-level tower” with “relative to the imported P3/P4 tower, and only after passing to the abstract scalar pure-midpoint model for the compat result.”
- L585: “selection-mechanism prerequisite” is too strong. Use “compatibility-template prerequisite.”
- L101: “L2 is already a theorem of P3” should be “already proved in P3, Proposition `prop:adjoints`.”

**Surface Issues**

- Wrong label: `prop:adjoint-refinement` should be `prop:mass-refinement`.
- Wrong manual section citation: `CascadeRefinementCompat` §1.5 should cite `sec:scope-and-gap` or current §1.1.
- “Conditional propagation lemma” in the abstract is a proposition/corollary package, not a lemma.
- “The paper is a mechanism paper, not a programme paper” conflicts tonally with “programme’s named dependency gate.” Say “not a programme survey.”

**Top Three Fixes**

1. Fix the worked-invocation model boundary at L641-L652 and L713-L744. State plainly that compat does not discharge O3 for P4’s full \(R_n\) on \(X_n^0\oplus X_n^1\); it discharges scaled vertex-sector O3 only in the abstract scalar pure-midpoint model.

2. Replace stale upstream citations: `CascadeRefinementCompat` §1.5 references at L99-L100, L130-L131, L721, L731-L732, L1010, L1075-L1077; `prop:adjoint-refinement` at L292, L1013, L1345.

3. Remove discharge overclaim language at L87-L96 and L1008-L1010. The current honest status is: O0 closed finite-dimensionally; O3 closed only in abstract compat scope; O2 false as stated with Schur substitute; O1 nontrivial selection open.
