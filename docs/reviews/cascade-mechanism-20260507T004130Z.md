**1. Claim Audit**

- `cascade-mechanism.tex:87-101`: abstract now states the final `cascade-refinement-compat` scope: `(O3)` closed only in the abstract scalar pure-midpoint model, `(O2)` as stated false, Schur substitute discharged, `(O1)` selection out of scope, P3/P4 lift conditional on `(L1)/(L3)`. Verified against `3320373`. The claim is correctly scoped.
- `cascade-mechanism.tex:123-131`: epistemic box carries the same corrected scope. Verified. No stale over-claim.
- `cascade-mechanism.tex:487-499`: Proposition “Conditional closure-residual compositionality” is established by the proof at `501-518`, assuming `R_k >= 0` from the standing setup. No over-claim.
- `cascade-mechanism.tex:520-536`: Corollary “Convergence propagation under flow intertwining” is established by `537-548`. It correctly does not invoke monotonicity.
- `cascade-mechanism.tex:660-676`: `(O1)` worked-invocation bullet is corrected. It no longer claims existence or spectral gap is open; it says selection of a physically meaningful nontrivial kernel element is open. This matches `cascade-refinement-compat` Proposition `prop:O1-status`.
- `cascade-mechanism.tex:677-703`: `(O2)/(O3)` bullets still say “not closed in the source” at `695` and `702`. This is defensible only if “source” means `CascadeClosureDynamics` alone, not the new companion paper. As written, it is stale-looking. Add “in `CascadeClosureDynamics` alone; see current verdict below.”
- `cascade-mechanism.tex:711-729`: current verdict correctly matches `cascade-refinement-compat`: `(O3)` closed for scaled curvature in the abstract model; `(O2)` substitute discharged; strict `(O2)` false; P3/P4 lift conditional.
- `cascade-mechanism.tex:804-810`: exact identity `||Cphi^{-1}|| = phi^2` is established by the shifted connected Laplacian argument. This is sound.
- `cascade-mechanism.tex:891-913` and `1153-1175`: ARIA empirical claims are explicitly imported and caveated, not proved here. That is acceptable.
- `cascade-mechanism.tex:1052-1071`: consolidation paragraph has the final scope. No stale “none of `(O1)-(O3)` closed” wording remains.
- `references.bib:22-26`: bibliography note is corrected and matches `3320373`.

**2. Internal Consistency**

- All `\ref`/`\eqref` targets in the target TeX resolve statically. All cited keys used by the TeX exist in `references.bib`.
- The main notation transition from abstract `R_k` to imported finite-level `R_n` is explicitly limited at `296-305`; no conflict.
- The remaining weak cross-reference is `cascade-mechanism.tex:733-734`: “nontrivial selection out of scope per §ARIA–§witness.” Those sections do not define the selection obligation. Cite `§3.4` / `ssec:consumer-api` instead.

**3. External Consistency**

- `CascadeRefinementCompat`: verified locally at commit `3320373`. It supports the abstract scalar pure-midpoint `(O3)` discharge, the Schur substitute for `(O2)`, false strict `(O2)`, and conditional P3/P4 lift.
- `CascadeClosureDynamics`: verified labels for gradient operator, energy dissipation, coercive contraction, refinement compatibility definition, flow existence, mass-only flow intertwining. The paper’s restriction to mass-only flow intertwining is accurate.
- `CascadeRefinementSpaces`: verified `thm:bonding`, `thm:commute`, and `prop:adjoints`; `(L2)` as already-proved input is supported.
- `CascadeAlgSubstrate`: verified `thm:pi-H`, `thm:icosian-closure`, `thm:shell-class`, and the recorded `94+26` spectrum split.
- `AriaClosureKernel`: verified local operator-norm, shell, degree, and variant-correlation numbers against local paper/repro expected outputs.
- `SmartARIAChess`: verified local source contains `17/18`, `18/18`, P10 `15` vs `20` permutation caveat, seed `42`, and HCP `-11.58σ/+6.80σ`.
- `SmartBAnomaly`: not locally verifiable in this repository. The target paper says it is external and commit-pinned, which is honest.
- `ObserverInstance`: mismatch. `docs/observer-instance-definition.md` defines a five-tuple observer instance, not the seven-tuple `Ocal=<B,S,M,G,I,C,A>` used at `cascade-mechanism.tex:1356-1359`. The row should cite the present paper as primary and mention `ObserverInstance` only as related upstream context.

**4. Tightness**

- `695`, `702`: replace “not closed in the source” with “not closed in `CascadeClosureDynamics` alone; the companion-paper update is stated below.”
- `733-734`: replace “per §ARIA–§witness” with “per the consumer API, `(O1)`, in §3.4.”
- `1356-1359`: replace “Observer instance” with “Observer-process architecture,” or change the cited object to the five-tuple from `ObserverInstance`.

**5. Surface Issues**

- No unresolved labels or missing bibliography keys found by static scan.
- I did not compile or run repro scripts because the workspace is read-only; the static LaTeX structure looked balanced.
- Minor prose issue at `1055-1056`: “residual zero, fixed-point status are propagated” should be “residual zero and fixed-point status are propagated.”

**6. Top Three Fixes**

1. Fix the Appendix C observer row at `1356-1359`; it currently conflates the paper’s seven-tuple with the cited five-tuple observer-instance document.
2. Disambiguate stale-looking source-state wording at `695` and `702`; otherwise a reviewer will read it as contradicting the final `cascade-refinement-compat` update.
3. Correct the wrong out-of-scope cross-reference at `733-734`; selection is out of scope by the consumer API, not by the ARIA/witness sections.
