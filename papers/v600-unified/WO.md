Read-only only. I did not edit or commit.

**SECTION A. Insight / External Content Relevance**

Already in the four V600 cascade papers:

- Paper 1 supplies the finite spine: K-multiset `{72:1, 0:1, 52:5, 20:5}` at `papers/bekenstein-incidence/bekenstein-incidence.tex:182-187`; `H=Dic_5` as the `K=72 ∪ K=0` bulk subgroup at `:193-204`; right-coset whole-cycle carriers at `:218-226`; `H` self-normalising/non-normal at `:257-260`; `V_24 = Fix(σ)` with 24 vertices at `:284-297`; incidence theorem at `:310-320`; τ-choice independence at `:348-356`.
- Paper 2 supplies only the exact σ-pair spectrum and finite first-law analogue: `E(v)=0` on `V_24`, `E(v)=5/2` on 96 mobile vertices at `papers/v600-hawking-quantum/v600-hawking-quantum.tex:189-200`, plus the per-coset identity at `:245-264`. It explicitly does not derive physical Hawking radiation or calibration at `:285-301` and `:310-328`.
- Paper 3 supplies `τ_σ`: right-coset construction at `papers/tau-sigma-construction/tau-sigma-construction.tex:139-156`, phase selection `{0,5}` at `:265-276`, canonical map at `:327-337`, theorem properties at `:356-369`, and the `Z_2^5` phase ambiguity at `:410-434`.
- Paper 4 supplies exact traces only as Layer 1, numerical comparison as Layer 2, and cosmological coupling as Layer 3 hypothesis: see `papers/v600-cosmic-tensions/v600-cosmic-tensions.tex:43-46`, trace theorem `:192-199`, admissibility `:215-224`, phase-independence `:268-276`, observational-only warning `:290-296`, coupling map hypothesis `Γ` at `:356-383`, and final caveat `:436-439`.
- Programme discipline already demands bounded scope: smallest undismissable claim at `papers/v600-programme/NARRATIVE.md:5`, no “one big paper” at `:56`, explicit scope sections at `:118-124`, strict dependency order at `:146-151`.

Only in `insight.md` or side notes, not Paper 5 foundation:

- `insight.md` contains E8/α/Standard-Model and conjugate-pair material at `insight.md:1-37`, `:47-78`, `:176-230`, `:363-407`. This is not part of Papers 1-4 and should not enter Paper 5 except as excluded future programme context.
- RH, god-prime, QMS-3, prime-locus, and pentagonal-holonomy content appears only in `insight.md:592-660`, `:664-715`, `:724-789`, `:830-890`. Direct relevance: quarantine it from this synthesis.
- CMB bulk-invariance has an internal route in `docs/closure-cosmogenesis.md`, but it is conditional: bulk invariance under accumulation assumes `ρ_t^B=0` at `:84-90`; coarse-graining has open `r,w` choices at `:106-120`; open items remain at `:164-168`. This cannot support “uniform T_CMB follows” inside Paper 5.
- The dipole/pre-registration scripts are working-hypothesis material: `preregister_k.py` admits the k-rule is fitted and underpredicts high-k existing data at `papers/cosmological-folding-rate/dynamics/preregister_k.py:19-27`; predictions are only listed for SPHEREx/LSST/SKA/DESI/Euclid/eROSITA at `:57-85`, not CMB-S4/Simons.

**SECTION B. Priority Gaps To Close The Task**

B1. Imported theorem registry  
Object: citation-only theorem table `I : {P1,P2,P3,P4} -> {T_1/4, T_Eq, T_tau, T_trace}`.  
Bridges: foundation papers to Paper 5 without re-proof.  
Route: strict import route.  
First step: write four imported theorem boxes with source theorem labels and no proof body.

B2. Structural spine lemma  
Object: finite-data tuple  
`Σ_V600 = (G=2I, T_tau, K-multiset, H=Dic_5, V_24, right cosets, τ_σ, A_K)`.  
Bridges: why all four papers use the same structure.  
Route: import from Papers 1, 3, 4.  
First step: table with columns “fact / source / used by Paper(s) / exact status”.

B3. Correct the `V_24` / bulk relation  
Object: incidence-distinction lemma.  
Correct statement: `Fix_σ(V600)=V_24`, `|V_24|=24`; `H=Dic_5=K72 ∪ K0`, `|H|=20`; `H∩V_24` has 4 vertices, not equality.  
Bridges: prevents Paper 5 from conflating σ-fixed vertices with K-special cycles.  
Route: direct Paper 1 import.  
First step: add warning note beside the structural spine table.

B4. Layer-3 cosmology firewall  
Object: imported hypothesis `Γ : {scale-rate, clustering-amplitude} -> A_K`.  
Bridges: exact trace ratios to H0/S8 interpretation.  
Route: Paper 4 hypothesis only.  
First step: every H0/S8 sentence in Paper 5 says “under Hypothesis Γ” unless it is only the exact trace identity.

B5. CMB bridge theorem, if pursued elsewhere  
Object: map `Θ : (F_t^B, π_C, calibration) -> T : S^2 -> R_+`.  
Bridges: bulk invariance to observed CMB temperature uniformity.  
Route: new derivation, not Paper 5 synthesis.  
First step: prove `ρ_t^B=0` for projection residuals and define the σ-invariant coarse-graining `π_C` with explicit weights.

B6. Dipole ladder audit  
Object: statistical audit map `D : survey catalogue -> nearest-rung residuals + look-elsewhere penalty`.  
Bridges: `1+k/2` ladder to evidence.  
Route: external empirical audit.  
First step: freeze survey inclusion, uncertainties, k-assignment rule, and null model before any Paper 5 claim.

B7. Prediction manifest integrity  
Object: timestamped manifest `R : observables -> formula, value, window, source commit`.  
Bridges: claims of pre-registration to falsifiability.  
Route: separate registry artifact, not synthesis theorem.  
First step: reconcile `preregister_k.py`, CSV, `UNIFIED_RESULT.md`, and SCOPE; remove CMB-S4/Simons unless a locked manifest exists.

**SECTION C. Reversals / Exact Replacements**

- At `papers/v600-unified/SCOPE.md:5` replace “modifications resolving the H_0 and σ_8 tensions” with “operator-trace ratios whose cosmological coupling is stated as a Layer-3 hypothesis”.
- At `papers/v600-unified/SCOPE.md:11` replace “It adds one new structural observation (CMB uniformity from bulk invariance) plus the synthesis itself.” with “It adds no new theorem-grade physical claim; it synthesises the four imported results and names future bridge builds.”
- At `papers/v600-unified/SCOPE.md:20` replace the whole CMB bullet with “Optional future-work note: a CMB bulk-projection bridge would require a map from σ-fixed bulk states to an observed temperature field, plus residual-support and coarse-graining theorems.”
- At `papers/v600-unified/SCOPE.md:22` replace “Reported as ancillary evidence.” with “Out of main scope; retain only as a separately audited empirical appendix if the statistical protocol is frozen.”
- At `papers/v600-unified/SCOPE.md:23` replace “Pre-registered predictions catalogue.” with “Pointer to an external timestamped prediction manifest, if reconciled; no new catalogue claims in the synthesis.”
- At `papers/v600-unified/SCOPE.md:40` replace “(1 ± 1/12) factors (cite Paper 4); empirical match.” with “exact operator-trace ratios (cite Paper 4); Layer-2 numerical comparison; Layer-3 coupling hypothesis.”
- At `papers/cosmological-folding-rate/dynamics/UNIFIED_RESULT.md:13` replace “6 left cosets: 1 bulk + 5 boundary (each = 1 K=52 + 1 K=20 cycle)” with “6 right cosets: 1 bulk plus 5 non-bulk right cosets, each carrying one whole K=52 cycle and one whole K=20 cycle; left cosets are not whole-cycle carriers.”

Global correction for any WO/draft text: replace `σ-fixed = V_24 = K=72 ∪ K=0` with `Fix_σ(V600)=V_24 is the 24-vertex fixed sublattice; H=Dic_5=K72∪K0 is the 20-vertex bulk subgroup; they intersect in 4 vertices per bulk coset`.

**SECTION D. Recommended Routes**

Route S, strict synthesis: recommended. Import four theorem blocks, one structural-spine table, one scope firewall, no CMB/dipole/prediction claims in the main theorem chain.

Route C, CMB bridge: separate future paper or appendix stub only. Needs `Θ`, `π_C`, residual support, and temperature calibration before “uniform T_CMB follows” is defensible.

Route E, empirical catalogue: separate registry artifact. Paper 5 may cite it as programme context only after internal inconsistencies are fixed.

**SECTION E. Attribution / Overclaim Audit**

- “Unified physical theory”: remove. Papers 1, 2, and 4 repeatedly state structural identity / analogy / hypothesis, not physical derivation.
- “CMB uniformity from bulk invariance”: remove from Paper 5 theorem path; current source has named open builds.
- “Cosmic dipole 1+k/2 ladder”: not load-bearing; current scripts are exploratory and fitted in part.
- “Pre-registered predictions catalogue”: only valid as external manifest; current SCOPE names CMB-S4/Simons without matching manifest lines.
- “Modifications resolving tensions”: replace with “trace ratios plus Layer-3 coupling hypothesis”; Paper 4 already enforces this.

**SECTION F. Top 3 Next Builds**

1. Build the Paper 5 import table at `papers/v600-unified/SCOPE.md:15-19`, backed by `NARRATIVE.md:146-151`. Content: four citation-only imported theorem statements, no proof sketches.

2. Build the structural-spine section at `papers/v600-unified/SCOPE.md:38`. Content: K-multiset, `Dic_5` self-normalising, right-coset carriers, corrected `V_24`/bulk distinction, `τ_σ` phase-independence.

3. Rewrite the scope firewall at `papers/v600-unified/SCOPE.md:5`, `:20`, `:22`, `:23`, `:40`, `:41`, `:51`. Content: math-scaffolding synthesis only; cosmological coupling remains Layer 3; CMB/dipole/predictions become named future builds or appendices, not new claims.
