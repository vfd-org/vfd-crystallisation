**1. Claim Audit**

- “(O2) partially closed at the boundary-energy / quadratic-form level” and “Strict operator- and flow-level intertwining of (O2) ... is the only substantive open ask remaining” (lines 91-95): false relative to the edited §3.5 and `cascade-refinement-compat` commit `3320373`. The correct statement is: (O2) as stated remains false; only a boundary-energy / Schur substitute is discharged, and the P3/P4 lift is still conditional on open (L1)/(L3).

- “(O1) and (O3) are open in the source state” (lines 117-119): stale. §3.5 and the ledger now say (O3) is closed in the abstract scalar pure-midpoint model, with P3/P4 lift conditional on (L1)/(L3). (O1) reduces to finite-dimensional spectral decomposition, with nontrivial selection out of scope.

- Proposition “Conditional closure-residual compositionality” (lines 475-487): proof establishes exactly the stated residual-zero and fixed-point propagation. It does not overclaim occurrence of a full cascade event; the surrounding remark correctly limits it (lines 538-566).

- Corollary “Convergence propagation under flow intertwining” (lines 508-523): proof establishes the claim, assuming continuity of the composite projection. It correctly does not invoke monotonicity.

- O1 bullet in worked invocation: “What is open ... [is] the existence and selection of a nontrivial top-rung fixed point ... with a positive spectral gap” (lines 656-660): overstates the open part. In the connected graph-Laplian abstract model, constants give a nonzero kernel and the finite-dimensional spectral gap on `ker^\perp` is standard. What remains open/out of scope is selection of a physically meaningful nonzero kernel element, not existence.

- O2 bullet (lines 662-680): established. `CascadeClosureDynamics` proves flow intertwining only in the mass-only case, not for the curvature flow used here.

- O3 bullet (lines 681-688): accurate only as the pre-compat “source state.” The current verdict later supersedes it. As written, the transition is understandable but fragile.

- Current verdict paragraph (lines 691-723): internally and externally correct against `cascade-refinement-compat` commit `3320373`. It correctly says (L1)/(L3) are open, (L2) is `CascadeRefinementSpaces` `prop:adjoints`, (O2) as stated is false, and the Schur substitute is discharged.

- Carrier claims: `|V_600|=120`, degree 12, shell sizes, spectrum, `94/26` split (lines 739-779): not proved here, but attributed and locally consistent with `cascade-algebraic-substrate` and the kernel repro material. The paper correctly avoids uniqueness.

- Operator identity `||C_phi^{-1}|| = phi^2` (lines 783-795): proof is sufficient, assuming connected unweighted graph Laplacian. This is a clean analytic claim.

- ARIA empirical witness claims (lines 876-898, 1133-1155): not proved here; the paper correctly labels them imported and caveated.

**2. Internal Consistency**

- Major conflict: abstract lines 87-95 retain old “partially closed” / “only O2 open” wording, while §3.5 lines 691-723 and ledger line 989 use the final false/substitute wording. This is a direct regression against the requested alignment pass.

- Major conflict: epistemic status lines 117-119 contradict §3.5 and the ledger. They still say (O1)/(O3) open and (O2) closed only for mass-only `L_n`; this no longer mirrors `cascade-refinement-compat`.

- Major conflict: “none of (O1)--(O3) is closed in the source state” (lines 1049-1051) contradicts the final §3.5/ledger scope.

- Cross-references: all `\ref`/`\eqref` targets in `cascade-mechanism.tex` resolve locally. No unresolved target was found.

**3. External Consistency**

- `CascadeRefinementCompat` at commit `3320373`: verified. It states (O3) closed in the abstract scalar pure-midpoint model, (O2) as stated false, boundary-energy / Schur substitute discharged, and P3/P4 lift conditional on open (L1)/(L3); (L2) is already P3. §3.5 lines 691-723 and ledger line 989 match this.

- `CascadeRefinementSpaces` `prop:adjoints`: verified at lines 655-671. It proves `j^1=(p^1)^*` and `p^1 j^1 = 1/2 id`, matching the claimed (L2) input.

- `CascadeClosureDynamics`: verified. It proves gradient operator, flow existence, energy dissipation, coercive contraction, mass-block compatibility, and mass-only flow intertwining. It explicitly does not prove curvature-flow intertwining.

- `CascadeAlgSubstrate`: verified for `thm:pi-H`, `thm:icosian-closure`, `thm:shell-class`, and the recorded/imported spectrum and `94+26` split. The spectrum is recorded as character-table input, not an independent proof in the current paper.

- `AriaClosureKernel`: verified for `C_phi`, degree 12, `||C_phi^{-1}||`, per-vertex correlation, weighted-variant underperformance, and AIC-tie caveats.

- `SmartARIAChess`: verified for the `17/18`, `18/18`, P10 `15` vs `20` permutation caveat, seed-42 six-signature claim, and HCP `-11.58σ/+6.80σ` distinction.

- `SmartBAnomaly`: not locally verifiable in this repository. The paper correctly labels it external and not re-executed.

**4. Tightness**

- Lines 91-95: replace with “(O2) as stated remains false; the boundary-energy / Schur substitute is discharged in the abstract model; P3/P4 lift remains conditional on (L1)/(L3).”

- Lines 117-119: replace with “§3.5 records the updated source-side status: (O3) closed only in the abstract scaled pure-midpoint model, (O2) as stated false, Schur substitute discharged, and P3/P4 lift conditional on (L1)/(L3).”

- Lines 656-660: replace with “The open content of (O1) is not existence of nonzero kernel states, but selection of a specific nontrivial state.”

- Lines 1049-1051: replace with the same final ledger wording as line 989, or delete this sentence.

**5. Surface Issues**

- `references.bib` lines 22-26 still say `CascadeRefinementCompat` discharges (O3) “on the imported P3/P4 finite-level tower” and “partially discharges (O2).” This is stale and externally inconsistent with commit `3320373`.

- Line 989 is too long for maintainable LaTeX and likely overfull; split the ledger row into shorter clauses.

- Line 225 is an overlong paragraph line; surface only.

- No undefined target refs found in `cascade-mechanism.tex`.

**6. Top Three Fixes**

1. Fix the stale alignment text in the abstract and epistemic box: lines 87-95 and 117-119 are the main regressions against the requested final scope.

2. Fix the stale consolidation paragraph at lines 1049-1051. It says none of (O1)--(O3) is closed, contradicting §3.5 and the ledger.

3. Correct O1 wording at lines 656-660: existence of nonzero kernel states and finite-dimensional spectral convergence are not the open problem in the connected graph-Laplacian model; only nontrivial selection is.
