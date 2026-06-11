Target line refs are to [cascade-refinement-compat.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-refinement-compat/cascade-refinement-compat.tex:1>).

**1. Claim Audit**
- “The scaling factor `2^n` is the unique exponential factor...” L286. Mostly established by the displayed recurrence `c_{n+1}/2=c_n`, but it silently assumes `A_n^{vertex}\ne 0`. Definition 1.1 permits edgeless graphs, where the identity is vacuous and no scaling is forced. Add “for nonzero parent Laplacian / nontrivial refinements.”
- “Schur complement ... is exactly half...” L362. Established. The proof is valid in the abstract scalar pure-midpoint model; the degree-2 midpoint hypothesis is used essentially at L453-L459.
- “verified to exact rational precision...” L501. Verified locally by running `explore_defect.py`; its output matches `repro/expected_outputs/explore_defect.txt`. This verifies only the two displayed finite instances, which the text correctly says.
- “Energy intertwining; discharge of (O3)” L525. The theorem is established in the abstract model. Equality iff harmonic extension follows from positive definiteness of `A_{II}`. However the proof text at L572-L578 contains a wrong algebraic phrase: after multiplying by `2^n`, one should regroup directly, not “divide by 2.”
- “(O3) is closed in the abstract pure-midpoint model” L584. Established, with the stated scope limitation.
- “Strict operator intertwining fails; kernel of the defect” L607. Established. The per-vertex defect formula and kernel splitting are correct. The graph-theory rank formula is externally cited, not proved locally.
- “Kernel and convergence of `\widetilde A_N`” L780. Established by standard finite-dimensional spectral decomposition. The nontrivial-selection caveat is appropriate.
- Worked Tower I/Tower II matrix claims L842 and L907. The Schur and defect matrices match the script. Remaining issue: Tower I still writes unsigned incidence as `B_0` at L895, contradicting the paper’s own `\mathcal{B}_n` disambiguation.

**2. Internal Consistency**
- The Round 4 O3 cross-reference is fixed in the main TeX: O3 now points to Theorem `\ref{thm:O3-discharge}` / Corollary `\ref{cor:O3-closed}`, not the Schur theorem.
- The lift-hypothesis section now correctly marks `(L2)` as already proved, L231-L238, and says only `(L1)` and `(L3)` are open, L243-L248. The status-table caption also preserves this distinction, L980-L985.
- The `B_n` collision fix is incomplete: L627-L631 uses `\mathcal{B}_n`, but L895 reintroduces `$B_0$`.
- I found no unresolved internal `\ref`/`\eqref` labels.
- The P3/P4 lift language is sometimes too compressed. At L1053-L1056 the “full Schläfli P3/P4 tower” is cited only to `CascadeClosureDynamics`; it should cite both `CascadeRefinementSpaces` and `CascadeClosureDynamics`, as earlier passages do.

**3. External Consistency**
- `CascadeRefinementSpaces` claims about vertices, midpoints, centroids, and extra edges at target L154-L169 are verified against [cascade-refinement-spaces.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-refinement-spaces/cascade-refinement-spaces.tex:273>) and L327-L330 there.
- The `F`-valued vertex/edge chain-space claim at target L162-L165 is verified against [cascade-refinement-spaces.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-refinement-spaces/cascade-refinement-spaces.tex:464>).
- `(L2)` as already-proved input is verified: `p^1(p^1)^* = 1/2 I` follows from Proposition `prop:adjoints` parts (3)-(4), [cascade-refinement-spaces.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-refinement-spaces/cascade-refinement-spaces.tex:655>).
- The coboundary refinement relation cited at target L214-L216 and L271-L275 is verified in [cascade-closure-dynamics.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:896>).
- The coboundary block `B_n` cited at target L630-L631 is verified in [cascade-closure-dynamics.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:366>).
- The cascade-mechanism API `(O0)--(O3)` is verified in [cascade-mechanism.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-mechanism/cascade-mechanism.tex:580>). The source-state/open-status and updated-status paragraphs are both present at L647-L719 there.
- I did not verify the claim “The reproduction bundle of `CascadeMechanism` is unaffected” at target L1076 from a cited source. Either justify it or delete it.

**4. Tightness**
- L40 “lifts the source’s coboundary ... relation” is stronger than necessary. Suggested edit: “gives an abstract-model curvature analogue of the source’s coboundary factor-`1/2` relation.”
- L286 “unique exponential factor” needs the nonzero-Laplacian caveat.
- L602 “closes the energy-level refinement question” should read “closes the energy-level refinement question in the abstract model.”
- L1001 “cascade-mechanism users invoking that substitute find it discharged here” risks implying the substitute is part of `(O2)`. Suggested edit: “This proves the substitute; it does not discharge `(O2)` as stated.”

**5. Surface Issues**
- L572-L578: algebraic wording error, “after dividing by 2.”
- L895: change `$B_0` to `$\mathcal{B}_0$`.
- L631: “Definition lines 366--376” is clumsy; cite `Definition~\texttt{def:Bn}` or name the definition.
- L1054: cite both P3 and P4 sources for the full tower.
- Hard-coded source line numbers in prose, e.g. L155, L215, L237, are brittle. Prefer labels where available.

**6. Top Three Fixes**
1. Fix the remaining scope/overclaim pressure around the P3/P4 lift: L222-L250, L973-L985, L1001-L1005, L1053-L1056. The abstract-model theorem is solid; do not let status prose imply a full-tower result.
2. Correct the mathematical precision issues: scaling uniqueness caveat at L286-L295 and the faulty “divide by 2” wording at L572-L578.
3. Finish the Round 4 notation cleanup: replace `B_0` at L895 with `\mathcal{B}_0`, and clean the associated source citation at L631.
