Target reviewed: `papers/cascade-refinement-compat/cascade-refinement-compat.tex`.

**1. Claim Audit**

- “`Schur(A_{n+1}^{vertex}) = 1/2 A_n^{vertex}`” (lines 332-345): established in the abstract pure-midpoint model. Hidden dependency: the child-edge orientations must be inherited coherently from the parent edge. Definition 1.1 says “unoriented edge convention” (lines 181-183) while the proof uses oriented children `(u,m_e),(m_e,v)` (lines 200-203, 431-445). Add this as an axiom.

- “`Schur(\widetilde A_{n+1}) = \widetilde A_n`” (lines 342-345): established, assuming the previous point. The scaling argument is correct.

- “The scaling factor `2^n` is the unique factor” (lines 275-277): over-claimed. It is unique only after fixing a normalization, e.g. `\lambda_0=1`; otherwise every `c 2^n` works.

- “(O3) ... with equality iff harmonic extension” (lines 491-501): established. The proof correctly uses the Schur minimizer and positive definiteness of `A_{II}`. This conflicts with the abstract, which says “if (but not in general only if)” (lines 57-60). In this model it is only-if.

- Corollary “(O3) is closed in the abstract pure-midpoint model” (lines 550-562): follows from Theorem 3.1, with the stated scope. No full P3/P4 claim is made here.

- Proposition 4.1 strict intertwining failure and defect formula (lines 572-593): the per-vertex formula `D_n\psi=B_n\delta(\psi)` is established by lines 614-638. This Round 1 fix stuck.

- Proposition 4.1 kernel decomposition (lines 595-606): the algebraic decomposition is established. The graph-theoretic criterion is not stated carefully enough. “closed walk of even length” (lines 600-602) should be “nonzero unsigned-incidence kernel, equivalently an even-cycle contribution in the relevant component”; closed walks with repeated edges make the current phrase ambiguous.

- Proposition 4.1(iii) “does not vanish ... not at all when `G_n` has at least one edge” (lines 607-609): the intended claim, that the restriction is not the zero operator, is true. The proof at lines 675-682 is weak because it allows cancellation. Use the constant boundary vector and zero midpoint values; then `B_n\delta` is positive on every non-isolated vertex.

- Proposition 5.1 kernel/convergence (lines 728-749): established. It is finite-dimensional graph Laplacian spectral theory. It does not supply a selection rule; the text mostly respects that.

- Numerical verification claim “all linear algebra is exact Fraction arithmetic” (lines 471-481): over-claimed. The Schur/defect matrix checks are exact, but the script computes displayed eigenvalues through floating `np.linalg.eigvalsh`. Say the load-bearing equalities are exact; eigenvalues are a float sanity check.

- “numerically they do not in general” for invariant sectors (lines 991-996): unsupported in the paper and not covered by `explore_defect.py`, which only tests the edge and triangle towers. Remove or add a C4/flow-invariance computation.

**2. Internal Consistency**

- Abstract equality condition conflicts with Theorem 3.1: lines 57-60 say equality is not only-if; lines 500-501 prove iff. Fix the abstract.

- Definition 1.1 mixes “unoriented edge convention” with oriented coboundaries and oriented child-edge averaging (lines 181-193, 197-203). The Schur proof depends on coherent orientations.

- Discussion says `range(H_{n+1}) = ker D_n` “when the parent graph has no bipartite component” (lines 957-958). This is false. Forests are bipartite and have equality; non-bipartite graphs with enough cycles can have nonzero unsigned-incidence kernel. Use the actual condition `ker B_n=0`.

- The O2 language oscillates. Lines 90-93 say O2 is “closed at the Schur / boundary-energy level”; lines 703-717 correctly say O2 as stated is flow-level and remains false. Prefer “Schur-energy replacement for O2” rather than “O2 closed.”

- Cross-references in the target file appear to resolve to defined labels. I did not find a broken `\ref`/`\eqref`.

**3. External Consistency**

- P3/P4 structural contrast is verified. `cascade-refinement-spaces.tex` has centroids and extra midpoint/centroid edges at lines 273-287, and `F`-valued oriented chain spaces at lines 464-493.

- P4 coboundary relation is verified. `cascade-closure-dynamics.tex` Proposition `coboundary-refinement` states `p^1 d_{n+1}=1/2 d_n p^0` at lines 896-937.

- CascadeMechanism consumer API is verified. `cascade-mechanism.tex` lists O0-O3 at lines 580-612 and proves conditional residual/fixed-point propagation at lines 475-506.

- The claim that `CascadeMechanism §3.5` records O1-O3 open (target lines 120-127) is only partly current. The local mechanism paper still records the old open-source-state analysis at lines 647-688, but then already incorporates this paper’s abstract-model update at lines 691-719. The target should say “original source-state analysis” or cite the precise paragraph.

- I could not verify from P3/P4 the statement that `A_{II}` invertibility is “the standard finite-dimensional case” (target lines 320-322). It is true in the abstract midpoint model, but not located as a P3/P4 result.

**4. Tightness**

- Line 59: replace with “with equality iff `\psi` is the harmonic extension of `p^0\psi`.”
- Line 275: replace “unique factor” with “unique up to an overall normalization.”
- Lines 320-322: replace the P3/P4 aside with “In Definition 1.1, `A_{II}=2I` on midpoints, hence invertible.”
- Lines 714-717 and 918: replace “discharges O2” with “discharges a Schur-energy substitute for O2; O2 as stated remains false.”
- Line 958: replace with “with equality exactly when `ker B_n=0`.”
- Lines 1006-1008: replace “all computations” with “the displayed Schur and defect matrix equalities.”

**5. Surface Issues**

- No undefined LaTeX macros found by inspection.
- “Schur is a quadratic operation” (line 463) is misleading; the Schur complement is nonlinear in blocks but homogeneous of degree one under scalar multiplication.
- “defect operator `Schur(A_1)-A_0`” (lines 873-875) conflicts with the paper’s named defect `D_n`; call it “Schur difference.”
- “not at all” (line 608) is colloquial and ambiguous.
- The checked-in `repro/output/explore_defect.txt` is stale relative to expected output, though the current script stdout matches `expected_outputs`.

**6. Top Three Fixes**

1. Fix Proposition 4.1’s incidence-kernel criterion and the false discussion statement at lines 600-606 and 957-958. This is the main residual mathematical error.

2. Add an explicit coherent-orientation hypothesis to Definition 1.1, because Theorem 2.1 depends on it through `p^1 d_{n+1}=1/2 d_n p^0` (lines 178-203, 431-445).

3. Reconcile the status/equality language: abstract lines 57-60 vs Theorem lines 500-501, and “O2 closed” phrasing at lines 90-93/918 vs the correct flow-level failure at lines 703-717.
