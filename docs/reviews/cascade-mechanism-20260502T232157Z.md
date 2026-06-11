**1. Claim Audit**

- “prove a conditional residual-compositionality proposition” (L61-L62; Proposition L352-L361): established. The proof at L364-L381 proves exactly residual-zero and fixed-point propagation downward from an already-given top fixed point, assuming Hypotheses 3.1 and 3.2. It proves no existence or convergence theorem; L383-L408 correctly says this.
- “finite-dimensional closure-flow infrastructure … is established” (L217-L229): verified only for the cited source’s quadratic \(F_n\), with mass-only flow intertwining. The caveat at L226-L229 is necessary and mostly sufficient.
- Flow intertwining hypothesis (L321-L345): not a claim; retained as a hypothesis. The differentiation-to-vector-field-compatibility sentence is now mathematically acceptable under the stated \(C^1\)/flow assumptions.
- \(\Vsub\) numerical structure: 120 vertices, degree 12, shell sequence, nine eigenvalues, \(94/26\) split (L425-L459): supported by `CascadeAlgSubstrate` and local scripts. The spectrum remains imported character-table/computational material, not proved anew here.
- \(\|\Cphi^{-1}\|=\varphi^2\) exactly (L469-L472, L737): established analytically from connectedness of the graph Laplacian and the \(\varphi^{-2}\) shift. This is stronger than merely “locally re-runnable.”
- Per-vertex correlation uniformity (L473-L477, L738-L739): supported as a numerical diagnostic. It does not prove any discrete-to-continuum convergence theorem.
- “\(\sigma\)-fixed eigenvectors do not preferentially localise on \(2T\)” (L490-L493, L724-L727): numerically supported in the averaged diagnostic, but the word “eigenvectors” is not basis-invariant in degenerate eigenspaces. State this as a claim about the \(\sigma\)-fixed spectral subspace or averaged eigenspace mass.
- ARIA empirical witness numbers (L543-L554, L746-L755): verified against the local ARIA paper. They establish only the imported substrate-witness profile, not closure-compatibility in Definition 3.1.
- \(b\to s\mu^+\mu^-\) witness (L581-L596): supported by the sibling `BANOMALY-001/vfd-b-anomaly` checkout, not by a paper inside this repository. The AIC caveat is correctly carried.
- Runtime module map (L775-L792, L806-L826): Tier 1 files exist in this repo. Tier 2 claims depend on upstream `ariaChessRepo`; branch identity and commit identity are not verifiable from this repository.

**2. Internal Consistency**

- The Round 7 appendix-reference fix worked: uses such as L443, L459, L469, L545, L594 now target `Appendix~\ref{app:field-signature-audit}, entry X`, so the rendered text and hyperlink target are coherent.
- No unresolved `\ref`/citation warnings appear in the build log scan. No `\eqref` use is present.
- Serious remaining mismatch: L242-L243 says geometric projection maps are “refinement-compatible in the sense of” `CascadeClosureDynamics` `def:refinement-compat`. That source definition is for bounded operator families \(T_n\) satisfying \(pT_{n+1}=T_np\), not for geometric maps \(G_{k+1}\to G_k\). Define “admissible projection” here or cite the P3 bonding maps instead.
- The observer-process section is now internally caveated: L506-L511 and L533-L536 avoid claiming ARIA satisfies Definition 3.1. That is consistent.

**3. External Consistency**

- `CascadeClosureDynamics`: verified. It proves the named \(F_n\) gradient/operator/flow facts and mass-only flow intertwining; it does not prove arbitrary \(R_k\) residual-flow intertwining.
- `CascadeRefinementSpaces`: verified for finite-level state spaces, downward bonding maps, and commutation identities.
- `CascadeAlgSubstrate`: verified for \(E_8\to H_4\) projection, \(V_{600}\cong2I\), shell-class structure, and \(94/26\) split; the Laplacian spectrum is explicitly imported there.
- `AriaClosureKernel`: verified for \(G(x)=(\varphi/2)e^{-|x|/\varphi}\), the operator norm, correlation values, and weighted-variant negative result.
- `SmartARIAChess`: verified for \(18/18\), six EEG signatures, and the HCP \(-11.58\sigma\)/\(+6.80\sigma\) caveats.
- `SmartBAnomaly`: not in this repository. A sibling checkout supports the stated AIC/sign-uniformity claims, but repo-local verification fails by definition.
- `SmartV`, `SmartVRev`: local files exist; current paper uses them only as out-of-scope context.

**4. Tightness**

- L166-L167: “ours is proposed as a further substrate-geometry parametrisation, parametrised by substrate geometry.” Edit to: “ours is proposed as a further substrate-geometry parametrisation.”
- L364: “Proof sketch” undersells a complete proof. Edit to: “Proof.”
- L490-L493 and L724-L727: edit to “the \(\sigma\)-fixed spectral subspace has average \(2T\)-mass at baseline,” not “eigenvectors do not localise.”
- L640-L642: edit label/reason to “Analytic identity, locally reproduced,” not just “Locally re-runnable.”
- L775-L792: “audited” is too strong for Tier 2 without a commit hash. Edit to: “mapped against the named upstream branch; commit-pinned audit deferred to publication.”

**5. Surface Issues**

- L166-L167 has a duplicated “parametrisation/parametrised” construction.
- Build log still reports overfull boxes in the claim ledger and runtime table, especially around L609-L665 and L821-L822.
- No undefined macros, missing labels, or broken citations found in the current build log.
- The bibliography portability issue from Round 7 appears fixed; no document-local `\ref` remains in the `ariaChessRepo` bib note.

**6. Top Three Fixes**

1. Fix L242-L243. The cited `def:refinement-compat` is not the right type of object for geometric projection maps.
2. Recast the \(2T\)-localisation negative at L490-L493 and L724-L727 in basis-invariant eigenspace language.
3. Separate repository-local evidence from external/sibling evidence for `SmartBAnomaly` and `ariaChessRepo` at L581-L596 and L775-L792.

Publication ready: **No**.
