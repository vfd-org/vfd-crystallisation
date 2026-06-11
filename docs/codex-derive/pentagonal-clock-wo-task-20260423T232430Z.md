**SECTION A. Insight / External Content Relevance**

Already in cascade papers:

- F1 is only `r=1+1/r` and the golden-ratio consequences; later arithmetic is an added layer, not contained in F1 itself: `papers/cascade-correspondence-foundations/foundations.tex:116-173`, scope warning at `:204-224`.
- `K=Q(sqrt(5))`, `O_K=Z[phi]`, and `sigma(phi)=1-phi=-1/phi` are already in hardened cascade material: `papers/cascade-12d-closure/cascade-12d-closure.tex:261-298`.
- Icosaian / `2I` / 600-cell arithmetic is already present, but the stronger substrate paper uses the canonical unit-icosian definition, not a naive basis: `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:480-514`, `:964-994`.
- Exact 600-cell shell and central class-sum computations are already part of the paper-XXII/substrate layer: `papers/paper-xxii/paper-xxii.tex:171-222`, `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:1042-1110`.
- Existing zeta material is formal or conditional: sigma-symmetrized transfer operators and Mellin symmetry are not yet this finite weighted Artin-Mazur zeta: `papers/cascade-correspondence-foundations/foundations.tex:2369-2476`.
- Observer-zeta notes explicitly say the cascade-native zeta and `F-Irr` bridge are not yet constructed: `papers/cascade-derivation/cascade-observer-zeta.md:46-70`, `:291-321`, `:456-499`.

Only in `insight.md` or external literature:

- The directly relevant new idea is the pentagonal holonomy connection: local 600-cell frames, `Z[phi]^x` edge cocycle, clock map, and Artin-Mazur zeta are proposed but not in the repo: `insight.md:830-893`, especially `:846-861` and `:878-890`.
- God-prime / apex material is only prior-session conjectural context for later observer-zeta routing, not needed to make the finite 600-cell zeta computable: `insight.md:664-715`.
- External citations needed: Washington for cyclotomic subfield/conductor criterion; Neukirch/Marcus for quadratic integer ring and norms; Conway-Sloane/Moody-Patera/Du Val for icosians and binary icosahedral group; Artin-Mazur/Ruelle for weighted dynamical zeta.

**SECTION B. Priority Gaps To Close The Task**

B1. `F1 -> O_K` arithmetic lift.  
Object: lemma from F1 to `K=Q(sqrt(5))`, `O_K=Z[phi]`, `sigma`. Type: field/ring construction. Bridges F1 to arithmetic substrate. Route: classical Neukirch/Marcus plus existing `cascade-12d`. First step: state `N(a+b phi)=a^2+ab-b^2`, `sigma(a+b phi)=(a+b)-b phi`.

B2. Pentagonal cyclotomic minimality.  
Object: criterion `Q(sqrt(5)) subset Q(zeta_n) iff 5 | n`. Domain `n in N`; codomain boolean. Bridges `Z[phi]` to genuine pentagonal symmetry. Route: Washington, conductor of quadratic character `chi_5`. First step: replace finite `n<=6` check with conductor/discriminant proof.

B3. Unit norm parity character.  
Object: `N_{K/Q}: O_K^x -> {+-1}`, `N(phi^n)=(-1)^n`. Bridges Claude’s `tau(u)=u sigma(u)` to standard norm. Route: classical unit theorem. First step: rename unit character away from quaternionic `tau`.

B4. Chirality monodromy lift.  
Object: `Z[phi]^x`-valued graph connection `omega in Z^1(G,O_K^x)` and monodromy `M: H_1(G,Z)->O_K^x`. Bridges algebraic norm sign to loop chirality. Route: new derivation from insight holonomy. First step: prove `N(M(gamma))=(-1)^{k(gamma)}` for the connection actually used.

B5. Order-10 pentagonal lift in `2I`.  
Object: classification of preimages of order-5 cyclic subgroups under `2I -> A5`. Domain 5-fold axes; codomain cyclic `C10` subgroups. Bridges norm `-1` to quaternionic central `-1`. Route: Du Val / Conway-Sloane plus exact enumeration. First step: prove for chosen lift `q`, `q^5=-1`, `q^10=1`.

B6. 600-cell local frame bundle.  
Object: `Fr_5(V600) -> V600`, fibre = oriented 5-fold local frames / `C10` choices. Bridges arbitrary `tau` choice to canonical local data. Route: new derivation. First step: define frames via 5-fold axes of the icosahedral or dual-120-cell structure, not “pentagonal faces” of the 600-cell.

B7. Clock map `T`.  
Object: `T_tau: V600 -> V600`, likely `T_tau(v)=tau v` after frame choice, or `T` on `Fr_5`. Bridges pentagonal lift to finite dynamics. Route: Route Q or Route K below. First step: exact proof that selected order-10 `tau` lies in nearest-neighbour shell and gives `T^5=-id`, `T^10=id`.

B8. Cocycle repair.  
Object: edge/frame transition `k:E^or -> Z` or `Z/10`, weight `omega(e)=phi^{k(e)}`. Bridges local frames to weighted zeta. Route: new Cech/groupoid derivation. First step: define `g_vw=F_w F_v^{-1}` and project to the pentagonal exponent; do not use scalar equation `phi^{-k} w v^{-1} in 2I`.

B9. Sigma covariance.  
Object: `Sigma` action on vertices/frames/edges with `omega(Sigma e)=sigma(omega(e))` and `Sigma T Sigma^{-1}=T^{+-1}`. Bridges arithmetic conjugation to finite 600-cell dynamics. Route: icosian star/twin map, existing substrate `papers/cascade-algebraic-substrate/...:600-619`. First step: verify exact permutation or paired-copy action on all 120 vertices and frames.

B10. Weighted Artin-Mazur zeta.  
Object: finite weighted zeta  
`Z_{T,omega}(z)=exp(sum_n z^n/n sum_{x in Fix(T^n)} Omega_n(x))`.  
Bridges `T,omega` to computable series. Route: Artin-Mazur/Ruelle finite product proof. First step: prove primitive-orbit product `prod_gamma (1-Omega(gamma)z^{|gamma|})^{-1}` and compute in exact `Z[phi]` pairs.

B11. Sigma-fixed / Mellin / Dedekind comparison.  
Object: comparison map from finite weighted orbit data to Dirichlet/Euler coefficients, if claimed. Bridges finite zeta to `zeta_K=zeta L(chi_5)`. Route: classical Dedekind factorization plus new transform. First step: define the transform explicitly; otherwise keep this as a separate build, not a consequence of B10.

B12. Exact arithmetic verifier.  
Object: `derive_pentagonal_clock.py` exact harness. Bridges all mathematics to computable endpoint. Route: new implementation using existing exact icosian code, no floats. First step: assert 120 vertices, closure, order-10 lifts, frame transitions, cocycle identities, `T` orbit counts, and zeta coefficients.

**SECTION C. Reversals / Corrections**

- at `docs/pentagonal-torsion-derivation.md:15` replace “The exact arithmetic verification script is:” with “The exact arithmetic verification script is Build B12 and is not currently present at this path:”
- at `docs/pentagonal-torsion-derivation.md:37` replace “nothing below depends on anything beyond this equation.” with “every later use of `Z[phi]`, cyclotomy, `2I`, local frames, and zeta functions is an additional classical or build-specific layer over this equation.”
- at `docs/pentagonal-torsion-derivation.md:93` replace “`Q(sqrt(5))` is the unique quadratic subfield of `Q(zeta_5)`. For `n < 5`, no `Q(zeta_n)` contains `Q(sqrt(5))`.” with “`Q(sqrt(5)) subset Q(zeta_n)` iff `5 | n`; hence the minimal cyclotomic level is `n=5`.”
- at `docs/pentagonal-torsion-derivation.md:133` replace “The map `tau: Z[phi]^x -> {+-1}`” with “The norm map `N_{K/Q}: Z[phi]^x -> {+-1}`”
- at `docs/pentagonal-torsion-derivation.md:143` replace “Theorem 4.4 (pentagonal chirality theorem)” with “Theorem 4.4 (unit-norm parity theorem; chirality lift supplied by Builds B4-B5)”
- at `docs/pentagonal-torsion-derivation.md:184` replace “pentagonal face of the 600-cell” with “5-fold axis of the icosahedral / dual-120-cell structure associated to the 600-cell”
- at `docs/pentagonal-torsion-derivation.md:209` replace “Define `T: V -> V`, `T(v)=tau v`.” with “For a chosen local 5-fold frame and order-10 lift `tau`, define `T_tau(v)=tau v`; Builds B6-B7 prove when this is canonical and nearest-neighbour.”
- at `docs/pentagonal-torsion-derivation.md:233` replace “`phi^{-k} · w · v^{-1} in 2I`” with “`k(v,w)` is the exponent of the exact frame transition `g_vw=F_w F_v^{-1}` under the pentagonal character of Build B8”
- at `docs/pentagonal-torsion-derivation.md:265` replace “`in Z[phi][[z]]`” with “initially in `Frac(Z[phi])[[z]]`; Build B10 proves the primitive-orbit product and the `Z[phi]` coefficient condition”
- at `docs/pentagonal-torsion-derivation.md:309` replace “The derivation is complete from F1 to clock construction.” with “The derivation is complete after Builds B1-B12 supply the arithmetic, frame, cocycle, covariance, and exact zeta steps.”

**SECTION D. Route Alternatives**

Route Q: quaternion clock. Choose exact nearest-shell `tau in 2I`, set `T(v)=tau v`. Fastest computable route; risk is canonicity unless B6 supplies the frame choice.

Route K: holonomy connection. Build `Fr_5`, edge transitions, `omega`, and define `T` by canonical local holonomy / nearest transition. Best match to `insight.md:846-890`; highest derivation load.

Route C: conjugation clock `T(v)=tau v tau^{-1}`. Axis-intrinsic, but likely has fixed classes and weaker clock dynamics.

Route P: observer-prime route. Connect weighted orbit zeta to `F-Irr -> V600/H4`. This depends on observer-zeta gaps at `cascade-observer-zeta.md:456-499`; defer until B10 exists.

Attribution audit: `tau(u)=u sigma(u)` is the norm, not a new torsion character; 600-cell has tetrahedral cells, not pentagonal faces; cyclotomic minimality needs Washington’s conductor theorem; `T=L_tau` is finite group dynamics, not automatically a quasicrystal hull translation.

**SECTION E. Exact-Arithmetic Verification Targets**

- B1-B3: pair arithmetic for `Z[phi]`, sigma, norm, unit parity.
- B5: enumerate exact `2I`, count/order all order-10 elements, verify `q^5=-1`.
- B6-B8: enumerate frames, transitions, cocycle identity on cycle basis.
- B9: verify sigma covariance on every vertex/frame/edge.
- B10: compute primitive orbits and zeta coefficients by product formula to fixed degree, using `(a,b)` coefficients for `a+b phi`.
- B12: no `float`, no `numpy`; fail on approximate equality.

**SECTION F. Top 3 Next Builds**

1. B6+B8 at `docs/pentagonal-torsion-derivation.md:226-243`, backed by `insight.md:878-890`: define the canonical local frame bundle and repair the cocycle type.

2. B5+B7 at `docs/pentagonal-torsion-derivation.md:174-224`, backed by `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:964-994`: classify order-10 pentagonal lifts and prove the chosen clock is nearest-shell/canonical.

3. B10+B12 at `docs/pentagonal-torsion-derivation.md:256-286`: implement exact primitive-orbit weighted Artin-Mazur zeta, then only afterwards attach sigma-fixed or Mellin/Dedekind comparisons.
