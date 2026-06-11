**1. Claim Audit**

- [cascade-closure-dynamics.tex:287](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:287>) Proposition “`X_n` is finite-dimensional”: established, conditional on P3’s finite-level Hilbert-space proposition.
- [cascade-closure-dynamics.tex:353](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:353>) Lemma “Coboundary-adjoint is the inner-product adjoint”: likely true, but the proof is too abbreviated for a load-bearing corrected point. It should explicitly use `(\pi_{F^0 -> F^1})^* = \iota_{F^1 -> F^0}` and track the oriented-edge `1/2`.
- [cascade-closure-dynamics.tex:417](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:417>) Proposition “Bounds on block operators”: essentially established. Line 451 is misstated: with oriented edges, a vertex appears as head or tail `2 deg(v)` times, not `deg(v)` times. The displayed `2 deg` bound is still compatible with the intended conclusion.
- [cascade-closure-dynamics.tex:532](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:532>) Theorem “Gradient operator”: established.
- [cascade-closure-dynamics.tex:598](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:598>) Theorem “Gradient flow exists and is unique”: established.
- [cascade-closure-dynamics.tex:639](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:639>) Corollary “matrix exponential is invertible”: established. Title is now mathematically honest.
- [cascade-closure-dynamics.tex:669](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:669>) Proposition “Energy dissipation identity”: established.
- [cascade-closure-dynamics.tex:715](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:715>) Corollary “Norm contractivity under positivity”: established.
- [cascade-closure-dynamics.tex:759](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:759>) Proposition “Euler step is energy-decreasing”: established.
- [cascade-closure-dynamics.tex:839](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:839>) Theorem “Strict contraction on coercive invariant subspaces”: over-claimed. The proof only gives `||G|| <= max(|1-eta m|, |1-eta M|)`. Equality and the claimed “optimal contraction rate” require `m_n` and `M_n` to be the actual spectral minimum and maximum, not merely any coercive bounds as in Definition 6.4.
- [cascade-closure-dynamics.tex:868](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:868>) Proposition “No global contraction without coercivity”: stated claim is established. The title is broader than the theorem: absence of coercivity is not the same as existence of a negative eigenvalue.
- [cascade-closure-dynamics.tex:922](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:922>) Proposition “Coboundary refinement-compatibility”: claim is true under P3’s edge-parent convention, but the written proof drops `\pi_{F^0 -> F^1}` throughout lines 939-960. As written, it compares `F^0` differences with an `F^1`-valued coboundary. Add the projection to both sides.
- [cascade-closure-dynamics.tex:980](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:980>) Proposition “Mass-block refinement compatibility”: established.
- [cascade-closure-dynamics.tex:1036](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:1036>) Theorem “`L_n` refinement-compatible in mass-only case”: established.
- [cascade-closure-dynamics.tex:1057](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:1057>) Theorem “Flow intertwining: mass-only case”: established by power series.
- [cascade-closure-dynamics.tex:1103](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:1103>) Corollary “Symmetries commuting with `L_n` commute with the flow”: established, conditional as stated.
- [cascade-closure-dynamics.tex:1178](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:1178>) Proposition “Generator bounds table”: mostly established. The `G_2` row needs one explicit sentence or citation that octonion automorphisms preserve the octonion norm, hence act orthogonally on `Im(O)`.
- [cascade-closure-dynamics.tex:1247](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:1247>) Theorem “Admissible intertwiners are bounded, continuous, Borel”: boundedness/continuity/Borel are established. The symmetry-intertwining clause needs more precise source/intermediate/codomain representations for inter-level compositions.

**2. Internal Consistency**

- All internal `\ref` / `\eqref` targets resolve.
- Label `prop:adjoint-refinement` at line 981 names a mass-block result, not an adjoint result. Rename to `prop:mass-refinement`.
- Theorem 6.5 uses `m_n, M_n` as if sharp spectral endpoints, while Definition 6.4 only says such constants exist. This is the main internal mismatch.
- Lines 1038-1054 are internally consistent but expose a conceptual limit: the only proved refinement-compatible flow is the mass-only case `L_n = -gamma C_n`, whose flow is `e^{gamma t C_n}` and generally grows in norm. The paper correctly avoids convergence claims, but the handoff should say this explicitly.

**3. External Consistency**

- P3 finite spaces, fibre definitions, dimensions, bonding maps, edge-parent map, adjoints, Coxeter unitarity, rational `sigma` scope, and absence of edge inverse-limit Hilbert space were verified locally in `papers/cascade-refinement-spaces/cascade-refinement-spaces.tex`.
- P3 supports `F^0`, `F^1`, `dim F^0 = 32`, `dim F^1 = 7` at lines 547-596; `X_n^0`, `X_n^1` at 603-636; dimension formula at 638-678; `p^0`, `p^1` at 687-722; bonding contractions at 726-778; adjoints and `p^1 j^1 = 1/2 id` at 813-878.
- P3 supports `sigma` not being a real Hilbert-space operator at lines 1324-1357 and 1457-1461.
- P2 supports `G_2`, stabilizer, and `SU(3)` identification at `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:1791` and `:1815`. It does not explicitly state the norm-one operator claim used in P4’s generator table; that is standard but should be cited or proved.
- The “false global theorem” characterization is consistent with `papers/cascade-correspondence-foundations/foundations.tex:1423`, where the abstract correspondence lemma asserts Borel/continuity/intertwining from broad hypotheses. P4 correctly does not rely on it.

**4. Tightness**

- Line 849: replace “The optimal contraction rate `||G||` is minimised” with “The displayed worst-case bound is minimised”.
- Line 868 title: replace “No global contraction without coercivity” with “Negative spectrum obstructs global contraction”.
- Line 1178 table: replace “Source” for `G_2` row with “P2 plus norm-preservation of octonion automorphisms”.
- Line 1377: “continuous-time semigroup flow” is fine, but add “no convergence target is implied.”

**5. Surface Issues**

- Line 451: “at most `deg` edges” should be “at most `2 deg` oriented incidences”.
- Lines 939-960: missing `\pi_{F^0 -> F^1}` in the coboundary-refinement proof.
- Line 1251: “operator on the finite-dimensional Hilbert space in its codomain” should be “operator between its finite-dimensional domain and codomain”.
- Line 981 label name is misleading.
- Line 325 antisymmetry computation also suppresses the projection; harmless but sloppy after the codomain repair.
- Line 63 uses `d_t F_n`; use `\frac{d}{dt}` in the abstract.

**6. Top Three Fixes**

1. Fix Theorem 6.5 at lines 839-852: either require `m_n = min spec(L_n|Y_n)` and `M_n = max spec(L_n|Y_n)`, or downgrade the equality/optimality statement to a bound.
2. Fix Proposition 7.1 proof at lines 939-960 by carrying `\pi_{F^0 -> F^1}` through the telescoping calculation.
3. Add an explicit no-convergence warning to the handoff around lines 1359-1388: the only proved refinement-compatible flow is mass-only and generally norm-expanding, so P4 supplies no attracting state or continuum convergence target.
