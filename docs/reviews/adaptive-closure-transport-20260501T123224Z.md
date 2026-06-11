Publication ready: no.

Must-fixes:
1. Line 527: the `18/18` ARIA upgrade is incompletely attributed. The local ARIA paper ties the final `18/18` result to the `N=20` P4 refinement plus the P13 state-reset/LOO protocol refinement, not P4 alone. Edit to: “`18/18` after documented P4 and P13 methodology refinements.”
2. Lines 159, 175, 79: the transport-law attribution is stale. The current local transport-law paper proves an explicit antisymmetric current and exact continuity/U(1) conservation in the Schrödinger-limit nearest-neighbour case; only the fuller dissipative setting remains programme-level. Distinguish those cases.
3. Lines 381 and 400 conflict with lines 457 and 520-533. The ARIA object-level dictionary is still unverified, but the active-regime substrate witness is now published locally. Say that precisely.

**Claim Audit**
- Line 172, “Passive regime reduces to the transport-law framework”: established as a definitional specialization. The external attribution in item one is outdated, as above.
- Lines 202-208, Nernst-Planck ansatz: fixed. The current is now oriented and antisymmetric with a vertex-valued `\Phi(W)`. No remaining mathematical objection; correctly scoped as ansatz, not derivation.
- Lines 228-229, selection statement: correctly labelled hypothesis, not theorem. Heavy analytic assumptions are explicit. No proof is claimed.
- Lines 240-262, Theorem `thm:lyapunov-closure`: proof establishes the stated convexity, coercivity, unique constrained minimizer, subgradient-flow convergence, gradient formula, and fast-subsystem hyperbolicity. Minor imprecision: “`C^\infty` on `\Omega`” at line 247 should say “restriction to `\Omega` of a `C^\infty` function on an open neighbourhood,” since `\Omega` has boundary.
- Line 253: tangent-cone wording is slightly wrong. Projection zeroes velocity components, not “components `\partial V_f/\partial W_e`.” Not publication-blocking, but fix it.
- Line 284: the Lyapunov-Simon/PL issue is fixed. Strong convexity gives `||∇V_f||^2 >= 2λ(V_f-V*)`, hence exponent `θ=1/2`, in the interior gradient-flow case.
- Lines 293-295, P2 isotypic preservation: verified locally in P2 §6. The paper correctly says this is vertex-space only.
- Lines 301-313, edge-space theorem: proof establishes the claim. Freeness of the edge action is valid; the `6 C[2I]` decomposition and listed isotypic dimensions follow.
- Lines 325-333, cascade-selection statement: correctly conditional. It proves only equivariance/orbit symmetry, and explicitly disclaims blockwise decoupling.
- Lines 350-357, passive/active dichotomy: established by definition.
- Lines 359-366, long-time-behaviour conjecture: correctly labelled hypothesis.
- Lines 555-612, numerical witnesses: numbers match the recorded JSON files. These are witnesses, not proofs; the theorem proofs do not depend on them.

**Internal Consistency**
- Line 92 says ARIA dictionary is “pending repository-backed verification”; lines 457 and 520-533 say the active-regime ARIA witness is now published. This is fixable by distinguishing dictionary-row verification from substrate-witness publication.
- Line 456 says strict convexity gives a single critical point, “automatically Morse.” For a constrained problem on a closed cone, that wording is too quick. Say: “in the interior unconstrained case it is nondegenerate/Morse; as a constrained minimizer it is unique.”
- Label `prop:classification` is attached to a Hypothesis at line 359. This will compile, but the label name is misleading.
- I found no obvious unresolved `\ref`/`\eqref` by static inspection. I did not compile because the workspace is read-only.

**External Consistency**
- Transport-law paper, lines 159/175/441: locally not accurately summarized. The current source proves the Schrödinger-limit current theorem; update scope.
- P2, lines 58/91/293/444: verified. P2 gives vertex `C[V_600] ≅ C[2I]`, shell-adjacency block preservation, and the `94+26` split; it does not give edge dynamics.
- Paper XIX, lines 211/442/458: verified. It gives scalar nonlinear residual and norm conservation, not a `W`-feedback law.
- Paper XXX, line 443: verified. Route C/E claims are conditional and not slow-manifold attractor claims.
- Paper XXXIII, line 100: verified. Measurement principle is proposal/candidate, not closed theorem.
- Paper XXXIV, line 445: verified. Kostant gauge is convention/hypothesis, not theorem-level pinning.
- Cascade alpha-chain, lines 177/433: verified in the conservative sense; microtubule `13` remains unclosed.
- Cascade meta-layer, line 446: verified. It gives moduli/matching/tiling structure and `T_meta ≅ Zphi^2`, not a `W`-space identification.
- ARIA chess, lines 520-533: separation of seed-42 six EEG signatures from the preregistered tally is fixed, but the `18/18` attribution omits the P13 refinement.
- B-anomaly, lines 489-512: cited source is outside this repository, so I could not verify it locally.

**Tightness**
- Line 53: “feedback along `∇W`-gradients” is not meaningful notation. Edit: “feedback through `W`-dependent potential gradients.”
- Line 81: “categorically different physical regime” is rhetorical. Edit: “a structurally different regime.”
- Line 237: “predicts the structural form of the answer” is too strong for a hypothesis stack. Edit: “would constrain the structural form of the answer.”
- Line 373: “non-living / living in biology” is broader than the math. Edit: “non-adaptive / adaptive biological transport models.”
- Line 557: “verify the two new theorems” overstates the scripts. Edit: “reproduce the numerical witnesses for the two new theorems.”

**Surface Issues**
- Line 50: `W` is called an “edge-conductivity tensor,” but it is defined as a scalar edge-weight vector. Use “edge-conductivity field” or “edge-weight vector.”
- Lines 247 and 284: avoid `C^\infty on \Omega`; use “smooth on an open neighbourhood, restricted to `\Omega`.”
- Line 253: fix tangent-cone projection wording.
- Line 527: add P13 refinement to the ARIA tally.
- No undefined macro stood out statically; `\twoI`, `\Zphi`, and `V_{600}` typography are now present/consistent.

**Top Three Fixes**
1. Correct the ARIA `18/18` attribution at lines 526-528 to include P13 as well as P4.
2. Update the transport-law attribution at lines 159 and 175 to reflect the current Schrödinger-limit theorem.
3. Resolve the ARIA dictionary/witness tension between lines 381/400 and 457/520-533.
