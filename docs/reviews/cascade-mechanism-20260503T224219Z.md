**1. Claim Audit**
- “prove a conditional residual-compositionality proposition” (l.61-62); Proposition: “Under Hypotheses… projected states… satisfy” zero residual and fixed-point propagation (l.391-402). The proof establishes exactly this. It does not establish existence of the top fixed point, convergence from arbitrary initial data, or occurrence of a cascade-closure event. The manuscript mostly admits this at l.451-459.
- Corollary: “Convergence propagation under flow intertwining” (l.424-436). The proof establishes convergence only from a projected top-rung initial datum, using continuity of the composite projection. It proves no residual-zero, fixed-point, or terminal-tower compatibility unless combined with further hypotheses.
- “A cascade-closure event… occurs… when…” (l.293-319). This is a definition, not a demonstrated event. No nontrivial example in the manuscript is shown to satisfy all clauses.
- “\(|\Vsub|=|2I|=120\)” and degree \(12\) (l.493-499). Supported by imported/local substrate sources. Fine, but “canonical bijection” is slightly stronger than necessary; the cited source supports the standard icosian identification.
- Shell sequence and conjugacy-shell statement (l.505-509). Supported at the identity by `CascadeAlgSubstrate`; extension to other source vertices follows by left translation, but that inference is not spelled out here.
- Laplacian spectrum and \(94/26\) split (l.510-517). Supported as an imported character-table/numerical fact, not proved in this manuscript. The wording correctly says it is imported/rechecked.
- “\(\|\Cphi^{-1}\|=\pphi^2\) exactly” (l.543-548). Established, assuming the standard connected unweighted graph Laplacian and spectral operator norm. This is one of the clean claims.
- Per-vertex correlation uniform to \(10^{-15}\) (l.549-555). Supported numerically by `results.json`; correctly labelled a diagnostic, not a convergence theorem.
- ARIA empirical witness profile: \(17/18\), \(18/18\), six signatures, \(-11.58\sigma\), \(+6.80\sigma\) (l.630-639). Verifiable in `papers/aria-chess-paper/paper/main.tex`; still imported, not rerun here. The source itself carries single-seed and node-count caveats.
- \(b\)-anomaly witness and AIC weights (l.671-692). Verifiable only in the sibling `BANOMALY-001/vfd-b-anomaly` checkout, not in this repo. The claim is appropriately framed as unaudited here.
- Appendix A/E/F numerical claims (l.823-862). A and E are locally supported; I reran the sigma-attractor script and it reproduces \(94/120\), \(26/120\), and baseline \(2T\)-mass. E matches the existing `results.json`. F is imported only.

**2. Internal Consistency**
- Serious contradiction: l.671-692 says the \(b\)-anomaly repository is commit-pinned, and `references.bib` also pins commit `6bdfc8f8...`; l.753 says “primary fit not commit-pinned in the bibliography.” That is false.
- The paper repeatedly says ARIA is only an architecture-level mapping (l.83-87, l.585-591), but the quotation at l.660-664 says ARIA metrics are “synthetic telemetry of an observer cascade.” That outruns the stated boundary.
- \(G_k\) is a geometric carrier (l.193), while \(G\) is also the goal/context component of \(\Ocal\) (l.598-604). Not fatal, but avoidable notation overload.
- \(C\), \(C_\varphi\), and source-paper \(C_n\) are used for different closure/mass/response objects. The manuscript usually disambiguates, but the reader has to work.
- Cross-references resolve. The log shows no undefined refs/cites. No `\eqref` issue found.

**3. External Consistency**
- `CascadeClosureDynamics`: verified. The cited labels exist and the manuscript accurately states the mass-only restriction for flow intertwining. The source’s own global \(\alpha,\beta,\gamma>0\) convention versus its \(\alpha=\beta=0\) subcase remains awkward, but this manuscript acknowledges the restriction.
- `CascadeRefinementSpaces`: verified for bonding maps and restricted Coxeter/\(\sigma\) identities. The current paper correctly refuses to import generic bonding identities.
- `CascadeAlgSubstrate`: verified for \(E_8\to H_4\) projection, icosian closure, shell-class theorem, and the \(94+26\) split. Caveat: the spectrum is explicitly imported there from the standard \(2I\) character table, not proved from first principles.
- `AriaClosureKernel`: verified for \(C_\varphi\), \(G(x)=(\varphi/2)e^{-|x|/\varphi}\), spectrum, norm, shell sizes, and correlation numbers.
- `SmartARIAChess`: verified for the quoted empirical tallies, but only as an imported preprint result.
- `ariaChessRepo`: not in this repository. The sibling frozen snapshot exists and the Tier-2 filenames listed in the runtime table exist there, but this is not repository-local evidence.
- `SmartBAnomaly`: not in this repository. The sibling checkout exists at the pinned commit and supports the AIC/sign-uniformity claims. The current repo alone cannot verify it.
- `SmartV`, `SmartVRev`: local files exist; the present manuscript uses them only as out-of-scope context, so there is no substantive claim here to audit.

**4. Tightness**
- l.52-57: replace “structural generalisation” with “proposed structural analogue/generalisation.” The paper does not derive OR as a special case.
- l.493-496: replace “canonical bijection” with “standard icosian identification used in the cited source.”
- l.617-618: replace “models the gradient flow” with “is used here as an architecture-level analogue of the gradient-flow role.”
- l.660-664: replace the whole sentence with: “Both are treated only as candidate process-level telemetry under this vocabulary.”
- l.667: rename section to “One externally reported substrate witness.” “Physical witness” is too strong for an unaudited, AIC-inconclusive fit.
- l.895-897: clarify that Tier 1 supports the kernel/demo slice, not the full `SmartARIAChess` validation suite.

**5. Surface Issues**
- No undefined macros, labels, or citations found in the existing LaTeX log.
- Overfull boxes occur around the claim ledger / longtable and the ARIA runtime paragraph; tighten table columns or shorten `\texttt{...}` entries.
- l.753 is not a typo; it is a factual contradiction and must be fixed.
- The title/abstract say “mechanism paper,” but the mathematical payload is a definition plus a conditional propagation lemma. That is acceptable only if the title/closing language stays modest.

**6. Top Three Fixes**
1. Add a nontrivial worked instance verifying Hypotheses l.360-389 and Definition l.293-319, or explicitly downgrade the paper to a definition-and-conditional-lemma paper. Right now no cascade-closure event is proved to occur.
2. Fix the \(b\)-anomaly provenance contradiction at l.753. It is commit-pinned, but external to this repo and not re-executed here.
3. Cut back ARIA language at l.660-664 and l.895-897. The paper supports an architecture-level mapping plus imported witness numbers, not an established “observer cascade” realisation.
