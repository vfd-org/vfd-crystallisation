**1. Claim Audit**

- “Definition [Cascade closure]” (l.279-305): this is stipulative, not proved. The paper correctly says so at l.321-325. No over-claim.

- “Under Hypotheses ... projected states ... satisfy” residual-zero and fixed-point propagation (l.376-386): the proof at l.390-406 establishes exactly this. It uses only non-negativity of \(R_k\), monotonicity, flow intertwining, and the composite-map definition. No existence or generic convergence is proved.

- “Convergence propagation under flow intertwining” (l.409-418): the proof at l.421-430 establishes convergence only from the projected top-rung initial datum. The nearby phrase “convergence from initial data” (l.330-331) is too broad unless changed to “from projected top-rung initial data.”

- “\(\Vsub\) ... \(120\) vertices ... degree \(12\)” (l.475-481): supported, but by different sources. The \(2I\) identification is in `CascadeAlgSubstrate`; degree \(12\) is supported by `AriaClosureKernel` / Appendix E, not by `thm:icosian-closure`.

- “shell sizes ... \((1,12,20,12,30,12,20,12,1)\)” (l.485-491): supported by `CascadeAlgSubstrate` `thm:shell-class` and locally by `verify_kernel.py`.

- “nine distinct eigenvalues ... \(94/120\), \(26/120\)” (l.492-499): supported as an imported \(2I\) character-table computation in `CascadeAlgSubstrate`, with local numerical reproduction. Not proved from first principles here; the text mostly admits that.

- “\(E_8\) minimal shell projects onto \(H_4/\Vsub\)” (l.502-506): verified in `CascadeAlgSubstrate` `thm:pi-H`. The “projection, not action” caveat is correct.

- “\(\|\Cphi^{-1}\|=\pphi^2\) exactly” (l.525-529): established, conditional on \(L_M\) being the connected unweighted graph Laplacian. The spectral-bottom argument is sufficient.

- “correlation uniform across the \(120\) source-vertex sweeps” (l.531-537): supported by existing `results.json`; it is numerical only. The manuscript correctly says it is not a convergence theorem.

- “\(\sigma\)-fixed spectral subspace has average \(2T\)-mass at baseline” (l.551-553, l.797-799): supported by the audit/script. This is correctly treated as an honest negative.

- “weighted variants ... underperform the unweighted variant” (l.555-557, l.812-815): supported by Appendix E / `results.json` values \(0.976\) vs \(0.888/0.884\).

- “ARIA empirical witness ... \(17/18\), \(18/18\), \(6/6\), \(-11.58\sigma\)” (l.607-617, l.719-721, l.819-828): locally present in `papers/aria-chess-paper`. This is imported empirical evidence, not a theorem. The caveat “substrate-witness scope only” is necessary and mostly maintained.

- “\(b\to s\mu^+\mu^-\) ... identifies a sign-uniform structural witness” (l.647-654): supported by the sibling `BANOMALY-001/vfd-b-anomaly` checkout, but not by this repository and not re-executed here. “Identifies” is too strong for an external, unreproduced fit; use “reports.”

- “Tier 2 ... branch-named external evidence ... exact commit hash will be added at publication” (l.861-868, table l.882-902): file names exist in sibling `../aria-chess/v4_locked_2026-04-29`, but there is no `.git` metadata in `../aria-chess`. This is not publication-grade provenance.

**2. Internal Consistency**

- Static scan: all `\ref{...}` targets in the TeX are defined. There are no `\eqref` uses. No missing bibliography keys found.

- Round 12’s ARIA downgrade is not complete. The section title and most text say “architecture-level mapping,” but l.562-564 still says “admits an implementation-level mapping into a concrete computational system.” That directly conflicts with l.566-572 and l.592-594.

- l.463 says “The Vibrational Field Dynamics implementation of cascade closure uses...” This is less severe than the ARIA line, but still stronger than the paper’s actual construction. It only defines the carrier/operator part.

- l.330-331 says convergence “from initial data” is added by the corollary. The corollary proves convergence from a specific top-rung datum projected downward, not arbitrary compatible initial towers.

**3. External Consistency**

- `CascadeClosureDynamics`: verified. The cited labels exist. `thm:flow-intertwining` is indeed mass-only; the manuscript correctly retains general flow intertwining as a hypothesis.

- `CascadeRefinementSpaces`: verified. `thm:bonding` and `thm:commute` exist. The manuscript correctly says `thm:commute` is not a generic bonding-map identity.

- `CascadeAlgSubstrate`: verified for `thm:pi-H`, `thm:icosian-closure`, and `thm:shell-class`. The spectrum is recorded there as an imported character-table fact, not an internally proved theorem.

- `AriaClosureKernel`: verified for degree \(12\), shell sizes, \(\|\Cphi^{-1}\|=\pphi^2\), per-vertex correlation \(0.976\), multi-source uniformity, and weighted-variant underperformance.

- `SmartARIAChess`: verified locally for the quoted empirical numbers and methodology-refinement caveats.

- `ariaChessRepo`: not commit-pinned. Sibling branch directory exists and contains the named Tier 2 files, but the evidence is branch/directory-level only.

- `SmartBAnomaly`: not in this repository. A sibling git checkout exists and supports the AIC/sign-uniformity summary, but the present paper’s bibliography gives no commit-pinned source.

- `SmartV`, `SmartVRev`: local files exist; the present paper cites them only as out-of-scope context. No problem.

**4. Tightness**

- l.562-564: replace “admits an implementation-level mapping into a concrete computational system” with “is compared with a concrete computational system at the architecture-description level.”

- l.463: replace “The Vibrational Field Dynamics implementation” with “The Vibrational Field Dynamics construction.”

- l.536-539: replace “all subsequent witnesses” with “the witnesses discussed here.”

- l.647-649: replace “identifies a sign-uniform structural witness” with “reports a sign-uniform structural witness.”

- l.330-331: replace “convergence from initial data” with “convergence from projected top-rung initial data.”

**5. Surface Issues**

- l.810-811: “per-vertex per-vertex correlation” is duplicated.

- l.475: “with \(|2I|=120\) vertices” is awkward. Write “with \(|\Vsub|=|2I|=120\) vertices.”

- l.562-564: residual “implementation-level” wording is both a surface issue and a claim-strength issue.

- I found no undefined macros or missing citation keys by static scan. I did not compile or re-run scripts; the workspace is read-only and `verify_kernel.py` writes `results.json`.

**6. Top Three Fixes**

1. Pin `ariaChessRepo` to an exact commit or remove/demote the Tier 2 module table: l.861-868 and l.882-902 are not publication-grade evidence.

2. Finish the ARIA downgrade: l.562-564 still says “implementation-level mapping,” contradicting the paper’s own architecture-level caveats.

3. Make external empirical provenance auditable: the b-anomaly claim at l.647-666 and ledger row l.722-724 need a commit/URL/report identifier, or the wording should be demoted to “externally reported, not locally audited.”

Publication ready: **NO**. The formal proposition and corollary are basically sound. What blocks publication is the unpinned ARIA Tier 2 evidence, the remaining implementation-level ARIA overclaim, and external empirical witnesses that are still not publication-grade auditable from the manuscript.
