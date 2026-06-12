# Round 1 Codex Review — Programme-Wide Synthesis

Date: 2026-05-22.
Inputs: 10 of 10 codex reviews complete.
Verdict across all 10: **NOT publication-ready** on substantive math /
attribution scope.

The papers' individual implementations are solid. The problem is the
**programme has drifted out of internal consistency** since
consolidation, and each paper has overclaimed in ways that read fine
in isolation but contradict each other or their own demos. Almost all
fixes are mechanical.

---

## Tier 0 — Foundation math discipline (BLOCKER)

These items in the foundation paper (01) cascade through every downstream
paper. Fix the foundation first.

### 0.1 The τ-semantics problem (THE programme-blocking issue)

The foundation paper proves theorems on `dim Fix(τ) = 94` (icosian τ),
but the included demos use spectral τ and report `dim Fix(τ) = 116`.
The paper's own `results.json` flags `D3: match=false`. Worse, multiple
companion papers cite "94" as if it is the empirically witnessed number.

**Resolution required:**
- Two τ conventions, two names: `τ_ico` (icosian, dim 94, unconditional Theorem fix-tau-94 in the precursor) and `τ_spec` (spectral approximation, dim 116, used in the published sim demos).
- Every theorem about dim 94 cites `τ_ico` explicitly and notes the spectral demo gives 116.
- D8 in `closure_demo.py` already does this honestly; the paper text needs to catch up.
- Papers 01, 02, 03, 04, 07 all use 94 in claim statements; each needs the τ-convention disambiguation.

### 0.2 Pointwise fixed vs invariant subspace

The Algebraic Existence theorem at L254–L269 of paper 01 says
`X = C(X)` is the criterion for existence. The proof confuses subspace
invariance (`C` maps `X` into itself) with pointwise fixed-set
(`C(v) = v` for all v in X). For an invertible map like `C_φ`, the
maximal `C(X) = X` subspace is generally all of `H`, not `Fix(C)`.

**Resolution required:**
- Pick one criterion: subspace invariance OR pointwise fixedness.
- Subspace invariance is the right structural object (matches sim D7).
- Pointwise fixedness needs the dynamic `I − λC_φ` step, not `C_φ` itself.
- Cascade through Papers 02 (memory persistence theorem L289), 03 (closure-cost L425), 07 (CCR definition).

### 0.3 The Banach / self-similarity errors

- L324: `r → 1 + 1/r` is not a contraction with constant `φ^-2` on [1,2].
- L352: `C_φ` does not satisfy the self-similarity condition with `k=φ^-2`; its eigenvalues exceed 1.

**Resolution required:**
- Both claims need to be rewritten as conditional results under the dynamic update `I − λC_φ` with stated step-size assumptions, OR removed.

### 0.4 CP-rung-9.3 and CP-universal-5.1 status flips

- Paper 01 marks CP-universal-5.1 both OPEN (L371, L943) and CLOSED (L878, L892).
- CP-rung-9.3 is claimed CLOSED for polytope rungs but C1 demo reports E8=156, H4=116, D4=22 (not the 120/94/24 the theorem expects).

**Resolution required:**
- Pick a single status for each per current evidence.
- Tighten CP-rung-9.3 to "spectral upper bound matches H4 rung within the substrate construction; pointwise verification is the icosian τ residual gap."

---

## Tier 1 — Programme-wide systemic fixes

These apply to all 10 papers. Each is roughly mechanical (find/replace
+ section addition).

### 1.1 Replace four-paper programme map with ten-paper map

Paper 01 §L1137–L1182 still describes a four-paper programme. The actual
programme is ten papers (4 structural + 6 empirical). Update:

- Paper 01 programme map → 10 papers
- Paper 02 cross-references → match 10-paper structure
- Paper 03 SL anchors → cite current SL-002 / SL-005 / SL-006 / SL-007 status
- README/REFINEMENT_STATUS → already 10-paper, but sync paper-1 to it

### 1.2 Refresh stale SL-005 / 006 / 007 references

Paper 01, Paper 02 cite SL-005/006/007 as "scaffolded" with
"preregistered hypotheses awaiting data." The current state is:

- SL-005 (08): ds007609 trait anxiety `d=+0.79`, plus ds004315 mood
- SL-006 (09): FlowIndex-v1, ds005520 MOBA-gaming and table-tennis both **diagnostic-predicted FAIL, observed FAIL**
- SL-007 (10): ds007471 musical hyperscanning honest negative; ds006802 collaborative-rule-learning moderate-positive trend

**Resolution required:**
- Every cite of SL-005/006/007 in 01, 02, 03 updated to current state.
- Honest negatives framed as methodology-validation successes (diagnostic predicted FAIL, observed FAIL is the wanted shape).
- ds006802 trend appendix in Paper 10; decision in Paper 07 whether to add it to the 14/15 ledger or label exploratory.

### 1.3 Add shared "claim status" classification

Every claim throughout the 10 papers should be classifiable as
exactly one of:

| Class | Examples | Markup |
|---|---|---|
| **Theorem** | Spectral lower bound for `C_φ`; existence of `Σ_𝓘` | `\begin{theorem}` |
| **Conditional Proposition** | Flow time-dilation (requires H-RP-1/2 + P-A) | `\begin{conditionalproposition}` |
| **Definition** | Living frame data tuple; R_cl 5-term decomposition | `\begin{definition}` |
| **First-order empirical proxy** | `R_phase`, `R_cl`, `FlowIndex`, `δ_AB^EEG` | `\textbf{Empirical proxy.}` |
| **Empirical anchor** | SL-002 ds005620 `14/14`, SL-005 `d=0.79` | `\textbf{Anchor:}` with cite |
| **Simulation demonstration** | D1–D8, L1–L13, C1–C5, B1–B3 | `\textbf{Sim demo:}` |
| **P-A-conditional interpretation** | Dyscoherence-as-suffering, qualia | Tagged `[P-A]` |
| **CAD-conditional empirical claim** | Real-data PASS/FAIL predictions | Tagged `[CAD-D1–D5-v1]` |

Many existing "Theorems" should be downgraded. Codex specifically flagged:
- Paper 02: boundary `L194-206`, memory `L289-293`, thought `L588-592`, flow `L843-845`, creativity `L874-878`, trust `L938-942`, self-deception `L973-975`
- Paper 03: sleep `L435`, anaesthesia `L449`, frame-time `L150`
- Paper 05: "basin/attractor" language throughout

### 1.4 Over-claim language sweep

Replace throughout (programme-wide):

| Bad | Good |
|---|---|
| "validated" | "operationalised and simulation-tested" |
| "proven" | "established under hypotheses X, Y" |
| "rules out volume conduction" | "argues against scalp volume conduction as sole explanation" |
| "instantiates the operator" | "provides operational support for" |
| "real-physics trajectories" | "biophysically parameterized BETSE trajectories" |
| "canonical flow paradigm" | "a plausible high-engagement motor paradigm" |
| "matched effect size" | "comparable in-sample statistic; CAD LOSO estimate is `X`" |
| "decisive evidence" | "strong robustness evidence" |
| "category mistake" | "type mismatch in this framework" |
| "exactly when" / "iff" | "in the present validation set, is best predicted by" |
| "transfers universally" | "has transferred in tested cases" |

### 1.5 LaTeX hygiene (bib + paths)

Six papers have `\bibliography{refs}` but the file is `references.bib`:
05, 06, 07, 08, 09, 10 (and possibly 01/02/03/04). Audit and fix.

- Bib key drift: `SmartLifeClosure` (used in 07, 08) vs `SmartLifeAsClosure` (used in 01, 02, 03)
- Missing `SolutionLab007` key in paper 09
- Path drift: `papers/existence-as-recursive-closure/` vs `papers/01-existence-as-closure/` (foundation 01, processing 03, life 02)

### 1.6 Cross-paper attribution audit

Confirmed errors:
- Paper 08 cites Life §13.3 for trauma; §13.3 is *flow*; trauma is §13.2
- Paper 07 cites `SmartExistenceClosure` (L222) where `SmartLifeClosure` is intended
- Paper 02 joint-meaning recap (L695–699) cites a loose inequality; Paper 01 has the exact equality (L626–627)
- Paper 03 imports ARIA `17/18 / 18/18` as theorem-grade; should be `\textbf{Reported in \citet{...}}`

### 1.7 Volume-conduction over-claim (SL-002 cascade)

Paper 06 says "rules out volume conduction" (L33, 97, 227, 254, 258, 370).
Paper 03 inherits this. SL-002's own limitations mention template anatomy
and ad-hoc identity noise covariance — source leakage and smoothing
remain. Soften across 03 and 06.

### 1.8 Replication discipline

Paper 06 says "two cohorts (pilot n=8 + held-out n=6)" without
separately reporting pilot/held-out statistics. Paper 06 also calls
ds004541 a "matched effect size replication" — but Paper 07's LOSO
re-analysis at n=7 gives `d_z=1.16`, not the `1.98` in-sample number.

**Resolution:**
- Separate in-sample, source-space, LOSO, and independent-cohort numbers in every paper that cites SL-002.
- "Replication" reserved for true cross-cohort; reanalyses and source-space refinement labelled as such.

### 1.9 CAD as formal scope gate

Paper 07 says the diagnostic is part of the method, not optional
(L44). Papers 03 and 02 cite CAD but treat it as a downstream remark.

**Resolution:**
- Every empirical bridge in 02, 03 gets a tagged `[CAD-D1–D5-v1]` scope statement.
- Paper 07 becomes the canonical versioned ledger (timestamps, prediction registry, current strict-CAD vs PASS-leaning status).

### 1.10 Effect-size vs statistical-significance separation

Multiple papers conflate `d > threshold` and `p < 0.05`. Programme-wide
rule: every empirical PASS/FAIL claim states both
**effect-size status** AND **significance status** explicitly.

Specific cases:
- Paper 08 `d=+0.79, p=0.07` — effect-size PASS, significance borderline
- Paper 09 H2 `d=2.83` but H2 was preregistered as Spearman ρ
- Paper 10 H3 `d_z=1.25` reported as "still met" when threshold is 1.5

---

## Tier 2 — CAD methodology fixes (Paper 07-driven)

The methodology paper itself (07) has 4 critical contradictions that
flow downstream. Fix 07 first, then cascade.

### 2.1 The "iff" contradiction

Paper 07 says CAD failure ⟺ closure can't beat single-axis (L33, 40,
49, 237, 366). RNN rows show CAD-FAIL substrates where closure beats
baseline (single-objective RNN `d_z=3.40` vs `0.64`; multi-objective
`3.99` vs `0.41`).

**Resolution:**
- Drop "iff" / "exactly when" / "universal" language.
- Replace with: "in the present validation set, is best predicted by."
- Acknowledge RNN as a substrate where the diagnostic underpredicts.

### 2.2 All-five gate vs PASS-leaning

L75 says substrate passes IFF all five criteria. Trait anxiety has
`D2=0, D3=0.64` (both fail strict thresholds), but is classified PASS
at L200, L207. The "14/15" classification ledger includes
"PASS-leaning" cases as PASS.

**Resolution:**
- Maintain separate columns: strict CAD-v1 PASS, PASS-leaning, FAIL.
- 14/15 ledger uses strict PASS only; PASS-leaning cases listed separately as a v1.5 boundary set.

### 2.3 Numerical inconsistencies in headline numbers

- L124 source LOSO: `d_z=2.07, t=7.00, p=3.1e-6, n=14` — these can't all hold (`t` from `d_z` and `n=14` is ≈ 7.74).
- L129 sensor LOSO: `d_z=1.43, t=6.83, p=1.3e-4` — `d_z=1.43, n=14` gives `t≈5.35`, not `6.83`.
- L174 says "8 + 3 = 11" but table has 9 paired + 3 controls.

**Resolution:**
- Recompute all headline numerical triples.
- Audit table row counts.

### 2.4 Mood case ledger

`ds004315` mood manipulation enters Paper 07 at L316 without being in
the 14/15 classification ledger. Paper 08 reports it as a diagnostic
false negative (08:L124-130, 195). Paper 07 says false negatives = 0
(L215).

**Resolution:**
- Decide whether mood is in or out of the ledger.
- Sync 07 + 08.

---

## Tier 3 — Per-paper specific fixes

### Paper 01 (Existence as Closure) — foundation
- **Top fix**: resolve τ-semantics + pointwise/invariant distinction; this unblocks everything else
- 4-paper → 10-paper programme map (§L1137-1182)
- Drop or weaken: L324 Banach, L352 self-similarity, L495–515 rung claim
- Fix repro paths (`papers/01-existence-as-closure/`)
- Resolve CP-universal-5.1 status (open vs closed flip)
- Add 10-paper status matrix near end

### Paper 02 (Life as Closure) — flagship
- **Top fix**: theorem→Conditional Proposition for boundary, memory, thought, flow, creativity, trust, self-deception
- 18 objects count instability: text says 10 demos, table says 13, glossary has 23 rows — pick one and propagate
- dim Σ ≤ 94 vs demo 116 — apply τ-disambiguation
- Update SL-005/006/007 status to current
- Bibliography: `references.bib:64` has stray `}`
- Path: `02-life-as-closure/repro/` not `life-as-closure/repro/`

### Paper 03 (Processing) — neuroscience bridge
- **Top fix**: recast `R_cl` and `R_phase` as operational proxies (not "validations")
- Distinguish `C` from `I-λC` for all closure-cost claims
- "≥ 35 subjects" → "21 unique subjects with source-space + LOSO reanalyses"
- Add CAD as formal scope gate for every empirical bridge
- ARIA theorem styling → import-cite

### Paper 04 (Cosmic) — held back
- Review completed. Held back from v1.0 regardless; but the structural problems are substantial.
- **Top fix**: theorem stack contains at least one *false* theorem:
  - Non-periodic recurrence theorem (L353–365) is FALSE as stated. Time-varying operators can still have periodic states. Banach doesn't apply on the fixed subspace (every vector in C is fixed if C∘P is identity on C).
  - Destruction theorem (L154–165) overclaims; symmetry breakdown makes Fix(τ) undefined, not necessarily zero-dimensional.
  - Closure-cascade cosmology (L369–377) depends on the false non-periodicity theorem.
  - Rung universality (L442–456) overclaims; Paper 01 says abstract rungs are rank-bound/open.
  - Hierarchical time (L464–470) only proves "if μ differs, ticks differ"; doesn't prove monotonicity.
  - Universe-as-frame conditional (L503–514) needs a generalized frame definition; Paper 01's BRF is O⊆V_600.
- Same `references.bib:64` stray `}` issue as Paper 02.
- C3 demo implements `P_Σ`, not `P_{Fix(τ)} ∘ P_{Fix(C_φ)}` as paper defines (L330–334).
- "H-evolve motivates non-periodic" should NOT be presented as "non-periodicity is shown."
- Wrong inequality direction at L126/L141: `||C^-1 b|| ≤ λ_min^-1 ||b||`, not ≥.
- "The answer is yes" / "closure geometry does not care" / "not metaphorical but precise" / "end of reality" / "Valid at every scale" — all overclaims for a held-back speculative paper.
- Apply Tier 1 fixes when activated; also rebuild the theorem stack.

### Paper 05 (SL-001 Bioelectric)
- **Top fix**: narrow "basin/attractor" language; reconcile with Paper 07's "BETSE 2-sec fails CAD"
- 4 vs 6 conditions, 19 vs 29 LOO replicates — internal consistency
- Title "in-vivo regeneration" but paper has no in-vivo data → "for in-vivo regeneration"
- "real-physics trajectories" → "biophysically parameterized BETSE trajectories"
- Add programme positioning box: SL-001 is operational BETSE/wet-lab instantiation of Paper 03's Levin bridge, not full-framework proof
- Bibliography reference path

### Paper 06 (SL-002 Cortical) — most-cited empirical paper
- **Top fix**: soften "rules out volume conduction" → "argues against scalp volume conduction as sole explanation"
- Separate in-sample / source / LOSO / independent-cohort statistics
- Pooled-vs-subject-centroid standardisation: pick one canonical convention; sync with Paper 08
- Beta band: 15–30 Hz here vs 13–30 Hz in Paper 08 — pick one and propagate
- Cross-band PLV non-integer ratios definition issue (L201, 218 internal contradictions)
- Frequency-band canonical statement

### Paper 07 (Closure-as-Distance) — methodology
- **Top fix**: drop "iff" language; reconcile RNN dominance with core claim
- Strict CAD-v1 vs PASS-leaning ledger separation
- Recompute headline numerical triples (L124, L129)
- Mood ledger decision
- Soften BETSE dismissal (matches Paper 05 narrow claim)
- Cite Life via correct key
- Companion-paper concordance table

### Paper 08 (SL-005 Trauma) — first-result
- **Top fix**: title overclaims "trauma"; anchor is trait anxiety. Retitle.
- Add real Methods section: preprocessing, channel list, exclusions, durations, artifact handling, standardisation, quartile rule, prereg timestamp, diagnostic computation, Hotelling implementation
- H2 reported as `d_z` but preregistered as Spearman ρ
- Beta band: align with Paper 06 (13 vs 15 Hz)
- Frequency-band synthetic `d=+41.38` implausibly large
- Mood `ds004315` between- vs within-subject contradiction
- Fix Life §13.3 (flow) attribution → §13.2 (trauma)
- Bib key `SmartLifeClosure` → `SmartLifeAsClosure`

### Paper 09 (SL-006 Flow)
- **Top fix**: MOBA "in-progress" vs "completed" contradiction (L132 vs L140)
- H2 (Spearman ρ vs d), H5 (multiplicative-necessity vs default-weight robustness) — fix to match preregistered
- FlowIndex formula differs between abstract and methods
- Add missing `SolutionLab007` bib key
- Demote "5/5 PASS" to "synthetic implementation behaves as designed; not validation of structural claim"
- Reframe as honest-negative methodology-boundary paper

### Paper 10 (SL-007 Hyperscanning)
- **Top fix**: one-vs-two real-data substrates contradiction (33 vs 113 vs 166)
- Separate formal δ_AB from empirical proxy `\widehat{δ}_{AB}^{EEG}`
- H3 fail at `d_z=1.25` reported as "still met" — incorrect
- ds006802 decision: official evidence or exploratory appendix
- Trial counts: 13×40=520 vs 13×80=1040 vs 13×69=897 — pick the right arithmetic
- Music-ensemble scope correction: this contrast is wrong substrate, not music as a whole

---

## Priority order for refinement

### Phase A — Foundation rebuild (BLOCKER, ~6-10h)

1. **A1**: Resolve τ-semantics globally (Paper 01 §§4–7 + propagate to 02/03/04/07)
2. **A2**: Pointwise/invariant distinction (Paper 01 theorems + cascade)
3. **A3**: Update 4-paper → 10-paper map (Paper 01 §§1, 17)
4. **A4**: Status updates for SL-005/006/007 references everywhere
5. **A5**: Bibliography hygiene sweep (all 10 papers — bib key, file path)

### Phase B — Methodology paper repair (~4-6h)

6. **B1**: Paper 07 "iff" → "best predicted by" + reconcile RNN
7. **B2**: Strict CAD vs PASS-leaning ledger separation
8. **B3**: Recompute headline numerical triples
9. **B4**: Mood ledger decision (07 + 08)

### Phase C — Flagship + Processing tightening (~6-8h)

10. **C1**: Paper 02 theorem→Conditional Proposition demotions
11. **C2**: Paper 02 demo count + dim consistency
12. **C3**: Paper 03 proxy framing + CAD scope gate
13. **C4**: Paper 03 subject-count correction

### Phase D — Empirical wing polish (~10-15h)

14. **D1**: Paper 05 narrow basin language + programme positioning
15. **D2**: Paper 06 volume-conduction softening + replication-discipline separation + frequency-band canonical
16. **D3**: Paper 08 retitle + add Methods section
17. **D4**: Paper 09 MOBA contradiction resolution + reframe
18. **D5**: Paper 10 formal/empirical δ_AB separation + scope correction

### Phase E — Programme-wide style (~3-5h)

19. **E1**: Over-claim language sweep
20. **E2**: Claim status classification applied
21. **E3**: Effect-size vs significance separation
22. **E4**: Volume-conduction softening downstream
23. **E5**: Cosmic (04) review-driven fixes when reviewed

### Phase F — Round 2 codex re-review

24. **F1**: Re-run codex on all 10 with focus on Phase A–E fixes
25. **F2**: Iterate until codex returns "publication ready: yes" per paper

**Total estimate: 30–45 hours of focused refinement to reach
"publication ready: yes" verdict across the 10 papers.**

---

## Key strategic decision points

These are the high-leverage decisions the user needs to make. They
shape the rest of the refinement:

### D1: τ semantics

Three options:
- **(a)** Make icosian τ the only τ. Theorems use dim 94. Demos updated to compute icosian τ (significant code work, ~10 hours).
- **(b)** Make spectral τ the canonical τ. Theorems updated to dim 116. The Theorem fix-tau-94 of the precursor becomes a separate "icosian witness" result not used by 01.
- **(c)** Two named τ's throughout, each used where appropriate. Most flexible but requires careful per-claim audit.

Recommend (c) for honesty; it's what D8 already does. Estimated impact: ~3-4h to propagate naming.

### D2: Subspace invariance vs pointwise fixedness

The cleanest fix is to make subspace invariance the criterion
("X exists iff C(X) = X as a subspace") and rename pointwise-fixedness
claims as a stronger separate property. This matches what the sims
actually verify. Estimated impact: ~2-3h.

### D3: Programme scope (4 papers vs 10 papers)

Foundation paper 01 still describes a 4-paper programme. Either:
- **(a)** Update 01 to 10-paper structure (recommended; reflects reality)
- **(b)** Demote 5–10 to "Solution Lab applications" appendix referenced from 01
- **(c)** Keep 01 as a 4-paper "core" with companion empirical wing as separate programme

Recommend (a). Estimated impact: ~1-2h.

### D4: SL-005 / SL-007 honest-negative framing

Paper 08 has anxiety result (anchor, not trauma) + mood manipulation
(diagnostic false negative). Paper 10 has musical-joint-action FAIL
(diagnostic correctly predicted FAIL) + ds006802 trend.

Option (a): retitle Paper 08 to "Trait-Anxiety Anchor + Mood
Replication"; Paper 10 stays as "Hyperscanning Honest Negative."

Option (b): keep current titles but rewrite abstracts/intros to
foreground the methodology-validation success, not the trauma /
joint-meaning claim.

Recommend (a). Estimated impact: ~3-4h per paper.

---

## What this synthesis enables

Once Phase A is done, the foundation is stable. Phase B fixes the
methodology paper that every other paper cites. After Phase A+B
(~10-16h), the programme should compile clean with no math errors and
match its own demos.

After Phase C+D, the flagship and empirical papers will be coherent
with the methodology and the foundation.

After Phase E, the prose discipline is uniform.

After Phase F, codex re-review can produce a clean "publication
ready: yes" verdict on the substantive scope.

---

*Synthesis prepared from all 10 codex reviews completed 2026-05-22.*

---

## Phase A–D refinement progress (2026-05-22 evening)

User selected "All phases sequential A→B→C→D→E→F". Progress so far:

### Phase A (foundation rebuild) — COMPLETE
- **A1 τ-semantics**: Paper 01 has explicit `τ_ico` (dim 94) vs `τ_spec` (dim 116) notation block. Paper 02 inherits via convention paragraph. Paper 03 R_cl/R_phase reframed as operationalised proxies.
- **A2 subspace invariance vs pointwise**: Paper 01 universal closure structure box rewritten. `C = Fix(τ)` as the maximal `τ`-stable `C_φ`-invariant subspace, not a pointwise fixed set.
- **A3 4-paper → 10-paper map**: Paper 01 §17 replaced with 10-paper table + 7 reading paths + empirical-record paragraph.
- **A4 SL-005/006/007 status refresh**: Paper 02 bib entries updated with current real-data results. Paper 03 cites SL-005, 006, 007 correctly.
- **A5 bib hygiene**: 6 papers had `\bibliography{refs}` fixed to `references`. `SmartLifeClosure` → `SmartLifeAsClosure` everywhere. Paper 02 `references.bib:64` stray brace removed.
- **Bonus**: L324 Banach error fixed; L352 self-similarity claim restricted; 10 stale repro paths corrected; demo counts D1-D6 → D1-D8; "≥35 subjects" → "21 unique subjects"; "volume conduction ruled out" → "argues against scalp volume conduction".

### Phase B (Paper 07 methodology repair) — COMPLETE
- **B1 "iff" → "best predicted by"**: 3 places softened. RNN calibration boundary acknowledged.
- **B2 strict-PASS vs PASS-leaning**: New audit script `src/strict_vs_passleaning_audit.py` produces verdict per substrate. 5 STRICT_PASS, 1 PASS_LEANING (cardiac AF), 1 FAIL (climate). Classification accounting paragraph updated.
- **B3 headline numerical triples recomputed**: From source-of-truth JSON: sensor `t = 5.35`, source `t = 7.76` (paper had wrong 6.83 and 7.00).
- **B4 mood ledger**: False-negative accounting paragraph added explaining the methodology-version decision.
- Cite-key fix: `SmartExistenceClosure` → `SmartLifeAsClosure` for the dyscoherence-definition context.
- BETSE softening: musical-joint-action scope restricted to this dataset/proxy/contrast.

### Phase C (Paper 02 + 03 tightening) — PARTIAL (3 of ~7 theorems demoted)
- **Memory persistence**: theorem → conditional proposition; subspace-vs-pointwise carefully distinguished.
- **Trust stability**: theorem → conditional proposition; "iff" → "two sufficient conditions"; "exhaustive" claim dropped.
- **Self-deception**: theorem → conditional proposition; partial-control assumption made explicit.
- Demo count consistency: "ten" → "thirteen", `repro/life_demo.py` → `papers/02-life-as-closure/repro/life_demo.py`.
- Remaining for full Phase C: Boundary theorem, Thought persistence, Flow time-dilation, Creativity theorem.

### Phase D (empirical wing polish) — PARTIAL
- **06 SL-002**: volume-conduction language softened in 3 places (abstract, source-section conclusion, source-figure caption). Cross-cohort "matched effect size" → "comparable in-sample" + cross-validated LOSO number cited honestly.
- **08 SL-005**: "identifies suffering with" → "P-A-conditional structural proxy for suffering". Beta band aligned to SL-002 canonical 15–30 Hz.
- **09 SL-006**: MOBA "in-progress" / "to be added" / "forthcoming" contradictions all resolved (4 places); script-frozen status corrected.
- Repository URL alignment: `vfd-aria` → `vfd-org`.

### Phase E (programme-wide style) — IN BATCHES
Mostly done as part of A-D edits:
- Over-claim language: "validated" → "operationalised", "rules out" → "argues against", "matched effect size" → "comparable in-sample", "decisive evidence" → "strong robustness evidence", "iff" → "best predicted by".
- Cross-paper attribution audit: Life §13.3 vs §13.2 trauma fix; SmartLifeAsClosure/SmartExistenceClosure key alignment.

### Phase F (Round-2 codex re-review) — IN FLIGHT
Three concurrent codex re-reviews running on Papers 01, 02, 07 (the most-refined load-bearing papers). Verdict awaited.

## Bundle state after refinement (2026-05-22)

| # | Paper | Pages | Status |
|--|---|--:|---|
| 01 | Existence | 33 | τ-disciplined, 10-paper map, Banach fixed |
| 02 | Life | 43 | Memory/Trust/Self-deception demoted, current SL bib |
| 03 | Processing | 18 | R_cl/R_phase reframed, subject count corrected, volume-conduction softened |
| 04 | Cosmic | 17 | Untouched (held back from v1.0) |
| 05 | Bioelectric | 20 | Bib fix only (Phase D narrow-basin work remaining) |
| 06 | Cortical | 17 | Volume-conduction softened + cross-validated LOSO cited |
| 07 | Closure-Distance | 18 | "iff" softened, strict/PASS-leaning split, headline numbers recomputed |
| 08 | Trauma | 9 | Suffering claim softened, beta band aligned |
| 09 | Flow | 9 | MOBA contradictions resolved |
| 10 | Hyperscanning | 8 | Bib fix; deeper rework remaining |

**Total: 192 pages.** All 10 compile cleanly with 0 broken refs. Workspace synced to source-of-truth locations.
