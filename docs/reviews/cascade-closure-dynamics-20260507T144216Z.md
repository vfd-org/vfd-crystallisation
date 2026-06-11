**Verdict**

P4 is publication-ready for the vfd-org programme drop in its current narrow role. I find no remaining mathematical blocker. It proves finite-level linear-algebra dynamics and mass-only refinement compatibility; it still proves no non-degenerate refinement-compatible cascade flow and no convergence theorem.

**1. Claim Audit**

- “`$X_n$ is finite-dimensional`” and dimension counts, lines 292-300: established, by direct import from P3. No over-claim.
- “`d_n^*` is the inner-product adjoint,” lines 361-365: established. The factor `1/2` is consistent with P3’s oriented-edge inner product.
- “Bounds on the block operators,” lines 454-470: established. Constants are non-sharp but valid. The text correctly denies uniform-in-`n` boundedness.
- “Gradient operator,” lines 579-591: established. The proof gives the representing self-adjoint operator and the gradient formula.
- “Gradient flow exists and is unique,” lines 645-667, and “matrix exponential is invertible,” lines 686-691: established. No hidden positivity assumption is used.
- “Energy dissipation identity,” lines 716-728: established. This is energy monotonicity only; the paper correctly avoids claiming norm decay or convergence.
- “Norm contractivity under positivity,” lines 762-767: established.
- “Euler step is energy-decreasing for small `η`,” lines 806-825: established pointwise. It does not imply a uniform step size except under later coercivity assumptions.
- “Strict contraction on coercive invariant subspaces,” lines 886-901: established. “Negative spectrum obstructs global contraction,” lines 922-927: established.
- “Coboundary refinement compatibility, with factor `1/2`,” lines 976-988: established, assuming exactly P3’s parent-fibre averaging and inherited oriented-edge subdivision. That assumption is locally verified.
- “Mass-block refinement compatibility,” lines 1038-1050: established.
- “`L_n` is refinement-compatible in the mass-only case,” lines 1094-1105, and “flow intertwining: mass-only case,” lines 1115-1125: established. The mass-only restriction is explicit and not oversold.
- “Symmetries commuting with `L_n` commute with the flow,” lines 1161-1166: established, but only conditional. It does not prove that the constructed `L_n` commutes with any particular symmetry.
- “Generator bounds table,” lines 1236-1301: established. The `j^1` norm follows from P3’s half-section adjoint identity.
- “Admissible intertwiners are bounded, continuous, Borel,” lines 1313-1346: established for finite syntactic expressions. Equivariance is only conditional, as stated.

**2. Internal Consistency**

All local `\ref` and `\eqref` targets resolve. All `\cite` keys used in P4 have local bibliography entries.

The remaining terminology risk is “intertwiner.” Definition 8.2 makes it syntactic, but the word normally implies an actual equivariance relation. The theorem only proves equivariance under the extra hypothesis in lines 1337-1345. This is not a logical error, but it is a downstream citation hazard.

The word “kinetic” still appears for the indefinite off-diagonal form, lines 545-561 and 1499. The caveat is present and adequate; a hostile downstream reader can still quote “kinetic” carelessly.

No cross-reference points to the wrong theorem. The mass-only scope is now consistently repeated.

**3. External Consistency**

- P3 finite-level fibres/spaces/dimensions cited at lines 282, 297: verified in P3, especially `not:fibres`, `def:Xn-0`, `def:Xn-1`, and `prop:Xn-Hilbert`.
- P3 edge-parent map, `p^0`, `p^1`, bonding contractions cited at lines 966, 984-1011, 1247-1249: verified in P3. The two-preimage oriented-edge fact is present.
- P3 adjoints and `j^1` half-section cited at lines 1252-1261: verified in P3. The norm `2^{-1/2}` follows.
- P3 Coxeter unitarity cited at lines 1266-1267 and 1307: verified in P3.
- P3 sigma limitation cited at lines 1201-1206: verified. P3 defines sigma only on the mixed rational vertex form, not the real Hilbert space.
- P3 vertex inverse-limit / no edge inverse-limit cited at lines 527-529: verified.
- P2 `G_2` stabilizer material cited at lines 1287-1299: verified in P2. Orthogonality of octonion automorphisms is supplied by Schafer, not by P2, and P4 says so.
- The historical claim about a false global Borel/equivariance theorem, lines 90-96 and 117-123: I can verify related broad correspondence machinery in `papers/cascade-correspondence-foundations/foundations.tex`, but not the exact quoted theorem wording as a current local theorem. Since P4 no longer uses it theorem-grade, this is not a blocker; cite the local draft path or soften it further.
- The earlier false discrete contraction claim, lines 945-948: verified in `foundations.tex`, where the old argument claimed contraction under `0 < η <= ||L_n||^{-1}` without the needed positivity hypothesis.

**4. Tightness**

- Lines 1023-1035: “the factor `1/2` is structural” is slightly too strong. Better: “With the present normalization, the factor `1/2` is forced by the averaging map.”
- Lines 1211-1231 and 1313-1346: “intertwiner” is stronger than the theorem proves. Better: “admissible finite-level operator expression,” with equivariance reserved for item (4).
- Lines 221-231: P2/P3 responsibility is blurred. Better: “P2 supplies the algebraic sector objects; P3 fixes the finite-level Hilbert fibres and inner products.”
- Lines 545-561 and 1499: replace “kinetic” in the notation table with “off-diagonal coboundary” to prevent resurrection of the old positive-kinetic interpretation.

**5. Surface Issues**

- No undefined local references found.
- No missing bibliography keys found.
- Line 666: write `e^{-0L_n}=\id` or simply `e^{0}=\id`; current `e^{0\cdot L_n}` is harmless but inelegant.
- Line 468: “bounded in operator norm uniformly on `X_n`” is awkward. Say “bounded on each finite-level space `X_n`.”
- `D_n` is defined at line 286 but never used. Remove unless a downstream paper needs the notation.
- The long optional citations around lines 984-987 are ugly but valid LaTeX.

**6. Top Three Fixes**

1. Lines 90-96, 117-123, 1380-1383: either cite the exact local historical source for the false global Borel/equivariance theorem or recast it as programme motivation. Do not leave a hostile reader guessing which draft is being corrected.

2. Lines 1211-1231 and 1313-1346: rename “admissible intertwiner” or add a prominent sentence that equivariance is not part of the base definition. This prevents downstream papers from citing Theorem 8.3 as an unconditional equivariance theorem.

3. Lines 545-561 and 1499: remove the remaining bare “kinetic” shorthand from the notation table. The paper fixed the mathematics; the terminology should stop inviting the old misreading.
