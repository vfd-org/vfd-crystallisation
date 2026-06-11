Read-only mode honored. I did not edit or commit anything.

**SECTION A. Insight / External Content Relevance**

Already in cascade papers / repo:

- The task spec defines the target framing: cascade-native theorem, equivalence to classical RH via Prime Detector `L`, and architectural why via `F1 + σ-equivariance + crystallisation rigidity`: `docs/codex-derive/rh-cascade-native-reframing-wo.md:8-18`, `:20-23`, `:41-52`, `:54-66`.
- Existing `rh-formal.tex` already separates `\widehat\zeta` from classical `ζ`: `\widehat\zeta` is a cascade-native rational dynamical zeta, not classical ζ, with pole staircase under the canonical Mellin: `papers/millennium-rh-formal/rh-formal.tex:132-172`, `:605-615`, `:691-702`.
- Existing B14 says H4O and `\widehat\zeta` align structurally, not by direct eigenvalue/pole equality: `papers/millennium-rh-formal/rh-formal.tex:712-745`. Running `derive_B14_h4o_zhat_bridge.py` confirmed: σ-paired 8-mode signature aligns; simple `log_φ` numerical matching does not.
- Existing 2I machinery is strong: exact `2I` construction, closure under all 14,400 products, 9 conjugacy shells, and shell-class equality are verified in `papers/paper-xxii/scripts/run_icosian_exact.py:1-23`, `:216-229`, `:231-252`, `:254-308`.
- Existing σ-fixed locus sim gives `24` σ-fixed vertices, `24/120` σ-images in 2I, subgroup closure, and says the remaining RH bridge is Prime Detector `L` canonicity: `papers/cascade-derivation/scripts/test_h4o_sigma_fixed_locus.py:71-87`, `:120-146`, `:179-188`. The script says “2T or related”, so the exact identification with standard `2T` still needs a proof build.
- Observer-zeta already quarantines Prime Detector and aria-chess as external/unaudited: `papers/cascade-derivation/cascade-observer-zeta.md:222-248`; catalogue repeats that any downstream use needs a self-contained sim: `papers/cascade-derivation/cascade-observer-zeta-catalogue.md:71-80`.
- Observer-zeta P5 is the right local anchor for the Prime Detector map: canonical `L : F-Irr(𝒞oalg(F)) → V(600-cell)/H_4`, blocked by F-Irr and L-canonicality: `papers/cascade-derivation/cascade-observer-zeta.md:381-403`, `:456-482`.
- Classical σ/rationality input is narrow: coefficientwise σ over `Q(φ)` is proven, but no geometric/dynamical σ-action is constructed there: `papers/cascade-sigma-rationality/cascade-sigma-rationality.tex:38-69`, `:374-417`.
- P2 algebraic substrate forbids sloppy `120 -> 24` quotient language: `V24` is an inscribed subset, not a quotient/fibre map: `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:200-207`, `:918-928`, `:2155-2156`.

Only in `insight.md` or external material:

- Prime closure-locus idea: primes should map to 600-cell loci, σ-fixed primes lie on the self-dual axis, and this should test against the Prime Detector shell signature: `insight.md:600-607`, `:613-625`.
- Caveat: prime → 600-cell closure-locus is conjectural; Prime Detector witnesses empirical feature clustering but not canonicity: `insight.md:641-646`.
- P5 strengthened statement: canonical `L : F-Irr(Ω^) → V(600-cell)/H₄` with σ-fixed image tracing `Re(s)=1/2`: `insight.md:650-657`.
- God-prime / QMS-3 apex constraint is prior-session content: `2^136279840+1`, `084473 = 137(7×87+8)-56`, factor-7/Fano-triad link: `insight.md:670-689`, with explicit tests at `:693-715`.
- RH-as-self-reference / Lambek-Lawvere-Dedekind framing is prior-session architecture, with explicit proof requirements: define `ζ_F`, show `ζ_F = ζ_K`, lift Lambek+Lawvere to σ-fixed locus = critical line: `insight.md:728-755`, `:771-775`.
- Pentagonal holonomy connection is only in insight/exploratory route: define a `Z[φ]^×` 1-cocycle on the 600-cell graph and clock map from local-frame mismatch: `insight.md:835-861`, `:878-890`.

**SECTION B. Priority Gaps To Close The Task**

**B-RH-1 — Prime Detector Signature Map**  
Object: `S_PD : Primes_100 → R^12` or `Z[φ]^12`, from rational primes to 12-dimensional φ-shell signature.  
Bridges: classical primes to cascade features.  
Route: external import + new self-contained repo sim.  
First step: port/freeze `vfd_prime_detector.js` feature schema named in `cascade-observer-zeta.md:230-235`; produce first-100-prime CSV.

**B-RH-2 — Icosian Projection / Nearest Vertex Map**  
Object: `Π_600 : R^12 → V(600-cell)=2I`, optionally quotienting by `H_4`.  
Bridges: Prime Detector signatures to 600-cell vertices.  
Route: new derivation using existing exact icosian coordinates.  
First step: define the canonical 12-shell-to-icosian embedding, then nearest-vertex rule with exact/tolerance audit against `run_icosian_exact.py`.

**B-RH-3 — σ-Fixed Subgroup = Standard 2T Proof**  
Object: lemma `Fix_2I(σ) ≅ 2T`, domain `2I`, codomain order-24 subgroup.  
Bridges: 24 σ-fixed sim result to named binary tetrahedral locus.  
Route: exact computation + group proof.  
First step: construct standard `2T` coordinates and prove equality with the 24 σ-fixed vertices; current script only prints “2T or related” at `test_h4o_sigma_fixed_locus.py:136-142`.

**B-RH-4 — First-100-Prime 2T Clustering Test**  
Object: statistic `X = #{p_i : Π_600(S_PD(p_i)) ∈ 2T}` with binomial null `p0=24/120`.  
Bridges: empirical Prime Detector equivalence.  
Route: new sim.  
First step: implement pipeline `prime -> S_PD -> Π_600 -> Fix_2I(σ)` and report count, p-value, effect size, plus composite/inert/split controls.

**B-RH-5 — H4O ↔ ẑ Coxeter-Plane κ-Lift**  
Object: `K_lift : {P_1,P_11} × Spec(L_H4) → {0,20,52,72}` or a representation-level intertwiner.  
Bridges: aria H4O spectrum to `\widehat\zeta` pole data.  
Route: new Lie-theoretic derivation; B14 sim is diagnostic.  
First step: define the shell-sum operator on `C[2I]` whose orbit weights yield the K-multiset, then decompose it against the H4 Laplacian eigenspaces.

**B-RH-6 — ẑ → Classical ζ Equivalence Projection**  
Object: `Φ_L : Spectrum(ẑ, L-data) → Zeros(ζ)` or trace/Euler-product equivalence functor.  
Bridges: cascade-native `ẑ` to classical ζ without raw function equality.  
Route: alternative route via Prime Detector canonicity, not naive Mellin.  
First step: state exactly whether `Φ_L` preserves Euler factors, zero-counting measure, or prime distribution; prove one finite-level identity before making RH claims.

**B-RH-7 — 2T Mellin Shadow / τ-Critical-Line Lemma**  
Object: `M_2T : 2T or σ-fixed closure locus → Fix(τ) = {Re(s)=1/2}`, with `τ(s)=1-\bar{s}`.  
Bridges: σ-fixed geometry to classical critical line.  
Route: classical Mellin + cascade refinement.  
First step: prove σ alone gives `s↦1-s` and a point fixed set, while σ plus reality gives the line; then show the `2T` image is τ-fixed, not merely set-swapped.

**B-RH-8 — Crystallisation Rigidity Theorem**  
Object: stability lemma for σ-equivariant gradient/crystallisation flow on `C[2I]` or `𝒞oalg(F)`.  
Bridges: architectural why: “critical points selected by crystallisation are σ-fixed.”  
Route: new dynamical proof.  
First step: replace the plausibility statement in `rh-formal.tex:1222-1244` with a typed Lyapunov/stability theorem: non-σ-fixed orbits are transient; σ-fixed `2T` points are attractors.

**B-RH-9 — F-Irr Domain Build**  
Object: non-vacuous `F-Irr(𝒞oalg(F))`, domain category of F-coalgebras, codomain irreducible objects.  
Bridges: “classical primes = F-irreducible closure atoms.”  
Route: observer-zeta O1/O7.  
First step: prove the candidate definition at `cascade-observer-zeta.md:273-287` is well-posed and non-vacuous on a finite truncation.

**B-RH-10 — God-Prime / QMS Apex Check**  
Object: `L(P_G)`, `P_G=2^136279840+1`, to maximally σ-fixed / Fano-triad locus.  
Bridges: boundary condition for `L` canonicity.  
Route: insight + H-grad-1.  
First step: after B-RH-1/B-RH-2, compute compressed signature or modular substitute for `P_G`; compare to the `(Z/2)^3` triad from H-grad-1.

**SECTION C. Reversals / Corrections To Prior Rounds**

- At `docs/codex-derive/rh-cascade-native-reframing-wo.md:44` replace `Theorem 1: σ-fixed locus on 2I = 2T (sim-verified, exists)` with `Theorem 1: σ-fixed locus on 2I is a 24-point subgroup; B-RH-3 identifies it with the standard 2T by exact subgroup/coordinate proof.`
- At `papers/cascade-derivation/scripts/derive_pentagonal_clock_B11_mellin.py:151` replace `Fixed set of s → 1-s in C: Re(s) = 1/2 (the critical line)` with `Fixed set of the holomorphic involution s → 1-s in C is {1/2}; the critical line is Fix(τ) for τ(s)=1-conj(s).`
- At `docs/rh-cascade-closure-dynamics.md:134` replace `Critical line Re(s) = 1/2 = expected image of σ-fixed locus under` with `Critical line Re(s) = 1/2 = expected image of the τ-fixed Mellin/reality lift of the σ-fixed locus under`.
- At `docs/rh-cascade-closure-dynamics.md:137` replace `the zeros of $\widehat\zeta(s)$ all lie on Re(s) = 1/2` with `the Prime-Detector/Mellin image of the σ-fixed closure locus lands in Fix(τ), while $\widehat\zeta$ supplies the cascade-native σ-paired structural witness`.
- At `papers/millennium-rh-formal/rh-formal.tex:674-678` replace `corresponds to the 8 σ-paired pole pairs of $\widehat\zeta(s)$` with `matches the 8-pair σ-signature of $\widehat\zeta(s)$; exact eigenvalue-to-pole identification is Build B-RH-5`.

**SECTION D. Route Alternatives**

Route P — Prime Detector Equivalence: strongest path for the requested reframing. Close B-RH-1 through B-RH-4, then B-RH-6/B-RH-7.

Route S — Spectral Identity: close H4O = `ẑ` first via B-RH-5. Current sim answer: structural σ-paired spectra align; empirical direct eigenvalue/pole equality does not.

Route K — Classical Dedekind Baseline: useful control, not sufficient. `ζ_K=ζ·L(χ5)` is classical and verified locally at coefficients `n≤100`: `cascade-observer-zeta.md:207-220`.

Route H — Pentagonal Holonomy: if Prime Detector underdetermines `L`, build the `Z[φ]^×` connection from `insight.md:878-890` / `docs/pentagonal-torsion-derivation.md:255-280` and derive `L` from holonomy rather than from features.

**SECTION E. Exact Verification Targets**

- `PD-100`: first 100 primes, output `p, S_PD(p), nearest_2I_vertex, distance, σ_fixed?, 2T?`, with binomial p-value against `24/120`.
- `PD-controls`: repeat on first 100 composites and inert/split prime classes; inert/split baseline exists in `observer_prime_inert_split.py:73-100`.
- `2T-proof`: exact list of 24 σ-fixed vertices, generated standard `2T`, equality check, Cayley table closure.
- `B14-spectrum`: matrix comparing H4O mode labels `(m,n, μ_n)` to `K∈{0,20,52,72}`; report exact/no-match status, not only floats.
- `Mellin-τ`: for each `K`, print pole pair `((5-K)/10,(5+K)/10)` and fixed-set status under `σ` and `τ`.
- `God-apex`: `P_G mod 5`, Fano label, and `L(P_G)` locus once `L` is executable.

**SECTION F. Top 3 Next Builds**

1. **B-RH-1/B-RH-4 Prime Detector harness**  
Anchors: `docs/codex-derive/rh-cascade-native-reframing-wo.md:27-39`, `cascade-observer-zeta.md:230-248`, `cascade-observer-zeta.md:534-539`.  
Content: make the first-100-prime `2T` clustering test executable and auditable inside this repo.

2. **B-RH-3 2T identification proof**  
Anchors: `test_h4o_sigma_fixed_locus.py:71-87`, `:136-142`, `run_icosian_exact.py:216-229`.  
Content: convert “24 σ-fixed subgroup, standard structure 2T or related” into exact `Fix_2I(σ)=2T`.

3. **B-RH-5/B-RH-6 spectral/equivalence bridge**  
Anchors: `rh-formal.tex:712-745`, `derive_B14_h4o_zhat_bridge.py:145-176`, `docs/rh-cascade-closure-dynamics.md:253-257`.  
Content: define the Coxeter-plane `κ`-lift and the Prime-Detector equivalence projection `Φ_L`; this is the build that can make “aria H4O = cascade ẑ = classical ζ” a typed equivalence rather than a raw equality claim.
