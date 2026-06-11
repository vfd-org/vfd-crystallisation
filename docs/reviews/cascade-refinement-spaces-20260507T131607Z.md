**Claim Audit**

- `Proposition 2.5`, “Refinement properties” (lines 460-472): mostly established from the definitions. The proof is thin for the labelled-edge multiset case: `E^{or}` and duplicate endpoint labels must be formal labelled edges, not ordinary graph edges. State that explicitly.
- Parenthetical claim that duplicate endpoint generation “does not occur at level `0 -> 1`” (lines 327-329): not proved and not used. Delete or cite a check.
- `Proposition 3.3`, finite Hilbert structure and dimensions (lines 628-638): established.
- `Theorem 4.3`, bonding contractions (lines 701-710): established. Edge proof has a coefficient slip: after line 731 the summed bound is `1/4 sum_sub`, not `1/2 sum_sub` as line 740 writes. The final contraction remains true.
- `Proposition 4.5`, adjoint relations and half-section (lines 784-798): established; the `1/2` adjoint scaling is correct.
- `Theorem 5.2`, `X_cyl^0 ≅ c_{00}` (lines 898-909): established, assuming vertex elements are formal set elements in the ascending union.
- `Lemma 5.5`, finite-level norm compatibility (lines 967-972): established.
- `Lemma 6.2`, inverse-limit inner-product limits (lines 1003-1008): established.
- `Theorem 6.3`, `X_inv^0 ≅ ell^2(V_infty;F^0)` (lines 1024-1040): established for the vertex sector.
- `Proposition 6.4`, density of `X_cyl^0` (lines 1082-1091): established.
- `Lemma 8.1`, Coxeter unitarity (lines 1155-1160): established at the real Hilbert level.
- `Theorem 8.3`, intertwining identities (lines 1289-1357): items (1)-(3) are established. Item (4) needs work: `g|_{\Q(\varphi)/\Q}` is used but never defined as an action on the mixed form, and the `D_4` case relies on the unstated fact that the standard `D_4` representation preserves `\Q^4`. The `H_4` exclusion is correct in spirit but overworded.

**Internal Consistency**

- Mis-cited label: line 389 says the edge bonding map `p^1` is “of Definition \ref{def:edge-parent}`. It is defined in `def:p1`, not `def:edge-parent`.
- False negative claim: lines 1109-1124 say contraction monotonicity does not establish completeness of the edge inverse-limit set. This is false in general: bounded compatible families for contractions are complete in the limit/sup norm by the standard coordinatewise Cauchy argument. You may decline to identify it with an `ell^2` edge space, but not on this ground.
- Labelled-edge multiset vs graph language remains unresolved (lines 291-292, 321-329, 612-623, 635-637). If `E_n` is a labelled multiset/multigraph, define oriented labelled edges and dimension counts for labelled edges.
- `g|_{\Q(\varphi)/\Q}` appears in Theorem 8.3(4) (line 1332) without a definition.
- Static extraction found no unresolved internal `\ref` labels or missing bibliography keys in this file. I did not recompile; no `.aux`/`.log` files were present.

**External Consistency**

- P1 labels `def:sigma`, `def:sigmaV`, `thm:pisigma-functorial` are present and support the cited facts. The theorem applies to scalar extensions of `\Q`-linear maps, matching the restricted use.
- P2 labels `def:V600`, `def:V24`, `prop:24-in-600`, `def:Cl-basis`, `def:octonions`, and `def:Q-forms` are present and support the relevant imports.
- P2 does **not** support line 1640’s description of `def:icosian-ring` as “the icosian ring `\Z[\varphi]^4`.” P2 explicitly says the icosian ring is not of that simple form. Fix this.
- Line 1642 says `V_{600}` has `\Z[\varphi]`-rational entries. P2’s coordinates include halves; say `\Q(\varphi)`-rational or `(1/2)\Z[\varphi]`-coordinates.
- The claim that `CascadeRefinementCompat` names the scope gap (lines 397-401) is verified: its `sec:scope-and-gap` exists and explicitly isolates the abstract scalar pure-midpoint model and lift hypotheses.
- The `W(H_4)` matrix-entry inference (lines 1652-1658) is correctly labelled as an inference, not a P2 theorem.

**Tightness**

- Lines 184-186: “Commuting refinement / Coxeter / `\sigma` intertwining identities” is too broad. Edit: “finite-level Coxeter intertwinings and mixed-form vertex `\sigma` intertwinings.”
- Lines 1339-1342 and 1368-1384: replace categorical “`W(H_4)` reflections ... are not” with “not all `W(H_4)` elements are defined over the chosen `\Q`-form.”
- Lines 1567-1572: “a non-trivial `W(H_4)` reflection” is too strong. Edit: “some `W(H_4)` reflections have non-rational `\Q(\varphi)` entries...”
- Lines 1112-1124: replace with “we do not identify the edge inverse limit with a concrete `ell^2` space or use it downstream.”

**Surface Issues**

- Line 389: wrong reference label for `p^1`.
- Line 740: coefficient should be `1/4` if following the displayed estimate sharply.
- Line 146: abstract edge-parent map omits the `\bot` codomain; write `E^{or}(G_n^\bullet)\cup\{\bot\}` or say “on subdividing edges.”
- Lines 115-117 name P5 and P9-P13 as consumers but give no bibliography entries for them.
- Lines 1640-1642 contain inaccurate P2 bibliography descriptions, as above.

**Top Three Fixes**

1. Fix the false edge inverse-limit statement at lines 1109-1124. This is the main mathematical defect.
2. Repair Theorem 8.3(4): define `g|_{\Q(\varphi)/\Q}`, state rational-form preservation for `D_4`, and weaken the `H_4` source-theorem exclusion wording (lines 1327-1343, 1362-1389, 1551-1572).
3. Clean the citation/definition defects: wrong `p^1` label at line 389 and inaccurate P2 descriptions at lines 1640-1642.
