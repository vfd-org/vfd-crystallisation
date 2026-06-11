All target line numbers refer to `papers/cascade-refinement-spaces/cascade-refinement-spaces.tex`.

**1. Claim Audit**
- Prop. refinement properties, lines 423-436: essentially established. Round 2 edge class (c) is present at lines 322-325 and closes the triangle faces at lines 327-335. Remaining hidden convention: `E_{n+1}` is called a “disjoint union” of unordered graph edges at line 313; if identical midpoint-midpoint pairs can arise from different faces, this is a tagged multigraph, not an ordinary graph edge set. State the convention.
- Prop. finite-level Hilbert structure, lines 570-580: established. Dimension counts follow from finite sets and fibres.
- Thm. bonding contractions, lines 643-653: established. Edge proof has a slack/mistyped constant: line 682 should follow from line 671 with a `1/4` subedge sum, not `1/2`; the weaker `1/2` bound still proves contraction.
- Prop. adjoint relation, lines 726-740: established, including the half-section identity.
- Thm. `X_cyl`, lines 836-847: established for the vertex sector.
- Lemma finite-level norm compatibility, lines 905-910: established.
- Lemma inverse-limit inner products, lines 941-946: established, though the cross-term convergence should explicitly cite polarization over the real Hilbert structure.
- Thm. `X_inv ~= ell^2`, lines 962-978: established. The proof at lines 1006-1010 should mention monotone/absolute convergence, but the claim is correct.
- Prop. density, lines 1020-1029: established.
- Lemma Coxeter unitarity, lines 1093-1097: established given the branchwise action.
- Thm. intertwining identities, lines 1206-1268: not fully proved as written. Item (1) is proved. Item (2) proves the `p^1` identity but omits the `j^1` argument; it follows by adjunction and unitarity, but must be stated. Item (3) is true by direct fibrewise inspection, but the proof at lines 1347-1361 invokes a nonexistent P1 theorem label and treats the mixed form as if it were a single scalar extension. Item (4) is appropriately restricted, but its source citation label is wrong.

**2. Internal Consistency**
- Round 2 H4 sigma repair only partially landed. Lines 1252-1257 and 1291-1295 correctly say the full H4 statement is not delivered and not claimed. But the abstract still says “fails” at lines 62-64, and the recommended citation repeats “fails as a structural matter” at lines 1430-1434. This contradicts the theorem/remark.
- Line 176 says “Commuting refinement / Coxeter / sigma intertwining identities” without the later restriction that sigma is vertex-sector mixed-form only. Tone should be narrowed.
- Lines 1246-1248 and 1369 use `|_{\Q(\varphi)}`; the defined notation is `|_{\Q(\varphi)/\Q}` at lines 1160-1162.
- Lines 1348-1352 introduce `|_\Q` and `F^0_\Q`, neither defined. Use the mixed-form notation already defined.
- Lines 1259-1262 say the Coxeter intertwinings of (1)-(2) descend to vertex cylindrical/inverse spaces. Only the vertex part of (1) descends there; edge inverse/direct-limit spaces are explicitly not constructed.
- Lines 351-356 say the constructions depend on edge classes (a) and (b), but the edge bonding map uses only subdividing edges, class (a). Class (b) is part of the finite edge set, not the parent-fibre average.

**3. External Consistency**
- P1 `def:sigma`: verified locally at `cascade-sigma-rationality.tex` lines 189-199.
- P1 coefficientwise sigma: verified as `def:sigmaV`, lines 297-308. The bibliography’s `sec:coefficientwise` at line 1489 is not a local label.
- P1 theorem: target cites `thm:sigma-commutes` at lines 1253, 1273, 1358, 1434, 1490. I cannot find that label. The local theorem is `thm:pisigma-functorial`, lines 590-610.
- P2 `V_{600}` coordinates: verified, but under `def:V600`, local lines 778-801, not target’s vague `\S 5` at line 251.
- P2 `V_{24} subset V_{600}` and congruent to rescaled `D4`: verified under `def:V24` and `prop:24-in-600`, local lines 810-830. Target line 254 cites `thm:shell-class`, which is about Euclidean shells/conjugacy classes, not this claim.
- P2 Clifford basis: target cites nonexistent `def:Cl-1-3-basis` at lines 1122 and 1504. Local label is `def:Cl-basis`, lines 1672-1684.
- P2 octonion basis: target cites nonexistent `def:octonion-basis` at lines 1126 and 1505. Local relevant label is `def:octonions`, lines 1717-1733.
- P2 H4 rational matrix-entry claim in bibliography lines 1499-1502 is only an inference from P2 coordinates/icosian material, not a stated result of `thm:icosian-closure`.
- `CascadeClosureDynamics` as downstream dynamics on P3 chain spaces is verified: local lines 126-134 and 220-224.
- `CascadeRefinementCompat` pure-midpoint gap/O3 claim is verified in substance: local lines 153-252 and 526-591. But target’s `\S1.5` at lines 364 and 1527 appears stale; use the local label `sec:scope-and-gap`.
- `CascadeMechanism` consumer API `(O0)--(O3)` is verified: local lines 581-625.

**4. Tightness**
- Lines 62-64: replace “full `W(H4)`-sigma commutation ... fails” with “is not claimed here; the source theorem does not supply it.”
- Lines 103-105: “and analogously for sigma from P1” overstates; replace with “and the mixed-form vertex-sector sigma restriction identity.”
- Lines 176-178: replace “Commuting refinement / Coxeter / sigma intertwining identities” with “finite-level Coxeter intertwinings and mixed-form vertex sigma intertwinings.”
- Lines 1430-1434: replace the parenthetical with “full `W(H4)`-sigma commutation on the `V_H4` summand is not supplied by P1’s functoriality theorem and is not asserted here.”
- Lines 216-222 are appropriately conservative.

**5. Surface Issues**
- Nonexistent local source labels: `thm:sigma-commutes`, `sec:coefficientwise`, `def:Cl-1-3-basis`, `def:octonion-basis`.
- Remaining non-label in-repo citations: lines 251, 502, 1118, 1133, 364, 1527. The “label-based citations” fix did not fully land.
- Line 1143: “Its R-extension” should be “Its `\R`-extension”.
- Line 552: “For `n >= 0` define” should include `\bullet`.
- Line 1107 splits `\ref` across lines; TeX likely accepts it, but it is ugly and avoidable.
- Lines 1348-1352 use undefined shorthand notation.
- I did not find a build log in the paper directory, so I did not verify compiled cross-reference output.

**6. Top Three Fixes**
1. Fix the H4 sigma contradiction and P1 theorem citation: lines 63, 1253, 1273, 1358, 1431, 1490. Use `thm:pisigma-functorial`, or give a direct fibrewise proof for line 1224 and stop claiming failure.
2. Repair the P2 attributions: line 254 should cite `prop:24-in-600`, lines 1122/1504 should cite `def:Cl-basis`, lines 1126/1505 should cite `def:octonions`, and lines 1499-1503 should separate stated P2 results from inferences.
3. Clean Theorem 8.3 proof/notation: define the mixed-form restrictions consistently, add the missing `j^1` adjunction argument, and narrow the descent statement at lines 1259-1262 to the vertex sector.
