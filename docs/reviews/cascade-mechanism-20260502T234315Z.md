All line numbers refer to `papers/cascade-mechanism/cascade-mechanism.tex`.

**1. Claim Audit**

- L370-L380, “Conditional closure-residual compositionality.” The proof establishes the two stated conclusions, assuming Hypotheses 3.4 and 3.5. It does not establish event occurrence, top-rung existence, basin attraction, or lower-rung convergence from arbitrary initial towers. The surrounding caveats mostly state this correctly.

- L401-L410, “Convergence propagation under flow intertwining.” Established, but the proof elides the induction from adjacent intertwining to the composite identity for `\pi^\sharp_{N,k}`. Add one sentence.

- L339-L362, “Flow intertwining.” Correctly stated as a hypothesis. The differentiation at L352-L355 is legitimate under the standing `C^1` flow/map assumptions, but only as a consequence of the hypothesis, not as new evidence.

- L462-L496, 600-cell carrier facts. Vertex count, degree, shell sizes, icosian closure, and spectrum are supported by local sources. Caveat: L469-L472 overstates “Euclidean / conjugacy shell decomposition from any vertex.” P2 proves shell = conjugacy class from the identity; shells from another vertex are left translates with the same sizes, not literally conjugacy classes.

- L500-L511, `\|\Cphi^{-1}\| = \varphi^2`. Established, assuming the spectral/operator norm on `\ell^2(V_600)` and connected unweighted graph Laplacian. This is correctly stated.

- L512-L518, per-source correlation uniformity. Supported by checked-in `results.json` (`max_minus_min = 1.998e-15`). Correctly caveated as diagnostic, not convergence theorem.

- L531-L538, honest-negatives. Supported: I reran `test_sigma_attractor_spectrum.py`; it gives `94/120`, `26/120`, and no 2T localisation above baseline. Weighted-kernel underperformance is supported by `results.json`.

- L587-L598, ARIA empirical anchor. Imported only. The claims are present in `papers/aria-chess-paper/paper/main.tex`, but this paper does not prove them. The wording is acceptable only because the section repeatedly says substrate-witness, not consciousness derivation.

- L624-L645, b-anomaly witness. Correctly marked external to this repository. I found the sibling checkout and the AIC/sign-uniformity claims are present there, but they remain non-local evidence for this paper.

**2. Internal Consistency**

- L341 uses `(\pi_{k+1,k})_k` after the Round 9 rewrite removed carrier-level `\pi`. This should be `(\pi^\sharp_{k+1,k})_k`.

- L246-L248 and L252 say the bonding maps satisfy “strict commutation identities” / “strict bonding identities” from `CascadeRefinementSpaces thm:commute`. That source theorem is Coxeter/sigma intertwining for `p^0,p^1`, not a generic bonding-identity theorem. This is still a live import mismatch.

- L219-L227 and L674-L676 under-qualify “refinement compatibility.” In `CascadeClosureDynamics`, exact compatibility for `L_n` and the flow is mass-only; full `(alpha,beta,gamma)` refinement-intertwining is explicitly not established.

- L197 and L274 still use “admissible state spaces,” while admissibility is defined two-tier only for bonding maps at L249-L256. Either define state-space admissibility or remove the adjective.

- Static check: all `\ref` targets and bibliography keys used in this file resolve. I could not run `pdflatex` because the environment filesystem is read-only, including `/tmp`.

**3. External Consistency**

- `CascadeClosureDynamics`: verified locally. Gradient operator, flow existence, energy dissipation, coercive contraction under coercive invariant subspace, and mass-only flow intertwining exist. The current paper must not imply full residual-flow refinement compatibility is imported.

- `CascadeRefinementSpaces`: verified locally for finite-level state spaces and downward bonding maps. It does not supply arbitrary `\Phi_{k+1}\to\Phi_k` analytic maps; those remain analogues/hypotheses here.

- `CascadeAlgSubstrate`: verified locally. `thm:pi-H`, `thm:icosian-closure`, `thm:shell-class`, spectrum fact, and `94/26` split exist. The spectrum is an imported character-table computation in that source, not a fresh theorem there; the present label mostly respects this.

- `AriaClosureKernel`: verified locally from its paper and `results.json`: `C_\varphi`, Green kernel, norm, correlations, and weighted-variant negative are present.

- `SmartARIAChess`: verified as locally present. I did not rerun its empirical harness. Tier-2 `aria-chess` files exist in a sibling snapshot, but that directory is not a git repository, so the branch/commit claim is not locally auditable.

- `SmartBAnomaly`: not in this repo; sibling checkout supports the cited numbers. The paper correctly says the primary fit is external.

**4. Tightness**

- L54-L55, L145, L175, L334, L527, L752: “attractor” is stronger than the formal math, which gives fixed points / trajectory limits, not stability basins. Edit: “closure-compatible fixed point” or “limit state.”

- L469-L472: edit to “The Euclidean shell decomposition from any source has these sizes; at the identity these shells coincide with conjugacy classes.”

- L674-L676: edit to “mass-block compatibility and mass-only flow intertwining,” not broad “refinement compatibility.”

- L589-L598: stronger than necessary. Edit: “the source reports `17/18` under standard validation and `18/18` after documented methodology refinement.”

**5. Surface Issues**

- L790: duplicated phrase, “per-vertex per-vertex correlation.”

- L512: “all choice of source vertex” should be “all choices of source vertex.”

- L341: missing `\sharp` is both notation and surface issue.

- No non-ASCII em dash found in the main `.tex`.

- No undefined citation keys or missing local labels found by static inspection.

**6. Top Three Fixes**

1. Fix the refinement/bonding import language at L246-L252 and L674-L676. The current wording still suggests more from `thm:commute` and P4 refinement compatibility than the sources prove.

2. Correct the shell/conjugacy statement at L469-L472. “From any vertex” is true for Euclidean shell sizes, not for literal conjugacy-class shells.

3. Replace “attractor” language with “fixed point” / “limit state” unless an actual attraction or basin theorem is added.

Publication ready: **No**.
