No files edited. Here is the derivation audit.

**SECTION A. Insight / External Content Relevance**
Already in cascade papers:

- F1 only gives the positive fixed point `r = φ`; it explicitly does not assert any 600-cell, Coxeter, SM, or zeta content: `foundations.tex:116-135`, scope fence at `foundations.tex:204-223`.
- `σ(φ)=1-φ=-1/φ` is already repo-supported: `foundations.tex:555-560`, `cascade-12d-closure.tex:261-269`.
- `O_K = Z[φ]`, discriminant `5`, PID, and torsion-free module freeness are in `cascade-12d-closure.tex:284-358`.
- The icosian / `E8` / `H4` substrate is in `cascade-12d-closure.tex:366-390`; exact `2I` group closure and shell/class matching are implemented in `run_icosian_exact.py:6-23`, `216-318`.
- The `E8 -> H4` two-to-one root-layer statement is already separated from phase claims: `cascade-fine-structure.tex:589-628`. Phase halving is explicitly a named hypothesis there, not automatic: `cascade-fine-structure.tex:630-652`; center-gauge `π` separation likewise needs construction: `742-768`.
- Paper XXII currently treats `α^{-1}=137+π/87` as a numerical/structural correspondence, not a loop-integral derivation: `paper-xxii.tex:295-301`, `410-424`.

Only in `insight.md` / prior-session:

- The actual missing object is not a static `T(v)=τv`; it is a local-frame holonomy connection: `insight.md:846-851`, `867-872`.
- The proposed definition is a `Z[φ]^×`-valued edge cocycle plus clock chosen by local frame matching: `insight.md:878-882`.
- The periodic-orbit / weighted Artin-Mazur zeta idea appears only in prior-session content: `insight.md:855-861`, `887-890`.
- God-prime / QMS-3 / closure-locus constraints are prior-session only: `insight.md:670-715`; RH framing needs separate zeta and Mellin builds: `insight.md:728-741`, `771-775`.

External classical sources to cite for builds: Washington for cyclotomic fields, Neukirch/Marcus for quadratic fields and norms, Conway-Sloane / Elser-Sloane / Moody-Patera for icosians and `E8 -> H4`, Artin-Mazur and Ruelle for dynamical zetas.

**SECTION B. Priority Gaps To Close**
B1. `F1 -> O_K -> units` lemma.  
Object: `K=Q(√5)`, `O_K=Z[φ]`, `O_K^×={±φ^n}`. Bridges F1 to exact coefficient arithmetic. Source route: classical quadratic number theory. First step: cite/prove fundamental-unit claim, not just Dirichlet rank.

B2. Cyclotomic minimality lemma.  
Object: `n ↦ Q(ζ_n)`; theorem `Q(√5)⊂Q(ζ_n) iff 5|n`. Bridges `φ` to pentagonal order. Source route: Washington / conductor-discriminant. First step: replace the `n≤6` check with the conductor-5 statement.

B3. Norm-sign character.  
Object: `N_{K/Q}: O_K^× -> {±1}`, `u ↦ uσ(u)`. Bridges unit arithmetic to the sign obstruction. Source route: classical norm map / Hilbert 90. First step: rename draft `τ` to `χ_N` or `N_±` to avoid collision with quaternion `τ`.

B4. Unit sign to geometric chirality.  
Object: a theorem: if a `Z[φ]^×` connection has loop exponent `k(γ)`, then `σ`-monodromy is `(-1)^{k(γ)}`. Bridges algebraic norm sign to geometric obstruction. Source route: new derivation. First step: define the connection and loop exponent before claiming chirality.

B5. Pentagonal stabilizer in `2I`.  
Object: `G_10={g∈2I : g^10=1, g^5=-1}` and its conjugacy classes. Bridges pentagonal order to unit quaternions. Source route: Conway-Sloane / Du Val plus exact enumeration. First step: enumerate all order-10 elements in exact arithmetic and identify which are nearest-neighbour steps.

B6. Canonical clock choice.  
Object: compare `T_L(v)=τv`, `T_R(v)=vτ`, and `T_C(v)=τvτ^{-1}`. Bridges generator choice to a canonical self-map. Source route: new derivation + exact finite check. First step: prove the selected `τ` and left/right convention are forced by an oriented local frame, not by order alone.

B7. Local frame bundle.  
Object: `P -> V(600-cell)`, fibre = admissible oriented pentagonal axes / `C10` frames at each vertex. Bridges global `2I` symmetry to local transition data. Source route: new derivation from insight. First step: enumerate frames per vertex and the stabilizer action exactly.

B8. Holonomy cocycle `ω`.  
Object: `ω:E^{or}(G_600)->Z[φ]^×`, preferably encoded as `(sign,k)` for `±φ^k`. Bridges frames to weights. Source route: new derivation. First step: replace scalar-rescaling `φ^{-k}wv^{-1}`; that cannot define nonzero `k` for unit quaternions. Define `k(v,w)` from frame transition instead.

B9. Weighted finite dynamical zeta.  
Object: for cycles `C` of `T`,  
`ζ_{T,ω}(z)=∏_C(1-W_C z^{|C|})^{-1}` with `W_C=∏_{e∈C}ω(e)`. Bridges `T,ω` to exact coefficients in `Z[φ][[z]]`. Source route: Artin-Mazur / Ruelle. First step: prove product formula; sanity check unweighted `T` gives `(1-z^10)^(-12)`.

B10. `σ`-equivariance theorem.  
Object: relation among `σ`, `T_τ`, `T_{σ(τ)}`, and `ω`. Bridges weighted zeta to σ-fixed structure. Source route: exact computation + lemma. First step: compute `σ(τ)` exactly and prove whether `σTτ = Tσ(τ)σ` or an orientation-reversed variant.

B11. Mellin / critical-line bridge.  
Object: a map from finite weighted orbit data to a Dirichlet/Mellin object. Bridges formal σ-symmetry to `s ↔ 1-s`. Source route: analytic new derivation; foundations only gives a formal symmetry, not spectral concentration (`foundations.tex:2460-2477`, `2534-2577`). First step: define the transform and prove σ corresponds to inversion before any critical-line statement.

B12. Classical reduction audit.  
Object: comparison invariant against `ζ_K=ζ·L(χ_5)` and against tiling-hull / quasicrystal dynamics. Bridges “new vs classical” verdict. Source route: `observer_zeta_dedekind.py:1-19`, `121-220`; Bellissard/Kellendonk/Sadun literature. First step: test whether `ω` is cohomologous to constant or collapses to Dedekind coefficients.

B13. Exact verifier.  
Object: `derive_pentagonal_clock_exact.py` using `Fraction` / integer pairs for `Q(√5)`. Bridges all above to a computable zeta to degree 30. Source route: fork `run_icosian_exact.py` (`6-23`). First step: add order-10 enumeration, cycle decomposition, `ω` weights, product-form zeta coefficients.

**SECTION C. Reversals / Corrections**
- at `docs/pentagonal-torsion-derivation.md:15` replace `Every number below is computable; the accompanying Python script ... verifies each identity independently.` with `The exact verifier is Build B13; no such script is present yet.`
- at `docs/pentagonal-torsion-derivation.md:105` replace `Every other rotational symmetry ... factors through pentagonal symmetry (n ≥ 10).` with `A cyclotomic rotation field contains Q(√5) exactly when 5 divides n; nonmultiples of 5 do not factor through the pentagonal field by cyclotomy alone.`
- at `docs/pentagonal-torsion-derivation.md:133` replace `The map τ ... is the pentagonal torsion character` with `The map N_{K/Q}(u)=uσ(u) is the field norm restricted to units; its geometric pentagonal interpretation is Build B4.`
- at `docs/pentagonal-torsion-derivation.md:174` replace `with a distinguished cyclic subgroup` with `with cyclic subgroups; choosing a distinguished order-10 subgroup requires Build B5/B6.`
- at `docs/pentagonal-torsion-derivation.md:182` replace `around a pentagonal face of the 600-cell` with `around a pentagonal stabilizer/axis in the icosahedral adjacency; the 600-cell has triangular faces.`
- at `docs/pentagonal-torsion-derivation.md:199` replace `This -1 is precisely the pentagonal torsion character τ` with `This central -1 is the quaternionic target that must be identified with the norm-sign character by Build B5.`
- at `docs/pentagonal-torsion-derivation.md:233` replace the `φ^{-k(v,w)} · w · v^{-1} ∈ ...` definition with `k(v,w) is defined by the H4-equivariant local-frame transition of Build B7/B8; scalar rescaling of a unit quaternion cannot supply the general edge label.`
- at `docs/pentagonal-torsion-derivation.md:238` replace `ω is H4-equivariant and σ-covariant` proof paragraph with `Proof obligation: Build B8, including full-unit codomain ±φ^Z and gauge-independence.`
- at `docs/pentagonal-torsion-derivation.md:276` replace `under the standard Mellin pairing` with `after Build B11 defines and proves the required Mellin/Dirichlet pairing.`
- at `docs/pentagonal-torsion-derivation.md:309` replace `The derivation is complete from F1 to the clock` with `The derivation is complete through F1 -> Z[φ] -> σ; Builds B4-B13 close the clock, cocycle, and zeta construction.`

**SECTION D. Route Alternatives**
Route K: finite `2I` clock. Choose an exact order-10 `τ`, prove canonicity, compute the finite weighted zeta. Fastest path to a computable object.

Route Q: holonomy connection. Build the local-frame connection from `insight.md:878-890`. More cascade-native; harder because uniqueness/gauge must be proved.

Route D: Dedekind comparison. Compare resulting coefficients with `ζ_K=ζ·L(χ_5)`; useful as a classical-collapse test, not as the construction itself.

Route H: tiling-hull route. Lift from finite 600-cell graph to model-set hull / Bellissard-Kellendonk-Sadun style dynamics. Stronger distinction from finite rotations, but much larger analytic load.

**SECTION E. Exact Verification Targets**
- B1-B3: exact `Q(√5)` pair arithmetic; verify `σ(φ)=-1/φ`, `N(±φ^n)=(-1)^n`.
- B5: enumerate all `g∈2I`, orders, conjugacy classes, and nearest-neighbour order-10 generators.
- B6: compute left/right/conjugation cycle decompositions; expected left order-10 clock has `12` cycles of length `10`.
- B7-B8: enumerate frame transitions; verify `ω(e^{-1})=ω(e)^{-1}`, H4-equivariance, σ-covariance, and gauge-change invariance of cycle weights.
- B9: compute product-form coefficients to degree 30 in `Z[φ]`; unweighted sanity check `(1-z^10)^(-12)`.
- B10: exact σ-pairing of cycles and weights.
- B11-B12: compare coefficient invariants with Dedekind coefficients and detect constant/coboundary collapse.
- B13: refuse floats; reuse the `Fraction` representation from `run_icosian_exact.py:6-11`.

**SECTION F. Top 3 Next Builds**
1. B8 at `docs/pentagonal-torsion-derivation.md:226-243`: replace the invalid scalar-rescaling cocycle with a real local-frame holonomy connection. This is the central mathematical object.

2. B5/B6 at `docs/pentagonal-torsion-derivation.md:174-213`: pin down the order-10 pentagonal generator and left/right clock convention by exact enumeration plus a canonicity lemma.

3. B9/B13 at `docs/pentagonal-torsion-derivation.md:265-274` and `341-343`: implement the exact product-form weighted zeta using the existing exact icosian machinery from `run_icosian_exact.py:6-23`.

External sources used: Washington’s *Introduction to Cyclotomic Fields* (Springer), Artin-Mazur “On periodic points”, Ruelle on weighted dynamical zetas, Elser-Sloane’s `E8` quasicrystal construction.
