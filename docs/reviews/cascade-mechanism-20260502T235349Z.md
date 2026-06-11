**1. Claim Audit**
- “Proposition [Conditional closure-residual compositionality]” (lines 376-385): proof establishes the two stated conclusions, but the convergence assumption is unused. The proof only needs a top-rung residual-zero fixed point plus Hypotheses 3.4 and 3.5. Either remove “the gradient flow … converges” from the proposition or move it entirely to Corollary 3.7.
- “Corollary [Convergence propagation under flow intertwining]” (lines 407-416): proof establishes the claim. Continuity of the composite maps is stated. Monotonicity is inherited via “hypotheses of Proposition” but is not used.
- “\|\Cphi^{-1}\| = \pphi^2 exactly” (lines 67-68, 519-523, 706-708): established, assuming the connected unweighted graph Laplacian convention. The argument is sufficient.
- “Euclidean shell sizes … conjugacy classes only at identity; left translates elsewhere” (lines 480-485): supported by P2 plus group invariance. This is now correctly qualified.
- “Laplacian spectrum … 94/120 sigma-fixed, 26/120 sigma-paired” (lines 486-493, 783-789): supported by P2 and by running `test_sigma_attractor_spectrum.py`.
- “per-vertex correlation uniform across 120 source-vertex sweeps” (lines 525-531, 803-805): supported by existing `results.json`, max-minus-min about `2e-15`. Not a convergence theorem; the text says this.
- “ARIA empirical witness: 17/18 standard; 18/18 after methodology refinement” (lines 600-611, 712-714, 811-820): locally supported by `papers/aria-chess-paper`, but line 612 overstates with “under preregistered protocols.” The local source has documented methodology refinements and a P10 prereg-exact rerun caveat.
- “b-anomaly closure-kernel witness” (lines 640-659, 715-717): not locally verifiable. The paper admits the primary fit is external; therefore this remains an imported external claim only.
- “ARIA runtime module mapping” (lines 839-858, 872-892): Tier 1 module paths exist locally. Tier 2 module claims are not locally verifiable and are not commit-pinned.

**2. Internal Consistency**
- All scanned `\ref` targets are defined. No unresolved internal labels found.
- Line 197 still says “admissible field states”; admissibility is later defined only for bonding maps. Replace with “field states” or define admissible states.
- Line 480 says the nearest-neighbour graph is used as `L_M`; line 517 correctly defines `L_M` as the graph Laplacian. Fix line 480 to “the Laplacian of this nearest-neighbour graph.”
- Lines 221-228 and 688-690 cite `def:refinement-compat` for mass-block compatibility. The actual P4 proof is `prop:adjoint-refinement`; the definition alone does not establish the mass-block result.
- Line 812: “$18/18$ … hold at $17/18$” is internally contradictory.

**3. External Consistency**
- `CascadeClosureDynamics`: labels exist. Flow intertwining is explicitly mass-only in P4; manuscript now mostly gets this right. Mass-block compatibility should cite P4 `prop:adjoint-refinement`, not only `def:refinement-compat`.
- `CascadeRefinementSpaces`: `thm:bonding` and `thm:commute` exist. The manuscript correctly avoids generalising `thm:commute`.
- `CascadeAlgSubstrate`: `thm:pi-H`, `thm:icosian-closure`, and `thm:shell-class` exist. The spectrum is recorded there as an imported character-table computation, not first-principles P2 theorem; the manuscript states this acceptably.
- `AriaClosureKernel`: norm, correlation, variant-ranking, and caveats are locally supported.
- `SmartARIAChess`: main numbers are locally supported, but the manuscript must preserve the methodology-refinement caveats.
- `SmartBAnomaly`: primary repository is not present locally. Cannot verify.
- `SmartV`, `SmartVRev`: local mass-spectrum papers exist; the present manuscript cites them only as out-of-scope context. Acceptable.
- `ariaChessRepo`: not locally commit-pinned. Tier 2 module claims remain branch-level external witnesses.

**4. Tightness**
- Line 65: change “computational implementation” to “architecture-level mapping to a computational system.”
- Line 612: change “under preregistered protocols” to “under preregistered thresholds with documented methodology refinements.”
- Line 711: change “ARIA realises the architecture” to “ARIA is mapped to the architecture.”
- Lines 805-807: change “weighted variants lose” to “the two tested weighted variants underperform.”
- Lines 688-690: change “Imported (Theorem)” to “Imported finite-level results/definitions.”

**5. Surface Issues**
- Line 197: undefined “admissible field states.”
- Line 480: graph/Laplacian wording error.
- Line 803: `2.618034 = \pphi^2` should be `\approx`; the decimal is truncated.
- Line 804: duplicate “per-vertex per-vertex.”
- Line 812: contradictory `18/18` / `17/18` wording.
- No undefined macros or missing bibliography keys found by static scan. I did not compile because the workspace is read-only.

**6. Top Three Fixes**
1. Fix the P4 import precision at lines 221-228 and 688-690: cite `prop:adjoint-refinement` for mass-block compatibility and stop labelling the whole row as theorem-only.
2. Fix ARIA empirical wording at lines 600-612, 712-714, and 811-820 so it says exactly: `17/18` standard validation, `18/18` after documented methodology refinement, thresholds unchanged, with remaining prereg caveats preserved.
3. Pin or demote Tier 2 runtime evidence at lines 851-858 and 872-892. Without an exact `ariaChessRepo` commit, those module-level claims are not publication-grade evidence.

Publication ready: **No**. The formal proposition/corollary are basically sound, but the external-evidence ledger and ARIA empirical wording still need tightening before publication.
