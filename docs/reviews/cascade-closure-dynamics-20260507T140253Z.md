**1. Claim Audit**

P4 line numbers unless stated.

- “`$X_n$ is finite-dimensional`” (286-294): established by P3 `prop:Xn-Hilbert`; verified locally at P3:638-654.
- “`d_n^*` is the inner-product adjoint” (343-347): proof is incomplete. The formula at 334-336 returns an element of `F^1=\Im(\OO)`, not visibly an element of `F^0`; the inclusion into the `V_8` summand of `F^0` must be stated. Without that, the codomain `X_n^0` is not actually defined.
- “`A_n` top-left block is the classical combinatorial graph Laplacian on `X_n^0`” (368-370): over-claim. Since `d_n` first projects `F^0` to `\Im(\OO)` (313-318), `d_n^*d_n` is a projected fibre Laplacian, not the full graph Laplacian on all 32 vertex fibre components.
- “Bounds on the block operators” (403-419): final bounds are established. The proof text at 437-438 should say oriented-edge counting gives up to `2 deg`, not “at most `deg`”; the weaker stated bound survives.
- “`E_n` is indefinite in general … eigenvalues `±sqrt(lambda)` for each `lambda >= 0`” (495-500): basically correct for nonzero singular values; change `\lambda \geq 0` to `\lambda>0`. Zero eigenvalues do not form an indefinite pair.
- “Gradient operator” theorem (518-530): established modulo the missing `F^1 -> F^0` inclusion in `d_n^*`.
- “Gradient flow exists and is unique” (584-606), “flow is reversible” (625-629), “energy dissipation” (654-665), “norm contractivity under positivity” (700-705): established.
- “Euler step is energy-decreasing for small `eta`” (744-763): established pointwise in the current state. The paper should not let the abstract/intro imply one fixed global step size unless it states the finite-dimensional uniform bound or restricts to a spectral subspace.
- “Strict contraction on coercive invariant subspaces” (824-837): established.
- “No global contraction without coercivity” (853-858): established.
- “Coboundary refinement compatibility, factor `1/2`” (910-921): established assuming P3’s edge-parent convention. Typo in proof: line 935 says “level-`(n+1)` edge `e`” but `e` is a level-`n` edge.
- “Mass-block refinement compatibility” (968-979): established.
- “`L_n` is refinement-compatible in the mass-only case” (1024-1035) and “flow intertwining” (1045-1055): established. In the proof, line 1064 should say powers are “intertwined by `p`”, not that they “commute” with `p`.
- “Symmetries commuting with `L_n` commute with the flow” (1091-1096): established, but only conditional. No theorem proves actual Coxeter equivariance of `L_n`.
- “Generator bounds table” (1166-1216): mostly established. The `j^1` norm equality at 1185-1187 is not stated in P3 `prop:adjoints`; it is derivable from P3:793-804 and should be proved or cited as a calculation. The `G_2` norm-one claim at 1211-1216 is not contained in the cited P2 labels alone; P2 gives the stabilizer and an SU(3) identification, but not as a quoted operator-norm theorem.
- “Admissible intertwiners are bounded, continuous, Borel” (1230-1254): boundedness/continuity/Borel are established for finite formal expressions, but the proof omits the scalar factors `|c_i|` required by the definition at 1150-1153. Item (4) only covers pure compositions, while admissible expressions also include sums.

**2. Internal Consistency**

- Line 905 says the paper will verify that “`A_n, B_n, C_n` form refinement-compatible families.” This directly conflicts with 1003-1009, which says no such identities are proved for `A_n` or `B_n`. Replace 905-908 with a statement that only `d_n` and `C_n` are analysed.
- The label `prop:adjoint-refinement` (969) names an adjoint result, but the proposition is mass-block compatibility. This is a bad leftover label; rename to `prop:mass-refinement`.
- The branch parameter `\bullet` is introduced in definitions but then suppressed in most theorem statements. Add “Fix `\bullet \in {H_4,D_4}` throughout” or quantify every theorem over `\bullet`.
- Internal `\ref`/`\eqref` labels resolve; I found no undefined or duplicate labels.
- “Finite-level generator list” (1113) contains parameterized families, especially `{e^{-tL_n}: t>=0}` and implicitly stabilizer elements. Do not call it a finite list.

**3. External Consistency**

- P3 finite-level spaces: P4 cites numeric “Defs. 4.2, 4.3” at 276. Verified as P3 `def:Xn-0` and `def:Xn-1` at P3:603-636, but this should be converted to label-form citation.
- P3 dimension claim: P4 291-293 verified by P3 `prop:Xn-Hilbert` at P3:638-654.
- P3 fibres: P4 cites numeric “Notation 3.3” at 314. Verified as P3 `not:fibres` at P3:547-596, but again not label-form.
- P3 bonding maps and edge-parent: P4 897-921 verified by P3 `def:edge-parent`, `def:p0`, `def:p1`, `thm:bonding` at P3:430-455 and 687-737.
- P3 adjoints: P4 1183-1187 cites `prop:adjoints`. The adjoint and half-section identities are verified at P3:813-878. The exact norm `\|j^1B\|^2=1/2\|B\|^2` is not stated there; it is derivable but not directly cited.
- P3 sigma/non-extension: P4 1131-1138 is verified for `\sigma` by P3 `def:sigma` at P3:1324-1358. The icosian star-map part relies on P2 plus the sigma identification; it is not a standalone P3 theorem.
- P3 Coxeter unitarity: P4 1192-1193 and 1221-1224 verified by P3 `lem:coxeter-unitary` at P3:1228-1255.
- P2 `G_2` stabilizer: P4 1211-1216 verified only partly. P2 `def:G2`, `def:stab-u`, `fact:SU3-stab` exist at P2:1791-1819; the norm-one orthogonal action on `\Im(\OO)` should be separately stated or cite P2’s sketch at P2:1821-1832.

**4. Tightness**

- 368-370: replace “the classical combinatorial graph Laplacian on `X_n^0`” with “the projected graph-Laplacian block induced by the `\Im(\OO)` quotient.”
- 625: replace “Flow is reversible” with “The matrix exponential is invertible.” The current wording is physically misleading for a dissipative gradient flow.
- 905-908: replace with “We verify the coboundary factor relation and exact mass-block compatibility.”
- 1232-1234: replace “operator on the finite-dimensional Hilbert space in its codomain” with “bounded linear map between the indicated finite-dimensional Hilbert spaces.”
- 68-70 / 152-156: say “pointwise energy descent for sufficiently small step size” unless adding a uniform spectral bound.

**5. Surface Issues**

- “explicit explicit” at 92 and 1369.
- “a explicit” at 199.
- “finite-generator” at 257 is still too strong for a parameterized generator family.
- Typo at 935: `e` is a level-`n` edge, not a level-`(n+1)` edge.
- Numeric local citations remain at 276 and 314 despite the stated label-citation cleanup.
- Table shorthand “`deg`” at 1204-1205 should be `\deg(G_n^\bullet)`.
- No obvious undefined macros; internal references resolve.

**6. Top Three Fixes**

1. Fix the `d_n^*` codomain and projected-Laplacian issue: lines 313-318, 329-336, 368-370. This is the main mathematical clarity problem.
2. Remove the false Section 7 setup claim that `A_n,B_n,C_n` are all refinement-compatible: lines 905-908. The actual theorem only supports `d_n` with factor `1/2` and `C_n` exactly.
3. Repair the generator/intertwiner theorem: lines 1127-1129, 1166-1216, 1230-1254. State the parameterized nature of the generators, add the missing scalar-bound argument, handle sums in the conditional symmetry clause, and either prove or correctly cite the `j^1` and `G_2` norm claims.
