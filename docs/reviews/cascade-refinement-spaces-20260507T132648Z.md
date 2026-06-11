**1. Claim Audit**

- `Proposition~\ref{prop:refinement-equivariant}` at line 464: mostly established. The formal refinement construction gives literal inclusion, equivariance, and two parent preimages. However the proof of (3) at lines 486-489 appeals to Coxeter’s Schläfli refinement rather than the paper’s own labelled-edge refinement. This should be proved by induction from Definitions 2.2-2.3. Also, the chosen \(W(D_4)\)-action on the \(V_{24}\) realization is not fixed explicitly enough.

- `Proposition~\ref{prop:Xn-Hilbert}` at line 632: established. Dimension counts at lines 638-641 follow from finite vertex/edge sets and the fibre dimensions.

- `Theorem~\ref{thm:bonding}` at line 705: established. The edge proof uses a weaker coefficient than the sharp Cauchy-Schwarz bound, but the contraction conclusion is valid.

- `Proposition~\ref{prop:adjoints}` at line 792: established. The factor \(1/2\) in \(j^1\) is correctly forced by the oriented-edge inner product.

- `Theorem~\ref{thm:Xcyl-direct-limit}` at line 906: established for the vertex sector.

- `Lemma~\ref{lem:Xcyl-compatibility}` at line 975: established. This also exposes a contradiction with the introduction: zero-extension is isometric under the counting measure used here.

- `Lemma~\ref{lem:Xinv-limit-exists}` at line 1011: established for real Hilbert spaces.

- `Theorem~\ref{thm:Xinv-Hilbert}` at line 1032: essentially established. The proof at lines 1076-1080 should add one sentence that the cross-term series is absolutely convergent by Cauchy-Schwarz in \(\ell^2\). Not a fatal gap.

- `Proposition~\ref{prop:Xcyl-dense}` at line 1090: established.

- `Lemma~\ref{lem:coxeter-unitary}` at line 1163: conditional on the missing explicit choice of the \(W(D_4)\)-action on the chosen \(V_{24}\) coordinate model. Once that is fixed, the proof is routine.

- `Theorem~\ref{thm:commute}` at line 1297: items (1)-(3) are established. Item (4), lines 1335-1369, is not stated with theorem-level precision: the \(D_4\) branch commutation is clear, but the \(H_4\) branch only asserts commutation on the \(\sigma\)-trivial summands. State the exact restricted subspace and equality, or split (4) into separate clauses.

- Numerical claims: \(120\) vertices for \(V_{600}\), \(24\) for \(V_{24}\), \(\dim F^0=32\), \(\dim F^1=7\), and mixed \(\mathbb Q\)-dimension \(36\) are all supported by the cited definitions/proofs.

**2. Internal Consistency**

- Serious contradiction: lines 130-136 say forward zero-extension “is not isometric under any naturally-normalized \(\ell^2\) structure.” But this paper uses counting measure, and zero-extension \(j^0\) is isometric; see lines 766-770 and 975-987. Replace with: “under probability-normalized finite-level \(\ell^2\), zero-extension is not isometric; in any case the system is inductive, not projective.”

- The \(D_4\) branch uses \(V_{24}\subset V_{600}\) but also invokes the “standard \(D_4\)-reflection representation” preserving \(\mathbb Q^4\), lines 1343-1349. The paper must specify whether this is the signed-permutation realization, the \(R\)-conjugated realization from P2, or a chosen \(W(D_4)\subset W(F_4)\) acting on the displayed \(V_{24}\).

- Local `\ref` targets resolve by source inspection. The external optional reference `\S\texttt{sec:scope-and-gap}` exists in `cascade-refinement-compat.tex`.

**3. External Consistency**

- P1 claims verified. `def:sigma`, `def:sigmaV`, and `thm:pisigma-functorial` exist in `papers/cascade-sigma-rationality/cascade-sigma-rationality.tex` and state what P3 says: coefficientwise \(\sigma\), and functoriality for scalar extensions of \(\mathbb Q\)-linear maps.

- P2 claims mostly verified. `def:icosian-ring`, `def:V600`, `def:V24`, `prop:24-in-600`, `thm:icosian-closure`, `def:Cl-basis`, `def:octonions`, and `def:Q-forms` exist and support the cited substrate data.

- The claim that \(W(D_4)\) preserves the chosen \(\mathbb Q\)-form is not explicitly established by the cited P2 labels `def:V24` and `def:Q-forms`. It is standard, but P3 should either cite P2 `def:D4` plus a classical Weyl-group fact, or spell out the matrices.

- Downstream citation descriptions are accurate in broad scope: `cascade-refinement-compat.tex` does name the abstract pure-midpoint model and lift hypotheses; `cascade-mechanism.tex` records O0-O3; P4 does put dynamics on the P3 finite-level spaces.

**4. Tightness**

- Line 135 is too strong and false in this paper’s own norm. Edit as above.

- Lines 65-67 are too compressed: “outside the hypothesis” should become “not scalar extensions of maps preserving the chosen standard \(\mathbb Q^4\subset\mathbb Q(\varphi)^4\).”

- Line 115 says these are “load-bearing inputs” for many future papers. Safer: “intended load-bearing inputs.”

- Lines 1335-1369 should not be a prose caveat inside a theorem item. State the exact restricted Coxeter-\(\sigma\) theorem.

**5. Surface Issues**

- Inconsistent notation: many maps are written \(X_n^0\), \(X_n^1\) without \(\bullet\) after the branch has notational significance.

- The phrase “standard \(\mathbb Q^4\)” for the \(H_4\) sector needs a fixed basis reference; P2’s \(V_{600}\) coordinates are in the quaternion coordinate basis, not an “icosian basis” in the ring-theoretic sense.

- No undefined local labels found by source scan.

- No broken LaTeX obvious from source inspection. I did not run a TeX build.

**6. Top Three Fixes**

1. Fix the zero-extension contradiction at lines 130-136. As written, the introduction denies the isometry that Lemma 6.2 proves and the rest of the vertex construction uses.

2. Make Theorem 8.3(4), lines 1335-1369, a precise restricted theorem. State the exact subspace for the \(H_4\) branch and the exact commuting identity there.

3. Define the \(W(D_4)\)-action on the chosen \(V_{24}\) model explicitly before using equivariance and rationality, especially lines 272-279, 1142-1156, and 1343-1349. This is a hidden hypothesis in the current proof chain.
