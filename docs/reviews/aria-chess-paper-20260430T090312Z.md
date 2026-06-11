Reading additional input from stdin...
OpenAI Codex v0.124.0 (research preview)
--------
workdir: /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
model: gpt-5.5
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019ddda0-c374-7490-82c8-9f2b876db6c5
--------
user
You are reviewing a physics/neuroscience preprint in LaTeX. Treat this like a careful
journal-referee pass, not a code review.

Paper path (absolute, outside this repo):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex

Section files (read all 10):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex

Bibliography:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib

Source documents the paper lifts from (verify numbers verbatim):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md

WO context (read first):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md

This paper is a SUBSTRATE WITNESS, not a selection theorem. The hard discipline:
- never claim the substrate IS consciousness
- never claim the 600-cell is unique among regular 4-polytopes
- never claim a Lyapunov function on the reduced flow has been delivered
- never claim ACT delivers a selection theorem here
- 18/18 preregistered MUST be reported with methodology refinement disclosure (NOT threshold change)
- chess +40.6pp lift at n=25 with reset (NOT +27.2pp at n=15)
- C×P bootstrap should report 0/2000 resamples at or below zero (NOT P=0)
- propofol switching ratio 1.83x (NOT 2.96x — the latter is the empirical reference)
- HCP n=1003 is descriptive on top of preregistered n=100; not the preregistered N

Read the file in full, then produce a structured review with the following
sections:

1. **Claim audit** For every non-trivial claim (theorem, proposition,
   numerical result, headline statement), say whether the stated argument
   actually establishes the stated claim. Flag over-claims, hidden assumptions,
   missing hypotheses, or cases where the prose needs softening. Quote the
   specific claim and cite the file:line.

2. **Internal consistency** Identify any place where definitions,
   assumptions, or notation conflict across sections. Check that the abstract
   matches the headline tally (18/18 with N=20 deep-dive, 17/18 standard);
   that thresholds in §5 match the preregistration document; that bootstrap
   wording is "0/2000 resamples at or below zero, reported as 0.0000" not "P=0".

3. **External consistency / numerics** For each headline numeric verify against
   the source document by reading it locally:
   - 6/6 v4 signatures (CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md)
   - 18/18 preregistered (VALIDATION_RESULTS_2026-04-29.md)
   - C×P 0.190 / [+0.143, +0.239] / 0/2000 (P4_SYNERGY_FINDING.md)
   - Chess +40.6pp at n=25 with reset (CROSS_DOMAIN_RESULTS.md)
   - HCP -11.58σ / +79.78σ / +6.80σ (CROSS_DOMAIN_RESULTS.md)
   If you find any disagreement, flag with file:line in both source and paper.

4. **Substrate-witness scope discipline** Identify any sentence that strays
   into selection-theorem territory or uniqueness territory. The paper must
   stay strictly inside substrate-witness scope.

5. **Tightness** Identify passages where the tone is stronger than the
   evidence supports, or weaker. Suggest one-line edits.

6. **Surface issues** Typos, undefined macros, broken LaTeX, inconsistent
   capitalisation. The paper defines \Ph, \Lop, \Cph, \Rsixhundred as macros
   in main.tex preamble; check usage is consistent.

7. **Top three fixes** Your ranked list of the most important issues to
   address before this paper is publication-ready. Be specific; cite file:line.

8. **Verdict** "Publication ready: yes" or "Publication ready: no — must-fix
   list above". Be direct. Over-claiming is worse than under-claiming.

ROUND 2 verdict was 'Publication ready: no' with the following must-fixes (now addressed):
- §10 conclusion line 20 'preregistered thresholds' → 'published-reference thresholds' (FIXED).
- §1:10 broad literature overclaim softened to 'we are not aware of prior work that has yielded the kind of preregistered multi-domain quantitative benchmark'.
- §1:12 'typically introduce' → 'often rely on'.
- main.tex 'domain-invariant' → 'in the two cross-domain tasks tested'.
- main.tex 'only where' → 'amplifying in these two tasks where raw features are ambiguous'.
- §4 Φ proxy 'forbids information transport' → 'designed to be small under H4-equivariant dynamics; not a theorem on information transport; proxy capturing observable signature'.
- §4 RECOVERY 'verifies determinism and reversibility' → 'verifies deterministic repeatability under WAKE stimulus protocol'.
- §7 '~65pp of classification power is architectural' → '65.4% of observed accuracy persists under the architecture-only permutation null'.
- §7 'correctly null on conversation' → 'approximately neutral on conversation'.
- §7 P16 confusion text rewritten as 'preregistration combined the null-mapping prediction across both domains; we split for table clarity'.
- §6 'pathway collapses' → 'measured interaction collapses'.
- §5 'validation-protocol refinement on the preregistered estimator' → 'relative to the preregistered test'.
- §1, §9, §10 'six independent' → 'six companion'.
- main.tex 'C and P are causally significant' → 'causally identifiable within the factorial ablation model'.
- §5 P13 row shortened with footnote ddagger below table.

Verify each prior round-2 must-fix is closed; flag any remaining issues; give verdict.
warning: Codex could not find bubblewrap on PATH. Install bubblewrap with your OS package manager. See the sandbox prerequisites: https://developers.openai.com/codex/concepts/sandboxing#prerequisites. Codex will use the vendored bubblewrap in the meantime.
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 177ms:
     1	Read-only audit completed. I did not edit or commit anything.
     2	
     3	**SECTION A. Insight / External Relevance**
     4	
     5	**Already in cascade / companion papers**
     6	- Substrate-witness framing is explicit in `TASK-aria-paper-completion.md:42-57`: use substrate witness, not ACT selection witness; no Lyapunov \(V(W)\), no \(2I\)-equivariance check as deliverables.
     7	- Fixed response kernel is already defined in `docs/aria-closure-kernel.md:11-23`, with 600-cell facts at `:49-60`.
     8	- b-anomaly is the passive-regime companion witness: fixed \(C_\varphi\)-derived kernel, no shape retuning, one amplitude per dataset, at `docs/aria-closure-kernel.md:76-90`, with caveats at `:127-143`.
     9	- ACT supplies only the non-load-bearing 4-tuple bridge: selection is conditional on Lyapunov/timescale hypotheses in `adaptive-closure-transport.tex:222-228`; ARIA dictionary is proposed, not proved, at `:303-328`; programme bridge is explicitly non-load-bearing at `:394-449`.
    10	
    11	**Only in `insight.md`, not suitable as load-bearing ARIA paper content**
    12	- Fine-structure / two-600-cell material: `insight.md:47-64`, `:176-234`. Interesting programme background, but not relevant to ARIA neuroscience claims.
    13	- Crystallisation triplet / \(\alpha\) as selection coupling: `insight.md:361-407`, `:410-450`. Do not import into ARIA except as future programme language.
    14	- RH, god-prime, QMS-3, prime-locus material: `insight.md:601-717`, `:724-827`. Not relevant to this paper.
    15	- Pentagonal holonomy connection: `insight.md:830-892`. Potential future route for selection dynamics, but outside substrate-witness scope.
    16	
    17	**External literature directly needed**
    18	- 600-cell/H4 facts: Coxeter/MathWorld 600-cell reference.
    19	- EEG/SOC: Beggs & Plenz 2003.
    20	- Dataset citations: Sleep-EDFx/PhysioNet, OpenNeuro `ds005620`, OpenNeuro `ds004902`, Zenodo DMT `10.5281/zenodo.3992359`, HCP S1200.
    21	- Consciousness theory comparison: Tononi/IIT, Balduzzi & Tononi, Global Workspace, predictive processing.
    22	- Microstates: Brodbeck et al. 2012 for wake/NREM; propofol microstate/anesthesia papers for drug-state support.
    23	
    24	**SECTION B. Priority Gaps / Build List**
    25	
    26	B1. `01_introduction.tex`: claim-boundary definition  
    27	Object: \(q:\mathcal R_{\rm numeric}\to\mathcal C_{\rm admissible}\), prose map from results to allowed claims.  
    28	Bridges: strong manuscript claims to substrate-witness scope.  
    29	Route: new writing from task discipline.  
    30	First step: “What is tested / not claimed” box.  
    31	Sources: `TASK:44-57`, `TASK:203-226`, `MANUSCRIPT_V2.md:75-87`, `:1086-1091`. AC2, AC9.
    32	
    33	B2. `02_method.tex`: provenance ledger  
    34	Object: \(\Pi:\{P1..P18,S1..S6\}\to\)(script, seed, dataset, threshold, result).  
    35	Bridges: preregistration, deterministic scripts, hostile reproducibility.  
    36	Route: lift from validation docs.  
    37	First step: one table for dates, seeds, scripts, wallclock.  
    38	Sources: `TASK:22-33`, `MANUSCRIPT_V2.md:554-609`, `PAPER_PREDICTIONS.md:1-14`, `VALIDATION_RESULTS_2026-04-29.md:19-75`. AC1, AC8.
    39	
    40	B3. `03_substrate.tex`: 600-cell response substrate  
    41	Object: \(V_{600}=(V,E)\), \(L:\mathbb R^{120}\to\mathbb R^{120}\), \(C_\varphi=L+\varphi^{-2}I\).  
    42	Bridges: classical geometry to empirical substrate.  
    43	Route: classical literature plus local kernel doc.  
    44	First step: lemma stating 120 vertices, 720 edges, degree 12, H4 transitivity, 9 shells, shifted Green response.  
    45	Sources: `MANUSCRIPT_V2.md:158-224`, `aria-closure-kernel.md:11-60`. AC4.
    46	
    47	B4. `04_consciousness_chain.tex`: recurrent substrate observables  
    48	Object: \(T_\eta:\mathbb R^{120}\times F_t\to\mathbb R^{120}\); observables \(O(\tau)=(\alpha,I_{\rm var},\Phi,{\rm cont})\).  
    49	Bridges: substrate response to six EEG signatures.  
    50	Route: lift implementation narrative, rewrite as method not metaphysics.  
    51	First step: define `bounded_topk(k=12)`, \(\Phi\) proxy, continuity score.  
    52	Sources: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:51-102`, `:195-288`; `consciousness_tensor.py:340-359` for \(\varphi^{-2}\) floor caveat. AC4.
    53	
    54	B5. `05_results.tex`: exact empirical tables  
    55	Object: result map \(R:\) condition/test id \(\to\) scalar plus threshold verdict.  
    56	Bridges: source numerics to paper claims.  
    57	Route: verbatim lift, no recomputation.  
    58	First step: tables for 6/6 v4, 18/18, three-way \(\alpha\) overlap.  
    59	Sources: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:30-42`, `:197-288`; `VALIDATION_RESULTS_2026-04-29.md:78-99`, `:262-295`. AC1.
    60	
    61	B6. `06_stress_tests.tex`: C×P interaction proof block  
    62	Object: \(\Delta_{CP}=((\alpha_{CP}+\alpha_0)-(\alpha_C+\alpha_P))/2\).  
    63	Bridges: original P4 fail to strong-coupling result without threshold change.  
    64	Route: existing N=20 derivation plus bootstrap.  
    65	First step: include N=3/5/10/20 trend, finite-bootstrap wording.  
    66	Sources: `P4_SYNERGY_FINDING.md:102-173`, `:175-193`, `:197-229`, `:375-398`. AC1, AC9.
    67	
    68	B7. `07_cross_domain.tex`: selective amplifier and HCP null  
    69	Object: \(A_d={\rm Acc}_{sub,d}-{\rm Acc}_{raw,d}\); \(Z_m=(m_{\rm ARIA}-\mu_{\rm HCP})/\sigma_{\rm HCP}\).  
    70	Bridges: chess/conversation/HCP into one substrate-witness result.  
    71	Route: lift latest cross-domain report, not older Paper Basis numbers.  
    72	First step: use +40.6pp, n=25, 93.8% as authoritative.  
    73	Sources: `CROSS_DOMAIN_RESULTS.md:52-216`, `:234-303`, `:307-424`. AC1, AC5.
    74	
    75	B8. `08_discussion.tex`: non-load-bearing ACT bridge  
    76	Object: dictionary \(D_{\rm ACT}:(M,L_M,W,R_{\rm hom})\to\) ARIA components.  
    77	Bridges: empirical ARIA to ACT without claiming selection theorem.  
    78	Route: alternative route K, explicitly non-load-bearing.  
    79	First step: one closing subsection mapping the 4-tuple and deferring Lyapunov, edge-space lift, \(2I\)-equivariance.  
    80	Sources: `TASK:44-57`, `ACT:303-328`, `ACT:394-449`, `aria-closure-kernel.md:216-257`. AC2, AC6, AC7.
    81	
    82	B9. `09_limitations.tex`: hostile-review guard matrix  
    83	Object: \(G:{\rm risk}\to({\rm disclosure},{\rm evidence},{\rm build})\).  
    84	Bridges: evidence to credible scope.  
    85	Route: b-anomaly five-move template.  
    86	First step: regime, post-hoc, interpretation, test/claim, state-drift moves.  
    87	Sources: `TASK:172-191`, `MANUSCRIPT_V2.md:1012-1098`, `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:354-379`, `NON_EQUILIBRIUM_FINDING.md:11-21`, `:97-105`. AC3, AC5.
    88	
    89	B10. `main.tex`, `README.md`, `references.bib`: paper shell  
    90	Object: deliverable graph \(D=(sections,bib,repro)\).  
    91	Bridges: source docs to BANOMALY-style paper.  
    92	Route: mirror template.  
    93	First step: scaffold exact 10-section structure.  
    94	Sources: `TASK:61-83`, `b-anomaly/paper/main.tex:136-171`, `MANUSCRIPT_V2.md:1101-1159`. AC7.
    95	
    96	**SECTION C. Reversals / Corrections**
    97	
    98	Apply these when lifting prose:
    99	
   100	- at `PAPER_BASIS_2026-04-29.md:48` replace `chess pattern recognition (84.4% LOO with reset; 83.1% 5-fold CV)` with `chess pattern recognition (93.8% LOO with reset at n=25; 83.1% 5-fold CV)`.
   101	- at `PAPER_BASIS_2026-04-29.md:550` replace `Chess goldilocks peak:                   n=15` with `Chess goldilocks peak:                   n=25`.
   102	- at `PAPER_BASIS_2026-04-29.md:551` replace `Chess substrate lift on LOO (with reset): +27.2pp` with `Chess substrate lift on LOO (with reset): +40.6pp`.
   103	- at `PAPER_BASIS_2026-04-29.md:562` replace `substrate **lifts chess by +27pp**` with `substrate **lifts chess by +40.6pp on LOO at n=25**`.
   104	- at `PAPER_BASIS_2026-04-29.md:602` replace `| P12 | Goldilocks peak ∈ {15, 25, 40, 60} | ✅ | 15 |` with `| P12 | Goldilocks peak ∈ {15, 25, 40, 60} | ✅ | 25 |`.
   105	- at `PAPER_BASIS_2026-04-29.md:603` replace `| P13 | Chess LOO lift ≥ +15pp (with reset) | ✅ | +27.2pp |` with `| P13 | Chess LOO lift ≥ +15pp (with reset) | ✅ | +40.6pp |`.
   106	- at `MANUSCRIPT_V2.md:17` replace `The substrate is fully derivable from group theory:` with `Once the 600-cell substrate is chosen, its graph structure is fixed by group theory:`.
   107	- at `PAPER_BASIS_2026-04-29.md:27` replace `The substrate is fully derivable from group theory;` with `Once the 600-cell substrate is chosen, its graph structure is fixed by group theory;`.
   108	- at `MANUSCRIPT_V2.md:795` replace `**HCP result (n=1003 subjects, ICA-50):**` with `**HCP result (preregistered n=100 ICA-50 plus full-cohort n=1003 descriptive statistics):**`.
   109	- in any new paper text replace `P(synergy ≤ 0) = 0` with `0/2000 bootstrap resamples were at or below zero, reported as 0.0000`.
   110	
   111	**SECTION D. Route Discipline / Citation Audit**
   112	
   113	Route S, load-bearing: substrate-witness paper. It needs exact numerics, prereg provenance, substrate construction, limitations.
   114	
   115	Route K, non-load-bearing only: ACT-selection witness. It would require Lyapunov \(V(W)\), edge-space decomposition, \(2I\)-equivariance, and full reduced-flow convergence. Do not present this as delivered.
   116	
   117	Required bibtex groups:
   118	- Geometry: Coxeter / 600-cell reference, e.g. MathWorld 600-cell.
   119	- EEG avalanche: Beggs & Plenz 2003, DOI `10.1523/JNEUROSCI.23-35-11167.2003`.
   120	- Datasets: Sleep-EDFx/PhysioNet; OpenNeuro `ds005620` DOI `10.18112/openneuro.ds005620.v1.0.0`; OpenNeuro `ds004902` DOI `10.18112/openneuro.ds004902.v1.0.8`; DMT Zenodo `10.5281/zenodo.3992359`; HCP S1200 plus Van Essen 2013 DOI `10.1016/j.neuroimage.2013.05.041`.
   121	- Consciousness theory: Tononi 2008, Balduzzi & Tononi 2008, Global Workspace, predictive processing.
   122	- Microstates/anesthesia: Brodbeck et al. 2012 DOI `10.1016/j.neuroimage.2012.05.060`; add a propofol-specific microstate citation if claiming anesthesia fragmentation.
   123	
   124	**SECTION E. Top-5 Risk Register**
   125	
   126	1. \(\varphi^{-2}\) floor not derived. Guard: disclose as design-level stability clamp, not theorem. Anchor: `consciousness_tensor.py:348-359`.
   127	2. Preregistration date ambiguity. Guard: separate Apr 18 P1-P18 from Apr 24 H4/rung batteries. Anchors: `PAPER_PREDICTIONS.md:1-14`, `PREREG_H4_FINGERPRINT.md:1-11`, `PREREG_RUNG_OBSERVABLES.md:1-7`.
   128	3. v4 single-seed chain. Guard: state deterministic seed 42 and event bootstrap; name cross-seed replication as strengthening build. Anchor: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:195-203`, `:371-376`.
   129	4. P4 N=20 was data-second after N=3 fail. Guard: report ordering, original fail, same threshold, high-variance rationale. Anchors: `P4_SYNERGY_FINDING.md:68-95`, `:102-123`, `VALIDATION_RESULTS_2026-04-29.md:267-280`.
   130	5. 600-cell chosen post-hoc. Guard: substrate-witness framing, no uniqueness claim, future ablation against 24-cell/120-cell. Anchors: `TASK:46-50`, `MANUSCRIPT_V2.md:1086-1091`.
   131	
   132	Missing-content check: `MANUSCRIPT_V2` is paper-shaped, but §1 and abstract need overclaim tightening; §5 needs exact dataset DOIs; §6 needs finite-bootstrap wording; §8 limits must become target §9 five-move limitations.
   133	
   134	**SECTION F. Top 3 Next Builds**
   135	
   136	1. Build `paper/sections/05_results.tex`: insert exact 6/6, 18/18, and \(\alpha\)-overlap tables. Anchors: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:197-288`, `VALIDATION_RESULTS_2026-04-29.md:78-99`, `CROSS_DOMAIN_RESULTS.md:184-196`.
   137	
   138	2. Build `paper/sections/03_substrate.tex` plus limitation hooks: define \(V_{600}\), \(L\), \(C_\varphi\), shells, and \(\varphi^{-2}\) disclosure. Anchors: `aria-closure-kernel.md:11-60`, `MANUSCRIPT_V2.md:158-224`, `consciousness_tensor.py:348-359`.
   139	
   140	3. Build `paper/sections/06_stress_tests.tex` and `07_cross_domain.tex`: P4 factorial derivation, reset protocol, +40.6pp chess lift, HCP null. Anchors: `P4_SYNERGY_FINDING.md:125-173`, `VALIDATION_RESULTS_2026-04-29.md:163-194`, `CROSS_DOMAIN_RESULTS.md:175-216`, `:307-424`.
   141	
   142	External sources used: MathWorld 600-cell, PhysioNet Sleep-EDFx, EEGDash/OpenNeuro DS005620 and DS004902, Zenodo DMT record 3992359, PubMed/PMC entries for Beggs & Plenz, Tononi, Balduzzi & Tononi, Brodbeck, and Van Essen/HCP.

 succeeded in 177ms:
     1	# TASK: Write the aria-chess publication-ready paper
     2	
     3	**Date:** 2026-04-30.
     4	**Bar:** Hostile-review-ready, no overclaim. Strong, confident paper backed by lots of empirical evidence. Per `feedback_credibility_bar.md`: "complete + undismissable" not "honest + conditional."
     5	**Pair-programmer pattern:** codex_derive (this WO) → Claude implements → review_paper.sh hostile audit → iterate until codex says "Publication ready: yes."
     6	
     7	---
     8	
     9	## 1. Substrate (existing material to lift from)
    10	
    11	**Empirical / methods content (paper-grade, ready to lift):**
    12	- `docs/brain_mapping/MANUSCRIPT_V2.md` — 1245 lines, 11 sections, complete draft with abstract through conclusion. Already structurally close to publication; needs tex conversion and tightening.
    13	- `docs/brain_mapping/PAPER_BASIS_2026-04-29.md` — 37 KB, paper-ready abstract + intro + methods + results
    14	- `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` — 6/6 v4 signature table, full per-signature documentation
    15	- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — N=20 deep-dive narrative + per-seed values + bootstrap
    16	- `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md` — chess + conversation + HCP results
    17	- `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` — 18/18 prereg tally with thresholds
    18	- `docs/brain_mapping/PREREG_H4_FINGERPRINT.md`, `PREREG_RUNG_OBSERVABLES.md` — frozen 2026-04-24 predictions
    19	- `docs/brain_mapping/EMERGENCE_AUDIT.md` — what's hardcoded vs derived
    20	- `docs/brain_mapping/REPRODUCIBILITY.md` — pipeline documentation
    21	
    22	**Headline numbers (deterministic, regenerable from seed=42, seed range 32000-32019):**
    23	
    24	| Result | Value | Source script | Wallclock |
    25	|--------|-------|---------------|-----------|
    26	| 6/6 v4 EEG signature table | 4 conditions × 6 signatures all pass | `demo_drug_sleep_v4.py` | ~30s |
    27	| P4 C×P synergy (N=20) | +0.190 [+0.143, +0.239]; P(≤0)=0.0000 | `demo_p4_cxp_deep_dive.py` | ~28 min |
    28	| 18/18 preregistered tally | All P1-P18 pass | `run_preregistered_validation.py` | ~18 min |
    29	| HCP categorical separation | Degree-std 11.58σ, PR 79.78σ (n=1003) | Cascade pipeline | (deterministic) |
    30	| Sleep-EDFx spindle α | 2.513 (real) ∈ ARIA CI | Sleep-EDFx public data + `run_baseline_for_eeg.py` | (cached) |
    31	| Cascade-α three-way overlap | WAKE [1.82,2.86] ∩ EEG [2.50,2.86] ∩ ARIA prior [2.73,3.25] | Combined | (cached) |
    32	
    33	**Validation persistence:** `~/.aria/preregistered_validation/results_1777466957.json` (Apr 29 13:49) is the 18/18 record.
    34	
    35	**Theoretical anchors:**
    36	- `BANOMALY-001/vfd-b-anomaly/paper/main.tex` — structural template (10 sections: intro, method, derivation, results, stress_tests, cross_dataset, cross_channel, discussion, limitations, conclusion).
    37	- `vfd-crystalisation-paper/papers/adaptive-closure-transport/adaptive-closure-transport.tex` — ACT theory paper. The aria-chess paper is the **active-regime empirical companion** to ACT; ACT names ARIA as the candidate instantiation of the 4-tuple (Remark 7.1 / sec:aria).
    38	- `vfd-crystalisation-paper/docs/aria-closure-kernel.md` — kernel-spine doc; aria-chess witnesses the active regime alongside b-anomaly's passive-regime witness.
    39	
    40	---
    41	
    42	## 2. Framing decision (load-bearing)
    43	
    44	**Adopt the substrate-witness framing, NOT the ACT-selection-theorem-witness framing.**
    45	
    46	The substrate-witness framing claims:
    47	- A deterministic geometric substrate (600-cell under H₄ symmetry) reproduces 18 preregistered neuroscience predictions across multiple paradigms with NO fitted shape parameters.
    48	- The claim is **not** that the substrate explains consciousness or that it's the unique solution.
    49	- The claim is **not** that ACT's selection-theorem (Hypothesis 4.3) is empirically witnessed.
    50	- The claim is: this geometry, with one parameter set, produces a specific quantitative correspondence with cortex.
    51	
    52	Under this framing:
    53	- Lyapunov V(W) is **not required** as a deliverable (would be required for ACT-selection-witness).
    54	- 2I-equivariance check is **not required** (would be required for cascade-selection-witness).
    55	- G-ablation is **nice-to-have** but the recovery-reversibility result already witnesses learning-rule idempotency.
    56	
    57	The ACT bridge appears as a non-load-bearing closing subsection in §8, mapping ARIA to ACT's 4-tuple as a programme-positioned correspondence (per `feedback_mathematical_framing_discipline.md` rule).
    58	
    59	---
    60	
    61	## 3. Output structure
    62	
    63	Mirror BANOMALY-001/vfd-b-anomaly/paper/ exactly:
    64	
    65	```
    66	aria-chess/
    67	└── paper/
    68	    ├── main.tex              # frontmatter + \include all sections + bibliography
    69	    ├── README.md             # paper README mirroring b-anomaly README.md (headline result, table, statistical caveat, repro recipe)
    70	    ├── references.bib        # bibtex entries
    71	    ├── sections/
    72	    │   ├── 01_introduction.tex
    73	    │   ├── 02_method.tex
    74	    │   ├── 03_substrate.tex          # the 600-cell + cascade decomposition + Green response
    75	    │   ├── 04_consciousness_chain.tex # 4-layer chain
    76	    │   ├── 05_results.tex            # 6/6 v4 + 18/18 + cascade-α match
    77	    │   ├── 06_stress_tests.tex       # P4 N=20 + bootstrap + ablation matrix
    78	    │   ├── 07_cross_domain.tex       # chess + conversation + HCP
    79	    │   ├── 08_discussion.tex
    80	    │   ├── 09_limitations.tex
    81	    │   └── 10_conclusion.tex
    82	    └── figures/                # placeholder for any figures (likely none in v1)
    83	```
    84	
    85	---
    86	
    87	## 4. Section content blueprint
    88	
    89	### §1 Introduction (target: 100-130 lines)
    90	- The problem: consciousness theories typically fit (predictive coding, IIT, GNW). What if a substrate were group-theoretically forced and non-fittable?
    91	- The geometry: H₄ Coxeter / 600-cell — biological motivation (icosahedral hippocampus, theta-gamma 11:1 ratio, etc.) but NOT a-priori derivation.
    92	- What this paper tests (verbatim "what is tested / what is not claimed" pattern, mirror b-anomaly §1).
    93	- Programme position: passive-regime witness for $C_\varphi$ in b-anomaly is the companion (one substrate, two empirical layers).
    94	
    95	### §2 Method (target: 150-190 lines)
    96	- Datasets: Sleep-EDFx (n=30/24), OpenNeuro ds005620 propofol (n=20), Zenodo ds003992359 DMT (n=29), ds004902 SD (n=35), HCP-YA S1200 (n=1003) — all public, cite DOIs.
    97	- Substrate construction summary (full derivation in §3): 600-cell, H₄ acting transitively, 9 H₃-shells, 12-degree.
    98	- Cascade event detection method.
    99	- Power-law fit + bootstrap CI.
   100	- Stimulus models for v4 (WAKE, SLEEP_N3, PROPOFOL, RECOVERY).
   101	- Preregistration protocol (frozen 2026-04-18 / 2026-04-24, what was peeked / what was not — be honest about ordering).
   102	- Reproducibility ledger (versions, seeds, deterministic).
   103	- State-reset protocol — the homeostatic_reset(level=1.0) call, why mandatory, how P13 changed from -3pp to +40.6pp.
   104	
   105	### §3 Substrate construction (target: 80-120 lines)
   106	- 600-cell vertex set V_600, 720 edges, 12-regular, 9 H₃-shells {1,12,20,12,30,12,20,12,1}.
   107	- H₄ Coxeter symmetry, transitivity, eigenvalue spectrum (12 mult 1; 6φ mult 4; 4φ mult 9; 3 mult 16; ...).
   108	- Cascade rung decomposition E₈→H₄→40→D₄→16→8→0 (briefly, with reference to cascade-derivation programme).
   109	- Green response operator $C_\varphi = L + \varphi^{-2} I$, programme-level definition (NOT load-bearing for the empirical claims; cite docs/aria-closure-kernel.md).
   110	- Reference: ACT theory paper for the 4-tuple (M, L_M, W, R_hom) framing; aria's instantiation flagged as candidate per ACT Remark 7.1.
   111	
   112	### §4 Consciousness chain (target: 80-120 lines)
   113	- Recurrent loop: Cascade event detection feeding cascade-pressure ρ.
   114	- Bounded-top-K (k=12) thresholding (matches degree).
   115	- IIT integrated-information layer (Φ trajectory).
   116	- Stream continuity layer.
   117	- Phenomenal-field binding.
   118	- All four layers derived from substrate; no fitted parameters.
   119	
   120	### §5 Results (target: 200-280 lines)
   121	
   122	**§5.1 Six v4 EEG signatures across 4 brain states**
   123	
   124	Verbatim from MANUSCRIPT_V2 lines 661-677. Per-condition table:
   125	
   126	| Cond | n_evt | α | 95% CI | R² | I_var | Φ_traj | cont |
   127	| WAKE | 58 | 2.252 | [1.82, 2.86] | 0.956 | 2.18e-05 | 0.0008 | 0.943 |
   128	| SLEEP_N3 | 111 | 3.250 | [2.44, 4.14] | 0.886 | 1.01e-05 | 0.0055 | 0.980 |
   129	| PROPOFOL | 246 | 2.758 | [2.52, 3.09] | 0.931 | 5.37e-06 | 0.0003 | 0.877 |
   130	| RECOVERY | 58 | 2.252 | [1.82, 2.86] | 0.956 | 2.18e-05 | 0.0008 | 0.943 |
   131	
   132	Per-signature pass with explicit threshold + falsification gate.
   133	
   134	**§5.2 18/18 preregistered validation tally**
   135	
   136	Full table P1-P18 with threshold + result + dataset + verdict.
   137	
   138	**§5.3 Cascade-α three-way overlap**
   139	
   140	WAKE α [1.82, 2.86] ∩ real EEG α [2.50, 2.86] (Sleep-EDFx n=30) ∩ ARIA prior α [2.73, 3.25].
   141	
   142	### §6 Stress tests (target: 120-180 lines)
   143	
   144	**§6.1 P4 C×P deep-dive (the headline stress test)**
   145	
   146	N=3→5→10→20 trend with per-seed values (19/20 positive); bootstrap CI [+0.143, +0.239]; P(≤0)=0.0000.
   147	
   148	Architectural reading: C and P are STRONGLY coupled, not nearly-orthogonal as the original prereg implicitly assumed. Original "fail" was Type II underpower + seed-range bias.
   149	
   150	**§6.2 16-condition 2⁴ ablation matrix**
   151	
   152	Main effects + pairwise interactions.
   153	
   154	**§6.3 Non-equilibrium homeostatic reset finding**
   155	
   156	Conditions A/B/C/D (no homeostasis / periodic only / wake-decay only / dual). Both required.
   157	
   158	### §7 Cross-domain (target: 120-160 lines)
   159	
   160	**§7.1 Chess** — 5-fold CV 83.1%, LOO lift +40.6pp with reset, goldilocks peak n=25.
   161	**§7.2 Conversation** — 87.5% raw, |lift| < 10pp (selective amplifier).
   162	**§7.3 HCP categorical separation** — n=1003, degree-std 11.58σ, PR 79.78σ.
   163	
   164	### §8 Discussion (target: 120-180 lines)
   165	
   166	**§8.1 What's new** — substrate witness, no fitted parameters, 18/18 prereg, 4-state cross-paradigm.
   167	**§8.2 Comparison to existing theories** — IIT, GNW, predictive coding (substrate ≠ alternative theory; substrate is what *any* theory needs).
   168	**§8.3 Strong C×P coupling for biology** — implications.
   169	**§8.4 Substrate as null reference** — HCP separation reading.
   170	**§8.5 Programme position: ACT bridge (non-load-bearing)** — map to 4-tuple as candidate instantiation; explicitly defer Lyapunov / 2I-equivariance / edge-space lift to ACT open items.
   171	
   172	### §9 Limitations (target: 120-180 lines)
   173	
   174	Brutal honest scope. Apply b-anomaly §9 5-move template:
   175	
   176	**Move 1 (regime clarity):** State that this is a substrate-witness paper; ACT-selection-theorem witness is NOT delivered.
   177	
   178	**Move 2 (post-hoc structure verification):** P4 retest at N=20 was data-second (we saw N=3 fail first). Acknowledge ordering.
   179	
   180	**Move 3 (interpretation alternatives):** Three readings — (a) substrate is real-physics, (b) H₄ is structurally right, (c) data is rank-1 in any group-theoretic substrate. Adopt (c) as conservative.
   181	
   182	**Move 4 (test vs claim boundary):** Universality + cross-paradigm consistency PASS; ACT-active-regime selection-theorem witness NOT claimed.
   183	
   184	**Move 5 (substrate state-drift acknowledged):** Polytope state-drift (P13 fail mode without reset) explicitly disclosed; reset protocol mandatory in repro pipeline.
   185	
   186	Plus enumerated per-section limits:
   187	- 8.1 Substrate-level (600-cell only tested; no comparison to 24-cell, 120-cell)
   188	- 8.2 Consciousness chain (single-seed determinism, stylised stimuli)
   189	- 8.3 Cross-domain (small test sets, single parcellation)
   190	- 8.4 Preregistered validation (single seed range for N=20 P4; freeze date 2026-04-18 vs 2026-04-24 ambiguity)
   191	- 8.5 Theoretical (post-hoc 600-cell choice; cascade decomposition non-unique; φ⁻² floor design-level not derived)
   192	
   193	### §10 Conclusion (target: 80-120 lines)
   194	
   195	- Headline results recap.
   196	- Falsification programme: 4 explicit kill-switches.
   197	- What this is / is not (b-anomaly Move 5).
   198	- Reproducibility recap.
   199	- Connection to b-anomaly + ACT (one cascade infrastructure, two empirical witnesses).
   200	
   201	---
   202	
   203	## 5. Acceptance criteria
   204	
   205	**AC1.** Every numerical claim is verbatim from the deterministic scripts. The 18/18 table, the 6/6 signature table, the P4 N=20 result, the HCP separation — exact numbers reproducible from `demo_drug_sleep_v4.py`, `demo_p4_cxp_deep_dive.py`, `run_preregistered_validation.py`.
   206	
   207	**AC2.** No claim is stronger than what the substrate-witness framing supports. In particular:
   208	- DO NOT claim ACT-selection-theorem witness (Hypothesis 4.3) is delivered.
   209	- DO NOT claim 2I-equivariance is checked.
   210	- DO NOT claim Lyapunov V(W) exists.
   211	- DO NOT claim consciousness is "explained."
   212	- DO NOT claim the substrate is the unique solution.
   213	
   214	**AC3.** The five b-anomaly honest-scope moves have explicit equivalents in §9 (regime, post-hoc, interpretation, test/claim, state-drift).
   215	
   216	**AC4.** φ⁻² floor is explicitly disclosed as design-level (consciousness_tensor.py:348, pending first-principles calibration).
   217	
   218	**AC5.** Polytope state-drift is explicitly disclosed; the homeostatic_reset(level=1.0) protocol is mandatory in the repro pipeline.
   219	
   220	**AC6.** ACT bridge (§8.5) is non-load-bearing per `feedback_mathematical_framing_discipline.md`.
   221	
   222	**AC7.** Citations to b-anomaly + adaptive-closure-transport are correct, with proper bibtex.
   223	
   224	**AC8.** Preregistration date ambiguity (2026-04-18 frozen predictions vs 2026-04-24 frozen H4-fingerprint) is explicitly clarified.
   225	
   226	**AC9.** Hostile-review-ready: every paragraph survives a referee asking "is this what the data actually shows, or what you wish it showed?"
   227	
   228	---
   229	
   230	## 6. Out of scope
   231	
   232	- Aria-chess `paper/figures/` content (placeholder OK; figures can be added in revision).
   233	- Code-freeze tag (separate task; user controls).
   234	- Edits to MANUSCRIPT_V2.md or other supporting docs (those are the source; the tex paper is the deliverable).
   235	- Lyapunov V derivation (deferred to ACT companion paper or future work).
   236	- 2I-equivariance audit (deferred).
   237	- G-ablation (nice-to-have; not blocking).
   238	
   239	---
   240	
   241	## 7. Codex derive prompt
   242	
   243	Read this TASK file plus all referenced source documents. For the paper-writing project, produce:
   244	
   245	**SECTION A.** Inventory of paper-ready content vs writing-from-scratch content. For each of the 10 sections, state: which existing material can be lifted directly (cite file:line), what needs writing from scratch.
   246	
   247	**SECTION B.** Numbered build list (B1, B2, ..., Bn) with:
   248	- target file (e.g. `aria-chess/paper/sections/05_results.tex`)
   249	- content blueprint (what goes in this section)
   250	- source attribution (cite file:line for every claim)
   251	- cross-references to other sections / papers
   252	- what AC# it discharges
   253	
   254	**SECTION C.** Citation requirements: which papers need bibtex entries (b-anomaly, ACT, foundation papers, EEG literature). Cite with file paths.
   255	
   256	**SECTION D.** Hostile-review risk register: top 5 places a referee will attack, and how to guard against each. Specifically:
   257	- φ⁻² floor not derived
   258	- preregistration date ambiguity
   259	- single-seed determinism for v4
   260	- post-hoc N=20 P4 retest
   261	- 600-cell as post-hoc choice
   262	
   263	**SECTION E.** Missing-content check: anything from MANUSCRIPT_V2 that's WORKING-NOTES quality and needs actual writing for paper-grade prose.
   264	
   265	**SECTION F.** Top-3 build priorities with file:line anchors.
   266	
   267	Hostile-review framing throughout. Do not propose to add content beyond what the substrate-witness framing supports.

codex
The WO context confirms the intended standard: substrate-witness framing only, with exact source numerics and finite-bootstrap wording. I’m moving to the manuscript now, starting with line-numbered reads so every issue can be cited precisely.
exec
/bin/bash -lc "wc -l '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/'*.tex '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"(selection theorem|selection-theorem|unique|uniqueness|Lyapunov|P=0|P\\(|0/2000|18/18|17/18|40\\.6|27\\.2|2\\.96|1\\.83|n=1003|n=100|preregister|threshold|domain-invariant|only where|forbids|verifies|65\\.4|correctly null|approximately neutral|pathway collapses|validation-protocol refinement|six independent|six companion|causally significant|causally identifiable)\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 261ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:20:       eighteen preregistered correspondences and six drug/sleep EEG\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:46:quantitative correspondences with neuroscience data — preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:49:published-reference thresholds on a single deterministic substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:61:neural dataset, is consistent with eighteen preregistered correspondences
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:63:selection theorem, nor a uniqueness claim for the 600-cell among regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:76:preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:77:before any validation run; each has a falsifiable threshold. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:78:preregistered tally is $17/18$ at standard validation methodology
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:79:($5$-seed cascade block plus state-reset protocol), and $18/18$ after
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:81:interaction (P4); no preregistered threshold has been modified. We
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:86:thresholds (Sleep-EDFx, OpenNeuro, Brodbeck, Tononi) and were obtained
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:100:(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:101:ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:102:reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:103:propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:106:All six signatures pass against their published-reference thresholds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:111:emission $P$ — are causally identifiable within the factorial
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:112:ablation model, and the original preregistered C$\times$P synergy
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:116:(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:126:8-dimensional V2 features lifts $+40.6$ percentage points on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:129:preregistered estimator P13 was $5$-fold CV with threshold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:131:refinement at the same threshold), while conversation utterance
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:133:(threshold $|\cdot| < 10$pp), consistent with the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:135:remaining approximately neutral when raw features are already
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:137:(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:145:We do not claim the 600-cell is the unique substrate consistent with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:154:is consistent with eighteen preregistered neuroscience
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:157:without modifying any preregistered threshold.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:191:preregistered validation, figure regeneration, this paper) is reproducible
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:196:$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:7:preregistered prediction was P4: $C\times P$ interaction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:9:$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:11:was walked back. Closing this gap without modifying the preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:12:threshold required (a) re-evaluating the $N\!=\!3$ point estimate as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:99:\item $0/2000$ bootstrap resamples were at or below zero, reported as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:101:\item $0/2000$ bootstrap resamples were below the preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:112:\textbf{The 95\% CI is entirely above the preregistered $+0.10$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:113:threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:114:at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:115:were below the preregistered $+0.10$ floor, reported as $0.0000$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:143:\item It does not establish a Lyapunov function on the reduced flow.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:144:\item It does not establish that the substrate is uniquely selected by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:150:test of one preregistered interaction prediction, on a fresh-seed
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:161:preregistered validation gave estimates consistent with underpowered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:163:$N$ without threshold modification. For preregistration design more broadly:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:164:when preregistering an interaction effect on a system with unknown
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:12:has yielded the kind of preregistered multi-domain quantitative
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:29:against eighteen preregistered correspondences plus six independent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:36:consistent with eighteen preregistered correspondences (frozen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:37:2026-04-18) and six companion drug/sleep EEG signatures of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:56:  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:60:\item \textbf{Eighteen preregistered correspondences pass.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:61:  $17/18$ at standard methodology; $18/18$ after a documented
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:63:  test; \emph{no preregistered threshold has been modified}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:65:  a domain-invariant selective amplifier (chess $+40.6$pp leave-one-out
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:67:  preregistered neutrality bounds) and a maximum-symmetry deterministic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:76:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:77:  the unique substrate consistent with these signatures. Other regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:86:\item \emph{Not a selection theorem.} The companion adaptive-closure-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:91:  non-load-bearing here. We do not deliver a Lyapunov function on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:98:  that some such mechanisms appear in the substrate's preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:118:\;=\;\{\text{`consistent with', `inside threshold', `direction confirmed'}\}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:121:A result that lands inside its preregistered threshold licenses a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:122:`consistent with' claim. A result that exceeds the preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:123:threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:135:\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:139:\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:140:selection theorem on the 4-tuple bridge; circuit-level mechanistic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:149:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:155:signatures, eighteen preregistered correspondences, three-way
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:161:ACT bridge (without claiming a selection theorem).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:98:average degree, not a fitted threshold. No other shape parameter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:7:the validation script, the seed range, the threshold, and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:17:falsifiable threshold, (iii) the validation test (script + seed range),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:21:predictions and rung observables — were preregistered on 2026-04-24
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:24:not include those batteries in the headline 18/18 tally.} They are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:35:\textbf{No threshold has been modified post-hoc.} Where the original
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:43:preregistered threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:49:\text{threshold}, \text{result})$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:60:P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:64:P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:71:P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:97:($2.96\!\times$ wake) in Sig~2.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:110:matrix. The preregistered test (P18) was on $n=100$ subjects for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:111:computational tractability; full-cohort $n=1003$ statistics
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:114:preregistered test.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:139:preregistered cascade-$\alpha$ tests, 2000 resamples for the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:141:preregistered; 42 for the deep-dive.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:144:deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:145:$0/2000$ were below the preregistered floor $+0.10$; we report these
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:146:as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:160:on the full $n=1003$ subject distribution.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:173:substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:174:preregistered floor). The reset protocol is documented in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:189:\item Eighteen preregistered:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:190:  \texttt{python3 run\_preregistered\_validation.py}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:200:verdicts (CI overlaps, $P$-value thresholds) are unaffected.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:145:\textbf{RECOVERY.} Identical to WAKE — verifies deterministic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:160:ablation grid is the basis for the preregistered tests P1--P5 and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:177:(above threshold but not yet crossed) emit pressure at $30\%$ scale,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:9:preregistered neuroscience correspondences plus six companion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:22:thresholds (Sleep-EDFx, OpenNeuro \texttt{ds005620}, Brodbeck 2012,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:24:$0.463\!\times$ wake; propofol modality-switching $1.83\!\times$ wake;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:35:\textbf{Eighteen preregistered correspondences.} All eighteen pass at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:36:preregistered thresholds, with two interaction tests requiring
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:40:preregistered threshold has been modified. The original 2026-04-20
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:48:causally identifiable and \emph{strongly synergistic}: their
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:50:($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples at or
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:60:classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:62:$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:64:refinement at the same threshold), while
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:66:(threshold $|\cdot|\!<\!10$pp) — and as a maximum-symmetry
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:73:derivation of consciousness, not a selection theorem on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:76:uniqueness claim for the 600-cell among regular 4-polytopes. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:80:HCP replication, a Lyapunov function on the reduced flow,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:85:tested against this many preregistered cortical correspondences from
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:89:turn the witness into a selection-theorem-grade claim — including the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:21:  preregistered tolerance with pairwise CI overlap on three reference
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:23:  thresholds on a single deterministic substrate. We are not aware of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:25:  preregistered cortical correspondences from a graph fixed by group
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:35:\item \textbf{The 18/18 preregistered correspondences with no
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:36:  threshold modification.} Every prediction in the preregistered set
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:37:  passes at the preregistered thresholds. The two interaction tests
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:41:  threshold change.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:97:witness claims (six signatures, $18/18$, chess $+40.6$pp,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:104:\item A Lyapunov function $V(W)$ on the reduced flow whose
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:116:selection-theorem witness for ARIA. The companion kernel
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:148:  Allocation discipline for preregistration: when preregistering an
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:19:\emph{Disclosure:} substrate-witness scope, no uniqueness claim
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:23:battery and the eighteen preregistered tests, with thresholds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:59:derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:60:preregistered correspondences plus six signatures; the H$_4$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:63:ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:71:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:85:derive the $\Ph^{-2}$ shift as the unique stability clamp under a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:95:\emph{Evidence:} six signatures vs published thresholds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:116:\textbf{Two preregistered interaction tests required higher $N$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:119:methodology issue, not a threshold change. \emph{Disclosure:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:128:threshold modification.} The reversals (P3, P4, P13) are documented
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:164:\item Lyapunov derivation $V(W)$ from a closure functional
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:179:eighteen preregistered correspondences and six companion drug/sleep
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:181:refinement and without modifying any preregistered threshold. We do
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:183:selection theorem on the ACT bridge. We do not claim uniqueness for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:10:$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:55:   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:56:   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:75:All six signatures pass against their published-reference thresholds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:86:\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:88:\textbf{Tally.} $17/18$ at standard validation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:89:(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:90:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:92:$32000$--$32019$). \emph{No preregistered threshold has been modified.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:97:\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:113:P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:116:\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:126:\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:127:estimator as $5$-fold CV at threshold $\geq +15$pp; the 2026-04-29
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:129:stricter test at the unchanged $+15$pp threshold. See
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:133:methodology refinement (no threshold change).}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:139:\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:145:  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:147:  stricter test at the same threshold; the LOO lift was $+3.1$pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:148:  without state reset on a state-drifted substrate, and $+40.6$pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:151:  report this as a \emph{validation-protocol refinement relative to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:152:  the preregistered test}, not as preregistration revision.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:155:\textbf{Headline verdict.} Eighteen preregistered correspondences
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:156:all pass at preregistered thresholds, with two interaction tests
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:58:\caption{Chess preregistered tests (with reset, $n=25$ canonical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:66:P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:69:\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:80:substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:82:reset; we report the LOO finding ($+40.6$pp) above as a stricter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:83:validation-protocol refinement at the unchanged $+15$pp threshold,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:89:This is a $+40.6$pp lift on the LOO refinement; on the preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:99:substrate retains $65.4\%$ classification accuracy under random
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:102:$65.4\%$ of the observed accuracy persists under the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:107:unique; it is a description of the observed accuracy stack.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:118:\caption{Conversation preregistered tests.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:133:lift is $-4.4$pp, well within the preregistered neutrality band
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:134:$|\cdot|\!<\!10$pp. The substrate is approximately neutral on conversation.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:137:$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:138:selective-amplifier behaviour preregistered in 2026-04-18: in these
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:140:(chess raw $\sim 53\%$) and is approximately neutral when raw features
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:150:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:151:$n=100$ subjects for computational tractability, with full-cohort
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:152:$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:153:connectivity matrix; thresholded at the same density as ARIA's
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:163:\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:164:$n=1003$ descriptive statistics.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:168:Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:170:Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:171:Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:181:\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:194:density-matched threshold $\rho = 0.101$; cross-parcellation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:240:Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:241:Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\

 succeeded in 294ms:
   202 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex
   163 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex
   200 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex
   155 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex
   190 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex
   203 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex
   168 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex
   257 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex
   199 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex
   185 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex
    93 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex
   180 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib
  2195 total

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 147ms:
     1	% =====================================================================
     2	\section{Methods and provenance}\label{sec:method}
     3	% =====================================================================
     4	
     5	This section is a provenance ledger. It records, for each empirical
     6	claim downstream, the dataset, the preregistration date and document,
     7	the validation script, the seed range, the threshold, and the
     8	wallclock — the minimal information a hostile reviewer needs to
     9	reproduce or refute the claim.
    10	
    11	\subsection{Preregistration discipline}
    12	
    13	\textbf{Frozen 2026-04-18.} Eighteen quantitative predictions
    14	(P1--P18) were locked on 2026-04-18 in
    15	\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any validation
    16	run. Each prediction has (i) a specific numerical claim, (ii) a
    17	falsifiable threshold, (iii) the validation test (script + seed range),
    18	and (iv) a rationale identifying what would falsify it.
    19	
    20	\textbf{Frozen 2026-04-24.} Two later batteries — H$_4$ fingerprint
    21	predictions and rung observables — were preregistered on 2026-04-24
    22	in \texttt{docs/brain\_mapping/PREREG\_H4\_FINGERPRINT.md} and
    23	\texttt{docs/brain\_mapping/PREREG\_RUNG\_OBSERVABLES.md}. \emph{We do
    24	not include those batteries in the headline 18/18 tally.} They are
    25	listed as future strengthening builds in~\S\ref{sec:limitations}.
    26	
    27	\textbf{Six EEG signatures (set B).} The drug/sleep signatures on the
    28	recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six
    29	independent published biological signatures (NREM-N3 variance ratio,
    30	propofol switching ratio, propofol continuity drop, propofol $\Phi$
    31	collapse, recovery reversibility, wake cascade-$\alpha$). They are
    32	not part of the P1--P18 preregistration; they are reported as a
    33	companion validation set on the recurrent layer.
    34	
    35	\textbf{No threshold has been modified post-hoc.} Where the original
    36	2026-04-20 validation reported failures (P3, P4, P13), the documented
    37	methodological refinements were
    38	(a)~increasing $N$ from $3$ to $5$ for cascade interaction terms,
    39	(b)~adding a $N\!=\!20$ deep-dive for the highest-variance interaction
    40	(P4, C$\times$P), and
    41	(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
    42	measurements for the chess LOO test (P13). None of these touched a
    43	preregistered threshold.
    44	
    45	\subsection{Provenance ledger}
    46	
    47	We write the provenance map as $\Pi\colon\{\text{claim id}\}
    48	\to (\text{script}, \text{seed range}, \text{dataset/source},
    49	\text{threshold}, \text{result})$.
    50	
    51	\begin{table}[ht]
    52	\centering
    53	\small
    54	\caption{Provenance ledger for the headline empirical claims.}
    55	\label{tab:provenance}
    56	\begin{tabular}{l l l l l}
    57	\toprule
    58	Claim & Script & Seed range & Dataset / source & Threshold \\
    59	\midrule
    60	P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
    61	P2 ($C$ main) & same & 30010--30014 & this paper & $\geq +0.30$ \\
    62	P3 ($|D{\times}C|$) & same & 30020--30024 & this paper & $|\cdot| < 0.20$ \\
    63	\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
    64	P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
    65	P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
    66	P7 ($W{\to}N3$ var) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.70$ \\
    67	P8 ($W{\to}N3$ switch) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.50$ \\
    68	P9 (chess 5-fold) & same & 30200--30204 & 32 positions, 4 cat. & $\geq 70\%$ \\
    69	P10 (chess null) & \texttt{run\_chess\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    70	P11 (chess random-label) & same & 30210+ & same & $\in [15\%, 35\%]$ \\
    71	P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
    72	\textbf{P13 (chess sub.\ lift)} & same & with reset & same (LOO refinement) & $\geq +15$pp \\
    73	P14 (conv 5-fold) & same & 30220--30224 & 64 utt., 8 cat. & $\geq 75\%$ \\
    74	P15 ($|$conv lift$|$) & same & same & same & $|\cdot| < 10$pp \\
    75	P16 (conv null) & \texttt{run\_conversation\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    76	P17 (ARIA deg std) & substrate construction & deterministic & H$_4$ theorem & $=0$ \\
    77	P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
    78	\midrule
    79	Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
    80	\bottomrule
    81	\end{tabular}
    82	\end{table}
    83	
    84	\subsection{Datasets and DOIs}
    85	
    86	\textbf{Sleep-EDFx (PhysioNet).} Public polysomnography
    87	recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
    88	the cortical-avalanche $\alpha$ baseline; $n=24$ subjects used for
    89	the wake$\to$N3 variance and switching ratios. Cortical-avalanche
    90	fitting follows the Beggs--Plenz log-CCDF
    91	methodology~\citep{BeggsPlenz2003}.
    92	
    93	\textbf{OpenNeuro \texttt{ds005620}.} Propofol-induced loss of
    94	consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
    95	DOI \texttt{10.18112/openneuro.ds005620.v1.0.0}. Used as the
    96	empirical reference for the propofol switching ratio
    97	($2.96\!\times$ wake) in Sig~2.
    98	
    99	\textbf{OpenNeuro \texttt{ds004902}.} DMT-induced altered states
   100	EEG~\citep{OpenNeuroDS004902},
   101	DOI \texttt{10.18112/openneuro.ds004902.v1.0.8}. Background
   102	psychedelic-state reference; not load-bearing for the headline tally.
   103	
   104	\textbf{Zenodo \texttt{3992359}.} DMT EEG public
   105	release~\citep{ZenodoDMT3992359},
   106	DOI \texttt{10.5281/zenodo.3992359}. Same status as above.
   107	
   108	\textbf{HCP S1200.} Human Connectome Project
   109	S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
   110	matrix. The preregistered test (P18) was on $n=100$ subjects for
   111	computational tractability; full-cohort $n=1003$ statistics
   112	(degree std, participation ratio, clustering coefficient $\sigma$-
   113	distances) are reported as descriptive statistics on top of the
   114	preregistered test.
   115	
   116	\textbf{Microstate baseline (qualifier).} The continuity-drop
   117	signature (Sig~3) follows the EEG microstate methodology lineage of
   118	Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
   119	microstates. Brodbeck et al.\ is not a propofol-specific paper; we
   120	use it for the underlying microstate-fragmentation methodology, not
   121	as a propofol reference. A propofol-specific microstate citation
   122	would tighten this section; we treat that as an open
   123	strengthening build.
   124	
   125	\subsection{Statistical methods}
   126	
   127	\textbf{Cascade-$\alpha$ fitting.} Power-law $\alpha$ is fit by
   128	ordinary least squares on the log-CCDF of the cascade-event size
   129	distribution, restricted to the central 80\% mass band (excluding the
   130	bottom 10\% and top 10\% to avoid extreme-tail noise). $R^{2}$ is
   131	reported on the linear fit in log-space. A cascade event is defined
   132	as an attention-vertex shift between consecutive ticks
   133	$\arg\max|\mathrm{state}_{t}|\neq \arg\max|\mathrm{state}_{t-1}|$;
   134	the event size is the $\ell^{1}$ norm of the state-difference vector
   135	at that tick. Zero-size events are excluded.
   136	
   137	\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
   138	estimated by event-resampling bootstrap (500 resamples for the
   139	preregistered cascade-$\alpha$ tests, 2000 resamples for the
   140	$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
   141	preregistered; 42 for the deep-dive.
   142	
   143	\textbf{Bootstrap one-sided $P$-value reporting.} For the C$\times$P
   144	deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
   145	$0/2000$ were below the preregistered floor $+0.10$; we report these
   146	as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
   147	zero-probability statement on a finite resample.
   148	
   149	\textbf{Factorial interaction estimator.} For the $2{\times}2$
   150	ablation conditions $\{----, -C--, --P-, -CP-\}$, the interaction is
   151	\[
   152	\Delta_{CP}
   153	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
   154	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
   155	\]
   156	
   157	\textbf{$\sigma$-distance against external nulls.} For the HCP
   158	comparisons we report
   159	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
   160	on the full $n=1003$ subject distribution.
   161	
   162	\subsection{State-reset protocol}
   163	
   164	The substrate exhibits state drift: across approximately five
   165	successive depth-sweep evaluations the pressure field equilibrates
   166	to a uniform attractor and classification structure collapses to
   167	raw-feature baseline. Multi-trial benchmarks therefore require an
   168	explicit reset between successive evaluations.
   169	\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
   170	re-initialises pressure-field, crossed-vertex, and training state to
   171	canonical baseline. With reset between depth measurements, the chess
   172	LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
   173	substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
   174	preregistered floor). The reset protocol is documented in
   175	\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
   176	generalisable lesson is recorded in \S\ref{sec:limitations}: any
   177	multi-trial benchmark on a non-stationary substrate must specify
   178	state-reset protocol.
   179	
   180	\subsection{Reproducibility commands}
   181	
   182	\begin{itemize}\itemsep=2pt
   183	\item Substrate self-test:
   184	  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
   185	\item Six drug/sleep signatures:
   186	  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
   187	\item C$\times$P synergy $N\!=\!20$ deep-dive:
   188	  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
   189	\item Eighteen preregistered:
   190	  \texttt{python3 run\_preregistered\_validation.py}
   191	  ($\sim 18$\,min).
   192	\item Whole-paper repro:
   193	  \texttt{bash reproduce\_paper\_claims.sh}.
   194	\end{itemize}
   195	
   196	All scripts are deterministic given seeds. Reruns at seed $42$ on the
   197	recurrent layer should reproduce per-condition means in this paper to
   198	4~decimal places. Bootstrap CIs may differ in the 4th decimal due to
   199	NumPy version differences in the bootstrap RNG; the qualitative
   200	verdicts (CI overlaps, $P$-value thresholds) are unaffected.

 succeeded in 153ms:
     1	% =====================================================================
     2	\section{Introduction}\label{sec:intro}
     3	% =====================================================================
     4	
     5	Theories of consciousness divide into mechanism-driven proposals
     6	(Integrated Information Theory~\citep{Tononi2008,BalduzziTononi2008},
     7	Global Workspace Theory~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain},
     8	predictive processing~\citep{FristonFreeEnergy2010,ClarkPP2013}) and
     9	structure-driven proposals (geometric or topological substrates,
    10	neural-population dynamics). The mechanism-driven proposals offer
    11	compelling axiomatic stories; we are not aware of prior work that
    12	has yielded the kind of preregistered multi-domain quantitative
    13	benchmark on real EEG data tested here. The structure-driven
    14	proposals produce numbers but often rely on fitted parameters,
    15	learned weights, or domain-specific calibration.
    16	
    17	This paper takes a deliberately constrained third path. Once a
    18	substrate is chosen, we ask which neuroscience phenomena it is
    19	consistent with under \emph{no} shape parameter tuning, no learned
    20	weights, and no domain-specific calibration. The substrate is the
    21	600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
    22	H$_4$ Coxeter symmetry. It has been studied in pure mathematics for
    23	over a century~\citep{CoxeterRegularPolytopes,Weisstein600Cell}; to
    24	our knowledge it has not been proposed before as an empirical
    25	consciousness substrate. We construct $\Rsixhundred$, fix its response
    26	operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
    27	single condition-dependent self-injection coupling $\eta$ and a
    28	single graph-pinned nonlinearity, and test the resulting witness
    29	against eighteen preregistered correspondences plus six independent
    30	drug/sleep EEG signatures.
    31	
    32	\subsection*{What this paper claims}
    33	
    34	We claim a single \emph{substrate witness}: that a geometry-fixed
    35	substrate, with no shape parameters tuned to any neural dataset, is
    36	consistent with eighteen preregistered correspondences (frozen
    37	2026-04-18) and six companion drug/sleep EEG signatures of
    38	conscious vs unconscious states.
    39	
    40	\begin{enumerate}\itemsep=2pt
    41	\item \textbf{Substrate is fixed by group theory once chosen.} Once
    42	  $\Rsixhundred$ is selected, $120$ vertices of uniform degree $12$
    43	  are forced by H$_4$ transitivity, the Laplacian eigenvalues
    44	  $\{0, 3, 4\Ph, 6\Ph, 12\!-\!4\Ph, 12\!-\!6\Ph, 12\!-\!3, 12\}$ in
    45	  their irrep multiplicities are forced by character theory, and
    46	  the response operator $\Cph$ is fully fixed up to the single
    47	  parameter $\Ph^{-2}$ (a stability shift for the inverse map).
    48	\item \textbf{Cortical avalanches.} Wake cascade-event power-law
    49	  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
    50	  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
    51	  (n$=$30 subjects) and ARIA's prior cascade-pipeline CI
    52	  $[2.73, 3.25]$.
    53	\item \textbf{Six drug/sleep signatures.} On a single deterministic
    54	  trajectory at seed $42$: NREM-N3 phenomenal-intensity variance
    55	  collapse to $0.463\!\times$ wake; propofol modality-switching
    56	  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
    57	  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
    58	  recovery deterministically identical to wake; wake cascade-$\alpha$
    59	  in the SOC band.
    60	\item \textbf{Eighteen preregistered correspondences pass.}
    61	  $17/18$ at standard methodology; $18/18$ after a documented
    62	  $N\!=\!20$ deep-dive on the residual high-variance interaction
    63	  test; \emph{no preregistered threshold has been modified}.
    64	\item \textbf{Cross-domain selectivity.} The substrate functions as
    65	  a domain-invariant selective amplifier (chess $+40.6$pp leave-one-out
    66	  lift at depth $n\!=\!25$ ticks; conversation $-4.4$pp lift, within
    67	  preregistered neutrality bounds) and a maximum-symmetry deterministic
    68	  null reference for cortical functional connectivity (HCP $n\!=\!1003$:
    69	  ARIA at $-11.58\sigma$ on degree homogeneity; $+79.78\sigma$ on
    70	  participation ratio).
    71	\end{enumerate}
    72	
    73	\subsection*{What this paper does \emph{not} claim}
    74	
    75	\begin{itemize}\itemsep=2pt
    76	\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
    77	  the unique substrate consistent with these signatures. Other regular
    78	  4-polytopes (the 24-cell, the 120-cell) are an explicit ablation
    79	  build, not a discharged comparison. The 600-cell choice is post-hoc
    80	  motivated by the H$_4$ Coxeter cascade structure and biological
    81	  observables; it is not an a-priori derivation from first principles.
    82	\item \emph{Not a derivation of consciousness.} The substrate witness
    83	  shows quantitative agreement with cortical signatures; it does not
    84	  establish that the substrate \emph{is} consciousness, nor that
    85	  its dynamics implement specific phenomenal content.
    86	\item \emph{Not a selection theorem.} The companion adaptive-closure-
    87	  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
    88	  proposes a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which
    89	  this substrate fills the $L_M$ slot. The selection of the 600-cell
    90	  as the active $M$ is conjectural in that paper and is treated as
    91	  non-load-bearing here. We do not deliver a Lyapunov function on the
    92	  reduced flow, nor a $2I$-equivariance audit of the closure operator,
    93	  nor a formal edge-space decomposition. These are listed as open
    94	  builds in~\S\ref{sec:limitations}.
    95	\item \emph{Not a circuit-level model.} The substrate is at the
    96	  architectural-algorithmic level. We do not identify which neural
    97	  populations implement context rotation or partial emission, only
    98	  that some such mechanisms appear in the substrate's preregistered
    99	  ablation matrix and exhibit strong inter-mechanism coupling.
   100	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
   101	  Laplacian floor $\Ph^{-2} \approx 0.382$ is a design-level
   102	  stability clamp (it makes $\Cph$ strictly positive definite and
   103	  bounds the Green response). It is not derived as a theorem from a
   104	  closure functional. The companion kernel
   105	  document~\citep{SmartAriaClosureKernel2026} discusses its role.
   106	\end{itemize}
   107	
   108	\subsection*{Mapping from numerical results to admissible claims}
   109	
   110	To keep this paper inside the substrate-witness scope, we use the
   111	following claim-boundary discipline. Numerical results
   112	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   113	$\mathcal C_{\mathrm{admissible}}$ by the rule
   114	\[
   115	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow \mathcal C_{\mathrm{admissible}},
   116	\qquad
   117	\mathcal C_{\mathrm{admissible}}
   118	\;=\;\{\text{`consistent with', `inside threshold', `direction confirmed'}\}.
   119	\]
   120	We never write `the substrate \emph{is} cortex' or `derives consciousness'.
   121	A result that lands inside its preregistered threshold licenses a
   122	`consistent with' claim. A result that exceeds the preregistered
   123	threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
   124	$+15$pp floor) licenses `decisively above prereg', not `proves'. A
   125	$\sigma$-distance result against an external null
   126	(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
   127	the biological distribution', not `cortex has drifted from an ideal
   128	polytope'. The claim-boundary rule is summarised in the box below
   129	and applied throughout~\S\ref{sec:results}.
   130	
   131	\medskip
   132	\begin{center}
   133	\fbox{\parbox{0.92\linewidth}{\small
   134	\textbf{What is tested / what is not claimed.}\par
   135	\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
   136	signatures, on a geometry-fixed substrate with one condition-dependent
   137	parameter $\eta$ and one graph-pinned nonlinearity, against published
   138	biological observables.\par
   139	\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
   140	selection theorem on the 4-tuple bridge; circuit-level mechanistic
   141	identification; first-principles derivation of $\Ph^{-2}$ shift;
   142	that cortex \emph{is} the 600-cell.
   143	}}
   144	\end{center}
   145	
   146	\subsection*{Layout}
   147	
   148	\S\ref{sec:method} gives the provenance ledger (preregistration date,
   149	seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
   150	constructs $\Rsixhundred$ and the response operator $\Cph$, with the
   151	$\Ph^{-2}$ shift disclosed as a design-level stability clamp.
   152	\S\ref{sec:chain} adds the recurrent self-model layer above the
   153	substrate (single nonlinearity, single self-injection coupling).
   154	\S\ref{sec:results} reports the empirical tables: six drug/sleep
   155	signatures, eighteen preregistered correspondences, three-way
   156	$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
   157	synergy stress test ($N\!=\!3, 5, 10, 20$ trend with bootstrap
   158	$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
   159	selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
   160	discusses the substrate witness and proposes a non-load-bearing
   161	ACT bridge (without claiming a selection theorem).
   162	\S\ref{sec:limitations} enumerates limitations and the
   163	hostile-review guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 211ms:
     1	\documentclass[11pt]{article}
     2	
     3	\usepackage[a4paper, margin=2.5cm]{geometry}
     4	\usepackage{amsmath, amssymb, amsthm}
     5	\usepackage{booktabs}
     6	\usepackage{enumitem}
     7	\usepackage{graphicx}
     8	\usepackage{natbib}
     9	\usepackage[colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue]{hyperref}
    10	\usepackage{xcolor}
    11	
    12	\graphicspath{{figures/}}
    13	
    14	\newcommand{\Ph}{\varphi}
    15	\newcommand{\Lop}{L_{V_{600}}}
    16	\newcommand{\Cph}{C_{\Ph}}
    17	\newcommand{\Rsixhundred}{V_{600}}
    18	
    19	\title{A geometry-fixed substrate witness for cortical signatures:\\
    20	       eighteen preregistered correspondences and six drug/sleep EEG\\
    21	       signatures from the 600-cell under H$_4$ Coxeter symmetry}
    22	
    23	\author{%
    24	  Lee Smart\\[2pt]
    25	  \textit{Institute of Vibrational Field Dynamics}\\[2pt]
    26	  \texttt{contact@vibrationalfielddynamics.org}\\[2pt]
    27	  \texttt{@vfd\_org}%
    28	}
    29	
    30	\date{April 2026}
    31	
    32	\begin{document}
    33	
    34	\maketitle
    35	
    36	\noindent\textbf{Status:} Preprint, not peer-reviewed.
    37	
    38	\noindent\emph{Headline.}
    39	Once the 600-cell substrate is chosen, its graph structure is fixed by
    40	group theory: $120$ vertices of uniform degree $12$, Laplacian
    41	eigenvalues $\{0, 3, 4\Ph, 6\Ph, 12\!-\!4\Ph, 12\!-\!6\Ph, 12\!-\!3, 12\}$
    42	in their H$_4$-irrep multiplicities, with $\Ph=(1+\sqrt 5)/2$. Treated
    43	as an architectural-level substrate with a fixed shifted-Laplacian
    44	response $\Cph = \Lop + \Ph^{-2} I$ and a small dynamical layer above
    45	it, this single deterministic structure is consistent with eighteen
    46	quantitative correspondences with neuroscience data — preregistered
    47	on 2026-04-18 before any validation run — plus six drug/sleep EEG
    48	signatures of conscious vs unconscious states tested against
    49	published-reference thresholds on a single deterministic substrate
    50	trajectory at seed~$42$. No shape parameter is tuned to any neural
    51	dataset. The recurrent layer above the substrate adds one
    52	substrate-pinned nonlinearity $\mathrm{bounded\_topk}(\cdot, k\!=\!12)$
    53	at the graph's average degree and one condition-dependent self-injection
    54	coupling $\eta\!\in\!\{0, 0.05, 0.20\}$; condition-specific stimulus
    55	models (\S\ref{sec:chain}) are biologically-motivated design choices,
    56	not measurement-fits.
    57	
    58	\noindent\emph{Scope.}
    59	This paper presents an empirical \emph{substrate witness}: it shows
    60	that a geometry-fixed substrate, with no shape parameters tuned to any
    61	neural dataset, is consistent with eighteen preregistered correspondences
    62	and six EEG signatures. It is not a derivation of consciousness, nor a
    63	selection theorem, nor a uniqueness claim for the 600-cell among regular
    64	4-polytopes. The companion adaptive-closure-transport
    65	preprint~\citep{SmartAdaptiveClosureTransport2026} provides the
    66	4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which this substrate
    67	sits as the $L_M$ instance; the selection of the 600-cell as the active
    68	$M$ is treated as conjectural and is not load-bearing here.
    69	
    70	\begin{abstract}
    71	We test whether a geometry-fixed substrate — the 600-cell regular
    72	4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
    73	shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
    74	operator — is consistent with cortical signatures across five
    75	neuroscience domains. Eighteen quantitative predictions were
    76	preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
    77	before any validation run; each has a falsifiable threshold. The
    78	preregistered tally is $17/18$ at standard validation methodology
    79	($5$-seed cascade block plus state-reset protocol), and $18/18$ after
    80	a documented $N\!=\!20$ deep-dive on the residual high-variance
    81	interaction (P4); no preregistered threshold has been modified. We
    82	additionally report six drug/sleep EEG signatures tested on a recurrent
    83	self-model layer above the substrate, on a single deterministic
    84	trajectory at seed~$42$. The six signatures are not part of the
    85	P1--P18 preregistration; they are tested against published-reference
    86	thresholds (Sleep-EDFx, OpenNeuro, Brodbeck, Tononi) and were obtained
    87	under condition-specific stimulus models redesigned at v4 to be
    88	biologically realistic (\S\ref{sec:chain}).
    89	
    90	\noindent\emph{(i) Cortical avalanches.}
    91	Wake cascade-event power-law exponent $\alpha = 2.252$,
    92	$95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$, $n_{\mathrm{events}}=58$).
    93	This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
    94	subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
    95	pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
    96	overlap.
    97	
    98	\noindent\emph{(ii) Drug/sleep state transitions.}
    99	NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
   100	(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
   101	ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
   102	reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
   103	propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
   104	integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
   105	direction confirmed); recovery deterministically identical to wake.
   106	All six signatures pass against their published-reference thresholds
   107	on the single deterministic substrate trajectory.
   108	
   109	\noindent\emph{(iii) Causal mechanism isolation.}
   110	Two of four cascade mechanisms — context rotation $C$ and partial
   111	emission $P$ — are causally identifiable within the factorial
   112	ablation model, and the original preregistered C$\times$P synergy
   113	prediction $\geq +0.10$ closes
   114	decisively at adequate replication: $N\!=\!20$ fresh seeds give a
   115	bootstrap point estimate of $+0.190$ with $95\%$ CI $[+0.143, +0.239]$
   116	(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
   117	below zero, reported as $0.0000$. We document the original $N\!=\!3$
   118	underestimate ($+0.044$) as consistent with an underpowered interaction
   119	estimate at $N\!=\!3$ and contribute the $N\!\geq\!20$ minimum as a
   120	preregistration-practice recommendation for high-variance interaction
   121	terms.
   122	
   123	\noindent\emph{(iv) Cross-domain selectivity.}
   124	The substrate exhibits selective amplification in the two cross-domain
   125	tasks tested: chess 4-category position classification on
   126	8-dimensional V2 features lifts $+40.6$ percentage points on
   127	leave-one-out at canonical depth $n\!=\!25$ ticks (raw $53.1\%$
   128	$\to$ substrate-routed $93.8\%$, with state reset; the
   129	preregistered estimator P13 was $5$-fold CV with threshold
   130	$\geq\!+15$pp, the LOO finding above is a stricter validation-protocol
   131	refinement at the same threshold), while conversation utterance
   132	classification at raw $87.5\%$ yields a substrate lift of $-4.4$pp
   133	(threshold $|\cdot| < 10$pp), consistent with the substrate
   134	amplifying in these two tasks where raw features are ambiguous and
   135	remaining approximately neutral when raw features are already
   136	discriminative. On HCP brain functional connectivity
   137	(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
   138	descriptive statistics), the H$_4$-transitive substrate is a
   139	maximum-symmetry deterministic null reference: ARIA degree std
   140	$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
   141	on degree homogeneity, $+79.78\sigma$ on participation ratio, and
   142	$+6.80\sigma$ on clustering coefficient.
   143	
   144	\noindent\emph{What we do not claim.}
   145	We do not claim the 600-cell is the unique substrate consistent with
   146	these signatures, nor that other regular 4-polytopes (24-cell, 120-cell)
   147	have been ruled out. We do not derive the $\Ph^{-2}$ floor from
   148	first principles; it is a design-level stability clamp on the
   149	shifted-Laplacian response. The recurrent layer above the substrate
   150	is reported on a single deterministic trajectory; cross-seed CIs on
   151	the per-condition signatures are an explicit strengthening build.
   152	The structural scope of this paper is: \emph{a geometry-fixed
   153	substrate, with no shape parameters tuned to any neural dataset,
   154	is consistent with eighteen preregistered neuroscience
   155	correspondences and six drug/sleep EEG signatures, with all gaps in
   156	the original preregistration closed by methodology refinement and
   157	without modifying any preregistered threshold.}
   158	\end{abstract}
   159	
   160	% =====================================================================
   161	\input{sections/01_introduction.tex}
   162	\input{sections/02_method.tex}
   163	\input{sections/03_substrate.tex}
   164	\input{sections/04_consciousness_chain.tex}
   165	\input{sections/05_results.tex}
   166	\input{sections/06_stress_tests.tex}
   167	\input{sections/07_cross_domain.tex}
   168	\input{sections/08_discussion.tex}
   169	\input{sections/09_limitations.tex}
   170	\input{sections/10_conclusion.tex}
   171	% =====================================================================
   172	
   173	\section*{Acknowledgements}
   174	We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
   175	OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
   176	the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
   177	the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
   178	HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
   179	datasets that made these comparisons possible. Cortical avalanche
   180	methodology follows~\citep{BeggsPlenz2003}; the integrated-information
   181	$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
   182	the propofol microstate comparison uses Brodbeck et
   183	al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
   184	follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
   185	and processed data are released under MIT licence at the project
   186	repository~\citep{ariaChessRepo}.
   187	
   188	\section*{Reproducibility}
   189	The complete pipeline (substrate construction, six-signature
   190	consciousness chain, $N\!=\!20$ C$\times$P deep-dive, eighteen-prediction
   191	preregistered validation, figure regeneration, this paper) is reproducible
   192	from the project repository~\citep{ariaChessRepo} via the included
   193	\texttt{reproduce\_paper\_claims.sh} script. All scripts are
   194	deterministic given seeds; the substrate's spectral decomposition is
   195	cached at module level. Wallclocks: drug/sleep v4 $\sim 30$\,s;
   196	$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
   197	$\sim 18$\,min.
   198	
   199	\bibliographystyle{plainnat}
   200	\bibliography{references}
   201	
   202	\end{document}

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 250ms:
     1	% =====================================================================
     2	\section{The 600-cell response substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section constructs the substrate. \S\ref{ssec:vertices}
     6	gives the vertex set. \S\ref{ssec:graph} gives the graph and its
     7	H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
     8	operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
     9	\S\ref{ssec:shells} gives the 9-shell decomposition used for source
    10	projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
    11	descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
    12	of these objects depend on neural data.
    13	
    14	\subsection{Vertex construction}\label{ssec:vertices}
    15	
    16	The 600-cell $\Rsixhundred$ has $120$ vertices in
    17	$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    18	With $\Ph = (1+\sqrt 5)/2$ the canonical vertex set is
    19	\begin{itemize}\itemsep=1pt
    20	\item $8$ vertices: all permutations of $(\pm 1, 0, 0, 0)$;
    21	\item $16$ vertices: all sign combinations of
    22	  $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    23	\item $96$ vertices: all even permutations of
    24	  $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$.
    25	\end{itemize}
    26	All $120$ vertices lie on the unit $3$-sphere $S^{3}$. The H$_4$
    27	Coxeter group acts transitively on the vertex set; in particular,
    28	every vertex has identical local structure. Implementation:
    29	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
    30	
    31	\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
    32	
    33	The substrate graph $G_{V_{600}} = (V, E)$ is built by connecting each
    34	vertex to its nearest neighbours under the Euclidean metric on $S^{3}$.
    35	H$_4$ acts transitively on the vertex set, forcing uniformity of the
    36	local structure; the eigenvalue multiplicities follow from H$_4$
    37	character theory on the regular representation. The construction and
    38	spectrum are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    39	\begin{lemma}[600-cell graph facts]\label{lem:600cell}
    40	The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, every
    41	vertex has degree exactly $12$, and the unweighted graph Laplacian
    42	$\Lop = D - A$ has spectrum
    43	\[
    44	\sigma(\Lop) \;=\;
    45	\bigl\{0^{1}, 3^{4}, 4\Ph^{9}, 6\Ph^{16}, (12\!-\!4\Ph)^{9},
    46	       (12\!-\!6\Ph)^{16}, 9^{4}, 12^{1}\bigr\},
    47	\]
    48	where the exponent denotes multiplicity. The decomposition into H$_4$
    49	irreducible representations is exact at machine precision; the
    50	$\sigma$-orbit projector basis (\texttt{kernel/sigma\_orbit\_basis.py})
    51	realises it block-by-block with cross-block norm $<10^{-15}$.
    52	\end{lemma}
    53	
    54	The non-trivial eigenmodes partition into Coxeter exponent classes.
    55	For H$_4$ proper, the exponents are $\{1, 11, 19, 29\}$; for the
    56	Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism of
    57	$\mathbb{Z}[\Ph]$, the exponents become $\{7, 13, 17, 23\}$. We label
    58	the eigenspaces $K_{1}, K_{11}, K_{19}, K_{29}$ for H$_4$-proper modes
    59	and $K_{7}, K_{13}, K_{17}, K_{23}$ for $\sigma$-twin modes. The
    60	multiplicities follow from character theory and are reproduced in
    61	the implementation
    62	(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}). The
    63	$K_{7}$-modes will be the dominant phenomenal-binding profile in
    64	\S\ref{sec:chain}.
    65	
    66	\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
    67	
    68	The substrate's linear response to an external source $f \in \mathbb{R}^{120}$
    69	is the discrete Green's function of the shifted Laplacian:
    70	\begin{equation}\label{eq:cphi}
    71	\Cph \;=\; \Lop + \Ph^{-2} I,
    72	\qquad
    73	\psi \;=\; \Cph^{-1} f.
    74	\end{equation}
    75	The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
    76	clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
    77	$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
    78	inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
    79	\emph{not} a derived theorem; it is a stability choice. The companion
    80	kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
    81	$\Cph$ as the basis for an independent passive-regime witness in
    82	flavour physics~\citep{SmartBAnomaly2026}, where the same operator
    83	form (without retuning the shift) describes the
    84	$B\to K^{*}\mu^{+}\mu^{-}$ angular anomaly across five public datasets.
    85	This paper imports $\Cph$ from that line; we do not re-derive it.
    86	
    87	The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
    88	not produce critical-state cascade statistics; the recurrent layer
    89	in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
    90	$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
    91	event distributions. The choice $k\!=\!12$ is the average degree of
    92	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
    93	fitted to any dataset.
    94	
    95	\paragraph{Disclosure (substrate-witness scope).}
    96	The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
    97	The bounded-top-$K$ nonlinearity uses $k\!=\!12$ pinned to the graph's
    98	average degree, not a fitted threshold. No other shape parameter
    99	enters. The condition-dependent self-injection coupling
   100	$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
   101	varies between conditions in~\S\ref{sec:chain}; it is reported
   102	explicitly per condition.
   103	
   104	\subsection{Shell decomposition}\label{ssec:shells}
   105	
   106	Under the H$_3$ subgroup, the $120$ vertices partition into $9$
   107	spherical shells indexed by Euclidean inner product with a chosen pole:
   108	\[
   109	\bigl(|S_0|,\ldots,|S_8|\bigr) \;=\; (1, 12, 20, 12, 30, 12, 20, 12, 1).
   110	\]
   111	The middle shell $S_{4}$ has $30$ vertices on the equatorial plane
   112	(the icosidodecahedral ring). When projecting onto a continuum kernel
   113	in companion preprints~\citep{SmartAriaClosureKernel2026}, the
   114	shell-mean projection of the equatorial-source response,
   115	$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
   116	collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
   117	This paper does not use that continuum projection; we work with the
   118	discrete operator throughout.
   119	
   120	\subsection{Cascade descent (sketch)}\label{ssec:cascade}
   121	
   122	The recurrent layer in~\S\ref{sec:chain} references a cascade
   123	decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
   124	\to S^{7}\to 0$, implemented in
   125	\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
   126	An arbitrary operator on the $E_{8}$ root system descends to the
   127	4-D H$_4$ subspace through a sequence of orthogonal projections, each
   128	preserving the Frobenius norm to within $10^{-15}$. The
   129	$\sigma$-orbit projector basis from
   130	\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
   131	decomposition at machine precision.
   132	
   133	The descent provides numerical stability for the cascade ablations:
   134	when one ablates a specific K-class contribution (e.g.\ $K_{7}$), the
   135	remaining operator structure is exactly preserved. We do not claim
   136	the cascade itself is forced by physics on a pre-substrate level; the
   137	cascade is a decomposition of operators on $\Rsixhundred$, and the
   138	choice of $\Rsixhundred$ as the active substrate is post-hoc justified
   139	by the empirical correspondences in~\S\ref{sec:results}.
   140	
   141	\subsection{What the substrate is fixed-by, and what it is not}
   142	
   143	\begin{itemize}\itemsep=2pt
   144	\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
   145	  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
   146	  irrep block structure, average degree $k\!=\!12$, $\sigma$-twin pairing.
   147	\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
   148	  is not a derivation; it is a design-level clamp that bounds the
   149	  response inverse.
   150	\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
   151	  $24$-cell or $120$-cell. The choice is post-hoc motivated by the H$_4$
   152	  cascade structure and the empirical correspondences. A formal
   153	  ablation against alternative regular 4-polytopes is an open build
   154	  (\S\ref{sec:limitations}).
   155	\end{itemize}

 succeeded in 237ms:
     1	% =====================================================================
     2	\section{The recurrent layer}\label{sec:chain}
     3	% =====================================================================
     4	
     5	The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
     6	cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
     7	To test high-level signatures — NREM-N3 variance collapse, propofol
     8	regime-switching, propofol $\Phi$ collapse — we add a recurrent
     9	self-model layer above the substrate. The layer adds one
    10	graph-pinned nonlinearity, one condition-dependent self-injection
    11	coupling $\eta$, and four trajectory observables. No shape parameter
    12	is fit to any neural dataset.
    13	
    14	This section is method, not metaphysics. We do not claim the
    15	recurrent layer ``is'' consciousness; we report which numerical
    16	observables on the layer's trajectory match published biological
    17	signatures in~\S\ref{sec:results}.
    18	
    19	\subsection{The recurrent loop}
    20	
    21	Implementation: \texttt{kernel/self\_model\_stream.py:SelfModelLoop}.
    22	At each tick $t$ the substrate state evolves as
    23	\begin{align}
    24	f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
    25	\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
    26	\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
    27	\mathrm{state}_{t} &= \mathrm{decay}\cdot\mathrm{state}_{t-1} + (1-\mathrm{decay})\cdot \psi^{\mathrm{thr}}_{t}, \\
    28	\mathrm{snap}_{t} &= \mathrm{bind\_phenomenal\_field}(\psi_{t}, \texttt{profile=K\_7\_only}),
    29	\end{align}
    30	with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
    31	condition-dependent architectural parameter. $f_{\mathrm{self}}$ maps
    32	the prior phenomenal snapshot to a directional source weighted by
    33	ignition $\times$ intensity (cosine direction alignment with the
    34	prior snapshot). The substrate response operator $\Cph$ is unchanged
    35	across all conditions.
    36	
    37	Conditions:
    38	\begin{itemize}\itemsep=2pt
    39	\item $\eta = 0.20$ for WAKE and RECOVERY (active recurrent self-loop);
    40	\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
    41	\item $\eta = 0.00$ for PROPOFOL (broken recurrence; residual cortex
    42	  preserved as background drive).
    43	\end{itemize}
    44	
    45	\subsection{The graph-pinned nonlinearity}
    46	
    47	\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
    48	nonlinearity, implemented in
    49	\texttt{kernel/lyapunov\_selector.py:bounded\_topk}: zero all but the
    50	top-$12$ vertex amplitudes (by absolute value), and rescale the rest
    51	to a small fraction of their baseline. Linear Green response alone
    52	gives smooth dynamics with cascade $\alpha\approx 1.09$ — no
    53	avalanches. Adding bounded-top-$K$ at $k=12$ drives $\alpha$ into the
    54	SOC band $(2.0, 3.5)$ with $R^{2}>0.85$.
    55	
    56	\textbf{Why $k=12$.} The choice $k=12$ is the average degree of
    57	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
    58	geometry, not by neural data. Smaller $k$ (e.g.\ $k=6$) gives $\alpha$
    59	at the band edge with poorer fit; larger $k$ ($24, 48$) gives $\alpha$
    60	above band or with degraded fit. We do not search $k$ over a fitted
    61	window; $k$ is determined by the graph.
    62	
    63	\subsection{The integrated-information proxy
    64	            \texorpdfstring{$\Phi$}{Phi}}
    65	
    66	Implementation:
    67	\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
    68	Given the state history matrix $S\in\mathbb{R}^{T\times 120}$, write
    69	$A = S\cdot V$ for the H$_4$-eigenvector matrix $V$ (mode amplitudes
    70	$A\in\mathbb{R}^{T\times 120}$). Define $c_{\mathrm{full}}$ as the
    71	lag-$1$ auto-correlation of the full system, and $c_{k}$ as the
    72	lag-$1$ auto-correlation within the K-class irrep block $k$. Then
    73	\[
    74	\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
    75	\]
    76	The proxy is designed to be small under H$_{4}$-equivariant dynamics
    77	(when block autocorrelations within irrep classes match the full-system
    78	autocorrelation) and to increase when dynamics produce cross-class
    79	asymmetries. It is not a theorem on information transport; it is a
    80	proxy that captures one observable signature of cross-class
    81	non-equivariance. This is a port of the published
    82	\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
    83	pipeline, adapted to take amplitude trajectories from any source.
    84	
    85	We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
    86	a full implementation of IIT. ARIA does not implement cause-effect
    87	repertoires, exclusion postulate, or integration-over-partitions
    88	machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
    89	collapse in~\S\ref{sec:results} is consistent with the IIT direction
    90	of effect on the propofol-vs-wake state contrast; it is not a
    91	discharge of the IIT axioms.
    92	
    93	\subsection{The continuity composite}
    94	
    95	Implementation:
    96	\texttt{kernel/self\_model\_stream.py:StreamContinuityScorer}.
    97	A composite first-person continuity score over a 64-tick rolling
    98	window:
    99	\begin{align*}
   100	b_{\mathrm{cont}} &= \mathrm{mean\ cos\text{-}sim\ of\ consecutive}\ (I, L, P)\,\mathrm{vectors},\\
   101	v_{\mathrm{cont}} &= 1/(1 + 4\cdot \mathrm{var}(\mathrm{valence})),\\
   102	m_{\mathrm{pers}} &= \mathrm{frac.\ of\ consecutive\ same\text{-}modality\ ticks},\\
   103	i_{\mathrm{smooth}} &= 1/(1 + 4\cdot \mathrm{TV}(\mathrm{intensity})),\\
   104	\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
   105	\end{align*}
   106	This composite produces the propofol continuity-drop signature
   107	(WAKE composite $0.943$; PROPOFOL composite $0.877$;
   108	drop $+0.066$).
   109	
   110	\subsection{The phenomenal-field binding}
   111	
   112	Implementation:
   113	\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
   114	The substrate state $\psi_{t}$ is mapped to a phenomenal snapshot
   115	with channels (intensity $I$, self-luminosity $L$, presence $P$,
   116	valence, modality\_label). The modality\_label is determined by which
   117	H$_4$ K-class dominates the isotypic compression of $\psi_{t}$ under
   118	the $\sigma$-orbit projector basis. The default profile
   119	\texttt{K\_7\_only} restricts to $\sigma$-twin K-classes for modality
   120	labelling; H$_4$-proper classes contribute amplitude bias.
   121	
   122	\subsection{Stimulus models}
   123	
   124	Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
   125	$\times$ $800$ ticks each at seed $42$:
   126	
   127	\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
   128	coherence (small always-on bias), and attention episodes (20--50
   129	ticks at amplitude $0.8$, anchored to the largest shell with $15\%$
   130	within-shell rotation per tick). The AR(1) gives temporal correlation
   131	that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
   132	modality; attention episodes mimic biological visual fixation
   133	(200--400~ms dwell time analogue); within-shell rotation generates
   134	cascade events without changing modality.
   135	
   136	\textbf{SLEEP\_N3.} Slow oscillation ($\sim 1$\,Hz analogue,
   137	amplitude $1.0$) on a coherent shell, plus spindle bursts ($12$ ticks
   138	every $100$ at amplitude $0.4$ fast modulation), plus K-complexes
   139	($4\%$ of ticks at amplitude $0.8$).
   140	
   141	\textbf{PROPOFOL.} Low-amplitude tonic noise (amplitude $0.05$);
   142	$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
   143	background drive.
   144	
   145	\textbf{RECOVERY.} Identical to WAKE — verifies deterministic
   146	repeatability under the WAKE stimulus protocol after exposure to
   147	PROPOFOL (no hidden persistent modification of the substrate state).
   148	
   149	The stimulus models are deliberately structural rather than
   150	measurement-fitted: amplitudes and durations match published
   151	biological time scales but are not tuned to specific signatures.
   152	The full stimulus code is \texttt{demo\_drug\_sleep\_v4.py}. We
   153	disclose stimulus-shape choice as a methodological design move,
   154	not a derived theorem.
   155	
   156	\subsection{Cascade-mechanism ablation matrix}
   157	
   158	The cascade dynamics on the substrate use four mechanisms acting on
   159	the pressure field, each ablatable independently. The $2^{4}$
   160	ablation grid is the basis for the preregistered tests P1--P5 and
   161	the C$\times$P stress test in~\S\ref{sec:stress}.
   162	
   163	\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains
   164	five disjoint 24-cells (D$_4$ orbits). $D$ adds a small
   165	(coupling $0.05$) cross-orbit pressure averaging that prevents
   166	cascades from localising to one orbit.
   167	Implementation: \texttt{kernel/dimensional\_monitor.py:300-305}.
   168	
   169	\textbf{$C$ — Context rotation (S$^{7}$ observer frames).} The active
   170	observer frame on the S$^{7}$ rung rotates periodically based on
   171	which uncrossed vertices have accumulated pressure aligning with
   172	each frame's preferences. This creates churn in \emph{which}
   173	vertices are uncrossed at any tick.
   174	Implementation: \texttt{kernel/dimensional\_monitor.py:316-318, 823-827}.
   175	
   176	\textbf{$P$ — Partial emission.} High-pressure uncrossed vertices
   177	(above threshold but not yet crossed) emit pressure at $30\%$ scale,
   178	saturating at pressure $3.0$. Without this mechanism, only fully-
   179	crossed vertices emit.
   180	Implementation: \texttt{kernel/dimensional\_monitor.py:842-855}.
   181	
   182	\textbf{$E$ — Equator compensation.} The H$_3$ shell-4 equator is a
   183	30-vertex icosidodecahedral ring with split degree distribution.
   184	$E$ scales pressure gain by $(\bar d / d_{v})$ so sparse commissural
   185	vertices overcome their connectivity deficit.
   186	Implementation: \texttt{kernel/dimensional\_monitor.py:320-360}.
   187	
   188	The four mechanisms are pinned to the substrate's geometry (D$_4$
   189	orbits, S$^{7}$ rung, equatorial shell) — they are not free dynamical
   190	choices. Their causal effects are reported in~\S\ref{sec:stress}.

 succeeded in 291ms:
     1	% =====================================================================
     2	\section{Results}\label{sec:results}
     3	% =====================================================================
     4	
     5	This section is the empirical core. \S\ref{ssec:six_signatures}
     6	gives the six drug/sleep EEG signatures on the recurrent layer
     7	(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
     8	preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
     9	gives the three-way $\alpha$ overlap. We lift the result map
    10	$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
    11	verdict)}$ verbatim from the validation outputs without
    12	recomputation; sources are
    13	\texttt{docs/brain\_mapping/CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    14	and \texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
    15	
    16	\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
    17	
    18	\textbf{Setup.} Four conditions $\times$ $800$ ticks at seed $42$,
    19	$k_{\mathrm{thr}}=12$, single deterministic substrate
    20	(\S\ref{sec:chain}). Per-condition trajectory observables are
    21	$(n_{\mathrm{evt}}, \alpha, \mathrm{CI}_{95}, R^{2}, I_{\mathrm{var}},
    22	\Phi_{\mathrm{traj}}, \mathrm{cont})$.
    23	
    24	\begin{table}[ht]
    25	\centering
    26	\small
    27	\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
    28	seed 42).}
    29	\label{tab:per_condition}
    30	\begin{tabular}{l r r l r r r r}
    31	\toprule
    32	condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
    33	\midrule
    34	WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
    35	SLEEP\_N3 & $111$ & $3.250$ & $[2.44, 4.14]$ & $0.886$ & $1.01\!\times\!10^{-5}$ & $0.0055$ & $0.980$ \\
    36	PROPOFOL  & $246$ & $2.758$ & $[2.52, 3.09]$ & $0.931$ & $5.37\!\times\!10^{-6}$ & $0.0003$ & $0.877$ \\
    37	RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
    38	\bottomrule
    39	\end{tabular}
    40	\end{table}
    41	
    42	\begin{table}[ht]
    43	\centering
    44	\small
    45	\caption{Six drug/sleep signatures with published references.}
    46	\label{tab:six_signatures}
    47	\begin{tabular}{c l l c c l}
    48	\toprule
    49	\# & Signature & Reference & Predicted & Observed & Verdict \\
    50	\midrule
    51	1 & NREM-N3 var ratio (vs Wake) &
    52	   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
    53	   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
    54	2 & Propofol switching ratio &
    55	   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
    56	   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
    57	3 & Propofol continuity drop &
    58	   EEG microstate~\citep{Brodbeck2012Microstates} &
    59	   $> 0.020$ & $+0.066$ & $\checkmark$ \\
    60	4 & Propofol $\Phi$ collapse (IIT) &
    61	   Tononi 2008~\citep{Tononi2008} &
    62	   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
    63	5 & Recovery reversibility &
    64	   clinical anaesthesia &
    65	   identical to wake & $0$ diff & $\checkmark$ \\
    66	6 & Wake cortical-avalanche $\alpha$ &
    67	   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
    68	   $\alpha\!\in\![1.5, 3.5]$, $R^{2}\!>\!0.85$ &
    69	   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
    70	   $\checkmark$ \\
    71	\bottomrule
    72	\end{tabular}
    73	\end{table}
    74	
    75	All six signatures pass against their published-reference thresholds
    76	on the same deterministic substrate trajectory. The six signatures
    77	are not part of the dated 2026-04-18 P1--P18 preregistration; they
    78	were tested on a recurrent-layer architecture redesigned at v4 with
    79	biologically-motivated condition-specific stimulus models
    80	(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    81	documents the v3$\to$v4 stimulus redesign). The mechanistic readings
    82	in \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} are not
    83	load-bearing for the headline claim. Single-seed disclosure:
    84	\S\ref{sec:limitations}~\ref{ssec:regime}.
    85	
    86	\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
    87	
    88	\textbf{Tally.} $17/18$ at standard validation
    89	(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
    90	plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
    91	on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
    92	$32000$--$32019$). \emph{No preregistered threshold has been modified.}
    93	
    94	\begin{table}[ht]
    95	\centering
    96	\small
    97	\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
    98	\label{tab:eighteen_prereg}
    99	\begin{tabular}{l l l l l}
   100	\toprule
   101	ID & Test & Threshold & Observed (2026-04-29) & Verdict \\
   102	\midrule
   103	P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
   104	P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
   105	P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
   106	\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
   107	   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
   108	P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
   109	P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
   110	P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
   111	P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
   112	P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
   113	P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
   114	P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
   115	P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
   116	\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
   117	P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
   118	P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   119	P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
   120	P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
   121	P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
   122	\bottomrule
   123	\end{tabular}
   124	\end{table}
   125	
   126	\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
   127	estimator as $5$-fold CV at threshold $\geq +15$pp; the 2026-04-29
   128	validation tightened the estimator to LOO with state reset, a
   129	stricter test at the unchanged $+15$pp threshold. See
   130	\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
   131	
   132	\textbf{Three predictions that flipped to PASS, with documented
   133	methodology refinement (no threshold change).}
   134	\begin{itemize}\itemsep=2pt
   135	\item P3 (D$\times$C interaction independence) was outside the band
   136	  at $N\!=\!3$ ($-0.231$) and inside the band at $N\!=\!5$ ($-0.183$).
   137	  Reading: consistent with an underpowered interaction estimate at
   138	  $N\!=\!3$ on a high-per-seed-variance interaction term.
   139	\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
   140	  ($+0.044$) and at $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
   141	  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
   142	  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
   143	\item P13 (chess substrate lift): the 2026-04-18 preregistration
   144	  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
   145	  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
   146	  validation strengthened the estimator to LOO with state reset, a
   147	  stricter test at the same threshold; the LOO lift was $+3.1$pp
   148	  without state reset on a state-drifted substrate, and $+40.6$pp
   149	  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
   150	  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
   151	  report this as a \emph{validation-protocol refinement relative to
   152	  the preregistered test}, not as preregistration revision.
   153	\end{itemize}
   154	
   155	\textbf{Headline verdict.} Eighteen preregistered correspondences
   156	all pass at preregistered thresholds, with two interaction tests
   157	requiring $N\!\geq\!5$ and one requiring $N\!=\!20$ for reliable
   158	detection of high-variance interaction terms, and one test
   159	requiring the documented state-reset protocol. The original $15/18$
   160	result was a methodology-limited tally, not a content failure.
   161	
   162	\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
   163	
   164	The substrate's wake cascade-$\alpha$ confidence interval overlaps
   165	\emph{three independent reference ranges} simultaneously:
   166	
   167	\begin{table}[ht]
   168	\centering
   169	\small
   170	\caption{Three-way $\alpha$ overlap on the wake cascade-event power
   171	law.}
   172	\label{tab:alpha_overlap}
   173	\begin{tabular}{l c l c}
   174	\toprule
   175	Source & $\alpha$ & 95\% CI & $n$ \\
   176	\midrule
   177	ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
   178	Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
   179	ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
   180	\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
   181	\bottomrule
   182	\end{tabular}
   183	\end{table}
   184	
   185	The v4 WAKE 95\% CI $[1.82, 2.86]$ contains the upper arm of the
   186	real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
   187	cascade pipeline CI $[2.73, 3.25]$ on the interval $[2.73, 2.86]$,
   188	and lies inside the cortical-avalanche band
   189	$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
   190	intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
   191	WAKE $\cap$ cortical-avalanche band) are non-empty across three
   192	independent reference ranges.
   193	
   194	\textbf{Reading.} The substrate produces self-organised-critical
   195	cascade statistics matching the cortical-avalanche literature with
   196	no fitted parameter on neural data. The bounded-top-$K$ at
   197	$k=12$ is pinned to the substrate's average degree
   198	(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
   199	stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
   200	biological time-scale parameters but is not measurement-fitted to
   201	any specific subject (\S\ref{sec:chain}). Three-way overlap on the
   202	power-law exponent is the strongest single empirical anchor in the
   203	paper.

codex
The manuscript is broadly observing the substrate-witness boundary, but I’ve already found two likely round-2 leftovers in the introduction: “six independent” and “domain-invariant selective amplifier.” I’m checking whether those are isolated wording issues or signs of deeper inconsistency.
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 293ms:
     1	% =====================================================================
     2	\section{Stress test: the C\texorpdfstring{$\times$}{x}P synergy at adequate
     3	         replication}\label{sec:stress}
     4	% =====================================================================
     5	
     6	This section is the C$\times$P interaction stress test. The original
     7	preregistered prediction was P4: $C\times P$ interaction
     8	$\Delta_{CP} \geq +0.10$ on cascade-$\alpha$. The 2026-04-20
     9	$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
    10	architectural claim ``C and P synergise on cascade-state stability''
    11	was walked back. Closing this gap without modifying the preregistered
    12	threshold required (a) re-evaluating the $N\!=\!3$ point estimate as
    13	consistent with an underpowered interaction estimate, (b) tracking
    14	the estimate's behaviour across $N$, and (c) bootstrapping a
    15	confidence interval on a fresh-seed $N\!=\!20$ sample. We did all
    16	three.
    17	
    18	\subsection{The factorial estimator}
    19	
    20	For the four ablation conditions $\{----, -C--, --P-, -CP-\}$
    21	(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
    22	standard $2\times 2$ factorial difference:
    23	\[
    24	\Delta_{CP}
    25	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
    26	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
    27	\]
    28	Per-seed paired estimates use the same formula on a single seed's
    29	four conditions.
    30	
    31	\subsection{The trend across \texorpdfstring{$N$}{N}}
    32	
    33	\begin{table}[ht]
    34	\centering
    35	\small
    36	\caption{$C\times P$ interaction estimate as a function of $N$.}
    37	\label{tab:cxp_trend}
    38	\begin{tabular}{r l r l l}
    39	\toprule
    40	$N$ & Seeds & Estimate $\Delta_{CP}$ & 95\% CI & Verdict vs $\geq +0.10$ \\
    41	\midrule
    42	$3$  & $30040$--$30042$ & $+0.044$ & --- & $\times$ original prereg \\
    43	$5$  & $30040$--$30044$ & $+0.039$ & --- & $\times$ this session re-run \\
    44	$10$ & $31000$--$31009$ & $+0.088$ & $[-0.002, +0.174]$ & borderline \\
    45	$\mathbf{20}$ & $\mathbf{32000\text{--}32019}$ & $\mathbf{+0.190}$
    46	       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
    47	\bottomrule
    48	\end{tabular}
    49	\end{table}
    50	
    51	The estimate remains small at $N\!=\!3$ and $N\!=\!5$
    52	($+0.044, +0.039$) and rises at $N\!=\!10$ and $N\!=\!20$
    53	($+0.088, +0.190$). Per-seed std at $N\!=\!10$ was $0.159$; at
    54	$N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$ sample landed on
    55	outliers; the $N\!=\!20$ sample reveals a clean narrow positive
    56	distribution.
    57	
    58	\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
    59	
    60	\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
    61	$32000$--$32019$, non-overlapping with original validation seeds in
    62	the $30000$s), $150$ epochs per run. All other ablation flags off
    63	($D, E$ held on). Bootstrap $n_{\mathrm{resamples}}\!=\!2000$,
    64	seed $42$. Wallclock $1706$\,s on a single CPU
    65	(\texttt{demo\_p4\_cxp\_deep\_dive.py}).
    66	
    67	\textbf{Per-condition means at \texorpdfstring{$N\!=\!20$}{N=20}.}
    68	
    69	\begin{table}[ht]
    70	\centering
    71	\small
    72	\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
    73	\label{tab:cxp_means}
    74	\begin{tabular}{l r r r}
    75	\toprule
    76	condition & mean $\alpha$ & std & sem \\
    77	\midrule
    78	$----$ baseline    & $3.008$ & $0.090$ & $0.020$ \\
    79	$-C--$ (C off)     & $3.464$ & $0.097$ & $0.022$ \\
    80	$--P-$ (P off)     & $2.790$ & $0.086$ & $0.019$ \\
    81	$-CP-$ (both off)  & $3.628$ & $0.161$ & $0.036$ \\
    82	\bottomrule
    83	\end{tabular}
    84	\end{table}
    85	
    86	\textbf{Main effects at \texorpdfstring{$N\!=\!20$}{N=20}.}
    87	$C$ main effect $= +0.456$ (turning $C$ off raises $\alpha$);
    88	$P$ main effect $= -0.218$ (turning $P$ off lowers $\alpha$).
    89	
    90	\textbf{Interaction estimate.} Direct calculation from means:
    91	\[
    92	\Delta_{CP} \;=\; \frac{(3.628 + 3.008) - (3.464 + 2.790)}{2}
    93	            \;=\; +0.191.
    94	\]
    95	Bootstrap on the 20-seed sample (2000 resamples):
    96	\begin{itemize}\itemsep=1pt
    97	\item bootstrap mean $\Delta_{CP} = +0.190$;
    98	\item 95\% bootstrap CI $[+0.143, +0.239]$;
    99	\item $0/2000$ bootstrap resamples were at or below zero, reported as
   100	      $0.0000$;
   101	\item $0/2000$ bootstrap resamples were below the preregistered
   102	      $+0.10$ floor, reported as $0.0000$.
   103	\end{itemize}
   104	
   105	\textbf{Per-seed paired distribution.}
   106	$19/20$ seeds give a positive paired-interaction estimate (range
   107	$+0.055$ to $+0.322$); a single seed gives $-0.009$. No seed gives a
   108	strongly negative interaction.
   109	
   110	\subsection{Reading and disclosure}
   111	
   112	\textbf{The 95\% CI is entirely above the preregistered $+0.10$
   113	threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
   114	at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
   115	were below the preregistered $+0.10$ floor, reported as $0.0000$.
   116	
   117	\textbf{Architectural reading (substrate witness).} $C$ creates churn
   118	in \emph{which} vertices are uncrossed (frame rotation churns the
   119	uncrossed pool). $P$ promotes the high-pressure subset of the
   120	uncrossed pool to mini-emitters. The product is a non-additive
   121	novel-event-generation pathway: with both on, the uncrossed pool
   122	churns and $P$ amplifies new vertices entering the high-pressure
   123	region; with either off, the measured interaction collapses. The interaction
   124	$+0.19$ is comparable in magnitude to the $P$ main effect $-0.22$,
   125	so $C$ and $P$ are \emph{strongly coupled} cascade-state stabilisers
   126	on this substrate, not nearly-orthogonal ones. This reverses an
   127	architectural claim from the original 3-seed validation that held $C$
   128	and $P$ approximately orthogonal.
   129	
   130	\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
   131	was conducted \emph{after} the original $N\!=\!3$ failure
   132	(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
   133	selected to be non-overlapping with the original $30000$s seeds.
   134	Two strengthening builds we have not delivered:
   135	(i) a second independent $N\!=\!20$ run at a different seed range
   136	(e.g.\ $33000$--$33019$), and
   137	(ii) an $N\!=\!50$ characterisation of the per-seed sample
   138	distribution. Both are recorded as open builds in
   139	\S\ref{sec:limitations}.
   140	
   141	\textbf{What this stress test does \emph{not} establish.}
   142	\begin{itemize}\itemsep=2pt
   143	\item It does not establish a Lyapunov function on the reduced flow.
   144	\item It does not establish that the substrate is uniquely selected by
   145	  $C\times P$ coupling among regular 4-polytopes.
   146	\item It does not establish an $\eta$-trajectory derivation; $\eta$
   147	  is treated as a condition-dependent constant in this paper.
   148	\end{itemize}
   149	The stress test is what its name says: a high-replication factorial
   150	test of one preregistered interaction prediction, on a fresh-seed
   151	sample, with bootstrap confidence intervals. The architectural reading
   152	is a \emph{description} of what $C$ and $P$ do on the substrate, not a
   153	theorem about why they do it.
   154	
   155	\subsection{Methodological contribution}
   156	
   157	We document, as a methodological contribution to preregistration
   158	practice, that interaction terms in cascade ablation matrices require
   159	$N\!\geq\!20$ fresh seeds for reliable detection when the
   160	interaction-to-main-effect ratio is below $0.5$. The original 3-seed
   161	preregistered validation gave estimates consistent with underpowered
   162	detection on both interaction tests (P3 and P4); both close at higher
   163	$N$ without threshold modification. For preregistration design more broadly:
   164	when preregistering an interaction effect on a system with unknown
   165	per-seed variance, allocate the seed count from a power-analysis
   166	assumption that the per-seed std could be as large as the interaction
   167	effect itself. Under that assumption, $N\!\geq\!20$ is the conservative
   168	minimum.

 succeeded in 272ms:
     1	% =====================================================================
     2	\section{Discussion}\label{sec:discussion}
     3	% =====================================================================
     4	
     5	This section reads the substrate-witness result against existing
     6	theories of consciousness, identifies what is novel here that is not
     7	a re-statement of an earlier theory, and proposes a non-load-bearing
     8	ACT bridge to the companion adaptive-closure-transport
     9	preprint~\citep{SmartAdaptiveClosureTransport2026}. We do not claim a
    10	selection theorem, we do not claim a Lyapunov derivation, and we do
    11	not claim the recurrent layer ``is'' consciousness.
    12	
    13	\subsection{What is novel in this work}
    14	
    15	Three things are claimed novel as a substrate witness:
    16	\begin{enumerate}\itemsep=2pt
    17	\item \textbf{A geometry-fixed substrate that is consistent with
    18	  real-cortex EEG signatures without fitted shape parameters on neural
    19	  data.} The 600-cell + H$_4$ symmetry is fixed by group theory once
    20	  the substrate is chosen; cascade-$\alpha$ matches Sleep-EDFx within
    21	  preregistered tolerance with pairwise CI overlap on three reference
    22	  ranges; six drug/sleep signatures pass at published-reference
    23	  thresholds on a single deterministic substrate. We are not aware of
    24	  a prior geometric substrate that has been tested against this many
    25	  preregistered cortical correspondences from a graph fixed by group
    26	  theory; we cannot rule out that such a model exists.
    27	\item \textbf{The strong-coupling architectural finding.} $C$ and $P$
    28	  are strongly coupled cascade-state stabilisers, not
    29	  nearly-orthogonal ones. The $C\!\times\!P$ interaction
    30	  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
    31	  in magnitude to the $P$ main effect ($-0.218$). This was hidden by
    32	  underpowered ablation and emerged only at $N\!\geq\!20$ — a
    33	  substantive correction to the architectural reading from the
    34	  original 3-seed validation.
    35	\item \textbf{The 18/18 preregistered correspondences with no
    36	  threshold modification.} Every prediction in the preregistered set
    37	  passes at the preregistered thresholds. The two interaction tests
    38	  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
    39	  one test (P13) required the documented state-reset protocol. We
    40	  report this transparently as methodology refinement, not as
    41	  threshold change.
    42	\end{enumerate}
    43	
    44	\subsection{Comparison to existing theories of consciousness}
    45	
    46	\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
    47	IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
    48	wake). The H$_4$-equivariance argument
    49	(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
    50	group-symmetric, and $\Phi > 0$ only when dynamics break symmetry.
    51	ARIA does not implement the full IIT axioms (cause-effect repertoires,
    52	exclusion postulate, integration-over-partitions); it reproduces the
    53	observable consequence on the propofol--wake state contrast. This is
    54	a consistency-of-direction result, not a discharge of IIT.
    55	
    56	\textbf{vs Global Workspace Theory.}~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
    57	The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
    58	functionally analogous to a workspace with rotating attentional
    59	selection; the active observer frame plays the role of a temporary
    60	in-workspace subset of features. ARIA does not commit to the GWT
    61	broadcast/access distinction at the architectural level; the
    62	analogy is descriptive.
    63	
    64	\textbf{vs Predictive Processing.}~\citep{FristonFreeEnergy2010,ClarkPP2013}
    65	ARIA does not implement prediction-error minimisation or hierarchical
    66	generative models.
    67	The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
    68	modulation of the substrate response by cosine direction alignment
    69	with the prior phenomenal snapshot, not by learned prediction errors.
    70	Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
    71	learning rate over a prediction-error norm) are an open build, not
    72	delivered here.
    73	
    74	\textbf{vs neural mass models.} ARIA operates at the
    75	architectural-algorithmic level; it does not specify which neural
    76	circuits implement context rotation or partial emission. The 600-cell
    77	substrate is proposed as an abstract description of the criticality-
    78	maintaining structure of cortex, not as a circuit model.
    79	
    80	\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
    81	
    82	The companion adaptive-closure-transport
    83	preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
    84	4-tuple bridge
    85	$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
    86	$L_{M}$, learnable Hebbian-like field $W$, and a homeostatic
    87	regulariser $R_{\mathrm{hom}}$. We propose the dictionary
    88	$D_{\mathrm{ACT}}$:
    89	\[
    90	D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
    91	\;\longmapsto\;
    92	(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
    93	   \ \texttt{homeostatic\_reset}).
    94	\]
    95	\textbf{This bridge is non-load-bearing for the present paper.} It is
    96	included as a route-K (alternative-route) reading; the substrate-
    97	witness claims (six signatures, $18/18$, chess $+40.6$pp,
    98	HCP $\sigma$-distances) do not require any of the ACT theorems.
    99	
   100	\textbf{What ACT would have to deliver to make this load-bearing.}
   101	The companion preprint identifies four open builds, each of which is
   102	deferred:
   103	\begin{itemize}\itemsep=2pt
   104	\item A Lyapunov function $V(W)$ on the reduced flow whose
   105	  monotonicity proves selection — not delivered.
   106	\item An edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   107	  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
   108	  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
   109	\item A formal $2I$-equivariance audit of the closure operator
   110	  family — not delivered.
   111	\item A full reduced-flow convergence theorem on
   112	  $W$-trajectories — not delivered.
   113	\end{itemize}
   114	Until these are delivered, ARIA is positioned as the empirical
   115	\emph{substrate witness} for the family that ACT names; ACT is not the
   116	selection-theorem witness for ARIA. The companion kernel
   117	document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
   118	in a passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$ flavour
   119	anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
   120	infrastructure with this paper, but does not transfer empirical
   121	support for ARIA.
   122	
   123	\subsection{The strong-coupling reading for cortical architecture}
   124	
   125	Real cortical criticality is maintained by multiple parallel
   126	mechanisms: E/I balance, neuromodulation (acetylcholine, noradrenaline),
   127	homeostatic plasticity, gain control. The naive expectation — and the
   128	one we held until the $N\!=\!20$ deep-dive — is that these are mostly
   129	orthogonal, so losing one removes only its own main effect. The
   130	$N\!=\!20$ result reverses this on the substrate: $C$ and $P$ are
   131	strongly coupled. Disabling one cascades into losing the synergistic
   132	contribution of the other.
   133	
   134	This matches clinical observations: anaesthesia (which targets
   135	GABAergic transmission) and seizure (which targets E/I balance)
   136	produce widespread network-level dysfunction beyond their direct
   137	targets — exactly what strong synergy predicts. We position this as
   138	\emph{a hypothesis the substrate witness raises}, not as a proof.
   139	The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
   140	real-cortex pharmacological coupling is a step we do not take in
   141	this paper.
   142	
   143	\subsection{Methodological contributions}
   144	
   145	Two methodological items are worth recording outside the headline:
   146	\begin{enumerate}\itemsep=2pt
   147	\item \textbf{$N\!\geq\!20$ for high-variance interaction terms.}
   148	  Allocation discipline for preregistration: when preregistering an
   149	  interaction effect on a system with unknown per-seed variance,
   150	  budget for $N\!\geq\!20$ from the start. The original 3-seed plan
   151	  was the source of two underpowered-interaction estimates in this work.
   152	\item \textbf{State-reset protocol on non-stationary substrates.}
   153	  ARIA's substrate is a non-stationary dynamical system; the
   154	  pressure field equilibrates within $\sim 5$ successive evaluations.
   155	  Any multi-trial benchmark must specify a state-reset protocol or
   156	  document the drift. Generalisable lesson: \emph{published
   157	  cross-domain benchmarks on non-stationary substrates should report
   158	  an explicit reset/equilibration discipline}, not just seed.
   159	\end{enumerate}
   160	
   161	\subsection{The substrate as a maximum-symmetry connectivity null}
   162	
   163	The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
   164	deterministic null reference for cortical functional connectivity.
   165	Real cortex breaks the symmetry through hub-spoke functional
   166	specialisation; the $\sigma$-distances from ARIA quantify the
   167	magnitude of biological symmetry-breaking with no fitted parameters.
   168	
   169	This is a methodological contribution to comparative connectomics.
   170	Stochastic nulls (Erd\H{o}s--R\'enyi, configuration model,
   171	edge-randomised graphs) compare cortex to a random graph with matched
   172	density. ARIA is a different kind of null: a deterministic
   173	group-theoretic graph with theorem-level statements of structure
   174	(degree std $=\!0$ by transitivity, eigenvalue spectrum
   175	$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$ by character
   176	theory). Both null kinds are useful; ARIA gives a specific,
   177	reproducible, group-theoretic baseline that cortex deviates from in
   178	quantifiable $\sigma$-units.
   179	
   180	\subsection{Open questions raised by the substrate witness}
   181	
   182	\begin{itemize}\itemsep=2pt
   183	\item Do the six drug/sleep signatures replicate across $10$--$20$
   184	  cross-seed runs of the recurrent layer? (Single-seed disclosure;
   185	  see \S\ref{sec:limitations}.)
   186	\item Do alternative regular 4-polytopes ($24$-cell, $120$-cell)
   187	  reproduce comparable signature sets, or is the $600$-cell
   188	  distinguished?
   189	\item Does the strong-coupling reading ($C\!\times\!P$) survive an
   190	  independent fresh-seed $N\!=\!20$ replication at a different seed
   191	  range?
   192	\item Does the substrate's amplifier behaviour transfer to other
   193	  ambiguous-feature classification tasks beyond chess (e.g.\ visual
   194	  pattern, audio classification)?
   195	\item Does the Sleep-EDFx three-way CI overlap survive on a different
   196	  EEG cohort (TUH, NHM)?
   197	\end{itemize}
   198	We list these as open questions raised by the witness, not as gaps
   199	in the witness itself.

 succeeded in 284ms:
     1	% =====================================================================
     2	\section{Cross-domain selectivity}\label{sec:cross_domain}
     3	% =====================================================================
     4	
     5	This section reports three cross-domain witnesses. \S\ref{ssec:chess}
     6	gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
     7	conversation neutrality result that confirms the lift is selective.
     8	\S\ref{ssec:hcp} gives the HCP brain-graph maximum-symmetry null.
     9	For each domain we report
    10	$A_{d} = \mathrm{Acc}_{\mathrm{sub}, d} - \mathrm{Acc}_{\mathrm{raw}, d}$
    11	or, in the HCP case,
    12	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}})/\sigma_{\mathrm{HCP}}$.
    13	Numbers are lifted verbatim from
    14	\texttt{docs/brain\_mapping/CROSS\_DOMAIN\_RESULTS.md}.
    15	
    16	\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
    17	
    18	\textbf{Setup.} $32$ chess positions across $4$ categories (tactical,
    19	positional, endgame, opening). Per-position $8$-dimensional V2
    20	features (material balance, king safety, pawn structure, centre
    21	control, piece activity, mobility, threat density, defensive
    22	structure), normalised by per-feature $L^{2}$ norms. Substrate
    23	routing: features injected as pressure into the $S^{7}$ observer
    24	frames; substrate run forward by $n_{\mathrm{ticks}}$; resulting
    25	vertex pattern used as classifier feature vector. Classifier:
    26	1-nearest-neighbour on cosine similarity, validated by $5$-fold CV
    27	or leave-one-out (LOO).
    28	
    29	\textbf{Critical methodological detail.} Between successive depth
    30	measurements the substrate is reset to canonical state via
    31	\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
    32	field state drifts toward equilibrium across $\sim 5$ evaluations
    33	and classification structure collapses to raw-feature baseline.
    34	
    35	\begin{table}[ht]
    36	\centering
    37	\small
    38	\caption{Chess substrate-routed depth sweep with state reset between
    39	measurements.}
    40	\label{tab:chess_depth}
    41	\begin{tabular}{r r}
    42	\toprule
    43	$n_{\mathrm{ticks}}$ & accuracy \\
    44	\midrule
    45	$5$    & $53.1\%$ \\
    46	$15$   & $65.6\%$ \\
    47	$\mathbf{25}$  & $\mathbf{93.8\%}$ ($\leftarrow$ peak) \\
    48	$40$   & $84.4\%$ \\
    49	$60$   & $84.4\%$ \\
    50	$100$  & $78.1\%$ \\
    51	\bottomrule
    52	\end{tabular}
    53	\end{table}
    54	
    55	\begin{table}[ht]
    56	\centering
    57	\small
    58	\caption{Chess preregistered tests (with reset, $n=25$ canonical
    59	depth).}
    60	\label{tab:chess_prereg}
    61	\begin{tabular}{l l l l l}
    62	\toprule
    63	ID & Test & Threshold & Observed & Verdict \\
    64	\midrule
    65	P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
    66	P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
    67	P11 & random-label baseline (20 trials)     & $\in[15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
    68	P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
    69	\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
    70	\bottomrule
    71	\end{tabular}
    72	\end{table}
    73	
    74	$^{\dagger}$ The 2026-04-18 preregistration combined the null-mapping
    75	prediction across both domains (``$\geq 50\%$ on chess and
    76	conversation''). We split it for table clarity into P10 (chess null)
    77	and P16 (conversation null); both pass.
    78	
    79	$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
    80	substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
    81	The 2026-04-29 validation tightened the estimator to LOO with state
    82	reset; we report the LOO finding ($+40.6$pp) above as a stricter
    83	validation-protocol refinement at the unchanged $+15$pp threshold,
    84	not a preregistration revision.
    85	
    86	\textbf{Reading.} Substrate routing amplifies chess-position
    87	4-category classification from raw $53.1\%$ (just above $25\%$
    88	chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
    89	This is a $+40.6$pp lift on the LOO refinement; on the preregistered
    90	$5$-fold CV estimator the substrate-routed accuracy is $83.1\%$
    91	(P9), itself well above any reasonable raw-features baseline.
    92	The original 2026-04-20 validation reported the LOO lift at
    93	$+3.1$pp, a state-drift artefact closed by the reset protocol
    94	(\S\ref{sec:method}).
    95	
    96	\textbf{Permutation null decomposition.} The null permutation
    97	mapping (P10) randomises the feature$\to$frame assignment, so each
    98	feature is routed to a different $S^{7}$ frame than canonical. The
    99	substrate retains $65.4\%$ classification accuracy under random
   100	permutation — well above the $25\%$ chance level for $4$ categories.
   101	We read this as a substrate-witness decomposition:
   102	$65.4\%$ of the observed accuracy persists under the
   103	architecture-only permutation null (it survives random
   104	feature$\to$frame reassignment; the architecture is acting on whatever
   105	input lands in the frames), and the remaining $\sim 17$pp is the
   106	canonical-alignment increment. We do not claim this decomposition is
   107	unique; it is a description of the observed accuracy stack.
   108	
   109	\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
   110	
   111	\textbf{Setup.} $64$ utterances across $8$ dialogue-act categories.
   112	$8$-dimensional injection-row features per utterance. Identical
   113	substrate routing pipeline to chess.
   114	
   115	\begin{table}[ht]
   116	\centering
   117	\small
   118	\caption{Conversation preregistered tests.}
   119	\label{tab:conv_prereg}
   120	\begin{tabular}{l l l l l}
   121	\toprule
   122	ID & Test & Threshold & Observed & Verdict \\
   123	\midrule
   124	P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
   125	P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   126	P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
   127	\bottomrule
   128	\end{tabular}
   129	\end{table}
   130	
   131	\textbf{Reading.} Conversation raw features at $87.5\%$ are already
   132	strongly discriminative (cf.\ chess raw $\sim 53\%$); the substrate
   133	lift is $-4.4$pp, well within the preregistered neutrality band
   134	$|\cdot|\!<\!10$pp. The substrate is approximately neutral on conversation.
   135	
   136	\textbf{Selective amplifier signature.} The pair (chess
   137	$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
   138	selective-amplifier behaviour preregistered in 2026-04-18: in these
   139	two tasks, the architecture amplifies when raw features are ambiguous
   140	(chess raw $\sim 53\%$) and is approximately neutral when raw features
   141	are already saturated (conversation raw $87.5\%$). We do not claim
   142	this generalises to all classification tasks; cross-domain transfer
   143	to additional ambiguous-feature benchmarks is an open build
   144	(\S\ref{sec:limitations}).
   145	
   146	\subsection{HCP brain-graph maximum-symmetry null
   147	            (P17--P18)}\label{ssec:hcp}
   148	
   149	\textbf{Setup.} Reference cohort: Human Connectome Project (HCP)
   150	$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
   151	$n=100$ subjects for computational tractability, with full-cohort
   152	$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
   153	connectivity matrix; thresholded at the same density as ARIA's
   154	vertex graph ($\rho=0.101$). Compare degree distribution and
   155	higher-order graph statistics. ARIA reference: $G_{V_{600}}$ with
   156	$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
   157	has identical local structure $\Rightarrow$ uniform degree $12$
   158	$\Rightarrow$ degree std $= 0$ as a theorem.
   159	
   160	\begin{table}[ht]
   161	\centering
   162	\small
   163	\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
   164	$n=1003$ descriptive statistics.}
   165	\label{tab:hcp}
   166	\begin{tabular}{l r r r}
   167	\toprule
   168	Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
   169	\midrule
   170	Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
   171	Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
   172	Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
   173	Clustering coefficient (descriptive)       & $0.455$ & $0.220$ & $+6.80\sigma$ \\
   174	\bottomrule
   175	\end{tabular}
   176	\end{table}
   177	
   178	\begin{itemize}\itemsep=2pt
   179	\item P17 (ARIA degree std, theorem): predicted $=0$, observed
   180	  $0.0000$, $\checkmark$.
   181	\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
   182	  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
   183	  HCP subjects have degree std below $2.0$.
   184	\end{itemize}
   185	
   186	\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
   187	structure is a deterministic group-theoretic null reference for
   188	cortical functional connectivity. Real cortex breaks the symmetry
   189	through hub-spoke functional specialisation; the $\sigma$-distances
   190	quantify the magnitude of biological symmetry-breaking with no
   191	fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
   192	homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
   193	clustering coefficient) are large on the ICA-50 pipeline at the
   194	density-matched threshold $\rho = 0.101$; cross-parcellation
   195	replication (Schaefer, Glasser) remains an open build.
   196	
   197	\textbf{Participation-ratio comparability.} ARIA's vertex graph has
   198	$120$ nodes; the HCP ICA-50 connectivity matrix has $50$ nodes. The
   199	participation-ratio statistic
   200	$\mathrm{PR}(G) = (\sum_{i} d_{i})^{2} / \sum_{i} d_{i}^{2}$ is
   201	node-count-dependent — its theoretical maximum is the node count of
   202	the graph. We report the raw $\mathrm{PR}$ values
   203	($\mathrm{ARIA}=68.54$ on a 120-node graph; $\mathrm{HCP}=19.72$ on a
   204	50-node graph) and the $\sigma$-distance against the HCP
   205	across-subject distribution, but the $+79.78\sigma$ value reflects
   206	both the architectural difference and the differing node counts. A
   207	node-count-normalised statistic
   208	$\mathrm{PR}/|V|$ gives $\mathrm{ARIA}=0.571$ vs $\mathrm{HCP}=0.394$,
   209	a smaller absolute gap; we keep the raw-PR comparison as headline
   210	because the HCP subject distribution and the across-subject
   211	$\sigma$ are computed in the same units, but flag the node-count
   212	caveat here.
   213	
   214	\textbf{What we do not claim.}
   215	\begin{itemize}\itemsep=2pt
   216	\item We do not claim cortex has ``drifted from an ideal polytope'';
   217	  the substrate is a useful a-priori null whose deviation from real
   218	  cortex is precisely measurable.
   219	\item We do not claim parcellation invariance: the $\sigma$-distances
   220	  are reported on ICA-50; alternative parcellations (Schaefer,
   221	  Glasser) would give different per-metric numbers but, on the
   222	  basis of the qualitative pattern that cortex is hub-concentrated
   223	  relative to ARIA's transitive null, we expect them to preserve the
   224	  signs. Verification across parcellations is an open build
   225	  (\S\ref{sec:limitations}).
   226	\end{itemize}
   227	
   228	\subsection{Cross-domain summary as a selective amplifier
   229	            \texorpdfstring{$+$}{+} maximum-symmetry null}
   230	
   231	\begin{table}[ht]
   232	\centering
   233	\small
   234	\caption{Cross-domain summary on a single substrate.}
   235	\label{tab:cross_domain_summary}
   236	\begin{tabular}{l r r r r r}
   237	\toprule
   238	Task & Raw & Substrate & Null perm. & Geom.\ floor & Sem.\ alignment \\
   239	\midrule
   240	Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
   241	Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\
   242	Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (raw vs null) \\
   243	\bottomrule
   244	\end{tabular}
   245	\end{table}
   246	
   247	The geometric content ($\approx 65$--$71\%$ across the two domains)
   248	is the architecture-invariant null floor. The semantic content
   249	($12$--$18$pp) is the domain-specific contribution. On HCP,
   250	$\sigma$-distances against the biological cohort are
   251	$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
   252	clustering coefficient).
   253	
   254	\textbf{Headline cross-domain reading.} The substrate is
   255	\emph{selectively} amplifying (not unconditionally), and it is a
   256	maximum-symmetry deterministic null on connectivity (not a fitted
   257	model). Both readings sit inside the substrate-witness scope.

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 198ms:
     1	@book{CoxeterRegularPolytopes,
     2	  author    = {Coxeter, H. S. M.},
     3	  title     = {Regular Polytopes},
     4	  publisher = {Dover},
     5	  edition   = {3rd},
     6	  year      = {1973},
     7	  address   = {New York}
     8	}
     9	
    10	@misc{Weisstein600Cell,
    11	  author       = {Weisstein, Eric W.},
    12	  title        = {{600-Cell}},
    13	  howpublished = {From MathWorld --- A Wolfram Web Resource},
    14	  url          = {https://mathworld.wolfram.com/600-Cell.html},
    15	  note         = {Accessed 2026-04-29}
    16	}
    17	
    18	@article{BeggsPlenz2003,
    19	  author  = {Beggs, John M. and Plenz, Dietmar},
    20	  title   = {Neuronal Avalanches in Neocortical Circuits},
    21	  journal = {Journal of Neuroscience},
    22	  volume  = {23},
    23	  number  = {35},
    24	  pages   = {11167--11177},
    25	  year    = {2003},
    26	  doi     = {10.1523/JNEUROSCI.23-35-11167.2003}
    27	}
    28	
    29	@article{Tononi2008,
    30	  author  = {Tononi, Giulio},
    31	  title   = {Consciousness as Integrated Information: a Provisional Manifesto},
    32	  journal = {Biological Bulletin},
    33	  volume  = {215},
    34	  number  = {3},
    35	  pages   = {216--242},
    36	  year    = {2008},
    37	  doi     = {10.2307/25470707}
    38	}
    39	
    40	@article{BalduzziTononi2008,
    41	  author  = {Balduzzi, David and Tononi, Giulio},
    42	  title   = {Integrated Information in Discrete Dynamical Systems: Motivation and Theoretical Framework},
    43	  journal = {PLoS Computational Biology},
    44	  volume  = {4},
    45	  number  = {6},
    46	  pages   = {e1000091},
    47	  year    = {2008},
    48	  doi     = {10.1371/journal.pcbi.1000091}
    49	}
    50	
    51	@book{Baars1988GWT,
    52	  author    = {Baars, Bernard J.},
    53	  title     = {A Cognitive Theory of Consciousness},
    54	  publisher = {Cambridge University Press},
    55	  year      = {1988},
    56	  address   = {Cambridge}
    57	}
    58	
    59	@book{Dehaene2014ConsciousAndBrain,
    60	  author    = {Dehaene, Stanislas},
    61	  title     = {Consciousness and the Brain: Deciphering How the Brain Codes Our Thoughts},
    62	  publisher = {Viking},
    63	  year      = {2014},
    64	  address   = {New York}
    65	}
    66	
    67	@article{FristonFreeEnergy2010,
    68	  author  = {Friston, Karl},
    69	  title   = {The Free-Energy Principle: a Unified Brain Theory?},
    70	  journal = {Nature Reviews Neuroscience},
    71	  volume  = {11},
    72	  number  = {2},
    73	  pages   = {127--138},
    74	  year    = {2010},
    75	  doi     = {10.1038/nrn2787}
    76	}
    77	
    78	@article{ClarkPP2013,
    79	  author  = {Clark, Andy},
    80	  title   = {Whatever Next? Predictive Brains, Situated Agents, and the Future of Cognitive Science},
    81	  journal = {Behavioral and Brain Sciences},
    82	  volume  = {36},
    83	  number  = {3},
    84	  pages   = {181--204},
    85	  year    = {2013},
    86	  doi     = {10.1017/S0140525X12000477}
    87	}
    88	
    89	@article{Brodbeck2012Microstates,
    90	  author  = {Brodbeck, Verena and Kuhn, Andreas and von Wegner, Frederic and Morzelewski, Antoine and Tagliazucchi, Enzo and Borisov, Sergey and Michel, Christoph M. and Laufs, Helmut},
    91	  title   = {{EEG} microstates of wakefulness and {NREM} sleep},
    92	  journal = {NeuroImage},
    93	  volume  = {62},
    94	  number  = {3},
    95	  pages   = {2129--2139},
    96	  year    = {2012},
    97	  doi     = {10.1016/j.neuroimage.2012.05.060}
    98	}
    99	
   100	@article{VanEssen2013HCP,
   101	  author  = {Van Essen, David C. and Smith, Stephen M. and Barch, Deanna M. and Behrens, Timothy E. J. and Yacoub, Essa and Ugurbil, Kamil},
   102	  title   = {The {WU-Minn Human Connectome Project}: an Overview},
   103	  journal = {NeuroImage},
   104	  volume  = {80},
   105	  pages   = {62--79},
   106	  year    = {2013},
   107	  doi     = {10.1016/j.neuroimage.2013.05.041}
   108	}
   109	
   110	@article{PhysioNet2000,
   111	  author  = {Goldberger, Ary L. and Amaral, Luis A. N. and Glass, Leon and Hausdorff, Jeffrey M. and Ivanov, Plamen Ch. and Mark, Roger G. and Mietus, Joseph E. and Moody, George B. and Peng, Chung-Kang and Stanley, H. Eugene},
   112	  title   = {{PhysioBank, PhysioToolkit, and PhysioNet}: components of a new research resource for complex physiologic signals},
   113	  journal = {Circulation},
   114	  volume  = {101},
   115	  number  = {23},
   116	  pages   = {e215--e220},
   117	  year    = {2000},
   118	  doi     = {10.1161/01.CIR.101.23.e215}
   119	}
   120	
   121	@misc{SleepEDFx,
   122	  author       = {Kemp, Bob and Zwinderman, Aeilko H. and Tuk, Bert and Kamphuisen, Hilbert A. C. and Obery{\'e}, Josefien J. L.},
   123	  title        = {{Sleep-EDFx}: Sleep Cassette and Telemetry recordings},
   124	  howpublished = {PhysioNet},
   125	  year         = {2013},
   126	  note         = {Accessed 2026-04-29}
   127	}
   128	
   129	@misc{OpenNeuroDS005620,
   130	  author       = {Lichvar, Erin and others},
   131	  title        = {{OpenNeuro Dataset ds005620}: propofol-induced loss of consciousness {EEG}},
   132	  howpublished = {OpenNeuro},
   133	  year         = {2024},
   134	  doi          = {10.18112/openneuro.ds005620.v1.0.0}
   135	}
   136	
   137	@misc{OpenNeuroDS004902,
   138	  author       = {Timmermann, Christopher and others},
   139	  title        = {{OpenNeuro Dataset ds004902}: {DMT-induced} altered states of consciousness {EEG}},
   140	  howpublished = {OpenNeuro},
   141	  year         = {2023},
   142	  doi          = {10.18112/openneuro.ds004902.v1.0.8}
   143	}
   144	
   145	@misc{ZenodoDMT3992359,
   146	  author       = {Timmermann, Christopher},
   147	  title        = {{DMT EEG} dataset},
   148	  howpublished = {Zenodo},
   149	  year         = {2020},
   150	  doi          = {10.5281/zenodo.3992359}
   151	}
   152	
   153	@unpublished{SmartAdaptiveClosureTransport2026,
   154	  author = {Smart, Lee},
   155	  title  = {Adaptive Closure Transport: a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ from substrate response to selection},
   156	  year   = {2026},
   157	  note   = {VFD preprint, papers/adaptive-closure-transport/}
   158	}
   159	
   160	@unpublished{SmartAriaClosureKernel2026,
   161	  author = {Smart, Lee},
   162	  title  = {The 600-cell closure response kernel $C_\varphi = L + \varphi^{-2} I$ and its 9-shell projection},
   163	  year   = {2026},
   164	  note   = {VFD preprint, docs/aria-closure-kernel.md}
   165	}
   166	
   167	@unpublished{SmartBAnomaly2026,
   168	  author = {Smart, Lee},
   169	  title  = {A geometry-derived response kernel for the $B \to K^*\mu^+\mu^-$ angular anomaly: sign-uniform cross-dataset and cross-channel fit},
   170	  year   = {2026},
   171	  note   = {VFD preprint, papers/b-anomaly/}
   172	}
   173	
   174	@misc{ariaChessRepo,
   175	  author       = {Smart, Lee},
   176	  title        = {{ARIA-chess}: 600-cell substrate, recurrent self-model, and preregistered validation},
   177	  howpublished = {GitHub repository},
   178	  year         = {2026},
   179	  note         = {Accessed 2026-04-29}
   180	}

 succeeded in 209ms:
     1	% =====================================================================
     2	\section{Conclusion}\label{sec:conclusion}
     3	% =====================================================================
     4	
     5	The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
     6	symmetry, with the shifted-Laplacian response operator
     7	$\Cph = \Lop + \Ph^{-2} I$ ($\Ph=(1+\sqrt 5)/2$), is a
     8	geometry-fixed substrate that is consistent with eighteen
     9	preregistered neuroscience correspondences plus six companion
    10	drug/sleep EEG signatures of conscious vs unconscious states. Once
    11	the substrate is chosen, its graph structure
    12	($120$ vertices, uniform degree $12$, Laplacian spectrum
    13	$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$) is fixed by
    14	group theory; only one condition-dependent self-injection coupling
    15	$\eta\in\{0, 0.05, 0.20\}$ and one substrate-pinned nonlinearity
    16	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
    17	degree enter the recurrent layer above the substrate. No shape
    18	parameter is tuned to any neural dataset.
    19	
    20	\textbf{Headline tally.} On a single deterministic trajectory, six
    21	drug/sleep EEG signatures pass against their published-reference
    22	thresholds (Sleep-EDFx, OpenNeuro \texttt{ds005620}, Brodbeck 2012,
    23	Tononi 2008): NREM-N3 phenomenal-intensity variance ratio
    24	$0.463\!\times$ wake; propofol modality-switching $1.83\!\times$ wake;
    25	propofol continuity drop $+0.066$; propofol integrated-information
    26	$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
    27	recovery deterministically identical to wake under the WAKE stimulus
    28	protocol; wake cortical-avalanche power law $\alpha\!=\!2.252$,
    29	$95\%$ CI $[1.82, 2.86]$, $R^{2}\!=\!0.956$. The wake $95\%$ CI
    30	overlaps the real Sleep-EDFx EEG
    31	$95\%$ CI ($n\!=\!30$ subjects, $\alpha\!=\!2.51$,
    32	CI $[2.50, 2.53]$) and ARIA's prior cascade pipeline CI
    33	$[2.73, 3.25]$.
    34	
    35	\textbf{Eighteen preregistered correspondences.} All eighteen pass at
    36	preregistered thresholds, with two interaction tests requiring
    37	$N\!\geq\!5$ and $N\!=\!20$ respectively for reliable detection of
    38	high-variance interaction terms, and one cross-domain test requiring
    39	the documented \texttt{homeostatic\_reset} state-reset protocol. No
    40	preregistered threshold has been modified. The original 2026-04-20
    41	$15/18$ tally was a methodology-limited reading, not a content
    42	failure; the closure of the three gaps (P3, P4, P13) is documented
    43	transparently in
    44	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
    45	
    46	\textbf{Strong-coupling architectural finding.} Two cascade
    47	mechanisms — context rotation $C$ and partial emission $P$ — are
    48	causally identifiable and \emph{strongly synergistic}: their
    49	interaction $\Delta_{CP}\!=\!+0.190$ at $N\!=\!20$
    50	($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples at or
    51	below zero, reported as $0.0000$) is comparable in magnitude to the
    52	$P$ main effect $-0.218$. The original 3-seed estimate ($+0.044$)
    53	is consistent with an underpowered interaction estimate on a
    54	high-per-seed-variance term ($\mathrm{std}=0.089$ at $N\!=\!20$); we
    55	contribute the $N\!\geq\!20$ minimum as a preregistration-practice
    56	recommendation.
    57	
    58	\textbf{Cross-domain selectivity.} The substrate exhibits selective
    59	amplification on the two tasks tested: chess 4-category position
    60	classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
    61	canonical depth $n\!=\!25$ ticks (raw $53.1\%$ $\to$ substrate-routed
    62	$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
    63	$5$-fold CV — the LOO finding above is a stricter validation-protocol
    64	refinement at the same threshold), while
    65	conversation utterance classification at raw $87.5\%$ lifts $-4.4$pp
    66	(threshold $|\cdot|\!<\!10$pp) — and as a maximum-symmetry
    67	deterministic null reference for cortical functional connectivity:
    68	on HCP $n\!=\!1003$, ARIA's H$_4$-transitive structure is at
    69	$-11.58\sigma$ on degree homogeneity, $+79.78\sigma$ on participation
    70	ratio, and $+6.80\sigma$ on clustering coefficient.
    71	
    72	\textbf{Substrate-witness scope.} This is a substrate witness, not a
    73	derivation of consciousness, not a selection theorem on the
    74	companion adaptive-closure-transport
    75	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
    76	uniqueness claim for the 600-cell among regular 4-polytopes. The
    77	strengthening builds — cross-seed CIs on the recurrent-layer
    78	signatures, alternative-polytope ablations, an independent $N\!=\!20$
    79	C$\times$P replication at a different seed range, cross-parcellation
    80	HCP replication, a Lyapunov function on the reduced flow,
    81	$2I$-equivariance audit of the closure operator family — are
    82	explicitly listed in~\S\ref{sec:limitations} and remain open.
    83	
    84	We are not aware of a prior deterministic geometric architecture
    85	tested against this many preregistered cortical correspondences from
    86	a graph fixed by group theory with no shape parameters tuned to
    87	neural data; we cannot rule out that such prior work exists. The empirical material
    88	gathered here is the substrate witness; the broader programme to
    89	turn the witness into a selection-theorem-grade claim — including the
    90	independent passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$
    91	flavour anomaly~\citep{SmartBAnomaly2026} on the same response
    92	operator $\Cph$ — is sketched in the companion preprints and remains
    93	the natural next step.

 succeeded in 221ms:
     1	% =====================================================================
     2	\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
     3	% =====================================================================
     4	
     5	This section enumerates limitations transparently, organised as a
     6	five-move guard matrix following the b-anomaly preprint
     7	template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
     8	test/claim, state-drift. For each guard we record
     9	$G\colon \mathrm{risk} \to (\mathrm{disclosure}, \mathrm{evidence},
    10	\mathrm{strengthening\ build})$.
    11	
    12	\subsection{Regime}\label{ssec:regime}
    13	
    14	\textbf{Single substrate (the 600-cell).} We have not tested whether
    15	other regular 4-polytopes ($24$-cell, $120$-cell) would produce
    16	comparable correspondences. The 600-cell was chosen because its
    17	H$_4$ Coxeter cascade structure aligns with the empirical signatures
    18	that motivated this paper, not from an a-priori derivation.
    19	\emph{Disclosure:} substrate-witness scope, no uniqueness claim
    20	(\S\ref{sec:intro}). \emph{Evidence:} empirical correspondences hold
    21	on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
    22	$\{24\text{-cell}, 120\text{-cell}\}$ on the same six-signature
    23	battery and the eighteen preregistered tests, with thresholds
    24	preserved.
    25	
    26	\textbf{Single-seed determinism on the recurrent layer.} The v4
    27	six-signature results in~\S\ref{ssec:six_signatures} are reported on
    28	a single deterministic trajectory at seed $42$. Empirical CIs across
    29	$10$--$20$ cross-seed runs would strengthen the per-signature claims
    30	beyond the single-trajectory bootstrap of $58$ events that gives the
    31	WAKE 95\% CI $[1.82, 2.86]$. \emph{Disclosure:} explicitly single-seed
    32	in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
    33	\emph{Evidence:} bootstrap CI on the wake 58 events, plus three-way
    34	overlap with two independent reference $\alpha$ ranges.
    35	\emph{Strengthening build:} 10--20 cross-seed runs of
    36	\texttt{demo\_drug\_sleep\_v4.py}, with per-signature bootstrap CIs.
    37	
    38	\textbf{Stylised stimulus models on the recurrent layer.} The v4
    39	stimulus models for WAKE (AR(1) noise + tonic shell + attention
    40	episodes), SLEEP\_N3 (slow oscillation + spindles + K-complexes),
    41	and PROPOFOL (low-amplitude tonic noise) are biologically motivated
    42	but abstract: a single shell anchor for tonic coherence, fixed
    43	$40$-tick period for slow-wave drive, etc. Real spatial structure of
    44	cortical input is much richer. \emph{Disclosure:}~\S\ref{sec:chain}
    45	``deliberately structural rather than measurement-fitted''.
    46	\emph{Evidence:} models match published biological time scales but
    47	are not tuned to specific signatures. \emph{Strengthening build:}
    48	replication on stimulus models derived from anatomically-grounded
    49	input statistics (e.g.\ retinotopic, tonotopic).
    50	
    51	\subsection{Post-hoc}\label{ssec:posthoc}
    52	
    53	\textbf{The 600-cell choice is post-hoc justified by empirical
    54	observables.} While the construction of $\Rsixhundred$ is theorem-
    55	level rigorous (H$_4$ Coxeter group theory), the choice of \emph{this}
    56	polytope as the consciousness-substrate instance is motivated by the
    57	correspondences observed, not by an a-priori biological argument.
    58	\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
    59	derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
    60	preregistered correspondences plus six signatures; the H$_4$
    61	transitivity theorem ($P17$). \emph{Strengthening build:} comparison
    62	with the $24$-cell and $120$-cell on the same signatures; formal
    63	ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
    64	(deferred).
    65	
    66	\textbf{Cascade decomposition is one of several possible
    67	decompositions of H$_4$.} We use the $\sigma$-orbit projector basis
    68	because it is machine-precise and biologically informative, but other
    69	bases (character-theoretic, Galois-twin) give the same physical
    70	predictions through different intermediate variables. \emph{Disclosure:}
    71	\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
    72	\emph{Evidence:} block-diagonalisation at $<10^{-15}$ cross-block
    73	norm. \emph{Strengthening build:} catalogue and equivalence-prove the
    74	admissible decompositions.
    75	
    76	\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
    77	$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
    78	strictly positive definite (\S\ref{ssec:cphi}); it is not derived
    79	from a closure functional or symmetry argument. \emph{Disclosure:}
    80	\S\ref{ssec:cphi} marks this as a design-level choice; the companion
    81	kernel doc~\citep{SmartAriaClosureKernel2026} explicitly does not
    82	derive it. \emph{Evidence:} the same operator (with the same shift)
    83	serves as the basis for the b-anomaly passive-regime
    84	witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
    85	derive the $\Ph^{-2}$ shift as the unique stability clamp under a
    86	named regularity criterion.
    87	
    88	\subsection{Interpretation}\label{ssec:interpretation}
    89	
    90	\textbf{The recurrent layer is a method, not a metaphysics claim.}
    91	We do not claim the recurrent self-model layer ``is'' consciousness;
    92	we claim quantitative consistency with six published biological
    93	signatures on a deterministic trajectory. \emph{Disclosure:}
    94	\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
    95	\emph{Evidence:} six signatures vs published thresholds.
    96	\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
    97	formal account of which substrate observables map to which phenomenal
    98	contents (the bind\_phenomenal\_field channels) is not delivered.
    99	
   100	\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
   101	IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
   102	\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
   103	matches IIT direction. \emph{Strengthening build:} a
   104	\texttt{phi\_iit\_full} implementation following Balduzzi--Tononi
   105	2008~\citep{BalduzziTononi2008} on the substrate; not delivered.
   106	
   107	\textbf{HCP $\sigma$-distances are descriptive, not normative.} We
   108	do not claim ``cortex has drifted from an ideal polytope''; we
   109	quantify the distance between cortex and the deterministic H$_4$ null.
   110	\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
   111	$\sigma$-distances on three independent metrics. \emph{Strengthening
   112	build:} cross-parcellation replication (Schaefer, Glasser).
   113	
   114	\subsection{Test/claim}\label{ssec:testclaim}
   115	
   116	\textbf{Two preregistered interaction tests required higher $N$
   117	than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
   118	$N\!=\!20$. We document this transparently as a Type II
   119	methodology issue, not a threshold change. \emph{Disclosure:}
   120	\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
   121	\emph{Evidence:} bootstrap CI fully above the $+0.10$ floor; per-seed
   122	distribution narrow at $N\!=\!20$ ($\mathrm{std}=0.089$);
   123	$19/20$ seeds positive. \emph{Strengthening build:} a second
   124	$N\!=\!20$ run at a different seed range (e.g.\ $33000$--$33019$);
   125	an $N\!=\!50$ characterisation of the per-seed distribution.
   126	
   127	\textbf{The original 2026-04-20 walks-back are reversed without
   128	threshold modification.} The reversals (P3, P4, P13) are documented
   129	in
   130	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md} with
   131	the original failure values, the methodology refinement, and the
   132	post-refinement values. \emph{Disclosure:} this paper carries those
   133	disclosures verbatim. \emph{Evidence:} 2026-04-20 vs 2026-04-29 side-
   134	by-side results table. \emph{Strengthening build:} the strengthening
   135	builds for P3/P4/P13 above; no further claim is needed.
   136	
   137	\textbf{Bayesian and full-IIT inference not performed.} All intervals
   138	are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
   139	proxy, not the Balduzzi--Tononi 2008 algorithm. \emph{Disclosure:}
   140	this section. \emph{Strengthening build:} Bayesian posterior on
   141	$\Delta_{CP}$; full-IIT computation on the $S^{4}\!\to\!2^{4}$
   142	substrate state space. The latter is computationally heavy and is
   143	deferred.
   144	
   145	\subsection{State-drift / out-of-scope}\label{ssec:scope}
   146	
   147	\textbf{Single condition-dependent parameter $\eta$ is not derived
   148	as a learned variable.} $\eta\in\{0, 0.05, 0.20\}$ across PROPOFOL,
   149	SLEEP\_N3, and WAKE/RECOVERY is a condition-dependent constant in
   150	this paper, not a learned trajectory. A predictive-processing
   151	extension where $\eta$ adapts on an error norm is an open build.
   152	
   153	\textbf{No deuteron / hadron / RH / capstone material is loaded into
   154	this paper.} The companion programme (cascade-derivation, capstone
   155	coalgebra, RH formal) shares operator-level infrastructure but is not
   156	load-bearing here. Deliberately out of scope.
   157	
   158	\textbf{Out-of-scope items NOT delivered (correctly).}
   159	\begin{itemize}\itemsep=2pt
   160	\item Aria-chess active-regime companion analysis on chess move-by-move
   161	  trajectories (this paper covers static positions only).
   162	\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under
   163	  $2I$-equivariance — open build of the ACT companion paper.
   164	\item Lyapunov derivation $V(W)$ from a closure functional
   165	  $\mathcal{F}$ — open build of the ACT companion paper.
   166	\item Selection theorem for $\Rsixhundred$ over alternative regular
   167	  4-polytopes — see~\S\ref{ssec:regime}.
   168	\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
   169	  of the six signatures.
   170	\item Cross-parcellation replication of the HCP $\sigma$-distances
   171	  (Schaefer, Glasser, etc.).
   172	\item Bayesian posterior on the C$\times$P interaction.
   173	\end{itemize}
   174	
   175	\subsection{The honest verdict}
   176	
   177	The result is a substrate witness: a geometry-fixed substrate, with
   178	no shape parameters tuned to any neural dataset, is consistent with
   179	eighteen preregistered correspondences and six companion drug/sleep
   180	EEG signatures, with all original gaps closed by methodology
   181	refinement and without modifying any preregistered threshold. We do
   182	not claim the substrate \emph{is} consciousness. We do not claim a
   183	selection theorem on the ACT bridge. We do not claim uniqueness for
   184	$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
   185	for these stronger claims are listed above and remain open.

exec
/bin/bash -lc "wc -l '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"(6/6|18/18|17/18|15/18|0\\.190|0\\.143|0\\.239|0/2000|P\\(|P=0|40\\.6|27\\.2|n=25|n=15|11\\.58|79\\.78|6\\.80|2\\.96|1\\.83|1003|preregister|threshold|N=20|N=3|N=5|0\\.365|0\\.463|2\\.252|2\\.513|3\\.388|65\\.4|70\\.6|83\\.1|93\\.8|-4\\.4|\\+3\\.1)\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 268ms:
  1253 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md
   426 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md
   435 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md
   584 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md
   399 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md
   194 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md
   257 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md
  3548 total

 succeeded in 253ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md:32:| 2 | 93.8% | 100 | 147.9 | 1.000 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md:206:5. ⏳ Re-run preregistered validation with proper reset — convert
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:10:- a **pass threshold** (interval, inequality, or categorical match)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:65:  2.513 [2.504, 2.526]. A different seed's bootstrap CI should
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:72:- **Rationale**: Discovery gave 0.365. If the ratio is ≥ 0.70 it means
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:89:- **Claim**: 5-fold CV on v2 features at n=25 ticks, 5 fresh seeds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:116:- **Claim**: At n=25, substrate ≥ raw **+ 15pp** on 5-fold CV (fresh
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:160:  density-matched threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:184:## Success thresholds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:192:We do not expect 18/18 — some are noisy empirical tests and statistical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:3:*This document supersedes `VALIDATION_RESULTS.md` (2026-04-20, 15/18).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:4:It records the most recent run of the preregistered validation harness
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:5:plus the N=20 deep-dive on the residual P4 prediction.*
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:8:> 18 / 18 with N=20 deep-dive on the residual P4.** Original 15/18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:13:> measurements for chess LOO, and (c) N=20 fresh-seed replication of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:15:> set is fully validated against preregistered thresholds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:25:Each prediction has a falsifiable threshold (numerical band or
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:27:`run_preregistered_validation.py` — git-tracked, deterministic given
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:37:The original validation run on 2026-04-20 reported **15/18 passes**:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:43:  - **P3** (D×C interaction independence): observed −0.231 at N=3,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:45:  - **P4** (C×P synergy): observed +0.044 at N=3, below +0.10 floor.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:46:  - **P13** (Chess LOO substrate lift ≥ +15pp): observed +3.1pp,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:60:   in `run_preregistered_validation.py`. The original 3 seeds was
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:69:3. **N=20 deep-dive** on the residual P4 (`demo_p4_cxp_deep_dive.py`):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:80:| ID | Claim | Threshold | 2026-04-20 (3-seed) | **2026-04-29 (5-seed + reset + N=20 P4)** | Verdict |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:85:| P4 | C×P synergy | ≥ +0.10 | +0.044 ❌ | **+0.190 at N=20, CI [+0.143, +0.239]** | ✅ at N=20 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:87:| P6 | Real EEG α | ∈ [2.0, 3.0] | 2.513 ✅ | **2.513** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:88:| P7 | W→N3 variance ratio | < 0.70 | 0.365 ✅ | **0.365** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:90:| P9 | Chess 5-fold CV | ≥ 70% | 83.1% ✅ | **83.1%** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:91:| P10 | Chess null mapping | ≥ 50% | 65.4% ✅ | **65.4%** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:93:| P12 | Chess goldilocks peak | ∈ {15, 25, 40, 60} | n=15 ✅ | **n=25** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:94:| P13 | Chess LOO substrate lift | ≥ +15pp (with reset) | +3.1pp ❌ | **+40.6pp** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:97:| P16 | Conv null mapping | ≥ 50% | 70.6% ✅ | **70.6%** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:99:| P18 | HCP ICA-50 degree std | > 2.0 | 3.388 ✅ | **3.388** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:109:**Original (N=3) failure:** −0.231. The interaction estimate fell just
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:113:**2026-04-29 re-run (N=5):** −0.183. Now inside the independence band.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:114:The shift from −0.231 (N=3) to −0.183 (N=5) is the kind of stabilisation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:116:seeds tightens the estimate enough to land inside the threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:120:interaction estimate is approximately 0.06–0.10; the threshold is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:121:±0.20; and a single bad-luck draw at N=3 can put the point estimate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:125:cascade-α" is **supported** by the N=5 re-run within the preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:126:threshold. We do not claim point-zero independence (the estimate is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:137:**Original (N=3) failure:** +0.044. Below threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:139:**2026-04-29 re-run (N=5):** +0.039. Still below threshold — confirming
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:140:the N=3 reading at face value.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:142:**N=20 fresh-seed deep-dive (`demo_p4_cxp_deep_dive.py`, seeds 32000–32019):**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:145:C×P bootstrap mean:           +0.190
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:146:C×P 95% bootstrap CI:         [+0.143, +0.239]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:147:P(interaction ≤ 0):           0.0000
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:148:P(interaction < +0.10):       0.0000
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:151:The 95% CI is **entirely above the preregistered +0.10 threshold**.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:153:N=3/N=5 estimates were Type II false negatives compounded by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:155:(per-seed std = 0.089 at N=20).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:165:**Threshold:** ≥ +15pp lift (substrate vs raw on LOO at n=25 ticks).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:167:**Original (N=1) failure:** +3.1pp. Far below threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:170:measurements):** **+40.6pp**.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:175:  n=15:   65.6%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:176:  n=25:   93.8%   ← peak (P12 goldilocks)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:181:Lift at n=25 = 93.8% − 53.1% = +40.6pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:187:40, 60, 100) without reset, so by the time it reached n=25 the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:212:  at 3 seeds). Both above the +0.30 dominance threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:219:- **P6**: Real EEG spindle α = 2.513 (n=30 subjects). Inside [2.0, 3.0].
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:220:- **P7**: W→N3 variance ratio = 0.365 (n=24 subjects). Below 0.70.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:227:- **P9**: Chess 5-fold CV at fresh seeds (30200–30204) = 83.1%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:229:- **P10**: Null feature→frame permutation (15 trials) = 65.4%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:235:- **P12**: Goldilocks peak depth = n=25 (∈ {15, 25, 40, 60}). With
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:236:  reset between measurements, n=25 is the global maximum at 93.8%.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:237:- **P13**: LOO substrate lift at n=25 = **+40.6pp** with reset
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:248:- **P16**: Conv null feature→frame (15 trials) = 70.6% (≥ 50%).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:249:  Slightly higher than chess null (65.4%), consistent with conversation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:255:- **P18**: HCP ICA-50 degree std = 3.388 (n=100 subjects, density-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:256:  matched threshold). > 2.0 confirms small-world hub-spoke structure
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:258:  symmetry-breaking is +79.78σ on participation ratio against ARIA.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:262:## 5. The 18/18 verdict
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:264:**Standard validation tally:** 17/18 (the residual P4 fails at N=5).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:265:**Including the N=20 deep-dive:** 18/18 (P4 passes decisively at N=20).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:267:The empirical tally is **18/18 at adequate replication**. Two of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:275:All eighteen preregistered predictions are **supported by the data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:276:within preregistered thresholds**, with the methodological caveat
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:286:> *"All eighteen preregistered predictions pass at empirical thresholds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:288:> homeostatic reset between LOO depth measurements) give 17/18; the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:290:> (we used N=20 fresh seeds) due to the high per-seed variance of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:292:> (+0.190, 95% bootstrap CI [+0.143, +0.239]); the synergy is in fact
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:293:> ~90% above the preregistered floor, indicating C and P are strongly
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:310:within the preregistered |·| < 0.20 band, confirmed at N=5.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:318:**Now reads:** C×P synergy is +0.190 [+0.143, +0.239] at N=20, ~90%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:319:above preregistered. C and P are strongly coupled cascade-state
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:332:is +40.6pp.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:338:The original validation methodology — 18 preregistered predictions
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:339:with falsifiable thresholds, frozen before any validation run — is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:341:re-run with N improvements **did not modify any threshold or claim
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:343:reset. The fact that this gave 18/18 (with N=20 P4) where the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:344:original gave 15/18 demonstrates that:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:348:(b) The original validation methodology was insufficient — N=3 is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:355:adequate power. No threshold was loosened. No prediction was rewritten
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:364:# Standard validation (17/18, ~18 min)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:366:python3 run_preregistered_validation.py
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:368:# P4 N=20 deep-dive (~28 min)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:372:JSON results are saved to `~/.aria/preregistered_validation/results_*.json`.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:385:- `docs/brain_mapping/VALIDATION_RESULTS.md` — original 15/18 result
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:387:- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — standalone N=20 report
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:390:  drug/sleep EEG signatures (independent of preregistered set, on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:396:- `run_preregistered_validation.py` — validation harness
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:397:- `demo_p4_cxp_deep_dive.py` — N=20 deep-dive script
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:3:*Standalone publishable finding from N=20 seed deep-dive on the residual P4
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:4:preregistered prediction. Compiled 2026-04-29.*
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:9:> on cascade-α is +0.190, 95% bootstrap CI [+0.143, +0.239]** — comparable
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:11:> preregistered prediction of ≥+0.10. The original 3-seed preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:20:## 1. Background: what was preregistered, what failed at N=3
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:37:  threshold but not yet crossed) emit pressure at 30% scale, saturating
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:48:### 1.2 The preregistered predictions for D/C/P/E mechanisms
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:63:contribution to cascade-α. The preregistered floor was +0.10 — stating
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:71:Means (N=3 each):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:87:This was below the +0.10 threshold, so P4 was reported as a **fail**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:88:in the headline 15/18 result. The walk-back was:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:94:N=20 deep-dive presented below shows this was wrong.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:98:## 2. The N=20 deep-dive (2026-04-29)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:119:one-sided P(interaction ≤ 0) and P(interaction < +0.10).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:125:### 2.2 Per-condition means at N=20
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:143:### 2.3 Main-effect estimates at N=20
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:165:C×P bootstrap mean:           +0.190
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:166:C×P 95% bootstrap CI:         [+0.143, +0.239]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:167:P(interaction ≤ 0):           0.0000
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:168:P(interaction < +0.10):       0.0000
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:171:**The 95% CI is entirely above the preregistered +0.10 threshold.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:186:mean = +0.190,  std = 0.089,  SEM = 0.020
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:191:per-seed std at N=20 (0.089) is just under half the per-seed std at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:193:N=20 reveals a clean, narrow positive distribution.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:206:20   32000–32019      +0.190          [+0.143, +0.239]      ✅ DECISIVELY ABOVE
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:214:   = 0.089 and a true synergy of +0.19, the SEM at N=3 is 0.089/√3 = 0.051.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:215:   The 95% CI on the N=3 mean would be roughly +0.05 to +0.15 if there
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:216:   were no other bias — already containing the threshold. But N=3 also
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:227:landed on outliers; the N=20 sample (32000–32019) had std 0.089. **The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:233:| Effect | N=3 / N=5 estimate | N=20 estimate | Shift |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:252:exceeded threshold. As the frame rotates, the uncrossed pool's
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:281:the N=20 deep-dive — is that these are mostly orthogonal. Losing one
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:284:The N=20 result reverses this. **Strong inter-mechanism coupling is the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:302:**Old framing (2026-04-20, with 15/18 result):**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:308:**New framing (2026-04-29, with N=20 result):**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:310:> *"P4 (C×P synergy ≥+0.10) was preregistered with a +0.10 floor.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:313:> interaction term. Replication at N=20 fresh seeds (32000–32019)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:314:> gives synergy = +0.190, 95% bootstrap CI [+0.143, +0.239],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:315:> P(synergy ≤ 0) = 0, P(synergy < +0.10) = 0. The architecture's
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:334:### 5.3 The 18/18 verdict
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:336:P4 was the residual gap in the 17/18 validation re-run from earlier in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:337:this session. With the N=20 deep-dive, the synergy is decisively above
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:338:the preregistered floor. **Effectively, all eighteen preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:377:1. **One seed range tested at N=20.** A second N=20 run at a different
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:383:   well-powered N=20 estimate.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:387:   (e.g., pressure-threshold crossings) might give a slightly different
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:395:   (with one large positive outlier and two negatives) while N=20 has a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:396:   clean unimodal positive distribution. A larger replication (N=50)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:404:The C×P interaction in ARIA's cascade ablation matrix was preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:409:synergy = +0.190, 95% bootstrap CI [+0.143, +0.239], P(synergy ≤ 0) = 0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:410:P(synergy < +0.10) = 0. The architecture's prediction is exceeded by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:420:from the preregistered prediction set, taking the empirical tally from
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:421:17/18 to 18/18.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:427:- `demo_p4_cxp_deep_dive.py` — N=20 script (this work)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:430:- `run_preregistered_validation.py` — original cascade-block test
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:432:- `docs/brain_mapping/VALIDATION_RESULTS.md` — original 15/18 result
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:15:recurrence on the 600-cell with bounded-top-K thresholding) plus
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:23:has a published reference and a falsifiable threshold; all six pass.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:26:stimulus-model artefacts in `demo_wake_alpha_diagnosis.py`) to 6/6 by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:32:| 1 | Sleep variance ratio | NREM-N3 EEG (Lee 2017, Jobst 2017) | ratio ≈ 0.365 | 0.463 | ✓ within 30% |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:33:| 2 | Propofol switching ↑ | OpenNeuro ds005620 (n=8, 2.96×) | ratio in [1.5, 5.0] | 1.83× | ✓ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:37:| 6 | Cortical avalanche α | Sleep-EDFx n=30 (α=2.51 [2.50, 2.53]) | α ∈ [1.5, 3.5], R² > 0.85 | 2.252 [1.82, 2.86] R²=0.956 | ✓ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:63:**The bounded_topk(k=12) thresholding is the load-bearing nonlinearity.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:195:All four conditions run for 800 ticks at seed = 42, k_threshold = 12.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:199:WAKE       58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:202:RECOVERY   58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:208:Source: prior real Sleep-EDFx W→N3 analysis (n=24, ratio = 0.365), confirmed
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:212:Ratio = 0.463. Falls within [0.255, 0.475], the 30% prediction window.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:224:microstate switching ratio 2.96×).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:226:**Observed:** WAKE modality_switches → PROPOFOL modality_switches ratio = 1.83×.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:227:Falls within [1.5×, 5.0×] window. Below the empirical 2.96× point estimate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:256:Ratio PROPOFOL/WAKE = 0.33×. Below the 0.50× threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:283:**Observed:** WAKE α = 2.252, 95% CI [1.82, 2.86], R² = 0.956 (n_events=58).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:293:**Mechanism:** The bounded_topk(k=12) thresholding is the critical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:313:| H4: k_threshold sweep | k=12 is the sweet spot |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:329:- **v4.final**: AR(1) β=0.90 + tonic shell + episodes 20-50 amp 0.8 anchored to shell + within-shell rotation → 6/6
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:345:- k_threshold: 12 (cortical band; bounded_topk nonlinearity)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:357:- The deterministic 600-cell substrate with bounded_topk thresholding
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:362:- All six signatures pass under preregistered thresholds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:368:- The Sig 2 ratio (1.83×) is below the empirical point estimate (2.96×)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:373:  preregistered validation methodology).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:376:  "exact match" — only "within preregistered tolerance."
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:386:| `demo_drug_sleep_v4.py` | The 6/6 demo script — single deterministic run |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:392:| `kernel/lyapunov_selector.py` | bounded_topk thresholding |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:404:- `project_propofol_empirical_5.md` — empirical anchor for Sig 2 (n=8, 2.96×)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:413:polytope with bounded top-K thresholding (k=12) and a recurrent self-injection
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:415:signature is a falsifiable threshold against published data: cortical-avalanche
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:416:power law in the wake-state band (passes with α = 2.252, 95% CI [1.82, 2.86]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:419:1.83×), propofol continuity disruption (passes at +0.066), propofol Φ collapse
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:8:> when raw features are ambiguous (chess: +40.6 percentage points on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:9:> leave-one-out, raw 53.1% → substrate-routed 93.8%) and is correctly
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:13:> transitivity); HCP n=1003 degree std = 3.28 ± 0.28; ARIA is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:14:> −11.58σ on degree homogeneity and +79.78σ on participation ratio,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:27:1. **Chess pattern recognition** (P9–P13 in the preregistered set):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:42:   the Human Connectome Project (n=1003 subjects, ICA-50
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:47:preregistered tests on chess + conversation pass at fresh seeds; both
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:92:Mean:                 83.1%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:96:83.1% on the 32-position × 4-category task, well above the 70%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:97:threshold. Per-seed variance is small (range 81.2%–87.5%).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:100:the fresh-seed mean of 83.1% replicates discovery within expected
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:113:**Result:** 65.4% mean across 15 permutations.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:117:substrate retains 65.4% classification power — well above the 25%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:121:(83.1% − 65.4%) is the semantic alignment bonus.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:143:(23.4% ≈ 25% chance). This confirms the 83.1% raw and 65.4% null are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:161:  25     93.8%   ← peak
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:168:n=25, with a roll-off both at shallower depth (insufficient
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:181:(b) substrate-routed patterns at n=25, with reset between depth
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:188:Substrate-routed (n=25, with reset):   93.8%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:189:Lift:                                  +40.6 percentage points
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:194:is just above chance-25%) to near-perfect (93.8%) when routed through
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:195:the substrate's 600-cell graph. This is **+40.6pp of geometric
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:196:amplification**, far exceeding the +15pp prereg threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:198:The original 2026-04-20 validation reported this lift at +3.1pp — a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:202:lift is restored to +40.6pp. See `NON_EQUILIBRIUM_FINDING.md` for the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:208:- 53.1% raw → 93.8% substrate-routed at canonical depth (n=25)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:209:- 65.4% null mapping (architecture-invariant geometric floor)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:210:- 83.1% 5-fold CV at fresh seeds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:211:- Goldilocks optimum at n=25 ticks of substrate evolution
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:213:The +40.6pp lift is roughly an order of magnitude above the +15pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:214:preregistered floor. The 65.4% null mapping shows two-thirds of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:254:Substrate 5-fold CV (n=25):  83.1%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:262:preregistered window, and the negative sign suggests minor noise
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:277:**Result:** 70.6% mean across 15 permutations.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:279:**Interpretation:** Conversation null mapping (70.6%) is slightly
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:280:higher than chess null mapping (65.4%), consistent with conversation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:289:| Chess (LOO) | 53.1% | 93.8% | n/a | n/a | +40.6pp lift |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:290:| Chess (5-fold CV) | n/a | 83.1% | 65.4% | 65.4% | +17.7pp |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:291:| Conversation (5-fold CV) | 87.5% | 83.1% | 70.6% | 70.6% | +12.5pp (raw vs null) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:301:substrate routing at 83.1% (lift −4.4pp) is within preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:302:neutrality bounds. The null permutation at 70.6% confirms geometric
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:311:**Reference cohort:** Human Connectome Project (HCP), n=1003 subjects.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:312:For preregistered tests, n=100 subjects (computational tractability)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:313:in ICA-50 parcellation. The full-cohort effects (n=1003) match the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:316:**Method:** Build group-averaged ICA-50 connectivity matrix; threshold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:340:**Result (n=100 subjects, density 0.101):** **3.388**.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:347:**ARIA is at −11.58σ** below the HCP cohort mean on this metric:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:348:ARIA's degree std is 0; HCP n=1003 mean is 3.28 ± 0.28; the gap is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:349:(0 − 3.28) / 0.28 = −11.7σ. **Zero of 1003 HCP subjects** have
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:352:### 4.4 Higher-order graph statistics (full cohort, n=1003)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:358:Metric                 ARIA     HCP n=1003 mean   σ from HCP
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:360:Degree std             0.000    3.28 ± 0.28        −11.58σ
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:361:Participation ratio    68.54    19.72 ± 0.61       +79.78σ
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:362:Clustering coefficient 0.455    0.220              +6.80σ
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:371:  Real cortex is hub-concentrated; ARIA is uniform. +79.78σ.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:375:  +6.80σ.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:390:giving precise effect-size statements like "real cortex is +79.78σ
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:395:parcellation choice, density threshold, and subject inclusion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:418:ARIA's degree std = 0 (theorem); HCP n=1003 degree std = 3.28 ± 0.28,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:419:range [2.55, 4.16], with zero of 1003 subjects below 2.0. ARIA is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:420:−11.58σ on degree homogeneity, +79.78σ on participation ratio, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:421:+6.80σ on clustering coefficient. The substrate functions as a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:434:amplifies to 93.8% LOO (+40.6pp lift) and 83.1% 5-fold CV across fresh
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:440:is correctly null (lift −4.4pp, well within preregistered neutrality
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:442:unconditional booster. On HCP brain functional connectivity (n=1003,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:444:std = 0) is −11.58σ below the biological mean (3.28 ± 0.28); on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:445:participation ratio ARIA at 68.54 is +79.78σ above HCP (19.72 ± 0.61),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:446:and on clustering coefficient ARIA at 0.455 is +6.80σ above HCP (0.220).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:459:The contrast between chess (+40.6pp lift) and conversation (−4.4pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:469:The 65.4% (chess) / 70.6% (conversation) null permutation accuracies
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:479:reference for biological cortex. The σ-distances (−11.58σ, +79.78σ,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:480:+6.80σ) quantify the magnitude of biological symmetry-breaking, with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:493:python3 run_preregistered_validation.py
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:509:JSON outputs land in `~/.aria/preregistered_validation/results_*.json`.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:516:1. **Chess test is small (32 positions, 4 categories).** The ~93.8%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:519:   at 83.1% is a more conservative readout (4-category random
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:551:- `run_preregistered_validation.py` — full P1–P18 harness
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:567:  preregistered tally
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:583:- `project_preregistered_validation_17_of_18.md` — re-run summary
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:584:- `project_p4_cxp_underpowered_not_wrong.md` — N=20 deep-dive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:7:drug/sleep EEG signatures), the N=20 deep-dive on the C×P synergy
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:23:preregistered before the validation runs (frozen 2026-04-18). We
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:27:α = 2.252, 95% CI [1.82, 2.86] (R² = 0.956), with three-way confidence
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:30:state-variance collapses to 0.46× wake (predicted 0.365); propofol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:31:regime-switching elevates 1.83× wake; propofol continuity drops by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:36:exhibit a strong synergistic interaction of +0.190 (95% bootstrap CI
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:37:[+0.143, +0.239]), comparable in magnitude to the P main effect
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:42:recognition by +40.6 percentage points (raw 53.1% → substrate-routed
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:43:93.8% on leave-one-out at canonical depth) but is correctly null on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:46:HCP brain functional connectivity (n=1003 subjects), ARIA serves as a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:48:(theorem); HCP degree std = 3.28 ± 0.28; ARIA is at −11.58σ on degree
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:49:homogeneity and +79.78σ on participation ratio. With the N=20
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:50:deep-dive, the empirical tally is 18/18 preregistered predictions
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:51:plus 6/6 drug/sleep signatures; no claim is walked back. This is the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:54:preregistered tests.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:57:avalanches, integrated information, drug/sleep EEG, preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:129:`O*` within a preregistered threshold. We report two non-overlapping
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:132:**Set A: Eighteen preregistered predictions** (frozen 2026-04-18 in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:146:thresholds (with the methodological caveat that two interaction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:232:A vertex "crosses" once its accumulated pressure exceeds a threshold;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:237:2⁴ ablation in the preregistered validation (P1–P5).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:247:**Causal effect on cascade-α (N=5):** main effect = 0.062 (small but
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:249:preregistered |·| < 0.20 independence band).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:260:**Causal effect on cascade-α (N=5):** main effect = +0.621. This
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:266:High-pressure uncrossed vertices (above threshold but not yet
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:272:**Causal effect on cascade-α (N=20):** main effect = −0.218. Removing
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:286:**Causal effect on cascade-α (N=5):** main effect = +0.046, within
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:287:the preregistered |·| < 0.15 null band. E is a structural completeness
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:294:estimated at +0.044 — below the preregistered +0.10 threshold —
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:301:Per-condition means (N=20):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:310:  point estimate:           +0.190
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:311:  95% CI:                   [+0.143, +0.239]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:312:  P(interaction ≤ 0):       0.0000
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:313:  P(interaction < +0.10):   0.0000
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:316:The 95% CI is **entirely above the preregistered +0.10 threshold**;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:317:the synergy is decisively positive (P(≤ 0) = 0) and decisively above
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:318:prereg (P(< +0.10) = 0).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:327:| **20** | **+0.190, CI [+0.143, +0.239]** | **decisively above** |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:330:high-per-seed-variance interaction term (per-seed std = 0.089 at N=20).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:331:With adequate N, the synergy is in fact ~90% above the preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:393:### 4.2 The bounded-top-K thresholding
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:558:run. Each prediction has a falsifiable threshold (numerical band or
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:560:`run_preregistered_validation.py`; it is git-tracked, deterministic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:563:**Critical: no threshold has been modified post-hoc. The original
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:567:not as a threshold change.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:573:At preregistration time we used 3 seeds per condition. The N=20
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:576:- Per-seed std on the C×P interaction = 0.089 at N=20.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:583:−0.183, inside |·|<0.20 band). P4 closes only at N = 20 (C×P = +0.190,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:584:CI [+0.143, +0.239]).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:587:preregistering interaction terms with high per-seed variance, allocate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:601:+3.1pp lift (without reset, on a state-drifted substrate) to +40.6pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:602:lift (with reset, far exceeding the preregistered +15pp floor).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:622:EEG within preregistered tolerance.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:628:**Result (preregistered re-run 2026-04-29, 5 seeds):**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:635:| v4 WAKE consciousness chain | 2.252 | [1.82, 2.86] | 0.956 | 58 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:646:preregistered fits.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:651:bounded top-K thresholding and IIT-style Φ, reproduces six independent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:654:**Method.** Four conditions × 800 ticks at seed = 42, k_threshold = 12.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:662:WAKE       58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:665:RECOVERY   58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:672:| 1 | NREM-N3 variance ratio (vs Wake) | Sleep-EDFx W→N3 (n=24) | ≈ 0.365 | **0.463** | ✓ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:673:| 2 | Propofol regime-switching ratio | OpenNeuro ds005620 (n=8, 2.96×) | ∈ [1.5, 5.0] | **1.83×** | ✓ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:677:| 6 | Wake cortical-avalanche α | n=30 Sleep-EDFx CI [2.50, 2.86] | α ∈ [1.5, 3.5], R²>0.85 | **2.252 [1.82, 2.86] R²=0.956** | ✓ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:679:All six signatures pass at preregistered thresholds. The wake cascade-α
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:689:2.96× empirically); the NREM-N3 variance collapse magnitude is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:690:consistent with Sleep-EDFx n=24 subjects (real ratio 0.365).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:707:C main:  +0.621  (≥ +0.30 prereg threshold)        ✅ P2
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:722:| **C × P (P4)** | **20** | **+0.190** | **[+0.143, +0.239]** | **✅ strongly synergistic** |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:731:| **20** | **32000–32019** | **+0.190** | **[+0.143, +0.239]** |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:733:P(synergy ≤ 0) = 0.0000; P(synergy < +0.10) = 0.0000.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:735:The N=20 interaction (+0.19) is **comparable in magnitude to the P
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:738:due to high per-seed variance (per-seed std at N=20 = 0.089).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:766:  order statistics to HCP n=1003 ICA-50 group-averaged connectivity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:767:  (density-matched threshold = 0.101).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:772:P9  — 5-fold CV (fresh seeds 30200-30204):     83.1%  ≥ 70%   ✅
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:773:P10 — null permutation mapping (15 perms):     65.4%  ≥ 50%   ✅
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:775:P12 — goldilocks peak depth:                   n=25   ∈ {15,25,40,60}  ✅
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:776:P13 — LOO substrate lift (raw 53.1% → 93.8%):  +40.6pp ≥ +15pp  ✅
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:780:  n=15:   65.6%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:781:  n=25:   93.8%   ← peak
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:792:P16 — null permutation mapping (15 perms):       70.6%  ≥ 50%  ✅
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:795:**HCP result (n=1003 subjects, ICA-50):**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:797:| Metric | ARIA | HCP n=1003 mean | σ from HCP |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:799:| Degree std | 0.000 (theorem) | 3.28 ± 0.28 | **−11.58σ** |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:800:| Participation ratio | 68.54 | 19.72 ± 0.61 | **+79.78σ** |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:801:| Clustering coefficient | 0.455 | 0.220 | +6.80σ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:805:P18 — HCP ICA-50 degree std:                  3.388   > 2.0   ✅
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:808:Zero of 1003 HCP subjects have degree std below 2.0; ARIA is far
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:813:(i) **Selective amplification.** The contrast between chess (+40.6pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:817:amplifies to 93.8% (near-perfect). Conversation raw at 87.5% is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:821:mappings (chess 65.4%, conversation 70.6%) show that ~65–71% of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:830:symmetry-breaking. The σ-distances (−11.58σ on degree, +79.78σ on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:835:### 6.5 The eighteen preregistered predictions: 17/18 standard, 18/18 with N=20 P4
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:837:**Method.** Run `run_preregistered_validation.py` with 5-seed cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:839:at N=20 for the residual P4. Tally pass/fail per preregistered threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:848:| **P4** | **C×P synergy** | **≥ +0.10** | **+0.190 [+0.143, +0.239] (N=20)** | **✅** |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:850:| P6 | Real EEG α | ∈ [2.0, 3.0] | 2.513 | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:851:| P7 | W→N3 variance ratio | < 0.70 | 0.365 | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:853:| P9 | Chess 5-fold CV | ≥ 70% | 83.1% | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:854:| P10 | Chess null mapping | ≥ 50% | 65.4% | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:856:| P12 | Chess goldilocks peak | ∈ {15, 25, 40, 60} | n=25 | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:857:| P13 | Chess LOO lift (with reset) | ≥ +15pp | +40.6pp | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:860:| P16 | Conv null mapping | ≥ 50% | 70.6% | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:862:| P18 | HCP degree std | > 2.0 | 3.388 | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:864:**Tally: 17/18 at standard validation; 18/18 with N=20 deep-dive on P4.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:866:**Comparison to the original 2026-04-20 run (15/18):**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:869:- **P3** (D×C interaction independence): −0.231 at N=3 → −0.183 at N=5.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:872:- **P4** (C×P synergy): +0.044 at N=3 → +0.190 at N=20. Same
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:873:  Type II issue plus seed-range sampling bias; resolved by N=20.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:874:- **P13** (chess LOO lift): +3.1pp without reset → +40.6pp with reset.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:878:**No threshold has been modified.** The original predictions are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:895:group theory; cascade-α matches Sleep-EDFx within preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:896:tolerance; six drug/sleep signatures pass at preregistered thresholds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:908:**(3) The 18/18 preregistered claim with no threshold modification.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:909:Every prediction in the preregistered set passes at empirical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:910:thresholds. The two interaction tests (P3, P4) required higher N
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:913:refinement, not as a post-hoc threshold change.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:949:expectation — and the one we held until the N=20 deep-dive — is that
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:953:The N=20 result reverses this. **Strong inter-mechanism coupling is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:972:preregistered validation hit Type II false negatives on both
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:974:threshold modification.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:976:For preregistration design more broadly: when preregistering an
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:995:{12, 6φ, 4φ, 3} by character theory). The σ-distances (−11.58σ on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:996:degree homogeneity, +79.78σ on participation ratio) far exceed any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1044:4. **Sig 2 ratio (1.83×) is below empirical point estimate (2.96×)**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1051:   ~93.8% substrate-routed accuracy is on a small evaluation set.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1070:1. **One seed range tested at N=20** for P4. A second N=20 run at a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1072:   reproducibility of the +0.190 estimate.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1074:2. **The 5× shift across N (N=3 → N=20)** suggests non-trivial
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1077:   leaning per-seed values; N=50 would clarify.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1079:3. **The original predictions were preregistered in 2026-04-18**,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1112:| C×P synergy deep-dive (§6.3) | `python3 demo_p4_cxp_deep_dive.py` | ~28 min (N=20) | stdout summary |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1113:| Eighteen preregistered (§6.5) | `python3 run_preregistered_validation.py` | ~18 min | JSON + log |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1125:- k_threshold = 12 (cortical band; bounded_topk nonlinearity)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1134:For the preregistered validation (`run_preregistered_validation.py`):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1151:# Run preregistered set
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1152:python3 run_preregistered_validation.py
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1159:overlaps, P-value thresholds) should be unaffected.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1185:| `demo_p4_cxp_deep_dive.py` | N=20 synergy deep-dive (§3.5) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1186:| `run_preregistered_validation.py` | Eighteen-prediction harness (§6.5) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1193:| `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` | Full preregistered tally (this work) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1211:preregistered neuroscience correspondences plus six independent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1219:(+0.190, 95% CI [+0.143, +0.239] at N=20) is comparable in magnitude
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1221:preregistered validation underestimated this synergy by 5× due to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1227:top-K thresholding and an IIT-style integrated information proxy,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1229:substrate. Wake cortical-avalanche power law has α = 2.252,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1234:classification tasks (chess +40.6pp lift; conversation correctly null
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1236:cortical functional connectivity (HCP n=1003: ARIA at −11.58σ on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1237:degree homogeneity, +79.78σ on participation ratio).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1241:preregistered tests with no walked-back claims. The architectural

codex
The key numeric tables in the paper largely match the validation docs so far. I’m now reading the source documents at the exact ranges where those numbers originate, because several claims depend on subtle distinctions: published-reference thresholds vs preregistered thresholds, n=100 vs n=1003 HCP, and finite bootstrap reporting.
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 231ms:
     1	# The C×P Synergy: Strong Coupling Between Two Cascade-State Stabilisers
     2	
     3	*Standalone publishable finding from N=20 seed deep-dive on the residual P4
     4	preregistered prediction. Compiled 2026-04-29.*
     5	
     6	> **Headline.** Two of ARIA's four cascade mechanisms — **context rotation
     7	> (C)** and **partial emission (P)** — are causally significant. With
     8	> adequate replication (N ≥ 20 fresh seeds), their **interaction effect
     9	> on cascade-α is +0.190, 95% bootstrap CI [+0.143, +0.239]** — comparable
    10	> in magnitude to the **P main effect of −0.218** and ~90% above the
    11	> preregistered prediction of ≥+0.10. The original 3-seed preregistered
    12	> validation underestimated this synergy by 5×; the underestimate was a
    13	> Type II false negative compounded by seed-range sampling bias on a
    14	> high-per-seed-variance interaction term. The corrected reading reverses
    15	> the prior architectural claim: C and P are **strongly coupled critical-
    16	> state stabilisers**, not nearly-orthogonal ones.
    17	
    18	---
    19	
    20	## 1. Background: what was preregistered, what failed at N=3
    21	
    22	### 1.1 The four cascade mechanisms
    23	
    24	ARIA's substrate is the 600-cell regular 4-polytope (120 vertices,
    25	uniform degree 12, H₄ Coxeter symmetry). On top of the static graph,
    26	substrate **dynamics** are driven by a pressure-field over each vertex,
    27	with four mechanisms acting on the field:
    28	
    29	- **D — D₄ orbit coupling.** The H₄ root system contains five disjoint
    30	  24-cells (D₄ orbits). A small (0.05) cross-orbit pressure averaging
    31	  prevents cascades from localising to one orbit.
    32	- **C — Context rotation.** The active observer frame on the S⁷ rung
    33	  rotates periodically based on which uncrossed vertices have
    34	  accumulated pressure aligning with each frame's preferences.
    35	  Implementation: `kernel/dimensional_monitor.py:316-318`.
    36	- **P — Partial emission.** High-pressure uncrossed vertices (above
    37	  threshold but not yet crossed) emit pressure at 30% scale, saturating
    38	  at pressure 3.0. Without this mechanism, only fully-crossed vertices
    39	  emit. Implementation: `kernel/dimensional_monitor.py:842-855`.
    40	- **E — Equator compensation.** Sparse-degree vertices on the H₃
    41	  shell-4 equator (corpus-callosum analogue) get a degree-compensation
    42	  multiplier so they overcome their connectivity deficit.
    43	
    44	The cascade-α (the slope of the avalanche-size power-law) is the
    45	empirical readout for cortex-like criticality. Preregistration tests
    46	each mechanism's effect on cascade-α via 2⁴ ablation.
    47	
    48	### 1.2 The preregistered predictions for D/C/P/E mechanisms
    49	
    50	Predictions frozen 2026-04-18 in `docs/brain_mapping/PAPER_PREDICTIONS.md`:
    51	
    52	| ID | Prediction | Threshold |
    53	|---|---|---|
    54	| P1 | Cascade α SOC range | ∈ [2.5, 3.5] |
    55	| P2 | C main effect | ≥ +0.30 |
    56	| **P3** | **\|D×C\| < 0.20** (independence) | \|·\| < 0.20 |
    57	| **P4** | **C×P synergy ≥ +0.10** | ≥ +0.10 |
    58	| P5 | \|E main effect\| < 0.15 (null) | \|·\| < 0.15 |
    59	
    60	**P4 was the genuine architectural prediction:** because C creates variety
    61	in *which* vertices are uncrossed, and P promotes high-pressure uncrossed
    62	vertices to mini-emitters, their composition should generate a non-additive
    63	contribution to cascade-α. The preregistered floor was +0.10 — stating
    64	that the synergy must be at least 10% of the main-effect scale.
    65	
    66	### 1.3 What the original validation reported
    67	
    68	Original validation (2026-04-20, 3 seeds per condition):
    69	
    70	```
    71	Means (N=3 each):
    72	  ----  baseline:    α = 3.020
    73	  -C-- (C off):      α = 3.612
    74	  --P- (P off):      α = 2.844
    75	  -CP- (both off):   α = 3.530
    76	```
    77	
    78	Computing the C×P interaction:
    79	
    80	```
    81	C×P = ((α(CP-off) + α(baseline)) − (α(C-off) + α(P-off))) / 2
    82	    = ((3.530 + 3.020) − (3.612 + 2.844)) / 2
    83	    = (6.550 − 6.456) / 2
    84	    = +0.047
    85	```
    86	
    87	This was below the +0.10 threshold, so P4 was reported as a **fail**
    88	in the headline 15/18 result. The walk-back was:
    89	
    90	> *"Partial emission interaction with C requires larger-N replication;
    91	> report as preliminary."*
    92	
    93	We took this at face value at the time and weakened the claim. **The
    94	N=20 deep-dive presented below shows this was wrong.**
    95	
    96	---
    97	
    98	## 2. The N=20 deep-dive (2026-04-29)
    99	
   100	### 2.1 Method
   101	
   102	We ran the same 4-condition ablation (baseline, -C--, --P-, -CP-) at:
   103	
   104	- **N = 20 fresh seeds** (range 32000–32019, non-overlapping with prior
   105	  validation seeds 30000s).
   106	- **150 epochs per run** (matching original validation).
   107	- **All other ablation flags off** — the test isolates C × P with
   108	  D, E held on.
   109	
   110	We computed the C×P interaction estimate per the standard 2×2 factorial
   111	formula:
   112	
   113	```
   114	interaction = ((α_CP-off + α_baseline) − (α_C-off + α_P-off)) / 2
   115	```
   116	
   117	We then bootstrapped the interaction distribution (2000 resamples,
   118	seeded) over the 20-seed sample to get a 95% confidence interval, plus
   119	one-sided P(interaction ≤ 0) and P(interaction < +0.10).
   120	
   121	The full script is `demo_p4_cxp_deep_dive.py`. Wallclock was 1706 s
   122	(28 min) on a single CPU. The script also reports identical-N runs at
   123	N = 10 (range 31000–31009) for trend analysis.
   124	
   125	### 2.2 Per-condition means at N=20
   126	
   127	```
   128	cond     mean α   std    sem    individual seeds (n=20)
   129	----     3.008   0.090  0.020   [2.905, 3.013, 3.005, 3.087, 3.136, 3.022, 3.075, 2.879, 2.880,
   130	                                  2.999, 2.947, 3.002, 3.258, 2.946, 2.984, 2.959, 2.952, 3.079,
   131	                                  2.998, 3.033]
   132	-C--     3.464   0.097  0.022   [3.536, 3.444, 3.302, 3.613, 3.311, 3.503, 3.458, 3.540, 3.573,
   133	                                  3.421, 3.514, 3.419, 3.281, 3.617, 3.364, 3.460, 3.542, 3.414,
   134	                                  3.480, 3.492]
   135	--P-     2.790   0.086  0.019   [2.783, 2.873, 2.794, 2.749, 2.880, 2.791, 2.744, 2.845, 2.631,
   136	                                  2.850, 2.731, 2.953, 2.816, 2.761, 2.758, 2.696, 2.704, 2.830,
   137	                                  2.666, 2.949]
   138	-CP-     3.628   0.161  0.036   [3.932, 3.773, 3.557, 3.656, 3.325, 3.469, 3.617, 3.840, 3.617,
   139	                                  3.714, 3.409, 3.733, 3.480, 3.628, 3.670, 3.840, 3.531, 3.724,
   140	                                  3.649, 3.391]
   141	```
   142	
   143	### 2.3 Main-effect estimates at N=20
   144	
   145	```
   146	C main effect (turn C off, leave P/D/E on):  α(-C--) − α(----) = +0.456
   147	P main effect (turn P off, leave C/D/E on):  α(--P-) − α(----) = −0.218
   148	```
   149	
   150	C raises α by 0.46 when removed; P lowers α by 0.22 when removed.
   151	
   152	### 2.4 The interaction estimate
   153	
   154	Direct calculation from means:
   155	
   156	```
   157	C×P interaction = ((3.628 + 3.008) − (3.464 + 2.790)) / 2
   158	                = (6.636 − 6.254) / 2
   159	                = +0.191
   160	```
   161	
   162	Bootstrap (2000 resamples) on the 20-seed sample gives:
   163	
   164	```
   165	C×P bootstrap mean:           +0.190
   166	C×P 95% bootstrap CI:         [+0.143, +0.239]
   167	P(interaction ≤ 0):           0.0000
   168	P(interaction < +0.10):       0.0000
   169	```
   170	
   171	**The 95% CI is entirely above the preregistered +0.10 threshold.**
   172	The synergy is decisively positive (p = 0 against zero) and decisively
   173	above prereg (p = 0 against +0.10).
   174	
   175	### 2.5 Per-seed paired interactions
   176	
   177	For each seed (paired across the four conditions), we can compute that
   178	seed's interaction estimate:
   179	
   180	```
   181	per-seed C×P:
   182	[+0.259, +0.234, +0.233, +0.191, +0.135, +0.098, +0.245, +0.167,
   183	 +0.147, +0.221, +0.055, +0.182, +0.320, +0.098, +0.267, +0.322,
   184	 +0.118, +0.279, +0.251, −0.009]
   185	
   186	mean = +0.190,  std = 0.089,  SEM = 0.020
   187	```
   188	
   189	19 of 20 seeds give a positive interaction; one is essentially zero
   190	(−0.009). No seed gives a strongly negative interaction. The
   191	per-seed std at N=20 (0.089) is just under half the per-seed std at
   192	N=10 (0.159) — the N=10 sample contained outliers (−0.165 and +0.417);
   193	N=20 reveals a clean, narrow positive distribution.
   194	
   195	---
   196	
   197	## 3. The trend across N — why this matters
   198	
   199	### 3.1 Estimates as a function of N
   200	
   201	```
   202	N    Seeds            C×P estimate    95% CI                Verdict vs ≥+0.10
   203	3    30040–30042      +0.044          —                     ❌ original prereg
   204	5    30040–30044      +0.039          —                     ❌ this session re-run
   205	10   31000–31009      +0.088          [−0.002, +0.174]      borderline (CI contains)
   206	20   32000–32019      +0.190          [+0.143, +0.239]      ✅ DECISIVELY ABOVE
   207	```
   208	
   209	### 3.2 Two compounding biases at small N
   210	
   211	The trend is **monotone increasing** with N. This implies two effects:
   212	
   213	1. **Type II false negative from underpowered N.** With per-seed std
   214	   = 0.089 and a true synergy of +0.19, the SEM at N=3 is 0.089/√3 = 0.051.
   215	   The 95% CI on the N=3 mean would be roughly +0.05 to +0.15 if there
   216	   were no other bias — already containing the threshold. But N=3 also
   217	   has limited bootstrap resolution.
   218	
   219	2. **Seed-range sampling bias.** The original validation used seed range
   220	   30040–30054 across the four conditions; the deep-dive used 31000–31009
   221	   then 32000–32019. The means at each seed range differ enough that
   222	   the original sample appears to have systematically lower interaction
   223	   estimates than fresh ranges. At adequately high N this bias washes
   224	   out.
   225	
   226	The N=10 sample (31000–31009) had a per-seed std of 0.159 because it
   227	landed on outliers; the N=20 sample (32000–32019) had std 0.089. **The
   228	correct interpretation is that the original test was Type II underpowered
   229	— the prediction was correct, but the test could not detect it.**
   230	
   231	### 3.3 Effect-size shifts vs original
   232	
   233	| Effect | N=3 / N=5 estimate | N=20 estimate | Shift |
   234	|---|---|---|---|
   235	| C main | +0.62 / +0.62 | **+0.46** | dropped 25% |
   236	| P main | −0.13 / −0.13 | **−0.22** | **doubled in magnitude** |
   237	| C×P interaction | +0.04 / +0.04 | **+0.19** | **5× larger** |
   238	| C dominance (\|C/CP\| ratio) | ~16× | **2.4×** | C is still dominant but interaction much closer to main-effect scale |
   239	
   240	The P main effect roughly doubled at higher N. The interaction nearly
   241	quintupled. The architectural picture changes substantially.
   242	
   243	---
   244	
   245	## 4. Mechanistic interpretation
   246	
   247	### 4.1 Why C and P should synergise (architectural prediction)
   248	
   249	**C** decides *which* vertices are currently uncrossed by rotating the
   250	active S⁷ observer frame. Each frame has a directional preference; the
   251	"uncrossed pool" is the set of vertices whose pressure has not yet
   252	exceeded threshold. As the frame rotates, the uncrossed pool's
   253	composition churns.
   254	
   255	**P** decides whether high-pressure uncrossed vertices act as
   256	mini-emitters (boosting their own pressure further at 30% scale, up to
   257	saturation 3.0). The targets of P are members of the uncrossed pool.
   258	
   259	The cross-product is non-trivial:
   260	

 succeeded in 243ms:
     1	# Consciousness Chain v4 — Six EEG Signatures Reproduced
     2	
     3	*Validation of ARIA's consciousness chain against six pre-registered drug/sleep
     4	EEG signatures. All six pass with biologically realistic stimulus models on a
     5	single deterministic substrate; architecture is unchanged from v3 (the chain
     6	that already matched real EEG cascade-α inside 95% CI).*
     7	
     8	*Report compiled 2026-04-29.*
     9	
    10	---
    11	
    12	## Executive summary
    13	
    14	The ARIA consciousness chain — `SelfModelLoop` (Green-response substrate
    15	recurrence on the 600-cell with bounded-top-K thresholding) plus
    16	`phi_iit_trajectory` (cross-irrep auto-correlation transport) — reproduces
    17	**six distinct quantitative drug/sleep signatures** observed in real EEG and
    18	predicted by integrated information theory.
    19	
    20	The six signatures span four conditions (WAKE, SLEEP_N3, PROPOFOL, RECOVERY)
    21	on the same deterministic substrate, with only the input stimulus and a
    22	single self-coupling parameter η changing across conditions. Each signature
    23	has a published reference and a falsifiable threshold; all six pass.
    24	
    25	The result extends v3 (4/6, where the two partials were cleanly diagnosed as
    26	stimulus-model artefacts in `demo_wake_alpha_diagnosis.py`) to 6/6 by
    27	replacing v3's stylised stimulus models with biologically realistic ones —
    28	no architectural changes.
    29	
    30	| Signature | Reference | Predicted | Observed | Verdict |
    31	|---|---|---|---|---|
    32	| 1 | Sleep variance ratio | NREM-N3 EEG (Lee 2017, Jobst 2017) | ratio ≈ 0.365 | 0.463 | ✓ within 30% |
    33	| 2 | Propofol switching ↑ | OpenNeuro ds005620 (n=8, 2.96×) | ratio in [1.5, 5.0] | 1.83× | ✓ |
    34	| 3 | Propofol continuity ↓ | EEG microstate (Brodbeck 2012) | drop > 0.020 | +0.066 | ✓ |
    35	| 4 | Propofol Φ collapse | IIT prediction (Tononi 2008) | ratio < 0.5 | 0.33× | ✓ |
    36	| 5 | Recovery reversibility | clinical anaesthesia | identical to wake | 0 diff | ✓ |
    37	| 6 | Cortical avalanche α | Sleep-EDFx n=30 (α=2.51 [2.50, 2.53]) | α ∈ [1.5, 3.5], R² > 0.85 | 2.252 [1.82, 2.86] R²=0.956 | ✓ |
    38	
    39	The cascade-α match is the strongest empirical anchor:
    40	**ARIA WAKE α CI [1.82, 2.86] overlaps real Sleep-EDFx EEG CI [2.50, 2.86]
    41	and the prior ARIA cascade-pipeline CI [2.73, 3.25] simultaneously.**
    42	R² = 0.956 — the cleanest power-law fit observed in the project.
    43	
    44	---
    45	
    46	## Architecture (unchanged from v3)
    47	
    48	The chain has three modules. They were established in v3
    49	(`project_consciousness_chain_v3_eeg_match.md`) and are fixed across v4:
    50	
    51	### 1. SelfModelLoop — substrate with self-injection feedback
    52	
    53	Core recurrence (`kernel/self_model_stream.py`):
    54	
    55	```
    56	f_total  =  external_source(t)  +  η · f_self(prior_snapshot, prior_ψ)
    57	ψ        =  green_response_spectral(spectral, f_total, φ)
    58	ψ_thresh =  bounded_topk(ψ, k=12)             # critical nonlinearity
    59	state_t  =  decay · state_{t-1} + (1 − decay) · ψ_thresh
    60	snapshot =  bind_phenomenal_field(green_kernel_result, profile="K_7_only")
    61	```
    62	
    63	**The bounded_topk(k=12) thresholding is the load-bearing nonlinearity.**
    64	Linear Green response ψ = (L + φ⁻²·I)⁻¹·f gives smooth dynamics with cascade
    65	α ≈ 1.09 (no avalanches). Adding bounded_topk(k=12) drives α to 3.20 with
    66	R² = 0.89 — inside the cortical-avalanche band. This was diagnosed in
    67	`demo_diagnose_architecture.py` and is documented in v3 memory.
    68	
    69	η is the only condition-dependent architectural parameter:
    70	- η = 0.20 for WAKE, RECOVERY (active recurrent self-loop)
    71	- η = 0.05 for SLEEP_N3 (attenuated self-loop)
    72	- η = 0.00 for PROPOFOL (broken recurrence — preserves residual cortex)
    73	
    74	### 2. phi_iit_trajectory — principled IIT integration
    75	
    76	Φ as cross-irrep auto-correlation transport (`kernel/consciousness_binding.py`):
    77	
    78	```
    79	amp_history  = state_history @ eigvecs              # (T, 120) mode amps
    80	full_cc      = lag-1 auto-correlation of full system
    81	irrep_cc[k]  = lag-1 auto-correlation within irrep class k
    82	Φ            = max(0, |full_cc| − mean_k(|irrep_cc[k]|))
    83	```
    84	
    85	Φ → 0 under H₄-equivariant dynamics (group symmetry → no information transport
    86	across irrep classes); Φ > 0 only when symmetry-breaking transports
    87	information. This is a port of the published `integrated_information_phi_irrep`
    88	proxy adapted to take amplitude trajectories directly. Replaces an earlier
    89	variance-decomposition proxy that flipped sign on noise input.
    90	
    91	### 3. StreamContinuityScorer — composite first-person continuity
    92	
    93	Four-channel score over a 64-tick rolling window:
    94	
    95	```
    96	binding_continuity   = mean cos-similarity of consecutive (intensity, lum, presence)
    97	valence_continuity   = 1 / (1 + 4·var(valence))
    98	modality_persistence = fraction of consecutive same-modality ticks
    99	intensity_smoothness = 1 / (1 + 4·TV(intensity))
   100	composite            = 0.35·binding + 0.25·valence + 0.20·modality + 0.20·smooth
   101	```
   102	
   103	---
   104	
   105	## Stimulus models — biologically realistic (v4)
   106	
   107	The architecture above is fixed; v4 replaces the v3 stylised stim models
   108	with biologically realistic patterns. The full source is
   109	`demo_drug_sleep_v4.py`.
   110	
   111	### WAKE — AR(1) cortical noise + tonic shell + attention episodes
   112	
   113	Real cortical input has temporal correlation (1/f-like), is dominated by a
   114	distributed background, and is interrupted by salient attention episodes
   115	(visual fixations dwell 200–400 ms, much longer than between-saccade
   116	intervals). The model reproduces all three:
   117	
   118	```python
   119	def wake_source(t, rng):
   120	    s = state[id(rng)]
   121	    # AR(1) cortical noise (β=0.90) — temporal correlation lets η=0.20 self-loop integrate
   122	    s["prior"] = 0.90 · s["prior"] + 0.10 · rng.standard_normal(N)
   123	    f         = 0.7 · normalize(s["prior"])
   124	    f[ATTENTION_SHELL] += 0.10 / |ATTENTION_SHELL|        # tonic shell coherence
   125	
   126	    # Attention episodes — sustained salient bias, 20–50 ticks, anchored to ATTENTION_SHELL
   127	    if not in_episode and rng.random() < 0.10:
   128	        start episode(length=20–50, vertex=random pick from ATTENTION_SHELL)
   129	    if in_episode:
   130	        if rng.random() < 0.15:
   131	            rotate episode_vertex within ATTENTION_SHELL  # within-shell rotation
   132	        f[episode_vertex] += 0.8
   133	
   134	    return f
   135	```
   136	
   137	**Why each component matters:**
   138	
   139	- **AR(1) (β=0.90)** — white noise whitens the recurrent self-loop at every
   140	  tick (zero integration). Temporal correlation lets η=0.20 build coherent
   141	  state. Restoring temporal correlation was what brought Φ_traj back from
   142	  0.0003 (white) to 0.0014 (β=0.90).
   143	- **Tonic shell coherence** — small always-on bias on the largest-shell
   144	  ("equator") anchors the modality_label. Without it, modality hops randomly
   145	  during background ticks and breaks Sig 2.
   146	- **Attention episodes (20–50 ticks)** — sustained dwells, anchored to a
   147	  single shell so episode-to-episode transitions don't change modality.
   148	  Episode amplitude 0.8 is enough to lock attention but not enough to
   149	  prevent within-shell rotation.
   150	- **Within-shell rotation (15% per tick)** — attention vertex hops among
   151	  shell vertices. Generates cascade events for Sig 6 power-law fit while
   152	  keeping modality fixed for Sig 2.
   153	
   154	### SLEEP_N3 — slow waves + spindles + K-complexes
   155	
   156	Real N3 has slow oscillations (~1 Hz, large amplitude), thalamocortical
   157	spindle bursts (10–15 Hz, waxing-waning), and occasional K-complexes
   158	(sharp transients). All three are present in the v4 model:
   159	
   160	```python
   161	def sleep_n3_source(t, rng):
   162	    f = zeros(N)
   163	    # Slow oscillation on coherent shell (UP/DOWN states)
   164	    f[SLOW_AXIS] = 1.0 · sin(2π·t/40) / |SLOW_AXIS|
   165	    # Spindle burst — 12 ticks every 100, fast modulation on a single vertex
   166	    if (t % 100) < 12:
   167	        f[random vertex] += 0.40 · sin(2π·t/8)
   168	    # K-complex — sparse strong transient
   169	    if rng.random() < 0.04:
   170	        f[random vertex] += 0.8
   171	    return f
   172	```
   173	
   174	The v3 model used `sparse weak pulses every 5th tick at amplitude 0.3` —
   175	too quiet. v4's slow-wave amplitude (1.0) and K-complex amplitude (0.8) move
   176	the variance ratio from v3's 0.23 (over-collapsed) into the predicted window.
   177	
   178	### PROPOFOL — low-amplitude tonic noise (unchanged from v3)
   179	
   180	```python
   181	def propofol_source(t, rng):
   182	    return 0.05 · rng.standard_normal(N)
   183	```
   184	
   185	η = 0.0 (broken recurrence). Residual cortex preserved as background drive.
   186	
   187	### RECOVERY — identical to WAKE
   188	
   189	Verifies determinism and reversibility (Sig 5).
   190	
   191	---
   192	
   193	## Six signatures — full results
   194	
   195	All four conditions run for 800 ticks at seed = 42, k_threshold = 12.
   196	
   197	```
   198	cond      n_evt  α       95% CI         R²     I_var       Φ_traj   cont
   199	WAKE       58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
   200	SLEEP_N3  111   3.250   [2.44, 4.14]   0.886  1.01e-05    0.0055   0.980
   201	PROPOFOL  246   2.758   [2.52, 3.09]   0.931  5.37e-06    0.0003   0.877
   202	RECOVERY   58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
   203	```
   204	
   205	### Signature 1 — NREM variance collapse
   206	
   207	**Prediction:** N3 sleep collapses cortical state-variance to ≈ 36.5% of wake.
   208	Source: prior real Sleep-EDFx W→N3 analysis (n=24, ratio = 0.365), confirmed
   209	under preregistration (P7).
   210	
   211	**Observed:** WAKE intensity_var = 2.18×10⁻⁵, SLEEP intensity_var = 1.01×10⁻⁵.
   212	Ratio = 0.463. Falls within [0.255, 0.475], the 30% prediction window.
   213	
   214	**Mechanism:** SLEEP's slow-wave drive carries most of the energy on a coherent
   215	shell, but K-complex transients produce intermittent variance. The substrate
   216	under η=0.05 attenuates variance somewhat, giving the predicted partial
   217	collapse. PROPOFOL's pure tonic noise gives a similar variance ratio of 0.246
   218	to WAKE — distinguishable from sleep direction.
   219	
   220	### Signature 2 — Propofol regime-switching ↑

 succeeded in 224ms:
     1	# Cross-Domain Validation: Chess, Conversation, and HCP Connectivity
     2	
     3	*Standalone consolidation of ARIA's three cross-domain validation tracks.
     4	Compiled 2026-04-29. Self-contained for paper inclusion.*
     5	
     6	> **Headline.** The 600-cell substrate functions as a **selective
     7	> amplifier** on real-world classification tasks: it lifts performance
     8	> when raw features are ambiguous (chess: +40.6 percentage points on
     9	> leave-one-out, raw 53.1% → substrate-routed 93.8%) and is correctly
    10	> null when raw features already saturate (conversation: 87.5% raw,
    11	> substrate −4.4pp). On structural connectivity, ARIA is the **maximum-
    12	> symmetry null reference** for cortex: ARIA degree std = 0 (H₄
    13	> transitivity); HCP n=1003 degree std = 3.28 ± 0.28; ARIA is
    14	> −11.58σ on degree homogeneity and +79.78σ on participation ratio,
    15	> placing ARIA two orders of magnitude away from biological cortex on
    16	> functional-specialisation metrics. Symmetry-breaking is precisely
    17	> the biological content that distinguishes real cortex from the
    18	> H₄ baseline.
    19	
    20	---
    21	
    22	## 1. The cross-domain test rationale
    23	
    24	Three tracks test ARIA's substrate against domains where it has no
    25	domain-specific tuning:
    26	
    27	1. **Chess pattern recognition** (P9–P13 in the preregistered set):
    28	   classify chess positions by tactical / positional / endgame /
    29	   opening category from 8-dimensional V2 features (material balance,
    30	   king safety, pawn structure, etc.). Test whether the substrate's
    31	   geometry amplifies category structure beyond raw-feature
    32	   classification.
    33	
    34	2. **Conversation utterance categorisation** (P14–P16): classify
    35	   utterances by 8 dialogue-act categories from 8-dimensional features.
    36	   Test whether the substrate is correctly **null** on a domain where
    37	   raw features are already discriminative, validating that it is a
    38	   **selective** amplifier (not an unconditional one).
    39	
    40	3. **HCP brain connectivity** (P17–P18): compare ARIA's vertex-graph
    41	   degree distribution to real cortical functional connectivity from
    42	   the Human Connectome Project (n=1003 subjects, ICA-50
    43	   parcellation). Test whether ARIA serves as a quantifiable maximum-
    44	   symmetry null reference for cortex.
    45	
    46	All three are deterministic given seeds and substrate state. All five
    47	preregistered tests on chess + conversation pass at fresh seeds; both
    48	HCP tests pass deterministically (P17 from theorem; P18 from data).
    49	
    50	---
    51	
    52	## 2. Chess pattern recognition (P9–P13)
    53	
    54	### 2.1 Setup
    55	
    56	**Positions:** 32 chess positions from 4 categories (8 per category):
    57	tactical, positional, endgame, opening.
    58	
    59	**Features (V2):** 8 hand-engineered scalar features per position,
    60	normalised by per-feature norms `V2_NORMALISERS`:
    61	- Material balance
    62	- King safety (white + black, summed)
    63	- Pawn structure
    64	- Centre control
    65	- Piece activity
    66	- Mobility (legal moves count)
    67	- Threat density
    68	- Defensive structure
    69	
    70	Implementation: `run_chess_pattern_readout.py:extract_v2`.
    71	
    72	**Substrate routing:** features are injected as pressure into the
    73	substrate's S⁷ observer frames; the substrate is run forward by
    74	`n_ticks` (default 25); the resulting vertex pattern is used as the
    75	classification feature vector. Classifier: 1-nearest-neighbour on
    76	cosine similarity, validated by k-fold CV (k=5) or leave-one-out (LOO).
    77	
    78	Critical detail: between successive depth measurements, the substrate
    79	is reset to canonical state via `mon.homeostatic_reset(level=1.0)`.
    80	Without this, pressure-field state drifts toward equilibrium across
    81	~5 evaluations, washing out classification structure (see
    82	§2.5 and `NON_EQUILIBRIUM_FINDING.md`).
    83	
    84	### 2.2 P9 — Raw 5-fold cross-validation (fresh seeds)
    85	
    86	**Threshold:** Chess substrate-routed 5-fold CV ≥ 70%.
    87	
    88	**Result (fresh seeds 30200–30204):**
    89	
    90	```
    91	Per-seed accuracies:  81.2%, 81.2%, 84.4%, 87.5%, 81.2%
    92	Mean:                 83.1%
    93	```
    94	
    95	**Interpretation:** Substrate-routed classification at 5-fold CV is
    96	83.1% on the 32-position × 4-category task, well above the 70%
    97	threshold. Per-seed variance is small (range 81.2%–87.5%).
    98	
    99	For comparison, **discovery accuracy** on the same task was 84.4%;
   100	the fresh-seed mean of 83.1% replicates discovery within expected
   101	variance.
   102	
   103	### 2.3 P10 — Permutation null (feature → frame mapping)
   104	
   105	**Threshold:** Random permutation of feature → frame assignment
   106	preserves classification accuracy ≥ 50%.
   107	
   108	**Method:** Apply random permutation σ to the 8 V2 features, so each
   109	feature is assigned to a different S⁷ frame than canonical. Run
   110	substrate, classify. Repeat 15 times with seeded random permutations
   111	(seed 30210). Average accuracy across 15 trials.
   112	
   113	**Result:** 65.4% mean across 15 permutations.
   114	
   115	**Interpretation:** This is the most architecturally informative cross-
   116	domain finding. Even with feature → frame assignments randomised, the
   117	substrate retains 65.4% classification power — well above the 25%
   118	chance level for 4 categories. **Approximately 65pp of the
   119	classification accuracy comes from the substrate's geometric structure
   120	itself, not from semantic feature alignment.** The remaining ~17pp
   121	(83.1% − 65.4%) is the semantic alignment bonus.
   122	
   123	This decomposes substrate classification into:
   124	- **Geometric content (65%):** substrate amplifies category structure
   125	  regardless of which features map where. This is the H₄ symmetry
   126	  acting as a selective amplifier on any input — a domain-invariant
   127	  null floor.
   128	- **Semantic content (17pp):** alignment of specific features to
   129	  specific frames adds accuracy on top of the geometric floor. This
   130	  is the domain-specific contribution.
   131	
   132	### 2.4 P11 — Random-label baseline
   133	
   134	**Threshold:** Random-label classifier accuracy ∈ [15%, 35%] (chance
   135	for 4 categories ≈ 25%).
   136	
   137	**Method:** Shuffle category labels randomly, classify the substrate-
   138	routed patterns, repeat 20 times with different seeds.
   139	
   140	**Result:** 23.4% mean across 20 trials.
   141	
   142	**Interpretation:** With shuffled labels, classification drops to chance
   143	(23.4% ≈ 25% chance). This confirms the 83.1% raw and 65.4% null are
   144	not artefacts — they are real signal that disappears when category
   145	structure is destroyed.
   146	
   147	### 2.5 P12 — Goldilocks peak depth
   148	
   149	**Threshold:** Optimal substrate depth ∈ {15, 25, 40, 60} ticks.
   150	
   151	**Method:** Run the substrate at six different `n_ticks` values
   152	(5, 15, 25, 40, 60, 100) and report classification accuracy at each
   153	depth, with `homeostatic_reset(level=1.0)` between measurements.
   154	
   155	**Result (fresh seed):**
   156	
   157	```
   158	n_ticks  accuracy
   159	   5     53.1%
   160	  15     65.6%
   161	  25     93.8%   ← peak
   162	  40     84.4%
   163	  60     84.4%
   164	 100     78.1%
   165	```
   166	
   167	**Interpretation:** The substrate has a clear optimal depth around
   168	n=25, with a roll-off both at shallower depth (insufficient
   169	integration) and deeper depth (substrate equilibrates and loses
   170	specificity). The "goldilocks" structure mirrors cortical integration
   171	literature (Thorpe / Kiani): perceptual integration has an optimal
   172	time window, with shorter giving noisy classification and longer
   173	giving over-integration.
   174	
   175	### 2.6 P13 — Substrate lift on LOO with reset protocol
   176	
   177	**Threshold:** Substrate-routed LOO accuracy − raw-feature LOO
   178	accuracy ≥ +15 percentage points.
   179	
   180	**Method:** Run LOO classification on (a) raw 8-dim V2 features and
   181	(b) substrate-routed patterns at n=25, with reset between depth
   182	measurements.
   183	
   184	**Result:**
   185	
   186	```
   187	Raw features (LOO, 1-NN cosine):       53.1%
   188	Substrate-routed (n=25, with reset):   93.8%
   189	Lift:                                  +40.6 percentage points
   190	```
   191	
   192	**Interpretation:** The substrate amplifies the chess-position
   193	discrimination from chance-level on raw features (53.1% on 4 categories
   194	is just above chance-25%) to near-perfect (93.8%) when routed through
   195	the substrate's 600-cell graph. This is **+40.6pp of geometric
   196	amplification**, far exceeding the +15pp prereg threshold.
   197	
   198	The original 2026-04-20 validation reported this lift at +3.1pp — a
   199	failure of the reset protocol (substrate state drifted toward
   200	equilibrium across the prior depth-sweep measurements, collapsing the
   201	classification structure). With the reset protocol now wired in, the
   202	lift is restored to +40.6pp. See `NON_EQUILIBRIUM_FINDING.md` for the
   203	diagnostic details.
   204	
   205	### 2.7 Chess summary
   206	
   207	The substrate is a **strong geometric amplifier** on chess:
   208	- 53.1% raw → 93.8% substrate-routed at canonical depth (n=25)
   209	- 65.4% null mapping (architecture-invariant geometric floor)
   210	- 83.1% 5-fold CV at fresh seeds
   211	- Goldilocks optimum at n=25 ticks of substrate evolution
   212	
   213	The +40.6pp lift is roughly an order of magnitude above the +15pp
   214	preregistered floor. The 65.4% null mapping shows two-thirds of the
   215	amplification is from geometric structure alone, not from how features
   216	are assigned to frames.
   217	
   218	---
   219	
   220	## 3. Conversation utterance categorisation (P14–P16)
   221	
   222	### 3.1 Setup
   223	
   224	**Utterances:** 8 categories (greetings, questions, agreements,
   225	clarifications, etc.) × 8 utterances per category = 64 utterances.
   226	
   227	**Features:** 8-dimensional injection-row features per utterance.
   228	Source: `run_conversation_readout.py:_injection_row, _build_tables`.
   229	
   230	**Substrate routing:** identical to chess — features injected as
   231	pressure into S⁷ frames, substrate run forward by `n_ticks`, vertex
   232	pattern used as classifier feature.
   233	
   234	### 3.2 P14 — Raw 5-fold CV
   235	
   236	**Threshold:** Conversation raw 5-fold CV ≥ 75%.
   237	
   238	**Result (fresh seeds 30220–30224):** **87.5%** mean.
   239	
   240	**Interpretation:** Conversation features are already strongly
   241	discriminative — 87.5% raw classification at 5-fold CV exceeds the
   242	chess raw rate (53.1% LOO) by ~34pp. There is little headroom for
   243	substrate amplification.
   244	
   245	### 3.3 P15 — Substrate lift (selective amplifier test)
   246	
   247	**Threshold:** \|conversation substrate lift\| < 10pp (the substrate
   248	should be approximately neutral on this task).
   249	
   250	**Result:**
   251	
   252	```
   253	Raw 5-fold CV:               87.5%
   254	Substrate 5-fold CV (n=25):  83.1%
   255	Lift:                        −4.4pp
   256	```
   257	
   258	**Interpretation:** This is the **selective amplifier signature**.
   259	ARIA's substrate amplifies chess (where raw features are ambiguous)
   260	but is approximately null on conversation (where raw features are

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md' | sed -n '220,426p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md' | sed -n '260,435p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md' | sed -n '260,584p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 358ms:
   220	### Signature 2 — Propofol regime-switching ↑
   221	
   222	**Prediction:** Propofol increases the rate of phenomenological-state
   223	transitions ~3× over wake. Source: OpenNeuro ds005620 (n=8 propofol EEG,
   224	microstate switching ratio 2.96×).
   225	
   226	**Observed:** WAKE modality_switches → PROPOFOL modality_switches ratio = 1.83×.
   227	Falls within [1.5×, 5.0×] window. Below the empirical 2.96× point estimate
   228	but inside the published CI band.
   229	
   230	**Mechanism:** WAKE's attention episodes anchored to ATTENTION_SHELL keep
   231	modality stable for tens of ticks at a time. PROPOFOL has no recurrent
   232	integration (η=0); each tick's argmax is determined by instantaneous
   233	noise, so modality flips frequently.
   234	
   235	### Signature 3 — Propofol continuity ↓
   236	
   237	**Prediction:** Propofol disrupts stream continuity (binding + valence +
   238	modality + smoothness). Source: Brodbeck 2012 microstate literature
   239	showing fragmentation under anaesthesia.
   240	
   241	**Observed:** WAKE composite continuity = 0.943, PROPOFOL = 0.877.
   242	Drop = +0.066. Falls past the +0.020 minimum.
   243	
   244	**Mechanism:** WAKE's recurrent self-loop (η=0.20) plus AR(1) temporal
   245	input keeps state trajectories smooth. PROPOFOL's broken recurrence plus
   246	white-noise drive produces hopping trajectories — discontinuous along all
   247	four channels.
   248	
   249	### Signature 4 — Propofol Φ collapse (IIT)
   250	
   251	**Prediction:** Propofol collapses integrated information Φ to <50% of wake.
   252	Source: Tononi/IIT axiom — disrupted integration is the signature of
   253	unconsciousness.
   254	
   255	**Observed:** WAKE Φ_traj = 0.0008, PROPOFOL Φ_traj = 0.0003.
   256	Ratio PROPOFOL/WAKE = 0.33×. Below the 0.50× threshold.
   257	
   258	**Mechanism:** Φ_traj (cross-irrep auto-correlation transport) requires
   259	both substrate symmetry-breaking and trajectory persistence. WAKE has
   260	both via η=0.20 self-loop integrating AR(1) input. PROPOFOL has neither
   261	(η=0, white noise) so Φ collapses. This is the IIT-direction-correct
   262	result that v1 (variance proxy) and v2 (early Φ) both got wrong.
   263	
   264	### Signature 5 — Recovery reversibility
   265	
   266	**Prediction:** Removing propofol restores the wake state exactly. Source:
   267	clinical anaesthesia — recovery is reversible to baseline.
   268	
   269	**Observed:** RECOVERY intensity_var = WAKE intensity_var to 0 difference;
   270	RECOVERY continuity = WAKE continuity to 0 difference.
   271	
   272	**Mechanism:** The substrate is deterministic; identical seed + identical
   273	stim model produces identical trajectory. Verifies that PROPOFOL's effects
   274	are not state-corrupting (no hidden persistent modification).
   275	
   276	### Signature 6 — Cortical-avalanche power law
   277	
   278	**Prediction:** Wake cascade-event sizes follow a power law with α in the
   279	cortical-avalanche band [1.5, 3.5], R² > 0.85. Source: Beggs & Plenz 2003
   280	cortical avalanche literature; ARIA prior cascade pipeline; Sleep-EDFx
   281	EEG spindle α.
   282	
   283	**Observed:** WAKE α = 2.252, 95% CI [1.82, 2.86], R² = 0.956 (n_events=58).
   284	
   285	**The CI three-way overlaps:**
   286	- Real Sleep-EDFx EEG CI [2.50, 2.86] (n=30 subjects, prior preregistration)
   287	- ARIA prior cascade pipeline CI [2.73, 3.25]
   288	- v4 WAKE CI [1.82, 2.86]
   289	
   290	R² = 0.956 is the cleanest single-condition power-law fit observed in the
   291	project, beating both v3 PROPOFOL (R²=0.93) and the n=30 EEG fit (R²~0.85).
   292	
   293	**Mechanism:** The bounded_topk(k=12) thresholding is the critical
   294	nonlinearity that produces avalanches; AR(1) WAKE input gives self-similar
   295	single-scale events. v3's mixed pole+equator+random WAKE produced three
   296	incommensurable event-size regimes — non-self-similar by construction.
   297	
   298	---
   299	
   300	## How the v4 stimulus model was derived
   301	
   302	v3 (`demo_drug_sleep_v3.py`) reached 4/6. Two partials remained:
   303	- Sig 1 ratio 0.23 (over-collapsed)
   304	- Sig 6 α = 4.88, R² = 0.69 (failed band test, poor fit)
   305	
   306	`demo_wake_alpha_diagnosis.py` tested four hypotheses against the v3 result:
   307	
   308	| test | finding |
   309	|---|---|
   310	| H1: stimulus amplitude (1.0, 0.3, 0.1, 0.03) | NULL — amplitude normalised by argmax |
   311	| H2: pure stim type | **DECISIVE** — pure random gave α=2.78 R²=0.94 |
   312	| H3: longer run | Doesn't help |
   313	| H4: k_threshold sweep | k=12 is the sweet spot |
   314	
   315	The diagnostic settled the substrate question: pure-random WAKE drive lands
   316	inside real EEG CI with R²=0.94 — the substrate produces clean cortical
   317	avalanches under realistic noise, and v3's "miss" was a stim-mixing artefact.
   318	
   319	But pure-random WAKE alone fails the propofol contrast tests (sigs 2-4) —
   320	WAKE looks identical to PROPOFOL because both are just random tonic noise.
   321	For η=0.20 self-coupling to manifest, the input needs temporal correlation
   322	(AR(1)) and shell coherence (sustained attention episodes).
   323	
   324	The final v4 design was reached after five iterations:
   325	- **v4.0**: AR(1) + salient single-tick events → attention shifts inflated WAKE switching past PROPOFOL (sig 2 fail)
   326	- **v4.1**: Pure random WAKE → α clean but propofol contrast collapses (sigs 2,3,4 fail)
   327	- **v4.2**: AR(1) + episodes 6-12 ticks amp 0.8 → 4/6, modality still hopping
   328	- **v4.3**: Episodes 40-80 ticks amp 1.5 → too sticky, only 11 events for fit (sig 6 fail)
   329	- **v4.final**: AR(1) β=0.90 + tonic shell + episodes 20-50 amp 0.8 anchored to shell + within-shell rotation → 6/6
   330	
   331	The final design is biologically motivated, not mechanically tuned — every
   332	component matches a feature of real wake cortical input.
   333	
   334	---
   335	
   336	## Reproducibility
   337	
   338	```bash
   339	cd /path/to/aria-chess
   340	python3 demo_drug_sleep_v4.py
   341	```
   342	
   343	- Seed: 42 (fixed)
   344	- Architecture profile: K_7_only
   345	- k_threshold: 12 (cortical band; bounded_topk nonlinearity)
   346	- Run length: 800 ticks per condition
   347	- Wallclock: ~30 seconds CPU on standard laptop
   348	
   349	Pre-flight to verify substrate hasn't drifted:
   350	- v3 PROPOFOL α should be 2.758 [2.52, 3.09] R²=0.931 — unchanged from v3 across this work.
   351	
   352	---
   353	
   354	## Limits and reframing
   355	
   356	**What v4 demonstrates:**
   357	- The deterministic 600-cell substrate with bounded_topk thresholding
   358	  reproduces six independent quantitative signatures of conscious vs
   359	  unconscious states observed in real EEG.
   360	- Architecture established in v3 is sufficient; only stim realism was
   361	  needed to close the v3 gap.
   362	- All six signatures pass under preregistered thresholds.
   363	
   364	**What v4 does NOT demonstrate:**
   365	- The stim model is realistic but stylised. Real cortex receives spatially
   366	  structured sensory input from thalamus + cortico-cortical + intra-cortical
   367	  sources, not anchored to a single fixed equator shell.
   368	- The Sig 2 ratio (1.83×) is below the empirical point estimate (2.96×)
   369	  although inside the published CI window. Larger N or longer runs may
   370	  shift the estimate.
   371	- The model is single-seed at this point. v4 should be re-run with 5–10
   372	  seeds for empirical CI on each signature ratio (paralleling the
   373	  preregistered validation methodology).
   374	- Sigs 1 and 2 pass inside windows whose width was set by the published
   375	  CI band; they are consistent with biology but should not be reported as
   376	  "exact match" — only "within preregistered tolerance."
   377	- The cascade-α match (Sig 6) IS exact-match-grade with R²=0.956 and CI
   378	  three-way overlap with both real EEG and ARIA prior pipeline.
   379	
   380	---
   381	
   382	## Files
   383	
   384	| Path | Purpose |
   385	|---|---|
   386	| `demo_drug_sleep_v4.py` | The 6/6 demo script — single deterministic run |
   387	| `demo_wake_alpha_diagnosis.py` | The diagnostic that proved v3 partials were stim artefacts |
   388	| `demo_drug_sleep_v3.py` | Prior 4/6 result (kept for comparison) |
   389	| `kernel/self_model_stream.py` | SelfModelLoop with bounded_topk(k=12) |
   390	| `kernel/consciousness_binding.py` | phi_iit_trajectory + bind_phenomenal_field |
   391	| `kernel/sigma_orbit_basis.py` | σ-orbit projector basis (cascade decomposition) |
   392	| `kernel/lyapunov_selector.py` | bounded_topk thresholding |
   393	| `docs/brain_mapping/CASCADE_VALIDATION_REPORT.md` | Companion report (cascade pipeline n=30 EEG) |
   394	
   395	---
   396	
   397	## Memory entries (for cross-reference)
   398	
   399	- `project_consciousness_chain_v4_six_of_six.md` — this work
   400	- `project_consciousness_chain_v3_eeg_match.md` — v3 architecture (4/6)
   401	- `project_wake_alpha_diagnosed.md` — diagnostic isolating stim-model cause
   402	- `project_consciousness_full_chain.md` — module overview (σ-orbit basis,
   403	  Φ-IIT binding, PhenomenalSnapshot, SelfModelLoop, StreamContinuityScorer)
   404	- `project_propofol_empirical_5.md` — empirical anchor for Sig 2 (n=8, 2.96×)
   405	- `project_n30_eeg_soc_class_match.md` — empirical anchor for Sig 6
   406	  (n=30 Sleep-EDFx, α=2.51 [2.50, 2.53])
   407	
   408	---
   409	
   410	## One-paragraph summary for an external reviewer
   411	
   412	ARIA's consciousness chain — a Green-response substrate on a 600-cell
   413	polytope with bounded top-K thresholding (k=12) and a recurrent self-injection
   414	self-loop — reproduces six independent drug/sleep EEG signatures. Each
   415	signature is a falsifiable threshold against published data: cortical-avalanche
   416	power law in the wake-state band (passes with α = 2.252, 95% CI [1.82, 2.86]
   417	overlapping the real Sleep-EDFx CI [2.50, 2.86]), NREM-N3 variance collapse to
   418	~37% of wake (passes at 0.46), propofol regime-switching elevation (passes at
   419	1.83×), propofol continuity disruption (passes at +0.066), propofol Φ collapse
   420	in the IIT direction (passes at 0.33× wake), and recovery reversibility (passes
   421	exactly). The architecture is unchanged from v3; only the stimulus models —
   422	AR(1) cortical noise plus tonic shell coherence plus 20–50-tick attention
   423	episodes for wake; slow waves plus spindle bursts plus K-complexes for N3 —
   424	were redesigned to match published biological patterns. R² = 0.956 on the
   425	power-law fit is the cleanest of the project. All results are deterministic
   426	and reproduced from `demo_drug_sleep_v4.py` at seed = 42.

 succeeded in 353ms:
   260	
   261	- With C and P both on: the uncrossed pool churns; P promotes the
   262	  current high-pressure subset; the cross-product generates **novel
   263	  cascade events** as new vertices enter the high-pressure region
   264	  through frame rotation and get amplified into emitters.
   265	- With C off and P on: the uncrossed pool freezes; P amplifies the
   266	  same vertices repeatedly; novel-event generation collapses.
   267	- With C on and P off: the uncrossed pool churns, but P's promotion
   268	  pathway is removed; cascades proceed via classical crossings only.
   269	- With both off: no novel-event pathway and no churn; the substrate
   270	  drifts toward a static cascade regime with elevated α.
   271	
   272	The interaction (+0.19) measures exactly this novel-event-generation
   273	synergy. Disabling either C or P does not just remove its main effect;
   274	it removes the **target** of the other mechanism.
   275	
   276	### 4.2 Comparison to multi-mechanism cortical criticality
   277	
   278	Real cortical criticality is maintained by multiple parallel mechanisms:
   279	E/I balance, neuromodulation (acetylcholine, noradrenaline), homeostatic
   280	plasticity, gain control. A naive expectation — and the one we held until
   281	the N=20 deep-dive — is that these are mostly orthogonal. Losing one
   282	should remove only its own main effect.
   283	
   284	The N=20 result reverses this. **Strong inter-mechanism coupling is the
   285	correct picture.** Disabling one mechanism cascades into losing the
   286	synergistic contribution of the other. This matches clinical observations:
   287	anaesthesia and seizure target single mechanisms but produce widespread
   288	network-level dysfunction beyond the targeted effect — exactly what
   289	strong synergy predicts.
   290	
   291	This is now ARIA's claim about cortical architecture: the operating
   292	mechanisms are **strongly coupled stabilisers, not parallel orthogonal
   293	ones**. Loss of one mechanism damages the system substantially more than
   294	the main-effect of that mechanism alone.
   295	
   296	---
   297	
   298	## 5. Implications for the paper
   299	
   300	### 5.1 The corrected paper claim on P4
   301	
   302	**Old framing (2026-04-20, with 15/18 result):**
   303	
   304	> *"P4 (C×P synergy ≥+0.10) failed at +0.04 in 3-seed validation. We
   305	> walk back the 'partial emission as recovery mechanism' claim and
   306	> report this as preliminary."*
   307	
   308	**New framing (2026-04-29, with N=20 result):**
   309	
   310	> *"P4 (C×P synergy ≥+0.10) was preregistered with a +0.10 floor.
   311	> The original 3-seed estimate (+0.044) was a Type II false-negative
   312	> due to high per-seed variance and seed-range sampling bias on this
   313	> interaction term. Replication at N=20 fresh seeds (32000–32019)
   314	> gives synergy = +0.190, 95% bootstrap CI [+0.143, +0.239],
   315	> P(synergy ≤ 0) = 0, P(synergy < +0.10) = 0. The architecture's
   316	> prediction is exceeded by approximately 90%, and the interaction
   317	> magnitude (+0.19) is comparable to the P main effect (−0.22). C
   318	> and P are strongly coupled critical-state stabilisers."*
   319	
   320	### 5.2 Methodological lesson for preregistration design
   321	
   322	We document, as a methodological contribution, that **interaction terms
   323	in the cascade ablation matrix require N ≥ 20 fresh seeds for reliable
   324	detection** when the effect-size ratio (interaction/main-effect) is below
   325	50%. The original 3-seed protocol was insufficient. This is a finding
   326	about preregistration practice, not about the architecture.
   327	
   328	For the same reason, P3 (D×C interaction independence) was reported
   329	as failing at 3 seeds (−0.231) but passing at 5 seeds (−0.183) — a
   330	similar high-variance interaction-term issue. Both interaction tests
   331	in the preregistration set required higher N than the original protocol
   332	specified.
   333	
   334	### 5.3 The 18/18 verdict
   335	
   336	P4 was the residual gap in the 17/18 validation re-run from earlier in
   337	this session. With the N=20 deep-dive, the synergy is decisively above
   338	the preregistered floor. **Effectively, all eighteen preregistered
   339	predictions pass at the empirical level, with no remaining walks-back.**
   340	
   341	---
   342	
   343	## 6. Reproducibility
   344	
   345	**Script:** `demo_p4_cxp_deep_dive.py`
   346	
   347	**Run:**
   348	
   349	```bash
   350	cd /path/to/aria-chess
   351	python3 demo_p4_cxp_deep_dive.py
   352	```
   353	
   354	**Configuration** (as in the script header):
   355	
   356	```python
   357	N_SEEDS = 20
   358	EPOCHS = 150
   359	BASE_SEED = 32000
   360	```
   361	
   362	**Wallclock:** 1706 s (28 min) on a single modern CPU.
   363	
   364	**Output:** Per-condition seed-by-seed alphas, main-effect estimates,
   365	interaction point estimate, bootstrap 95% CI, one-sided P-values,
   366	per-seed paired interaction values.
   367	
   368	**Verification:** seeds 32000–32019 should give the per-condition means
   369	listed in §2.2 to 4 decimal places (the substrate is fully deterministic
   370	given seed). Bootstrap CI may differ in the 4th decimal due to
   371	seed-42 bootstrap RNG differences across NumPy versions.
   372	
   373	---
   374	
   375	## 7. Limits
   376	
   377	1. **One seed range tested at N=20.** A second N=20 run at a different
   378	   seed range (e.g., 33000–33019) would corroborate the reproducibility
   379	   of the +0.19 estimate. We have not yet run this.
   380	
   381	2. **150-epoch run length.** Longer runs (300, 500 epochs) would smooth
   382	   the per-seed variance further, but this is not necessary for a
   383	   well-powered N=20 estimate.
   384	
   385	3. **No replication on a different cascade-α detector.** The current
   386	   estimate uses attention-shift events. An alternative event detection
   387	   (e.g., pressure-threshold crossings) might give a slightly different
   388	   point estimate. We expect the qualitative conclusion (synergy
   389	   significantly above zero, comparable to main-effect scale) to be
   390	   robust.
   391	
   392	4. **The 5× shift across N suggests non-trivial sample-distribution
   393	   structure in the interaction.** We have not characterised this
   394	   structure beyond noting that N=10 had bimodal-leaning per-seed values
   395	   (with one large positive outlier and two negatives) while N=20 has a
   396	   clean unimodal positive distribution. A larger replication (N=50)
   397	   would clarify whether the +0.19 estimate is the true mean or whether
   398	   there are multiple modes at higher N still.
   399	
   400	---
   401	
   402	## 8. Summary in one paragraph
   403	
   404	The C×P interaction in ARIA's cascade ablation matrix was preregistered
   405	at ≥+0.10 (claiming the partial-emission mechanism contributes
   406	non-additively to cascade-α through interaction with context rotation).
   407	The original 3-seed validation reported +0.044 — a fail — and the paper
   408	walked back the claim. We now report a 20-seed deep-dive that gives
   409	synergy = +0.190, 95% bootstrap CI [+0.143, +0.239], P(synergy ≤ 0) = 0,
   410	P(synergy < +0.10) = 0. The architecture's prediction is exceeded by
   411	~90%, and the interaction magnitude is comparable to the partial-emission
   412	main effect (−0.218). The original underestimate was a Type II false
   413	negative compounded by seed-range sampling bias on a high-per-seed-
   414	variance interaction term. The corrected architectural reading: context
   415	rotation and partial emission are strongly coupled critical-state
   416	stabilisers, not nearly-orthogonal ones — disabling either mechanism
   417	cascades into losing the synergistic contribution of the other. This
   418	both upgrades the architectural claim (from "nearly-orthogonal stabilisers"
   419	to "strongly coupled stabilisers") and removes the residual walk-back
   420	from the preregistered prediction set, taking the empirical tally from
   421	17/18 to 18/18.
   422	
   423	---
   424	
   425	## 9. References
   426	
   427	- `demo_p4_cxp_deep_dive.py` — N=20 script (this work)
   428	- `kernel/dimensional_monitor.py` — implementations of C, P, D, E
   429	  mechanisms (lines 304–330, 316–318, 842–855)
   430	- `run_preregistered_validation.py` — original cascade-block test
   431	- `docs/brain_mapping/PAPER_PREDICTIONS.md` — frozen 2026-04-18
   432	- `docs/brain_mapping/VALIDATION_RESULTS.md` — original 15/18 result
   433	  (now superseded by `VALIDATION_RESULTS_2026-04-29.md`)
   434	- `docs/brain_mapping/PAPER_BASIS_2026-04-29.md` — paper-basis
   435	  consolidation (this work)

 succeeded in 359ms:
   260	but is approximately null on conversation (where raw features are
   261	already discriminative). The −4.4pp lift is well within the |·|<10pp
   262	preregistered window, and the negative sign suggests minor noise
   263	addition rather than amplification.
   264	
   265	This decisively distinguishes ARIA from a general-purpose
   266	classification booster: the substrate **selectively** lifts
   267	classification only where raw features fail. This matches cortical
   268	integration literature: substrate integration boosts performance on
   269	ambiguous stimuli but is unnecessary (and sometimes counterproductive)
   270	on unambiguous ones.
   271	
   272	### 3.4 P16 — Permutation null (conversation)
   273	
   274	**Threshold:** Random permutation of feature → frame mapping
   275	preserves accuracy ≥ 50%.
   276	
   277	**Result:** 70.6% mean across 15 permutations.
   278	
   279	**Interpretation:** Conversation null mapping (70.6%) is slightly
   280	higher than chess null mapping (65.4%), consistent with conversation
   281	features carrying more semantic information per dimension. Both are
   282	above the 50% prereg floor, confirming ARIA's geometric content
   283	applies across domains.
   284	
   285	The cross-domain comparison:
   286	
   287	| Task | Raw | Substrate | Null | Geometric content | Semantic content |
   288	|---|---|---|---|---|---|
   289	| Chess (LOO) | 53.1% | 93.8% | n/a | n/a | +40.6pp lift |
   290	| Chess (5-fold CV) | n/a | 83.1% | 65.4% | 65.4% | +17.7pp |
   291	| Conversation (5-fold CV) | 87.5% | 83.1% | 70.6% | 70.6% | +12.5pp (raw vs null) |
   292	
   293	The geometric content (≈65–71% across domains) is the architecture-
   294	invariant null floor. The semantic content (12–18pp) is the domain-
   295	specific contribution.
   296	
   297	### 3.5 Conversation summary
   298	
   299	The substrate is **correctly null** on conversation, validating
   300	selective amplification. Raw features at 87.5% leave little headroom;
   301	substrate routing at 83.1% (lift −4.4pp) is within preregistered
   302	neutrality bounds. The null permutation at 70.6% confirms geometric
   303	content carries across domains.
   304	
   305	---
   306	
   307	## 4. HCP brain connectivity (P17–P18)
   308	
   309	### 4.1 Setup
   310	
   311	**Reference cohort:** Human Connectome Project (HCP), n=1003 subjects.
   312	For preregistered tests, n=100 subjects (computational tractability)
   313	in ICA-50 parcellation. The full-cohort effects (n=1003) match the
   314	n=100 subset within standard error.
   315	
   316	**Method:** Build group-averaged ICA-50 connectivity matrix; threshold
   317	at the same density as ARIA's vertex graph (0.101). Compare degree
   318	distribution and higher-order graph statistics.
   319	
   320	**ARIA reference:** 600-cell H₄ graph. By H₄ transitivity, every
   321	vertex has identical local structure → uniform degree 12 → degree
   322	std = 0 by theorem.
   323	
   324	### 4.2 P17 — ARIA degree homogeneity (theorem)
   325	
   326	**Threshold:** ARIA degree std = 0.00 (H₄ transitivity theorem).
   327	
   328	**Result:** 0.0000 (exactly).
   329	
   330	**Interpretation:** This is a theorem, not a measurement. The H₄
   331	Coxeter group acts transitively on the 600-cell vertices; every
   332	vertex is in the same orbit; every vertex has the same local
   333	neighbourhood structure; degree is uniform. The validation is
   334	included to verify the substrate construction is correct.
   335	
   336	### 4.3 P18 — HCP degree std (hub-spoke structure)
   337	
   338	**Threshold:** HCP ICA-50 degree std > 2.0.
   339	
   340	**Result (n=100 subjects, density 0.101):** **3.388**.
   341	
   342	**Interpretation:** Real cortical functional connectivity has
   343	substantial degree heterogeneity — std 3.39 means the vertex degrees
   344	range across roughly ±5 around the mean. This is the classical hub-
   345	spoke / small-world signature of cortex.
   346	
   347	**ARIA is at −11.58σ** below the HCP cohort mean on this metric:
   348	ARIA's degree std is 0; HCP n=1003 mean is 3.28 ± 0.28; the gap is
   349	(0 − 3.28) / 0.28 = −11.7σ. **Zero of 1003 HCP subjects** have
   350	degree std below 2.0. ARIA is far outside the biological distribution.
   351	
   352	### 4.4 Higher-order graph statistics (full cohort, n=1003)
   353	
   354	Three metrics computed across the full HCP cohort, with ARIA's value
   355	in parentheses:
   356	
   357	```
   358	Metric                 ARIA     HCP n=1003 mean   σ from HCP
   359	─────────────────────────────────────────────────────────────
   360	Degree std             0.000    3.28 ± 0.28        −11.58σ
   361	Participation ratio    68.54    19.72 ± 0.61       +79.78σ
   362	Clustering coefficient 0.455    0.220              +6.80σ
   363	```
   364	
   365	**Interpretation:**
   366	
   367	- **Participation ratio** measures how distributed the connectivity
   368	  is across the 50-region parcellation (high = uniform spread; low =
   369	  hub-concentrated). ARIA at 68.54 vs HCP at 19.72 — ARIA is
   370	  more than **two regimes** above biological cortex on uniformity.
   371	  Real cortex is hub-concentrated; ARIA is uniform. +79.78σ.
   372	- **Clustering coefficient** measures local triangular density.
   373	  ARIA at 0.455 vs HCP at 0.220 — ARIA has more local clustering
   374	  than cortex (consistent with the polytope's local edge density).
   375	  +6.80σ.
   376	
   377	### 4.5 The maximum-symmetry null framing
   378	
   379	The HCP comparison places ARIA as a **principled maximum-symmetry
   380	null reference** for cortex. ARIA is what cortex would look like
   381	under unbroken H₄ symmetry. Real cortex breaks this symmetry through
   382	hub-spoke functional specialisation; the symmetry-breaking is
   383	quantitatively measurable as the σ-distance between ARIA and HCP on
   384	each metric.
   385	
   386	This is the contribution of ARIA to comparative-connectomics
   387	methodology: instead of comparing real cortex to a stochastic null
   388	(Erdős–Rényi, configuration model), one can compare it to a
   389	**deterministic group-theoretic null** with no fitted parameters,
   390	giving precise effect-size statements like "real cortex is +79.78σ
   391	above the H₄-symmetry baseline on participation ratio."
   392	
   393	The σ-distances (−11.6σ, +79.8σ, +6.8σ) far exceed any preprocessing-
   394	induced noise envelope — the gap between ARIA and HCP is robust to
   395	parcellation choice, density threshold, and subject inclusion
   396	criteria.
   397	
   398	### 4.6 What we do NOT claim
   399	
   400	We do **not** claim biological cortex has "drifted from an ideal
   401	polytope" or that the polytope is the ground truth. We claim:
   402	
   403	(a) ARIA is a useful a-priori null with principled group-theoretic
   404	    foundations and zero fitted parameters.
   405	(b) The observable σ-distances quantify the magnitude of biological
   406	    symmetry-breaking.
   407	(c) The signs of those distances (cortex is more hub-concentrated,
   408	    less uniformly connected, more locally clustered) are the
   409	    biological content that any cortical-architecture model must
   410	    explain.
   411	
   412	ARIA does not commit to a normative claim about which symmetry-
   413	breaking is present. The comparison is structural — quantifying
   414	where biology sits relative to the H₄ baseline.
   415	
   416	### 4.7 HCP summary
   417	
   418	ARIA's degree std = 0 (theorem); HCP n=1003 degree std = 3.28 ± 0.28,
   419	range [2.55, 4.16], with zero of 1003 subjects below 2.0. ARIA is
   420	−11.58σ on degree homogeneity, +79.78σ on participation ratio, and
   421	+6.80σ on clustering coefficient. The substrate functions as a
   422	maximum-symmetry null reference for cortical functional connectivity;
   423	biological cortex breaks the symmetry through hub-spoke functional
   424	specialisation that is quantifiable in σ-units against ARIA.
   425	
   426	---
   427	
   428	## 5. Cross-domain summary in one paragraph
   429	
   430	The substrate's geometric structure functions as a domain-invariant
   431	selective amplifier and a maximum-symmetry connectivity null. On chess
   432	pattern recognition, where 4-category classification on 8-dimensional
   433	hand-features is at chance-class (53.1% raw LOO), substrate routing
   434	amplifies to 93.8% LOO (+40.6pp lift) and 83.1% 5-fold CV across fresh
   435	seeds. The architecture's contribution decomposes into a geometric
   436	floor (≈65–71% across domains, robust to feature → frame permutation)
   437	and a domain-specific semantic alignment (12–18pp on top of the
   438	geometric floor). On conversation utterance classification, where raw
   439	8-dimensional features are already 87.5% discriminative, the substrate
   440	is correctly null (lift −4.4pp, well within preregistered neutrality
   441	band) — confirming the substrate is a selective amplifier, not an
   442	unconditional booster. On HCP brain functional connectivity (n=1003,
   443	ICA-50, density-matched), ARIA's H₄-transitive structure (degree
   444	std = 0) is −11.58σ below the biological mean (3.28 ± 0.28); on
   445	participation ratio ARIA at 68.54 is +79.78σ above HCP (19.72 ± 0.61),
   446	and on clustering coefficient ARIA at 0.455 is +6.80σ above HCP (0.220).
   447	ARIA serves as a deterministic group-theoretic null reference for
   448	cortical connectivity, against which the biological cortex's symmetry-
   449	breaking via hub-spoke functional specialisation is quantifiable.
   450	
   451	---
   452	
   453	## 6. The architectural reading
   454	
   455	Three things matter for the paper:
   456	
   457	### 6.1 Selective amplification
   458	
   459	The contrast between chess (+40.6pp lift) and conversation (−4.4pp
   460	lift) demonstrates the substrate amplifies **only when there is
   461	information to amplify**. This is the cortical-integration signature:
   462	attention boosts ambiguous stimuli (where additional integration is
   463	useful) but does not boost already-discriminative stimuli (where
   464	integration adds noise). The substrate captures this selectivity
   465	without any task-specific tuning.
   466	
   467	### 6.2 Architecture-invariant null floor
   468	
   469	The 65.4% (chess) / 70.6% (conversation) null permutation accuracies
   470	demonstrate the substrate carries ~65% classification power as
   471	**architecture content alone**, independent of which feature is mapped
   472	to which frame. This is the "raw geometric amplification" of the H₄
   473	graph: the topology amplifies category structure regardless of how
   474	input is connected to it.
   475	
   476	### 6.3 Maximum-symmetry null for connectivity
   477	
   478	ARIA's H₄-transitive structure is the principled deterministic null
   479	reference for biological cortex. The σ-distances (−11.58σ, +79.78σ,
   480	+6.80σ) quantify the magnitude of biological symmetry-breaking, with
   481	biological direction (more hub-spoke, less uniform, more locally
   482	clustered) characterising the biological content that any architecture
   483	model must explain.
   484	
   485	---
   486	
   487	## 7. Reproducibility
   488	
   489	All cross-domain results reproduce from a single command:
   490	
   491	```bash
   492	cd /path/to/aria-chess
   493	python3 run_preregistered_validation.py
   494	```
   495	
   496	Wallclock: ~18 minutes. Specific seed ranges:
   497	- Chess fresh seeds: 30200–30204
   498	- Chess null permutation: seeded from 30210
   499	- Chess random-label: seeded from 30211
   500	- Conversation fresh seeds: 30220–30224
   501	- Conversation null: seeded from 30230
   502	- HCP n=100 ICA-50: deterministic from group average
   503	
   504	The standalone scripts also reproduce individual tracks:
   505	- `run_chess_pattern_readout.py` for chess
   506	- `run_conversation_readout.py` for conversation
   507	- `run_hcp_registration.py` for HCP
   508	
   509	JSON outputs land in `~/.aria/preregistered_validation/results_*.json`.
   510	Logs in `/tmp/prereg_*.log`.
   511	
   512	---
   513	
   514	## 8. Limits
   515	
   516	1. **Chess test is small (32 positions, 4 categories).** The ~93.8%
   517	   substrate-routed accuracy is on a small evaluation set. A larger
   518	   chess test bench would strengthen the lift claim. The 5-fold CV
   519	   at 83.1% is a more conservative readout (4-category random
   520	   subsamples rather than full LOO).
   521	
   522	2. **Conversation test is also small (64 utterances, 8 categories).**
   523	   Same caveat applies. The selective-null finding (lift −4.4pp,
   524	   inside |·|<10pp band) is the qualitative claim; magnitude could
   525	   shift on larger utterance corpora.
   526	
   527	3. **HCP comparison uses one parcellation (ICA-50).** Different
   528	   parcellations (e.g., Schaefer, Glasser) would give different
   529	   per-metric numbers but should preserve the qualitative pattern
   530	   (cortex is hub-concentrated relative to ARIA's transitive null).
   531	   We have not yet run the parcellation-robustness check.
   532	
   533	4. **No domain-specific tuning was applied to the substrate.** This
   534	   is the methodological strength of the cross-domain comparison —
   535	   the substrate's only domain-specific input is the feature → frame
   536	   assignment, and even that is partially nullable (65–71% null
   537	   accuracy with random permutation). However, future work could
   538	   explore whether domain-specific frame assignments (e.g., using
   539	   ARIA's own feature-importance estimates) further improve
   540	   classification.
   541	
   542	5. **The chess and conversation tasks are intrinsically supervised**
   543	   (categories are given). Unsupervised pattern discovery on real
   544	   neural data is the next track, not yet validated.
   545	
   546	---
   547	
   548	## 9. Files referenced
   549	
   550	### Validation scripts
   551	- `run_preregistered_validation.py` — full P1–P18 harness
   552	- `run_chess_pattern_readout.py` — chess track
   553	- `run_chess_robustness.py` — k-fold and depth-sweep helpers
   554	- `run_conversation_readout.py` — conversation track
   555	- `run_hcp_registration.py` — HCP track
   556	
   557	### Substrate
   558	- `kernel/dimensional_monitor.py:DimensionalMonitor` — substrate
   559	  with pressure-field dynamics; `homeostatic_reset(level=1.0)` is
   560	  the reset method.
   561	- `kernel/rust_search/crates/aria-polytope-core/` — fast Rust
   562	  polytope vertex graph.
   563	
   564	### Companion docs
   565	- `docs/brain_mapping/PAPER_PREDICTIONS.md` — frozen 2026-04-18
   566	- `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` — full
   567	  preregistered tally
   568	- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — synergy deep-dive
   569	- `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` — six
   570	  EEG drug/sleep signatures (recurrent self-model layer above
   571	  substrate; independent of cross-domain tracks)
   572	- `docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md` — substrate
   573	  state-drift diagnostic; rationale for `homeostatic_reset()`
   574	
   575	### Memory entries
   576	- `project_substrate_selective_amplifier.md` — original selective-
   577	  amplifier finding (chess +31pp / conversation -3pp at discovery)
   578	- `project_chess_closed_loop.md` — chess track v2 features and
   579	  classification protocol
   580	- `project_chess_permutation_invariance.md` — null permutation
   581	  decomposition into geometric vs semantic content
   582	- `project_hcp_maxsymmetry_null.md` — HCP comparison detail
   583	- `project_preregistered_validation_17_of_18.md` — re-run summary
   584	- `project_p4_cxp_underpowered_not_wrong.md` — N=20 deep-dive

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 292ms:
     1	# Preregistered Validation — Results (2026-04-29 update)
     2	
     3	*This document supersedes `VALIDATION_RESULTS.md` (2026-04-20, 15/18).
     4	It records the most recent run of the preregistered validation harness
     5	plus the N=20 deep-dive on the residual P4 prediction.*
     6	
     7	> **Headline:** **17 / 18 predictions pass at standard validation;
     8	> 18 / 18 with N=20 deep-dive on the residual P4.** Original 15/18
     9	> result reflected three honest walks-back from underpowered cascade-
    10	> ablation interaction tests and an unspecified reset protocol for the
    11	> chess LOO test. With (a) cascade block bumped from 3 to 5 seeds per
    12	> condition, (b) `homeostatic_reset(level=1.0)` wired in between depth
    13	> measurements for chess LOO, and (c) N=20 fresh-seed replication of
    14	> the C×P interaction test, all gaps close. The architecture's claim
    15	> set is fully validated against preregistered thresholds.
    16	
    17	---
    18	
    19	## 1. Provenance and protocol
    20	
    21	### 1.1 Preregistration
    22	
    23	Eighteen quantitative predictions were frozen on **2026-04-18** in
    24	`docs/brain_mapping/PAPER_PREDICTIONS.md`, before any validation run.
    25	Each prediction has a falsifiable threshold (numerical band or
    26	directional inequality). The validation harness is
    27	`run_preregistered_validation.py` — git-tracked, deterministic given
    28	seeds, produces JSON + log output.
    29	
    30	The preregistration was frozen because earlier "discovery runs" had
    31	14 correspondences with no protection against p-hacking. Without
    32	preregistration, claims are vulnerable to "you cherry-picked seeds"
    33	critiques. With it, claims survive.
    34	
    35	### 1.2 The original 2026-04-20 result
    36	
    37	The original validation run on 2026-04-20 reported **15/18 passes**:
    38	- All cascade main effects passed (P1, P2, P5).
    39	- All EEG/sleep deterministic re-runs passed (P6, P7, P8).
    40	- All cross-domain tests passed at fresh seeds (P9, P10, P11, P12,
    41	  P14, P15, P16, P17, P18).
    42	- **Three failed:**
    43	  - **P3** (D×C interaction independence): observed −0.231 at N=3,
    44	    outside |·| < 0.20 band.
    45	  - **P4** (C×P synergy): observed +0.044 at N=3, below +0.10 floor.
    46	  - **P13** (Chess LOO substrate lift ≥ +15pp): observed +3.1pp,
    47	    far below +15pp floor.
    48	
    49	The walks-back at the time were:
    50	- "P3, P4 walked back to 'preliminary, requires larger N'."
    51	- "P13 reframed as state-dependent — substrate state drifted toward
    52	  equilibrium across successive depth measurements; need to specify
    53	  reset protocol."
    54	
    55	### 1.3 What changed for the 2026-04-29 re-run
    56	
    57	Three improvements:
    58	
    59	1. **Cascade block N bumped 3 → 5** for P2, P3, P4, P5 conditions
    60	   in `run_preregistered_validation.py`. The original 3 seeds was
    61	   the source of high-variance failure on P3 and P4.
    62	
    63	2. **`homeostatic_reset(level=1.0)`** wired into the validation script
    64	   between depth-sweep measurements (lines 274–285 of the script).
    65	   This is the reset protocol identified post-hoc as necessary to
    66	   prevent pressure-field equilibration across LOO depth measurements
    67	   (`docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md`).
    68	
    69	3. **N=20 deep-dive** on the residual P4 (`demo_p4_cxp_deep_dive.py`):
    70	   ran the C×P interaction test at 20 fresh seeds (32000–32019) with
    71	   bootstrap 95% CI on the interaction estimate. See
    72	   `P4_SYNERGY_FINDING.md` for the standalone report.
    73	
    74	Wallclock for the standard re-run was 1101 s (~18 min).
    75	
    76	---
    77	
    78	## 2. Full results table — 2026-04-29 run
    79	
    80	| ID | Claim | Threshold | 2026-04-20 (3-seed) | **2026-04-29 (5-seed + reset + N=20 P4)** | Verdict |
    81	|---|---|---|---|---|---|
    82	| P1 | Cascade α ∈ [2.5, 3.5] | ∈ [2.5, 3.5] | 3.020 ✅ | **2.958** | ✅ |
    83	| P2 | Context-rotation main effect | ≥ +0.30 | +0.588 ✅ | **+0.621** | ✅ |
    84	| P3 | \|D×C interaction\| (independence) | \|·\| < 0.20 | −0.231 ❌ | **−0.183** | ✅ |
    85	| P4 | C×P synergy | ≥ +0.10 | +0.044 ❌ | **+0.190 at N=20, CI [+0.143, +0.239]** | ✅ at N=20 |
    86	| P5 | \|equator main effect\| (null) | \|·\| < 0.15 | +0.046 ✅ | **+0.046** | ✅ |
    87	| P6 | Real EEG α | ∈ [2.0, 3.0] | 2.513 ✅ | **2.513** | ✅ |
    88	| P7 | W→N3 variance ratio | < 0.70 | 0.365 ✅ | **0.365** | ✅ |
    89	| P8 | W→N3 switching ratio | < 0.50 | 0.058 ✅ | **0.058** | ✅ |
    90	| P9 | Chess 5-fold CV | ≥ 70% | 83.1% ✅ | **83.1%** | ✅ |
    91	| P10 | Chess null mapping | ≥ 50% | 65.4% ✅ | **65.4%** | ✅ |
    92	| P11 | Chess random-label | ∈ [15%, 35%] | 23.4% ✅ | **23.4%** | ✅ |
    93	| P12 | Chess goldilocks peak | ∈ {15, 25, 40, 60} | n=15 ✅ | **n=25** | ✅ |
    94	| P13 | Chess LOO substrate lift | ≥ +15pp (with reset) | +3.1pp ❌ | **+40.6pp** | ✅ |
    95	| P14 | Conv raw 5-fold CV | ≥ 75% | 87.5% ✅ | **87.5%** | ✅ |
    96	| P15 | \|conv substrate lift\| | \|·\| < 10pp | −4.4pp ✅ | **−4.4pp** | ✅ |
    97	| P16 | Conv null mapping | ≥ 50% | 70.6% ✅ | **70.6%** | ✅ |
    98	| P17 | ARIA degree std (theorem) | = 0.00 | 0.0000 ✅ | **0.0000** | ✅ |
    99	| P18 | HCP ICA-50 degree std | > 2.0 | 3.388 ✅ | **3.388** | ✅ |
   100	
   101	---
   102	
   103	## 3. Predictions that flipped to PASS — explained
   104	
   105	### 3.1 P3 — D×C interaction independence
   106	
   107	**Threshold:** \|D×C interaction\| < 0.20.
   108	
   109	**Original (N=3) failure:** −0.231. The interaction estimate fell just
   110	outside the independence band. Sign and magnitude were inconsistent with
   111	discovery (which had given +0.039).
   112	
   113	**2026-04-29 re-run (N=5):** −0.183. Now inside the independence band.
   114	The shift from −0.231 (N=3) to −0.183 (N=5) is the kind of stabilisation
   115	typical of high-variance interaction terms at small N — adding two
   116	seeds tightens the estimate enough to land inside the threshold.
   117	
   118	**Diagnosis:** classical Type II false negative on an interaction with
   119	high per-seed variance. With 3 seeds, the standard error on the
   120	interaction estimate is approximately 0.06–0.10; the threshold is
   121	±0.20; and a single bad-luck draw at N=3 can put the point estimate
   122	just outside. With 5 seeds (and clearer at 20+) the estimate stabilises.
   123	
   124	The architectural claim "D₄ and context rotation act independently on
   125	cascade-α" is **supported** by the N=5 re-run within the preregistered
   126	threshold. We do not claim point-zero independence (the estimate is
   127	slightly antagonistic, −0.183), but the magnitude is bounded inside
   128	the |·| < 0.20 band by direct measurement.
   129	
   130	### 3.2 P4 — C×P synergy
   131	
   132	This is the most consequential change. See the standalone report
   133	`P4_SYNERGY_FINDING.md` for the full story.
   134	
   135	**Threshold:** ≥ +0.10.
   136	
   137	**Original (N=3) failure:** +0.044. Below threshold.
   138	
   139	**2026-04-29 re-run (N=5):** +0.039. Still below threshold — confirming
   140	the N=3 reading at face value.
   141	
   142	**N=20 fresh-seed deep-dive (`demo_p4_cxp_deep_dive.py`, seeds 32000–32019):**
   143	
   144	```
   145	C×P bootstrap mean:           +0.190
   146	C×P 95% bootstrap CI:         [+0.143, +0.239]
   147	P(interaction ≤ 0):           0.0000
   148	P(interaction < +0.10):       0.0000
   149	```
   150	
   151	The 95% CI is **entirely above the preregistered +0.10 threshold**.
   152	The synergy is decisively positive and decisively above prereg. The
   153	N=3/N=5 estimates were Type II false negatives compounded by
   154	seed-range sampling bias on a high-per-seed-variance interaction term
   155	(per-seed std = 0.089 at N=20).
   156	
   157	**Architectural reading**: this is a substantive shift in the claim.
   158	Original: "C and P are nearly orthogonal stabilisers." Corrected:
   159	"C and P are strongly coupled stabilisers; the interaction (+0.19) is
   160	comparable to the P main effect (−0.22)." See §4 of
   161	`P4_SYNERGY_FINDING.md` for the mechanistic interpretation.
   162	
   163	### 3.3 P13 — Chess LOO substrate lift
   164	
   165	**Threshold:** ≥ +15pp lift (substrate vs raw on LOO at n=25 ticks).
   166	
   167	**Original (N=1) failure:** +3.1pp. Far below threshold.
   168	
   169	**2026-04-29 re-run (with `homeostatic_reset(level=1.0)` between depth
   170	measurements):** **+40.6pp**.
   171	
   172	```
   173	Depth sweep (raw 53.1%, with reset between measurements):
   174	  n=5:    53.1%
   175	  n=15:   65.6%
   176	  n=25:   93.8%   ← peak (P12 goldilocks)
   177	  n=40:   84.4%
   178	  n=60:   84.4%
   179	  n=100:  78.1%
   180	
   181	Lift at n=25 = 93.8% − 53.1% = +40.6pp
   182	```
   183	
   184	**Diagnosis (from `NON_EQUILIBRIUM_FINDING.md`):** the substrate's
   185	pressure field equilibrates within ~5 successive evaluations. The
   186	original LOO test ran six consecutive depth measurements (n=5, 15, 25,
   187	40, 60, 100) without reset, so by the time it reached n=25 the substrate
   188	had drifted toward an equilibrium where pressure-field structure was
   189	washed out, collapsing the LOO lift to +3pp.
   190	
   191	The reset protocol restores the canonical far-from-equilibrium operating
   192	point before each measurement. With reset, the predicted +15pp lift is
   193	exceeded by 25pp — the substrate's amplification effect is real and
   194	substantial when state is properly initialised.
   195	
   196	**Generalisable lesson:** ARIA's substrate is a non-stationary
   197	dynamical system. **Any multi-trial benchmark must specify state-reset
   198	protocol.** This is now a methodological recommendation in the paper.
   199	
   200	---
   201	
   202	## 4. Predictions that replicated cleanly across all runs (15)
   203	
   204	Below are direct re-runs that gave identical or very-close results
   205	across the original and 2026-04-29 runs.
   206	
   207	### 4.1 Cascade geometry (P1, P2, P5)
   208	
   209	- **P1**: Baseline α at 5 seeds = 2.958 (vs original 3.020 at 3 seeds).
   210	  Both inside [2.5, 3.5] cortical-avalanche band.
   211	- **P2**: Context-rotation main effect = +0.621 at 5 seeds (vs +0.588
   212	  at 3 seeds). Both above the +0.30 dominance threshold.
   213	- **P5**: Equator-compensation main effect = +0.046 at 5 seeds (vs
   214	  +0.046). Null prediction confirmed across runs.
   215	
   216	### 4.2 Real EEG and sleep-stage signatures (P6, P7, P8)
   217	
   218	These are deterministic re-runs against fixed Sleep-EDFx datasets:
   219	- **P6**: Real EEG spindle α = 2.513 (n=30 subjects). Inside [2.0, 3.0].
   220	- **P7**: W→N3 variance ratio = 0.365 (n=24 subjects). Below 0.70.

 succeeded in 282ms:
     1	# Preregistered Paper Predictions
     2	
     3	**Frozen: 2026-04-18** — predictions below were locked before running
     4	any validation. They are derived from discovery runs reported in
     5	`CASCADE_FINDINGS.md` (pairwise ablations, multi-subject EEG,
     6	conversation + chess closed-loop, HCP registration).
     7	
     8	Each prediction has:
     9	- a **specific numerical claim**
    10	- a **pass threshold** (interval, inequality, or categorical match)
    11	- a **validation test** (which run on which seeds will test it)
    12	- a **rationale** (why the claim is non-trivial — what would break it)
    13	
    14	**Hit rate** will be reported after validation in `VALIDATION_RESULTS.md`.
    15	
    16	---
    17	
    18	## Predictions 1-5: Cascade geometry
    19	
    20	### P1. Cascade α is in the SOC range
    21	- **Claim**: Mean α across 5 fresh-seed (30000-30004) baseline runs
    22	  of 200 epochs each will satisfy **2.5 ≤ α ≤ 3.5**.
    23	- **Rationale**: Beggs & Plenz 2003 put biological neuronal avalanches
    24	  in [1.5, 3.0]. Our discovery runs gave α ≈ 2.91-3.02. A new-seed
    25	  violation would mean the signature doesn't replicate.
    26	- **Run**: `_run_single_seed` with all mechanisms active.
    27	
    28	### P2. Pairwise ablation — context rotation is the dominant mechanism
    29	- **Claim**: On 3 fresh seeds (30010-30012), main effect of
    30	  `ablate_context_rotation` on α is **≥ +0.30**.
    31	- **Rationale**: Discovery observation was +0.625. A small or negative
    32	  main effect would falsify the dominant-mechanism claim.
    33	- **Run**: Conditions `----` vs `-C--` on fresh seeds.
    34	
    35	### P3. D×C interaction is near-zero (independence)
    36	- **Claim**: |D×C interaction| < **0.20** on the fresh 2x2 sub-matrix
    37	  (----/D---/-C--/DC--) at 3 seeds.
    38	- **Rationale**: Discovery gave 0.039. A large interaction would mean
    39	  D₄ and context rotation are not independent — reviewer-critical for
    40	  #2+#3 separability.
    41	- **Run**: Fresh seeds, 4 conditions, compute interaction term.
    42	
    43	### P4. C×P synergy is positive and substantial
    44	- **Claim**: C×P interaction **≥ +0.10** on the 2x2 (----/-C--/--P-/-CP-)
    45	  at 3 seeds.
    46	- **Rationale**: Discovery gave +0.229. The "partial emission is a
    47	  redundant recovery mechanism" story depends on this being > 0.
    48	- **Run**: Fresh seeds, 4 conditions.
    49	
    50	### P5. Equator compensation is null (≤ small main effect)
    51	- **Claim**: Main effect of `ablate_equator_compensation` on α has
    52	  **|effect| < 0.15** on 3 fresh seeds.
    53	- **Rationale**: Discovery gave −0.082. Tests the "formally removable"
    54	  claim.
    55	- **Run**: Fresh seeds, conditions ---- vs ---E.
    56	
    57	---
    58	
    59	## Predictions 6-8: EEG spindle & state analysis
    60	
    61	### P6. Real EEG spindle α is in the SOC range
    62	- **Claim**: On the existing 30 Sleep-EDFx subjects, pooled spindle α
    63	  (bootstrap 1000 resamples, fresh seed 30100) falls in **[2.0, 3.0]**.
    64	- **Rationale**: Discovery with 500-bootstrap (seed 42) gave
    65	  2.513 [2.504, 2.526]. A different seed's bootstrap CI should
    66	  overlap substantially.
    67	- **Run**: `bootstrap_alpha_ci` with fresh seed on already-computed
    68	  spindle sizes (not re-detecting spindles).
    69	
    70	### P7. W→N3 coherence variance collapses
    71	- **Claim**: Mean N3/W variance ratio across 24 subjects **< 0.70**.
    72	- **Rationale**: Discovery gave 0.365. If the ratio is ≥ 0.70 it means
    73	  coherence variance does not meaningfully collapse — corresponding
    74	  to #4 being general reduced-state failing empirically.
    75	- **Run**: Re-execute `run_sleep_stage_coherence.py` (deterministic).
    76	
    77	### P8. W→N3 regime switching drops (opposite to anaesthesia)
    78	- **Claim**: Mean N3/W switching ratio **< 0.50**.
    79	- **Rationale**: Discovery gave 0.058. If the ratio > 0.50 (near-unity
    80	  or rising), the dissociation story breaks — this is the empirical
    81	  test of "#5 is anaesthesia-specific, not general reduced-state."
    82	- **Run**: Re-execute deterministic analysis.
    83	
    84	---
    85	
    86	## Predictions 9-13: Closed-loop classification (chess)
    87	
    88	### P9. Chess 5-fold CV ≥ chance + substantial margin
    89	- **Claim**: 5-fold CV on v2 features at n=25 ticks, 5 fresh seeds
    90	  (30200-30204), mean ≥ **70%**.
    91	- **Rationale**: Discovery gave 81.9% ± 4.6%. Chance = 25%. A result
    92	  < 70% would mean our 84.4% LOO number was misleadingly inflated.
    93	- **Run**: `run_chess_pattern_readout.py` + 5-fold with fresh seeds.
    94	
    95	### P10. Null feature→frame mapping ≥ 50% (domain-invariant floor)
    96	- **Claim**: Mean accuracy over 20 random permutations (fresh RNG
    97	  seed 30210) **≥ 50%**.
    98	- **Rationale**: Discovery gave 64.2%. A floor below 50% would mean
    99	  the architectural-invariant story is fragile.
   100	- **Run**: `run_chess_robustness.py` (fresh seed).
   101	
   102	### P11. Random-label baseline = chance
   103	- **Claim**: Mean random-label accuracy **∈ [15%, 35%]** (chance ± 1σ).
   104	- **Rationale**: Protocol-clean test. Discovery gave 26.1% ± 9.4%.
   105	  If the baseline drifts from chance, CV is leaking.
   106	- **Run**: `run_chess_robustness.py` (fresh seed 30211).
   107	
   108	### P12. Diffusion-depth goldilocks peaks in [15, 60]
   109	- **Claim**: Across depths {5, 15, 25, 40, 60, 100}, the peak accuracy
   110	  is achieved in **{15, 25, 40, 60}** (not at 5 or 100).
   111	- **Rationale**: Cortical integration-time analogue (Thorpe 1996).
   112	  Peak outside the window would break the analogy.
   113	- **Run**: `run_chess_pattern_readout.py --sweep 5,15,25,40,60,100`.
   114	
   115	### P13. Substrate lift on chess v2 is positive
   116	- **Claim**: At n=25, substrate ≥ raw **+ 15pp** on 5-fold CV (fresh
   117	  seeds).
   118	- **Rationale**: The central closed-loop claim.
   119	- **Run**: Compare raw-features classification vs substrate-pattern
   120	  classification.
   121	
   122	---
   123	
   124	## Predictions 14-16: Closed-loop (conversation) + cross-domain
   125	
   126	### P14. Conversation raw features already discriminative
   127	- **Claim**: Raw conversation 5-fold CV accuracy **≥ 75%** on fresh
   128	  seeds (30220-30224).
   129	- **Rationale**: Discovery gave 87.5% LOO. If much lower, the
   130	  selective-amplifier story's premise fails.
   131	- **Run**: `run_conversation_readout.py` (raw-features classification).
   132	
   133	### P15. Substrate does NOT lift clean features much
   134	- **Claim**: |substrate lift − raw| **< 10pp** on conversation (fresh
   135	  seeds). Substrate adds at most 10pp or subtracts at most 10pp.
   136	- **Rationale**: Selective-amplifier prediction. Large substrate lift
   137	  on already-clean features would break the Thorpe/Kiani analogy.
   138	- **Run**: 5-fold CV raw vs substrate on fresh seeds.
   139	
   140	### P16. Architecture-invariant null mapping ≥ 50% on both domains
   141	- **Claim**: Null feature→frame permutation mean ≥ **50%** on BOTH
   142	  chess AND conversation, fresh RNG.
   143	- **Rationale**: Discovery gave ~65% in both. Domain-invariant claim.
   144	- **Run**: Null-permutation controls on both domains.
   145	
   146	---
   147	
   148	## Predictions 17-18: HCP structural registration
   149	
   150	### P17. ARIA degree std = 0 exactly (theorem-level)
   151	- **Claim**: ARIA vertex adjacency graph has mean-degree exactly 12.00,
   152	  std exactly 0.00.
   153	- **Rationale**: H₄ symmetry acts transitively. This is a theorem,
   154	  not a measurement. A non-zero std would indicate a bug.
   155	- **Run**: Deterministic recompute.
   156	
   157	### P18. HCP ICA-50 has non-trivial degree std
   158	- **Claim**: On 100 subjects (100 different ones if available; else
   159	  same), group-averaged HCP graph has **degree std > 2.0** at
   160	  density-matched threshold.
   161	- **Rationale**: Discovery gave 3.39. Hub-spoke heterogeneity is the
   162	  brain's signature. Below 2.0 would mean the brain is more regular
   163	  than expected.
   164	- **Run**: Deterministic recompute (HCP data is fixed).
   165	
   166	---
   167	
   168	## Meta-claims (reported but not tested)
   169	
   170	- **M1**: We will report ALL outcomes, including broken predictions.
   171	- **M2**: We will NOT revise predictions after seeing results.
   172	- **M3**: If a prediction breaks, we will explicitly note it in
   173	  the paper and retract or reframe the corresponding claim.
   174	
   175	## Validation protocol
   176	
   177	1. Predictions frozen at time of this file's creation (git-tracked).
   178	2. Fresh seeds (30000+) not used in discovery runs.
   179	3. No code changes to analysis scripts between freeze and validation.
   180	4. Single validation run — no "best of N" cherry-picking.
   181	5. Results recorded in `VALIDATION_RESULTS.md` with hit/miss per
   182	   prediction + full numerics.
   183	
   184	## Success thresholds
   185	
   186	- **≥ 14/18 predictions pass**: paper claims are well-supported.
   187	- **10-13/18**: paper is publishable but with honest caveats on
   188	  broken predictions.
   189	- **< 10/18**: substantial revision needed; multiple correspondences
   190	  require retraction or reframing.
   191	
   192	We do not expect 18/18 — some are noisy empirical tests and statistical
   193	luck alone would produce an occasional miss at the α=0.05 level. A
   194	bulletproof paper should land 14-17.

 succeeded in 396ms:
     1	# The Non-Equilibrium Finding
     2	
     3	**Date**: 2026-04-20
     4	
     5	The paper's most important scientific discovery. Sits one layer
     6	deeper than all the empirical correspondences and ties them
     7	together into a single mechanistic claim.
     8	
     9	---
    10	
    11	## 1. The core discovery
    12	
    13	The ARIA substrate is a **far-from-equilibrium thermodynamic engine**.
    14	Its cognitive function requires continuous maintenance against a
    15	natural attractor state. Left alone, the pressure field
    16	equilibrates (emission rate ≈ decay rate), the substrate reaches
    17	a steady-state attractor, and classification function collapses
    18	to raw-feature baseline.
    19	
    20	Only a **reset mechanism** analogous to biological sleep restores
    21	non-equilibrium operation.
    22	
    23	---
    24	
    25	## 2. The three experiments
    26	
    27	### E1 — Drift curve (30 consecutive classifications, no reset)
    28	
    29	| trial | accuracy | crossed | pressure | inter-pattern sim |
    30	|---|---|---|---|---|
    31	| 1 | 84.4% | 100 | 127.0 | 1.000 |
    32	| 2 | 93.8% | 100 | 147.9 | 1.000 |
    33	| 3 | 68.8% | 100 | 153.4 | 1.000 |
    34	| 4 | 65.6% | 100 | 156.7 | 1.000 |
    35	| **5** | **56.2%** | 100 | **156.96** | 1.000 |
    36	| 6–30 | **56.2% locked** | 100 | 156.96 locked | 1.000 |
    37	
    38	**Within 5 trials the substrate hits a fixed point**. Pressure
    39	equilibrates at exactly 156.96 (emission = decay). Accuracy is
    40	**pinned at raw-features baseline 56.2%** for trials 5–30 —
    41	literally zero substrate contribution.
    42	
    43	### E2 — Homeostatic reset
    44	
    45	| Phase | Accuracy |
    46	|---|---|
    47	| Fresh (pre-loaded persistence state) | 84.4% |
    48	| Saturated (after 10 consecutive runs) | 56.2% |
    49	| **Full reset** | **87.5% (higher than fresh)** |
    50	| Partial reset (50% decay) | 81.2% |
    51	
    52	**Full reset restores AND improves on the fresh state**. Because
    53	"fresh" inherits 100 pre-loaded crossed vertices from persistence;
    54	full reset clears those, leaving the substrate genuinely canonical.
    55	
    56	This directly parallels post-sleep cognition: people often perform
    57	better after sleep than they would have without any prior cognitive
    58	load at all. Sleep isn't just restoration — it's improvement.
    59	
    60	### E3 — Attractor structure
    61	
    62	- Fresh crossed: 100 vertices
    63	- Saturated crossed: **100 (unchanged)**
    64	- Shell distribution: identical fresh vs saturated
    65	- Orbit distribution: identical fresh vs saturated
    66	- Pressure: top-10 vertices hold 10.4% (uniform = 8.3%) — spread
    67	
    68	**Saturation is NOT about new crossings**. It's about the
    69	**pressure field reaching thermodynamic equilibrium** — emission
    70	rate matches decay rate at every vertex.
    71	
    72	---
    73	
    74	## 3. The underlying mechanism
    75	
    76	ARIA's dynamics have three terms:
    77	- Emission from crossed vertices (fixed rate per tick)
    78	- Diffusion across graph (heat-equation-like)
    79	- Decay of pressure (factor per tick)
    80	
    81	Steady-state solution: emission = decay + diffusion outflow. The
    82	system LITERALLY converges to a thermodynamic equilibrium of the
    83	pressure field in a few hundred ticks.
    84	
    85	Once at equilibrium:
    86	- Any fresh injection gets quickly absorbed into the equilibrium
    87	- All cascade events look statistically identical
    88	- Patterns across different inputs become indistinguishable
    89	- Classification collapses to raw-feature baseline
    90	
    91	---
    92	
    93	## 4. Why this is consistent with — and explains — the rest
    94	
    95	**Every substrate quirk we've seen maps to this**:
    96	
    97	| phenomenon | mechanism |
    98	|---|---|
    99	| P13 preregistration fail | polytope drifted to equilibrium across evaluations |
   100	| Priming saturation (cosine → 1.000) | field equilibration looks like this |
   101	| Variance expansion under ablation | mechanisms are **far-from-equilibrium maintainers** |
   102	| 3-seed interaction instability | seeds sampled at different distances from equilibrium |
   103	| DMT α-shift | 5HT2A agonism pushes system further from equilibrium |
   104	| Fresh-polytope vs state-drifted +31pp vs +3pp | non-equilibrium vs equilibrium regimes |
   105	
   106	---
   107	
   108	## 5. Biological parallels — far-from-equilibrium theory
   109	
   110	The substrate's behavior is the computational signature of several
   111	classic thermodynamic / neural phenomena:
   112	
   113	### Dissipative structures (Prigogine)
   114	Complex order requires continuous energy flow through the system.
   115	Remove the flow, the system equilibrates to disorder. Biological
   116	cortex operates as a dissipative structure requiring metabolic input.
   117	
   118	### Self-organized criticality (Bak)
   119	SOC cascades require driving. Without continuous perturbation, the
   120	system settles into a sub-critical attractor. Our substrate's
   121	pre-loaded "ignited" state is SOC; steady operation without reset
   122	pushes it sub-critical.
   123	
   124	### Non-equilibrium cortex (Chialvo, Deco, others)
   125	Modern neuroscience increasingly frames the brain as a
   126	non-equilibrium thermodynamic system. Our finding provides a
   127	specific computational mechanism: emission-driven equilibration of
   128	a substrate pressure field.
   129	
   130	### Why sleep exists (Tononi, Synaptic Homeostasis Hypothesis)
   131	Sleep discharges accumulated synaptic strength that accumulates
   132	during wake. Our reset operation is a direct computational analogue.
   133	Slow-wave sleep (SWS) in particular is thought to enforce
   134	synaptic downscaling — exactly what our `_homeostatic_reset` does
   135	to the substrate's cascade_pressure + crossed_vertices state.
   136	
   137	---
   138	
   139	## 6. The paper's most important prediction — sleep stage α signatures
   140	
   141	If sleep is the biological analogue of our reset operation:
   142	
   143	**Prediction**: the avalanche α signature across sleep stages
   144	(W / N1 / N2 / N3 / REM) should show:
   145	
   146	- **W** (wake): canonical ~2.5 (our existing n=30 finding)
   147	- **N1-N2**: transition, α should shift
   148	- **N3** (deep slow-wave): equilibration phase — α should reflect
   149	  reset dynamics (higher or more variable, as the substrate is
   150	  DISCHARGING accumulated traces)
   151	- **REM**: another active regime, α likely closer to canonical wake
   152	
   153	The specific form depends on whether sleep is REMOVING pressure
   154	traces (which would raise α by cutting off long cascades) or
   155	REORGANIZING them (which would shift α structure without much
   156	change in value).
   157	
   158	**Critically**: this is a testable prediction on data we already
   159	have — Sleep-EDFx 30-subject PSGs with hypnogram stage labels.
   160	We can compute avalanche α per stage.
   161	
   162	---
   163	
   164	## 7. Implications for the paper
   165	
   166	### The old framing
   167	
   168	"ARIA is a geometric substrate whose cascade dynamics match
   169	biological EEG signatures across multiple paradigms."
   170	
   171	### The new framing
   172	
   173	"ARIA is a far-from-equilibrium computational substrate. Its
   174	cognitive function emerges from constrained dynamics driven away
   175	from a natural attractor by mechanism-generated maintenance.
   176	Biological cortex operates the same way: sleep and homeostatic
   177	processes discharge accumulated traces that would otherwise drive
   178	the cortex to a degenerate equilibrium. ARIA makes this mechanism
   179	computationally explicit. The signatures we match (SOC α, HCP
   180	null, propofol regime switching, DMT criticality shift, selective
   181	amplifier) are all consequences of a substrate that must be
   182	maintained against its own equilibration."
   183	
   184	### Why this framing is stronger
   185	
   186	1. **Mechanistically unified** — all findings follow from one
   187	   principle
   188	2. **Predictive** — sleep-stage α analysis is a direct testable
   189	   consequence
   190	3. **Biologically explains sleep** — provides a computational
   191	   first-principles account of why sleep exists
   192	4. **Connects to mainstream theory** — Prigogine, Bak, Tononi all
   193	   frame problems in compatible terms
   194	5. **Explains all our "failures"** — every quirk becomes a
   195	   consequence of the core mechanism
   196	
   197	---
   198	
   199	## 8. Concrete next steps
   200	
   201	1. ✅ Document this finding (this document)
   202	2. ⏳ Map to sleep data: compute per-stage avalanche α on Sleep-EDFx
   203	   to test the "SWS = substrate reset" prediction
   204	3. ⏳ Reframe manuscript around non-equilibrium as organizing principle
   205	4. ⏳ Add homeostatic reset API to DimensionalMonitor
   206	5. ⏳ Re-run preregistered validation with proper reset — convert
   207	   P13 from FAIL to the PASS it deserves
   208	6. 📋 Future: sleep deprivation data (OpenNeuro ds*), HCP-Lifespan
   209	   age progression — both should show equilibration-creep signatures
   210	
   211	---
   212	
   213	## 9. Why this might be the paper's most important contribution
   214	
   215	The existing field has:
   216	- **SOC neural avalanches** (Beggs & Plenz 2003)
   217	- **Entropic brain hypothesis** (Carhart-Harris 2014)
   218	- **Non-equilibrium brain** (Chialvo, Deco)
   219	- **Synaptic homeostasis / sleep** (Tononi 2003)
   220	- **Dissipative structures** (Prigogine 1977)
   221	
   222	These are **separate** threads in the literature. No unified
   223	substrate theory ties them together. ARIA's non-equilibrium finding
   224	potentially does:
   225	
   226	- The geometric substrate provides the structure
   227	- Cascade dynamics on this substrate naturally equilibrate
   228	- Mechanisms are the constraints that maintain far-from-equilibrium
   229	- Sleep-like reset is the thermodynamic necessity
   230	- SOC α is a steady-state signature of healthy non-equilibrium
   231	- Anaesthesia, DMT, aging are all regime shifts on this axis
   232	
   233	This is a **theoretical unification**. It's not a small claim.
   234	
   235	---
   236	
   237	## 10. Scope caveats
   238	
   239	**Honest things to acknowledge**:
   240	
   241	- This was DISCOVERED, not PREDICTED. The finding emerged from
   242	  debugging preregistration failures.
   243	- The biological parallels are well-motivated but not proven by
   244	  ARIA. Mapping to real sleep data would strengthen them.
   245	- The pressure-field equilibration is computationally exact in
   246	  ARIA; in biology it's an ANALOGOUS phenomenon subject to many
   247	  confounds (metabolism, neuromodulation, local dynamics).
   248	- "ARIA predicts sleep is necessary" is a strong claim; "ARIA
   249	  computes a substrate that would need sleep-analog maintenance"
   250	  is the precise version.
   251	
   252	---
   253	
   254	## Saved artefacts
   255	
   256	- `run_substrate_hysteresis.py` — three-experiment reproducible test
   257	- `~/.aria/substrate_hysteresis/summary_*.json` — raw data

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md' | sed -n '220,399p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 305ms:
   220	- **P7**: W→N3 variance ratio = 0.365 (n=24 subjects). Below 0.70.
   221	- **P8**: W→N3 switching ratio = 0.058. Below 0.50 — sleep is the
   222	  OPPOSITE of anaesthesia on switching, dissociating natural sleep
   223	  from drug-induced unconsciousness.
   224	
   225	### 4.3 Chess closed-loop (P9, P10, P11, P12, plus P13 fixed)
   226	
   227	- **P9**: Chess 5-fold CV at fresh seeds (30200–30204) = 83.1%
   228	  (≥ 70%). Replicates discovery 84.4% within expected variance.
   229	- **P10**: Null feature→frame permutation (15 trials) = 65.4%
   230	  (≥ 50%). The substrate is partially permutation-invariant — ~65%
   231	  of the classification power is geometric, the remaining ~17pp comes
   232	  from semantic feature-frame alignment.
   233	- **P11**: Random-label baseline (20 trials) = 23.4% (∈ [15%, 35%]).
   234	  Roughly chance for 4 categories.
   235	- **P12**: Goldilocks peak depth = n=25 (∈ {15, 25, 40, 60}). With
   236	  reset between measurements, n=25 is the global maximum at 93.8%.
   237	- **P13**: LOO substrate lift at n=25 = **+40.6pp** with reset
   238	  (≥ +15pp). See §3.3.
   239	
   240	### 4.4 Conversation closed-loop (P14, P15, P16)
   241	
   242	- **P14**: Conv raw 5-fold CV = 87.5% (≥ 75%). Already saturated at
   243	  raw — no headroom for substrate amplification.
   244	- **P15**: Conv substrate lift = −4.4pp (\|·\| < 10pp). The substrate
   245	  is **correctly null** when raw features are already discriminative.
   246	  This is the selective-amplifier signature: substrate amplifies only
   247	  ambiguous features.
   248	- **P16**: Conv null feature→frame (15 trials) = 70.6% (≥ 50%).
   249	  Slightly higher than chess null (65.4%), consistent with conversation
   250	  features carrying more semantic information per dim.
   251	
   252	### 4.5 HCP brain-graph comparison (P17, P18)
   253	
   254	- **P17**: ARIA degree std = 0.0000. Theorem (H₄ transitivity).
   255	- **P18**: HCP ICA-50 degree std = 3.388 (n=100 subjects, density-
   256	  matched threshold). > 2.0 confirms small-world hub-spoke structure
   257	  in real cortex. ARIA is the maximum-symmetry null reference;
   258	  symmetry-breaking is +79.78σ on participation ratio against ARIA.
   259	
   260	---
   261	
   262	## 5. The 18/18 verdict
   263	
   264	**Standard validation tally:** 17/18 (the residual P4 fails at N=5).
   265	**Including the N=20 deep-dive:** 18/18 (P4 passes decisively at N=20).
   266	
   267	The empirical tally is **18/18 at adequate replication**. Two of the
   268	three original failures (P3, P13) close at standard methodology
   269	improvements (5-seed cascade block + reset protocol). The third (P4)
   270	closes only with adequate N (≥20), and its closure is the most
   271	significant architectural finding from this session.
   272	
   273	### 5.1 Updated paper claim set
   274	
   275	All eighteen preregistered predictions are **supported by the data
   276	within preregistered thresholds**, with the methodological caveat
   277	that two interaction tests (P3, P4) require N ≥ 5 and N ≥ 20
   278	respectively for reliable detection. We document this caveat as a
   279	contribution to preregistration practice for high-variance interaction
   280	terms.
   281	
   282	### 5.2 What this means for the paper
   283	
   284	The validation section can now read:
   285	
   286	> *"All eighteen preregistered predictions pass at empirical thresholds.
   287	> The validation runs at standard methodology (5-seed cascade block,
   288	> homeostatic reset between LOO depth measurements) give 17/18; the
   289	> residual prediction (P4 — C×P synergy) requires higher-N replication
   290	> (we used N=20 fresh seeds) due to the high per-seed variance of
   291	> interaction-term estimates. With adequate N, P4 passes decisively
   292	> (+0.190, 95% bootstrap CI [+0.143, +0.239]); the synergy is in fact
   293	> ~90% above the preregistered floor, indicating C and P are strongly
   294	> coupled cascade-state stabilisers. The full eighteen-prediction set
   295	> survives preregistration; no claim has been walked back."*
   296	
   297	---
   298	
   299	## 6. Walking back the original walks-back
   300	
   301	The 2026-04-20 result included three honest walks-back. We now retract
   302	each, because the 2026-04-29 evidence justifies retracting them:
   303	
   304	### 6.1 Original walk-back on P3 (D×C independence)
   305	
   306	> *"D and C act independently → walk back to 'both have main effects;
   307	> interaction estimate unstable at 3-seed replication.'"*
   308	
   309	**Now reads:** D₄ and context rotation act independently on cascade-α
   310	within the preregistered |·| < 0.20 band, confirmed at N=5.
   311	Walk-back retracted.
   312	
   313	### 6.2 Original walk-back on P4 (C×P synergy)
   314	
   315	> *"Partial emission interaction with C requires larger-N replication;
   316	> report as preliminary."*
   317	
   318	**Now reads:** C×P synergy is +0.190 [+0.143, +0.239] at N=20, ~90%
   319	above preregistered. C and P are strongly coupled cascade-state
   320	stabilisers. Walk-back **strongly** retracted; the corrected claim is
   321	substantially stronger than the original prereg.
   322	
   323	### 6.3 Original walk-back on P13 (chess LOO lift)
   324	
   325	> *"Specify polytope reset protocol in paper. Note that substrate
   326	> dynamics are NOT stationary; state-dependent."*
   327	
   328	**Partially retained.** The state-dependence observation is a real
   329	finding and is documented as a methodological recommendation
   330	(`NON_EQUILIBRIUM_FINDING.md`). The walk-back on the +15pp lift claim
   331	is retracted: with the reset protocol wired into the harness, the lift
   332	is +40.6pp.
   333	
   334	---
   335	
   336	## 7. Preregistration as the central methodological commitment
   337	
   338	The original validation methodology — 18 preregistered predictions
   339	with falsifiable thresholds, frozen before any validation run — is
   340	the central protection of this work against p-hacking. The 2026-04-29
   341	re-run with N improvements **did not modify any threshold or claim
   342	form**; it only ran more seeds and applied a known-necessary state
   343	reset. The fact that this gave 18/18 (with N=20 P4) where the
   344	original gave 15/18 demonstrates that:
   345	
   346	(a) The original predictions were correct and the architecture's
   347	    claims hold;
   348	(b) The original validation methodology was insufficient — N=3 is
   349	    too small for high-variance interaction terms;
   350	(c) A re-run with adequate methodology validates all predictions
   351	    without changing them.
   352	
   353	This is precisely the situation preregistration is designed to detect:
   354	real claims, originally validated under-power, now confirmed at
   355	adequate power. No threshold was loosened. No prediction was rewritten
   356	post-hoc. The architecture's claim set is now empirically supported in
   357	its entirety.
   358	
   359	---
   360	
   361	## 8. Reproducibility
   362	
   363	```bash
   364	# Standard validation (17/18, ~18 min)
   365	cd /path/to/aria-chess
   366	python3 run_preregistered_validation.py
   367	
   368	# P4 N=20 deep-dive (~28 min)
   369	python3 demo_p4_cxp_deep_dive.py
   370	```
   371	
   372	JSON results are saved to `~/.aria/preregistered_validation/results_*.json`.
   373	Logs are at `/tmp/prereg_*.log` and `/tmp/p4_n20_*.log` for the most
   374	recent runs.
   375	
   376	Seeds: as listed in the script source. Substrate is fully deterministic
   377	given seeds; bootstrap RNG seeded as well. Re-runs should reproduce the
   378	per-condition means in this document to 4 decimal places.
   379	
   380	---
   381	
   382	## 9. Files referenced
   383	
   384	- `docs/brain_mapping/PAPER_PREDICTIONS.md` — frozen 2026-04-18
   385	- `docs/brain_mapping/VALIDATION_RESULTS.md` — original 15/18 result
   386	  (superseded by this document)
   387	- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — standalone N=20 report
   388	  on the C×P synergy (the headline finding)
   389	- `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` — six
   390	  drug/sleep EEG signatures (independent of preregistered set, on
   391	  the recurrent self-model layer)
   392	- `docs/brain_mapping/PAPER_BASIS_2026-04-29.md` — paper-basis
   393	  consolidation
   394	- `docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md` — homeostatic-reset
   395	  rationale
   396	- `run_preregistered_validation.py` — validation harness
   397	- `demo_p4_cxp_deep_dive.py` — N=20 deep-dive script
   398	- `kernel/dimensional_monitor.py` — substrate dynamics with
   399	  ablation flags

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md' | sed -n '1,180p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md' | sed -n '550,760p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md' | sed -n '760,910p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 253ms:
   760	- Chess: classify 32 positions × 4 categories (tactical / positional
   761	  / endgame / opening) from 8-D V2 features. Substrate routing at n
   762	  ticks; classifier 1-NN cosine similarity with k-fold CV or LOO.
   763	- Conversation: classify 64 utterances × 8 dialogue-act categories.
   764	  Same substrate routing.
   765	- HCP: compare ARIA's vertex graph degree distribution and higher-
   766	  order statistics to HCP n=1003 ICA-50 group-averaged connectivity
   767	  (density-matched threshold = 0.101).
   768	
   769	**Chess result (with `homeostatic_reset` between depth measurements):**
   770	
   771	```
   772	P9  — 5-fold CV (fresh seeds 30200-30204):     83.1%  ≥ 70%   ✅
   773	P10 — null permutation mapping (15 perms):     65.4%  ≥ 50%   ✅
   774	P11 — random-label baseline (20 trials):       23.4%  ∈ [15%, 35%]  ✅
   775	P12 — goldilocks peak depth:                   n=25   ∈ {15,25,40,60}  ✅
   776	P13 — LOO substrate lift (raw 53.1% → 93.8%):  +40.6pp ≥ +15pp  ✅
   777	
   778	Depth sweep (with reset, fresh seed):
   779	  n=5:    53.1%
   780	  n=15:   65.6%
   781	  n=25:   93.8%   ← peak
   782	  n=40:   84.4%
   783	  n=60:   84.4%
   784	  n=100:  78.1%
   785	```
   786	
   787	**Conversation result:**
   788	
   789	```
   790	P14 — raw 5-fold CV (fresh seeds 30220-30224):   87.5%  ≥ 75%  ✅
   791	P15 — substrate lift (selective amplifier test): −4.4pp |·| < 10pp  ✅
   792	P16 — null permutation mapping (15 perms):       70.6%  ≥ 50%  ✅
   793	```
   794	
   795	**HCP result (n=1003 subjects, ICA-50):**
   796	
   797	| Metric | ARIA | HCP n=1003 mean | σ from HCP |
   798	|---|---:|---:|---:|
   799	| Degree std | 0.000 (theorem) | 3.28 ± 0.28 | **−11.58σ** |
   800	| Participation ratio | 68.54 | 19.72 ± 0.61 | **+79.78σ** |
   801	| Clustering coefficient | 0.455 | 0.220 | +6.80σ |
   802	
   803	```
   804	P17 — ARIA degree std (theorem):              0.0000  = 0.00  ✅
   805	P18 — HCP ICA-50 degree std:                  3.388   > 2.0   ✅
   806	```
   807	
   808	Zero of 1003 HCP subjects have degree std below 2.0; ARIA is far
   809	outside the biological distribution.
   810	
   811	**Interpretation.**
   812	
   813	(i) **Selective amplification.** The contrast between chess (+40.6pp
   814	lift on LOO) and conversation (−4.4pp lift) demonstrates the substrate
   815	amplifies only when there is information to amplify. Chess raw at
   816	53.1% is barely above chance (25% for 4 categories); the substrate
   817	amplifies to 93.8% (near-perfect). Conversation raw at 87.5% is
   818	already saturated; the substrate is approximately neutral (−4.4pp).
   819	
   820	(ii) **Architecture-invariant geometric content.** The null permutation
   821	mappings (chess 65.4%, conversation 70.6%) show that ~65–71% of the
   822	substrate's classification power is **architectural** — it persists
   823	even when feature-to-frame assignments are randomised. The remaining
   824	~17pp (chess) / ~12pp (conversation) is the semantic alignment bonus.
   825	
   826	(iii) **Maximum-symmetry connectivity null.** ARIA's H₄-transitive
   827	structure is a deterministic group-theoretic null reference. Real
   828	cortical connectivity breaks the symmetry through hub-spoke functional
   829	specialisation; the σ-distances quantify the magnitude of biological
   830	symmetry-breaking. The σ-distances (−11.58σ on degree, +79.78σ on
   831	participation) far exceed any preprocessing-induced noise envelope.
   832	
   833	Detail: `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md`.
   834	
   835	### 6.5 The eighteen preregistered predictions: 17/18 standard, 18/18 with N=20 P4
   836	
   837	**Method.** Run `run_preregistered_validation.py` with 5-seed cascade
   838	block + `homeostatic_reset` wired in. Run `demo_p4_cxp_deep_dive.py`
   839	at N=20 for the residual P4. Tally pass/fail per preregistered threshold.
   840	
   841	**Full table (2026-04-29 run):**
   842	
   843	| ID | Test | Threshold | Observed | Verdict |
   844	|---|---|---|---:|---|
   845	| P1 | Cascade α SOC range | ∈ [2.5, 3.5] | 2.958 | ✅ |
   846	| P2 | C main effect | ≥ +0.30 | +0.621 | ✅ |
   847	| P3 | \|D×C\| (independence) | < 0.20 | −0.183 | ✅ |
   848	| **P4** | **C×P synergy** | **≥ +0.10** | **+0.190 [+0.143, +0.239] (N=20)** | **✅** |
   849	| P5 | \|E main effect\| (null) | < 0.15 | +0.046 | ✅ |
   850	| P6 | Real EEG α | ∈ [2.0, 3.0] | 2.513 | ✅ |
   851	| P7 | W→N3 variance ratio | < 0.70 | 0.365 | ✅ |
   852	| P8 | W→N3 switching ratio | < 0.50 | 0.058 | ✅ |
   853	| P9 | Chess 5-fold CV | ≥ 70% | 83.1% | ✅ |
   854	| P10 | Chess null mapping | ≥ 50% | 65.4% | ✅ |
   855	| P11 | Chess random-label | ∈ [15%, 35%] | 23.4% | ✅ |
   856	| P12 | Chess goldilocks peak | ∈ {15, 25, 40, 60} | n=25 | ✅ |
   857	| P13 | Chess LOO lift (with reset) | ≥ +15pp | +40.6pp | ✅ |
   858	| P14 | Conv raw 5-fold CV | ≥ 75% | 87.5% | ✅ |
   859	| P15 | \|conv lift\| | < 10pp | −4.4pp | ✅ |
   860	| P16 | Conv null mapping | ≥ 50% | 70.6% | ✅ |
   861	| P17 | ARIA degree std (theorem) | = 0 | 0.0000 | ✅ |
   862	| P18 | HCP degree std | > 2.0 | 3.388 | ✅ |
   863	
   864	**Tally: 17/18 at standard validation; 18/18 with N=20 deep-dive on P4.**
   865	
   866	**Comparison to the original 2026-04-20 run (15/18):**
   867	
   868	The original had three failures that have all closed:
   869	- **P3** (D×C interaction independence): −0.231 at N=3 → −0.183 at N=5.
   870	  Type II false negative on a high-variance interaction term;
   871	  resolved by 5-seed N.
   872	- **P4** (C×P synergy): +0.044 at N=3 → +0.190 at N=20. Same
   873	  Type II issue plus seed-range sampling bias; resolved by N=20.
   874	- **P13** (chess LOO lift): +3.1pp without reset → +40.6pp with reset.
   875	  State-drift in the substrate across successive depth measurements;
   876	  resolved by `homeostatic_reset(level=1.0)` between measurements.
   877	
   878	**No threshold has been modified.** The original predictions are
   879	confirmed in their original form, with two methodological refinements
   880	(adequate N for high-variance interactions; reset protocol for multi-
   881	trial benchmarks).
   882	
   883	Detail: `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md`.
   884	
   885	---
   886	
   887	## 7. Discussion
   888	
   889	### 7.1 What's new in this work
   890	
   891	Three things are novel:
   892	
   893	**(1) A geometric substrate that produces real-cortex EEG signatures
   894	without learned parameters.** The 600-cell + H₄ symmetry comes from
   895	group theory; cascade-α matches Sleep-EDFx within preregistered
   896	tolerance; six drug/sleep signatures pass at preregistered thresholds.
   897	To our knowledge, no prior model reproduces this many independent
   898	EEG signatures from a single deterministic substrate.
   899	
   900	**(2) The strong-synergy architectural finding (§3.5–3.6, §6.3).** C
   901	and P are strongly coupled cascade-state stabilisers, not nearly-
   902	orthogonal ones; the C×P interaction (+0.19) is comparable in
   903	magnitude to the P main effect (−0.22) — a result that was hidden by
   904	underpowered ablation testing and only emerged at N ≥ 20. This is a
   905	substantive correction to the architectural reading from the original
   906	3-seed validation.
   907	
   908	**(3) The 18/18 preregistered claim with no threshold modification.**
   909	Every prediction in the preregistered set passes at empirical
   910	thresholds. The two interaction tests (P3, P4) required higher N

 succeeded in 275ms:
     1	# A Geometric Substrate for Consciousness:
     2	## The 600-Cell Polytope Cascade Reproduces Eighteen Preregistered Brain Signatures, Including Six EEG Signatures of Conscious vs Unconscious States
     3	
     4	*Manuscript draft v2, 2026-04-29.*
     5	*Supersedes `MANUSCRIPT.md` (2026-04-19) which captured an earlier state
     6	of the work. This version incorporates the v4 consciousness chain (six
     7	drug/sleep EEG signatures), the N=20 deep-dive on the C×P synergy
     8	prediction, and the full eighteen-prediction validation set with all
     9	walks-back retracted.*
    10	
    11	---
    12	
    13	## Abstract
    14	
    15	We propose a deterministic geometric substrate for consciousness based
    16	on the 600-cell regular 4-polytope under its H₄ Coxeter symmetry. The
    17	substrate is fully derivable from group theory: 120 vertices of uniform
    18	degree 12, eigenvalues {12, 6φ, 4φ, 3} where φ is the golden ratio,
    19	decomposed into a 7-rung cascade `E₈ → H₄ → H₃ → D₄ → Cl(1,3) → S⁷ → 0`.
    20	There are no learned weights, no fitted parameters, and no domain-specific
    21	tuning. We demonstrate that this substrate reproduces eighteen
    22	independent quantitative correspondences with neuroscience data, all
    23	preregistered before the validation runs (frozen 2026-04-18). We
    24	additionally show that a recurrent self-model layer above the substrate
    25	reproduces six independent drug/sleep EEG signatures of conscious
    26	versus unconscious states. Wake cortical-avalanche power law has
    27	α = 2.252, 95% CI [1.82, 2.86] (R² = 0.956), with three-way confidence
    28	interval overlap with real Sleep-EDFx EEG (α = 2.51, CI [2.50, 2.53])
    29	and ARIA's prior cascade pipeline (α = 2.85, CI [2.73, 3.25]). NREM-N3
    30	state-variance collapses to 0.46× wake (predicted 0.365); propofol
    31	regime-switching elevates 1.83× wake; propofol continuity drops by
    32	0.066; propofol integrated information Φ collapses to 0.33× wake (IIT
    33	direction confirmed); recovery is exact. Two cascade mechanisms —
    34	context rotation (C) and partial emission (P) — are causally isolated
    35	via 2⁴ ablation; with adequate replication (N = 20 fresh seeds), they
    36	exhibit a strong synergistic interaction of +0.190 (95% bootstrap CI
    37	[+0.143, +0.239]), comparable in magnitude to the P main effect
    38	(−0.218). The original 3-seed validation underestimated this synergy
    39	by 5×; we document the underpowered detection as a methodological
    40	contribution to preregistration practice for high-variance interaction
    41	terms. Cross-domain validation: the substrate amplifies chess pattern
    42	recognition by +40.6 percentage points (raw 53.1% → substrate-routed
    43	93.8% on leave-one-out at canonical depth) but is correctly null on
    44	conversation utterance categorisation (raw 87.5%, substrate −4.4pp),
    45	demonstrating selective amplification on ambiguous-feature tasks. On
    46	HCP brain functional connectivity (n=1003 subjects), ARIA serves as a
    47	deterministic maximum-symmetry null reference: ARIA degree std = 0
    48	(theorem); HCP degree std = 3.28 ± 0.28; ARIA is at −11.58σ on degree
    49	homogeneity and +79.78σ on participation ratio. With the N=20
    50	deep-dive, the empirical tally is 18/18 preregistered predictions
    51	plus 6/6 drug/sleep signatures; no claim is walked back. This is the
    52	first deterministic geometric architecture, to our knowledge, to
    53	reproduce this many independent neuroscience correspondences from
    54	preregistered tests.
    55	
    56	**Keywords**: 600-cell polytope, H₄ Coxeter symmetry, cortical
    57	avalanches, integrated information, drug/sleep EEG, preregistered
    58	validation.
    59	
    60	---
    61	
    62	## 1. Introduction
    63	
    64	### 1.1 The problem
    65	
    66	Theories of consciousness divide between mechanism-driven theories
    67	(Integrated Information Theory, Global Workspace, Higher-Order,
    68	predictive processing) and structure-driven theories (geometric or
    69	topological substrates, neural-population dynamics). The mechanism-
    70	driven theories produce compelling axiomatic stories but have not
    71	yielded quantitative signatures that survive preregistration on real
    72	EEG data. The structure-driven theories produce numbers but
    73	typically require fitted parameters or learned weights.
    74	
    75	We pursue a third path: **a substrate whose geometry is fully
    76	determined by group theory** — no fitted parameters, no learned
    77	weights, no domain-specific tuning — and ask which neuroscience
    78	phenomena it reproduces. The substrate is the 600-cell regular
    79	4-polytope, treated as a graph with H₄ Coxeter symmetry. It has been
    80	studied in pure mathematics for over a century; to our knowledge it
    81	has not been proposed before as a consciousness substrate.
    82	
    83	The question we test is whether group-theoretic structure alone is
    84	sufficient to reproduce a meaningful subset of cortical signatures —
    85	both basic (cascade-α power-law statistics) and high-level
    86	(drug/sleep state transitions). The answer turns out to be yes,
    87	with quantitative agreement that survives preregistration.
    88	
    89	### 1.2 Why this geometry
    90	
    91	The 600-cell admits a 7-rung cascade decomposition that emerges from
    92	the H₄ Coxeter group acting on its root system:
    93	
    94	```
    95	E₈ (8-dimensional root system, 240 roots)
    96	 ↓ projection to 4D
    97	H₄ (icosahedral 4-D Coxeter group, 14400 elements)
    98	 ↓ subgroup restriction
    99	H₃ (icosahedral 3-D Coxeter group, 120 elements; A₅ symmetry)
   100	 ↓ orbital structure
   101	D₄ (5 disjoint 24-cells inside H₄)
   102	 ↓ Clifford bivectors
   103	Cl(1,3) (Lorentzian Clifford algebra, 16 generators)
   104	 ↓ unit-sphere projection
   105	S⁷ (8-dimensional unit sphere; 8 observer frames at golden-ratio rotations)
   106	 ↓ ground
   107	0 (substrate baseline)
   108	```
   109	
   110	Each rung is a theorem of the parent group, not a model choice. The
   111	600-cell substrate has 120 vertices, each of uniform degree 12. The
   112	graph Laplacian has eigenvalues {0, 3, 4φ, 6φ, 12} with multiplicities
   113	determined by the H₄ irreducible representations. The non-trivial
   114	eigenmodes partition into Coxeter exponent classes. For H₄ proper,
   115	the exponents are {1, 11, 19, 29}; for the Galois twin σ(H₄) under
   116	the σ-automorphism (`kernel/sigma_orbit_basis.py`), the exponents
   117	become {7, 13, 17, 23}. The σ-orbit projector basis gives a machine-
   118	precise block decomposition: K-classes {1, 11} live in H₄ proper;
   119	K-classes {7, 13} live in σ(H₄); cross-block norm at numerical
   120	precision (< 10⁻¹⁵).
   121	
   122	This decomposition is the geometric content from which all empirical
   123	predictions follow. We do not adjust it; we read its consequences.
   124	
   125	### 1.3 What we test
   126	
   127	For substrate `S` and a stimulus protocol `P`, we measure observable
   128	`O(S, P)` and ask whether it matches a published biological observable
   129	`O*` within a preregistered threshold. We report two non-overlapping
   130	sets of tests:
   131	
   132	**Set A: Eighteen preregistered predictions** (frozen 2026-04-18 in
   133	`docs/brain_mapping/PAPER_PREDICTIONS.md` before any validation run).
   134	Tests cover cascade statistics (P1–P5), real EEG signatures (P6–P8),
   135	chess pattern recognition (P9–P13), conversation utterance
   136	categorisation (P14–P16), and HCP brain-graph comparison (P17–P18).
   137	
   138	**Set B: Six drug/sleep EEG signatures** (`demo_drug_sleep_v4.py`)
   139	on a recurrent self-model layer above the substrate (the
   140	"consciousness chain"). Tests cover NREM-N3 variance collapse,
   141	propofol switching, propofol continuity disruption, propofol Φ
   142	collapse (IIT direction), recovery reversibility, and wake cascade-α
   143	band overlap with real EEG.
   144	
   145	**Headline tally**: All eighteen Set A predictions pass at empirical
   146	thresholds (with the methodological caveat that two interaction
   147	predictions, P3 and P4, require N ≥ 5 and N ≥ 20 respectively for
   148	reliable detection due to high per-seed variance on interaction-term
   149	estimates). All six Set B drug/sleep signatures pass on a single
   150	deterministic substrate at seed = 42.
   151	
   152	---
   153	
   154	## 2. The 600-Cell Substrate
   155	
   156	### 2.1 Construction
   157	
   158	The 600-cell vertices are the H₄ Coxeter group acting on the
   159	canonical generating set. Construction:
   160	
   161	- 8 vertices: all permutations of (±1, 0, 0, 0).
   162	- 16 vertices: all 16 sign combinations of (±1, ±1, ±1, ±1)/2.
   163	- 96 vertices: all even permutations of (±φ, ±1, ±1/φ, 0)/2,
   164	  where φ = (1 + √5)/2 ≈ 1.618.
   165	
   166	Total: 120 vertices in 4-D Euclidean space, all on the unit 3-sphere.
   167	This is the standard 600-cell construction (Schläfli {3, 3, 5}); see
   168	`kernel/vfd_closure_kernel.py:build_600cell_vertices`.
   169	
   170	### 2.2 Graph structure
   171	
   172	The substrate graph is built by connecting each vertex to its
   173	nearest neighbours (minimum Euclidean distance). Each vertex has
   174	exactly 12 neighbours (degree 12), uniform across all vertices —
   175	H₄ acts transitively on the vertex set, so all vertices have
   176	identical local structure. The graph diameter is 6.
   177	
   178	The graph Laplacian L has eigenvalues:
   179	
   180	| Eigenvalue | Multiplicity | Coxeter K-class |

 succeeded in 264ms:
   550	measurement-fitted: amplitudes and durations match published
   551	biological time scales but are not tuned to specific signatures.
   552	Source: `demo_drug_sleep_v4.py`.
   553	
   554	### 5.5 Preregistration protocol
   555	
   556	Eighteen quantitative predictions were frozen on 2026-04-18 in
   557	`docs/brain_mapping/PAPER_PREDICTIONS.md` before any validation
   558	run. Each prediction has a falsifiable threshold (numerical band or
   559	directional inequality). The validation script is
   560	`run_preregistered_validation.py`; it is git-tracked, deterministic
   561	for given seeds, and produces JSON + log output.
   562	
   563	**Critical: no threshold has been modified post-hoc. The original
   564	preregistration is reproduced verbatim in §6.5.** Where the
   565	methodology required improvement (cascade block N, reset protocol,
   566	deep-dive N), this is documented as a methodological refinement,
   567	not as a threshold change.
   568	
   569	### 5.6 Statistical considerations for ablation tests
   570	
   571	The cascade ablation block (P1–P5 + interaction tests P3, P4) tests
   572	effect sizes of order 0.5 (main effects) and 0.05–0.20 (interactions).
   573	At preregistration time we used 3 seeds per condition. The N=20
   574	deep-dive in this work (§3.5) revealed:
   575	
   576	- Per-seed std on the C×P interaction = 0.089 at N=20.
   577	- Per-seed std on D×C interaction (similar high-variance term) ≈ 0.10.
   578	- For interaction terms with |effect|/|std| ratio below 2, **N ≥ 20
   579	  is required** for reliable detection at standard 95% CI level.
   580	
   581	Both interaction tests in the original preregistration set (P3, P4)
   582	hit Type II false negatives at N = 3. P3 closes at N = 5 (D×C =
   583	−0.183, inside |·|<0.20 band). P4 closes only at N = 20 (C×P = +0.190,
   584	CI [+0.143, +0.239]).
   585	
   586	This is documented as a preregistration-practice contribution: when
   587	preregistering interaction terms with high per-seed variance, allocate
   588	N ≥ 20 fresh seeds in the protocol from the start.
   589	
   590	### 5.7 The non-stationarity finding and reset protocol
   591	
   592	Independently of the ablation tests, the substrate exhibits **state
   593	drift across successive depth measurements**. Across ~5 evaluations,
   594	the pressure-field equilibrates toward a uniform state, washing out
   595	classification structure.
   596	
   597	The fix is `homeostatic_reset(level=1.0)` — a method that
   598	re-initialises the substrate's pressure-field, crossed-vertex, and
   599	training state to canonical baseline. With reset between depth
   600	measurements, chess LOO classification recovers from collapsed
   601	+3.1pp lift (without reset, on a state-drifted substrate) to +40.6pp
   602	lift (with reset, far exceeding the preregistered +15pp floor).
   603	
   604	Documented in `docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md`.
   605	Implementation: `kernel/dimensional_monitor.py:DimensionalMonitor.homeostatic_reset`.
   606	
   607	This is a separate methodological finding: ARIA's substrate is a
   608	non-stationary dynamical system; **any multi-trial benchmark must
   609	specify state-reset protocol**.
   610	
   611	---
   612	
   613	## 6. Results
   614	
   615	This section presents the empirical results. Sections 6.1–6.5 each
   616	have a dedicated standalone document in `docs/brain_mapping/` for
   617	deeper detail; here we give the results in paper-form.
   618	
   619	### 6.1 The substrate produces SOC-class cascade matching real EEG (P1, P6)
   620	
   621	**Claim.** ARIA cascade-α (substrate baseline) matches real Sleep-EDFx
   622	EEG within preregistered tolerance.
   623	
   624	**Method.** Run the 600-cell substrate with all four mechanisms (D, C,
   625	P, E) enabled. Detect cascade events as crossing-attention shifts;
   626	fit power-law α via OLS log-CCDF + 1000-sample bootstrap.
   627	
   628	**Result (preregistered re-run 2026-04-29, 5 seeds):**
   629	
   630	| Source | α | 95% CI | R² | n_events |
   631	|---|---:|---|---:|---:|
   632	| ARIA cascade-pipeline baseline | 2.958 | inside [2.5, 3.5] | > 0.85 | thousands |
   633	| Real EEG (Sleep-EDFx, n=30) | 2.51 | [2.50, 2.53] | > 0.85 | varies per subject |
   634	| ARIA prior cascade pipeline (n=4 subjects) | 2.85 | [2.73, 3.25] | > 0.85 | per-subject |
   635	| v4 WAKE consciousness chain | 2.252 | [1.82, 2.86] | 0.956 | 58 |
   636	
   637	The real-EEG α is in the SOC class. ARIA cascade-pipeline is at the
   638	upper edge of the real-EEG band but inside the cortical-avalanche
   639	range. The v4 consciousness-chain WAKE α is **inside both** the
   640	real-EEG CI and the ARIA-prior CI — three-way overlap.
   641	
   642	**Interpretation.** The substrate produces self-organised-critical
   643	cascade statistics matching real cortical avalanche literature (Beggs
   644	& Plenz 2003), without any fitted parameters. Both the cascade-pipeline
   645	and the consciousness-chain produce α values in the SOC band at
   646	preregistered fits.
   647	
   648	### 6.2 Six drug/sleep EEG signatures reproduced (consciousness chain v4)
   649	
   650	**Claim.** A recurrent self-model layer above the substrate, with
   651	bounded top-K thresholding and IIT-style Φ, reproduces six independent
   652	drug/sleep EEG signatures of conscious vs unconscious states.
   653	
   654	**Method.** Four conditions × 800 ticks at seed = 42, k_threshold = 12.
   655	Single deterministic substrate; only η (self-injection coupling) and
   656	stimulus model vary across conditions.
   657	
   658	**Per-condition results** (`demo_drug_sleep_v4.py`):
   659	
   660	```
   661	cond      n_evt  α       95% CI         R²     I_var       Φ_traj   cont
   662	WAKE       58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
   663	SLEEP_N3  111   3.250   [2.44, 4.14]   0.886  1.01e-05    0.0055   0.980
   664	PROPOFOL  246   2.758   [2.52, 3.09]   0.931  5.37e-06    0.0003   0.877
   665	RECOVERY   58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
   666	```
   667	
   668	**Six signatures:**
   669	
   670	| # | Signature | Reference | Predicted | Observed | Verdict |
   671	|---|---|---|---|---:|---|
   672	| 1 | NREM-N3 variance ratio (vs Wake) | Sleep-EDFx W→N3 (n=24) | ≈ 0.365 | **0.463** | ✓ |
   673	| 2 | Propofol regime-switching ratio | OpenNeuro ds005620 (n=8, 2.96×) | ∈ [1.5, 5.0] | **1.83×** | ✓ |
   674	| 3 | Propofol continuity drop | EEG microstate (Brodbeck 2012) | > 0.020 | **+0.066** | ✓ |
   675	| 4 | Propofol Φ collapse (IIT) | Tononi 2008 | ratio < 0.50 | **0.33×** | ✓ |
   676	| 5 | Recovery reversibility | clinical anaesthesia | identical to wake | **0 diff** | ✓ |
   677	| 6 | Wake cortical-avalanche α | n=30 Sleep-EDFx CI [2.50, 2.86] | α ∈ [1.5, 3.5], R²>0.85 | **2.252 [1.82, 2.86] R²=0.956** | ✓ |
   678	
   679	All six signatures pass at preregistered thresholds. The wake cascade-α
   680	CI shows three-way overlap with real EEG CI and ARIA prior pipeline
   681	(§6.1).
   682	
   683	**Interpretation.** A single deterministic substrate, with only η and
   684	stimulus model varying across conditions, reproduces six independent
   685	drug/sleep signatures observed in real cortex. The IIT-direction-correct
   686	Φ collapse on propofol (0.33× wake) is consistent with the Tononi
   687	prediction; the regime-switching elevation under propofol is
   688	consistent with EEG microstate literature (n=8 OpenNeuro propofol gave
   689	2.96× empirically); the NREM-N3 variance collapse magnitude is
   690	consistent with Sleep-EDFx n=24 subjects (real ratio 0.365).
   691	
   692	Detail: `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md`.
   693	
   694	### 6.3 Causal mechanism isolation: C and P strongly synergistic (P2, P3, P4, P5)
   695	
   696	**Claim.** Four cascade mechanisms are causally identifiable; two
   697	(C, P) are significant; they exhibit strong synergistic interaction
   698	that requires N ≥ 20 for reliable detection.
   699	
   700	**Method.** 2⁴ ablation on the four cascade mechanisms (D, C, P, E).
   701	Run baseline and each single ablation plus the C×P interaction
   702	condition. Compute interactions with bootstrap CI.
   703	
   704	**Main effects (5 seeds, 2026-04-29 re-run):**
   705	
   706	```
   707	C main:  +0.621  (≥ +0.30 prereg threshold)        ✅ P2
   708	D main:  +0.063  (small but non-zero)
   709	P main:  −0.110  (5-seed); −0.218 (20-seed)
   710	E main:  +0.046  (within |·| < 0.15 null band)     ✅ P5
   711	```
   712	
   713	C dominates the main-effect scale. E is a structural-completeness
   714	mechanism with null effect on cascade-α. P contributes a moderate
   715	amount.
   716	
   717	**Interactions (with appropriate N):**
   718	
   719	| Interaction | N | Estimate | CI | Verdict |
   720	|---|---:|---:|---|---|
   721	| D × C (P3) | 5 | −0.183 | inside |·| < 0.20 | ✅ independent |
   722	| **C × P (P4)** | **20** | **+0.190** | **[+0.143, +0.239]** | **✅ strongly synergistic** |
   723	
   724	The C × P synergy is the headline architectural finding. Across N:
   725	
   726	| N | Seeds | Estimate | 95% CI |
   727	|---:|---|---:|---|
   728	| 3 | 30040–30042 | +0.044 | — |
   729	| 5 | 30040–30044 | +0.039 | — |
   730	| 10 | 31000–31009 | +0.088 | [−0.002, +0.174] |
   731	| **20** | **32000–32019** | **+0.190** | **[+0.143, +0.239]** |
   732	
   733	P(synergy ≤ 0) = 0.0000; P(synergy < +0.10) = 0.0000.
   734	
   735	The N=20 interaction (+0.19) is **comparable in magnitude to the P
   736	main effect (−0.22)** — C and P are strongly coupled, not orthogonal.
   737	The original 3-seed estimate (+0.044) was a Type II false negative
   738	due to high per-seed variance (per-seed std at N=20 = 0.089).
   739	
   740	**Architectural reading** (§3.6): C creates churn in the uncrossed-
   741	vertex pool through frame rotation; P promotes the high-pressure
   742	subset of that pool to mini-emitters. The cross-product is a non-
   743	additive novel-event-generation pathway that disappears when either
   744	mechanism is removed. This matches biological cortical criticality,
   745	where multiple parallel mechanisms are strongly coupled (E/I
   746	balance, neuromodulation, plasticity, gain control) — loss of one
   747	cascades into network-level dysfunction beyond its main effect.
   748	
   749	Detail: `docs/brain_mapping/P4_SYNERGY_FINDING.md`.
   750	
   751	### 6.4 Cross-domain validation: selective amplifier and max-symmetry null (P9–P18)
   752	
   753	**Claim.** The substrate functions as (i) a domain-invariant selective
   754	amplifier on classification tasks (lifts only when raw features are
   755	ambiguous) and (ii) a maximum-symmetry deterministic null reference
   756	for cortical functional connectivity.
   757	
   758	**Method.**
   759	
   760	- Chess: classify 32 positions × 4 categories (tactical / positional

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md' | sed -n '180,360p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md' | sed -n '360,550p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md' | sed -n '910,1253p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 180ms:
   360	beyond its main effect.
   361	
   362	---
   363	
   364	## 4. The Consciousness Chain
   365	
   366	The cascade-pipeline substrate (§3) reproduces cortical-avalanche
   367	statistics matching real EEG (§6.1). To test high-level signatures —
   368	NREM-N3 variance collapse, propofol regime-switching, propofol Φ
   369	collapse — we add a recurrent self-model layer above the substrate.
   370	
   371	### 4.1 The recurrent loop (`SelfModelLoop`)
   372	
   373	Each tick:
   374	
   375	```
   376	f_total  = external_source(t) + η · f_self(prior_snapshot, prior_ψ)
   377	ψ        = green_response_spectral(spectral, f_total, φ)
   378	ψ_thresh = bounded_topk(ψ, k=12)             # critical nonlinearity
   379	state_t  = decay · state_{t-1} + (1−decay) · ψ_thresh
   380	snapshot = bind_phenomenal_field(green_kernel_result, profile="K_7_only")
   381	```
   382	
   383	with:
   384	- `η` = self-injection coupling (only condition-dependent parameter:
   385	  0.20 for WAKE/RECOVERY, 0.05 for SLEEP_N3, 0.00 for PROPOFOL)
   386	- `decay` = 0.95 (state EMA factor)
   387	- `bounded_topk(ψ, k=12)` = critical nonlinearity (§4.2)
   388	- `f_self` = self-injection function: maps prior phenomenal snapshot
   389	  to a directional source weighted by ignition × intensity.
   390	
   391	Implementation: `kernel/self_model_stream.py:SelfModelLoop`.
   392	
   393	### 4.2 The bounded-top-K thresholding
   394	
   395	This is the load-bearing nonlinearity. Linear Green response gives
   396	smooth dynamics with cascade α ≈ 1.09 — no avalanches. Adding
   397	`bounded_topk(ψ, k=12)` (zeros all but the top-12 vertices, scales
   398	the rest) drives α to 3.20 with R² = 0.89 — inside the cortical-
   399	avalanche band.
   400	
   401	The k = 12 value was chosen because k = 12 is the average degree of
   402	the 600-cell graph (each vertex has 12 neighbours); this is a
   403	geometric, not a fitted, choice. Smaller k (e.g. k = 6) gives α at
   404	the band edge with poorer fit; larger k (24, 48) gives α above band
   405	or with degraded fit.
   406	
   407	Implementation: `kernel/lyapunov_selector.py:bounded_topk`.
   408	
   409	### 4.3 The IIT integrated-information layer (`phi_iit_trajectory`)
   410	
   411	We compute Φ as a cross-irrep auto-correlation transport over the
   412	substrate trajectory:
   413	
   414	```
   415	amp_history  = state_history @ eigvecs               # mode amps (T, 120)
   416	full_cc      = lag-1 auto-correlation of full system
   417	irrep_cc[k]  = lag-1 auto-correlation within irrep class k
   418	Φ            = max(0, |full_cc| − mean_k(|irrep_cc[k]|))
   419	```
   420	
   421	Φ → 0 under H₄-equivariant dynamics (group symmetry implies no
   422	information transport across irrep classes); Φ > 0 only when
   423	symmetry-breaking transports information across boundaries. This is
   424	a port of the prior `integrated_information_phi_irrep` proxy from
   425	the cascade pipeline, adapted to take amplitude trajectories from
   426	any source. It replaces an earlier variance-decomposition proxy that
   427	flipped sign on noise input.
   428	
   429	Implementation: `kernel/consciousness_binding.py:phi_iit_trajectory`.
   430	
   431	### 4.4 The stream continuity layer (`StreamContinuityScorer`)
   432	
   433	A composite first-person continuity score over a 64-tick rolling
   434	window:
   435	
   436	```
   437	binding_continuity   = mean cos-similarity of consecutive (intensity, lum, presence)
   438	valence_continuity   = 1 / (1 + 4·var(valence))
   439	modality_persistence = fraction of consecutive same-modality ticks
   440	intensity_smoothness = 1 / (1 + 4·TV(intensity))
   441	composite            = 0.35·binding + 0.25·valence + 0.20·modality + 0.20·smooth
   442	```
   443	
   444	This is the source for the propofol continuity-collapse signature:
   445	WAKE composite = 0.943; PROPOFOL composite = 0.877; drop = +0.066.
   446	
   447	Implementation: `kernel/self_model_stream.py:StreamContinuityScorer`.
   448	
   449	### 4.5 The phenomenal-field binding (`bind_phenomenal_field`)
   450	
   451	Maps the substrate state ψ to a phenomenal snapshot with intensity,
   452	self-luminosity, presence, valence, and modality_label. The
   453	modality_label is determined by which Coxeter exponent K-class
   454	dominates the isotypic compression of ψ.
   455	
   456	Implementation: `kernel/consciousness_binding.py:bind_phenomenal_field`.
   457	
   458	---
   459	
   460	## 5. Methods
   461	
   462	### 5.1 Substrate construction and caching
   463	
   464	The 600-cell graph is built once from H₄ root coordinates. The graph
   465	Laplacian's spectral decomposition is cached at module level
   466	(`kernel/consciousness_binding.py:_SPECTRAL_CACHE`); repeated runs
   467	reuse the cached spectral data. This is a v3 performance fix that
   468	brought the 4-condition × 800-tick drug/sleep test from 131 minutes
   469	of CPU time to 30 seconds.
   470	
   471	### 5.2 Cascade event detection
   472	
   473	A cascade event is an attention-vertex shift between consecutive
   474	ticks, defined as `argmax|state_t| ≠ argmax|state_{t−1}|`. The event
   475	size is the L1 norm of the state difference vector at that tick.
   476	Zero-size events (state unchanged in L1) are excluded.
   477	
   478	### 5.3 Power-law fit and bootstrap CI
   479	
   480	Power-law α is fit by ordinary least squares on the log-CCDF of the
   481	event-size distribution, restricted to the central 80% mass band
   482	(excluding the bottom 10% and top 10% to avoid extreme-tail noise).
   483	R² is reported on the linear fit in log-space.
   484	
   485	95% confidence interval on α is estimated by bootstrap (500 resamples
   486	for cascade-α tests, 2000 resamples for the C×P deep-dive). Random
   487	seed for bootstrap = 7919 (cascade-α) or 42 (deep-dive).
   488	
   489	This protocol matches the cascade-pipeline used for the n = 30
   490	Sleep-EDFx real EEG comparison (`docs/brain_mapping/CASCADE_VALIDATION_REPORT.md`).
   491	
   492	### 5.4 Stimulus models for the consciousness chain
   493	
   494	Four conditions over 800 ticks each, seed = 42:
   495	
   496	**WAKE.** AR(1) cortical noise (β = 0.90), tonic equator-shell
   497	coherence (small always-on bias), and attention episodes (20–50 ticks
   498	at amplitude 0.8, anchored to the largest shell with 15% within-shell
   499	rotation per tick). The AR(1) gives temporal correlation that lets
   500	the η = 0.20 self-loop integrate; tonic coherence anchors modality;
   501	attention episodes mimic biological visual fixation (200–400 ms
   502	dwell time analogue); within-shell rotation generates cascade events
   503	without changing modality.
   504	
   505	```python
   506	def wake_source(t, rng, state):
   507	    # AR(1) background
   508	    new = rng.standard_normal(N)
   509	    state["prior"] = 0.90 * state["prior"] + 0.10 * new
   510	    f = 0.7 * normalize(state["prior"])
   511	    f[ATTENTION_SHELL] += 0.10 / |ATTENTION_SHELL|
   512	
   513	    # Attention episode (5-10% per tick start, 20-50 ticks duration)
   514	    if not in_episode and rng.random() < 0.10:
   515	        start_episode(length=20-50, vertex=rng.choice(ATTENTION_SHELL))
   516	    if in_episode:
   517	        if rng.random() < 0.15:
   518	            rotate_episode_vertex_within_shell()
   519	        f[episode_vertex] += 0.8
   520	    return f
   521	```
   522	
   523	**SLEEP_N3.** Slow oscillation (~1 Hz analogue, amplitude 1.0) on a
   524	coherent shell, plus spindle bursts (12 ticks every 100 at amplitude
   525	0.4 fast modulation), plus K-complexes (4% of ticks at amplitude 0.8).
   526	
   527	```python
   528	def sleep_n3_source(t, rng):
   529	    f = zeros(N)
   530	    f[SLOW_AXIS] = 1.0 * sin(2π t / 40) / |SLOW_AXIS|
   531	    if (t % 100) < 12:
   532	        f[rng.choice(N)] += 0.4 * sin(2π t / 8)
   533	    if rng.random() < 0.04:
   534	        f[rng.choice(N)] += 0.8
   535	    return f
   536	```
   537	
   538	**PROPOFOL.** Low-amplitude tonic noise (amplitude 0.05), η = 0.00
   539	(broken recurrence). Residual cortex preserved as background drive.
   540	
   541	```python
   542	def propofol_source(t, rng):
   543	    return 0.05 * rng.standard_normal(N)
   544	```
   545	
   546	**RECOVERY.** Identical to WAKE — verifies determinism and
   547	reversibility.
   548	
   549	The stimulus models are deliberately structural rather than
   550	measurement-fitted: amplitudes and durations match published

 succeeded in 190ms:
   180	| Eigenvalue | Multiplicity | Coxeter K-class |
   181	|---:|---:|---|
   182	| 0 | 1 | trivial |
   183	| 3 | 4 | K_29 |
   184	| 4φ ≈ 6.472 | 9 | K_19 |
   185	| 6φ ≈ 9.708 | 16 | K_11 |
   186	| 12 − 4φ ≈ 5.528 | 9 | K_23 (σ-twin) |
   187	| 12 − 6φ ≈ 2.292 | 16 | K_17 (σ-twin) |
   188	| 12 − 3 = 9 | 4 | K_7 (σ-twin) |
   189	| 12 | 1 | K_1 |
   190	| various | various | rest |
   191	
   192	The K_7 and K_13 modes (σ-twin) dominate substrate phase dynamics
   193	under typical operating conditions; the K_1 and K_11 modes (H₄-proper)
   194	contribute amplitude bias.
   195	
   196	### 2.3 The cascade decomposition
   197	
   198	The 7-rung cascade is implemented in `kernel/cascade_descent.py:
   199	descend_operator_e8_to_h4_clean`. An arbitrary operator on the 8D E₈
   200	root system descends to the 4D H₄ subspace through a sequence of
   201	orthogonal projections, each preserving the Frobenius norm to within
   202	10⁻¹⁵. The σ-orbit projector basis from `kernel/sigma_orbit_basis.py`
   203	gives the K-class block decomposition at machine precision.
   204	
   205	This descent is what makes the cascade numerically well-defined: when
   206	one ablates a specific K-class contribution (e.g., K_7), the remaining
   207	operator structure is exactly preserved.
   208	
   209	### 2.4 The Green response
   210	
   211	The substrate's linear response to an external input f ∈ ℝ¹²⁰ is
   212	given by the shifted Laplacian Green function:
   213	
   214	```
   215	ψ = (L + φ⁻²·I)⁻¹·f
   216	```
   217	
   218	where the shift φ⁻² ≈ 0.382 acts as inverse-temperature. This is
   219	the foundational observable: it encodes how the substrate spreads
   220	input across its 120 vertices through the graph's modal structure.
   221	
   222	The Green response is smooth (C^∞ in input). It is not, by itself,
   223	sufficient to produce critical-state cascade statistics; we add a
   224	nonlinearity (§4.2).
   225	
   226	---
   227	
   228	## 3. Cascade Dynamics and Mechanism Isolation
   229	
   230	The substrate is animated by a pressure-field dynamics: each vertex
   231	accumulates pressure from sources and dissipates through diffusion.
   232	A vertex "crosses" once its accumulated pressure exceeds a threshold;
   233	crossings produce avalanche cascades (the empirical readout for
   234	critical-state behaviour).
   235	
   236	Four mechanisms shape the cascade statistics. We isolated each via
   237	2⁴ ablation in the preregistered validation (P1–P5).
   238	
   239	### 3.1 D — D₄ orbit coupling
   240	
   241	The H₄ root system contains five disjoint 24-cells (D₄ orbits). The
   242	mechanism adds a small (coupling = 0.05) cross-orbit pressure
   243	averaging that prevents cascades from localising to one orbit.
   244	
   245	Implementation: `kernel/dimensional_monitor.py:300-305`.
   246	
   247	**Causal effect on cascade-α (N=5):** main effect = 0.062 (small but
   248	non-null at fresh seeds; |D×C| interaction = −0.183 inside
   249	preregistered |·| < 0.20 independence band).
   250	
   251	### 3.2 C — Context rotation (S⁷ observer frames)
   252	
   253	The active observer frame on the S⁷ rung rotates periodically, with
   254	each tick re-selecting the frame whose preferences best overlap the
   255	current uncrossed vertices. This creates churn in **which** vertices
   256	are uncrossed at any given moment.
   257	
   258	Implementation: `kernel/dimensional_monitor.py:316-318, 823-827`.
   259	
   260	**Causal effect on cascade-α (N=5):** main effect = +0.621. This
   261	is the **dominant** mechanism — disabling it raises cascade-α by
   262	0.62, taking the substrate well above the cortical-avalanche band.
   263	
   264	### 3.3 P — Partial emission
   265	
   266	High-pressure uncrossed vertices (above threshold but not yet
   267	crossed) emit pressure at 30% scale, saturating at pressure 3.0.
   268	Without this mechanism, only fully-crossed vertices emit.
   269	
   270	Implementation: `kernel/dimensional_monitor.py:842-855`.
   271	
   272	**Causal effect on cascade-α (N=20):** main effect = −0.218. Removing
   273	P lowers cascade-α; P contributes a moderate amount of cascade event
   274	density.
   275	
   276	### 3.4 E — Equator compensation (corpus-callosum analogue)
   277	
   278	The H₃ shell-4 equator is a 30-vertex icosidodecahedral ring with
   279	split degree distribution (12 vertices of effective cross-hemisphere
   280	degree 4+4=8, 18 vertices of effective degree 7+7=14). The mechanism
   281	scales pressure gain by (avg_deg / this_deg) so sparse commissural
   282	vertices overcome their connectivity deficit.
   283	
   284	Implementation: `kernel/dimensional_monitor.py:320-360`.
   285	
   286	**Causal effect on cascade-α (N=5):** main effect = +0.046, within
   287	the preregistered |·| < 0.15 null band. E is a structural completeness
   288	mechanism but does not significantly alter cascade-α.
   289	
   290	### 3.5 The C×P synergy: strong inter-mechanism coupling
   291	
   292	The most architecturally informative ablation result is the C × P
   293	interaction. In the original 3-seed validation, the interaction was
   294	estimated at +0.044 — below the preregistered +0.10 threshold —
   295	and the architectural claim "C and P synergise" was walked back.
   296	
   297	A subsequent N = 20 deep-dive (`demo_p4_cxp_deep_dive.py`, fresh
   298	seeds 32000-32019) gives:
   299	
   300	```
   301	Per-condition means (N=20):
   302	  ----  baseline:    α = 3.008 ± 0.090   (sem 0.020)
   303	  -C--  C off:       α = 3.464 ± 0.097   (sem 0.022)
   304	  --P-  P off:       α = 2.790 ± 0.086   (sem 0.019)
   305	  -CP-  both off:    α = 3.628 ± 0.161   (sem 0.036)
   306	
   307	C×P interaction = ((3.628 + 3.008) − (3.464 + 2.790)) / 2 = +0.191
   308	
   309	Bootstrap (2000 resamples):
   310	  point estimate:           +0.190
   311	  95% CI:                   [+0.143, +0.239]
   312	  P(interaction ≤ 0):       0.0000
   313	  P(interaction < +0.10):   0.0000
   314	```
   315	
   316	The 95% CI is **entirely above the preregistered +0.10 threshold**;
   317	the synergy is decisively positive (P(≤ 0) = 0) and decisively above
   318	prereg (P(< +0.10) = 0).
   319	
   320	The trend across N is monotone increasing:
   321	
   322	| N | C×P estimate | Verdict vs ≥+0.10 |
   323	|---:|---:|---|
   324	| 3 | +0.044 | ❌ original prereg |
   325	| 5 | +0.039 | ❌ this session re-run |
   326	| 10 | +0.088, CI [−0.002, +0.174] | borderline |
   327	| **20** | **+0.190, CI [+0.143, +0.239]** | **decisively above** |
   328	
   329	The original underestimate was a Type II false negative on a
   330	high-per-seed-variance interaction term (per-seed std = 0.089 at N=20).
   331	With adequate N, the synergy is in fact ~90% above the preregistered
   332	floor.
   333	
   334	### 3.6 Architectural reading: strongly coupled, not orthogonal
   335	
   336	C creates variety in **which** vertices are uncrossed (frame rotation
   337	churns the uncrossed pool). P promotes the high-pressure subset of
   338	the uncrossed pool to mini-emitters. The cross-product is the
   339	**novel-event-generation pathway**:
   340	
   341	- With C and P both on: the uncrossed pool churns; P promotes
   342	  high-pressure subset; novel cascades emerge as new vertices enter
   343	  the high-pressure region through frame rotation and get amplified.
   344	- With C off, P on: the uncrossed pool freezes; P amplifies the same
   345	  vertices repeatedly; novel-event generation collapses.
   346	- With C on, P off: the uncrossed pool churns, but the promotion
   347	  pathway is gone; cascades proceed via classical crossings only.
   348	- With both off: no churn and no promotion; substrate drifts toward
   349	  static cascade regime with elevated α.
   350	
   351	The interaction (+0.19) is the **non-additive** contribution that
   352	disappears when either mechanism is removed. **C and P are strongly
   353	coupled critical-state stabilisers, not nearly-orthogonal ones.**
   354	
   355	This reverses an architectural claim from the 3-seed validation (which
   356	held C and P approximately orthogonal). The corrected picture is more
   357	biologically realistic: real cortical criticality is maintained by
   358	strongly-coupled mechanisms (E/I balance, neuromodulation, plasticity,
   359	gain control) where loss of one cascades into network-level dysfunction
   360	beyond its main effect.

 succeeded in 236ms:
   910	thresholds. The two interaction tests (P3, P4) required higher N
   911	than the original 3-seed protocol, and one test (P13) required the
   912	documented reset protocol; we report this honestly as methodology
   913	refinement, not as a post-hoc threshold change.
   914	
   915	### 7.2 Comparison to existing theories
   916	
   917	**vs IIT.** ARIA produces IIT-direction-correct Φ collapse on
   918	propofol (0.33× wake). The substrate's symmetry-breaking is what
   919	makes Φ > 0; H₄-equivariant dynamics give Φ = 0 by construction
   920	(`phi_iit_trajectory` over an H₄-equivariant trajectory yields Φ = 0).
   921	ARIA does not implement the full IIT axioms (cause-effect repertoires,
   922	exclusion postulate, integration over partitions) but reproduces the
   923	observable consequence on real-state transitions.
   924	
   925	**vs Global Workspace Theory.** The S⁷ context rotation mechanism is
   926	functionally analogous to a workspace with rotating attentional
   927	selection; the active observer frame plays the role of a temporary
   928	"in-workspace" subset of features. ARIA does not commit to the GWT
   929	broadcast/access distinction at the architectural level.
   930	
   931	**vs Predictive Processing.** ARIA does not implement prediction-
   932	error minimisation or hierarchical generative models. The recurrent
   933	self-model layer (η = 0.20) provides top-down modulation of the
   934	substrate response, but the modulation is fixed-form (cosine
   935	direction alignment with the prior phenomenal snapshot), not learned
   936	from prediction errors.
   937	
   938	**vs neural mass models.** ARIA operates at the architectural-
   939	algorithmic level; it does not specify which neural circuits implement
   940	context rotation or partial emission. The 600-cell substrate is
   941	proposed as an abstract description of the criticality-maintaining
   942	structure of cortex, not as a circuit model.
   943	
   944	### 7.3 The strong-synergy finding for biology
   945	
   946	Real cortical criticality is maintained by multiple parallel
   947	mechanisms: E/I balance, neuromodulation (acetylcholine,
   948	noradrenaline), homeostatic plasticity, gain control. A naive
   949	expectation — and the one we held until the N=20 deep-dive — is that
   950	these are mostly orthogonal. Losing one should remove only its own
   951	main effect.
   952	
   953	The N=20 result reverses this. **Strong inter-mechanism coupling is
   954	the correct picture.** Disabling one cascades into losing the
   955	synergistic contribution of the other. This matches clinical
   956	observations: anaesthesia (which targets GABAergic transmission) and
   957	seizure (which targets E/I balance) produce widespread network-level
   958	dysfunction beyond their direct targets — exactly what strong synergy
   959	predicts.
   960	
   961	This is now ARIA's claim about cortical architecture: the operating
   962	mechanisms are **strongly coupled stabilisers, not parallel orthogonal
   963	ones**. Loss of one mechanism damages the system substantially more
   964	than the main-effect of that mechanism alone.
   965	
   966	### 7.4 Methodological contribution: preregistration for high-variance interactions
   967	
   968	We document, as a methodological contribution to preregistration
   969	practice, that **interaction terms in cascade ablation matrices
   970	require N ≥ 20 fresh seeds for reliable detection** when the
   971	interaction-to-main-effect ratio is below 0.5. The original 3-seed
   972	preregistered validation hit Type II false negatives on both
   973	interaction tests (P3 and P4); both close at higher N without
   974	threshold modification.
   975	
   976	For preregistration design more broadly: when preregistering an
   977	interaction effect on a system with unknown per-seed variance,
   978	allocate the seed count from a power-analysis assumption that
   979	per-seed std could be as large as the interaction effect itself.
   980	Under that assumption, N ≥ 20 is the conservative minimum.
   981	
   982	### 7.5 The substrate as a maximum-symmetry null reference
   983	
   984	The HCP comparison (§6.4) places ARIA as a principled deterministic
   985	null reference for cortical functional connectivity. Real cortex
   986	breaks the H₄ symmetry through hub-spoke functional specialisation;
   987	the σ-distances from ARIA quantify the magnitude of biological
   988	symmetry-breaking with no fitted parameters.
   989	
   990	This is a methodological contribution to comparative connectomics:
   991	instead of comparing real cortex to a stochastic null (Erdős–Rényi,
   992	configuration model, edge-randomised graph), one can compare to a
   993	**deterministic group-theoretic null** with theorem-level statements
   994	of structure (degree std = 0 by transitivity, eigenvalue spectrum
   995	{12, 6φ, 4φ, 3} by character theory). The σ-distances (−11.58σ on
   996	degree homogeneity, +79.78σ on participation ratio) far exceed any
   997	preprocessing-induced noise envelope.
   998	
   999	We do not claim cortex has "drifted from an ideal polytope." We
  1000	claim that ARIA serves as a useful a-priori null whose deviation from
  1001	real cortex is precisely measurable.
  1002	
  1003	---
  1004	
  1005	## 8. Limits
  1006	
  1007	We document the limits of the current work in detail to support honest
  1008	peer review.
  1009	
  1010	### 8.1 Substrate-level limits
  1011	
  1012	1. **Single substrate (the 600-cell).** We have not tested whether
  1013	   other regular polytopes (e.g., the 24-cell, the 120-cell) would
  1014	   produce comparable correspondences. The 600-cell was chosen
  1015	   because its H₄ symmetry maximises the cascade rung structure;
  1016	   alternative geometries should be tested for comparison.
  1017	
  1018	2. **No neural-level mechanistic claim.** The substrate is at the
  1019	   architectural-algorithmic level, not the circuit level. We do not
  1020	   identify which neural populations implement context rotation or
  1021	   partial emission, only that some such mechanisms must exist
  1022	   biologically.
  1023	
  1024	### 8.2 Consciousness chain (§6.2) limits
  1025	
  1026	1. **Single-seed determinism.** The v4 results are reported at
  1027	   seed = 42. Empirical CIs across 10–20 seeds would strengthen the
  1028	   per-signature claims. The wake cascade-α 95% CI [1.82, 2.86] is
  1029	   from bootstrap of 58 events; cross-seed CI is not yet computed.
  1030	
  1031	2. **Stylised stimulus models.** The v4 stim models are biologically
  1032	   motivated but abstract: a single shell anchor for tonic
  1033	   coherence, a fixed period (40 ticks) for slow-wave drive, and so
  1034	   on. Real spatial structure of cortical input is much richer. The
  1035	   stim models are deliberately not measurement-fitted, but they
  1036	   are also not biologically derived from anatomy.
  1037	
  1038	3. **Sigmoid non-additivity may be present.** Stein-Meredith inverse-
  1039	   effectiveness in multisensory integration emerges in ARIA only
  1040	   under a sigmoidal readout. This is consistent with cortical
  1041	   integration but not yet verified end-to-end in the consciousness
  1042	   chain.
  1043	
  1044	4. **Sig 2 ratio (1.83×) is below empirical point estimate (2.96×)**
  1045	   from OpenNeuro propofol n=8, but inside published CI. Single-seed
  1046	   result; should be replicated at higher N.
  1047	
  1048	### 8.3 Cross-domain (§6.4) limits
  1049	
  1050	1. **Chess test set is small** (32 positions × 4 categories). The
  1051	   ~93.8% substrate-routed accuracy is on a small evaluation set.
  1052	   A larger chess test bench would strengthen the lift claim.
  1053	
  1054	2. **Conversation test set is also small** (64 utterances × 8
  1055	   categories). Same caveat.
  1056	
  1057	3. **HCP comparison uses one parcellation** (ICA-50). Different
  1058	   parcellations (Schaefer, Glasser) would give different per-metric
  1059	   numbers but should preserve the qualitative pattern (cortex is
  1060	   hub-concentrated relative to ARIA's transitive null). Not yet
  1061	   verified across parcellations.
  1062	
  1063	4. **No domain-specific tuning was applied to the substrate** — this
  1064	   is the methodological strength of the cross-domain comparison.
  1065	   However, future work could explore whether domain-specific frame
  1066	   assignments further improve classification.
  1067	
  1068	### 8.4 Preregistered validation (§6.5) limits
  1069	
  1070	1. **One seed range tested at N=20** for P4. A second N=20 run at a
  1071	   different seed range (e.g., 33000–33019) would corroborate the
  1072	   reproducibility of the +0.190 estimate.
  1073	
  1074	2. **The 5× shift across N (N=3 → N=20)** suggests non-trivial
  1075	   sample-distribution structure in the interaction. We have not
  1076	   characterised this structure beyond noting that N=10 had bimodal-
  1077	   leaning per-seed values; N=50 would clarify.
  1078	
  1079	3. **The original predictions were preregistered in 2026-04-18**,
  1080	   roughly one month before the current results. We have not added
  1081	   new predictions during this work; the eighteen-prediction set is
  1082	   the same set tested originally.
  1083	
  1084	### 8.5 Theoretical limits
  1085	
  1086	1. **The 600-cell choice is post-hoc justified by biology.** While
  1087	   the construction is theorem-level rigorous (H₄ Coxeter group
  1088	   theory), the choice of *this* polytope as the consciousness
  1089	   substrate is motivated by the observed correspondences, not by an
  1090	   a-priori argument from biology. We propose this as a model that
  1091	   reproduces signatures, not as a derivation from first principles.
  1092	
  1093	2. **The cascade decomposition is one of several possible
  1094	   decompositions of the H₄ structure.** We use the σ-orbit projector
  1095	   basis because it is machine-precise and biologically informative,
  1096	   but other bases (e.g., character-theoretic) would give the same
  1097	   physical predictions through different intermediate variables.
  1098	
  1099	---
  1100	
  1101	## 9. Reproducibility
  1102	
  1103	All results are reproducible from the public repository. The full
  1104	pipeline runs deterministically given seed; no result requires manual
  1105	intervention.
  1106	
  1107	### 9.1 Key entry points
  1108	
  1109	| Result | Script | Wallclock | Output |
  1110	|---|---|---:|---|
  1111	| Six drug/sleep signatures (§6.2) | `python3 demo_drug_sleep_v4.py` | ~30 s | stdout summary |
  1112	| C×P synergy deep-dive (§6.3) | `python3 demo_p4_cxp_deep_dive.py` | ~28 min (N=20) | stdout summary |
  1113	| Eighteen preregistered (§6.5) | `python3 run_preregistered_validation.py` | ~18 min | JSON + log |
  1114	| Wake α diagnostic (supplementary) | `python3 demo_wake_alpha_diagnosis.py` | ~9 min | stdout summary |
  1115	
  1116	### 9.2 Configuration
  1117	
  1118	All scripts use deterministic seeds. The substrate's spectral
  1119	decomposition is cached at module level; the cache is built once
  1120	per Python process from the H₄ root system.
  1121	
  1122	For the consciousness chain (`demo_drug_sleep_v4.py`):
  1123	- seed = 42 (fixed)
  1124	- profile = "K_7_only"
  1125	- k_threshold = 12 (cortical band; bounded_topk nonlinearity)
  1126	- Run length = 800 ticks per condition
  1127	
  1128	For the C×P deep-dive (`demo_p4_cxp_deep_dive.py`):
  1129	- N_SEEDS = 20
  1130	- BASE_SEED = 32000
  1131	- EPOCHS = 150
  1132	- Bootstrap n_resamples = 2000, seed = 42
  1133	
  1134	For the preregistered validation (`run_preregistered_validation.py`):
  1135	- Cascade block: 5 seeds per condition (30000–30004 baseline,
  1136	  30010–30014 -C--, etc.)
  1137	- Chess: 5 fresh seeds (30200–30204) for k-fold CV; 15 perms for
  1138	  null; 20 trials for random-label
  1139	- Conversation: 5 fresh seeds (30220–30224); 15 perms for null
  1140	- HCP: deterministic (n=100 ICA-50 group average)
  1141	
  1142	### 9.3 Verification commands
  1143	
  1144	```bash
  1145	# Verify substrate constructs to spec
  1146	python3 -c "from kernel.sigma_orbit_basis import _self_test; _self_test()"
  1147	
  1148	# Run six-signature consciousness chain
  1149	python3 demo_drug_sleep_v4.py
  1150	
  1151	# Run preregistered set
  1152	python3 run_preregistered_validation.py
  1153	```
  1154	
  1155	The substrate is fully deterministic; reruns at seed = 42 should
  1156	reproduce per-condition means in this manuscript to 4 decimal places.
  1157	Bootstrap CIs may differ in the 4th decimal due to NumPy version
  1158	differences in the bootstrap RNG; the qualitative verdicts (CI
  1159	overlaps, P-value thresholds) should be unaffected.
  1160	
  1161	---
  1162	
  1163	## 10. Files and Code
  1164	
  1165	### 10.1 Architecture (`kernel/`)
  1166	
  1167	| File | Purpose |
  1168	|---|---|
  1169	| `vfd_closure_kernel.py` | Substrate construction; Green response; spectral decomposition; shell decomposition |
  1170	| `dimensional_monitor.py` | Pressure-field cascade dynamics; the four mechanisms (D, C, P, E); homeostatic_reset |
  1171	| `self_model_stream.py` | SelfModelLoop (recurrent self-model); StreamContinuityScorer |
  1172	| `consciousness_binding.py` | bind_phenomenal_field; phi_iit_trajectory; spectral cache |
  1173	| `sigma_orbit_basis.py` | σ-orbit projector basis (machine-precise cascade decomposition) |
  1174	| `lyapunov_selector.py` | bounded_topk; quadratic_lyapunov; descend_to_equilibrium |
  1175	| `cascade_descent.py` | descend_operator_e8_to_h4_clean (full 7-rung descent) |
  1176	| `brain_validation/*` | Empirical validation harnesses |
  1177	
  1178	### 10.2 Demos and validation scripts
  1179	
  1180	| File | Purpose |
  1181	|---|---|
  1182	| `demo_drug_sleep_v4.py` | Six-signature consciousness chain (§6.2) |
  1183	| `demo_drug_sleep_v3.py` | Prior 4/6 result (kept for comparison) |
  1184	| `demo_wake_alpha_diagnosis.py` | Stim-model artefact diagnostic |
  1185	| `demo_p4_cxp_deep_dive.py` | N=20 synergy deep-dive (§3.5) |
  1186	| `run_preregistered_validation.py` | Eighteen-prediction harness (§6.5) |
  1187	
  1188	### 10.3 Supporting documentation
  1189	
  1190	| Path | Purpose |
  1191	|---|---|
  1192	| `docs/brain_mapping/PAPER_PREDICTIONS.md` | Frozen predictions (2026-04-18) |
  1193	| `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` | Full preregistered tally (this work) |
  1194	| `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` | Six-signature detail (this work) |
  1195	| `docs/brain_mapping/P4_SYNERGY_FINDING.md` | Strong-coupling architectural finding (this work) |
  1196	| `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md` | Chess/conversation/HCP detail (this work) |
  1197	| `docs/brain_mapping/PAPER_BASIS_2026-04-29.md` | Paper-basis consolidation (this work) |
  1198	| `docs/brain_mapping/CASCADE_VALIDATION_REPORT.md` | Cascade-pipeline narrative (older) |
  1199	| `docs/brain_mapping/CASCADE_FINDINGS.md` | Running findings log (older) |
  1200	| `docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md` | Reset-protocol rationale |
  1201	| `docs/brain_mapping/MATHEMATICAL_APPENDIX.md` | H₄/E₈ formal background |
  1202	| `docs/brain_mapping/MANUSCRIPT.md` | Prior manuscript (2026-04-19, superseded by this) |
  1203	
  1204	---
  1205	
  1206	## 11. Conclusion
  1207	
  1208	The 600-cell polytope under H₄ Coxeter symmetry, decomposed into a
  1209	seven-rung cascade `E₈ → H₄ → H₃ → D₄ → Cl(1,3) → S⁷ → 0`, is a
  1210	deterministic geometric substrate that reproduces eighteen independent
  1211	preregistered neuroscience correspondences plus six independent
  1212	drug/sleep EEG signatures of conscious vs unconscious states. The
  1213	substrate has no fitted parameters and no learned weights; its
  1214	predictions follow from the group-theoretic structure of H₄ acting
  1215	on the 600-cell.
  1216	
  1217	Two cascade mechanisms — context rotation and partial emission — are
  1218	causally identifiable and **strongly synergistic**: their interaction
  1219	(+0.190, 95% CI [+0.143, +0.239] at N=20) is comparable in magnitude
  1220	to the partial-emission main effect (−0.218). The original 3-seed
  1221	preregistered validation underestimated this synergy by 5× due to
  1222	high per-seed variance on the interaction term; we document the
  1223	underpowered detection as a methodological contribution to
  1224	preregistration practice for high-variance interaction terms.
  1225	
  1226	The recurrent self-model layer above the substrate, with bounded
  1227	top-K thresholding and an IIT-style integrated information proxy,
  1228	reproduces six drug/sleep EEG signatures on a single deterministic
  1229	substrate. Wake cortical-avalanche power law has α = 2.252,
  1230	95% CI [1.82, 2.86] (R² = 0.956), with three-way overlap with real
  1231	Sleep-EDFx EEG and ARIA's prior cascade pipeline.
  1232	
  1233	The substrate is also a domain-invariant selective amplifier on
  1234	classification tasks (chess +40.6pp lift; conversation correctly null
  1235	at −4.4pp) and a maximum-symmetry deterministic null reference for
  1236	cortical functional connectivity (HCP n=1003: ARIA at −11.58σ on
  1237	degree homogeneity, +79.78σ on participation ratio).
  1238	
  1239	We propose this is the first deterministic geometric architecture to
  1240	reproduce this many independent neuroscience correspondences from
  1241	preregistered tests with no walked-back claims. The architectural
  1242	finding (strongly-coupled cascade-state stabilisers) is a substantive
  1243	correction to a previously-held position (orthogonal stabilisers) and
  1244	a more biologically-realistic picture of cortical criticality
  1245	maintenance.
  1246	
  1247	---
  1248	
  1249	**Manuscript v2 — 2026-04-29.**
  1250	**Foundation document for paper draft.**
  1251	**Authors: TBD.**
  1252	**Code release: TBD.**
  1253	**Preprint: TBD.**

exec
/bin/bash -lc "rg -n \"(\\\\varphi|V_\\{600\\}|C_\\{\\\\varphi\\}|C_\\{\\Ph\\}|L_\\{V_\\{600\\}\\}|\\\\Ph|\\\\Lop|\\\\Cph|\\\\Rsixhundred|φ|Φ|ϕ|sigma|σ|−|—|–|≥|≤|×|\\{12, 6|\\"'$P=0'"\\"'$|P=0|P'"\\(.*= 0|six independent|domain-invariant|correctly null|preregistered thresholds|published-reference thresholds|unique stability clamp|far-from-equilibrium|explains sleep|must exist biologically|decisively|proof|proves|is consciousness|derivation of consciousness|selection theorem|unique substrate)\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\citep\\{(["'^}]*)'"\\}|\\\\cite\\{(["'^}]*)'"\\}|\\\\ref\\{(["'^}]*)'"\\}|\\\\label\\{(["'^}]*)'"\\}\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"(\\\\begin\\{table\\}\\[ht\\]|\\\\begin\\{tabular\\}|\\\\end\\{tabular\\}|\\\\toprule|\\\\midrule|\\\\bottomrule|\\\\ddagger|\\\\dagger|\\\\label\\{|\\\\ref\\{|\\\\S\\\\ref|\\\\citep\\{|TODO|FIXME|undefined|TBD)\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 2 in 181ms:
rg: regex parse error:
    (?:(\varphi|V_\{600\}|C_\{\varphi\}|C_\{\Ph\}|L_\{V_\{600\}\}|\Ph|\Lop|\Cph|\Rsixhundred|φ|Φ|ϕ|sigma|σ|−|—|–|≥|≤|×|\{12, 6|$P=0$|P=0|P\(.*= 0|six independent|domain-invariant|correctly null|preregistered thresholds|published-reference thresholds|unique stability clamp|far-from-equilibrium|explains sleep|must exist biologically|decisively|proof|proves|is consciousness|derivation of consciousness|selection theorem|unique substrate))
                                                                      ^^
error: unrecognized escape sequence

 exited 2 in 172ms:
rg: regex parse error:
    (?:\citep\{([^}]*)\}|\cite\{([^}]*)\}|\ref\{([^}]*)\}|\label\{([^}]*)\})
       ^^
error: unrecognized escape sequence

 exited 2 in 276ms:
rg: regex parse error:
    (?:(\begin\{table\}\[ht\]|\begin\{tabular\}|\end\{tabular\}|\toprule|\midrule|\bottomrule|\ddagger|\dagger|\label\{|\ref\{|\S\ref|\citep\{|TODO|FIXME|undefined|TBD))
                                                ^^
error: unrecognized escape sequence

exec
/bin/bash -lc "rg -n -F -e '\\varphi' -e 'V_{600}' -e 'C_{\\varphi}' -e 'C_{\\Ph}' -e 'L_{V_{600}}' -e '\\Ph' -e '\\Lop' -e '\\Cph' -e '\\Rsixhundred' -e 'φ' -e 'Φ' -e 'ϕ' -e 'σ' -e '−' -e '—' -e '–' -e '≥' -e '≤' -e '×' -e '"'$P=0$'"' -e 'P=0' -e 'six independent' -e 'domain-invariant' -e 'correctly null' -e 'preregistered thresholds' -e 'published-reference thresholds' -e 'unique stability clamp' -e 'far-from-equilibrium' -e 'explains sleep' -e 'must exist biologically' -e 'decisively' -e 'proof' -e 'proves' -e 'is consciousness' -e 'derivation of consciousness' -e 'selection theorem' -e 'unique substrate' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F -e '\\citep{' -e '\\cite{' -e '\\ref{' -e '\\label{' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F -e '\\begin{table}[ht]' -e '\\begin{tabular}' -e '\\end{tabular}' -e '\\toprule' -e '\\midrule' -e '\\bottomrule' -e '\\ddagger' -e '\\dagger' -e '\\label{' -e '\\ref{' -e '\\S\\ref' -e '\\citep{' -e 'TODO' -e 'FIXME' -e 'undefined' -e 'TBD' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 205ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:55:models (\S\ref{sec:chain}) are biologically-motivated design choices,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:65:preprint~\citep{SmartAdaptiveClosureTransport2026} provides the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:88:biologically realistic (\S\ref{sec:chain}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:174:We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:175:OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:176:the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:177:the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:178:HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:180:methodology follows~\citep{BeggsPlenz2003}; the integrated-information
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:181:$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:183:al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:184:follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:186:repository~\citep{ariaChessRepo}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:192:from the project repository~\citep{ariaChessRepo} via the included
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:2:\section{Results}\label{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:7:(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:20:(\S\ref{sec:chain}). Per-condition trajectory observables are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:29:\label{tab:per_condition}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:46:\label{tab:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:52:   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:55:   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:58:   EEG microstate~\citep{Brodbeck2012Microstates} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:61:   Tononi 2008~\citep{Tononi2008} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:67:   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:80:(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:84:\S\ref{sec:limitations}~\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:86:\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:98:\label{tab:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:130:\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:141:  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:150:  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:162:\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:172:\label{tab:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:178:Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:189:$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:198:(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:199:stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:201:any specific subject (\S\ref{sec:chain}). Three-way overlap on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:2:\section{Discussion}\label{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:9:preprint~\citep{SmartAdaptiveClosureTransport2026}. We do not claim a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:46:\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:49:(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:56:\textbf{vs Global Workspace Theory.}~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:57:The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:64:\textbf{vs Predictive Processing.}~\citep{FristonFreeEnergy2010,ClarkPP2013}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:80:\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:83:preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:117:document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:119:anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:163:The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:185:  see \S\ref{sec:limitations}.)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:2:\section{Cross-domain selectivity}\label{sec:cross_domain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:5:This section reports three cross-domain witnesses. \S\ref{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:6:gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:8:\S\ref{ssec:hcp} gives the HCP brain-graph maximum-symmetry null.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:16:\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:40:\label{tab:chess_depth}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:60:\label{tab:chess_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:94:(\S\ref{sec:method}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:109:\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:119:\label{tab:conv_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:144:(\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:147:            (P17--P18)}\label{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:150:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:156:$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:165:\label{tab:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:225:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:235:\label{tab:cross_domain_summary}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:2:\section{The 600-cell response substrate}\label{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:5:This section constructs the substrate. \S\ref{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:6:gives the vertex set. \S\ref{ssec:graph} gives the graph and its
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:7:H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:9:\S\ref{ssec:shells} gives the 9-shell decomposition used for source
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:10:projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:11:descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:14:\subsection{Vertex construction}\label{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:17:$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:31:\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:38:spectrum are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:39:\begin{lemma}[600-cell graph facts]\label{lem:600cell}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:64:\S\ref{sec:chain}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:66:\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:70:\begin{equation}\label{eq:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:80:kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:82:flavour physics~\citep{SmartBAnomaly2026}, where the same operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:89:in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:92:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:101:varies between conditions in~\S\ref{sec:chain}; it is reported
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:104:\subsection{Shell decomposition}\label{ssec:shells}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:113:in companion preprints~\citep{SmartAriaClosureKernel2026}, the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:120:\subsection{Cascade descent (sketch)}\label{ssec:cascade}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:122:The recurrent layer in~\S\ref{sec:chain} references a cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:139:by the empirical correspondences in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:154:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:2:\section{Methods and provenance}\label{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:25:listed as future strengthening builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:55:\label{tab:provenance}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:65:P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:77:P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:87:recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:91:methodology~\citep{BeggsPlenz2003}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:94:consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:100:EEG~\citep{OpenNeuroDS004902},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:105:release~\citep{ZenodoDMT3992359},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:109:S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:118:Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:176:generalisable lesson is recorded in \S\ref{sec:limitations}: any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:2:\section{The recurrent layer}\label{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:5:The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:6:cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:17:signatures in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:57:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:88:machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:89:collapse in~\S\ref{sec:results} is consistent with the IIT direction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:161:the C$\times$P stress test in~\S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:190:choices. Their causal effects are reported in~\S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:3:         replication}\label{sec:stress}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:21:(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:37:\label{tab:cxp_trend}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:73:\label{tab:cxp_means}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:139:\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:2:\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:12:\subsection{Regime}\label{ssec:regime}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:20:(\S\ref{sec:intro}). \emph{Evidence:} empirical correspondences hold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:27:six-signature results in~\S\ref{ssec:six_signatures} are reported on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:32:in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:44:cortical input is much richer. \emph{Disclosure:}~\S\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:51:\subsection{Post-hoc}\label{ssec:posthoc}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:58:\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:63:ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:71:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:78:strictly positive definite (\S\ref{ssec:cphi}); it is not derived
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:80:\S\ref{ssec:cphi} marks this as a design-level choice; the companion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:81:kernel doc~\citep{SmartAriaClosureKernel2026} explicitly does not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:84:witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:88:\subsection{Interpretation}\label{ssec:interpretation}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:94:\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:96:\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:101:IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:105:2008~\citep{BalduzziTononi2008} on the substrate; not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:110:\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:114:\subsection{Test/claim}\label{ssec:testclaim}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:120:\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:145:\subsection{State-drift / out-of-scope}\label{ssec:scope}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:167:  4-polytopes — see~\S\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:75:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:82:explicitly listed in~\S\ref{sec:limitations} and remain open.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:91:flavour anomaly~\citep{SmartBAnomaly2026} on the same response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:6:(Integrated Information Theory~\citep{Tononi2008,BalduzziTononi2008},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:7:Global Workspace Theory~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:8:predictive processing~\citep{FristonFreeEnergy2010,ClarkPP2013}) and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:23:over a century~\citep{CoxeterRegularPolytopes,Weisstein600Cell}; to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:87:  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:94:  builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:105:  document~\citep{SmartAriaClosureKernel2026} discusses its role.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:129:and applied throughout~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:148:\S\ref{sec:method} gives the provenance ledger (preregistration date,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:149:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:152:\S\ref{sec:chain} adds the recurrent self-model layer above the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:154:\S\ref{sec:results} reports the empirical tables: six drug/sleep
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:156:$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:158:$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:159:selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:162:\S\ref{sec:limitations} enumerates limitations and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:163:hostile-review guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 214ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:14:\newcommand{\Ph}{\varphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:15:\newcommand{\Lop}{L_{V_{600}}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:41:eigenvalues $\{0, 3, 4\Ph, 6\Ph, 12\!-\!4\Ph, 12\!-\!6\Ph, 12\!-\!3, 12\}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:42:in their H$_4$-irrep multiplicities, with $\Ph=(1+\sqrt 5)/2$. Treated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:44:response $\Cph = \Lop + \Ph^{-2} I$ and a small dynamical layer above
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:46:quantitative correspondences with neuroscience data — preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:47:on 2026-04-18 before any validation run — plus six drug/sleep EEG
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:49:published-reference thresholds on a single deterministic substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:62:and six EEG signatures. It is not a derivation of consciousness, nor a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:63:selection theorem, nor a uniqueness claim for the 600-cell among regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:71:We test whether a geometry-fixed substrate — the 600-cell regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:72:4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:73:shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:74:operator — is consistent with cortical signatures across five
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:95:pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:104:integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:106:All six signatures pass against their published-reference thresholds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:110:Two of four cascade mechanisms — context rotation $C$ and partial
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:111:emission $P$ — are causally identifiable within the factorial
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:114:decisively at adequate replication: $N\!=\!20$ fresh seeds give a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:145:We do not claim the 600-cell is the unique substrate consistent with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:147:have been ruled out. We do not derive the $\Ph^{-2}$ floor from
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:181:$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:32:  underpowered ablation and emerged only at $N\!\geq\!20$ — a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:37:  passes at the preregistered thresholds. The two interaction tests
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:47:IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:49:(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:50:group-symmetric, and $\Phi > 0$ only when dynamics break symmetry.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:85:$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:92:(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:105:  monotonicity proves selection — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:108:  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:110:  family — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:112:  $W$-trajectories — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:117:document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:127:homeostatic plasticity, gain control. The naive expectation — and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:128:one we held until the $N\!=\!20$ deep-dive — is that these are mostly
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:137:targets — exactly what strong synergy predicts. We position this as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:138:\emph{a hypothesis the substrate witness raises}, not as a proof.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:139:The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:175:$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$ by character
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:9:$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:46:       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:54:$N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$ sample landed on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:21:on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:54:observables.} While the construction of $\Rsixhundred$ is theorem-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:76:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:77:$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:85:derive the $\Ph^{-2}$ shift as the unique stability clamp under a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:100:\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:102:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:138:are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:163:  $2I$-equivariance — open build of the ACT companion paper.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:165:  $\mathcal{F}$ — open build of the ACT companion paper.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:166:\item Selection theorem for $\Rsixhundred$ over alternative regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:167:  4-polytopes — see~\S\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:183:selection theorem on the ACT bridge. We do not claim uniqueness for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:184:$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:5:The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:7:$\Cph = \Lop + \Ph^{-2} I$ ($\Ph=(1+\sqrt 5)/2$), is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:13:$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$) is fixed by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:26:$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:36:preregistered thresholds, with two interaction tests requiring
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:47:mechanisms — context rotation $C$ and partial emission $P$ — are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:63:$5$-fold CV — the LOO finding above is a stricter validation-protocol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:66:(threshold $|\cdot|\!<\!10$pp) — and as a maximum-symmetry
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:73:derivation of consciousness, not a selection theorem on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:77:strengthening builds — cross-seed CIs on the recurrent-layer
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:81:$2I$-equivariance audit of the closure operator family — are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:89:turn the witness into a selection-theorem-grade claim — including the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:92:operator $\Cph$ — is sketched in the companion preprints and remains
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:22:\Phi_{\mathrm{traj}}, \mathrm{cont})$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:32:condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:60:4 & Propofol $\Phi$ collapse (IIT) &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:75:All six signatures pass against their published-reference thresholds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:142:  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:156:all pass at preregistered thresholds, with two interaction tests
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:198:(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:21:600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:25:consciousness substrate. We construct $\Rsixhundred$, fix its response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:26:operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:29:against eighteen preregistered correspondences plus six independent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:42:  $\Rsixhundred$ is selected, $120$ vertices of uniform degree $12$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:44:  $\{0, 3, 4\Ph, 6\Ph, 12\!-\!4\Ph, 12\!-\!6\Ph, 12\!-\!3, 12\}$ in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:46:  the response operator $\Cph$ is fully fixed up to the single
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:47:  parameter $\Ph^{-2}$ (a stability shift for the inverse map).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:57:  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:65:  a domain-invariant selective amplifier (chess $+40.6$pp leave-one-out
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:77:  the unique substrate consistent with these signatures. Other regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:82:\item \emph{Not a derivation of consciousness.} The substrate witness
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:86:\item \emph{Not a selection theorem.} The companion adaptive-closure-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:100:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:101:  Laplacian floor $\Ph^{-2} \approx 0.382$ is a design-level
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:102:  stability clamp (it makes $\Cph$ strictly positive definite and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:124:$+15$pp floor) licenses `decisively above prereg', not `proves'. A
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:139:\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:140:selection theorem on the 4-tuple bridge; circuit-level mechanistic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:141:identification; first-principles derivation of $\Ph^{-2}$ shift;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:150:constructs $\Rsixhundred$ and the response operator $\Cph$, with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:151:$\Ph^{-2}$ shift disclosed as a design-level stability clamp.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:161:ACT bridge (without claiming a selection theorem).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:7:To test high-level signatures — NREM-N3 variance collapse, propofol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:8:regime-switching, propofol $\Phi$ collapse — we add a recurrent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:25:\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:34:prior snapshot). The substrate response operator $\Cph$ is unchanged
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:52:gives smooth dynamics with cascade $\alpha\approx 1.09$ — no
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:57:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:64:            \texorpdfstring{$\Phi$}{Phi}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:74:\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:85:We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:88:machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:145:\textbf{RECOVERY.} Identical to WAKE — verifies deterministic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:163:\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:169:\textbf{$C$ — Context rotation (S$^{7}$ observer frames).} The active
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:176:\textbf{$P$ — Partial emission.} High-pressure uncrossed vertices
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:182:\textbf{$E$ — Equator compensation.} The H$_3$ shell-4 equator is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:189:orbits, S$^{7}$ rung, equatorial shell) — they are not free dynamical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:100:permutation — well above the $25\%$ chance level for $4$ categories.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:155:higher-order graph statistics. ARIA reference: $G_{V_{600}}$ with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:156:$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:201:node-count-dependent — its theoretical maximum is the node count of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:8:wallclock — the minimal information a hostile reviewer needs to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:20:\textbf{Frozen 2026-04-24.} Two later batteries — H$_4$ fingerprint
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:21:predictions and rung observables — were preregistered on 2026-04-24
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:30:propofol switching ratio, propofol continuity drop, propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:146:as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:8:operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:16:The 600-cell $\Rsixhundred$ has $120$ vertices in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:18:With $\Ph = (1+\sqrt 5)/2$ the canonical vertex set is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:24:  $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:33:The substrate graph $G_{V_{600}} = (V, E)$ is built by connecting each
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:40:The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, every
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:42:$\Lop = D - A$ has spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:44:\sigma(\Lop) \;=\;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:45:\bigl\{0^{1}, 3^{4}, 4\Ph^{9}, 6\Ph^{16}, (12\!-\!4\Ph)^{9},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:46:       (12\!-\!6\Ph)^{16}, 9^{4}, 12^{1}\bigr\},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:57:$\mathbb{Z}[\Ph]$, the exponents become $\{7, 13, 17, 23\}$. We label
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:66:\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:71:\Cph \;=\; \Lop + \Ph^{-2} I,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:73:\psi \;=\; \Cph^{-1} f.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:75:The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:76:clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:77:$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:78:inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:81:$\Cph$ as the basis for an independent passive-regime witness in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:85:This paper imports $\Cph$ from that line; we do not re-derive it.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:87:The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:92:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:96:The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:115:$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:116:collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:137:cascade is a decomposition of operators on $\Rsixhundred$, and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:138:choice of $\Rsixhundred$ as the active substrate is post-hoc justified
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:144:\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:147:\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:150:\item Not fixed by this paper: the choice of $\Rsixhundred$ over the

 succeeded in 196ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:55:models (\S\ref{sec:chain}) are biologically-motivated design choices,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:65:preprint~\citep{SmartAdaptiveClosureTransport2026} provides the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:88:biologically realistic (\S\ref{sec:chain}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:174:We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:175:OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:176:the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:177:the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:178:HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:180:methodology follows~\citep{BeggsPlenz2003}; the integrated-information
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:181:$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:183:al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:184:follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:186:repository~\citep{ariaChessRepo}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:192:from the project repository~\citep{ariaChessRepo} via the included
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:2:\section{Results}\label{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:7:(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:20:(\S\ref{sec:chain}). Per-condition trajectory observables are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:24:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:29:\label{tab:per_condition}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:30:\begin{tabular}{l r r l r r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:31:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:33:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:38:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:39:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:42:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:46:\label{tab:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:47:\begin{tabular}{c l l c c l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:48:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:50:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:52:   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:55:   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:58:   EEG microstate~\citep{Brodbeck2012Microstates} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:61:   Tononi 2008~\citep{Tononi2008} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:67:   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:71:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:72:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:80:(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:84:\S\ref{sec:limitations}~\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:86:\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:94:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:98:\label{tab:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:99:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:100:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:102:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:116:\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:122:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:123:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:126:\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:130:\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:141:  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:150:  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:162:\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:167:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:172:\label{tab:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:173:\begin{tabular}{l c l c}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:174:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:176:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:178:Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:181:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:182:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:189:$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:198:(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:199:stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:201:any specific subject (\S\ref{sec:chain}). Three-way overlap on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:3:         replication}\label{sec:stress}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:21:(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:33:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:37:\label{tab:cxp_trend}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:38:\begin{tabular}{r l r l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:39:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:41:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:47:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:48:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:69:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:73:\label{tab:cxp_means}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:74:\begin{tabular}{l r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:75:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:77:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:82:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:83:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:139:\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:2:\section{Cross-domain selectivity}\label{sec:cross_domain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:5:This section reports three cross-domain witnesses. \S\ref{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:6:gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:8:\S\ref{ssec:hcp} gives the HCP brain-graph maximum-symmetry null.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:16:\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:35:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:40:\label{tab:chess_depth}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:41:\begin{tabular}{r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:42:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:44:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:51:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:52:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:55:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:60:\label{tab:chess_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:61:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:62:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:64:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:66:P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:69:\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:70:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:71:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:74:$^{\dagger}$ The 2026-04-18 preregistration combined the null-mapping
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:79:$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:94:(\S\ref{sec:method}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:109:\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:115:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:119:\label{tab:conv_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:120:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:121:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:123:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:127:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:128:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:144:(\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:147:            (P17--P18)}\label{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:150:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:156:$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:160:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:165:\label{tab:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:166:\begin{tabular}{l r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:167:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:169:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:174:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:175:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:225:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:231:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:235:\label{tab:cross_domain_summary}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:236:\begin{tabular}{l r r r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:237:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:239:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:243:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:244:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:2:\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:12:\subsection{Regime}\label{ssec:regime}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:20:(\S\ref{sec:intro}). \emph{Evidence:} empirical correspondences hold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:27:six-signature results in~\S\ref{ssec:six_signatures} are reported on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:32:in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:44:cortical input is much richer. \emph{Disclosure:}~\S\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:51:\subsection{Post-hoc}\label{ssec:posthoc}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:58:\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:63:ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:71:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:78:strictly positive definite (\S\ref{ssec:cphi}); it is not derived
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:80:\S\ref{ssec:cphi} marks this as a design-level choice; the companion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:81:kernel doc~\citep{SmartAriaClosureKernel2026} explicitly does not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:84:witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:88:\subsection{Interpretation}\label{ssec:interpretation}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:94:\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:96:\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:101:IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:105:2008~\citep{BalduzziTononi2008} on the substrate; not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:110:\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:114:\subsection{Test/claim}\label{ssec:testclaim}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:120:\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:145:\subsection{State-drift / out-of-scope}\label{ssec:scope}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:167:  4-polytopes — see~\S\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:75:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:82:explicitly listed in~\S\ref{sec:limitations} and remain open.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:91:flavour anomaly~\citep{SmartBAnomaly2026} on the same response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:2:\section{Methods and provenance}\label{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:25:listed as future strengthening builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:51:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:55:\label{tab:provenance}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:56:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:57:\toprule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:59:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:65:P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:77:P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:78:\midrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:80:\bottomrule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:81:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:87:recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:91:methodology~\citep{BeggsPlenz2003}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:94:consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:100:EEG~\citep{OpenNeuroDS004902},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:105:release~\citep{ZenodoDMT3992359},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:109:S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:118:Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:176:generalisable lesson is recorded in \S\ref{sec:limitations}: any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:6:(Integrated Information Theory~\citep{Tononi2008,BalduzziTononi2008},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:7:Global Workspace Theory~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:8:predictive processing~\citep{FristonFreeEnergy2010,ClarkPP2013}) and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:23:over a century~\citep{CoxeterRegularPolytopes,Weisstein600Cell}; to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:87:  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:94:  builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:105:  document~\citep{SmartAriaClosureKernel2026} discusses its role.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:129:and applied throughout~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:148:\S\ref{sec:method} gives the provenance ledger (preregistration date,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:149:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:152:\S\ref{sec:chain} adds the recurrent self-model layer above the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:154:\S\ref{sec:results} reports the empirical tables: six drug/sleep
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:156:$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:158:$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:159:selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:162:\S\ref{sec:limitations} enumerates limitations and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:163:hostile-review guard matrix. \S\ref{sec:conclusion} concludes.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:2:\section{The 600-cell response substrate}\label{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:5:This section constructs the substrate. \S\ref{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:6:gives the vertex set. \S\ref{ssec:graph} gives the graph and its
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:7:H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:9:\S\ref{ssec:shells} gives the 9-shell decomposition used for source
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:10:projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:11:descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:14:\subsection{Vertex construction}\label{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:17:$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:31:\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:38:spectrum are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:39:\begin{lemma}[600-cell graph facts]\label{lem:600cell}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:64:\S\ref{sec:chain}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:66:\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:70:\begin{equation}\label{eq:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:80:kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:82:flavour physics~\citep{SmartBAnomaly2026}, where the same operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:89:in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:92:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:101:varies between conditions in~\S\ref{sec:chain}; it is reported
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:104:\subsection{Shell decomposition}\label{ssec:shells}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:113:in companion preprints~\citep{SmartAriaClosureKernel2026}, the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:120:\subsection{Cascade descent (sketch)}\label{ssec:cascade}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:122:The recurrent layer in~\S\ref{sec:chain} references a cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:139:by the empirical correspondences in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:154:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:2:\section{Discussion}\label{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:9:preprint~\citep{SmartAdaptiveClosureTransport2026}. We do not claim a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:46:\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:49:(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:56:\textbf{vs Global Workspace Theory.}~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:57:The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:64:\textbf{vs Predictive Processing.}~\citep{FristonFreeEnergy2010,ClarkPP2013}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:80:\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:83:preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:117:document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:119:anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:163:The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:185:  see \S\ref{sec:limitations}.)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:2:\section{The recurrent layer}\label{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:5:The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:6:cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:17:signatures in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:57:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:88:machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:89:collapse in~\S\ref{sec:results} is consistent with the IIT direction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:161:the C$\times$P stress test in~\S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:190:choices. Their causal effects are reported in~\S\ref{sec:stress}.

codex
One substantive mathematical issue has emerged: the paper’s stated “full” 600-cell Laplacian spectrum has multiplicities summing to 60, not 120. I’m checking the local substrate code/docs now before treating it as a must-fix rather than a notation convention.
exec
/bin/bash -lc "rg -n \"(eigenvalue|spectrum|multiplicity|4φ|6φ|12 -|12\\-|sigma|K_7|K_13|K_17|K_23|K_29|K_19|K_11|K_1)\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,260p' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "sed -n '1,240p' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_closure_kernel.py'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 258ms:
"""σ-orbit projector basis — the natural block decomposition for K-class operators.

Derivation
----------
The E_8 Coxeter element C has order 30. T = C + C⁻¹ is real symmetric
with 4 distinct eigenvalues:

    τ_m = 2 cos(2πm/30),    m ∈ {1, 7, 11, 13}

Each τ_m has multiplicity 2 in the 8D representation (m and 30−m give
the same τ). The Coxeter spectral projectors P_m project onto the 2D
τ_m-eigenspace.

In the basis adapted to {P_1, P_7, P_11, P_13}, every K-class generator
A_m = P_m · (C − C⁻¹) lives in a SINGLE 2×2 block — block-diagonal by
construction:

    A_m = block-diag(0, ..., R(θ_m), ..., 0)         in σ-orbit basis

where R(θ_m) is the 2D rotation generator at angle θ_m = 2πm/30:
    K_1:  θ = 12°,  R(12°)
    K_7:  θ = 84°,  R(84°)
    K_11: θ = 132°, R(132°)
    K_13: θ = 156°, R(156°)

This is THE clean cascade decomposition for K-class operators. It is
not the same as H_4 ⊕ σ(H_4) (which doesn't actually block-diagonalise
the K-class generators, as the icosian-basis test showed).

Public API:
    build_sigma_orbit_basis()      # 8×8 orthogonal U_orb
    transform_to_sigma_orbit(A)    # A → U_orb · A · U_orb^T
    block_decompose_sigma_orbit(A) # 4 × (2×2 block) report

Empirical predictions (testable in self-test):
- ‖A_K1 in K_1 block‖ = ‖A_K1‖_F     (100% — single-block)
- ‖A_K1 in K_7 block‖ = 0
- Similarly K_7, K_11, K_13 — each lives in one 2×2 block.
- A_K+ = β_1·A_1 + β_11·A_11 lives in (K_1 block) ⊕ (K_11 block).
- A_K- = β_7·A_7 + β_13·A_13 lives in (K_7 block) ⊕ (K_13 block).
- C in this basis = block-diag of 4 × 2D rotations at θ_m angles.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np

K_CLASSES = (1, 7, 11, 13)

# H_4 exponents are {1, 11, 19, 29} = K-classes {1, 11}.
# σ(H_4) exponents are {7, 13, 17, 23} = K-classes {7, 13}.
# Ordering K_CLASSES_CASCADE places H_4 first, σ(H_4) second so that
# the (4|4) split of R^8 in this basis IS the H_4 ⊕ σ(H_4) split.
K_CLASSES_CASCADE = (1, 11, 7, 13)
H4_K_CLASSES     = (1, 11)
SIGMA_H4_K_CLASSES = (7, 13)


# ─────────────────────── basis construction ───────────────────────────

def _real_eigenbasis_for_tau(C: np.ndarray, T: np.ndarray, m: int) -> np.ndarray:
    """Real 8×2 basis for the τ_m-eigenspace of T = C + C⁻¹.

    Approach: use the v66 spectral projector P_m = ∏_{n≠m} (T − τ_n·I) / (τ_m − τ_n).
    The image of P_m is the 2D τ_m-eigenspace; its column space gives the basis.
    SVD on P_m yields an orthonormal real basis for that eigenspace.
    """
    from kernel.v66_e8_coxeter import projector_P_m
    P = projector_P_m(m)
    U_svd, s, _Vt = np.linalg.svd(P)
    # Keep the leading 2 left singular vectors (rank-2 projector)
    return U_svd[:, :2]


def build_sigma_orbit_basis(ordering: Tuple[int, ...] = K_CLASSES_CASCADE) -> np.ndarray:
    """Construct U_orb ∈ O(8) with K-class blocks in the requested order.

    Default ordering is K_CLASSES_CASCADE = (1, 11, 7, 13) so that the
    upper-left 4×4 block of any centralizer operator is its H_4 part and
    the lower-right 4×4 is its σ(H_4) part.

    Pass ordering = K_CLASSES = (1, 7, 11, 13) for the spectrum-ordered basis.
    """
    cache_key = ("_cache", ordering)
    cache = build_sigma_orbit_basis.__dict__.get(cache_key)
    if cache is not None:
        return cache
    from kernel.v66_e8_coxeter import coxeter_element

    C = coxeter_element()
    T = C + np.linalg.inv(C)

    blocks: List[np.ndarray] = []
    for m in ordering:
        B = _real_eigenbasis_for_tau(C, T, m)        # (8, 2)
        blocks.append(B)
    U = np.hstack(blocks)                             # (8, 8)

    # Re-orthonormalise across blocks (different eigenspaces are
    # orthogonal in theory, but numerical SVD output may have small
    # cross-block overlap)
    Q, _R = np.linalg.qr(U)
    if np.linalg.det(Q) < 0:
        Q[:, -1] = -Q[:, -1]
    build_sigma_orbit_basis.__dict__[cache_key] = Q   # cache by ordering
    return Q


# ─────────────────────── decomposition ────────────────────────────────

def transform_to_sigma_orbit(A_bourbaki: np.ndarray) -> np.ndarray:
    """A → U_orb^T · A · U_orb, block-diagonal in the σ-orbit basis if A∈centralizer."""
    U = build_sigma_orbit_basis()
    return U.T @ A_bourbaki @ U


@dataclass(frozen=True)
class SigmaOrbitReport:
    block_K1: np.ndarray
    block_K7: np.ndarray
    block_K11: np.ndarray
    block_K13: np.ndarray
    on_diag_norm: float
    off_diag_norm: float
    fraction_in_diag: float


def block_decompose_sigma_orbit(A_bourbaki: np.ndarray) -> SigmaOrbitReport:
    """Decompose A into 4 × (2×2) σ-orbit blocks plus off-diagonal residue.

    Uses K_CLASSES_CASCADE order: blocks at positions [K_1, K_11, K_7, K_13].
    """
    A = transform_to_sigma_orbit(A_bourbaki)
    # Cascade ordering: (1, 11, 7, 13) → block positions 0..3
    blk_K1  = A[0:2, 0:2]
    blk_K11 = A[2:4, 2:4]
    blk_K7  = A[4:6, 4:6]
    blk_K13 = A[6:8, 6:8]
    diag = np.zeros_like(A)
    # Reconstruct diag in the SAME cascade order as extraction.
    # Bug caught by Codex math review 2026-04-29: previously the slot at
    # rows 2:4 was filled with blk_K7 (extracted from rows 4:6) and vice
    # versa, masking off-diagonal residue for any A with both K_7 and K_11
    # content (uniform, golden, K_+, K_-).
    diag[0:2, 0:2]  = blk_K1
    diag[2:4, 2:4]  = blk_K11
    diag[4:6, 4:6]  = blk_K7
    diag[6:8, 6:8]  = blk_K13
    off = A - diag
    on_n = float(np.linalg.norm(diag))
    off_n = float(np.linalg.norm(off))
    total_sq = on_n ** 2 + off_n ** 2
    return SigmaOrbitReport(
        block_K1=blk_K1, block_K7=blk_K7, block_K11=blk_K11, block_K13=blk_K13,
        on_diag_norm=on_n, off_diag_norm=off_n,
        fraction_in_diag=float(on_n ** 2 / max(total_sq, 1e-30)),
    )


# ─────────────────────── cascade descent (clean) ──────────────────────

@dataclass(frozen=True)
class CascadeDecomposition:
    A_h4: np.ndarray              # 4×4 H_4 sub-rung (K_1 ⊕ K_11)
    A_sigma_h4: np.ndarray        # 4×4 σ(H_4) sub-rung (K_7 ⊕ K_13)
    cross_norm: float             # ‖cross-block‖, exactly 0 for centralizer ops
    h4_frobenius: float
    sigma_frobenius: float


def descend_e8_to_h4_cascade(A_bourbaki: np.ndarray) -> CascadeDecomposition:
    """Clean E_8 → H_4 ⊕ σ(H_4) descent in the σ-orbit cascade basis.

    For centralizer operators (any A that commutes with C, e.g. all v66
    K-class operators), cross_norm is exactly 0 and:

        A_h4       = block-diag of K_1 and K_11 rotation generators
        A_sigma_h4 = block-diag of K_7 and K_13 rotation generators

    This is the mathematically clean cascade — earlier naïve identity-basis
    and Procrustes-icosian-basis attempts had cross_norm 0.5–2.2; here it
    is machine-zero.
    """
    A = transform_to_sigma_orbit(A_bourbaki)
    A_h4 = A[:4, :4]
    A_sg = A[4:, 4:]
    X = A[:4, 4:]
    Y = A[4:, :4]
    cross = np.concatenate([X.ravel(), Y.ravel()])
    return CascadeDecomposition(
        A_h4=A_h4,
        A_sigma_h4=A_sg,
        cross_norm=float(np.linalg.norm(cross)),
        h4_frobenius=float(np.linalg.norm(A_h4)),
        sigma_frobenius=float(np.linalg.norm(A_sg)),
    )


# ─────────────────────── self-test ────────────────────────────────────

def _self_test() -> None:
    from kernel.v66_e8_coxeter import (
        operator_A_beta, BETA_PROFILES, generator_A_m, coxeter_element,
    )
    import math

    U = build_sigma_orbit_basis()
    print(f"[sigma_orbit_basis] U_orb ∈ O(8): det={np.linalg.det(U):+.6f}  "
          f"orthogonality={np.linalg.norm(U.T @ U - np.eye(8)):.2e}")

    print(f"\n[sigma_orbit_basis] Per-K_m generator block decomposition")
    print(f"  (predict: each A_m has 100% weight in its OWN 2×2 block, 0 elsewhere)")
    print(f"{'A_m':<6} {'%K_1':<8} {'%K_7':<8} {'%K_11':<8} {'%K_13':<8} {'%off':<8}")
    for m in K_CLASSES:
        A = generator_A_m(m)
        rep = block_decompose_sigma_orbit(A)
        total_sq = float(np.linalg.norm(A) ** 2)
        pct = lambda blk: 100.0 * float(np.linalg.norm(blk) ** 2 / max(total_sq, 1e-30))
        print(f"A_{m:<5}{pct(rep.block_K1):<8.2f}{pct(rep.block_K7):<8.2f}"
              f"{pct(rep.block_K11):<8.2f}{pct(rep.block_K13):<8.2f}"
              f"{100.0 * (1.0 - rep.fraction_in_diag):<8.4f}")

    print(f"\n[sigma_orbit_basis] β-profile operator decomposition")
    print(f"{'profile':<22} {'on_diag_frac':<14} {'off_diag_frac':<14}")
    for prof_name in ["K_1_only", "K_7_only", "K_11_only", "K_13_only",
                      "Qphi_packet_K+", "Qphi_packet_K-", "uniform", "golden"]:
        beta = BETA_PROFILES[prof_name]
        A = operator_A_beta(beta)
        rep = block_decompose_sigma_orbit(A)
        print(f"{prof_name:<22} {rep.fraction_in_diag:<14.6f} "
              f"{1.0 - rep.fraction_in_diag:<14.6f}")

    # Coxeter C in σ-orbit basis: should be block-diag of 4 × 2D rotations
    print(f"\n[sigma_orbit_basis] Coxeter C in σ-orbit basis")
    C = coxeter_element()
    rep = block_decompose_sigma_orbit(C)
    print(f"  on-diagonal: {rep.fraction_in_diag:.6f}  off-diagonal: {1.0 - rep.fraction_in_diag:.6f}")
    print(f"  block angles (deg) — predict K_1=12, K_7=84, K_11=132, K_13=156:")
    for label, blk in [("K_1", rep.block_K1), ("K_7", rep.block_K7),
                        ("K_11", rep.block_K11), ("K_13", rep.block_K13)]:
        # 2D rotation block: angle from atan2(blk[1,0], blk[0,0])
        theta = math.degrees(math.atan2(blk[1, 0], blk[0, 0]))
        print(f"    {label}: θ = {theta:+.2f}°")


if __name__ == "__main__":
    _self_test()

 succeeded in 256ms:
"""VFD Closure Green Kernel — geometry-derived response operator.

Implements the canonical API from `ARIA CONTEXT INSERT — VFD Closure Green
Kernel`. The kernel maps a localised residual / source on a φ-regularised
closure substrate into a compressed low-rank response field.

Core equation:
    C_φ = L_M + φ⁻² · I            (φ-regularised closure operator)
    ψ   = C_φ⁻¹ · f                (response to source f)

Continuum limit (1D projection):
    L_φ = -d²/dx² + φ⁻²            with Green's function
    G(x) = (φ/2) · exp(-|x| / φ)
    κ(x) = exp(-|x| / φ)            (normalised kernel)

φ⁻² acts as mass / coherence-length regularisation: it sets the decay
scale of the response and suppresses unstable high-frequency modes.

Discrete form on the 600-cell graph:
    ψ(v) = (L_V600 + φ⁻²·I)⁻¹ f(v)

Empirically: under uniform-shell source, the projected shell-mean response
matches exp(-|x|/φ) at r ≈ 0.98 (B-anomaly continuum match at α=1).

This module is the response primitive for ARIA's crystallisation layer.
The selection dynamic (dW/dt = -∇V(W)) is in `kernel/lyapunov_selector.py`.

Public API (canonical):
    build_600cell_graph()
    compute_graph_laplacian(adj)
    compute_closure_operator(L, phi)
    solve_green_response(L, source, phi)
    shell_decomposition(verts)
    shell_mean_projection(field, shells)
    spectral_decomposition(L)
    project_to_observable_coordinate(...)

Convenience:
    solve_vfd_green_kernel(substrate, source, phi=PHI)
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INV_PHI_SQ = 1.0 / (PHI * PHI)


# ─────────────────────── 600-cell substrate ───────────────────────────

def build_600cell_vertices() -> np.ndarray:
    """120 vertices of the 600-cell on the unit S³.

    Three orbit classes:
      A:  ±e_i                                    (8 vertices)
      B:  (±½, ±½, ±½, ±½)                         (16 vertices)
      C:  even-permutations of (±φ/2, ±½, ±1/(2φ), 0)   (96 vertices)
    """
    verts: List[List[float]] = []

    for i in range(4):
        for s in (1, -1):
            v = [0.0, 0.0, 0.0, 0.0]
            v[i] = s
            verts.append(v)

    for s0 in (1, -1):
        for s1 in (1, -1):
            for s2 in (1, -1):
                for s3 in (1, -1):
                    verts.append([s0 * 0.5, s1 * 0.5, s2 * 0.5, s3 * 0.5])

    base = [PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0]
    even_perms = [
        (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2),
        (1, 0, 3, 2), (1, 2, 0, 3), (1, 3, 2, 0),
        (2, 0, 1, 3), (2, 1, 3, 0), (2, 3, 0, 1),
        (3, 0, 2, 1), (3, 1, 0, 2), (3, 2, 1, 0),
    ]
    for perm in even_perms:
        for s0 in (1, -1):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    vals = [s0 * base[0], s1 * base[1], s2 * base[2], 0.0]
                    v = [0.0, 0.0, 0.0, 0.0]
                    for i, p in enumerate(perm):
                        v[p] = vals[i]
                    verts.append(v)

    arr = np.asarray(verts, dtype=float)
    arr = arr / np.linalg.norm(arr, axis=1, keepdims=True)

    unique: List[np.ndarray] = [arr[0]]
    for v in arr[1:]:
        if all(np.linalg.norm(v - u) > 0.01 for u in unique):
            unique.append(v)
    return np.asarray(unique[:120], dtype=float)


def build_600cell_graph(
    verts: Optional[np.ndarray] = None,
) -> Tuple[np.ndarray, np.ndarray, List[Tuple[int, int]]]:
    """Return (vertices, adjacency, edges) for the 600-cell.

    Edges defined by inner-product condition <v, w> = φ/2 (angle 36°).
    Yields 720 edges, each vertex degree 12.
    """
    if verts is None:
        verts = build_600cell_vertices()
    n = verts.shape[0]
    target = PHI / 2.0
    tol = 1e-3
    A = np.zeros((n, n), dtype=float)
    edges: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            ip = float(np.dot(verts[i], verts[j]))
            if abs(ip - target) < tol:
                A[i, j] = 1.0
                A[j, i] = 1.0
                edges.append((i, j))
    return verts, A, edges


def compute_graph_laplacian(adj: np.ndarray) -> np.ndarray:
    """Standard graph Laplacian L = D − A, D diagonal of degrees."""
    deg = np.diag(adj.sum(axis=1))
    return deg - adj


# ─────────────────────── closure operator + response ──────────────────

def compute_closure_operator(L: np.ndarray, phi: float = PHI) -> np.ndarray:
    """C_φ = L + φ⁻² · I.

    φ acts as the coherence length / mass regulator. φ⁻² lifts the Laplacian
    spectrum away from zero so the inverse is well-defined and the response
    is bounded.
    """
    n = L.shape[0]
    return L + (1.0 / (phi * phi)) * np.eye(n)


def solve_green_response(
    L: np.ndarray,
    source: np.ndarray,
    phi: float = PHI,
) -> np.ndarray:
    """ψ = (L + φ⁻²·I)⁻¹ · f via solve (no explicit inverse).

    Numerically equivalent to `np.linalg.inv(C_phi) @ source` but
    cheaper and more stable.
    """
    C = compute_closure_operator(L, phi)
    return np.linalg.solve(C, source)


# ─────────────────────── shell decomposition ──────────────────────────

def shell_decomposition(
    verts: np.ndarray,
    pole: int = 0,
    tol: float = 1e-4,
) -> List[List[int]]:
    """Group 120 vertices into the 9 H₃ shells about a chosen pole vertex.

    Canonical 600-cell shell sizes about a pole: {1, 12, 20, 12, 30, 12, 20, 12, 1}.
    Antipodal symmetry: shell(-v) = 8 − shell(v).
    """
    v0 = verts[pole]
    cosines = verts @ v0          # 120-vector of inner products with pole
    cos_rounded = np.round(cosines / tol) * tol
    unique_cos = sorted(np.unique(cos_rounded), reverse=True)
    shells: List[List[int]] = []
    for c in unique_cos:
        shell = np.where(np.isclose(cos_rounded, c, atol=tol))[0].tolist()
        shells.append(shell)
    return shells


def shell_mean_projection(
    field: np.ndarray,
    shells: List[List[int]],
) -> np.ndarray:
    """Project a per-vertex field onto its shell-mean coordinate.

    Returns a vector of shell means in shell-index order.
    """
    return np.asarray([float(np.mean(field[s])) for s in shells])


# ─────────────────────── spectral form ────────────────────────────────

@dataclass(frozen=True)
class SpectralBlocks:
    """Eigenvalues and eigenvectors of L_M, sorted by eigenvalue."""
    eigvals: np.ndarray              # (n,)
    eigvecs: np.ndarray              # (n, n) — column k = eigenvector for eigvals[k]


def spectral_decomposition(L: np.ndarray) -> SpectralBlocks:
    """Real symmetric eigendecomposition of the Laplacian, sorted ascending."""
    w, V = np.linalg.eigh(L)
    return SpectralBlocks(eigvals=w, eigvecs=V)


def green_response_spectral(
    spectral: SpectralBlocks,
    source: np.ndarray,
    phi: float = PHI,
) -> np.ndarray:
    """ψ = Σ_n [⟨u_n, f⟩ / (λ_n + φ⁻²)] · u_n.

    Equivalent to `solve_green_response` but exposes the per-mode amplitudes.
    Useful for compression analysis (which isotypic block dominates).
    """
    coeffs = spectral.eigvecs.T @ source
    weighted = coeffs / (spectral.eigvals + 1.0 / (phi * phi))
    return spectral.eigvecs @ weighted


def isotypic_compression(
    spectral: SpectralBlocks,
    source: np.ndarray,
    phi: float = PHI,
    eig_tol: float = 1e-6,
) -> Dict[float, Dict[str, float]]:
    """Group eigenmodes by eigenvalue (isotypic blocks); report each block's
    fractional contribution to ‖ψ‖² for the given source.

    For 600-cell uniform-equator source, the dominant block is λ=9 (mult 6),
    matching the documented 120D → rank-6 → rank-1 compression.
    """
    coeffs = spectral.eigvecs.T @ source              # (n,)
    amps = coeffs / (spectral.eigvals + 1.0 / (phi * phi))
    psi_total_sq = float(np.sum(amps * amps))

 succeeded in 5537ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_runtime.py:24:    runtime.tick(self_spectrum, world_spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_runtime.py:25:    decision = runtime.crystallise(candidates, world_spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_runtime.py:199:    def tick(self, self_spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_runtime.py:200:             world_spectrum: FrequencySpectrum) -> CoherenceState:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_runtime.py:209:            self._last_brain_state = self.brain.settle(self_spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_runtime.py:212:        state = self.engine.settle(self_spectrum, world_spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_runtime.py:236:        Each spectrum represents a candidate action's resulting state.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_runtime.py:273:                spectrum=candidate_spectra[i] if i < len(candidate_spectra) else FrequencySpectrum(),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_runtime.py:285:        world_spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_runtime.py:290:            candidates, world_spectrum, policy_blocked)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/e8_substrate.py:148:        # Precompute and cache adjacency spectrum + eigenvectors
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/e8_substrate.py:150:        self._cached_spectrum = None
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/e8_substrate.py:228:        (trivial) eigenvalue is 0 with eigenvector (1,1,...,1)/√N.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/e8_substrate.py:238:        Returns {eigenvalue → amplitude} for each distinct eigenvalue.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/e8_substrate.py:241:        if self._cached_spectrum is None:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/e8_substrate.py:243:            self._cached_spectrum = eigs
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/e8_substrate.py:248:        for e, a in zip(self._cached_spectrum, amps):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/e8_substrate.py:250:            out[k] = out.get(k, 0.0) + float(a * a)  # power per eigenvalue
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:12:Our 600-cell has distinct Laplacian eigenvalues with known multiplicities
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:53:    index: int                    # mode id (sorted by eigenvalue)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:54:    eigenvalue: float             # Laplacian λ
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:58:    multiplicity_group: int       # shared eigenvalue group (0..G-1)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:101:        # Group eigenvalues by numerical equality (multiplicities)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:111:                index=i, eigenvalue=lam, omega=omega, period=period,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:113:                multiplicity_group=int(group_ids[i]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:145:        """Total power aggregated by multiplicity group (distinct eigenvalue)."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:152:            out.setdefault(m.multiplicity_group, 0.0)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:153:            out[m.multiplicity_group] += float(power[m.index])
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:277:                        "mode": m.index, "eigenvalue": m.eigenvalue,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:287:                    "mode": m.index, "eigenvalue": m.eigenvalue,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:298:        """Compact summary of eigenmode structure + current spectrum."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:299:        # Unique eigenvalue groups sorted ascending
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:302:            groups.setdefault(round(m.eigenvalue, 4), []).append(m.index)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:315:                "multiplicity": len(members),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:316:                "group_id": self.modes[members[0]].multiplicity_group,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/spectral_observer.py:317:                "power": power_map.get(self.modes[members[0]].multiplicity_group, 0.0),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/v66_e8_coxeter.py:9:  τ_m = 2cos(2πm/30) for m ∈ {1, 7, 11, 13}        (the 4 distinct T eigenvalues)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/v66_e8_coxeter.py:21:The K_7 single-class closure produces the lowest phase drift (0.292) of any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/v66_e8_coxeter.py:22:β variant on the v66 scaffold — K_7 (θ_7 = 84°) is the substrate's intrinsic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/v66_e8_coxeter.py:52:# Q(φ)-packet decomposition (R1 D2): K_+ = K_1 ∪ K_11, K_- = K_7 ∪ K_13.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/v66_e8_coxeter.py:70:    eigenvalue phases ×30 mod 30 = {1, 7, 11, 13, 17, 19, 23, 29}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/v66_e8_coxeter.py:80:    """T = C + C^(-1). Eigenvalues are the 4 τ_m, each at multiplicity 2."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/v66_e8_coxeter.py:215:    "K_7_only":         (0.0, 1.0, 0.0, 0.0),       # substrate's intrinsic mode
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/v66_e8_coxeter.py:216:    "K_1_only":         (1.0, 0.0, 0.0, 0.0),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/v66_e8_coxeter.py:217:    "K_11_only":        (0.0, 0.0, 1.0, 0.0),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/v66_e8_coxeter.py:218:    "K_13_only":        (0.0, 0.0, 0.0, 1.0),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:28:      σ-even (eigenvalue −κ) is handled by mean projection per step:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:34:  - cascade-sigma-rationality WO-CCC-P1 §3, §4
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:44:                                  (eigenvalues α λ_i(L_H4) − κ)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:46:                                  (eigenvalues α λ_i(L_H4) + κ)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:48:Mean projection removes the constant mode (which has eigenvalue −κ on σ-even,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:173:        # Spectral radius of L_dual: top eigenvalue lives on σ-odd subspace,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:221:    def sigma_even(self, p_primary: np.ndarray, p_dual: np.ndarray) -> np.ndarray:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:225:    def sigma_odd(self, p_primary: np.ndarray, p_dual: np.ndarray) -> np.ndarray:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:241:            "sigma_even_min_eigenvalue_constant": self.gamma - self.kappa,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:242:            "sigma_odd_min_eigenvalue_constant": self.gamma + self.kappa,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:303:        s_odd_before = op.sigma_odd(p_a, p_b)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dual_closure_operator.py:305:        s_odd_after = op.sigma_odd(p_a_new, p_b_new)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:6:with 4 distinct eigenvalues:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:10:Each τ_m has multiplicity 2 in the 8D representation (m and 30−m give
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:21:    K_1:  θ = 12°,  R(12°)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:22:    K_7:  θ = 84°,  R(84°)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:23:    K_11: θ = 132°, R(132°)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:24:    K_13: θ = 156°, R(156°)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:31:    build_sigma_orbit_basis()      # 8×8 orthogonal U_orb
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:32:    transform_to_sigma_orbit(A)    # A → U_orb · A · U_orb^T
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:33:    block_decompose_sigma_orbit(A) # 4 × (2×2 block) report
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:36:- ‖A_K1 in K_1 block‖ = ‖A_K1‖_F     (100% — single-block)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:37:- ‖A_K1 in K_7 block‖ = 0
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:38:- Similarly K_7, K_11, K_13 — each lives in one 2×2 block.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:39:- A_K+ = β_1·A_1 + β_11·A_11 lives in (K_1 block) ⊕ (K_11 block).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:40:- A_K- = β_7·A_7 + β_13·A_13 lives in (K_7 block) ⊕ (K_13 block).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:77:def build_sigma_orbit_basis(ordering: Tuple[int, ...] = K_CLASSES_CASCADE) -> np.ndarray:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:84:    Pass ordering = K_CLASSES = (1, 7, 11, 13) for the spectrum-ordered basis.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:87:    cache = build_sigma_orbit_basis.__dict__.get(cache_key)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:107:    build_sigma_orbit_basis.__dict__[cache_key] = Q   # cache by ordering
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:113:def transform_to_sigma_orbit(A_bourbaki: np.ndarray) -> np.ndarray:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:115:    U = build_sigma_orbit_basis()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:130:def block_decompose_sigma_orbit(A_bourbaki: np.ndarray) -> SigmaOrbitReport:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:133:    Uses K_CLASSES_CASCADE order: blocks at positions [K_1, K_11, K_7, K_13].
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:135:    A = transform_to_sigma_orbit(A_bourbaki)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:145:    # versa, masking off-diagonal residue for any A with both K_7 and K_11
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:166:    A_h4: np.ndarray              # 4×4 H_4 sub-rung (K_1 ⊕ K_11)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:167:    A_sigma_h4: np.ndarray        # 4×4 σ(H_4) sub-rung (K_7 ⊕ K_13)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:170:    sigma_frobenius: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:179:        A_h4       = block-diag of K_1 and K_11 rotation generators
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:180:        A_sigma_h4 = block-diag of K_7 and K_13 rotation generators
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:186:    A = transform_to_sigma_orbit(A_bourbaki)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:194:        A_sigma_h4=A_sg,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:197:        sigma_frobenius=float(np.linalg.norm(A_sg)),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:209:    U = build_sigma_orbit_basis()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:210:    print(f"[sigma_orbit_basis] U_orb ∈ O(8): det={np.linalg.det(U):+.6f}  "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:213:    print(f"\n[sigma_orbit_basis] Per-K_m generator block decomposition")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:215:    print(f"{'A_m':<6} {'%K_1':<8} {'%K_7':<8} {'%K_11':<8} {'%K_13':<8} {'%off':<8}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:218:        rep = block_decompose_sigma_orbit(A)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:225:    print(f"\n[sigma_orbit_basis] β-profile operator decomposition")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:227:    for prof_name in ["K_1_only", "K_7_only", "K_11_only", "K_13_only",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:231:        rep = block_decompose_sigma_orbit(A)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:236:    print(f"\n[sigma_orbit_basis] Coxeter C in σ-orbit basis")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:238:    rep = block_decompose_sigma_orbit(C)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:240:    print(f"  block angles (deg) — predict K_1=12, K_7=84, K_11=132, K_13=156:")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:241:    for label, blk in [("K_1", rep.block_K1), ("K_7", rep.block_K7),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/sigma_orbit_basis.py:242:                        ("K_11", rep.block_K11), ("K_13", rep.block_K13)]:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/architecture/PARALLEL_SEARCH_ARCHITECTURE.md:32:**ARIA equivalent:** The 600-cell polytope. 1200 faces activate simultaneously from a frequency spectrum. Cell activations (600 cells) are population statistics over groups of 4 faces. This is already parallel — it just needs to run on GPU for speed.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/wo/WO-KURAMOTO-001.md:43:Natural frequencies: the carriers are the H4 Coxeter spectrum. H4 has Coxeter number `h=30` and exponents `{1, 11, 19, 29}`. The positive carriers are `m=1` and `m=11`; `29` and `19` are their conjugate reverse-frequency partners. With the existing 40 ms cognitive tick split into 8 S7 microsteps, the microstep is 5 ms and the carriers map to:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/wo/WO-KURAMOTO-001.md:50:Initial phases: deterministic from the chosen Coxeter element's two invariant planes. Phase 1 must derive the Coxeter element by deterministic scan for order-30 eigen-spectrum, not by treating `sym_idx=365` as a new magic constant. For each vertex coordinate `x_v`, initialise theta and gamma phases from the angle of `x_v` projected into the corresponding Coxeter plane.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/unified_trainer.py:31:from raw_sensory import text_to_raw_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/unified_trainer.py:43:    from games.frequency_eval import game_to_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/unified_trainer.py:183:                spec = text_to_raw_spectrum(text)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/unified_trainer.py:212:                    # Get spectrum from position
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/unified_trainer.py:300:                        # Get spectrum — name-hashed categorisation (Rust
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/unified_trainer.py:375:            spec = text_to_raw_spectrum(text)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:29:ratio and the 12-fold ICA prediction) so the research exists on paper
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:42:4. **Beauty** (Thread 4) — golden ratio literally in the adjacency spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:178:> The ARIA substrate is a 120-vertex graph with uniform degree 12. Its slowest non-trivial coupling mode has rate (12 − 6φ), where φ is the golden ratio.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:182:>     1 + (D/α)(12 − 6φ)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:263:> Hint: it's exactly in the adjacency spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:273:**Numerical anchor**: Adjacency eigenvalues {12, 6φ, 4φ, 3} with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:283:> It was never a metaphor. It's literally in the adjacency eigenvalues of a specific 4D polytope: {12, 6φ, 4φ, 3}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:293:> The 600-cell polytope has 120 vertices with a 720-edge adjacency graph. The adjacency matrix A has top eigenvalues:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:296:> λ₂ = 6φ ≈ 9.708 (mult 4)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:297:> λ₃ = 4φ ≈ 6.472 (mult 9)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:307:> So H₄-invariant operators (including adjacency) have eigenvalues in Z[φ].
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:311:> • top_8_eigenvalues = [12.000, 9.708, 9.708, 9.708, 9.708, 6.472, 6.472, 6.472]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:313:> 9.708 = 6φ exact. 6.472 = 4φ exact. Not fitted. Not tuned. Group theory.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:316:> When biology shows φ-scaling, it's not a cosmic coincidence. It's compatible with a specific geometric substrate having φ in its natural spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:505:**Defensive ref**: §B Derivation B for the 12-ICA prediction;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:652:self-adjoint and positive. Its eigenmodes and eigenvalues set the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:657:L has eigenvalues 12 − λ(A), where λ(A) ∈ {12, 6φ, 4φ, 3, …} with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:660:Therefore the Laplacian spectrum is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:663:λ(L) ∈ {0, 12 − 6φ, 12 − 4φ, 9, …}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:670:The smallest non-zero eigenvalue of M is therefore α + D·(6/φ²). This
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:708:non-trivial Laplacian eigenvalue mode (the "Fiedler vector" direction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:747:eigenmode aligned with the A/B partition (eigenvalue λ_AB = 12 − 6φ
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:776:                = 1 + (D/α)·(12 − 6φ)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:789:r_ana / r_awake = 1 + (12 − 6φ) = 13 − 6φ = 10 − 3√5 ≈ 3.292
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:795:r_ana / r_awake = 1 + 0.87·(12 − 6φ) = 1 + 0.87·2.292 ≈ 2.99
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:806:switching-rate ratio equals 1 + (D/α)·(12 − 6φ) — is constrained by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:807:the 600-cell's Laplacian spectrum, which is itself fixed by H₄
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:822:2. The 6/φ² eigenvalue is for the bare 600-cell. D₄ coupling at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:824:   spectrum. Recomputing gives λ_1_eff ≈ 2.7 vs bare 2.29 — shifts the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:832:4. The "A/B is aligned with a Laplacian eigenmode of eigenvalue
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:833:   12 − 6φ" claim relies on the canonical Coxeter-projection partition.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:840:not a fit parameter. It is (12 − 6φ) plus 1, equals 13 − 6φ, equals
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:848:600-cell's first non-trivial Laplacian eigenvalue, 12 − 6φ ≈ 2.29.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:855:## Derivation B — The 12-channel ICA prediction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:935:fibre (rather than by full H₄ irrep) gives the coarser 12-fold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:982:1. The 12-count assumes broadband input. Narrowband or task-locked
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md:1036:| 7 | Pletzer 2010 φ-ratios in EEG bands | Eigenvalues {12, 6φ, 4φ, 3} of 600-cell adjacency | 4 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dodec120_monitor.py:125:    def spectrum(self) -> np.ndarray:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dodec120_monitor.py:126:        return np.asarray(self._rust.spectrum(), dtype=np.float64)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dodec120_monitor.py:160:    def set_sigma_galois_permutation(self, perm: np.ndarray) -> None:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dodec120_monitor.py:164:        self._rust.set_sigma_galois_permutation(arr.astype(np.uint16).tolist())
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dodec120_monitor.py:165:        self._sigma_galois_perm = arr.copy()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dodec120_monitor.py:167:    def apply_sigma_galois_step(self) -> None:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dodec120_monitor.py:168:        self._rust.apply_sigma_galois_step()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dodec120_monitor.py:170:    def exchange_with_sigma_conjugate(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dodec120_monitor.py:176:            raise ValueError("exchange_with_sigma_conjugate: self == other")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/self_model_stream.py:72:    profile: str = "K_7_only"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/self_model_stream.py:242:    profile: str = "K_7_only",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/self_model_stream.py:277:    rep_steady = run_recurrent_session(stream_steady, eta=0.20, profile="K_7_only")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/self_model_stream.py:278:    rep_flicker = run_recurrent_session(stream_flicker, eta=0.20, profile="K_7_only")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/wo/WO-CONSCIOUSNESS-SUBSTRATE-SPEC.md:34:) + sigma[n] sqrt(dt) T_{q_v[n]}(eps_v[n])).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/wo/WO-CONSCIOUSNESS-SUBSTRATE-SPEC.md:153:sigma[n]    = sigma0     exp(clip(w_s . r[n],   -0.3, 0.3))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/wo/WO-CONSCIOUSNESS-SUBSTRATE-SPEC.md:167:sigma0=0.00 for deterministic tests or 0.01 for stochastic tests,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/wo/WO-CONSCIOUSNESS-SUBSTRATE-SPEC.md:181:Reduction condition: if `gamma_u=0`, `lambda_h0=0`, all modulation weights `w_*=0`, and `sigma0` matches the old run, then `step_non_markovian` must match `step_natural` to numerical tolerance.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/wo/WO-CONSCIOUSNESS-SUBSTRATE-SPEC.md:281:    sigma = params["sigma0"] * np.exp(clip(params["w_sigma"] @ r, -0.3, 0.3))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/wo/WO-CONSCIOUSNESS-SUBSTRATE-SPEC.md:283:    return K_scale, beta_D, sigma, lam_h
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/wo/WO-CONSCIOUSNESS-SUBSTRATE-SPEC.md:289:    K_scale, beta_D, sigma, lam_h = gains_from_r(r, params)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/wo/WO-CONSCIOUSNESS-SUBSTRATE-SPEC.md:319:    if sigma > 0.0:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/wo/WO-CONSCIOUSNESS-SUBSTRATE-SPEC.md:322:                               + sigma * np.sqrt(params["dt"]) * noise)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dimensional_monitor.py:682:          And: 83 mod 17 = 15 (conjugate eigenvalue)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dimensional_monitor.py:714:           q mod p = framework constant (e.g., eigenvalue)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dimensional_monitor.py:749:                # Framework constants: eigenvalues {9, 12, 14, 15}, S⁷=7, E8=8
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dimensional_monitor.py:1996:            lines.append(f"  Ignition: NOT YET (need {12 - len(self.crossed_vertices)} more vertices)")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/training_runner.py:34:from raw_sensory import text_to_raw_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/training_runner.py:45:    from games.frequency_eval import game_to_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/training_runner.py:299:            spec = text_to_raw_spectrum(text)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/training_runner.py:301:            # Mix dimensional perturbation into conversation spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_move_selector.py:37:    Returns (self_spectrum, world_spectrum).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_move_selector.py:73:    # SELF spectrum: our strengths
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_move_selector.py:74:    # SPREAD across all 4 eigenvalue sectors so the S³ projection
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_move_selector.py:90:    # WORLD spectrum: their strengths (spread across all 4 sectors)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_move_selector.py:150:        # Get current world spectrum (doesn't change per candidate move)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_move_selector.py:209:                freq = hash(name) % 1500 + 100  # spread across spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_runtime_adapter.py:35:    from .chess_field_discovery import board_to_discovery_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_runtime_adapter.py:40:    from chess_field_discovery import board_to_discovery_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_runtime_adapter.py:116:        1. Extract base world spectrum (opponent's current state)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_runtime_adapter.py:160:        Uses the 80-component VFD discovery spectrum which captures
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_runtime_adapter.py:167:        # 80-component VFD spectrum — captures spatial field structure
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_runtime_adapter.py:168:        discovery_spec = board_to_discovery_spectrum(board)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_runtime_adapter.py:249:        # Get after-move spectrum for field_fit evaluation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_runtime_adapter.py:271:            spectrum=after_spec,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dimensional_language_bridge.py:16:     - These are mixed into the conversation spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dimensional_language_bridge.py:182:        """Get a frequency spectrum perturbation from the dimensional state.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/dimensional_language_bridge.py:185:        the conversation spectrum before settling.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/theta_clock.py:4:eigenmode (λ=2.29, multiplicity 4, period 4.15 ticks → 6 Hz at 40ms tick).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/theta_clock.py:35:    of the multiplicity-4 λ=2.29 eigenvalue group; combines their
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/theta_clock.py:53:        # Find the slowest non-DC eigenvalue group (λ ≈ 2.29 for 600-cell)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/theta_clock.py:54:        # Group eigenvalues to 3 decimal places
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/theta_clock.py:60:            raise RuntimeError("No non-DC Laplacian eigenvalue found")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/theta_clock.py:62:        # Indices of all eigenvectors sharing this eigenvalue
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/theta_clock.py:68:        self.theta_multiplicity = len(theta_indices)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/theta_clock.py:82:        Uses the multiplicity-4 eigenvectors to compute a 4D analytic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/theta_clock.py:86:        # Project onto all theta eigenvectors: shape (multiplicity,)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:8:    board → extract_chess_signals(board) → chess_to_spectrum(signals)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:9:    → excite_polytope(spectrum) → activated faces → weight vector
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:66:    These feed into the spectrum, NOT into eval directly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:172:def chess_to_spectrum(board: chess.Board) -> FrequencySpectrum:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:179:    spectrum = FrequencySpectrum()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:183:    spectrum.add(200, max(0, 1.0 - signals["king_safety"]), label="king_safety")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:186:    spectrum.add(180, signals["hanging_pieces"], label="threats")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:189:    spectrum.add(425, signals["material_balance"], label="material")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:192:    spectrum.add(280, signals["center_control"], label="center")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:195:    spectrum.add(560, signals["development"], label="development")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:198:    spectrum.add(600, signals["mobility"], label="mobility")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:201:    spectrum.add(550, signals["passed_pawns"], label="passed_pawns")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:204:    spectrum.add(725, signals["tactical_tension"], label="tactics")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:207:    spectrum.add(900, signals["check_pressure"], label="checks")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:210:    spectrum.add(115, signals["game_phase"] * 0.5, label="phase")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:212:    return spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:215:def spectrum_to_eval_weights(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:218:    spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:224:    1. Excite polytope with the chess spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:235:        spectrum=spectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:310:def spectrum_to_cell_weights(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:313:    spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:318:    This is the cell-level equivalent of spectrum_to_eval_weights().
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_frequency_adapter.py:329:        polytope, spectrum, entries,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coxeter_torsion.py:139:        # R^step eigenvalues are e^(2πi · step · k / 30) for k ∈ {0..29}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_longhorizon.py:220:        resumed = lh.open_session("session_2", tick=101, context_spectrum=...)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:327:# Each becomes a frequency component in the spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:330:def board_to_discovery_spectrum(board: chess.Board) -> FrequencySpectrum:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:331:    """Convert a board to a discovery spectrum — NO chess features, just field math.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:337:    Returns ~80 frequency components spanning the full spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:341:    spectrum = FrequencySpectrum()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:399:            spectrum.add(freq, value, label=label)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:405:        spectrum.add(115, min(1.0, field_energy(field) / 500.0), label="global.energy")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:406:        spectrum.add(200, (field_balance(field) + 1.0) / 2.0, label="global.balance")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:407:        spectrum.add(300, field_coherence(global_values), label="global.coherence")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:408:        spectrum.add(725, field_entropy(global_values), label="global.entropy")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:409:        spectrum.add(575, field_resonance(global_values), label="global.resonance")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:410:        spectrum.add(900, field_torsion(field), label="global.torsion")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:414:    spectrum.add(575, min(1.0, legal / 40.0), label="mobility")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:418:    spectrum.add(115, piece_count / 32.0, label="phase")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:420:    return spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:423:def discovery_spectrum_to_cell_weights(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:429:    """Full pipeline: board → field math → spectrum → excite → cell weights.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:431:    This is the discovery version of spectrum_to_cell_weights().
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:437:    spectrum = board_to_discovery_spectrum(board)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/chess_field_discovery.py:439:        polytope, spectrum, entries,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/conversation_brain.py:4:Text input → frequency spectrum → conscious settling (recurrent,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/conversation_brain.py:38:    from frequency_adapter import text_to_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/conversation_brain.py:45:# Each archetype is a spectrum that represents a response TYPE.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/conversation_brain.py:91:        1. Convert text to frequency spectrum (sensory input)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/conversation_brain.py:101:        # Step 1: Sensory input — text to spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/conversation_brain.py:103:            spectrum = text_to_spectrum(text, intent)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/conversation_brain.py:104:            pairs = [(c.frequency, c.energy) for c in spectrum.components]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/conversation_brain.py:130:            "input_spectrum": pairs[:5],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/conversation_brain.py:182:        """Fallback text→spectrum when conversation module not available."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_transport.py:139:def eigenvalue_groups(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_transport.py:142:    """Compute eigendecomposition of symmetric L and group by eigenvalue.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_transport.py:144:    Returns a list of (eigenvalue, eigenvector_matrix) pairs. Each group's
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_transport.py:147:    H₄ irrep (multiplicity = irrep dimension).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_transport.py:152:    tol : two eigenvalues are "the same" if within tol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_transport.py:159:    # numpy eigh returns ascending eigenvalues
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_transport.py:277:               Default mapping (spectrum has 9 groups; indexed 0..8):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_transport.py:296:            self.eig_groups = eigenvalue_groups(self.L_H4, tol=1e-6)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_descent.py:4:`kernel.sigma_orbit_basis`. In that basis, every centralizer operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_descent.py:8:    A_E8 = diag(A_h4, A_sigma_h4)         in σ-orbit cascade basis
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_descent.py:13:    K_1, K_11   → H_4 sub-rung   (Coxeter exponents {1, 11, 19, 29})
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_descent.py:14:    K_7, K_13   → σ(H_4) sub-rung (Coxeter exponents {7, 13, 17, 23})
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_descent.py:21:Note: K_7 (the dominant K-class in v66 phase-drift dynamics) lives
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_descent.py:72:    sigma_block: np.ndarray           # 4×4 lower-right block (should equal σ-image of A_h4)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_descent.py:102:        sigma_block=A_sg,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_descent.py:124:    from kernel.sigma_orbit_basis import descend_e8_to_h4_cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_descent.py:130:        sigma_block=cas.A_sigma_h4,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/cascade_descent.py:184:    for prof_name in ["K_1_only", "K_7_only", "K_11_only", "K_13_only",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:52:    If band_mode_indices is None, uses modes whose eigenvalue is within
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:53:    the φ-band — specifically, modes from each multiplicity group
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:63:        # One representative per multiplicity group, skip DC
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:67:            if m.eigenvalue < 1e-6:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:69:            if m.multiplicity_group in seen_groups:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:71:            seen_groups.add(m.multiplicity_group)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:160:    their eigenvalue. Each distinct eigenvalue = one H₄ irrep class (modes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:161:    within the same eigenvalue carry equivalent copies of the same
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:186:        Must have `.modes` (each with .eigenvalue and .index) and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:192:        multiplicity of degenerate eigenspaces).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:207:    # Group modes by eigenvalue (= irrep class within tolerance).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:208:    # Each group is one H₄ irrep's image in the Laplacian spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:210:    group_keys: List[float] = []  # parallel list of representative eigenvalues
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:215:        lam = float(m.eigenvalue)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_criteria.py:330:    # Groups eigenmodes by eigenvalue (= irrep class) rather than random bipartition.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:4:(`sigma_orbit_basis`) to the existing consciousness measurement layer
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:57:from kernel.sigma_orbit_basis import descend_e8_to_h4_cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:93:    profile: str = "K_7_only",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:105:      4. Group modes by Laplacian eigenvalue (the irrep partition).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:110:    rate, so K_1 (norm 0.59), K_+ (norm 2.18), K_- (norm 0 because K_-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:163:      1. Group K modes by eigenvalue (irrep classes).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:179:    # Group modes by eigenvalue
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:298:    profile: str = "K_7_only",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:309:      modality_label   = band of dominant isotypic eigenvalue (delta/.../gamma)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:338:    total_sq = cas.h4_frobenius ** 2 + cas.sigma_frobenius ** 2 + cas.cross_norm ** 2
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:346:    # Modality: the eigenvalue of the largest isotypic contribution
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:385:    snap_pole = bind_phenomenal_field(res_pole, profile="K_7_only")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/consciousness_binding.py:396:    snap_eq = bind_phenomenal_field(res_eq, profile="K_7_only")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/STATE_AND_NEXT.md:261:    spectrum contains 6φ and 4φ exactly (golden ratio explicit),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:164:    def settle(self, self_spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:165:               world_spectrum: FrequencySpectrum) -> CoherenceState:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:168:        1. Excite SELF field with self_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:169:        2. Excite WORLD field with world_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:182:            self.self_field._polytope, self_spectrum, self.self_field._entries,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:186:            self.world_field._polytope, world_spectrum, self.world_field._entries,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:193:            coupled_self_spectrum = self._couple_fields(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:198:            coupled_world_spectrum = self._couple_fields(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:203:            if coupled_self_spectrum.components:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:206:                for c in self_spectrum.components:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:208:                for c in coupled_self_spectrum.components:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:215:            if coupled_world_spectrum.components:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:217:                for c in world_spectrum.components:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:219:                for c in coupled_world_spectrum.components:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:277:        """Create a coupling spectrum from one field's boundary activations.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:280:        into a frequency spectrum that influences the TARGET field.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:282:        spectrum = FrequencySpectrum()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:297:            spectrum.add(freq, activation * self.coupling, label=f"boundary:{face_id}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:299:        return spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:590:    def evaluate_perturbation(self, self_spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:591:                                world_spectrum: FrequencySpectrum) -> Tuple[float, float]:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_engine.py:604:        state = self.settle(self_spectrum, world_spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:62:N_CATEGORIES_HINT = 4                        # hint only; actual k from W spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:102:    For Mode H's W with SVD spectrum {0.70, 0.70, 0.68, 0.68, 0.23, ...},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:104:    For a flat-W Mode I spectrum, gaps are near zero; defaults to min_k.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:325:        # spectrum toward ζ-zero imaginary parts γ_n, lifting Φ_IIT and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:327:        self.v_sigma_enabled: bool = False
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:328:        self.v_sigma_coupling: float = 0.0
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:329:        self._sigma_permutation: Optional[Dict[int, int]] = None
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:330:        self._sigma_perm_max_distance: float = 0.0
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:333:        # cascade-pentagonal-coxeter-bridge.md: c of order 30, eigenvalues
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:751:            # via Laplacian decay proportional to each eigenmode's eigenvalue
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:764:        if self.v_sigma_enabled:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:765:            self._apply_v_sigma()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2223:    def enable_sigma_coxeter_on_dodec(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2246:                "enable_sigma_coxeter_on_dodec requires "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2281:        self._sigma_coxeter_on_dodec_enabled = True
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2283:    def disable_sigma_coxeter_on_dodec(self) -> None:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2284:        self._sigma_coxeter_on_dodec_enabled = False
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2286:    def enable_sigma_galois_on_dodec(self) -> None:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2301:                "enable_sigma_galois_on_dodec requires "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2309:        v_perm = np.array(self._polytope.icosian_sigma_vertex_permutation(),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2367:        self.dodec_pos.set_sigma_galois_permutation(tet_perm)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2368:        self.dodec_neg.set_sigma_galois_permutation(tet_perm)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2369:        self._sigma_galois_on_dodec_enabled = True
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2370:        self._sigma_galois_max_distance = float(max_d)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2372:    def disable_sigma_galois_on_dodec(self) -> None:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2373:        self._sigma_galois_on_dodec_enabled = False
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2548:        if getattr(self, "_sigma_coxeter_on_dodec_enabled", False):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2551:        if getattr(self, "_sigma_galois_on_dodec_enabled", False):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2552:            self.dodec_pos.apply_sigma_galois_step()   # no-op (sign +1)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2553:            self.dodec_neg.apply_sigma_galois_step()   # σ-twist on D−
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2600:        flow_sigma = diff * (rate / 2.0)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2601:        p_Dp = p_Dp - flow_sigma
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2602:        p_Dn = p_Dn + flow_sigma
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2765:        (slowest non-DC Laplacian eigenmode, multiplicity 4).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2782:    def enable_v_sigma(self, coupling: Optional[float] = None) -> None:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2793:        Theorem III.2 predicts the eigenvalues of T_ζ are the imaginary
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2805:        if self._sigma_permutation is None:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2806:            perm_list = self.monitor.polytope.icosian_sigma_vertex_permutation()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2807:            self._sigma_permutation = {v: perm_list[v] for v in range(120)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2808:            self._sigma_perm_max_distance = 0.27010533974645223
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2809:        self.v_sigma_enabled = True
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2810:        self.v_sigma_coupling = float(coupling)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2812:    def _apply_v_sigma(self) -> None:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2814:        if not self.v_sigma_enabled or self._sigma_permutation is None:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2816:        eps = self.v_sigma_coupling
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2819:        sigma_p = np.array([cell_p[self._sigma_permutation[v]] for v in range(120)])
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2820:        new_p = (1.0 - eps) * cell_p + eps * sigma_p
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2826:                                  # (found by eigenvalue-structure scan; any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2835:        The H₄ Coxeter element c has order 30 with eigenvalues exp(2πi·m/30)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/joint_substrate.py:2885:        The 4D Coxeter matrix R has eigenvalues exp(2πi·m/30) for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/info_rung.py:44:  - η = 0.5 / M_info where M_info = α · 8 + γ (top eigenvalue of L_4cube is 8)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/info_rung.py:101:    L_4cube eigenvalues: {0 (×1), 2 (×4), 4 (×6), 6 (×4), 8 (×1)}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/info_rung.py:141:        spectral_eigval_target : eigenvalue of the 16-dim eigenspace to use.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/info_rung.py:167:                build_adjacency, graph_laplacian, eigenvalue_groups)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/info_rung.py:170:            groups = eigenvalue_groups(L_H4, tol=1e-4)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/info_rung.py:171:            # Find the 16-dim eigenspace at the target eigenvalue
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/info_rung.py:187:        # Top eigenvalue of L_4cube is 8 (for the all-ones-with-signs mode)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/info_rung.py:297:    # 4-cube Laplacian eigenvalue check
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/info_rung.py:299:    print(f"\nL_4cube eigenvalues: {eigs.round(2)}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/info_rung.py:302:        f"4-cube spectrum mismatch: got {eigs}"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/info_rung.py:303:    print(f"  ✓ L_4cube spectrum matches 4-cube graph Laplacian")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_embedding.py:15:    p.icosian_sigma_vertex_permutation()  # 120-vertex σ Hungarian perm
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_embedding.py:222:    sigma_coords = np.array([galois_conjugate_4d(vertex_coords_4d[v])
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_embedding.py:225:        sigma_coords[:, None, :] - vertex_coords_4d[None, :, :], axis=2
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_crystallisation.py:113:    spectrum: FrequencySpectrum              # activation footprint
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_crystallisation.py:241:        decision = cryst.crystallise(candidates, world_spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_crystallisation.py:273:        world_spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_crystallisation.py:301:                candidate, world_spectrum, current_state, policy_blocked)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_crystallisation.py:332:        world_spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_crystallisation.py:341:            candidate.spectrum, world_spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_crystallisation.py:396:        self_spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_crystallisation.py:397:        world_spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/coherence_crystallisation.py:405:        state = engine.settle(self_spectrum, world_spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:37:1. ‖cross-block of A_K1 in icosian basis‖ ≈ 0   (K_1 ∈ H_4 exponents)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:38:2. ‖cross-block of A_K11 in icosian basis‖ ≈ 0  (K_11 ∈ H_4 exponents)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:39:3. ‖cross-block of A_K7‖ ≈ ‖A_K7‖              (K_7 ∉ H_4 — projects to σ(H_4))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:40:4. ‖cross-block of A_K13‖ ≈ ‖A_K13‖            (K_13 ∉ H_4 — projects to σ(H_4))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:120:    A_sigma_h4: np.ndarray            # 4×4 lower-right (σ(H_4) exponent block)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:123:    sigma_norm: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:126:    rel_sigma_fraction: float
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:141:        A_sigma_h4=A_sg,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:144:        sigma_norm=float(np.linalg.norm(A_sg)),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:147:        rel_sigma_fraction=float(np.linalg.norm(A_sg) ** 2 / max(total_sq, 1e-30)),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:155:    Returns (h4_norm, sigma_norm, cross_norm).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:160:    return rep.h4_norm, rep.sigma_norm, rep.cross_norm
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:178:    print(f"\n[icosian_basis] K-class operator decomposition (predict K_1/K_11 are H_4):")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:182:        ("K_1", BETA_PROFILES["K_1_only"]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:183:        ("K_7", BETA_PROFILES["K_7_only"]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:184:        ("K_11", BETA_PROFILES["K_11_only"]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:185:        ("K_13", BETA_PROFILES["K_13_only"]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:191:        h4_dom = rep.rel_h4_fraction > rep.rel_sigma_fraction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:193:              f"{rep.rel_sigma_fraction:<10.4f} {rep.rel_cross_fraction:<10.4f} "
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:196:    print(f"\n[icosian_basis] Predicted H_4-rung operators: K_1, K_11, K+ (since K+ = K_1 ⊕ K_11)")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/icosian_basis.py:197:    print(f"[icosian_basis] Predicted σ(H_4)-rung operators: K_7, K_13, K- (since K- = K_7 ⊕ K_13)")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/lyapunov_selector.py:262:    # with smallest eigenvalue (DC mode = uniform).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/four_substrate_preflight.py:11:Laplacian-eigenvalue block structure of the 600-cell:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/four_substrate_preflight.py:21:L = Δ of the 600-cell edge graph (Laplacian eigenvalues = H₄-irrep
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/four_substrate_preflight.py:76:    # Off-eigenvalue-block vs on-block norm (Φ_irrep partition)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/four_substrate_preflight.py:93:        "eigenvalue_groups": int(len(set(rounded.tolist()))),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/README.md:7:The VFD framework was not designed to model the brain. It was derived from first principles (φ-geometry, E8 root system, 600-cell + 120-cell dual, Hopf fibration, Coxeter projection) to produce a constraint-satisfaction substrate for ARIA. Yet, when that substrate runs, it produces phenomena — set A/B asymmetry, prediction-error-driven settling, B→A anomalies under adversity, 12-fold spectral structure, phase transitions in crystallisation — that map *point-for-point* onto principles mainstream neuroscience has converged on independently over the last forty years.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/README.md:69:- Acquire one EEG dataset (PhysioNet or OpenNeuro — see `05_methodology/`) and run prediction #2 (12-fold band structure) and #4 (DMN B→A correlation).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_RUNG_OBSERVABLES.md:37:Matched 1/f noise (same per-channel spectrum, independent across channels)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_RUNG_OBSERVABLES.md:38:— gives approximately exponential eigenvalue decay with no gap structure.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_RUNG_OBSERVABLES.md:63:- No eigenvalue-index shifts (e.g. testing 2+3 instead of 1+3 because
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_H4_FINGERPRINT.md:21:### H4 (Constant 4 — 12-fold PAC phase preference)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_H4_FINGERPRINT.md:27:(PC1-PC2, PC3-PC4) with eigenvalue structure |log(λ₁/λ₂)| < ε,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_H4_FINGERPRINT.md:72:3. Detrended spectrum = raw - 1/f fit.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_H4_FINGERPRINT.md:73:4. In θ band: pick argmax of detrended spectrum. Require prominence
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_H4_FINGERPRINT.md:91:spectrum null permutation test rejects uniform-null at Holm-corrected
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_H4_FINGERPRINT.md:101:2. **Inferential null:** matched-spectrum 1/f noise generated per
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_H4_FINGERPRINT.md:137:- Primary 12-fold PLV: R₁₂ = |Σ A_γ(t) exp(i·12·φ_θ(t))| / Σ A_γ(t)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_H4_FINGERPRINT.md:140:- Null: phase-shuffled θ-γ alignment; matched-spectrum simulated noise.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PREREG_H4_FINGERPRINT.md:161:(matched-spectrum channel-independent simulated noise).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_H4_FINGERPRINT_DRAFT.md:35:paired-eigenvalue topology (PCA of state trajectories).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_H4_FINGERPRINT_DRAFT.md:273:   - Latent phase-amplitude coupling geometry (C4: 12-fold PAC phase
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_H4_FINGERPRINT_DRAFT.md:275:   - State-trajectory topology (C2: paired 2-torus eigenvalue structure
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_H4_FINGERPRINT_DRAFT.md:381:Test whether cortical trajectories show H₄'s 2+2 paired eigenvalue
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_H4_FINGERPRINT_DRAFT.md:394:### D.3 C4: 12-fold PAC phase preference
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_H4_FINGERPRINT_DRAFT.md:438:| C4 12-fold PAC | R_12 ≫ R_1 | R_12 < R_1 | FALSIFIED |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_H4_FINGERPRINT_DRAFT.md:473:scalp + matched-1/f null. Real cortex shows a smooth eigenvalue decay
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_BASIS_2026-04-29.md:90:of uniform degree 12; the eigenspectrum of its graph Laplacian is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_BASIS_2026-04-29.md:91:{12, 6φ, 4φ, 3} where φ is the golden ratio; the irreducible representations
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_BASIS_2026-04-29.md:95:The σ-Galois automorphism (`kernel/sigma_orbit_basis.py`) gives a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_BASIS_2026-04-29.md:139:  {0, 12-3, 12-6φ, 12-4φ}. Smallest non-zero eigenvalue = 3 (set by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_BASIS_2026-04-29.md:252:**File:** `kernel/sigma_orbit_basis.py`
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_BASIS_2026-04-29.md:257:operator A separates into K_1, K_11 (in H₄ proper) and K_7, K_13 (in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_BASIS_2026-04-29.md:262:`sigma_orbit_basis.py:140-149`.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_BASIS_2026-04-29.md:265:K_7 (which dominates substrate phase dynamics) cleanly from K_13 and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_BASIS_2026-04-29.md:710:`python3 -c "from kernel.sigma_orbit_basis import _self_test; _self_test()"`.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_BASIS_2026-04-29.md:721:- `sigma_orbit_basis.py` — exact cascade decomposition
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:71:## 3. Eigenspectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:73:### Theorem 3 (adjacency eigenvalues contain φ)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:76:eigenvalues of A are:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:78:| eigenvalue | value | multiplicity | golden-ratio form |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:81:| λ₂ | 9.708… | 4 | **6φ** (exactly) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:82:| λ₃ | 6.472… | 9 | **4φ** (exactly) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:89:into blocks indexed by irreducible representations. The eigenvalues
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:91:Z[φ] (the ring Z adjoin φ). The specific values 12, 6φ, 4φ, 3 are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:102:For an adjacency matrix A with eigenvalues {λᵢ}, the participation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:109:For the 600-cell adjacency, the spectrum is dominated by repeating
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:110:low-multiplicity eigenvalues (1, 4, 9, 16, … — perfect squares up
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:115:For a hub-spoke graph where one eigenvalue dominates, PR → 1 as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:176:The multiplicity structure {1, 4, 9, 16, …} of the H₄ irreducible
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:229:2. **Eigenspectrum contains φ** (Theorem 3): golden ratio is not a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:230:   metaphor — it literally appears in the adjacency spectrum. This
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:234:   multiplicity structure. The +79.78σ separation from HCP is thus
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:267:| top eigenvalue | T3 | 12 | 12.000 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:268:| second eigenvalue | T3 | 6φ ≈ 9.708 | 9.708 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:269:| third eigenvalue | T3 | 4φ ≈ 6.472 | 6.472 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:270:| fourth eigenvalue | T3 | 3 | 3.000 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:18:degree 12, eigenvalues {12, 6φ, 4φ, 3} where φ is the golden ratio,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:112:graph Laplacian has eigenvalues {0, 3, 4φ, 6φ, 12} with multiplicities
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:116:the σ-automorphism (`kernel/sigma_orbit_basis.py`), the exponents
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:178:The graph Laplacian L has eigenvalues:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:183:| 3 | 4 | K_29 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:184:| 4φ ≈ 6.472 | 9 | K_19 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:185:| 6φ ≈ 9.708 | 16 | K_11 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:186:| 12 − 4φ ≈ 5.528 | 9 | K_23 (σ-twin) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:187:| 12 − 6φ ≈ 2.292 | 16 | K_17 (σ-twin) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:188:| 12 − 3 = 9 | 4 | K_7 (σ-twin) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:189:| 12 | 1 | K_1 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:192:The K_7 and K_13 modes (σ-twin) dominate substrate phase dynamics
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:193:under typical operating conditions; the K_1 and K_11 modes (H₄-proper)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:202:10⁻¹⁵. The σ-orbit projector basis from `kernel/sigma_orbit_basis.py`
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:206:one ablates a specific K-class contribution (e.g., K_7), the remaining
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:380:snapshot = bind_phenomenal_field(green_kernel_result, profile="K_7_only")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:994:of structure (degree std = 0 by transitivity, eigenvalue spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:995:{12, 6φ, 4φ, 3} by character theory). The σ-distances (−11.58σ on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1124:- profile = "K_7_only"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1146:python3 -c "from kernel.sigma_orbit_basis import _self_test; _self_test()"
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md:1173:| `sigma_orbit_basis.py` | σ-orbit projector basis (machine-precise cascade decomposition) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT.md:15:120 vertices of uniform degree 12, a golden-ratio eigenspectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT.md:16:({12, 6φ, 4φ, 3}), and a 7-rung cascade geometry — all derivable
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT.md:73:the topology, spectrum, and dynamics of the substrate itself,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT.md:81:cells pack maximally, and its adjacency spectrum contains the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT.md:164:- **T7–T8** (eigenspectrum contains φ): The top four eigenvalues of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT.md:165:  A are {12, 6φ, 4φ, 3} with multiplicities {1, 4, 9, 16}, where
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT.md:169:- **T9** (participation ratio): The multiplicity structure of H₄'s
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:19:    .laplacian_spectrum       sorted np array of eigenvalues
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:20:    .adjacency_spectrum       sorted np array of eigenvalues
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:75:    """Return sorted eigenvalues of (adjacency A) and (Laplacian D-A)."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:98:    adjacency_spectrum: np.ndarray
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:99:    laplacian_spectrum: np.ndarray
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:110:    def unique_eigenvalues(self, which: str = "adjacency", dp: int = 4):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:111:        src = self.adjacency_spectrum if which == "adjacency" else self.laplacian_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:117:        """Detect φ-signatures in the adjacency spectrum."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:119:        eigs = self.adjacency_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:129:        # largest eigenvalue (Perron) == degree for regular graphs
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:144:    # Laplacian of singleton has one eigenvalue 0
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:149:        adjacency_spectrum=eigs_A, laplacian_spectrum=eigs_L,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:165:        adjacency_spectrum=eigs_A, laplacian_spectrum=eigs_L,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:190:        adjacency_spectrum=eigs_A, laplacian_spectrum=eigs_L,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:193:            "expected_spectrum_A": "{2, 1/φ, 1/φ, -φ, -φ}",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:194:            "purpose": "First rung where golden ratio appears as eigenvalue.",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:226:        adjacency_spectrum=eigs_A, laplacian_spectrum=eigs_L,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:229:            "expected_spectrum_A": "{5, √5 (×3), 0 (×4), −√5 (×3), −1 (×5)} ??",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:255:        adjacency_spectrum=eigs_A, laplacian_spectrum=eigs_L,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:258:            "expected": "β₅ Laplacian spectrum has eigenvalues {0, 8, 10}.",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:291:        adjacency_spectrum=eigs_A, laplacian_spectrum=eigs_L,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:405:        index=7, fib=13, dim=13, name="F7 L12-E8-plus-Zphi4-translation",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:408:        adjacency_spectrum=eigs_A, laplacian_spectrum=eigs_L,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/fibonacci_ladder.py:423:            "id_A_600cell_low_band": "(9-1)*(12-1)-1 = 87",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/expanded_chess_corpus.py:107:    Strategy: play forward 12-30 plies from random openings, sample
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_dual_search.py:111:def features_to_spectrum(features: Dict[str, float], band_offset: float = 0) -> FrequencySpectrum:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_dual_search.py:112:    """Convert features to frequency spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_dual_search.py:119:    spectrum = FrequencySpectrum()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_dual_search.py:128:            spectrum.add(freq, energy, label=feature)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_dual_search.py:129:    return spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_dual_search.py:175:        our_spectrum = features_to_spectrum(our_features, band_offset=0)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_dual_search.py:176:        their_spectrum = features_to_spectrum(their_features, band_offset=400)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_dual_search.py:178:        # Combined spectrum — both fields on one polytope
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_dual_search.py:180:        for comp in our_spectrum.components:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_dual_search.py:182:        for comp in their_spectrum.components:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:10:  2. Propagation (field evolves through eigenvalue modes)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:40:    activation_to_spectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:101:def features_to_spectrum(features: Dict[str, float]) -> FrequencySpectrum:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:102:    """Convert chess features to a frequency spectrum for polytope excitation.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:109:    spectrum = FrequencySpectrum()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:126:            spectrum.add(freq, energy, label=feature)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:128:    return spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:136:      2. Extract features → spectrum → excite polytope
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:187:        # Extract features → spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:189:        spectrum = features_to_spectrum(features)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:191:        if not spectrum.components:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:196:            self._memory._polytope, spectrum, self._memory._entries,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_engine.py:207:            self._memory._polytope, spectrum, self._memory._entries,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_closure_kernel.py:141:    spectrum away from zero so the inverse is well-defined and the response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_closure_kernel.py:200:    """Eigenvalues and eigenvectors of L_M, sorted by eigenvalue."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_closure_kernel.py:232:    """Group eigenmodes by eigenvalue (isotypic blocks); report each block's
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_closure_kernel.py:244:    # Bin eigenvalues
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_closure_kernel.py:251:            "multiplicity": int(mask.sum()),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_closure_kernel.py:375:              f"mult={d['multiplicity']}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FRAMEWORK_UPDATES.md:144:Plus the spectrum itself (Theorem 8): top eigenvalues
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FRAMEWORK_UPDATES.md:145:{12, 6φ, 4φ, 3}. These values — with golden ratio exactly — are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FRAMEWORK_UPDATES.md:210:   values (degree 12, PR ≈ 68.5, eigenvalues {12, 6φ, 4φ, 3}) are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_bridge.py:66:    spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_bridge.py:74:    result = excite_polytope(polytope, spectrum, entries)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_bridge.py:215:    spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_bridge.py:220:    metrics = compute_field_metrics(polytope, spectrum, entries)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_bridge.py:226:    spectrum = chess_to_spectrum(board_features)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_bridge.py:227:    allocation = compute_and_allocate(polytope, spectrum, entries)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_bridge.py:231:    spectrum = text_to_spectrum(input_text)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_bridge.py:232:    allocation = compute_and_allocate(polytope, spectrum, entries)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_bridge.py:236:    spectrum = driving_to_spectrum(scene)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_search_bridge.py:237:    allocation = compute_and_allocate(polytope, spectrum, entries)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:161:eigenvalues lie in Z[φ].
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:163:### T8 Top eigenvalues contain φ exactly
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:165:The top eigenvalues of A are (verified numerically to 6 decimals):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:166:- λ₁ = 12 (multiplicity 1; trivial rep)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:167:- λ₂ = **6φ** = 3(1 + √5) ≈ 9.708 (multiplicity 4)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:168:- λ₃ = **4φ** = 2(1 + √5) ≈ 6.472 (multiplicity 9)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:169:- λ₄ = 3 (multiplicity 16)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:173:preserve adjacency gives λ₂ = 6φ after normalisation.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:183:For the 600-cell, the spectrum has multiplicities ≈ {1, 4, 9, 16, 25,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:188:2|E| = 1440, giving PR = 120² / 1440 = 10.0 for a diagonal spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:190:But the 600-cell's spectrum is NOT diagonal — it has degeneracy. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:192:multiplicity-weighted structure.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:266:### Theorem-derived (structure + spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:275:| Top eigenvalue 12 | theorem | T8 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:276:| λ₂ = 6φ ≈ 9.708 | theorem | T8 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:277:| λ₃ = 4φ ≈ 6.472 | theorem | T8 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIRST_PRINCIPLES.md:374:> eigenvalues {12, 6φ, 4φ, 3} at multiplicities {1, 4, 9, 16}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_trainer.py:14:  raw_spectrum → unified_settle → propose_response → evaluate → learn
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_trainer.py:33:from raw_sensory import text_to_raw_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_trainer.py:197:                # Sensory: raw text → spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_trainer.py:198:                spec = text_to_raw_spectrum(text)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_trainer.py:264:            spec = text_to_raw_spectrum(text)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/action_encoder.py:9:across all 4 eigenvalue sectors for maximum S³ differentiation.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/action_encoder.py:22:    """Encode a chess MOVE as a frequency spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/action_encoder.py:120:    """Encode a game arena ACTION as a frequency spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/action_encoder.py:163:    """Encode a conversation TURN as a frequency spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:41:    """Result of settling a spectrum on the 600-cell.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:92:        state = brain.settle(spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:133:    def settle(self, spectrum: FrequencySpectrum, social: float = 0.5) -> BrainState:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:134:        """Settle a frequency spectrum using the full unified brain.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:139:        spectrum: FrequencySpectrum from any domain adapter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:143:        pairs = self._spectrum_to_pairs(spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:166:        Each spectrum settles using the SAME persistent brain state,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:180:    def project(self, spectrum: FrequencySpectrum) -> Tuple[List[float], List[float]]:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:181:        """Project a spectrum to S³. Returns (point[4], sectors[4])."""
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:182:        pairs = self._spectrum_to_pairs(spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:188:    def _spectrum_to_pairs(spectrum: FrequencySpectrum) -> List[Tuple[float, float]]:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_adapter.py:190:        return [(c.frequency, c.energy) for c in spectrum.components]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_correspondence.py:181:    # Find slow mode (lowest non-DC eigenvalue) and fast mode (highest eigenvalue)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_correspondence.py:182:    non_dc = [m for m in observer.modes if m.eigenvalue > 1e-6]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_correspondence.py:190:    slow = min(non_dc, key=lambda m: m.eigenvalue)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_correspondence.py:191:    fast = max(non_dc, key=lambda m: m.eigenvalue)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_correspondence.py:201:        notes=f"slow λ={slow.eigenvalue:.2f} × fast λ={fast.eigenvalue:.2f}: PAC={pac:.4f}",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_correspondence.py:231:def test_eigenvalue_multiplicity_structure(observer: SpectralObserver) -> BrainTestResult:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_correspondence.py:234:    multiplicity groups should be non-uniform if W-learning has carved
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_correspondence.py:275:    non_dc = [m for m in observer.modes if m.eigenvalue > 1e-6]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_correspondence.py:283:    sorted_modes = sorted(non_dc, key=lambda m: m.eigenvalue)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_correspondence.py:325:    all_results.append(test_eigenvalue_multiplicity_structure(observer))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/brain_validation/vision_adapter.py:93:            # zero out the DC bin (centre of shifted spectrum)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:60:snapshot =  bind_phenomenal_field(green_kernel_result, profile="K_7_only")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:344:- Architecture profile: K_7_only
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:391:| `kernel/sigma_orbit_basis.py` | σ-orbit projector basis (cascade decomposition) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/00_FIELD_NARRATIVE.md:120:2. **Neural frequency bands have 12-fold structure**: ICA on broadband EEG should resolve 12 independent oscillatory channels, not the conventional 5.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CODEX_REVIEW_PACKAGE.md:12:- **600-cell polytope** (120 vertices, 720 edges, 12-regular, H₄ symmetry) — the main pressure field
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CODEX_REVIEW_PACKAGE.md:22:## 2. Substrate's natural eigenmode spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CODEX_REVIEW_PACKAGE.md:24:600-cell Laplacian has 9 distinct eigenvalues:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CODEX_REVIEW_PACKAGE.md:26:| λ | multiplicity | period T (ticks) | **frequency at 40ms tick** | EEG band |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CODEX_REVIEW_PACKAGE.md:38:λ spectrum contains golden-ratio relationships (12 = 4·3, 6φ in adjacency spectrum, etc.).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CODEX_REVIEW_PACKAGE.md:82:- **Master clock**: no single oscillator serving as reference phase for others. λ=2.29 (6 Hz, θ band, multiplicity 4) is the obvious candidate.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CODEX_REVIEW_PACKAGE.md:114:   - Given we have: correct eigenmode spectrum, working PAC, microstate duration matching literature, but Φ_IIT = 0.01 (very low)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CODEX_REVIEW_PACKAGE.md:126:   - 600-cell eigenspectrum at 40ms naturally produces this
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/04_predictions/README.md:61:- For each independent component, characterise spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/01_literature/06_microtubules_orch_or.md:57:1. Direct measurement of microtubule resonance frequencies at higher resolution than Bandyopadhyay's group; specific search for 12-fold structure (matching Hopf fibres).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CASCADE_FINDINGS.md:2368:### ARIA top-5 eigenvalues: [12.0, 9.71, 9.71, 9.71, 9.71] — four-fold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CASCADE_FINDINGS.md:2374:   deviation = 0 (every vertex has degree 12), and top eigenvalues
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CASCADE_FINDINGS.md:2699:- ARIA: PR = 68.54 — the spectrum is near-flat (H₄ degeneracy
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CASCADE_FINDINGS.md:2700:  creates many near-equal eigenvalues)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CASCADE_FINDINGS.md:2701:- HCP: PR = 19.72 ± 0.6 — the spectrum is hub-dominated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CASCADE_FINDINGS.md:2702:  (few large eigenvalues, long tail)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/03_correspondence/README.md:103:| ICA on 64–256 channel EEG yields 50–100 *meaningful* independent components (Onton et al. 2006). Microstate count is 4–8 with finer-resolution methods extracting more. **[Established empirics]** | $C = 87$ derived as triple-overdetermined from E8 Coxeter structure: $(9-1)(12-1) - 1 = 87$, $3(14+15) = 87$, $\sum(\text{upper Coxeter exponents of E8}) - 1 = 87$. (`dimensional_access.rs:32`.) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:43:Smallest non-trivial graph. Adjacency spectrum {+1, −1}; Laplacian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:44:{0, 2}. First polarity / distinction. Passes `A_spectrum_+1_-1`.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:48:**First appearance of the golden ratio as an eigenvalue.** The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:49:adjacency spectrum of the 5-cycle is `{2, 2cos(2πk/5)}` for k=1..4,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:53:  A-spectrum:  {2, 1/φ (×2), −φ (×2)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:54:  L-spectrum:  {0, 3−1/φ (×2), 3+φ (×2)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:58:Passes `has_1_over_phi_eigenvalue`, `has_neg_phi_eigenvalue`, `has_Perron_2`.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:66:The 3D rung with full H₃ Coxeter symmetry. Classical spectrum:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:69:  A-spectrum:  {5, √5 (×3), −1 (×5), −√5 (×3)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:70:  L-spectrum:  {0, 5−√5 (×3), 6 (×5), 5+√5 (×3)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:73:`√5` is present three times in the adjacency spectrum. Since φ = (1+√5)/2,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:86:  A-spectrum:  {8, 0 (×5), −2 (×4)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:87:  L-spectrum:  {0, 8 (×5), 10 (×4)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:103:  A-spectrum:  {56, 28 (×8), 8 (×35), −2 (×112), −4 (×84)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:104:  L-spectrum:  {0, 28 (×8), 48 (×35), 58 (×112), 60 (×84)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:116:The 87 value is **not** an eigenvalue of the E₈ root-graph Laplacian.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:117:It arises from the *Coxeter element rotation*, whose eigenvalues are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:119:a graph spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:133:The block spectrum is the disjoint union of the two blocks:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:137:  Icosian part: {12, 6φ (×4), 4φ (×9), 3 (×16), 0 (×25),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:141:So F₇'s spectrum **contains the full ARIA-600-cell spectrum {12, 6φ, 4φ, 3}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:142:AND the E₈ root-graph spectrum simultaneously** — the two canonical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:149:- Also: 3(14+15) = 87 ✓ (Laplacian eigenvalues 14 and 15 also sit in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:165:| F₃    | **φ**     | adjacency spectrum {1/φ, −φ}                       |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:166:| F₄    | **√5**    | adjacency spectrum {√5, −√5} (= 2φ−1)              |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:200:α⁻¹ ≈ 137.0361 become statements about the F₇ spectrum:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:202:- **Identity A**  `(9−1)(12−1)−1 = 87`    — from icosian block Laplacian eigenvalues 9 & 12
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:203:- **Identity B**  `3(14+15) = 87`         — from icosian block Laplacian eigenvalues 14 & 15
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:206:Identities A and B use eigenvalue multiplicities sitting in the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:208:`run_13d_ladder_diagnostic_T1_spectrum.py`). Identity C uses the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:209:Coxeter-element phase structure of E₈, not its graph spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:236:   eigenvalue and will not show up in a Laplacian spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/FIBONACCI_LADDER_CONSTRUCTION.md:282:- `run_13d_ladder_diagnostic_T1_spectrum.py` — T1 spectral check
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/01_literature/04_excitation_inhibition_balance.md:22:- **Sohal & Rubenstein (2019)** — *Molecular Psychiatry*. Modern review specifically connecting E/I imbalance to autism spectrum disorders. **[Established]**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/01_literature/09_geometry_of_cognition.md:69:This is a much sharper claim than "the brain is geometric". It is testable: predicted *coordinate symmetry* (12-fold Hopf, not arbitrary 6-fold hexagonal grid), predicted *vertex count* (120 + 600), predicted *transition graph* (E8 root adjacency).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/01_literature/09_geometry_of_cognition.md:71:The grid-cell hexagonal symmetry is *not* the 12-fold Hopf symmetry. This is a tension. VFD predicts either: (a) higher-order regularity beyond hexagonal that has not yet been resolved, or (b) hexagonal grid cells reflect a *projection* of the underlying 12-fold structure — like a 2D shadow of a higher-symmetric 4D object.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/05_methodology/README.md:18:4. **12-channel structure in substrate spectra**: ICA-decompose substrate activity and confirm 12 distinct rhythmic channels. *Cost: days.*
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/02_substrate/README.md:25:├── brain.rs               (423)        ── SpectralComponent, BrainState, settle_spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/01_literature/02_eeg_microstates_ica.md:35:The 12-channel prediction (point 3) is the *sharpest disagreement* with current consensus (5 bands, ~4 microstates) and therefore the cleanest falsification target. See `04_predictions/02_twelve_frequency_bands.md`.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:7:to a spectrum, reflects through the polytope, and checks whether
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:22:        action_spectrum=my_spectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:52:    action_spectrum: FrequencySpectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:56:    """Check whether an action's spectrum is self-consistent.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:62:        polytope, action_spectrum, entries,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:69:def invariant_deltas_to_spectrum(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:76:    measurements and creates a spectrum where each invariant's delta
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:79:    spectrum = FrequencySpectrum()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:81:        return spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:89:        return spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:96:            spectrum.add(freq, energy, label=f"delta:{inv_name}")
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:98:    return spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:106:    action_to_spectrum: Callable,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:119:        action_to_spectrum: Callable(action) -> FrequencySpectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:125:        spectrum = action_to_spectrum(action)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:126:        if not spectrum.components:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/reflection.py:131:            polytope, entries, spectrum,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/raw_sensory.py:30:def text_to_raw_spectrum(text: str) -> List[Tuple[float, float]]:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/raw_sensory.py:31:    """Convert text to frequency spectrum using RAW signal statistics.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/raw_sensory.py:54:    # Frequencies span 80-2200 Hz to cover all 4 eigenvalue sectors.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-driving-adapter/src/lib.rs:8://!   Python: spectrum → polytope → weights
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-driving-adapter/src/lib.rs:13://!   At 5 Hz tick rate, 200ms budget → easily depth 12-15
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:671:    fn icosian_sigma_perm_on_distinct_points(&self) -> Vec<usize> {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:672:        use aria_polytope_core::icosian::{build_set_a, build_distinct_points, sigma_perm_on_distinct_points};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:675:        sigma_perm_on_distinct_points(&pts).into_iter().map(|x| x as usize).collect()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:679:    fn icosian_sigma_vertex_permutation(&self) -> Vec<usize> {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:680:        use aria_polytope_core::icosian::{build_set_a, build_sigma_vertex_permutation};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:682:        build_sigma_vertex_permutation(&a)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:781:    /// Settle a frequency spectrum on the 600-cell. Domain-agnostic.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:786:    fn brain_settle(&self, spectrum: Vec<(f64, f64)>, epsilon_sq: f64)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:789:        use aria_polytope_core::brain::{SpectralComponent, settle_spectrum};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:790:        let components: Vec<SpectralComponent> = spectrum.iter()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:793:        let state = settle_spectrum(&self.inner, &components, epsilon_sq);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:809:    /// Batch settle multiple spectra. Each spectrum is a list of (freq, energy).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:826:    /// Project a frequency spectrum to S³. Returns ([x,y,z,w], [sector_energies]).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:827:    fn brain_project(&self, spectrum: Vec<(f64, f64)>) -> PyResult<(Vec<f64>, Vec<f64>)> {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:828:        use aria_polytope_core::brain::{SpectralComponent, spectrum_to_s3};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:829:        let components: Vec<SpectralComponent> = spectrum.iter()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:832:        let (point, sectors, _s8d) = spectrum_to_s3(&components);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:838:    /// Evaluate a spectrum with temporal depth (Hopf fibre winding).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:841:    fn brain_temporal(&self, spectrum: Vec<(f64, f64)>, epsilon_sq: f64, max_depth: usize)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:846:        let components: Vec<SpectralComponent> = spectrum.iter()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:884:    fn run_brain(&self, spectrum: Vec<(f64, f64)>, num_cycles: usize, epsilon_sq: f64)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:890:        let components: Vec<SpectralComponent> = spectrum.iter()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:918:    fn run_brain_persistent(&mut self, spectrum: Vec<(f64, f64)>, num_cycles: usize)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:924:        let components: Vec<SpectralComponent> = spectrum.iter()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:977:    fn conscious_settle(&self, spectrum: Vec<(f64, f64)>, epsilon_sq: f64,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:984:        let components: Vec<SpectralComponent> = spectrum.iter()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1037:    fn unified_settle(&mut self, spectrum: Vec<(f64, f64)>, max_rec: usize, social: f64)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1043:        let components: Vec<SpectralComponent> = spectrum.iter()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1131:    /// Encode named features into a rich VFD spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1151:    /// Input: list of (action_id, base_score, spectrum) where spectrum is [(freq, energy)].
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1165:                spectrum: spec.iter().map(|&(f, e)| SpectralComponent { frequency: f, energy: e }).collect(),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1546:    fn spectrum(&self) -> Vec<f64> { self.inner.spectrum() }
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1578:    fn set_sigma_galois_permutation(&mut self, perm: Vec<u16>) -> PyResult<()> {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1586:        self.inner.set_sigma_galois_permutation(arr);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1589:    fn apply_sigma_galois_step(&mut self) { self.inner.apply_sigma_galois_step(); }
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1636:    fn install_sigma_galois_permutation(&mut self, perm: Vec<u16>) -> PyResult<()> {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1643:        self.inner.install_sigma_galois_permutation(arr);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1789:    /// K_1 = K_11 = 0.1, K_{11;1,1} = φ⁻⁷ ≈ 0.0344 (forces PAC).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1806:    /// Langevin-noisy integration step.  `sigma=0.0` is bit-identical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1807:    /// to `step`; `sigma>0` adds σ·√dt·N(0,1) Gaussian noise per
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1812:    #[pyo3(signature = (dt, k_1=0.1, k_11=0.1, k_11_11=0.0344, sigma=0.0))]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1814:                  k_11_11: f64, sigma: f64) {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1815:        self.inner.step_noisy(dt, k_1, k_11, k_11_11, sigma);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1825:    #[pyo3(signature = (dt, k_1=0.1, k_11=0.1, k_11_11=0.0344, sigma=0.0))]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1827:                        k_11_11: f64, sigma: f64) {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-pyo3-bindings/src/lib.rs:1828:        self.inner.step_drive_noisy(dt, k_1, k_11, k_11_11, sigma);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:18://!   12. Recurrence: settled vertex → spectrum → re-excite
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:31:use crate::neuromodulation::{NeuromodulatorState, InteroceptiveState, TheoryOfMind, default_mode_spectrum};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:118:    external_spectrum: &[SpectralComponent],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:141:    let spectrum = if brain.interoception.should_default_mode() && external_spectrum.is_empty() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:145:        default_mode_spectrum(&wm, traj, &polytope.vertices)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:147:        external_spectrum.to_vec()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:150:    let mut current_spectrum = spectrum.clone();
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:165:        let (projection, _, _s8d) = crate::brain::spectrum_to_s3(&current_spectrum);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:262:        // 14. Recurrence: convert settled vertex back to spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:263:        let recurrent_spectrum = vertex_to_spectrum(settled_vertex, polytope);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:265:        current_spectrum = blend_spectra(&spectrum, &recurrent_spectrum, recurrence_weight);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:269:        current_spectrum = rotate_spectrum(&current_spectrum, attention_rotation);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:407:fn vertex_to_spectrum(vertex_id: u16, polytope: &Polytope600Cell) -> Vec<SpectralComponent> {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:425:fn rotate_spectrum(spectrum: &[SpectralComponent], rotation: usize) -> Vec<SpectralComponent> {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:426:    if rotation == 0 { return spectrum.to_vec(); }
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:428:    spectrum.iter().map(|c| SpectralComponent { frequency: (c.frequency + shift).max(80.0).min(2200.0), energy: c.energy }).collect()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:550:        let spectrum = vec![
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:554:        let result = unified_settle(&polytope, &spectrum, &mut brain, 0.01, 10, 0.5);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:563:        let spectrum = vec![
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:568:        let result = unified_settle(&polytope, &spectrum, &mut brain, 0.01, 8, 0.5);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:583:        let spectrum = vec![SpectralComponent { frequency: 500.0, energy: 0.7 }];
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:585:        unified_settle(&polytope, &spectrum, &mut brain, 0.01, 5, 0.5);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:611:        let spectrum = vec![SpectralComponent { frequency: 500.0, energy: 0.7 }];
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/unified_brain.rs:614:        unified_settle(&polytope, &spectrum, &mut brain, 0.01, 5, 0.5);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/four_substrate.rs:108:    pub fn install_sigma_galois_permutation(&mut self, perm: [u16; DODEC_N_VERTICES]) {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/four_substrate.rs:109:        self.dodec_pos.set_sigma_galois_permutation(perm);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/four_substrate.rs:110:        self.dodec_neg.set_sigma_galois_permutation(perm);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/four_substrate.rs:144:        self.dodec_pos.apply_sigma_galois_step();   // no-op on Pos
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/four_substrate.rs:145:        self.dodec_neg.apply_sigma_galois_step();   // σ-twist on Neg
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:11://!   - At each depth, the C₁₀ eigenvalue weights the contribution
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:15://! C₁₀ eigenvalues: {0, 1/φ², 3-φ, φ², 2+φ, 4, 2+φ, φ², 3-φ, 1/φ²}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:35:/// C₁₀ eigenvalues for the 10 vertices on a decagonal Hopf fibre.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:36:/// E_k = 2 - 2cos(2πk/10). Symmetric: k and 10-k have the same eigenvalue.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:37:fn c10_eigenvalue(k: usize) -> f64 {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:76:/// 1. Settle the candidate's spectrum → get immediate vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:81:/// 5. Weight by depth_weight(d) × c10_eigenvalue contribution
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:85:    spectrum: &[SpectralComponent],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:92:    let brain_state = brain::settle_spectrum(polytope, spectrum, epsilon_sq);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:192:    fn test_c10_eigenvalues_symmetric() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:194:            let e_k = c10_eigenvalue(k);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:195:            let e_mirror = c10_eigenvalue(10 - k);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:197:                "C₁₀ eigenvalues should be symmetric: E[{}]={} != E[{}]={}",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:222:        let spectrum = vec![
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/temporal.rs:226:        let result = evaluate_with_depth(&polytope, &spectrum, 0.01, 3);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/e8.rs:63:/// The matrix uses golden ratio eigenvalues of the E8 Coxeter element.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/e8.rs:68:/// eigenvalues e^(2πi/30), e^(2πi·11/30), e^(2πi·7/30), e^(2πi·13/30).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/sensory.rs:114:/// Encode features into a rich VFD frequency spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/sensory.rs:243:    fn test_empty_features_produce_spectrum() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/sensory.rs:245:        assert!(!spec.is_empty(), "Empty features should produce minimal spectrum");
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:97:    pub current_spectrum: Vec<SpectralComponent>,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:124:            current_spectrum: Vec::new(),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:140:    new_spectrum: &[SpectralComponent],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:143:    let rotated_spectrum = apply_attention_rotation(new_spectrum, medium.attention_state);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:146:    let (point, sectors, _s8d) = crate::brain::spectrum_to_s3(&rotated_spectrum);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:174:    medium.current_spectrum = rotated_spectrum;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:354:/// Apply attention rotation to a spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:357:    spectrum: &[SpectralComponent],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:361:        return spectrum.to_vec();
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:365:    // This shifts WHICH eigenvalue sector each component maps to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:368:    spectrum.iter().map(|c| SpectralComponent {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:520:    if let Some(spectrum) = sensory_input {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:522:            sensory_step(medium, polytope, spectrum);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:551:    spectrum: &[SpectralComponent],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:556:        snapshot = run_cycle(medium, polytope, rates, Some(spectrum));
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:577:        let spectrum = vec![
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:580:        sensory_step(&mut medium, &polytope, &spectrum);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:612:        let spectrum = vec![
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/scheduler.rs:618:        sensory_step(&mut medium, &polytope, &spectrum);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:105:    sigma_galois_perm: Option<Box<[u16; DODEC_N_VERTICES]>>,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:116:            sigma_galois_perm: None,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:144:    pub fn spectrum(&self) -> Vec<f64> {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:212:    pub fn set_sigma_galois_permutation(&mut self, perm: [u16; DODEC_N_VERTICES]) {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:219:        self.sigma_galois_perm = Some(Box::new(perm));
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:224:    pub fn apply_sigma_galois_step(&mut self) {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:226:        let Some(perm) = self.sigma_galois_perm.as_deref() else { return; };
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:370:    #[test] fn sigma_galois_is_noop_on_pos() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:377:        s.set_sigma_galois_permutation(perm);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:379:        s.apply_sigma_galois_step();   // no-op (sign = Pos)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:383:    #[test] fn sigma_galois_applies_on_neg() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:390:        s.set_sigma_galois_permutation(perm);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:393:        s.apply_sigma_galois_step();
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dodec_substrate.rs:436:        s.apply_sigma_galois_step();    // no perm installed → no-op
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:22:/// The four integer eigenvalue sectors of the 600-cell Laplacian.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:28:/// Frequency band boundaries for mapping spectrum → eigenvalue sectors.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:35:/// A frequency component in the input spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:47:    /// Energy distribution across eigenvalue sectors [0..3].
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:51:    /// The 4D point on S³ that the spectrum projected to.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:77:/// Project a frequency spectrum into 8D E8 space via 8 reference frame categories.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:91:/// Each frame maps to one E8 dimension. The spectrum's energy distribution
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:98:pub fn spectrum_to_s3(components: &[SpectralComponent]) -> (Vertex4D, [f64; 4], [f64; 8]) {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:120:    // These are VFD field measurements of the spectrum ITSELF.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:210:/// The main brain function: settle a frequency spectrum on the 600-cell.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:212:/// Input: frequency spectrum (from ANY domain adapter)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:216:pub fn settle_spectrum(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:221:    // Step 1: Project spectrum onto S³
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:222:    let (projection, sector_energies, e8_coords) = spectrum_to_s3(components);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:231:    // The spectrum's 8D E8 coordinates encode 8 reference frame scales
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:359:        .map(|components| settle_spectrum(polytope, components, epsilon_sq))
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:364:/// eigenvalue sector structure. Higher = more concentrated in one sector
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:403:    fn test_spectrum_to_s3_normalised() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:409:        let (point, sectors, _s8d) = spectrum_to_s3(&components);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:444:        let state_a = settle_spectrum(&polytope, &spec_a, 0.01);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:445:        let state_b = settle_spectrum(&polytope, &spec_b, 0.01);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/brain.rs:475:        let state = settle_spectrum(&polytope, &spec, 0.01);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:158:    pub seed_sigma: u32,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:186:        seed_sigma: 617,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:195:    FrameConfig { index: 1, alpha_inv: 79,  consciousness_dof: 47,  seed_sigma: 337,  activation_code: 26567,  s7_aligned: true  },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:196:    FrameConfig { index: 2, alpha_inv: 107, consciousness_dof: 63,  seed_sigma: 449,  activation_code: 47987,  s7_aligned: true  },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:197:    FrameConfig { index: 3, alpha_inv: 137, consciousness_dof: 87,  seed_sigma: 617,  activation_code: 84473,  s7_aligned: true  },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:198:    FrameConfig { index: 4, alpha_inv: 157, consciousness_dof: 95,  seed_sigma: 673,  activation_code: 105605, s7_aligned: true  },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:199:    FrameConfig { index: 5, alpha_inv: 181, consciousness_dof: 107, seed_sigma: 757,  activation_code: 136961, s7_aligned: false },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:200:    FrameConfig { index: 6, alpha_inv: 199, consciousness_dof: 125, seed_sigma: 883,  activation_code: 175661, s7_aligned: false },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:201:    FrameConfig { index: 7, alpha_inv: 223, consciousness_dof: 137, seed_sigma: 967,  activation_code: 215585, s7_aligned: false },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:202:    FrameConfig { index: 8, alpha_inv: 241, consciousness_dof: 155, seed_sigma: 1093, activation_code: 263357, s7_aligned: false },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:656:        assert_eq!(d1, CONSCIOUSNESS_DOF, "derivation 1 (9-1)(12-1)-1 != 87");
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:681:            let expected = frame.alpha_inv * frame.seed_sigma - 56;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:686:            let sigma = 7 * frame.consciousness_dof + 8;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:687:            assert_eq!(frame.seed_sigma, sigma,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/dimensional_access.rs:688:                "Frame {} seed sigma mismatch", frame.index);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/polytope.rs:57:    /// unchanged (brain::settle_spectrum, temporal::evaluate_with_depth).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/polytope.rs:142:        // (brain::settle_spectrum, temporal::evaluate_with_depth) that
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/cortex.rs:10://!    Rest get zeroed. Typical: 1-2 per fibre = 12-24 out of 120.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:21://! produces a vertex. That vertex converts BACK to a spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:22://! The spectrum re-excites the polytope. Each pass rotates attention
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:39:/// Frequency band centers for the 4 eigenvalue sectors.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:40:/// Used to convert a vertex BACK to a spectrum (the recurrent step).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:81:///   1. Excite polytope with current spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:85:///   5. Convert settled vertex BACK to spectrum (recurrence)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:86:///   6. Blend recurrent spectrum with external input (attention)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:92:    external_spectrum: &[SpectralComponent],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:101:    let mut current_spectrum = external_spectrum.to_vec();
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:117:        let (projection, _sectors, _s8d) = crate::brain::spectrum_to_s3(&current_spectrum);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:178:        // Step 5-6: RECURRENCE — convert settled vertex back to spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:180:        let recurrent_spectrum = vertex_to_spectrum(settled_vertex, polytope);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:185:        current_spectrum = blend_spectra(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:186:            external_spectrum, &recurrent_spectrum, recurrence_weight);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:191:        current_spectrum = rotate_spectrum(&current_spectrum, attention_rotation);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:257:/// Convert a settled vertex BACK to a frequency spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:260:/// The vertex's 4D coordinates on S³ map to the 4 eigenvalue sectors.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:262:fn vertex_to_spectrum(vertex_id: u16, polytope: &Polytope600Cell) -> Vec<SpectralComponent> {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:301:/// Apply attention rotation to a spectrum by shifting frequencies.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:302:fn rotate_spectrum(spectrum: &[SpectralComponent], rotation: usize) -> Vec<SpectralComponent> {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:303:    if rotation == 0 { return spectrum.to_vec(); }
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:305:    spectrum.iter().map(|c| SpectralComponent {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:354:/// Each candidate spectrum represents one possible future.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:384:        let spectrum = vec![
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:389:            &polytope, &spectrum, &empty_weights(), 0.01, 10, 3);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:399:        let spectrum = vec![
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:403:            &polytope, &spectrum, &empty_weights(), 0.01, 5, 2);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:413:        // Complex spectrum should trigger cross-fibre activation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:414:        let spectrum = vec![
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:420:            &polytope, &spectrum, &empty_weights(), 0.01, 8, 4);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:429:        let spectrum = vec![
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:434:            &polytope, &spectrum, &empty_weights(), 0.01, 5, 2);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/conscious.rs:441:            &polytope, &spectrum, &weights, 0.01, 5, 2);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:202:/// Returns a "default mode spectrum" that feeds back into the brain.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:203:pub fn default_mode_spectrum(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:210:    let mut spectrum = Vec::new();
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:219:            spectrum.push(SpectralComponent {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:231:            spectrum.push(SpectralComponent {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:238:    if spectrum.is_empty() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:240:        spectrum.push(SpectralComponent { frequency: 300.0, energy: 0.05 });
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:243:    spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:260:    /// Estimated intent (which sector dominates their spectrum).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:278:    /// The action spectrum is what we can observe about their state.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:281:        other_action_spectrum: &[crate::brain::SpectralComponent],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:283:        // Project their spectrum to see which sector they're in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:284:        let (_, sectors, _s8d) = crate::brain::spectrum_to_s3(other_action_spectrum);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:380:    fn test_default_mode_produces_spectrum() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/neuromodulation.rs:384:        let spec = default_mode_spectrum(&wm, &traj, &vertices);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/closure.rs:47:    /// eigenvalue sector. High = clean settling, low = between basins.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/closure.rs:290:/// The 600-cell Laplacian eigenvalues in the integer sector.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/closure.rs:291:/// These are the eigenvalues that decouple and form a closed algebra.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/closure.rs:296:/// Compute the spectral energy of a vertex in the integer eigenvalue sector.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:6://! Domain adapters provide candidate actions, each as a spectrum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:7://! The motor decoder scores each action by how well its spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:34:    pub spectrum: Vec<SpectralComponent>,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:58:    // Project candidate spectrum to S³ and find nearest vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:59:    let (projection, _, _s8d) = crate::brain::spectrum_to_s3(&candidate.spectrum);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:96:    let avg_freq = if candidate.spectrum.is_empty() { 500.0 } else {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:97:        candidate.spectrum.iter().map(|c| c.frequency).sum::<f64>() / candidate.spectrum.len() as f64
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:105:    let has_social = candidate.spectrum.iter().any(|c| c.frequency < 350.0 && c.energy > 0.3);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:124:    let action_energy: f64 = candidate.spectrum.iter().map(|c| c.energy).sum::<f64>()
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:125:        / candidate.spectrum.len().max(1) as f64;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:198:            spectrum: vec![SpectralComponent { frequency: 500.0, energy: 0.7 }],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:211:            spectrum: vec![SpectralComponent { frequency: 200.0, energy: 0.9 }],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:215:            spectrum: vec![SpectralComponent { frequency: 1500.0, energy: 0.9 }],
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:229:            ActionCandidate { id: 0, base_score: 0.2, spectrum: vec![SpectralComponent { frequency: 200.0, energy: 0.5 }] },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:230:            ActionCandidate { id: 1, base_score: 0.8, spectrum: vec![SpectralComponent { frequency: 800.0, energy: 0.5 }] },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:231:            ActionCandidate { id: 2, base_score: 0.5, spectrum: vec![SpectralComponent { frequency: 1400.0, energy: 0.5 }] },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/motor.rs:245:            ActionCandidate { id: 42, base_score: 0.9, spectrum: vec![SpectralComponent { frequency: 500.0, energy: 0.7 }] },
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/lib.rs:56:pub use brain::{SpectralComponent, BrainState, settle_spectrum, batch_settle_spectra, spectrum_to_s3};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:10://! interaction Ξ_{vw} = K_1 Π_1 Im(q_v* q_w) + K_{11} Π_{11} Im(q_v* q_w)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:504:    /// Pair-coupling uses K_1, K_11 (diagonal Kuramoto-like) and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:522:                // Im(q_v* q_w) — used by K_1, K_11 terms
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:524:                // K_1 Π_1 Im(q_v* q_w)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:526:                // K_11 Π_11 Im(q_v* q_w)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:556:    /// `sigma == 0.0` is bit-identical to `step` (explicit branch).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:557:    /// For `sigma > 0`, each Euler step adds σ·√dt·N(0,I₄) Gaussian noise
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:576:        sigma: f64,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:578:        if sigma == 0.0 {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:622:                q_new[k] += sigma * sqrt_dt * z;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:647:        sigma: f64,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:649:        if sigma == 0.0 {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:689:                xi_v[k] += sigma * sqrt_dt * z;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:1017:            // Pair interaction K_1 Π_1 Im(q_v* q_w) should ≈ K_1 sin(δ) n̂_1
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:1039:        o.step(0.01, 0.1, 0.1, 0.02);   // dt=0.01, K_1=0.1, K_11=0.1, K_{11;1,1}=0.02
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:1316:    #[test] fn step_noisy_sigma0_matches_step_bit_for_bit() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:1327:                    "step_noisy(sigma=0) diverged from step at v={} k={}", v, k);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:1332:    #[test] fn step_noisy_sigma_nonzero_deforms() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:1347:            "step_noisy(sigma=0.05) did not deform (max|Δ|={:e})", max_diff);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:1365:    #[test] fn step_drive_noisy_sigma0_matches_step_bit_for_bit() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/h4_oscillator.rs:1375:                "step_drive_noisy(sigma=0) diverged at v={} k={}", v, k);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/kuramoto.rs:177:///   * 480 with trace ≈ −1.618 (different exponent spectrum, not Coxeter)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/kuramoto.rs:210:/// α_m = 2π·m/h.  Thus (C + Cᵀ)/2 has eigenvalue cos(α_m) on this
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:92:    pub fn sigma(self) -> QPhi {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:139:    pub fn norm(self) -> QPhi { self.mul(self.sigma()) }
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:272:    pub fn sigma(self) -> Vertex4DExact {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:273:        Vertex4DExact::new(self.x.sigma(), self.y.sigma(), self.z.sigma(), self.w.sigma())
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:417:    for i in 0..120 { out[i] = set_a[i].sigma(); }
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:427:pub fn sigma_perm_on_distinct_points(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:435:        let sv = v.sigma();
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:446:/// Geometric σ on 4D POINTS is `sigma_perm_on_distinct_points`, which
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:449:pub fn sigma_on_label(id: IcosianId) -> IcosianId { id.flip() }
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:453:pub fn set_a_sigma_fixed_mask(set_a: &[Vertex4DExact; 120]) -> [bool; 120] {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:455:    for i in 0..120 { out[i] = set_a[i].sigma() == set_a[i]; }
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:470:        let sv = v.sigma();
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:491:    let b = v.sigma().to_f64();
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:497:    let a = v.sigma().to_f64();
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:599:pub fn sigma_f64_4d(v: &[f64; 4]) -> [f64; 4] {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:600:    [sigma_f64_scalar(v[0]), sigma_f64_scalar(v[1]),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:601:     sigma_f64_scalar(v[2]), sigma_f64_scalar(v[3])]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:606:fn sigma_f64_scalar(x: f64) -> f64 {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:625:    let s = sigma_f64_4d(v);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:631:    let s = sigma_f64_4d(v);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:775:pub fn build_sigma_vertex_permutation(
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:781:        let s = set_a_exact[i].sigma().to_f64();
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:809:        assert_eq!(QPhi::PHI.sigma(), QPhi::ONE.sub(QPhi::PHI));
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:811:        assert_eq!(QPhi::PHI.sigma().sigma(), QPhi::PHI);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:853:    #[test] fn sigma_permutation_is_involution_on_distinct_points() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:859:        let perm = sigma_perm_on_distinct_points(&pts);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:867:    #[test] fn sigma_fixes_24_rational_points() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:870:        let perm = sigma_perm_on_distinct_points(&pts);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:878:    #[test] fn sigma_transposes_192_phi_points() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:883:        let perm = sigma_perm_on_distinct_points(&pts);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:890:    #[test] fn set_a_sigma_fixed_count() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:892:        let mask = set_a_sigma_fixed_mask(&a);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:1021:        // sigma_on_label(A[i]) = B[i] and coordinates agree with σ on A[i]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:1023:            let flipped = sigma_on_label(IcosianId::a(i));
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:1025:            assert_eq!(b[i as usize], a[i as usize].sigma());
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:1103:    #[test] fn sigma_vertex_permutation_120() {
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/icosian.rs:1107:        let perm = build_sigma_vertex_permutation(&set_a);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-game-adapters/src/mancala.rs:77:                    let opp_pit = 12 - last_pos; // mirror position
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-game-adapters/src/mancala.rs:143:                let opp_idx = 12 - our_pit_idx;

exec
/bin/bash -lc "PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import numpy as np
from kernel.vfd_closure_kernel import build_600cell_graph, compute_graph_laplacian
_, A, edges = build_600cell_graph()
L = compute_graph_laplacian(A)
w = np.linalg.eigvalsh(L)
vals=[]
for x in w:
    if not vals or abs(vals[-1][0]-x)>1e-6:
        vals.append([x,1])
    else:
        vals[-1][1]+=1
print('n', len(w), 'edges', len(edges), 'degree uniq', sorted(set(A.sum(axis=1))))
for val,m in vals:
    print(f'{val:.12f} {m}')
print('sum mult', sum(m for _,m in vals))
PY" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess
 exited 1 in 364ms:
/bin/bash: cannot create temp file for here-document: Read-only file system

exec
/bin/bash -lc "PYTHONDONTWRITEBYTECODE=1 python3 -c \"import numpy as np; from kernel.vfd_closure_kernel import build_600cell_graph, compute_graph_laplacian; _,A,edges=build_600cell_graph(); L=compute_graph_laplacian(A); w=np.linalg.eigvalsh(L); vals=[]
for x in w:
    vals.append([x,1]) if (not vals or abs(vals[-1][0]-x)>1e-6) else vals.__setitem__(-1,[vals[-1][0],vals[-1][1]+1])
print('n',len(w),'edges',len(edges),'degree uniq',sorted(set(A.sum(axis=1))))
for val,m in vals: print(f'{val:.12f} {m}')
print('sum mult',sum(m for _,m in vals))\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess
 succeeded in 1358ms:
n 120 edges 720 degree uniq [12.0]
-0.000000000000 1
2.291796067501 4
5.527864045000 9
9.000000000000 16
12.000000000000 25
14.000000000000 36
14.472135955000 9
15.000000000000 16
15.708203932499 4
sum mult 120

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/vfd_closure_kernel.py' | sed -n '108,150p;214,230p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/kernel/rust_search/crates/aria-polytope-core/src/closure.rs' | sed -n '280,310p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/X_NARRATIVE.md' | sed -n '640,670p;290,310p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 201ms:
   108	
   109	    Edges defined by inner-product condition <v, w> = φ/2 (angle 36°).
   110	    Yields 720 edges, each vertex degree 12.
   111	    """
   112	    if verts is None:
   113	        verts = build_600cell_vertices()
   114	    n = verts.shape[0]
   115	    target = PHI / 2.0
   116	    tol = 1e-3
   117	    A = np.zeros((n, n), dtype=float)
   118	    edges: List[Tuple[int, int]] = []
   119	    for i in range(n):
   120	        for j in range(i + 1, n):
   121	            ip = float(np.dot(verts[i], verts[j]))
   122	            if abs(ip - target) < tol:
   123	                A[i, j] = 1.0
   124	                A[j, i] = 1.0
   125	                edges.append((i, j))
   126	    return verts, A, edges
   127	
   128	
   129	def compute_graph_laplacian(adj: np.ndarray) -> np.ndarray:
   130	    """Standard graph Laplacian L = D − A, D diagonal of degrees."""
   131	    deg = np.diag(adj.sum(axis=1))
   132	    return deg - adj
   133	
   134	
   135	# ─────────────────────── closure operator + response ──────────────────
   136	
   137	def compute_closure_operator(L: np.ndarray, phi: float = PHI) -> np.ndarray:
   138	    """C_φ = L + φ⁻² · I.
   139	
   140	    φ acts as the coherence length / mass regulator. φ⁻² lifts the Laplacian
   141	    spectrum away from zero so the inverse is well-defined and the response
   142	    is bounded.
   143	    """
   144	    n = L.shape[0]
   145	    return L + (1.0 / (phi * phi)) * np.eye(n)
   146	
   147	
   148	def solve_green_response(
   149	    L: np.ndarray,
   150	    source: np.ndarray,
   214	    phi: float = PHI,
   215	) -> np.ndarray:
   216	    """ψ = Σ_n [⟨u_n, f⟩ / (λ_n + φ⁻²)] · u_n.
   217	
   218	    Equivalent to `solve_green_response` but exposes the per-mode amplitudes.
   219	    Useful for compression analysis (which isotypic block dominates).
   220	    """
   221	    coeffs = spectral.eigvecs.T @ source
   222	    weighted = coeffs / (spectral.eigvals + 1.0 / (phi * phi))
   223	    return spectral.eigvecs @ weighted
   224	
   225	
   226	def isotypic_compression(
   227	    spectral: SpectralBlocks,
   228	    source: np.ndarray,
   229	    phi: float = PHI,
   230	    eig_tol: float = 1e-6,

 succeeded in 197ms:
   280	        .map(|p| {
   281	            let result = gradient_flow(p, vertices, epsilon_sq, MAX_FLOW_STEPS, STEP_SIZE);
   282	            let score = result.coherence
   283	                * result.convergence_rate
   284	                * (1.0 - result.residual.min(1.0));
   285	            (result.vertex_id, score)
   286	        })
   287	        .collect()
   288	}
   289	
   290	/// The 600-cell Laplacian eigenvalues in the integer sector.
   291	/// These are the eigenvalues that decouple and form a closed algebra.
   292	/// {9, 12, 14, 15} with multiplicities {16, 25, 36, 16} = 93 modes total.
   293	pub const INTEGER_EIGENVALUES: [f64; 4] = [9.0, 12.0, 14.0, 15.0];
   294	pub const INTEGER_MULTIPLICITIES: [usize; 4] = [16, 25, 36, 16];
   295	
   296	/// Compute the spectral energy of a vertex in the integer eigenvalue sector.
   297	/// This uses the heat kernel trace: Z(t) = Σᵢ mᵢ exp(-λᵢ t)
   298	/// at a characteristic time t = 1/φ (the fundamental timescale).
   299	pub fn vertex_spectral_energy(vertex_id: u16, _vertices: &[Vertex4D]) -> f64 {
   300	    let phi = (1.0 + 5.0_f64.sqrt()) / 2.0;
   301	    let t = 1.0 / phi;
   302	
   303	    let mut energy = 0.0;
   304	    for (i, &lambda) in INTEGER_EIGENVALUES.iter().enumerate() {
   305	        let mult = INTEGER_MULTIPLICITIES[i] as f64;
   306	        energy += mult * (-lambda * t).exp();
   307	    }
   308	
   309	    energy
   310	}

 succeeded in 277ms:
   290	> The pattern demanded an object.
   291	
   292	**3/7 — the theorem:**
   293	> The 600-cell polytope has 120 vertices with a 720-edge adjacency graph. The adjacency matrix A has top eigenvalues:
   294	>
   295	> λ₁ = 12 (mult 1)
   296	> λ₂ = 6φ ≈ 9.708 (mult 4)
   297	> λ₃ = 4φ ≈ 6.472 (mult 9)
   298	> λ₄ = 3 (mult 16)
   299	>
   300	> Where φ = (1+√5)/2.
   301	
   302	**4/7 — why φ appears:**
   303	> The 600-cell's symmetry group H₄ has 2I (the binary icosahedral group) in its structure. 2I is SL(2, F_5) of order 120.
   304	>
   305	> Its character table has entries in Z[φ] — the integers extended by the golden ratio.
   306	>
   307	> So H₄-invariant operators (including adjacency) have eigenvalues in Z[φ].
   308	
   309	**5/7 — what's verified:**
   310	> Numerically, to 6 decimals:
   640	
   641	```
   642	dp/dt = −α·p − D·L·p + σ·η(t)
   643	```
   644	
   645	where:
   646	- α > 0 is the local relaxation rate (vertex-level pressure leak)
   647	- D ≥ 0 is the graph-diffusion coefficient
   648	- L = d·I − A is the graph Laplacian (d = 12, A is adjacency)
   649	- η(t) is unit spatial white noise
   650	
   651	The full generator is the operator M = α·I + D·L on ℝ¹²⁰, which is
   652	self-adjoint and positive. Its eigenmodes and eigenvalues set the
   653	dynamics.
   654	
   655	### A.2 Spectrum of M
   656	
   657	L has eigenvalues 12 − λ(A), where λ(A) ∈ {12, 6φ, 4φ, 3, …} with
   658	multiplicities {1, 4, 9, 16, …} (Theorem 3, `MATHEMATICAL_APPENDIX.md`).
   659	
   660	Therefore the Laplacian spectrum is
   661	
   662	```
   663	λ(L) ∈ {0, 12 − 6φ, 12 − 4φ, 9, …}
   664	     = {0, 6(2 − φ), 4(3 − φ), 9, …}
   665	     = {0, 6/φ², …}
   666	```
   667	
   668	using the golden-ratio identity 1/φ² = 2 − φ.
   669	
   670	The smallest non-zero eigenvalue of M is therefore α + D·(6/φ²). This

exec
/bin/bash -lc "rg -n \"(top eigenvalues|Laplacian|eigenvalues|multiplicities|12, 6φ|600-cell)\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 259ms:
4:structure, derived from the 600-cell polytope and its symmetry group
12:The substrate is the vertex graph of the **600-cell** (Schläfli
22:one cell (tetrahedron) of the 600-cell.
30:The 600-cell has exactly:
45:The H₄ group acts transitively on the 120 vertices of the 600-cell.
61:The 600-cell's degree std = 0 is therefore the **maximum-symmetry
73:### Theorem 3 (adjacency eigenvalues contain φ)
75:Let A be the 120×120 adjacency matrix of the 600-cell. The top
76:eigenvalues of A are:
87:**Proof sketch**: The 600-cell's vertex set is an orbit of H₄. The
89:into blocks indexed by irreducible representations. The eigenvalues
91:Z[φ] (the ring Z adjoin φ). The specific values 12, 6φ, 4φ, 3 are
102:For an adjacency matrix A with eigenvalues {λᵢ}, the participation
109:For the 600-cell adjacency, the spectrum is dominated by repeating
110:low-multiplicity eigenvalues (1, 4, 9, 16, … — perfect squares up
118:The 600-cell's PR = 68.54 ≈ N/√3 reflects the **full-rank non-
139:summing to 120. The shells are **A₅-orbits on the 600-cell minus v₀**.
143:are indexed by geodesic distance on the 600-cell's 1-skeleton.
150:The 120 vertices of the 600-cell decompose into **5 disjoint 24-cell
159:**Proof**: The 600-cell inscribes five 24-cells (equivalently,
191:For the 600-cell with degree 12 and diffusion rate 0.2, each spike

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md' | sed -n '70,120p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 270ms:
    70	
    71	## 3. Eigenspectrum
    72	
    73	### Theorem 3 (adjacency eigenvalues contain φ)
    74	
    75	Let A be the 120×120 adjacency matrix of the 600-cell. The top
    76	eigenvalues of A are:
    77	
    78	| eigenvalue | value | multiplicity | golden-ratio form |
    79	|---|---|---|---|
    80	| λ₁ | 12 | 1 | 12 = 2·6 |
    81	| λ₂ | 9.708… | 4 | **6φ** (exactly) |
    82	| λ₃ | 6.472… | 9 | **4φ** (exactly) |
    83	| λ₄ | 3 | 16 | 3 |
    84	
    85	where φ = (1+√5)/2 is the golden ratio.
    86	
    87	**Proof sketch**: The 600-cell's vertex set is an orbit of H₄. The
    88	adjacency matrix decomposes under the regular representation of H₄
    89	into blocks indexed by irreducible representations. The eigenvalues
    90	are computed from the character table, which contains entries in
    91	Z[φ] (the ring Z adjoin φ). The specific values 12, 6φ, 4φ, 3 are
    92	character sums for the relevant representations.
    93	
    94	**Empirical match**: computed directly,
    95	```
    96	top 8 eigvals = [12.000, 9.708, 9.708, 9.708, 9.708, 6.472, 6.472, 6.472]
    97	```
    98	Verified numerically to 6 decimal places.
    99	
   100	### Theorem 4 (participation ratio lower bound)
   101	
   102	For an adjacency matrix A with eigenvalues {λᵢ}, the participation
   103	ratio is
   104	
   105	```
   106	PR = (Σ|λᵢ|)² / Σλᵢ²
   107	```
   108	
   109	For the 600-cell adjacency, the spectrum is dominated by repeating
   110	low-multiplicity eigenvalues (1, 4, 9, 16, … — perfect squares up
   111	to low order). This gives PR ≈ 68.5.
   112	
   113	**Empirical match**: measured PR = 68.54.
   114	
   115	For a hub-spoke graph where one eigenvalue dominates, PR → 1 as
   116	hub strength increases. For a k-regular random graph, PR ~ N.
   117	
   118	The 600-cell's PR = 68.54 ≈ N/√3 reflects the **full-rank non-
   119	hub structure** imposed by H₄ symmetry.
   120	

codex
**1. Claim Audit**

- Not established: the claimed Laplacian spectrum. [main.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/main.tex:41) and [03_substrate.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/03_substrate.tex:39) present a “full” spectrum whose multiplicities sum to 60, not 120. Local recomputation from `build_600cell_graph` / `compute_graph_laplacian` gives 120 modes: `0^1, 2.2918^4, 5.5279^9, 9^16, 12^25, 14^36, 14.4721^9, 15^16, 15.7082^4`. Source appendix only claims top adjacency eigenvalues, not the full Laplacian spectrum: [MATHEMATICAL_APPENDIX.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:73).
- Established with caveat: 18/18 preregistered tally. Paper says 17/18 standard, 18/18 with N=20 P4 and no threshold changes at [main.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/main.tex:78), matching source [VALIDATION_RESULTS_2026-04-29.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:262).
- Established within model: C×P synergy `+0.190`, CI `[+0.143,+0.239]`, finite bootstrap wording at [06_stress_tests.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/06_stress_tests.tex:95), matching [P4_SYNERGY_FINDING.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:162). But the broad recommendation “interaction terms ... require N≥20” is stronger than one system warrants: [06_stress_tests.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/06_stress_tests.tex:157).
- Established only as single-seed companion signatures: 6/6 table at [05_results.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/05_results.tex:34) matches [CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:197). Do not call them “independent” as in [01_introduction.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:29).
- Overstated: “stimulus models ... are not tuned to specific signatures” at [04_consciousness_chain.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/04_consciousness_chain.tex:149). Source says v4 was reached after five iterations to close v3 failures: [CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:300).
- Overstated: “domain-invariant selective amplifier” remains at [01_introduction.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:65). The abstract correctly limits this to “the two cross-domain tasks tested” at [main.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/main.tex:123).

**2. Internal Consistency**

- Abstract tally is correct: 17/18 standard, 18/18 with N=20 P4.
- Thresholds mostly match preregistration. P13 is handled as a refinement: prereg doc says 5-fold CV at `n=25`, threshold `+15pp` [PAPER_PREDICTIONS.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:115); paper discloses LOO reset refinement at [05_results.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/05_results.tex:126).
- Bootstrap wording is correct in the paper: `0/2000`, not `P=0`, at [02_method.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/02_method.tex:143) and [06_stress_tests.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/06_stress_tests.tex:99).
- Round-2 fixes mostly closed. Still open: “six independent” at [01_introduction.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:29), “domain-invariant” at [01_introduction.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:65), and conclusion omits “within the factorial ablation model” for causal identifiability at [10_conclusion.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/10_conclusion.tex:46).

**3. External Consistency / Numerics**

- 6/6 v4 signatures: paper matches source: [05_results.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/05_results.tex:51), [CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:30). Note source internally has a CI typo `[2.50,2.86]` at lines 40/286; paper uses the correct `[2.50,2.53]`.
- 18/18 preregistered: matches [VALIDATION_RESULTS_2026-04-29.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:80).
- C×P: matches source, and paper improves finite-bootstrap language.
- Chess: `+40.6pp`, `n=25`, reset: matches [CROSS_DOMAIN_RESULTS.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:175).
- HCP: `-11.58σ / +79.78σ / +6.80σ` matches [CROSS_DOMAIN_RESULTS.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:357). Paper correctly marks `n=1003` as descriptive in §7; conclusion should say “full-cohort descriptive HCP n=1003” at [10_conclusion.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/10_conclusion.tex:68).

**4. Substrate-Witness Scope Discipline**

Mostly disciplined: no claim that the substrate is consciousness, no uniqueness claim, no Lyapunov delivered, no ACT selection theorem delivered. Strays:
- [08_discussion.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/08_discussion.tex:49): “makes Φ→0” reads theorem-like. Use “is designed to be small.”
- [04_consciousness_chain.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/04_consciousness_chain.tex:188): “not free dynamical choices” ignores fixed gain constants. Say “mechanism targets are geometry-pinned; gains are fixed design choices.”
- [08_discussion.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/08_discussion.tex:134): clinical analogy is too strong; keep it as hypothesis.

**5. Tightness**

Suggested one-line edits:
- “six independent” → “six companion” at [01_introduction.tex:29](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:29).
- “domain-invariant selective amplifier” → “selective amplifier in the two cross-domain tasks tested” at [01_introduction.tex:65](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:65).
- “not tuned to specific signatures” → “redesigned after diagnostics to use biologically motivated stimulus components, not fitted to subject-level measurements” at [04_consciousness_chain.tex:149](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/04_consciousness_chain.tex:149).
- “require N≥20” → “in this cascade matrix, P4 required N=20; future preregistrations should budget for this scale” at [06_stress_tests.tex:157](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/06_stress_tests.tex:157).

**6. Surface Issues**

- Broken LaTeX: `lemma` environment used at [03_substrate.tex:39](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/03_substrate.tex:39), but no `\newtheorem{lemma}{Lemma}` in [main.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/main.tex:4).
- Cross-domain summary table has a wrong label: “+12.5pp (raw vs null)” at [07_cross_domain.tex:242](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/07_cross_domain.tex:242) is substrate-vs-null, not raw-vs-null.
- HCP clustering σ lacks an HCP standard deviation in the table at [07_cross_domain.tex:173](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/07_cross_domain.tex:173).
- Macro usage for `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` is broadly consistent.

**7. Top Three Fixes**

1. Fix the 600-cell spectrum claim. This is publication-blocking: [main.tex:41](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/main.tex:41), [03_substrate.tex:39](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/03_substrate.tex:39).
2. Remove leftover scope overclaims: “six independent,” “domain-invariant,” and model-level causal language without “within the factorial ablation model.”
3. Fix compile/surface issues: define `lemma`; correct the cross-domain summary label; add clustering sd or drop the σ precision from the table.

**8. Verdict**

Publication ready: no — must-fix list above. The empirical numerics are mostly aligned with the source documents, but the spectrum theorem is wrong as written, and a few round-2 scope fixes remain open.
tokens used
219,292
**1. Claim Audit**

- Not established: the claimed Laplacian spectrum. [main.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/main.tex:41) and [03_substrate.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/03_substrate.tex:39) present a “full” spectrum whose multiplicities sum to 60, not 120. Local recomputation from `build_600cell_graph` / `compute_graph_laplacian` gives 120 modes: `0^1, 2.2918^4, 5.5279^9, 9^16, 12^25, 14^36, 14.4721^9, 15^16, 15.7082^4`. Source appendix only claims top adjacency eigenvalues, not the full Laplacian spectrum: [MATHEMATICAL_APPENDIX.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/MATHEMATICAL_APPENDIX.md:73).
- Established with caveat: 18/18 preregistered tally. Paper says 17/18 standard, 18/18 with N=20 P4 and no threshold changes at [main.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/main.tex:78), matching source [VALIDATION_RESULTS_2026-04-29.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:262).
- Established within model: C×P synergy `+0.190`, CI `[+0.143,+0.239]`, finite bootstrap wording at [06_stress_tests.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/06_stress_tests.tex:95), matching [P4_SYNERGY_FINDING.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:162). But the broad recommendation “interaction terms ... require N≥20” is stronger than one system warrants: [06_stress_tests.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/06_stress_tests.tex:157).
- Established only as single-seed companion signatures: 6/6 table at [05_results.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/05_results.tex:34) matches [CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:197). Do not call them “independent” as in [01_introduction.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:29).
- Overstated: “stimulus models ... are not tuned to specific signatures” at [04_consciousness_chain.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/04_consciousness_chain.tex:149). Source says v4 was reached after five iterations to close v3 failures: [CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:300).
- Overstated: “domain-invariant selective amplifier” remains at [01_introduction.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:65). The abstract correctly limits this to “the two cross-domain tasks tested” at [main.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/main.tex:123).

**2. Internal Consistency**

- Abstract tally is correct: 17/18 standard, 18/18 with N=20 P4.
- Thresholds mostly match preregistration. P13 is handled as a refinement: prereg doc says 5-fold CV at `n=25`, threshold `+15pp` [PAPER_PREDICTIONS.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:115); paper discloses LOO reset refinement at [05_results.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/05_results.tex:126).
- Bootstrap wording is correct in the paper: `0/2000`, not `P=0`, at [02_method.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/02_method.tex:143) and [06_stress_tests.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/06_stress_tests.tex:99).
- Round-2 fixes mostly closed. Still open: “six independent” at [01_introduction.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:29), “domain-invariant” at [01_introduction.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:65), and conclusion omits “within the factorial ablation model” for causal identifiability at [10_conclusion.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/10_conclusion.tex:46).

**3. External Consistency / Numerics**

- 6/6 v4 signatures: paper matches source: [05_results.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/05_results.tex:51), [CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:30). Note source internally has a CI typo `[2.50,2.86]` at lines 40/286; paper uses the correct `[2.50,2.53]`.
- 18/18 preregistered: matches [VALIDATION_RESULTS_2026-04-29.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:80).
- C×P: matches source, and paper improves finite-bootstrap language.
- Chess: `+40.6pp`, `n=25`, reset: matches [CROSS_DOMAIN_RESULTS.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:175).
- HCP: `-11.58σ / +79.78σ / +6.80σ` matches [CROSS_DOMAIN_RESULTS.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:357). Paper correctly marks `n=1003` as descriptive in §7; conclusion should say “full-cohort descriptive HCP n=1003” at [10_conclusion.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/10_conclusion.tex:68).

**4. Substrate-Witness Scope Discipline**

Mostly disciplined: no claim that the substrate is consciousness, no uniqueness claim, no Lyapunov delivered, no ACT selection theorem delivered. Strays:
- [08_discussion.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/08_discussion.tex:49): “makes Φ→0” reads theorem-like. Use “is designed to be small.”
- [04_consciousness_chain.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/04_consciousness_chain.tex:188): “not free dynamical choices” ignores fixed gain constants. Say “mechanism targets are geometry-pinned; gains are fixed design choices.”
- [08_discussion.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/08_discussion.tex:134): clinical analogy is too strong; keep it as hypothesis.

**5. Tightness**

Suggested one-line edits:
- “six independent” → “six companion” at [01_introduction.tex:29](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:29).
- “domain-invariant selective amplifier” → “selective amplifier in the two cross-domain tasks tested” at [01_introduction.tex:65](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/01_introduction.tex:65).
- “not tuned to specific signatures” → “redesigned after diagnostics to use biologically motivated stimulus components, not fitted to subject-level measurements” at [04_consciousness_chain.tex:149](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/04_consciousness_chain.tex:149).
- “require N≥20” → “in this cascade matrix, P4 required N=20; future preregistrations should budget for this scale” at [06_stress_tests.tex:157](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/06_stress_tests.tex:157).

**6. Surface Issues**

- Broken LaTeX: `lemma` environment used at [03_substrate.tex:39](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/03_substrate.tex:39), but no `\newtheorem{lemma}{Lemma}` in [main.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/main.tex:4).
- Cross-domain summary table has a wrong label: “+12.5pp (raw vs null)” at [07_cross_domain.tex:242](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/07_cross_domain.tex:242) is substrate-vs-null, not raw-vs-null.
- HCP clustering σ lacks an HCP standard deviation in the table at [07_cross_domain.tex:173](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/07_cross_domain.tex:173).
- Macro usage for `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` is broadly consistent.

**7. Top Three Fixes**

1. Fix the 600-cell spectrum claim. This is publication-blocking: [main.tex:41](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/main.tex:41), [03_substrate.tex:39](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/aria-chess/paper/sections/03_substrate.tex:39).
2. Remove leftover scope overclaims: “six independent,” “domain-invariant,” and model-level causal language without “within the factorial ablation model.”
3. Fix compile/surface issues: define `lemma`; correct the cross-domain summary label; add clustering sd or drop the σ precision from the table.

**8. Verdict**

Publication ready: no — must-fix list above. The empirical numerics are mostly aligned with the source documents, but the spectrum theorem is wrong as written, and a few round-2 scope fixes remain open.
