Files reviewed: P4 `cascade-closure-dynamics.tex`, plus local P2/P3/foundations sources.

**Verdict**

P4 has converged on the core finite-level dynamics. The Round 3 fixes are present: mass-only refinement scope is explicit, the coboundary proof carries `π`, the contraction theorem is downgraded to a bound, and the handoff warns against convergence claims.

It is **not quite publication-ready**. I see no fatal error in the main finite-level theorems, but there are remaining publication blockers in source consistency and citation contract.

**1. Claim Audit**

- P4 l.287, “`X_n` is finite-dimensional”: established by P3 `prop:Xn-Hilbert`; OK.
- P4 l.356, “`d_n^*` is the inner-product adjoint”: formula is correct, but proof is too compressed. It must explicitly use `π_{F^0→F^1}^* = ι_{F^1→F^0}` and the oriented-edge `1/2` convention.
- P4 l.420, “Bounds on block operators”: bound is valid and conservative. Line 442 suppresses the projection `π`; harmless for the bound, but sloppy.
- P4 l.539, “Gradient operator”: established. The proof gives the representing operator and gradient correctly.
- P4 l.605, “Gradient flow exists and is unique”: established.
- P4 l.646, “`e^{-tL_n}` invertible”: established.
- P4 l.676, “Energy dissipation”: established, including indefinite `L_n`.
- P4 l.722, “Norm contractivity under positivity”: established.
- P4 l.766, “Euler step energy-decreasing for small `η`”: exact one-step formula is established. Do not let downstream cite this as fixed-step global monotonicity without adding a uniform spectral bound.
- P4 l.846, “Strict contraction on coercive invariant subspaces”: statement is correct. Proof line 869 overstates equality over `[m_n,M_n]`; it should say “bounded by the maximum over the interval” unless `m_n,M_n` are spectral endpoints.
- P4 l.877, “Negative spectrum obstructs global contraction”: established.
- P4 l.931, “Coboundary refinement compatibility with factor `1/2`”: established under P3’s parent-fibre averaging convention.
- P4 l.993, “Mass-block refinement compatibility”: established.
- P4 l.1049 and l.1070, mass-only `L_n` and flow refinement compatibility: established.
- P4 l.1116, “Symmetries commuting with `L_n` commute with the flow”: established, conditional as stated.
- P4 l.1191, “Generator bounds table”: mostly established. The `G_2` stabilizer norm-one row needs either a local P2 lemma or an explicit proof that octonion automorphisms restrict orthogonally to `Im(O)`.
- P4 l.1260, “Admissible intertwiners are bounded, continuous, Borel”: established for fixed finite formal expressions. “Intertwiner” remains a misleading name because equivariance is only conditional in item (4).

**2. Internal Consistency**

- All internal `\ref`/`\eqref` targets resolve by static check; all citation keys have local `\bibitem`s.
- Major semantic conflict: P4 defines `E_n` as the indefinite off-diagonal coboundary/Dirac form, l.511-521. Earlier/current foundations use `E` as positive divergence/kinetic square. If P4 is replacing that, say so explicitly. Otherwise downstream “kinetic” citations will be ambiguous.
- P4’s “energy monotonicity” phrasing at l.68-69 and l.1363-1367 is too broad for the discrete scheme. The proved result is one-step descent under a pointwise step bound, not a blanket monotone iteration theorem.
- The notation `X_n` suppresses the branch `\bullet`; acceptable, but the paper should state once that all claims are branchwise.
- “Admissible finite-level intertwiner” is syntactic bounded-operator language, not actual intertwining unless the conditional symmetry hypotheses of l.1284-1292 are supplied.

**3. External Consistency**

- P3 fibres, dimensions, `X_n^0`, `X_n^1`: verified locally in P3 l.547-596 and l.603-678.
- P3 `p^0`, `p^1`, edge-parent map, two subdividing preimages: verified in P3 l.430-455, l.469-504, l.687-722.
- P3 bonding contraction and adjoint embeddings: verified in P3 l.726-778 and l.782-878. The `j^1` norm `2^{-1/2}` is locally supported.
- P3 Coxeter action/unitarity and sigma limitation: verified in P3 l.1172-1255 and l.1324-1358, with the “no real Hilbert-space sigma” warning at l.1457-1461.
- P3 vertex inverse limit / no edge Hilbert inverse limit: verified in P3 l.1053-1163.
- P2 octonions, `G_2`, stabilizer `SU(3)`, rational forms, icosian star: labels exist and the broad facts are present in P2 l.516-527, l.1717-1733, l.1791-1819, l.1867-1891.
- I could not verify in P2 the exact statement “the `G_2`-stabilizer fibre map has operator norm exactly 1” as a printed theorem. It follows classically, but P4 should not pretend P2 already printed that bound.
- F2 uniqueness claim exists in `cascade-foundations.md` l.143-163. P4 correctly does not use it as theorem-grade input.
- I could not find the exact quoted earlier theorem “all correspondences arising from closure dynamics are Borel/equivariant” as a current local theorem with that wording/number. Current `foundations.tex` does contain related broad correspondence machinery at l.1423-1467 and the false no-positivity discrete contraction claim at l.1231-1274. P4 should cite the concrete local target or remove the theorem-number language.

**4. Tightness**

- P4 l.130-134: replace “Every operator appearing in downstream constructions…” with “Every operator in the generator list below…”.
- P4 l.511-521: replace “kinetic / coboundary form” with “off-diagonal coboundary form”; add that it is not the positive kinetic square used in earlier foundations.
- P4 l.1363-1367: replace “energy monotonicity” with “one-step energy descent under the stated step-size condition”.
- P4 l.869-871: replace “equals the maximum over `[m_n,M_n]`” with “is bounded by the maximum over `[m_n,M_n]`”.
- P4 l.1241-1246: add one sentence proving norm-one action of `G_2` on `Im(O)`, or downgrade the citation.
- P4 l.1262-1264: fix “bounded linear linear map”.

**5. Surface Issues**

- Typo: “bounded linear linear map” at l.1263-1264.
- Line 442 should include `π(...)` in the displayed norm or explicitly say the projection has norm `≤1`.
- Line 1214 says “unitarity of the inner-product adjoint”; adjoints are not unitary. Say “the adjoint identity”.
- Line 518-521: the spectral-pair statement for `B_n` should say positive singular values; zero multiplicities need not pair cleanly.
- No unresolved local refs/cites found by static check. I did not compile because the workspace is read-only.

**6. Top Three Fixes**

1. Clarify the `E_n` redefinition conflict with earlier foundations: P4 l.511-521 versus foundations l.1131-1137. This is the most likely downstream citation trap.
2. Repair the source-audit/citation contract: P4 l.90-96, l.130-134, l.1325-1343 overstate what is locally verifiable about the old global theorem and P5-P13 operator coverage.
3. Expand the load-bearing proof details: adjoint proof l.356-370, coercive-contraction proof l.865-871, and `G_2` norm row l.1241-1246.

Core theorem convergence: yes. Publication-ready for programme drop: **no, not until the three fixes above are made.**
