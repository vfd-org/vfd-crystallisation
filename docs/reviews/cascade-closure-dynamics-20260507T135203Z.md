**1. Claim Audit**

- P4:278, “`X_n` is finite-dimensional.” Established, assuming P3 Prop. 4.4. The P3 result exists as `prop:Xn-Hilbert` at P3:638.
- P4:335, “`d_n^*` is the inner-product adjoint.” Under-proved. The formula omits the embedding `Im(O) -> F^0` into the `V_8` summand. As written, the RHS is not literally `F^0`-valued.
- P4:395, “Bounds on the block operators.” Mostly established. But `deg(G_n^\bullet)` must be defined as maximum labelled multigraph degree; the proof’s oriented-edge counting at P4:429 is imprecise.
- P4:504, “Gradient operator.” Established for the stated finite-dimensional quadratic form, provided the prior adjoint/fibre issue is fixed.
- P4:570, “Gradient flow exists and is unique.” Established.
- P4:611, “Flow is reversible.” Mathematically established as invertibility of a finite-dimensional linear flow. The wording is physically misleading but not false.
- P4:640, “Energy dissipation identity.” Established. Note that this is dissipation of an indefinite quadratic functional, not norm decay or bounded-below energy.
- P4:686, “Norm contractivity under positivity.” Established.
- P4:730, “Euler step is energy-decreasing for small eta.” Established.
- P4:810, “Strict contraction on coercive invariant subspaces.” Established under the stated spectral-gap hypothesis.
- P4:839, “No global contraction without coercivity.” Established.
- P4:896, “Coboundary refinement compatibility with factor `1/2`.” The computation is sound for P3’s class-(a) subdividing edges. It should cite P3 `def:edge-parent` as well as `def:p1`; P4 currently attributes the edge-parent map to Def. 5.2 at P4:903-907.
- P4:954, “Mass-block refinement compatibility.” Established.
- P4:1010 and P4:1031, mass-only refinement/flow intertwining. Algebraically established, but inconsistent with P4:495, where `alpha,beta,gamma > 0` are fixed “throughout the paper.” Under the paper’s own parameter convention, `alpha = beta = 0` is inadmissible.
- P4:1077, “Symmetries commuting with `L_n` commute with the flow.” Established, but only conditional. P4 does not prove `rho_n(g)L_n=L_n rho_n(g)`.
- P4:1145, “Generator bounds table.” Not established as stated. The P3 rows for `p`, `j`, and Coxeter actions are mostly recoverable, but the P2 fibre-map rows are wrong or under-specified. In particular, the `sigma` action is not a bounded real Hilbert-space operator.
- P4:1207, “Admissible intertwiners are bounded, continuous, Borel.” False as stated because its generator list includes rationality-side `sigma`/star material that P3 explicitly says does not extend to a real-linear Hilbert-space operator.

**2. Internal Consistency**

- Fatal parameter conflict: P4:495 fixes `alpha,beta,gamma > 0` “throughout the paper,” but P4:1012 and P4:1033 require `alpha = beta = 0`. Change the parameter convention to allow the mass-only specialization, or remove the mass-only theorems.
- P4:224 claims “commuting Coxeter/`sigma` actions” from P3. P3 only defines `sigma` on the mixed rational vertex form and explicitly says it does not extend to the real Hilbert space; see P3:1342-1357.
- P4:460-462 invokes P3 inverse-limit theorems in a way that suggests the full `X_n^0 \oplus X_n^1` dynamics is controlled level-by-level. P3 constructs only a vertex inverse limit and explicitly refuses an edge cylindrical limit at P3:962-976.
- P4:1099 calls the generator list finite, but P4:1112 includes `e^{-tL_n}` for every `t >= 0`. This is a parameterized family, not a finite generator.
- P4:1122 calls every syntactic expression an “intertwiner,” but no intertwining relation is built into the definition except conditionally at P4:1225-1230. Rename these “admissible finite-level operators.”
- All internal `\ref`/`\eqref` labels I checked are present. The surrounding text is still misleading at P4:247: “establishes refinement intertwining” should say “establishes mass-only refinement intertwining.”

**3. External Consistency**

- P3 finite spaces are verified: P4:268 and P4:283 correspond to P3 `def:Xn-0` at P3:604, `def:Xn-1` at P3:619, and `prop:Xn-Hilbert` at P3:638.
- P3 bonding maps are verified: `def:p0` P3:688, `def:p1` P3:704, `thm:bonding` P3:727. P4 should cite these labels explicitly.
- P3 adjoints are verified: `prop:adjoints` P3:814 gives `j^0=(p^0)^*`, `j^1=(p^1)^*`, and `p^1j^1=1/2 id`.
- P3 Coxeter unitarity is not correctly cited. P4:1171 cites P3 Def. 8.1, but unitarity is P3 `lem:coxeter-unitary` at P3:1228.
- P2 icosian star is partly verified: P2 `def:icosian-star` is at P2:516. But P4:1385 says it is “on `Lambda(E8)`”; P2 defines it on the icosian ring `I`, with the lattice relation mediated later.
- P2 stabilizer citation is wrong. P4:1195 and P4:1388 cite “Def. 7.4”; the relevant P2 material is in section 8: `def:G2` P2:1791, `def:stab-u` P2:1806, `fact:SU3-stab` P2:1815.
- P2/P3 do not verify P4’s bounded Hilbert-space `sigma` generator. P2 `thm:sigma-compat-P2` at P2:1895 is about `Q`-defined maps after scalar extension. P3:1342-1350 explicitly blocks the real-Hilbert interpretation.
- The O3 discharge in `cascade-refinement-compat` is only for the abstract scalar pure-midpoint model: see compat:37-72, compat:153-223, compat:526-602. The full P3/P4 lift remains open under `(L1)` and `(L3)` at compat:223-241 and compat:1062-1067. P4 is consistent only if it is not cited as a full P3/P4 O3 discharge.

**4. Tightness**

- P4:125-134, “Every operator appearing in downstream constructions...” Too strong. Edit: “The finite-level operators listed in Definition 8.1 are given explicit bounds.”
- P4:90-96, “finite-generator list.” False with `t >= 0`. Edit: “explicit generator families.”
- P4:247-249, “establishes refinement intertwining.” Edit: “establishes mass-only refinement intertwining and records the obstruction to claiming more.”
- P4:460-462, inverse-limit remark. Delete or replace with: “No inverse-limit boundedness statement for these operators is proved here.”
- P4:1190-1204, fibre maps. Replace with a narrower statement excluding `sigma` from real Hilbert-space bounded operators.

**5. Surface Issues**

- P4:326-328: specify that edge values are inserted into the `V_8`/`Im(O)` summand of `F^0`.
- P4:409, “uniformly on `X_n`” is meaningless. Say “bounded on each finite-level `X_n`.”
- P4:457-458, “introduces new vertices with higher degree” is not established and not needed.
- P4:955 label `prop:adjoint-refinement` is misleading; it is mass-block compatibility, not an adjoint result.
- P4:1172 should cite P3 unitarity lemma, not the action definition.
- P4:1195 and P4:1388 have the wrong P2 stabilizer citation.
- No obvious undefined LaTeX macros in P4 by text inspection; I did not compile.

**6. Top Three Fixes**

1. Fix the parameter convention: P4:495 conflicts with the mass-only theorems at P4:1012 and P4:1033. This currently makes the refinement-compatibility theorems formally outside the paper’s own hypotheses.
2. Remove or quarantine the `sigma`/star material from the Hilbert-space generator theorem: P4:1113-1116, P4:1190-1204, P4:1207. As stated, Theorem 8.3 is false.
3. Rewrite the P3/P2 citation contract using actual labels and correct scope: P4:883-907, P4:1155-1172, P4:1385-1407. In particular, do not imply P3 gives an edge inverse-limit Hilbert theory or a real Hilbert-space `sigma` action.
