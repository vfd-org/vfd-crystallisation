**Claim Audit**
- l.227-233, “A cascade-closure event … converges to a fixed point … with `R_k=0`”: definition only. No theorem is being proved, and the text mostly respects that.
- l.253-256, “Conditions under which a specific instance does admit convergence are stated below…”: false. Hypotheses 3.1-3.2 plus Proposition 3.1 do not give convergence; Proposition 3.1 assumes convergence at rung `N`.
- l.282-291, Proposition 3.1: part (1) is established by Hypothesis 3.2 alone. Part (2) uses Hypothesis 3.1, but only if “commutes with gradient operator” is strong enough to imply flow-intertwining. As written, the proof imports a stronger condition than the hypothesis states.
- l.283-291: Hypotheses 3.1 and 3.2 are both load-bearing for the combined proposition, but not for each subclaim: monotonicity proves residual-zero propagation; refinement intertwining proves fixed-point propagation.
- l.199-206, imported gradient-flow infrastructure: locally verified in `cascade-closure-dynamics`, but the cited list omits `thm:flow-exists`; “refinement compatibility” is mass-only in the source, not generic.
- l.339-349, 600-cell graph, shell sizes, spectrum, `94/26` split: locally verified. However the ledger cites only `thm:pi-H` and `thm:icosian-closure`, not the actual spectrum/shell results.
- l.351-355, “`E_8` acts on `V_600` via the projection `E_8 -> H_4`”: overclaim. The cited source supports a projection/minimal-shell image, not an `E_8` action on `V_600`.
- l.359-369, `||C_phi^{-1}|| = phi^2` and uniform correlation: locally supported by `verify_kernel.py` / `results.json`. “Exactly to machine precision” is sloppy: either prove exactness from the shifted Laplacian spectrum or call it numerical.
- l.403-414, observer-process tuple: definition only. Fine.
- l.417-426, “The tuple realises the cascade-closure mechanism”: too strong. The text later says it only models the gradient flow; call this an architectural implementation, not a realisation of Definition 3.1.
- l.430-439, ARIA empirical witness: verified in `aria-chess-paper`; the source itself carries single-seed and substrate-witness caveats. The present paper preserves the “not consciousness” boundary.
- l.464-482, b-anomaly witness: verified in the sibling `BANOMALY-001/vfd-b-anomaly` checkout. The draft correctly keeps this at AIC parity, not preference, and restricts it to the unweighted operator.
- l.558-567, out-of-scope paragraph: mostly successful. The phrase “citing this one as the mechanism prerequisite” for SmartV/SmartVRev is not locally verified; those papers do not appear to cite this paper.
- l.629-685, ARIA runtime mapping: Tier 1 files exist in the repo bundle; Tier 2 files exist in sibling `aria-chess`, including a `v4_locked_2026-04-29` tree, but the bibliography gives no URL or commit hash. This is not publication-grade traceability.

**Internal Consistency**
- l.87 and l.529 say “brain / EEG” applications are out of scope, while l.430-439 and l.605-613 use brain/EEG evidence as the ARIA witness. Revise to “standalone brain/EEG applications beyond the ARIA witness.”
- l.225 defines `pi^\sharp_{N,k}` by a composite but never defines the identity case `pi^\sharp_{N,N}`.
- l.269-274 states operator intertwining; l.302-305 uses flow intertwining. These are not the same hypothesis unless linearity/smoothness and flow existence are made explicit.
- l.278, “every `\Phi_{k+1} \in \Phi_{k+1}`” uses the same symbol for state and state space.
- Source scan found all local `\ref` targets in this file. I could not run LaTeX because the filesystem sandbox is read-only and even `/tmp` is not writable.

**External Consistency**
- `CascadeClosureDynamics`: labels for gradient operator, energy dissipation, coercive contraction, refinement compatibility, flow existence, and flow intertwining exist. But `thm:flow-intertwining` is explicitly mass-only; generic use must remain a hypothesis.
- `CascadeRefinementSpaces`: `thm:bonding` and `thm:commute` exist and support the imported bonding/commutation infrastructure.
- `CascadeAlgSubstrate`: verifies `E_8 -> H_4` projection and `V_600 = 2I`, and separately verifies shell/spectrum data. It does not support “`E_8` acts on `V_600`.”
- `SmartARIAChess`: supports `18/18`, `6/6`, HCP `-11.58 sigma`, and `+6.80 sigma`, with caveats. It does not claim consciousness.
- `AriaClosureKernel`: supports the unweighted `C_phi` kernel, `0.976` per-vertex correlation, weighted variants underperforming, and operator-witness scope.
- `SmartBAnomaly`: not inside this repo, but present as sibling checkout. It supports five-dataset sign uniformity and explicitly says AIC is unresolved: `w_VFD=0.348` vs `w_FREE_C9=0.652`.
- `SmartV` / `SmartVRev`: support mass-spectrum material as conditional numerical correspondence / interpretive spectral-projection class. They do not verify the “citing this one” claim.

**Tightness**
- l.253: replace with “Compositional propagation, conditional on top-rung convergence, is stated below…”
- l.351: replace “`E_8` acts on `V_600` via the projection” with “the `E_8` minimal shell projects onto the `H_4` / `V_600` carrier.”
- l.366: replace “exactly to machine precision” with either “numerically to machine precision” or add the one-line spectral proof.
- l.417: replace “realises the cascade-closure mechanism” with “implements the observer-process architecture associated with the mechanism.”
- l.455-459: replace “Brain waves are the visible telemetry…” with “In this vocabulary, brain-wave signatures are treated as biological telemetry…”
- l.562-563: replace “citing this one as the mechanism prerequisite” with “to be cited by this one only as out-of-scope context” unless those papers are updated.

**Surface Issues**
- Claim ledger l.505-507 omits `thm:flow-exists`, `thm:refinement-compat`, and `thm:flow-intertwining`.
- Claim ledger l.511-513 says “spectral substrate” but cites no spectrum label.
- `Appendix A/E/F` are unnumbered `\subsection*` headings; references are textual, not hyperlinkable subsection refs.
- Tier 2 ARIA evidence is not commit-pinned; l.640-643 admits this. Fix before publication.
- Slash style is inconsistent: “brain / EEG”, “drug / sleep”, “goal / context.” Pick one style.
- No obvious undefined macro in the source scan.

**Top Three Fixes**
1. Fix Proposition 3.1’s support chain, l.253-305. State that convergence is assumed, strengthen Hypothesis 3.1 to flow-intertwining or prove operator-intertwining implies it, and update the ledger.
2. Repair the imported-carrier claims, l.339-355 and l.511-513. Replace the false `E_8` action language and cite the actual shell/spectrum labels.
3. Clean the scope boundary, l.87, l.430-439, l.529, l.558-567. The v2 scope cut is mostly defensible, but the brain/EEG out-of-scope row contradicts the ARIA witness, and the mass-spectrum “citing this one” phrase is not verified.
