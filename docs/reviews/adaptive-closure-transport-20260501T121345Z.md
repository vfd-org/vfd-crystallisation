Publication ready: no.

Must-fixes: fix the active-current inconsistency at lines 123/127/205; either prove or remove the claimed Łojasiewicz-Simon exponent at lines 66 and 284; correct the ARIA witness attribution at lines 521-526.

**1. Claim Audit**
- Fact, “Passive regime reduces…” line 173: established only as a specialization after choosing the transport-law current. The imported consequences at lines 175-177 are adequately caveated as conditional/hypothesis-level.
- Hypothesis, “Selection statement…” line 229: honestly labelled as a hypothesis. No theorem is being proved; acceptable.
- Theorem, “Closure-derived Lyapunov…” lines 240-260: convexity, coercivity, unique minimizer, and the Brezis subgradient-flow contraction are plausibly established. But the theorem does not state or prove the advertised “Łojasiewicz-Simon exponent θ=1/2” claimed in the abstract and status remark at lines 66 and 284. Add it to the theorem with proof, or delete the claim.
- Same theorem, line 259: “realisation of the abstract learning rule G(ρ,j,W)” is over-clean. The construction uses ψ* and ignores j; with arbitrary f, ψ* need not be a non-negative density ρ. State it as a scalar-field gradient-flow example, not a full ACT learning-rule realization without added hypotheses.
- Numerical witness, line 280 and Section 12: the JSON matches the table, but the script demonstrates one clipped explicit-Euler run. It does not numerically verify strict convexity, coercivity, the subgradient theorem, or the LS exponent.
- Fact, “Isotypic preservation…” line 294: verified against P2 §6. It is vertex-space only, as stated.
- Theorem, “Explicit 2I edge-space decomposition…” lines 301-312: proof establishes the undirected 720-edge action, freeness, six orbits, and the complexified regular-representation decomposition. “Explicit” means dimensions/orbits, not projectors or orbit representatives; tolerable, but do not oversell it.
- Hypothesis, “Cascade-selection…” lines 325-333: the equivariance conclusion follows from the stated assumptions. The no-blockwise-decoupling caveat is correct.
- Fact, “Definitional passive / active dichotomy” lines 350-357: established. The abstract shorthand “Active (dot W != 0)” at line 53 is pointwise sloppy; the body correctly classifies rules by G not identically zero.
- Hypothesis, “Long-time-behaviour conjecture…” lines 359-365: correctly scoped as conjectural.

**2. Internal Consistency**
- Major defect: line 123 defines j as antisymmetric on oriented edges, and line 127 makes that the learning-rule input convention. The active ansatz at line 205 is not antisymmetric unless μ=0 or ρ_v=ρ_w, because the drift term uses ρ_v rather than an antisymmetric edge density. Also, (∇W)_{vw} is undefined while W lives on undirected edges. This is publication-blocking.
- Theorem 4.1 uses ρ as a density elsewhere, but the worked fast variable ψ*=C^{-1}f may be sign-changing unless f and positivity-preserving assumptions are imposed.
- Line 459 says “R^{E_M} decomposes… into 9 isotypic components” using complex irrep dimensions. The theorem itself correctly says “after complexification”; the open-item summary should match.
- ARIA status is muddy: lines 381/400 say no repository-backed verification; line 457 says the dictionary is partially anchored. That is not fatal, but the distinction between “active-regime witness” and “ACT dictionary verified” must be explicit.
- Source parsing found no unresolved `\ref`/`\eqref` targets. Label `prop:classification` is attached to a Hypothesis; not broken, just sloppy.

**3. External Consistency**
- Transport-law paper: locally verified. It supports conditional U(1) conservation, Schrödinger-limit current closure, dispersion as hypothesis, and photon identification as conditional. Line 441’s “exactly the setting” is too strong for the whole passive regime; it is a specialization.
- P2: locally verified. It supplies V600=2I, shell-class centrality, vertex isotypic blocks, and the 94+26 split. It supplies no edge-space decomposition, W-dynamics, Lyapunov potential, or selection theorem.
- Paper XIX: locally verified. It gives a nonlinear residual and exact L2 conservation; it does not give a W-feedback law. Current manuscript states this correctly.
- Paper XXX: locally verified. Route C and Route E are conditional Born-rule arguments; no slow-manifold attractor identification is present. Current manuscript is cautious enough.
- Paper XXXIII: locally verified as a proposed closure-projection measurement template, not a closed theorem chain.
- Paper XXXIV: locally verified. The 88->87 Kostant step is a convention/hypothesis, not a theorem. Current manuscript is consistent.
- Alpha-chain note: locally verified. T_PH_2 is “needs polish”; T_MT_1 is not rigorously closed. Current manuscript’s cautious photon/microtubule language is justified.
- Meta-layer note: locally verified. It supports moduli/matching/tiling and T_meta ≅ Z[φ]^2, not identification with this paper’s W-space.
- ARIA chess paper: locally verified with caveat. It supports six drug/sleep signatures at seed 42 and an 18/18 tally only after documented N=20 P4 refinement; it does not say one seed-42 trajectory establishes all eighteen correspondences. Lines 521-526 must be corrected.
- B-anomaly paper: cited source is outside this repository. The primary claim at lines 491-511 cannot be verified locally from the cited paper.

**4. Tightness**
- Line 53: replace “Active (dot W != 0)” with “Active (G not identically zero; dot W nonzero on an open set).”
- Line 207: replace “This is the Nernst-Planck form…” with “This is a schematic Nernst-Planck-type ansatz; the graph gradient and antisymmetrisation remain to be specified.”
- Line 259: replace “realisation of the abstract learning rule” with “gradient-flow example compatible with the abstract learning-rule slot after identifying ρ with ψ* and suppressing j.”
- Lines 66/284: either add “for the unconstrained interior analytic strongly convex case” with proof, or remove “Łojasiewicz-Simon exponent θ=1/2.”
- Line 441: replace “exactly the setting” with “specialises to the setting.”
- Lines 521-526: say “ARIA reports six seed-42 EEG signatures and a 17/18 standard, 18/18 refined preregistered tally,” not that a single trajectory proves both.

**5. Surface Issues**
- Undefined `(∇W)_{vw}` at line 205.
- Plain `$2I$` at line 177 should be `$\twoI$`.
- Section title “Numerical verification (delivered)” line 547 is too strong. Use “Numerical witnesses.”
- “Published preprint” at lines 68/520 is awkward; use “released preprint” unless there is an actual publication venue.
- `V\textsubscript{600}` at line 283 is typographically unnecessary; use `$V_{600}$`.
- I did not compile because the sandbox is read-only; source-level reference parsing found no broken internal refs.

**6. Top Three Fixes**
1. Lines 123/127/205: repair the current convention. Either make active j genuinely antisymmetric and define `(∇W)_{vw}`, or explicitly allow non-conservative oriented fluxes and stop calling j antisymmetric globally.
2. Lines 66/284/547/550: remove theorem-verification overreach. The analytic theorem is mostly fine; the LS exponent and numerical “verification” language are not.
3. Lines 521-526: fix the ARIA attribution. Separate the seed-42 six-signature result from the 17/18 standard and 18/18 refined preregistered correspondence result, and state that neither verifies the ACT selection theorem.
