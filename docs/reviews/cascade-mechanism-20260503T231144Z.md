Line numbers refer to `papers/cascade-mechanism/cascade-mechanism.tex`.

**Claim Audit**
- L77-80, “no nontrivial instance is shown here to satisfy all clauses”: established by inspection. The paper defines the event and proves only conditional propagation.
- L337-355, “clause (2) is implied by clause (1)” in the smooth unconstrained case: correct only with the added hypothesis “manifold without boundary.” That condition is not stated in the standing hypotheses at L225-239. Also both references to `ssec:closure-residual` are broken.
- L427-437, Proposition “Conditional closure-residual compositionality”: proof at L441-458 establishes exactly the two stated conclusions under Hypotheses 1 and 2. It does not establish existence, convergence, or occurrence of a cascade event; the paper correctly says so at L490-509.
- L460-475, Corollary “Convergence propagation”: proof at L477-488 establishes convergence only from projected top-rung initial data. It does not prove residual zero or fixed-point status unless Proposition L427-437 also applies.
- L532-556, finite carrier data: `|V|=120`, degree 12, shell sizes, nine Laplacian eigenvalues, and 94/26 split are not proved in this paper. They are imported and/or script-recorded. That is acceptable if kept as imported/numerical.
- L576-588, `||C_phi^{-1}|| = phi^2` exactly: established, assuming the stated connected unweighted graph Laplacian. This is an elementary spectral consequence, not merely a numerical witness.
- L589-595, per-vertex correlation uniform to `~10^-15`: numerically supported by the local `results.json`, but the present paper should say this is a multiplicity-weighted shell-radius correlation, not 119 independent radial samples.
- L667-685, ARIA empirical profile: not proved or re-executed here. The source paper contains the reported 17/18, 18/18, P10 caveat, seed-42 EEG, and HCP sigma numbers. The caveats are mostly carried.
- L717-741, b-anomaly witness: primary source is external to this repository. The paper admits this, so the claim is scoped correctly, but it is not locally auditable.
- L935-1011, ARIA runtime mapping: Tier 1 module existence is locally verifiable. Tier 2 module claims are not locally verifiable from this repository.

**Internal Consistency**
- Broken references: L338 and L351 cite `\ref{ssec:closure-residual}`, but the closure-residual subsection at L204 has no label.
- The standing hypotheses L225-239 do not explicitly say “without boundary,” but L337-355 relies on that.
- `R_k` is introduced as an arbitrary residual functional at L211-217, while L253 calls it the residual component of the imported P4 construction. This is only consistent under the finite-level imported specialization; say that explicitly.
- L817-821 says projection-compatibility “propagates downward.” In the proof, projection-compatibility is built into the definition `phi_k := pi_{N,k} phi_N`; it is not a dynamical consequence of the hypotheses.
- No `\eqref` references are present. All visible `\ref` targets resolve except `ssec:closure-residual`.

**External Consistency**
- `CascadeClosureDynamics` at L241-267, L396-419, L490-515: verified locally. The cited source proves the listed gradient-flow facts for its finite quadratic `F_n`, and flow intertwining only in the mass-only case. Current paper states that limitation correctly.
- `CascadeRefinementSpaces` at L264-284 and L773-775: verified locally. The source constructs specific `p^0`, `p^1` bonding maps and specific Coxeter/sigma identities, not generic bonding identities; current paper correctly limits the import.
- `CascadeAlgSubstrate` at L532-572 and L776-784: verified locally for `E8 -> H4`, `2I`, shell-class, and 94/26 decomposition. The spectrum in that source is itself an imported character-table fact, not newly proved there; current paper mostly states this.
- `AriaClosureKernel` at L538, L582-595, L949-950: verified locally for degree, operator norm, correlations, and weighted-variant underperformance. Add the shell-correlation caveat.
- `SmartARIAChess` at L667-685 and L794-796: verified locally as reported claims, not independently re-run.
- `ariaChessRepo` at L689-692 and L953-970: not locally verifiable; the cited production snapshot is outside this repository.
- `SmartBAnomaly` at L717-741 and L797-799: primary paper/repo not local. Only secondary summaries in this repository support the framing.
- `SmartV`, `SmartVRev` at L837-840: locally present; the current paper cites them only as out-of-scope context, which is acceptable.

**Tightness**
- L62-64: replace “candidate generalisation” with “candidate structural analogue.” A generalisation should include OR as a recoverable case; this paper explicitly does not.
- L589-595: replace “per-vertex correlation” with “multiplicity-weighted shell-radius per-vertex correlation.”
- L727-730: replace “physical example” with “external-use example” unless the b-anomaly primary analysis is included or locally audited.
- L817-821: replace “projection-compatibility propagate downward” with “projection-compatibility is inherited by the projected tower.”
- L696: replace “strongest form the data supports” with “strongest form the cited data supports,” since the present manuscript does not rerun the ARIA validation.

**Surface Issues**
- Add `\label{ssec:closure-residual}` at L204 or change the two references.
- Define `2T` before L609.
- Expand AIC and HCP at first use.
- “test P10” at L675 is opaque without source context; call it “the source’s test P10.”
- Appendix entry labels `app:fsa-A`, `app:fsa-E`, `app:fsa-F` exist but are not used; prefer direct references where possible.

**Top Three Fixes**
1. Fix the broken cross-reference and missing boundary hypothesis: L204, L225-239, L338, L351.
2. Demote or make locally auditable the external witness/runtime material: b-anomaly primary at L717-741 and ARIA Tier 2 at L953-970, L984-1004.
3. Tighten the mechanism and numerical wording: OR “generalisation” at L62-64, shell-correlation wording at L589-595, and projection-compatibility “propagation” at L817-821.
