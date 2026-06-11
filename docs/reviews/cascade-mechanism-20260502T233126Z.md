**1. Claim Audit**

- `cascade-mechanism.tex:361`: “Conditional closure-residual compositionality.” The proof establishes the stated two conclusions: residual-zero propagation and fixed-point propagation. It does not establish existence, convergence, lower-rung flow convergence from projected initial data, or occurrence of a cascade event. The paper mostly says this correctly. However the convergence assumption on the top flow is unused; the proposition only needs a top fixed point with zero residual. Either weaken the hypothesis or add the stronger convergence conclusion for projected initial data.

- `cascade-mechanism.tex:330`: “Flow intertwining.” This is a hypothesis, not proved. The differentiation at `343–346` is valid only under the standing `C^1`/flow regularity assumptions, but those assumptions are separated from the definition of “admissible” projections. Tighten this.

- `cascade-mechanism.tex:356`: “Monotonicity.” Pure hypothesis. No proof attempted; no issue.

- `cascade-mechanism.tex:434–451`: 600-cell carrier facts. The vertex count, degree, shell-size sequence, and spectrum are supported, but not all at the same evidential level. `CascadeAlgSubstrate` proves/imports the algebraic/shell-class facts; the spectrum is explicitly an imported character-table computation in that source, not an internally proved theorem. The paper’s wording is acceptable only because it says “imported” at `464–466`.

- `cascade-mechanism.tex:478–481`: “\(\|\Cphi^{-1}\|=\varphi^2\).” Established, assuming the norm is the spectral/operator norm on \(\ell^2(V_{600})\). State that norm explicitly.

- `cascade-mechanism.tex:482–486`: “per-vertex correlation ... uniform across all 120 vertices.” Supported by checked-in `results.json` (`max_minus_min ≈ 2e-15`), but the sentence is ambiguous. It should say this is a sweep over all choices of source vertex, not “correlation across vertices” in one run.

- `cascade-mechanism.tex:499–506` and Appendix A `738–740`: the 2T-localisation negative is supported. I reran `test_sigma_attractor_spectrum.py`; it reports `94/120`, `26/120`, and 2T mass `0.200` vs baseline `0.200`.

- `cascade-mechanism.tex:553–564`: ARIA empirical witness claims are imported, not proved here. They are present in `papers/aria-chess-paper/paper/main.tex` and sections, but this paper should not call them more than imported substrate-witness facts.

- `cascade-mechanism.tex:589–610`: b-anomaly witness is correctly marked external to this repo. I found the sibling checkout and the cited AIC/sign-uniform claims are present there, but they are not repository-local evidence for this paper.

**2. Internal Consistency**

- Major issue: `cascade-mechanism.tex:237–260` defines geometric maps \(\pi_{k+1,k}:G_{k+1}\to G_k\) and induced pushforwards. But `CascadeRefinementSpaces` mainly provides state-space bonding maps \(p_{n+1,n}\), with vertex restriction from nested vertex sets and an edge-parent map. It does not provide a literal general carrier map \(G_{k+1}\to G_k\) in the form used here. Define the bonding maps directly on \(\Phi_k\), or add the missing carrier-level construction.

- `cascade-mechanism.tex:242–247` says admissible pushforwards are continuous; `201–212` later require them to be \(C^1\). Make “admissible” include the analytic regularity needed for Hypothesis 3.1, or split “geometric admissibility” from “analytic admissibility.”

- Cross-references and citation keys resolve by text comparison. I found no missing `\ref`, `\eqref`, or bibliography key.

- `cascade-mechanism.tex:648–650` says Appendix E gives exact shell sizes. Appendix E points to `verify_kernel.py`, which is floating-point/tolerance based. Exactness is supported by `CascadeAlgSubstrate`, not by that script alone.

**3. External Consistency**

- `CascadeClosureDynamics` claims at `217–225`, `338–351`, `639–641`: verified locally. It proves the gradient operator, flow existence, energy dissipation, and mass-only flow intertwining. But coercive contraction is conditional on a coercive invariant subspace; call it “conditional coercive contraction.”

- `CascadeRefinementSpaces` at `231–244`, `642–644`: verified for finite-level Hilbert spaces and downward bonding maps. It does not justify the paper’s literal geometric \(\pi:G_{k+1}\to G_k\) notation without further definition.

- `CascadeAlgSubstrate` at `437`, `455–466`, `645–647`: verified. `thm:pi-H`, `thm:shell-class`, and `thm:icosian-closure` exist. The Laplacian spectrum is recorded there as an imported character-table fact, not a fresh theorem.

- `AriaClosureKernel` at `484`, `794`: verified locally from its paper and `repro/results.json`: norm, shell sizes, per-vertex correlations, and weighted-variant negative are present. I did not rerun `verify_kernel.py` because it writes `results.json`.

- `SmartARIAChess` at `554–564`, `660–662`: verified as present in the local paper. I did not rerun its empirical harness. Tier 1 files in Appendix B exist in this repo. Tier 2 files exist only in sibling `../aria-chess/v4_locked_2026-04-29`; there is no `.git` metadata there, so the branch/commit claim remains unaudited.

- `SmartBAnomaly` at `591–610`, `663–665`: not in this repo. Sibling checkout supports the AIC weights and sign-uniform claims, but the paper correctly cannot count this as repo-local evidence.

- `SmartV`, `SmartVRev` at `701–702`: verified as local preprints containing mass/spectral projection material. Since this paper cites them only as out-of-scope context, no issue.

**4. Tightness**

- `121–124`: “This vocabulary names the event without saying what it is” is too sweeping. Edit: “This vocabulary does not by itself specify a substrate-level selection mechanism.”

- `492–496`: “through the \(H_4\) Coxeter symmetry it constrains which attractor geometries can crystallise” is stronger than proved. Edit: “would constrain admissible attractor geometries in instances whose dynamics respects \(H_4\).”

- `539–545`, `573–584`: “implements” is too strong for a broad tuple plus file mapping. Edit: “is mapped to an observer-process architecture” or “realises this architecture at the process-description level.”

- `361–370`: the proposition is weaker than the hypotheses permit. Add a corollary: if \(\Psi_N^t\phi_N^{(0)}\to\phi_N^\star\), then \(\Psi_k^t\pi^\sharp_{N,k}\phi_N^{(0)}\to\pi^\sharp_{N,k}\phi_N^\star\).

**5. Surface Issues**

- `166–167`: duplicated wording remains: “parametrisation, parametrised by substrate geometry.” This was supposedly fixed; it is not.

- `640`: Unicode em dash in table cell. Probably fine under modern LaTeX, but use `---` for portability.

- `654–656`: specify `operator norm on \(\ell^2(V_{600})\)`.

- `779–781`: good disclosure that `verify_kernel.py` writes output; consistent with not rerunning in a read-only review.

- No undefined macros found by inspection.

**6. Top Three Fixes**

1. Fix the projection/bonding-map formalism at `237–260`. The cited refinement paper does not give the carrier-level \(\pi:G_{k+1}\to G_k\) used here. This is the main mathematical gap.

2. Downgrade or formalise the ARIA “implements” claim at `539–545` and `573–584`, especially because Tier 2 is not commit-pinned and not repo-local.

3. Correct evidential labels around exactness and imported computations: `648–656` should distinguish exact P2 algebra, floating-point local reproduction, and analytic identity.

Publication ready: **No**. The central proposition is salvageable, but the projection-map formalism and implementation-evidence language still overstate what is actually established.
