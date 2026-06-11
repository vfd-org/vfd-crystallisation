**1. Claim Audit**

- “Cascade closure” is defined as an event with convergence, residual zero, flow invariance, and terminal projection compatibility (l.279-305). This is stipulative, not proved. The text correctly says so at l.320-332. No over-claim.

- Imported P4 closure-flow infrastructure (l.219-238): verified locally in `papers/cascade-closure-dynamics/cascade-closure-dynamics.tex`. The cited labels exist and the scope restriction is accurate: full flow-intertwining is mass-only, not generic. Round 11’s import precision is substantially fixed.

- Proposition 3.6: “Under Hypotheses ... top-rung state ... Then the projected states ... satisfy residual zero and fixed-point” (l.376-386). The proof establishes exactly this. It does not establish existence, convergence, or occurrence of a Definition 3.1 event; the paper correctly states that at l.433-458.

- Corollary 3.7: “if ... rung-N flow converges ... and each projection is continuous, then rung-k flow converges from the projected initial datum” (l.409-418). The proof establishes this by composing flow-intertwining and passing limits. Continuity is already implied by the standing adjacent \(C^1\) assumptions for finite composites, but the redundancy is harmless.

- Carrier claims: \(|2I|=120\), shell sizes, shell/class relation, and \(94/26\) spectral split (l.475-496) are locally supported. The icosian and shell claims are in `CascadeAlgSubstrate`; the spectrum is imported there from the standard \(2I\) character table and locally reproduced. The statement “uniform vertex degree 12” is true in the local ARIA closure-kernel source, but it is not established by the specific `thm:icosian-closure` citation at l.478. Add a direct citation to Appendix E or `AriaClosureKernel`.

- \(\|\Cphi^{-1}\|=\varphi^2\) exactly (l.516-526, l.710-712) is established, conditional on \(L_M\) being the connected unweighted graph Laplacian. The proof is the elementary spectral-bottom argument. This is sound.

- Per-source correlation uniformity “max minus min on the order of \(10^{-15}\)” (l.528-534) is a numerical diagnostic only. The paper says that explicitly. Verified in committed `results.json`.

- ARIA empirical witness: \(17/18\), \(18/18\), \(6/6\), and HCP \(-11.58\sigma\) / \(+6.80\sigma\) claims (l.603-616, l.716-718, l.816-826) are present in the local ARIA paper. The paper’s caveat “substrate-witness scope only” is necessary and mostly observed.

- \(b\)-anomaly witness (l.642-669, l.719-721): the paper correctly says the primary fit is external to this repository and not re-executed here. The AIC-inconclusive framing is supported by the sibling checkout, but it is not repository-local evidence.

**2. Internal Consistency**

- All `\ref{...}` references in the TeX resolve to labels present in the file. There are no `\eqref` uses. I found no undefined macros in the target file.

- The Round 11 ARIA softening is incomplete. The abstract says “architecture-level mapping” (l.65), but the reader map and section title still say “computational implementation” (l.107, l.557). Appendix B then says the tuple “is realised by ARIA” (l.847) and the production architecture is “realised across” modules (l.854). That conflicts with the paper’s own caveat at l.83-86 and l.587-591.

- Claim ledger row for P3 still says “Imported (Theorem)” while the row includes state spaces and refinement infrastructure (l.695-697). This should match the P4 precision style: “Imported finite-level definitions / results.”

- Appendix E/F text is now internally consistent in the TeX (l.803-826). However, the referenced full audit file `FIELD_SIGNATURE_AUDIT.md` still contains stronger/staler language: “2.618034 = φ²,” “weighted variants LOSE,” and “18/18” without the 17/18 standard-validation caveat. Since the TeX points readers to that full audit at l.780-782, this is still a consistency problem.

**3. External Consistency**

- `CascadeClosureDynamics`: verified. The cited gradient operator, energy dissipation, coercive contraction, mass-block compatibility, flow existence, and mass-only flow-intertwining labels exist and support the restricted import.

- `CascadeRefinementSpaces`: verified. `thm:bonding` and `thm:commute` exist. The target text correctly notes that `thm:commute` is for specific \(p^0,p^1\) maps, not generic bonding maps.

- `CascadeAlgSubstrate`: verified for \(E_8\to H_4\) projection, icosian closure, shell-class theorem, and the spectrum/94-26 split. The degree-12 graph fact is better supported by `AriaClosureKernel` than by the cited P2 theorem at l.478.

- `AriaClosureKernel`: verified for \(G(x)=(\varphi/2)e^{-|x|/\varphi}\), \(\|\Cphi^{-1}\|=\varphi^2\), per-vertex correlation \(0.976\), weighted variants \(0.888/0.884\), and multi-source uniformity.

- `SmartARIAChess`: verified for the ARIA empirical numbers and the methodology-refinement caveats.

- `ariaChessRepo`: Tier 1 files exist locally in the release bundle. Tier 2 filenames exist in sibling `../aria-chess/v4_locked_2026-04-29`, but that directory has no `.git`, and the paper gives no commit hash. The branch/commit claim is not locally auditable.

- `SmartBAnomaly`: not part of this repository. A sibling git checkout exists and supports the AIC/sign-uniformity summary, but this remains external evidence, as the paper admits.

**4. Tightness**

- l.107 / l.557: Replace “ARIA as a computational implementation” with “ARIA as an architecture-level observer-process mapping.”

- l.563-565: Replace “one architecture-level realisation/mapping” with “one architecture-level mapping.”

- l.470: Replace “construction is realised” with “carrier/operator part of the construction is defined.”

- l.745-746: Replace “observer-process implementation” with “observer-process mapping.”

- l.847-855: Replace “is realised by ARIA” / “architecture realised across” with “is mapped to ARIA source tiers” / “architecture is represented at the module-description level.”

**5. Surface Issues**

- l.807-808: “per-vertex per-vertex correlation” duplicate.

- l.107 and l.557 preserve the old “computational implementation” language despite the abstract fix.

- l.695-697: P3 ledger label should not be “Imported (Theorem)” for a definitions-plus-results row.

- l.859-863 and `references.bib` l.162-168: branch pin without commit hash is explicitly admitted, but not publication-grade provenance.

- No broken labels or undefined target-file macros found by inspection.

**6. Top Three Fixes**

1. Downgrade all remaining ARIA “implementation/realised” language: l.107, l.557, l.563-565, l.745-746, l.847-855. This is the main surviving over-claim.

2. Make Tier 2 ARIA provenance publication-grade: l.859-863 and table l.877-897 need an exact URL/commit hash, or the Tier 2 module claims must be demoted further.

3. Align the audit/citation precision: fix P3 ledger wording at l.695-697, cite degree 12 properly at l.475-480, and update `FIELD_SIGNATURE_AUDIT.md` because the TeX points readers to it at l.780-782.

Publication ready: **No**. The central formal proposition is now sound, but the paper still has publication-blocking provenance and claim-tightness problems.
