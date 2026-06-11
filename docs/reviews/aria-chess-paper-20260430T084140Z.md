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
session id: 019ddd8d-bcad-7343-9b81-363c897a1be3
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
warning: Codex could not find bubblewrap on PATH. Install bubblewrap with your OS package manager. See the sandbox prerequisites: https://developers.openai.com/codex/concepts/sandboxing#prerequisites. Codex will use the vendored bubblewrap in the meantime.
codex
I’ll read the WO context first, then the LaTeX and source documents, and I’ll keep this as a referee-style claim/numerics audit rather than editing the files.
  → Read WO context and map required scope constraints
  • Read paper LaTeX and bibliography with line numbers
  • Read source documents and verify headline numerics
  • Cross-check claims, consistency, and LaTeX surface issues
  • Write structured referee review with file-line citations
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 241ms:
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

 succeeded in 243ms:
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
The WO context is explicit: the paper must be a substrate witness, with ACT only as a non-load-bearing bridge. I’m now reading the LaTeX with line numbers and then I’ll cross-check the specific numeric claims against the source markdown.
  ✓ Read WO context and map required scope constraints
  → Read paper LaTeX and bibliography with line numbers
  • Read source documents and verify headline numerics
  • Cross-check claims, consistency, and LaTeX surface issues
  • Write structured referee review with file-line citations
exec
/bin/bash -lc 'wc -l "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 568ms:
  185 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex
  161 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex
  196 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex
  152 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex
  187 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex
  186 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex
  166 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex
  223 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex
  195 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex
  185 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex
   88 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex
  142 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib
 2066 total

exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 333ms:
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
    72	\textbf{P13 (chess LOO lift)} & same & with reset & same & $\geq +15$pp \\
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
   116	\textbf{Brodbeck microstate baseline.} EEG microstate analysis
   117	methodology of Brodbeck et al.~\citep{Brodbeck2012Microstates} is
   118	used as the reference for the propofol continuity-drop signature
   119	(Sig~3).
   120	
   121	\subsection{Statistical methods}
   122	
   123	\textbf{Cascade-$\alpha$ fitting.} Power-law $\alpha$ is fit by
   124	ordinary least squares on the log-CCDF of the cascade-event size
   125	distribution, restricted to the central 80\% mass band (excluding the
   126	bottom 10\% and top 10\% to avoid extreme-tail noise). $R^{2}$ is
   127	reported on the linear fit in log-space. A cascade event is defined
   128	as an attention-vertex shift between consecutive ticks
   129	$\arg\max|\mathrm{state}_{t}|\neq \arg\max|\mathrm{state}_{t-1}|$;
   130	the event size is the $\ell^{1}$ norm of the state-difference vector
   131	at that tick. Zero-size events are excluded.
   132	
   133	\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
   134	estimated by event-resampling bootstrap (500 resamples for the
   135	preregistered cascade-$\alpha$ tests, 2000 resamples for the
   136	$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
   137	preregistered; 42 for the deep-dive.
   138	
   139	\textbf{Bootstrap one-sided $P$-value reporting.} For the C$\times$P
   140	deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
   141	$0/2000$ were below the preregistered floor $+0.10$; we report these
   142	as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
   143	zero-probability statement on a finite resample.
   144	
   145	\textbf{Factorial interaction estimator.} For the $2{\times}2$
   146	ablation conditions $\{----, -C--, --P-, -CP-\}$, the interaction is
   147	\[
   148	\Delta_{CP}
   149	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
   150	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
   151	\]
   152	
   153	\textbf{$\sigma$-distance against external nulls.} For the HCP
   154	comparisons we report
   155	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
   156	on the full $n=1003$ subject distribution.
   157	
   158	\subsection{State-reset protocol}
   159	
   160	The substrate exhibits state drift: across approximately five
   161	successive depth-sweep evaluations the pressure field equilibrates
   162	to a uniform attractor and classification structure collapses to
   163	raw-feature baseline. Multi-trial benchmarks therefore require an
   164	explicit reset between successive evaluations.
   165	\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
   166	re-initialises pressure-field, crossed-vertex, and training state to
   167	canonical baseline. With reset between depth measurements, the chess
   168	LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
   169	substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
   170	preregistered floor). The reset protocol is documented in
   171	\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
   172	generalisable lesson is recorded in \S\ref{sec:limitations}: any
   173	multi-trial benchmark on a non-stationary substrate must specify
   174	state-reset protocol.
   175	
   176	\subsection{Reproducibility commands}
   177	
   178	\begin{itemize}\itemsep=2pt
   179	\item Substrate self-test:
   180	  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
   181	\item Six drug/sleep signatures:
   182	  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
   183	\item C$\times$P synergy $N\!=\!20$ deep-dive:
   184	  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
   185	\item Eighteen preregistered:
   186	  \texttt{python3 run\_preregistered\_validation.py}
   187	  ($\sim 18$\,min).
   188	\item Whole-paper repro:
   189	  \texttt{bash reproduce\_paper\_claims.sh}.
   190	\end{itemize}
   191	
   192	All scripts are deterministic given seeds. Reruns at seed $42$ on the
   193	recurrent layer should reproduce per-condition means in this paper to
   194	4~decimal places. Bootstrap CIs may differ in the 4th decimal due to
   195	NumPy version differences in the bootstrap RNG; the qualitative
   196	verdicts (CI overlaps, $P$-value thresholds) are unaffected.

 succeeded in 355ms:
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
    45	it, this single deterministic structure reproduces eighteen
    46	quantitative correspondences with neuroscience data — preregistered
    47	on 2026-04-18 before any validation run — plus six independent
    48	drug/sleep EEG signatures of conscious vs unconscious states. There
    49	are no fitted shape parameters and no learned weights; only one
    50	condition-dependent self-injection coupling $\eta$ and one substrate
    51	nonlinearity $\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ pinned to the
    52	graph's average degree.
    53	
    54	\noindent\emph{Scope.}
    55	This paper presents an empirical \emph{substrate witness}: it shows
    56	that a geometry-fixed substrate, with no shape parameters tuned to any
    57	neural dataset, is consistent with eighteen preregistered correspondences
    58	and six EEG signatures. It is not a derivation of consciousness, nor a
    59	selection theorem, nor a uniqueness claim for the 600-cell among regular
    60	4-polytopes. The companion adaptive-closure-transport
    61	preprint~\citep{SmartAdaptiveClosureTransport2026} provides the
    62	4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which this substrate
    63	sits as the $L_M$ instance; the selection of the 600-cell as the active
    64	$M$ is treated as conjectural and is not load-bearing here.
    65	
    66	\begin{abstract}
    67	We test whether a geometry-fixed substrate — the 600-cell regular
    68	4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
    69	shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
    70	operator — is consistent with cortical signatures across five
    71	neuroscience domains. Eighteen quantitative predictions were
    72	preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
    73	before any validation run; each has a falsifiable threshold. After
    74	adequate replication ($N\!\geq\!5$ for cascade interaction terms,
    75	$N\!=\!20$ for the highest-variance interaction, and a documented
    76	state-reset protocol for multi-trial benchmarks), all eighteen
    77	predictions pass at empirical thresholds. We additionally report six
    78	independent drug/sleep EEG signatures reproduced on a recurrent
    79	self-model layer above the substrate, on a single deterministic
    80	trajectory at seed~42.
    81	
    82	\noindent\emph{(i) Cortical avalanches.}
    83	Wake cascade-event power-law exponent $\alpha = 2.252$,
    84	$95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$, $n_{\mathrm{events}}=58$).
    85	This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
    86	subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
    87	pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
    88	overlap.
    89	
    90	\noindent\emph{(ii) Drug/sleep state transitions.}
    91	NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
    92	(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
    93	ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$); propofol
    94	continuity drop $+0.066$ (threshold $>\!0.020$); propofol integrated-
    95	information $\Phi$ collapse to $0.33\!\times$ wake (IIT direction
    96	confirmed); recovery deterministically identical to wake. All six
    97	drug/sleep signatures pass at preregistered thresholds.
    98	
    99	\noindent\emph{(iii) Causal mechanism isolation.}
   100	Two of four cascade mechanisms — context rotation $C$ and partial
   101	emission $P$ — are causally significant, and the original
   102	preregistered C$\times$P synergy prediction $\geq +0.10$ closes
   103	decisively at adequate replication: $N\!=\!20$ fresh seeds give a
   104	bootstrap point estimate of $+0.190$ with $95\%$ CI $[+0.143, +0.239]$
   105	(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
   106	below zero, reported as $0.0000$. We document the original $N\!=\!3$
   107	underestimate ($+0.044$) as a Type II false negative and contribute
   108	the $N\!\geq\!20$ minimum as a preregistration-practice recommendation
   109	for high-variance interaction terms.
   110	
   111	\noindent\emph{(iv) Cross-domain selectivity.}
   112	The substrate is a domain-invariant selective amplifier: chess
   113	4-category position classification on 8-dimensional V2 features lifts
   114	$+40.6$ percentage points on leave-one-out at canonical depth
   115	$n\!=\!25$ ticks (raw $53.1\%$ $\to$ substrate-routed $93.8\%$, with
   116	state reset; threshold $\geq\!+15$pp), while conversation utterance
   117	classification at raw $87.5\%$ yields a substrate lift of $-4.4$pp
   118	(threshold $|\cdot| < 10$pp), confirming the substrate amplifies only
   119	where raw features are ambiguous. On HCP brain functional connectivity
   120	(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
   121	descriptive statistics), the H$_4$-transitive substrate is a
   122	maximum-symmetry deterministic null reference: ARIA degree std
   123	$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
   124	on degree homogeneity, $+79.78\sigma$ on participation ratio, and
   125	$+6.80\sigma$ on clustering coefficient.
   126	
   127	\noindent\emph{What we do not claim.}
   128	We do not claim the 600-cell is the unique substrate consistent with
   129	these signatures, nor that other regular 4-polytopes (24-cell, 120-cell)
   130	have been ruled out. We do not derive the $\Ph^{-2}$ floor from
   131	first principles; it is a design-level stability clamp on the
   132	shifted-Laplacian response. The recurrent layer above the substrate
   133	is reported on a single deterministic trajectory; cross-seed CIs on
   134	the per-condition signatures are an explicit strengthening build.
   135	The structural scope of this paper is: \emph{a geometry-fixed
   136	substrate, with no shape parameters tuned to any neural dataset,
   137	is consistent with eighteen preregistered neuroscience
   138	correspondences and six drug/sleep EEG signatures, with all gaps in
   139	the original preregistration closed by methodology refinement and
   140	without modifying any preregistered threshold.}
   141	\end{abstract}
   142	
   143	% =====================================================================
   144	\input{sections/01_introduction.tex}
   145	\input{sections/02_method.tex}
   146	\input{sections/03_substrate.tex}
   147	\input{sections/04_consciousness_chain.tex}
   148	\input{sections/05_results.tex}
   149	\input{sections/06_stress_tests.tex}
   150	\input{sections/07_cross_domain.tex}
   151	\input{sections/08_discussion.tex}
   152	\input{sections/09_limitations.tex}
   153	\input{sections/10_conclusion.tex}
   154	% =====================================================================
   155	
   156	\section*{Acknowledgements}
   157	We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
   158	OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
   159	the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
   160	the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
   161	HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
   162	datasets that made these comparisons possible. Cortical avalanche
   163	methodology follows~\citep{BeggsPlenz2003}; the integrated-information
   164	$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
   165	the propofol microstate comparison uses Brodbeck et
   166	al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
   167	follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
   168	and processed data are released under MIT licence at the project
   169	repository~\citep{ariaChessRepo}.
   170	
   171	\section*{Reproducibility}
   172	The complete pipeline (substrate construction, six-signature
   173	consciousness chain, $N\!=\!20$ C$\times$P deep-dive, eighteen-prediction
   174	preregistered validation, figure regeneration, this paper) is reproducible
   175	from the project repository~\citep{ariaChessRepo} via the included
   176	\texttt{reproduce\_paper\_claims.sh} script. All scripts are
   177	deterministic given seeds; the substrate's spectral decomposition is
   178	cached at module level. Wallclocks: drug/sleep v4 $\sim 30$\,s;
   179	$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
   180	$\sim 18$\,min.
   181	
   182	\bibliographystyle{plainnat}
   183	\bibliography{references}
   184	
   185	\end{document}

 succeeded in 343ms:
     1	% =====================================================================
     2	\section{Introduction}\label{sec:intro}
     3	% =====================================================================
     4	
     5	Theories of consciousness divide into mechanism-driven proposals
     6	(Integrated Information Theory~\citep{Tononi2008,BalduzziTononi2008},
     7	Global Workspace, predictive processing) and structure-driven
     8	proposals (geometric or topological substrates, neural-population
     9	dynamics). The mechanism-driven proposals offer compelling axiomatic
    10	stories but have not yielded preregistered quantitative signatures
    11	that survive on real EEG data. The structure-driven proposals produce
    12	numbers but typically introduce fitted parameters, learned weights,
    13	or domain-specific tuning.
    14	
    15	This paper takes a deliberately constrained third path. Once a
    16	substrate is chosen, we ask which neuroscience phenomena it is
    17	consistent with under \emph{no} shape parameter tuning, no learned
    18	weights, and no domain-specific calibration. The substrate is the
    19	600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
    20	H$_4$ Coxeter symmetry. It has been studied in pure mathematics for
    21	over a century~\citep{CoxeterRegularPolytopes,Weisstein600Cell}; to
    22	our knowledge it has not been proposed before as an empirical
    23	consciousness substrate. We construct $\Rsixhundred$, fix its response
    24	operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
    25	single condition-dependent self-injection coupling $\eta$ and a
    26	single graph-pinned nonlinearity, and test the resulting witness
    27	against eighteen preregistered correspondences plus six independent
    28	drug/sleep EEG signatures.
    29	
    30	\subsection*{What this paper claims}
    31	
    32	We claim a single \emph{substrate witness}: that a geometry-fixed
    33	substrate, with no shape parameters tuned to any neural dataset, is
    34	consistent with eighteen preregistered correspondences (frozen
    35	2026-04-18) and six independent drug/sleep EEG signatures of
    36	conscious vs unconscious states.
    37	
    38	\begin{enumerate}\itemsep=2pt
    39	\item \textbf{Substrate is fixed by group theory once chosen.} Once
    40	  $\Rsixhundred$ is selected, $120$ vertices of uniform degree $12$
    41	  are forced by H$_4$ transitivity, the Laplacian eigenvalues
    42	  $\{0, 3, 4\Ph, 6\Ph, 12\!-\!4\Ph, 12\!-\!6\Ph, 12\!-\!3, 12\}$ in
    43	  their irrep multiplicities are forced by character theory, and
    44	  the response operator $\Cph$ is fully fixed up to the single
    45	  parameter $\Ph^{-2}$ (a stability shift for the inverse map).
    46	\item \textbf{Cortical avalanches.} Wake cascade-event power-law
    47	  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
    48	  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
    49	  (n$=$30 subjects) and ARIA's prior cascade-pipeline CI
    50	  $[2.73, 3.25]$.
    51	\item \textbf{Six drug/sleep signatures.} On a single deterministic
    52	  trajectory at seed $42$: NREM-N3 phenomenal-intensity variance
    53	  collapse to $0.463\!\times$ wake; propofol modality-switching
    54	  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
    55	  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
    56	  recovery deterministically identical to wake; wake cascade-$\alpha$
    57	  in the SOC band.
    58	\item \textbf{Eighteen preregistered correspondences pass.}
    59	  $17/18$ at standard methodology; $18/18$ after a documented
    60	  $N\!=\!20$ deep-dive on the residual high-variance interaction
    61	  test; \emph{no preregistered threshold has been modified}.
    62	\item \textbf{Cross-domain selectivity.} The substrate functions as
    63	  a domain-invariant selective amplifier (chess $+40.6$pp leave-one-out
    64	  lift at depth $n\!=\!25$ ticks; conversation $-4.4$pp lift, within
    65	  preregistered neutrality bounds) and a maximum-symmetry deterministic
    66	  null reference for cortical functional connectivity (HCP $n\!=\!1003$:
    67	  ARIA at $-11.58\sigma$ on degree homogeneity; $+79.78\sigma$ on
    68	  participation ratio).
    69	\end{enumerate}
    70	
    71	\subsection*{What this paper does \emph{not} claim}
    72	
    73	\begin{itemize}\itemsep=2pt
    74	\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
    75	  the unique substrate consistent with these signatures. Other regular
    76	  4-polytopes (the 24-cell, the 120-cell) are an explicit ablation
    77	  build, not a discharged comparison. The 600-cell choice is post-hoc
    78	  motivated by the H$_4$ Coxeter cascade structure and biological
    79	  observables; it is not an a-priori derivation from first principles.
    80	\item \emph{Not a derivation of consciousness.} The substrate witness
    81	  shows quantitative agreement with cortical signatures; it does not
    82	  establish that the substrate \emph{is} consciousness, nor that
    83	  its dynamics implement specific phenomenal content.
    84	\item \emph{Not a selection theorem.} The companion adaptive-closure-
    85	  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
    86	  proposes a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which
    87	  this substrate fills the $L_M$ slot. The selection of the 600-cell
    88	  as the active $M$ is conjectural in that paper and is treated as
    89	  non-load-bearing here. We do not deliver a Lyapunov function on the
    90	  reduced flow, nor a $2I$-equivariance audit of the closure operator,
    91	  nor a formal edge-space decomposition. These are listed as open
    92	  builds in~\S\ref{sec:limitations}.
    93	\item \emph{Not a circuit-level model.} The substrate is at the
    94	  architectural-algorithmic level. We do not identify which neural
    95	  populations implement context rotation or partial emission, only
    96	  that some such mechanisms appear in the substrate's preregistered
    97	  ablation matrix and exhibit strong inter-mechanism coupling.
    98	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
    99	  Laplacian floor $\Ph^{-2} \approx 0.382$ is a design-level
   100	  stability clamp (it makes $\Cph$ strictly positive definite and
   101	  bounds the Green response). It is not derived as a theorem from a
   102	  closure functional. The companion kernel
   103	  document~\citep{SmartAriaClosureKernel2026} discusses its role.
   104	\end{itemize}
   105	
   106	\subsection*{Mapping from numerical results to admissible claims}
   107	
   108	To keep this paper inside the substrate-witness scope, we use the
   109	following claim-boundary discipline. Numerical results
   110	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   111	$\mathcal C_{\mathrm{admissible}}$ by the rule
   112	\[
   113	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow \mathcal C_{\mathrm{admissible}},
   114	\qquad
   115	\mathcal C_{\mathrm{admissible}}
   116	\;=\;\{\text{`consistent with', `inside threshold', `direction confirmed'}\}.
   117	\]
   118	We never write `the substrate \emph{is} cortex' or `derives consciousness'.
   119	A result that lands inside its preregistered threshold licenses a
   120	`consistent with' claim. A result that exceeds the preregistered
   121	threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
   122	$+15$pp floor) licenses `decisively above prereg', not `proves'. A
   123	$\sigma$-distance result against an external null
   124	(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
   125	the biological distribution', not `cortex has drifted from an ideal
   126	polytope'. The claim-boundary rule is summarised in the box below
   127	and applied throughout~\S\ref{sec:results}.
   128	
   129	\medskip
   130	\begin{center}
   131	\fbox{\parbox{0.92\linewidth}{\small
   132	\textbf{What is tested / what is not claimed.}\par
   133	\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
   134	signatures, on a geometry-fixed substrate with one condition-dependent
   135	parameter $\eta$ and one graph-pinned nonlinearity, against published
   136	biological observables.\par
   137	\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
   138	selection theorem on the 4-tuple bridge; circuit-level mechanistic
   139	identification; first-principles derivation of $\Ph^{-2}$ shift;
   140	that cortex \emph{is} the 600-cell.
   141	}}
   142	\end{center}
   143	
   144	\subsection*{Layout}
   145	
   146	\S\ref{sec:method} gives the provenance ledger (preregistration date,
   147	seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
   148	constructs $\Rsixhundred$ and the response operator $\Cph$, with the
   149	$\Ph^{-2}$ shift disclosed as a design-level stability clamp.
   150	\S\ref{sec:chain} adds the recurrent self-model layer above the
   151	substrate (single nonlinearity, single self-injection coupling).
   152	\S\ref{sec:results} reports the empirical tables: six drug/sleep
   153	signatures, eighteen preregistered correspondences, three-way
   154	$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
   155	synergy stress test ($N\!=\!3, 5, 10, 20$ trend with bootstrap
   156	$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
   157	selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
   158	discusses the substrate witness and proposes a non-load-bearing
   159	ACT bridge (without claiming a selection theorem).
   160	\S\ref{sec:limitations} enumerates limitations and the
   161	hostile-review guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 390ms:
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
    35	H$_4$ transitivity then forces:
    36	\begin{lemma}[600-cell graph facts]\label{lem:600cell}
    37	The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, every
    38	vertex has degree exactly $12$, and the unweighted graph Laplacian
    39	$\Lop = D - A$ has spectrum
    40	\[
    41	\sigma(\Lop) \;=\;
    42	\bigl\{0^{1}, 3^{4}, 4\Ph^{9}, 6\Ph^{16}, (12\!-\!4\Ph)^{9},
    43	       (12\!-\!6\Ph)^{16}, 9^{4}, 12^{1}\bigr\},
    44	\]
    45	where the exponent denotes multiplicity. The decomposition into H$_4$
    46	irreducible representations is exact at machine precision; the
    47	$\sigma$-orbit projector basis (\texttt{kernel/sigma\_orbit\_basis.py})
    48	realises it block-by-block with cross-block norm $<10^{-15}$.
    49	\end{lemma}
    50	
    51	The non-trivial eigenmodes partition into Coxeter exponent classes.
    52	For H$_4$ proper, the exponents are $\{1, 11, 19, 29\}$; for the
    53	Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism of
    54	$\mathbb{Z}[\Ph]$, the exponents become $\{7, 13, 17, 23\}$. We label
    55	the eigenspaces $K_{1}, K_{11}, K_{19}, K_{29}$ for H$_4$-proper modes
    56	and $K_{7}, K_{13}, K_{17}, K_{23}$ for $\sigma$-twin modes. The
    57	multiplicities follow from character theory and are reproduced in
    58	the implementation
    59	(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}). The
    60	$K_{7}$-modes will be the dominant phenomenal-binding profile in
    61	\S\ref{sec:chain}.
    62	
    63	\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
    64	
    65	The substrate's linear response to an external source $f \in \mathbb{R}^{120}$
    66	is the discrete Green's function of the shifted Laplacian:
    67	\begin{equation}\label{eq:cphi}
    68	\Cph \;=\; \Lop + \Ph^{-2} I,
    69	\qquad
    70	\psi \;=\; \Cph^{-1} f.
    71	\end{equation}
    72	The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
    73	clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
    74	$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
    75	inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
    76	\emph{not} a derived theorem; it is a stability choice. The companion
    77	kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
    78	$\Cph$ as the basis for an independent passive-regime witness in
    79	flavour physics~\citep{SmartBAnomaly2026}, where the same operator
    80	form (without retuning the shift) describes the
    81	$B\to K^{*}\mu^{+}\mu^{-}$ angular anomaly across five public datasets.
    82	This paper imports $\Cph$ from that line; we do not re-derive it.
    83	
    84	The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
    85	not produce critical-state cascade statistics; the recurrent layer
    86	in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
    87	$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
    88	event distributions. The choice $k\!=\!12$ is the average degree of
    89	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
    90	fitted to any dataset.
    91	
    92	\paragraph{Disclosure (substrate-witness scope).}
    93	The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
    94	The bounded-top-$K$ nonlinearity uses $k\!=\!12$ pinned to the graph's
    95	average degree, not a fitted threshold. No other shape parameter
    96	enters. The condition-dependent self-injection coupling
    97	$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
    98	varies between conditions in~\S\ref{sec:chain}; it is reported
    99	explicitly per condition.
   100	
   101	\subsection{Shell decomposition}\label{ssec:shells}
   102	
   103	Under the H$_3$ subgroup, the $120$ vertices partition into $9$
   104	spherical shells indexed by Euclidean inner product with a chosen pole:
   105	\[
   106	\bigl(|S_0|,\ldots,|S_8|\bigr) \;=\; (1, 12, 20, 12, 30, 12, 20, 12, 1).
   107	\]
   108	The middle shell $S_{4}$ has $30$ vertices on the equatorial plane
   109	(the icosidodecahedral ring). When projecting onto a continuum kernel
   110	in companion preprints~\citep{SmartAriaClosureKernel2026}, the
   111	shell-mean projection of the equatorial-source response,
   112	$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
   113	collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
   114	This paper does not use that continuum projection; we work with the
   115	discrete operator throughout.
   116	
   117	\subsection{Cascade descent (sketch)}\label{ssec:cascade}
   118	
   119	The recurrent layer in~\S\ref{sec:chain} references a cascade
   120	decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
   121	\to S^{7}\to 0$, implemented in
   122	\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
   123	An arbitrary operator on the $E_{8}$ root system descends to the
   124	4-D H$_4$ subspace through a sequence of orthogonal projections, each
   125	preserving the Frobenius norm to within $10^{-15}$. The
   126	$\sigma$-orbit projector basis from
   127	\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
   128	decomposition at machine precision.
   129	
   130	The descent provides numerical stability for the cascade ablations:
   131	when one ablates a specific K-class contribution (e.g.\ $K_{7}$), the
   132	remaining operator structure is exactly preserved. We do not claim
   133	the cascade itself is forced by physics on a pre-substrate level; the
   134	cascade is a decomposition of operators on $\Rsixhundred$, and the
   135	choice of $\Rsixhundred$ as the active substrate is post-hoc justified
   136	by the empirical correspondences in~\S\ref{sec:results}.
   137	
   138	\subsection{What the substrate is fixed-by, and what it is not}
   139	
   140	\begin{itemize}\itemsep=2pt
   141	\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
   142	  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
   143	  irrep block structure, average degree $k\!=\!12$, $\sigma$-twin pairing.
   144	\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
   145	  is not a derivation; it is a design-level clamp that bounds the
   146	  response inverse.
   147	\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
   148	  $24$-cell or $120$-cell. The choice is post-hoc motivated by the H$_4$
   149	  cascade structure and the empirical correspondences. A formal
   150	  ablation against alternative regular 4-polytopes is an open build
   151	  (\S\ref{sec:limitations}).
   152	\end{itemize}

exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 340ms:
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
    67	   Sleep-EDFx $n=30$ CI~$[2.50, 2.86]$~\citep{BeggsPlenz2003,SleepEDFx} &
    68	   $\alpha\!\in\![1.5, 3.5]$, $R^{2}\!>\!0.85$ &
    69	   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
    70	   $\checkmark$ \\
    71	\bottomrule
    72	\end{tabular}
    73	\end{table}
    74	
    75	All six signatures pass at preregistered thresholds on the same
    76	deterministic substrate. The mechanistic readings are recorded in
    77	\texttt{docs/brain\_mapping/CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    78	and are not load-bearing for the headline claim. Single-seed
    79	disclosure: \S\ref{sec:limitations} item~3.
    80	
    81	\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
    82	
    83	\textbf{Tally.} $17/18$ at standard validation
    84	(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
    85	plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
    86	on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
    87	$32000$--$32019$). \emph{No preregistered threshold has been modified.}
    88	
    89	\begin{table}[ht]
    90	\centering
    91	\small
    92	\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
    93	\label{tab:eighteen_prereg}
    94	\begin{tabular}{l l l l l}
    95	\toprule
    96	ID & Test & Threshold & Observed (2026-04-29) & Verdict \\
    97	\midrule
    98	P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
    99	P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
   100	P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
   101	\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
   102	   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
   103	P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
   104	P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
   105	P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
   106	P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
   107	P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
   108	P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
   109	P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
   110	P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
   111	\textbf{P13} & Chess LOO lift (with reset)   & $\geq +15$pp     & $+40.6$pp & $\checkmark$ \\
   112	P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
   113	P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   114	P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
   115	P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
   116	P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
   117	\bottomrule
   118	\end{tabular}
   119	\end{table}
   120	
   121	\textbf{Three predictions that flipped to PASS, with documented
   122	methodology refinement (no threshold change).}
   123	\begin{itemize}\itemsep=2pt
   124	\item P3 (D$\times$C interaction independence) failed at $N\!=\!3$
   125	  ($-0.231$, just outside $|\cdot|\!<\!0.20$ band) and passed at
   126	  $N\!=\!5$ ($-0.183$). Diagnosis: classical Type II false negative
   127	  on a high-per-seed-variance interaction term.
   128	\item P4 (C$\times$P synergy) failed at $N\!=\!3$ ($+0.044$) and at
   129	  $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
   130	  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
   131	  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
   132	\item P13 (chess LOO lift) failed at $+3.1$pp without state reset on
   133	  a state-drifted substrate; with
   134	  \texttt{homeostatic\_reset(level=1.0)} between depth measurements
   135	  (\S\ref{sec:method}, \texttt{NON\_EQUILIBRIUM\_FINDING.md}), the
   136	  lift is restored to $+40.6$pp at the same $\geq +15$pp threshold.
   137	\end{itemize}
   138	
   139	\textbf{Headline verdict.} Eighteen preregistered correspondences
   140	all pass at preregistered thresholds, with two interaction tests
   141	requiring $N\!\geq\!5$ and one requiring $N\!=\!20$ for reliable
   142	detection of high-variance interaction terms, and one test
   143	requiring the documented state-reset protocol. The original $15/18$
   144	result was a methodology-limited tally, not a content failure.
   145	
   146	\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
   147	
   148	The substrate's wake cascade-$\alpha$ confidence interval overlaps
   149	\emph{three independent reference ranges} simultaneously:
   150	
   151	\begin{table}[ht]
   152	\centering
   153	\small
   154	\caption{Three-way $\alpha$ overlap on the wake cascade-event power
   155	law.}
   156	\label{tab:alpha_overlap}
   157	\begin{tabular}{l c l c}
   158	\toprule
   159	Source & $\alpha$ & 95\% CI & $n$ \\
   160	\midrule
   161	ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
   162	Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
   163	ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
   164	\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
   165	\bottomrule
   166	\end{tabular}
   167	\end{table}
   168	
   169	The v4 WAKE 95\% CI $[1.82, 2.86]$ overlaps:
   170	(i) the real Sleep-EDFx EEG CI $[2.50, 2.53]$ (containing the upper
   171	arm of the WAKE CI $[2.50, 2.86]$); (ii) the ARIA prior cascade
   172	pipeline CI $[2.73, 3.25]$; and (iii) the cortical-avalanche
   173	band $\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The shared
   174	overlap interval is $[2.73, 2.86]$, which is non-empty on three
   175	independent measurements at the substrate-witness level.
   176	
   177	\textbf{Reading.} The substrate produces self-organised-critical
   178	cascade statistics matching the cortical-avalanche literature with
   179	no fitted parameter on neural data. The bounded-top-$K$ at
   180	$k=12$ is pinned to the substrate's average degree
   181	(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
   182	stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
   183	biological time-scale parameters but is not measurement-fitted to
   184	any specific subject (\S\ref{sec:chain}). Three-way overlap on the
   185	power-law exponent is the strongest single empirical anchor in the
   186	paper.

 succeeded in 353ms:
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
    76	By construction $\Phi\to 0$ under H$_{4}$-equivariant dynamics, since
    77	group symmetry forbids information transport across irrep classes;
    78	$\Phi > 0$ only when the dynamics break symmetry and transport
    79	information across class boundaries. This is a port of the published
    80	\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
    81	pipeline, adapted to take amplitude trajectories from any source.
    82	
    83	We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
    84	a full implementation of IIT. ARIA does not implement cause-effect
    85	repertoires, exclusion postulate, or integration-over-partitions
    86	machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
    87	collapse in~\S\ref{sec:results} is consistent with the IIT direction
    88	of effect on the propofol-vs-wake state contrast; it is not a
    89	discharge of the IIT axioms.
    90	
    91	\subsection{The continuity composite}
    92	
    93	Implementation:
    94	\texttt{kernel/self\_model\_stream.py:StreamContinuityScorer}.
    95	A composite first-person continuity score over a 64-tick rolling
    96	window:
    97	\begin{align*}
    98	b_{\mathrm{cont}} &= \mathrm{mean\ cos\text{-}sim\ of\ consecutive}\ (I, L, P)\,\mathrm{vectors},\\
    99	v_{\mathrm{cont}} &= 1/(1 + 4\cdot \mathrm{var}(\mathrm{valence})),\\
   100	m_{\mathrm{pers}} &= \mathrm{frac.\ of\ consecutive\ same\text{-}modality\ ticks},\\
   101	i_{\mathrm{smooth}} &= 1/(1 + 4\cdot \mathrm{TV}(\mathrm{intensity})),\\
   102	\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
   103	\end{align*}
   104	This composite produces the propofol continuity-drop signature
   105	(WAKE composite $0.943$; PROPOFOL composite $0.877$;
   106	drop $+0.066$).
   107	
   108	\subsection{The phenomenal-field binding}
   109	
   110	Implementation:
   111	\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
   112	The substrate state $\psi_{t}$ is mapped to a phenomenal snapshot
   113	with channels (intensity $I$, self-luminosity $L$, presence $P$,
   114	valence, modality\_label). The modality\_label is determined by which
   115	H$_4$ K-class dominates the isotypic compression of $\psi_{t}$ under
   116	the $\sigma$-orbit projector basis. The default profile
   117	\texttt{K\_7\_only} restricts to $\sigma$-twin K-classes for modality
   118	labelling; H$_4$-proper classes contribute amplitude bias.
   119	
   120	\subsection{Stimulus models}
   121	
   122	Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
   123	$\times$ $800$ ticks each at seed $42$:
   124	
   125	\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
   126	coherence (small always-on bias), and attention episodes (20--50
   127	ticks at amplitude $0.8$, anchored to the largest shell with $15\%$
   128	within-shell rotation per tick). The AR(1) gives temporal correlation
   129	that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
   130	modality; attention episodes mimic biological visual fixation
   131	(200--400~ms dwell time analogue); within-shell rotation generates
   132	cascade events without changing modality.
   133	
   134	\textbf{SLEEP\_N3.} Slow oscillation ($\sim 1$\,Hz analogue,
   135	amplitude $1.0$) on a coherent shell, plus spindle bursts ($12$ ticks
   136	every $100$ at amplitude $0.4$ fast modulation), plus K-complexes
   137	($4\%$ of ticks at amplitude $0.8$).
   138	
   139	\textbf{PROPOFOL.} Low-amplitude tonic noise (amplitude $0.05$);
   140	$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
   141	background drive.
   142	
   143	\textbf{RECOVERY.} Identical to WAKE — verifies determinism and
   144	reversibility.
   145	
   146	The stimulus models are deliberately structural rather than
   147	measurement-fitted: amplitudes and durations match published
   148	biological time scales but are not tuned to specific signatures.
   149	The full stimulus code is \texttt{demo\_drug\_sleep\_v4.py}. We
   150	disclose stimulus-shape choice as a methodological design move,
   151	not a derived theorem.
   152	
   153	\subsection{Cascade-mechanism ablation matrix}
   154	
   155	The cascade dynamics on the substrate use four mechanisms acting on
   156	the pressure field, each ablatable independently. The $2^{4}$
   157	ablation grid is the basis for the preregistered tests P1--P5 and
   158	the C$\times$P stress test in~\S\ref{sec:stress}.
   159	
   160	\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains
   161	five disjoint 24-cells (D$_4$ orbits). $D$ adds a small
   162	(coupling $0.05$) cross-orbit pressure averaging that prevents
   163	cascades from localising to one orbit.
   164	Implementation: \texttt{kernel/dimensional\_monitor.py:300-305}.
   165	
   166	\textbf{$C$ — Context rotation (S$^{7}$ observer frames).} The active
   167	observer frame on the S$^{7}$ rung rotates periodically based on
   168	which uncrossed vertices have accumulated pressure aligning with
   169	each frame's preferences. This creates churn in \emph{which}
   170	vertices are uncrossed at any tick.
   171	Implementation: \texttt{kernel/dimensional\_monitor.py:316-318, 823-827}.
   172	
   173	\textbf{$P$ — Partial emission.} High-pressure uncrossed vertices
   174	(above threshold but not yet crossed) emit pressure at $30\%$ scale,
   175	saturating at pressure $3.0$. Without this mechanism, only fully-
   176	crossed vertices emit.
   177	Implementation: \texttt{kernel/dimensional\_monitor.py:842-855}.
   178	
   179	\textbf{$E$ — Equator compensation.} The H$_3$ shell-4 equator is a
   180	30-vertex icosidodecahedral ring with split degree distribution.
   181	$E$ scales pressure gain by $(\bar d / d_{v})$ so sparse commissural
   182	vertices overcome their connectivity deficit.
   183	Implementation: \texttt{kernel/dimensional\_monitor.py:320-360}.
   184	
   185	The four mechanisms are pinned to the substrate's geometry (D$_4$
   186	orbits, S$^{7}$ rung, equatorial shell) — they are not free dynamical
   187	choices. Their causal effects are reported in~\S\ref{sec:stress}.

 succeeded in 388ms:
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
    12	threshold required (a) ruling out the $N\!=\!3$ point estimate as a
    13	Type II false negative, (b) confirming the trend across $N$, and
    14	(c) bootstrapping a confidence interval on a fresh-seed $N\!=\!20$
    15	sample. We did all three.
    16	
    17	\subsection{The factorial estimator}
    18	
    19	For the four ablation conditions $\{----, -C--, --P-, -CP-\}$
    20	(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
    21	standard $2\times 2$ factorial difference:
    22	\[
    23	\Delta_{CP}
    24	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
    25	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
    26	\]
    27	Per-seed paired estimates use the same formula on a single seed's
    28	four conditions.
    29	
    30	\subsection{The trend across \texorpdfstring{$N$}{N}}
    31	
    32	\begin{table}[ht]
    33	\centering
    34	\small
    35	\caption{$C\times P$ interaction estimate as a function of $N$.}
    36	\label{tab:cxp_trend}
    37	\begin{tabular}{r l r l l}
    38	\toprule
    39	$N$ & Seeds & Estimate $\Delta_{CP}$ & 95\% CI & Verdict vs $\geq +0.10$ \\
    40	\midrule
    41	$3$  & $30040$--$30042$ & $+0.044$ & --- & $\times$ original prereg \\
    42	$5$  & $30040$--$30044$ & $+0.039$ & --- & $\times$ this session re-run \\
    43	$10$ & $31000$--$31009$ & $+0.088$ & $[-0.002, +0.174]$ & borderline \\
    44	$\mathbf{20}$ & $\mathbf{32000\text{--}32019}$ & $\mathbf{+0.190}$
    45	       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
    46	\bottomrule
    47	\end{tabular}
    48	\end{table}
    49	
    50	The trend is monotone-increasing in $N$. Per-seed std at $N\!=\!10$
    51	was $0.159$; at $N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$
    52	sample landed on outliers, the $N\!=\!20$ sample reveals a clean
    53	narrow positive distribution.
    54	
    55	\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
    56	
    57	\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
    58	$32000$--$32019$, non-overlapping with original validation seeds in
    59	the $30000$s), $150$ epochs per run. All other ablation flags off
    60	($D, E$ held on). Bootstrap $n_{\mathrm{resamples}}\!=\!2000$,
    61	seed $42$. Wallclock $1706$\,s on a single CPU
    62	(\texttt{demo\_p4\_cxp\_deep\_dive.py}).
    63	
    64	\textbf{Per-condition means at \texorpdfstring{$N\!=\!20$}{N=20}.}
    65	
    66	\begin{table}[ht]
    67	\centering
    68	\small
    69	\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
    70	\label{tab:cxp_means}
    71	\begin{tabular}{l r r r}
    72	\toprule
    73	condition & mean $\alpha$ & std & sem \\
    74	\midrule
    75	$----$ baseline    & $3.008$ & $0.090$ & $0.020$ \\
    76	$-C--$ (C off)     & $3.464$ & $0.097$ & $0.022$ \\
    77	$--P-$ (P off)     & $2.790$ & $0.086$ & $0.019$ \\
    78	$-CP-$ (both off)  & $3.628$ & $0.161$ & $0.036$ \\
    79	\bottomrule
    80	\end{tabular}
    81	\end{table}
    82	
    83	\textbf{Main effects at \texorpdfstring{$N\!=\!20$}{N=20}.}
    84	$C$ main effect $= +0.456$ (turning $C$ off raises $\alpha$);
    85	$P$ main effect $= -0.218$ (turning $P$ off lowers $\alpha$).
    86	
    87	\textbf{Interaction estimate.} Direct calculation from means:
    88	\[
    89	\Delta_{CP} \;=\; \frac{(3.628 + 3.008) - (3.464 + 2.790)}{2}
    90	            \;=\; +0.191.
    91	\]
    92	Bootstrap on the 20-seed sample (2000 resamples):
    93	\begin{itemize}\itemsep=1pt
    94	\item bootstrap mean $\Delta_{CP} = +0.190$;
    95	\item 95\% bootstrap CI $[+0.143, +0.239]$;
    96	\item $0/2000$ bootstrap resamples were at or below zero, reported as
    97	      $0.0000$;
    98	\item $0/2000$ bootstrap resamples were below the preregistered
    99	      $+0.10$ floor, reported as $0.0000$.
   100	\end{itemize}
   101	
   102	\textbf{Per-seed paired distribution.}
   103	$19/20$ seeds give a positive paired-interaction estimate (range
   104	$+0.055$ to $+0.322$); a single seed gives $-0.009$. No seed gives a
   105	strongly negative interaction.
   106	
   107	\subsection{Reading and disclosure}
   108	
   109	\textbf{The 95\% CI is entirely above the preregistered $+0.10$
   110	threshold} on a fresh-seed sample. The synergy is decisively positive
   111	($P(\Delta_{CP}\!\leq\!0)$ reported as $0.0000$ on $0/2000$ bootstrap
   112	resamples) and decisively above prereg ($P(\Delta_{CP}\!<\!+0.10)$
   113	reported as $0.0000$ on $0/2000$ bootstrap resamples).
   114	
   115	\textbf{Architectural reading (substrate witness).} $C$ creates churn
   116	in \emph{which} vertices are uncrossed (frame rotation churns the
   117	uncrossed pool). $P$ promotes the high-pressure subset of the
   118	uncrossed pool to mini-emitters. The product is a non-additive
   119	novel-event-generation pathway: with both on, the uncrossed pool
   120	churns and $P$ amplifies new vertices entering the high-pressure
   121	region; with either off, the pathway collapses. The interaction
   122	$+0.19$ is comparable in magnitude to the $P$ main effect $-0.22$,
   123	so $C$ and $P$ are \emph{strongly coupled} cascade-state stabilisers
   124	on this substrate, not nearly-orthogonal ones. This reverses an
   125	architectural claim from the original 3-seed validation that held $C$
   126	and $P$ approximately orthogonal.
   127	
   128	\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
   129	was conducted \emph{after} the original $N\!=\!3$ failure
   130	(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
   131	selected to be non-overlapping with the original $30000$s seeds.
   132	Two strengthening builds we have not delivered:
   133	(i) a second independent $N\!=\!20$ run at a different seed range
   134	(e.g.\ $33000$--$33019$), and
   135	(ii) an $N\!=\!50$ characterisation of the per-seed sample
   136	distribution. Both are recorded as open builds in
   137	\S\ref{sec:limitations}.
   138	
   139	\textbf{What this stress test does \emph{not} establish.}
   140	\begin{itemize}\itemsep=2pt
   141	\item It does not establish a Lyapunov function on the reduced flow.
   142	\item It does not establish that the substrate is uniquely selected by
   143	  $C\times P$ coupling among regular 4-polytopes.
   144	\item It does not establish an $\eta$-trajectory derivation; $\eta$
   145	  is treated as a condition-dependent constant in this paper.
   146	\end{itemize}
   147	The stress test is what its name says: a high-replication factorial
   148	test of one preregistered interaction prediction, on a fresh-seed
   149	sample, with bootstrap confidence intervals. The architectural reading
   150	is a \emph{description} of what $C$ and $P$ do on the substrate, not a
   151	theorem about why they do it.
   152	
   153	\subsection{Methodological contribution}
   154	
   155	We document, as a methodological contribution to preregistration
   156	practice, that interaction terms in cascade ablation matrices require
   157	$N\!\geq\!20$ fresh seeds for reliable detection when the
   158	interaction-to-main-effect ratio is below $0.5$. The original 3-seed
   159	preregistered validation hit Type II false negatives on both
   160	interaction tests (P3 and P4); both close at higher $N$ without
   161	threshold modification. For preregistration design more broadly:
   162	when preregistering an interaction effect on a system with unknown
   163	per-seed variance, allocate the seed count from a power-analysis
   164	assumption that the per-seed std could be as large as the interaction
   165	effect itself. Under that assumption, $N\!\geq\!20$ is the conservative
   166	minimum.

 succeeded in 402ms:
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
    66	P10 & null perm. mapping (15 perms)         & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
    67	P11 & random-label baseline (20 trials)     & $\in[15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
    68	P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
    69	\textbf{P13} & LOO substrate lift (with reset) & $\geq +15$pp & $\mathbf{+40.6}$pp & $\checkmark$ \\
    70	\bottomrule
    71	\end{tabular}
    72	\end{table}
    73	
    74	\textbf{Reading.} Substrate routing amplifies chess-position
    75	4-category classification from raw $53.1\%$ (just above $25\%$
    76	chance) to substrate-routed $93.8\%$ at canonical depth — a $+40.6$pp
    77	lift at the same threshold the preregistered prediction set
    78	($\geq +15$pp). The original 2026-04-20 validation reported this
    79	lift at $+3.1$pp, a state-drift artefact closed by the reset
    80	protocol (\S\ref{sec:method}).
    81	
    82	\textbf{Permutation null decomposition.} The null permutation
    83	mapping (P10) randomises the feature$\to$frame assignment, so each
    84	feature is routed to a different $S^{7}$ frame than canonical. The
    85	substrate retains $65.4\%$ classification accuracy under random
    86	permutation — well above the $25\%$ chance level for $4$ categories.
    87	We read this as a substrate-witness decomposition:
    88	$\sim 65$pp of classification power is \emph{architectural} (it
    89	persists when feature$\to$frame assignment is randomised; it is the
    90	H$_4$-symmetric amplifier acting on whatever input lands in the
    91	frames), and the remaining $\sim 17$pp is the semantic-alignment
    92	bonus. We do not claim this decomposition is unique; it is a
    93	description of the observed accuracy stack.
    94	
    95	\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
    96	
    97	\textbf{Setup.} $64$ utterances across $8$ dialogue-act categories.
    98	$8$-dimensional injection-row features per utterance. Identical
    99	substrate routing pipeline to chess.
   100	
   101	\begin{table}[ht]
   102	\centering
   103	\small
   104	\caption{Conversation preregistered tests.}
   105	\label{tab:conv_prereg}
   106	\begin{tabular}{l l l l l}
   107	\toprule
   108	ID & Test & Threshold & Observed & Verdict \\
   109	\midrule
   110	P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
   111	P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   112	P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
   113	\bottomrule
   114	\end{tabular}
   115	\end{table}
   116	
   117	\textbf{Reading.} Conversation raw features at $87.5\%$ are already
   118	strongly discriminative (cf.\ chess raw $\sim 53\%$); the substrate
   119	lift is $-4.4$pp, well within the preregistered neutrality band
   120	$|\cdot|\!<\!10$pp. The substrate is correctly null on conversation.
   121	
   122	\textbf{Selective amplifier signature.} The pair (chess
   123	$+40.6$pp lift; conversation $-4.4$pp lift) confirms the substrate
   124	amplifies only when raw features are ambiguous. This is the
   125	selective-amplifier behaviour preregistered in 2026-04-18: a single
   126	domain-invariant geometric architecture lifts on ambiguous inputs and
   127	is approximately neutral on saturated inputs, without per-domain
   128	tuning.
   129	
   130	\subsection{HCP brain-graph maximum-symmetry null
   131	            (P17--P18)}\label{ssec:hcp}
   132	
   133	\textbf{Setup.} Reference cohort: Human Connectome Project (HCP)
   134	$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
   135	$n=100$ subjects for computational tractability, with full-cohort
   136	$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
   137	connectivity matrix; thresholded at the same density as ARIA's
   138	vertex graph ($\rho=0.101$). Compare degree distribution and
   139	higher-order graph statistics. ARIA reference: $G_{V_{600}}$ with
   140	$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
   141	has identical local structure $\Rightarrow$ uniform degree $12$
   142	$\Rightarrow$ degree std $= 0$ as a theorem.
   143	
   144	\begin{table}[ht]
   145	\centering
   146	\small
   147	\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
   148	$n=1003$ descriptive statistics.}
   149	\label{tab:hcp}
   150	\begin{tabular}{l r r r}
   151	\toprule
   152	Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
   153	\midrule
   154	Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
   155	Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
   156	Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
   157	Clustering coefficient (descriptive)       & $0.455$ & $0.220$ & $+6.80\sigma$ \\
   158	\bottomrule
   159	\end{tabular}
   160	\end{table}
   161	
   162	\begin{itemize}\itemsep=2pt
   163	\item P17 (ARIA degree std, theorem): predicted $=0$, observed
   164	  $0.0000$, $\checkmark$.
   165	\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
   166	  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
   167	  HCP subjects have degree std below $2.0$.
   168	\end{itemize}
   169	
   170	\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
   171	structure is a deterministic group-theoretic null reference for
   172	cortical functional connectivity. Real cortex breaks the symmetry
   173	through hub-spoke functional specialisation; the $\sigma$-distances
   174	quantify the magnitude of biological symmetry-breaking with no
   175	fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
   176	homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
   177	clustering) far exceed any preprocessing-induced noise envelope on
   178	the chosen ICA-50 parcellation.
   179	
   180	\textbf{What we do not claim.}
   181	\begin{itemize}\itemsep=2pt
   182	\item We do not claim cortex has ``drifted from an ideal polytope'';
   183	  the substrate is a useful a-priori null whose deviation from real
   184	  cortex is precisely measurable.
   185	\item We do not claim parcellation invariance: the $\sigma$-distances
   186	  are reported on ICA-50; alternative parcellations (Schaefer,
   187	  Glasser) would give different per-metric numbers but, on the
   188	  basis of the qualitative pattern that cortex is hub-concentrated
   189	  relative to ARIA's transitive null, we expect them to preserve the
   190	  signs. Verification across parcellations is an open build
   191	  (\S\ref{sec:limitations}).
   192	\end{itemize}
   193	
   194	\subsection{Cross-domain summary as a selective amplifier
   195	            \texorpdfstring{$+$}{+} maximum-symmetry null}
   196	
   197	\begin{table}[ht]
   198	\centering
   199	\small
   200	\caption{Cross-domain summary on a single substrate.}
   201	\label{tab:cross_domain_summary}
   202	\begin{tabular}{l r r r r r}
   203	\toprule
   204	Task & Raw & Substrate & Null perm. & Geom.\ floor & Sem.\ alignment \\
   205	\midrule
   206	Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
   207	Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\
   208	Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (raw vs null) \\
   209	\bottomrule
   210	\end{tabular}
   211	\end{table}
   212	
   213	The geometric content ($\approx 65$--$71\%$ across the two domains)
   214	is the architecture-invariant null floor. The semantic content
   215	($12$--$18$pp) is the domain-specific contribution. On HCP,
   216	$\sigma$-distances against the biological cohort are
   217	$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
   218	clustering coefficient).
   219	
   220	\textbf{Headline cross-domain reading.} The substrate is
   221	\emph{selectively} amplifying (not unconditionally), and it is a
   222	maximum-symmetry deterministic null on connectivity (not a fitted
   223	model). Both readings sit inside the substrate-witness scope.

exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 290ms:
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
    18	  real-cortex EEG signatures without learned parameters.} The
    19	  600-cell + H$_4$ symmetry is fixed by group theory; cascade-$\alpha$
    20	  matches Sleep-EDFx within preregistered tolerance with three-way CI
    21	  overlap; six drug/sleep signatures pass at preregistered thresholds
    22	  on a single deterministic substrate. To our knowledge, no prior
    23	  geometric model reproduces this many independent EEG signatures
    24	  from a substrate fixed by group theory.
    25	\item \textbf{The strong-coupling architectural finding.} $C$ and $P$
    26	  are strongly coupled cascade-state stabilisers, not
    27	  nearly-orthogonal ones. The $C\!\times\!P$ interaction
    28	  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
    29	  in magnitude to the $P$ main effect ($-0.218$). This was hidden by
    30	  underpowered ablation and emerged only at $N\!\geq\!20$ — a
    31	  substantive correction to the architectural reading from the
    32	  original 3-seed validation.
    33	\item \textbf{The 18/18 preregistered correspondences with no
    34	  threshold modification.} Every prediction in the preregistered set
    35	  passes at the preregistered thresholds. The two interaction tests
    36	  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
    37	  one test (P13) required the documented state-reset protocol. We
    38	  report this transparently as methodology refinement, not as
    39	  threshold change.
    40	\end{enumerate}
    41	
    42	\subsection{Comparison to existing theories of consciousness}
    43	
    44	\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
    45	IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
    46	wake). The H$_4$-equivariance argument
    47	(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
    48	group-symmetric, and $\Phi > 0$ only when dynamics break symmetry.
    49	ARIA does not implement the full IIT axioms (cause-effect repertoires,
    50	exclusion postulate, integration-over-partitions); it reproduces the
    51	observable consequence on the propofol--wake state contrast. This is
    52	a consistency-of-direction result, not a discharge of IIT.
    53	
    54	\textbf{vs Global Workspace Theory.} The $S^{7}$ context-rotation
    55	mechanism (\S\ref{sec:chain}) is functionally analogous to a workspace
    56	with rotating attentional selection; the active observer frame plays
    57	the role of a temporary in-workspace subset of features. ARIA does
    58	not commit to the GWT broadcast/access distinction at the
    59	architectural level; the analogy is descriptive.
    60	
    61	\textbf{vs Predictive Processing.} ARIA does not implement
    62	prediction-error minimisation or hierarchical generative models.
    63	The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
    64	modulation of the substrate response by cosine direction alignment
    65	with the prior phenomenal snapshot, not by learned prediction errors.
    66	Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
    67	learning rate over a prediction-error norm) are an open build, not
    68	delivered here.
    69	
    70	\textbf{vs neural mass models.} ARIA operates at the
    71	architectural-algorithmic level; it does not specify which neural
    72	circuits implement context rotation or partial emission. The 600-cell
    73	substrate is proposed as an abstract description of the criticality-
    74	maintaining structure of cortex, not as a circuit model.
    75	
    76	\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
    77	
    78	The companion adaptive-closure-transport
    79	preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
    80	4-tuple bridge
    81	$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
    82	$L_{M}$, learnable Hebbian-like field $W$, and a homeostatic
    83	regulariser $R_{\mathrm{hom}}$. We propose the dictionary
    84	$D_{\mathrm{ACT}}$:
    85	\[
    86	D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
    87	\;\longmapsto\;
    88	(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
    89	   \ \texttt{homeostatic\_reset}).
    90	\]
    91	\textbf{This bridge is non-load-bearing for the present paper.} It is
    92	included as a route-K (alternative-route) reading; the substrate-
    93	witness claims (six signatures, $18/18$, chess $+40.6$pp,
    94	HCP $\sigma$-distances) do not require any of the ACT theorems.
    95	
    96	\textbf{What ACT would have to deliver to make this load-bearing.}
    97	The companion preprint identifies four open builds, each of which is
    98	deferred:
    99	\begin{itemize}\itemsep=2pt
   100	\item A Lyapunov function $V(W)$ on the reduced flow whose
   101	  monotonicity proves selection — not delivered.
   102	\item An edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   103	  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
   104	  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
   105	\item A formal $2I$-equivariance audit of the closure operator
   106	  family — not delivered.
   107	\item A full reduced-flow convergence theorem on
   108	  $W$-trajectories — not delivered.
   109	\end{itemize}
   110	Until these are delivered, ARIA is positioned as the empirical
   111	\emph{substrate witness} for the family that ACT names; ACT is not the
   112	selection-theorem witness for ARIA. The companion kernel
   113	document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
   114	in a passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$ flavour
   115	anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
   116	infrastructure with this paper, but does not transfer empirical
   117	support for ARIA.
   118	
   119	\subsection{The strong-coupling reading for cortical architecture}
   120	
   121	Real cortical criticality is maintained by multiple parallel
   122	mechanisms: E/I balance, neuromodulation (acetylcholine, noradrenaline),
   123	homeostatic plasticity, gain control. The naive expectation — and the
   124	one we held until the $N\!=\!20$ deep-dive — is that these are mostly
   125	orthogonal, so losing one removes only its own main effect. The
   126	$N\!=\!20$ result reverses this on the substrate: $C$ and $P$ are
   127	strongly coupled. Disabling one cascades into losing the synergistic
   128	contribution of the other.
   129	
   130	This matches clinical observations: anaesthesia (which targets
   131	GABAergic transmission) and seizure (which targets E/I balance)
   132	produce widespread network-level dysfunction beyond their direct
   133	targets — exactly what strong synergy predicts. We position this as
   134	\emph{a hypothesis the substrate witness raises}, not as a proof.
   135	The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
   136	real-cortex pharmacological coupling is a step we do not take in
   137	this paper.
   138	
   139	\subsection{Methodological contributions}
   140	
   141	Two methodological items are worth recording outside the headline:
   142	\begin{enumerate}\itemsep=2pt
   143	\item \textbf{$N\!\geq\!20$ for high-variance interaction terms.}
   144	  Allocation discipline for preregistration: when preregistering an
   145	  interaction effect on a system with unknown per-seed variance,
   146	  budget for $N\!\geq\!20$ from the start. The original 3-seed plan
   147	  was the source of two Type II false negatives in this work.
   148	\item \textbf{State-reset protocol on non-stationary substrates.}
   149	  ARIA's substrate is a non-stationary dynamical system; the
   150	  pressure field equilibrates within $\sim 5$ successive evaluations.
   151	  Any multi-trial benchmark must specify a state-reset protocol or
   152	  document the drift. Generalisable lesson: \emph{published
   153	  cross-domain benchmarks on non-stationary substrates should report
   154	  an explicit reset/equilibration discipline}, not just seed.
   155	\end{enumerate}
   156	
   157	\subsection{The substrate as a maximum-symmetry connectivity null}
   158	
   159	The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
   160	deterministic null reference for cortical functional connectivity.
   161	Real cortex breaks the symmetry through hub-spoke functional
   162	specialisation; the $\sigma$-distances from ARIA quantify the
   163	magnitude of biological symmetry-breaking with no fitted parameters.
   164	
   165	This is a methodological contribution to comparative connectomics.
   166	Stochastic nulls (Erd\H{o}s--R\'enyi, configuration model,
   167	edge-randomised graphs) compare cortex to a random graph with matched
   168	density. ARIA is a different kind of null: a deterministic
   169	group-theoretic graph with theorem-level statements of structure
   170	(degree std $=\!0$ by transitivity, eigenvalue spectrum
   171	$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$ by character
   172	theory). Both null kinds are useful; ARIA gives a specific,
   173	reproducible, group-theoretic baseline that cortex deviates from in
   174	quantifiable $\sigma$-units.
   175	
   176	\subsection{Open questions raised by the substrate witness}
   177	
   178	\begin{itemize}\itemsep=2pt
   179	\item Do the six drug/sleep signatures replicate across $10$--$20$
   180	  cross-seed runs of the recurrent layer? (Single-seed disclosure;
   181	  see \S\ref{sec:limitations}.)
   182	\item Do alternative regular 4-polytopes ($24$-cell, $120$-cell)
   183	  reproduce comparable signature sets, or is the $600$-cell
   184	  distinguished?
   185	\item Does the strong-coupling reading ($C\!\times\!P$) survive an
   186	  independent fresh-seed $N\!=\!20$ replication at a different seed
   187	  range?
   188	\item Does the substrate's amplifier behaviour transfer to other
   189	  ambiguous-feature classification tasks beyond chess (e.g.\ visual
   190	  pattern, audio classification)?
   191	\item Does the Sleep-EDFx three-way CI overlap survive on a different
   192	  EEG cohort (TUH, NHM)?
   193	\end{itemize}
   194	We list these as open questions raised by the witness, not as gaps
   195	in the witness itself.

 succeeded in 281ms:
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
   179	eighteen preregistered correspondences and six independent drug/sleep
   180	EEG signatures, with all original gaps closed by methodology
   181	refinement and without modifying any preregistered threshold. We do
   182	not claim the substrate \emph{is} consciousness. We do not claim a
   183	selection theorem on the ACT bridge. We do not claim uniqueness for
   184	$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
   185	for these stronger claims are listed above and remain open.

 succeeded in 351ms:
     1	% =====================================================================
     2	\section{Conclusion}\label{sec:conclusion}
     3	% =====================================================================
     4	
     5	The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
     6	symmetry, with the shifted-Laplacian response operator
     7	$\Cph = \Lop + \Ph^{-2} I$ ($\Ph=(1+\sqrt 5)/2$), is a
     8	geometry-fixed substrate that is consistent with eighteen
     9	preregistered neuroscience correspondences plus six independent
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
    21	drug/sleep EEG signatures pass at preregistered thresholds:
    22	NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake;
    23	propofol modality-switching $1.83\!\times$ wake; propofol continuity
    24	drop $+0.066$; propofol integrated-information $\Phi$ collapse to
    25	$0.33\!\times$ wake (IIT direction confirmed); recovery
    26	deterministically identical to wake; wake cortical-avalanche power
    27	law $\alpha\!=\!2.252$, $95\%$ CI $[1.82, 2.86]$, $R^{2}\!=\!0.956$.
    28	The wake $95\%$ CI overlaps simultaneously the real Sleep-EDFx EEG
    29	$95\%$ CI ($n\!=\!30$ subjects, $\alpha\!=\!2.51$,
    30	CI $[2.50, 2.53]$) and ARIA's prior cascade pipeline CI
    31	$[2.73, 3.25]$.
    32	
    33	\textbf{Eighteen preregistered correspondences.} All eighteen pass at
    34	preregistered thresholds, with two interaction tests requiring
    35	$N\!\geq\!5$ and $N\!=\!20$ respectively for reliable detection of
    36	high-variance interaction terms, and one cross-domain test requiring
    37	the documented \texttt{homeostatic\_reset} state-reset protocol. No
    38	preregistered threshold has been modified. The original 2026-04-20
    39	$15/18$ tally was a methodology-limited reading, not a content
    40	failure; the closure of the three gaps (P3, P4, P13) is documented
    41	transparently in
    42	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
    43	
    44	\textbf{Strong-coupling architectural finding.} Two cascade
    45	mechanisms — context rotation $C$ and partial emission $P$ — are
    46	causally identifiable and \emph{strongly synergistic}: their
    47	interaction $\Delta_{CP}\!=\!+0.190$ at $N\!=\!20$
    48	($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples at or
    49	below zero, reported as $0.0000$) is comparable in magnitude to the
    50	$P$ main effect $-0.218$. The original 3-seed estimate ($+0.044$)
    51	was a Type II false negative on a high-per-seed-variance interaction
    52	term ($\mathrm{std}=0.089$ at $N\!=\!20$); we contribute the
    53	$N\!\geq\!20$ minimum as a preregistration-practice recommendation.
    54	
    55	\textbf{Cross-domain selectivity.} The substrate functions as a
    56	domain-invariant selective amplifier — chess 4-category position
    57	classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
    58	canonical depth $n\!=\!25$ ticks (raw $53.1\%$ $\to$ substrate-routed
    59	$93.8\%$, with state reset; threshold $\geq\!+15$pp), while
    60	conversation utterance classification at raw $87.5\%$ lifts $-4.4$pp
    61	(threshold $|\cdot|\!<\!10$pp) — and as a maximum-symmetry
    62	deterministic null reference for cortical functional connectivity:
    63	on HCP $n\!=\!1003$, ARIA's H$_4$-transitive structure is at
    64	$-11.58\sigma$ on degree homogeneity, $+79.78\sigma$ on participation
    65	ratio, and $+6.80\sigma$ on clustering coefficient.
    66	
    67	\textbf{Substrate-witness scope.} This is a substrate witness, not a
    68	derivation of consciousness, not a selection theorem on the
    69	companion adaptive-closure-transport
    70	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
    71	uniqueness claim for the 600-cell among regular 4-polytopes. The
    72	strengthening builds — cross-seed CIs on the recurrent-layer
    73	signatures, alternative-polytope ablations, an independent $N\!=\!20$
    74	C$\times$P replication at a different seed range, cross-parcellation
    75	HCP replication, a Lyapunov function on the reduced flow,
    76	$2I$-equivariance audit of the closure operator family — are
    77	explicitly listed in~\S\ref{sec:limitations} and remain open.
    78	
    79	We propose this is the first deterministic geometric architecture, to
    80	our knowledge, to be consistent with this many independent
    81	preregistered neuroscience correspondences from group-theoretic
    82	structure with no fitted shape parameters. The empirical material
    83	gathered here is the substrate witness; the broader programme to
    84	turn the witness into a selection-theorem-grade claim — including the
    85	independent passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$
    86	flavour anomaly~\citep{SmartBAnomaly2026} on the same response
    87	operator $\Cph$ — is sketched in the companion preprints and remains
    88	the natural next step.

 succeeded in 350ms:
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
    51	@article{Brodbeck2012Microstates,
    52	  author  = {Brodbeck, Verena and Kuhn, Andreas and von Wegner, Frederic and Morzelewski, Antoine and Tagliazucchi, Enzo and Borisov, Sergey and Michel, Christoph M. and Laufs, Helmut},
    53	  title   = {{EEG} microstates of wakefulness and {NREM} sleep},
    54	  journal = {NeuroImage},
    55	  volume  = {62},
    56	  number  = {3},
    57	  pages   = {2129--2139},
    58	  year    = {2012},
    59	  doi     = {10.1016/j.neuroimage.2012.05.060}
    60	}
    61	
    62	@article{VanEssen2013HCP,
    63	  author  = {Van Essen, David C. and Smith, Stephen M. and Barch, Deanna M. and Behrens, Timothy E. J. and Yacoub, Essa and Ugurbil, Kamil},
    64	  title   = {The {WU-Minn Human Connectome Project}: an Overview},
    65	  journal = {NeuroImage},
    66	  volume  = {80},
    67	  pages   = {62--79},
    68	  year    = {2013},
    69	  doi     = {10.1016/j.neuroimage.2013.05.041}
    70	}
    71	
    72	@article{PhysioNet2000,
    73	  author  = {Goldberger, Ary L. and Amaral, Luis A. N. and Glass, Leon and Hausdorff, Jeffrey M. and Ivanov, Plamen Ch. and Mark, Roger G. and Mietus, Joseph E. and Moody, George B. and Peng, Chung-Kang and Stanley, H. Eugene},
    74	  title   = {{PhysioBank, PhysioToolkit, and PhysioNet}: components of a new research resource for complex physiologic signals},
    75	  journal = {Circulation},
    76	  volume  = {101},
    77	  number  = {23},
    78	  pages   = {e215--e220},
    79	  year    = {2000},
    80	  doi     = {10.1161/01.CIR.101.23.e215}
    81	}
    82	
    83	@misc{SleepEDFx,
    84	  author       = {Kemp, Bob and Zwinderman, Aeilko H. and Tuk, Bert and Kamphuisen, Hilbert A. C. and Obery{\'e}, Josefien J. L.},
    85	  title        = {{Sleep-EDFx}: Sleep Cassette and Telemetry recordings},
    86	  howpublished = {PhysioNet},
    87	  year         = {2013},
    88	  note         = {Accessed 2026-04-29}
    89	}
    90	
    91	@misc{OpenNeuroDS005620,
    92	  author       = {Lichvar, Erin and others},
    93	  title        = {{OpenNeuro Dataset ds005620}: propofol-induced loss of consciousness {EEG}},
    94	  howpublished = {OpenNeuro},
    95	  year         = {2024},
    96	  doi          = {10.18112/openneuro.ds005620.v1.0.0}
    97	}
    98	
    99	@misc{OpenNeuroDS004902,
   100	  author       = {Timmermann, Christopher and others},
   101	  title        = {{OpenNeuro Dataset ds004902}: {DMT-induced} altered states of consciousness {EEG}},
   102	  howpublished = {OpenNeuro},
   103	  year         = {2023},
   104	  doi          = {10.18112/openneuro.ds004902.v1.0.8}
   105	}
   106	
   107	@misc{ZenodoDMT3992359,
   108	  author       = {Timmermann, Christopher},
   109	  title        = {{DMT EEG} dataset},
   110	  howpublished = {Zenodo},
   111	  year         = {2020},
   112	  doi          = {10.5281/zenodo.3992359}
   113	}
   114	
   115	@unpublished{SmartAdaptiveClosureTransport2026,
   116	  author = {Smart, Lee},
   117	  title  = {Adaptive Closure Transport: a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ from substrate response to selection},
   118	  year   = {2026},
   119	  note   = {VFD preprint, papers/adaptive-closure-transport/}
   120	}
   121	
   122	@unpublished{SmartAriaClosureKernel2026,
   123	  author = {Smart, Lee},
   124	  title  = {The 600-cell closure response kernel $C_\varphi = L + \varphi^{-2} I$ and its 9-shell projection},
   125	  year   = {2026},
   126	  note   = {VFD preprint, docs/aria-closure-kernel.md}
   127	}
   128	
   129	@unpublished{SmartBAnomaly2026,
   130	  author = {Smart, Lee},
   131	  title  = {A geometry-derived response kernel for the $B \to K^*\mu^+\mu^-$ angular anomaly: sign-uniform cross-dataset and cross-channel fit},
   132	  year   = {2026},
   133	  note   = {VFD preprint, papers/b-anomaly/}
   134	}
   135	
   136	@misc{ariaChessRepo,
   137	  author       = {Smart, Lee},
   138	  title        = {{ARIA-chess}: 600-cell substrate, recurrent self-model, and preregistered validation},
   139	  howpublished = {GitHub repository},
   140	  year         = {2026},
   141	  note         = {Accessed 2026-04-29}
   142	}

codex
I’ve read the paper source and bibliography. The main shape is disciplined, but a few claims already look stronger than the supporting methodology, especially novelty, “preregistered” wording for the six signatures, and some deterministic-null readings. I’m checking the source markdown now so the numeric audit is anchored to the local records.
  ✓ Read WO context and map required scope constraints
  ✓ Read paper LaTeX and bibliography with line numbers
  → Read source documents and verify headline numerics
  • Cross-check claims, consistency, and LaTeX surface issues
  • Write structured referee review with file-line citations
exec
/bin/bash -lc 'wc -l "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 338ms:
  1253 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md
   426 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md
   435 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md
   584 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md
   399 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md
   194 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md
   257 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md
  3548 total

exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"6/6|ALL 6|PASS|WAKE|SLEEP_N3|PROPOFOL|RECOVERY|0\\.463|1\\.83|2\\.96|0\\.066|0\\.33|2\\.252|\\[1\\.82, 2\\.86\\]\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"18/18|17/18|15/18|P4|P13|0\\.190|\\+0\\.143|\\+0\\.239|0/2000|0\\.0000|threshold|modified|methodolog|2\\.958|2\\.513|3\\.388|\\+40\\.6|n=25|25\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"0\\.190|\\+0\\.143|\\+0\\.239|0/2000|0\\.0000|19/20|\\+0\\.044|\\+0\\.039|\\+0\\.088|\\+0\\.191|std|32000|32019|Type II|threshold\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 418ms:
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

 succeeded in 447ms:
20:The six signatures span four conditions (WAKE, SLEEP_N3, PROPOFOL, RECOVERY)
26:stimulus-model artefacts in `demo_wake_alpha_diagnosis.py`) to 6/6 by
32:| 1 | Sleep variance ratio | NREM-N3 EEG (Lee 2017, Jobst 2017) | ratio ≈ 0.365 | 0.463 | ✓ within 30% |
33:| 2 | Propofol switching ↑ | OpenNeuro ds005620 (n=8, 2.96×) | ratio in [1.5, 5.0] | 1.83× | ✓ |
34:| 3 | Propofol continuity ↓ | EEG microstate (Brodbeck 2012) | drop > 0.020 | +0.066 | ✓ |
35:| 4 | Propofol Φ collapse | IIT prediction (Tononi 2008) | ratio < 0.5 | 0.33× | ✓ |
37:| 6 | Cortical avalanche α | Sleep-EDFx n=30 (α=2.51 [2.50, 2.53]) | α ∈ [1.5, 3.5], R² > 0.85 | 2.252 [1.82, 2.86] R²=0.956 | ✓ |
40:**ARIA WAKE α CI [1.82, 2.86] overlaps real Sleep-EDFx EEG CI [2.50, 2.86]
70:- η = 0.20 for WAKE, RECOVERY (active recurrent self-loop)
71:- η = 0.05 for SLEEP_N3 (attenuated self-loop)
72:- η = 0.00 for PROPOFOL (broken recurrence — preserves residual cortex)
111:### WAKE — AR(1) cortical noise + tonic shell + attention episodes
154:### SLEEP_N3 — slow waves + spindles + K-complexes
178:### PROPOFOL — low-amplitude tonic noise (unchanged from v3)
187:### RECOVERY — identical to WAKE
199:WAKE       58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
200:SLEEP_N3  111   3.250   [2.44, 4.14]   0.886  1.01e-05    0.0055   0.980
201:PROPOFOL  246   2.758   [2.52, 3.09]   0.931  5.37e-06    0.0003   0.877
202:RECOVERY   58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
211:**Observed:** WAKE intensity_var = 2.18×10⁻⁵, SLEEP intensity_var = 1.01×10⁻⁵.
212:Ratio = 0.463. Falls within [0.255, 0.475], the 30% prediction window.
217:collapse. PROPOFOL's pure tonic noise gives a similar variance ratio of 0.246
218:to WAKE — distinguishable from sleep direction.
224:microstate switching ratio 2.96×).
226:**Observed:** WAKE modality_switches → PROPOFOL modality_switches ratio = 1.83×.
227:Falls within [1.5×, 5.0×] window. Below the empirical 2.96× point estimate
230:**Mechanism:** WAKE's attention episodes anchored to ATTENTION_SHELL keep
231:modality stable for tens of ticks at a time. PROPOFOL has no recurrent
241:**Observed:** WAKE composite continuity = 0.943, PROPOFOL = 0.877.
242:Drop = +0.066. Falls past the +0.020 minimum.
244:**Mechanism:** WAKE's recurrent self-loop (η=0.20) plus AR(1) temporal
245:input keeps state trajectories smooth. PROPOFOL's broken recurrence plus
255:**Observed:** WAKE Φ_traj = 0.0008, PROPOFOL Φ_traj = 0.0003.
256:Ratio PROPOFOL/WAKE = 0.33×. Below the 0.50× threshold.
259:both substrate symmetry-breaking and trajectory persistence. WAKE has
260:both via η=0.20 self-loop integrating AR(1) input. PROPOFOL has neither
269:**Observed:** RECOVERY intensity_var = WAKE intensity_var to 0 difference;
270:RECOVERY continuity = WAKE continuity to 0 difference.
273:stim model produces identical trajectory. Verifies that PROPOFOL's effects
283:**Observed:** WAKE α = 2.252, 95% CI [1.82, 2.86], R² = 0.956 (n_events=58).
288:- v4 WAKE CI [1.82, 2.86]
291:project, beating both v3 PROPOFOL (R²=0.93) and the n=30 EEG fit (R²~0.85).
294:nonlinearity that produces avalanches; AR(1) WAKE input gives self-similar
295:single-scale events. v3's mixed pole+equator+random WAKE produced three
315:The diagnostic settled the substrate question: pure-random WAKE drive lands
319:But pure-random WAKE alone fails the propofol contrast tests (sigs 2-4) —
320:WAKE looks identical to PROPOFOL because both are just random tonic noise.
325:- **v4.0**: AR(1) + salient single-tick events → attention shifts inflated WAKE switching past PROPOFOL (sig 2 fail)
326:- **v4.1**: Pure random WAKE → α clean but propofol contrast collapses (sigs 2,3,4 fail)
329:- **v4.final**: AR(1) β=0.90 + tonic shell + episodes 20-50 amp 0.8 anchored to shell + within-shell rotation → 6/6
350:- v3 PROPOFOL α should be 2.758 [2.52, 3.09] R²=0.931 — unchanged from v3 across this work.
368:- The Sig 2 ratio (1.83×) is below the empirical point estimate (2.96×)
386:| `demo_drug_sleep_v4.py` | The 6/6 demo script — single deterministic run |
404:- `project_propofol_empirical_5.md` — empirical anchor for Sig 2 (n=8, 2.96×)
416:power law in the wake-state band (passes with α = 2.252, 95% CI [1.82, 2.86]
419:1.83×), propofol continuity disruption (passes at +0.066), propofol Φ collapse
420:in the IIT direction (passes at 0.33× wake), and recovery reversibility (passes

 succeeded in 461ms:
3:*This document supersedes `VALIDATION_RESULTS.md` (2026-04-20, 15/18).
5:plus the N=20 deep-dive on the residual P4 prediction.*
8:> 18 / 18 with N=20 deep-dive on the residual P4.** Original 15/18
15:> set is fully validated against preregistered thresholds.
25:Each prediction has a falsifiable threshold (numerical band or
37:The original validation run on 2026-04-20 reported **15/18 passes**:
45:  - **P4** (C×P synergy): observed +0.044 at N=3, below +0.10 floor.
46:  - **P13** (Chess LOO substrate lift ≥ +15pp): observed +3.1pp,
50:- "P3, P4 walked back to 'preliminary, requires larger N'."
51:- "P13 reframed as state-dependent — substrate state drifted toward
59:1. **Cascade block N bumped 3 → 5** for P2, P3, P4, P5 conditions
61:   the source of high-variance failure on P3 and P4.
69:3. **N=20 deep-dive** on the residual P4 (`demo_p4_cxp_deep_dive.py`):
72:   `P4_SYNERGY_FINDING.md` for the standalone report.
80:| ID | Claim | Threshold | 2026-04-20 (3-seed) | **2026-04-29 (5-seed + reset + N=20 P4)** | Verdict |
82:| P1 | Cascade α ∈ [2.5, 3.5] | ∈ [2.5, 3.5] | 3.020 ✅ | **2.958** | ✅ |
85:| P4 | C×P synergy | ≥ +0.10 | +0.044 ❌ | **+0.190 at N=20, CI [+0.143, +0.239]** | ✅ at N=20 |
87:| P6 | Real EEG α | ∈ [2.0, 3.0] | 2.513 ✅ | **2.513** | ✅ |
93:| P12 | Chess goldilocks peak | ∈ {15, 25, 40, 60} | n=15 ✅ | **n=25** | ✅ |
94:| P13 | Chess LOO substrate lift | ≥ +15pp (with reset) | +3.1pp ❌ | **+40.6pp** | ✅ |
98:| P17 | ARIA degree std (theorem) | = 0.00 | 0.0000 ✅ | **0.0000** | ✅ |
99:| P18 | HCP ICA-50 degree std | > 2.0 | 3.388 ✅ | **3.388** | ✅ |
116:seeds tightens the estimate enough to land inside the threshold.
120:interaction estimate is approximately 0.06–0.10; the threshold is
126:threshold. We do not claim point-zero independence (the estimate is
130:### 3.2 P4 — C×P synergy
133:`P4_SYNERGY_FINDING.md` for the full story.
137:**Original (N=3) failure:** +0.044. Below threshold.
139:**2026-04-29 re-run (N=5):** +0.039. Still below threshold — confirming
145:C×P bootstrap mean:           +0.190
146:C×P 95% bootstrap CI:         [+0.143, +0.239]
147:P(interaction ≤ 0):           0.0000
148:P(interaction < +0.10):       0.0000
151:The 95% CI is **entirely above the preregistered +0.10 threshold**.
161:`P4_SYNERGY_FINDING.md` for the mechanistic interpretation.
163:### 3.3 P13 — Chess LOO substrate lift
165:**Threshold:** ≥ +15pp lift (substrate vs raw on LOO at n=25 ticks).
167:**Original (N=1) failure:** +3.1pp. Far below threshold.
170:measurements):** **+40.6pp**.
176:  n=25:   93.8%   ← peak (P12 goldilocks)
181:Lift at n=25 = 93.8% − 53.1% = +40.6pp
186:original LOO test ran six consecutive depth measurements (n=5, 15, 25,
187:40, 60, 100) without reset, so by the time it reached n=25 the substrate
193:exceeded by 25pp — the substrate's amplification effect is real and
198:protocol.** This is now a methodological recommendation in the paper.
209:- **P1**: Baseline α at 5 seeds = 2.958 (vs original 3.020 at 3 seeds).
212:  at 3 seeds). Both above the +0.30 dominance threshold.
219:- **P6**: Real EEG spindle α = 2.513 (n=30 subjects). Inside [2.0, 3.0].
225:### 4.3 Chess closed-loop (P9, P10, P11, P12, plus P13 fixed)
235:- **P12**: Goldilocks peak depth = n=25 (∈ {15, 25, 40, 60}). With
236:  reset between measurements, n=25 is the global maximum at 93.8%.
237:- **P13**: LOO substrate lift at n=25 = **+40.6pp** with reset
254:- **P17**: ARIA degree std = 0.0000. Theorem (H₄ transitivity).
255:- **P18**: HCP ICA-50 degree std = 3.388 (n=100 subjects, density-
256:  matched threshold). > 2.0 confirms small-world hub-spoke structure
262:## 5. The 18/18 verdict
264:**Standard validation tally:** 17/18 (the residual P4 fails at N=5).
265:**Including the N=20 deep-dive:** 18/18 (P4 passes decisively at N=20).
267:The empirical tally is **18/18 at adequate replication**. Two of the
268:three original failures (P3, P13) close at standard methodology
269:improvements (5-seed cascade block + reset protocol). The third (P4)
276:within preregistered thresholds**, with the methodological caveat
277:that two interaction tests (P3, P4) require N ≥ 5 and N ≥ 20
286:> *"All eighteen preregistered predictions pass at empirical thresholds.
287:> The validation runs at standard methodology (5-seed cascade block,
288:> homeostatic reset between LOO depth measurements) give 17/18; the
289:> residual prediction (P4 — C×P synergy) requires higher-N replication
291:> interaction-term estimates. With adequate N, P4 passes decisively
292:> (+0.190, 95% bootstrap CI [+0.143, +0.239]); the synergy is in fact
313:### 6.2 Original walk-back on P4 (C×P synergy)
318:**Now reads:** C×P synergy is +0.190 [+0.143, +0.239] at N=20, ~90%
323:### 6.3 Original walk-back on P13 (chess LOO lift)
329:finding and is documented as a methodological recommendation
332:is +40.6pp.
336:## 7. Preregistration as the central methodological commitment
338:The original validation methodology — 18 preregistered predictions
339:with falsifiable thresholds, frozen before any validation run — is
341:re-run with N improvements **did not modify any threshold or claim
343:reset. The fact that this gave 18/18 (with N=20 P4) where the
344:original gave 15/18 demonstrates that:
348:(b) The original validation methodology was insufficient — N=3 is
350:(c) A re-run with adequate methodology validates all predictions
355:adequate power. No threshold was loosened. No prediction was rewritten
364:# Standard validation (17/18, ~18 min)
368:# P4 N=20 deep-dive (~28 min)
385:- `docs/brain_mapping/VALIDATION_RESULTS.md` — original 15/18 result
387:- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — standalone N=20 report

 succeeded in 450ms:
9:> on cascade-α is +0.190, 95% bootstrap CI [+0.143, +0.239]** — comparable
13:> Type II false negative compounded by seed-range sampling bias on a
37:  threshold but not yet crossed) emit pressure at 30% scale, saturating
87:This was below the +0.10 threshold, so P4 was reported as a **fail**
104:- **N = 20 fresh seeds** (range 32000–32019, non-overlapping with prior
128:cond     mean α   std    sem    individual seeds (n=20)
159:                = +0.191
165:C×P bootstrap mean:           +0.190
166:C×P 95% bootstrap CI:         [+0.143, +0.239]
167:P(interaction ≤ 0):           0.0000
168:P(interaction < +0.10):       0.0000
171:**The 95% CI is entirely above the preregistered +0.10 threshold.**
182:[+0.259, +0.234, +0.233, +0.191, +0.135, +0.098, +0.245, +0.167,
186:mean = +0.190,  std = 0.089,  SEM = 0.020
191:per-seed std at N=20 (0.089) is just under half the per-seed std at
203:3    30040–30042      +0.044          —                     ❌ original prereg
204:5    30040–30044      +0.039          —                     ❌ this session re-run
205:10   31000–31009      +0.088          [−0.002, +0.174]      borderline (CI contains)
206:20   32000–32019      +0.190          [+0.143, +0.239]      ✅ DECISIVELY ABOVE
213:1. **Type II false negative from underpowered N.** With per-seed std
216:   were no other bias — already containing the threshold. But N=3 also
221:   then 32000–32019. The means at each seed range differ enough that
226:The N=10 sample (31000–31009) had a per-seed std of 0.159 because it
227:landed on outliers; the N=20 sample (32000–32019) had std 0.089. **The
228:correct interpretation is that the original test was Type II underpowered
252:exceeded threshold. As the frame rotates, the uncrossed pool's
311:> The original 3-seed estimate (+0.044) was a Type II false-negative
313:> interaction term. Replication at N=20 fresh seeds (32000–32019)
314:> gives synergy = +0.190, 95% bootstrap CI [+0.143, +0.239],
359:BASE_SEED = 32000
368:**Verification:** seeds 32000–32019 should give the per-condition means
387:   (e.g., pressure-threshold crossings) might give a slightly different
407:The original 3-seed validation reported +0.044 — a fail — and the paper
409:synergy = +0.190, 95% bootstrap CI [+0.143, +0.239], P(synergy ≤ 0) = 0,
412:main effect (−0.218). The original underestimate was a Type II false

exec
/bin/bash -lc "rg -n \"\\+40\\.6|93\\.8|53\\.1|n=25|n = 25|with reset|reset|\\+27\\.2|n=15|83\\.1|87\\.5|-4\\.4|70\\.6|65\\.4|HCP|1003|-11\\.58|79\\.78|6\\.80|3\\.28|0/1003|3\\.388|descriptive|preregistered\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"0\\.190|\\+0\\.143|\\+0\\.239|0/2000|0\\.0000|\\+0\\.044|\\+0\\.039|\\+0\\.088|\\+0\\.191|19/20|P\\(synergy|P\\(interaction|resamples|bootstrap\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"reset|homeostatic_reset|\\+40\\.6|\\+3\\.1|drift|n=25|93\\.8|53\\.1|\\+27\\.2|n=15|without reset|with reset\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"600-cell|unique|selection|Lyapunov|consciousness|18/18|17/18|15/18|\\+40\\.6|\\+27\\.2|0/2000|P\\(|2\\.96|1\\.83|1003|N=100|n=100|n=1003|threshold|methodolog|reset\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 325ms:
20:Only a **reset mechanism** analogous to biological sleep restores
27:### E1 — Drift curve (30 consecutive classifications, no reset)
32:| 2 | 93.8% | 100 | 147.9 | 1.000 |
43:### E2 — Homeostatic reset
49:| **Full reset** | **87.5% (higher than fresh)** |
50:| Partial reset (50% decay) | 81.2% |
52:**Full reset restores AND improves on the fresh state**. Because
54:full reset clears those, leaving the substrate genuinely canonical.
99:| P13 preregistration fail | polytope drifted to equilibrium across evaluations |
104:| Fresh-polytope vs state-drifted +31pp vs +3pp | non-equilibrium vs equilibrium regimes |
121:pre-loaded "ignited" state is SOC; steady operation without reset
132:during wake. Our reset operation is a direct computational analogue.
134:synaptic downscaling — exactly what our `_homeostatic_reset` does
141:If sleep is the biological analogue of our reset operation:
149:  reset dynamics (higher or more variable, as the substrate is
203:   to test the "SWS = substrate reset" prediction
205:4. ⏳ Add homeostatic reset API to DimensionalMonitor
206:5. ⏳ Re-run preregistered validation with proper reset — convert
229:- Sleep-like reset is the thermodynamic necessity

 succeeded in 341ms:
9:> on cascade-α is +0.190, 95% bootstrap CI [+0.143, +0.239]** — comparable
117:We then bootstrapped the interaction distribution (2000 resamples,
119:one-sided P(interaction ≤ 0) and P(interaction < +0.10).
159:                = +0.191
162:Bootstrap (2000 resamples) on the 20-seed sample gives:
165:C×P bootstrap mean:           +0.190
166:C×P 95% bootstrap CI:         [+0.143, +0.239]
167:P(interaction ≤ 0):           0.0000
168:P(interaction < +0.10):       0.0000
182:[+0.259, +0.234, +0.233, +0.191, +0.135, +0.098, +0.245, +0.167,
186:mean = +0.190,  std = 0.089,  SEM = 0.020
203:3    30040–30042      +0.044          —                     ❌ original prereg
204:5    30040–30044      +0.039          —                     ❌ this session re-run
205:10   31000–31009      +0.088          [−0.002, +0.174]      borderline (CI contains)
206:20   32000–32019      +0.190          [+0.143, +0.239]      ✅ DECISIVELY ABOVE
217:   has limited bootstrap resolution.
311:> The original 3-seed estimate (+0.044) was a Type II false-negative
314:> gives synergy = +0.190, 95% bootstrap CI [+0.143, +0.239],
315:> P(synergy ≤ 0) = 0, P(synergy < +0.10) = 0. The architecture's
365:interaction point estimate, bootstrap 95% CI, one-sided P-values,
371:seed-42 bootstrap RNG differences across NumPy versions.
407:The original 3-seed validation reported +0.044 — a fail — and the paper
409:synergy = +0.190, 95% bootstrap CI [+0.143, +0.239], P(synergy ≤ 0) = 0,
410:P(synergy < +0.10) = 0. The architecture's prediction is exceeded by

 succeeded in 321ms:
6:of the work. This version incorporates the v4 consciousness chain (six
15:We propose a deterministic geometric substrate for consciousness based
16:on the 600-cell regular 4-polytope under its H₄ Coxeter symmetry. The
31:regime-switching elevates 1.83× wake; propofol continuity drops by
39:by 5×; we document the underpowered detection as a methodological
42:recognition by +40.6 percentage points (raw 53.1% → substrate-routed
46:HCP brain functional connectivity (n=1003 subjects), ARIA serves as a
50:deep-dive, the empirical tally is 18/18 preregistered predictions
56:**Keywords**: 600-cell polytope, H₄ Coxeter symmetry, cortical
66:Theories of consciousness divide between mechanism-driven theories
78:phenomena it reproduces. The substrate is the 600-cell regular
81:has not been proposed before as a consciousness substrate.
91:The 600-cell admits a 7-rung cascade decomposition that emerges from
111:600-cell substrate has 120 vertices, each of uniform degree 12. The
129:`O*` within a preregistered threshold. We report two non-overlapping
140:"consciousness chain"). Tests cover NREM-N3 variance collapse,
146:thresholds (with the methodological caveat that two interaction
158:The 600-cell vertices are the H₄ Coxeter group acting on the
167:This is the standard 600-cell construction (Schläfli {3, 3, 5}); see
232:A vertex "crosses" once its accumulated pressure exceeds a threshold;
266:High-pressure uncrossed vertices (above threshold but not yet
294:estimated at +0.044 — below the preregistered +0.10 threshold —
312:  P(interaction ≤ 0):       0.0000
313:  P(interaction < +0.10):   0.0000
316:The 95% CI is **entirely above the preregistered +0.10 threshold**;
317:the synergy is decisively positive (P(≤ 0) = 0) and decisively above
318:prereg (P(< +0.10) = 0).
393:### 4.2 The bounded-top-K thresholding
402:the 600-cell graph (each vertex has 12 neighbours); this is a
429:Implementation: `kernel/consciousness_binding.py:phi_iit_trajectory`.
456:Implementation: `kernel/consciousness_binding.py:bind_phenomenal_field`.
464:The 600-cell graph is built once from H₄ root coordinates. The graph
466:(`kernel/consciousness_binding.py:_SPECTRAL_CACHE`); repeated runs
492:### 5.4 Stimulus models for the consciousness chain
558:run. Each prediction has a falsifiable threshold (numerical band or
563:**Critical: no threshold has been modified post-hoc. The original
565:methodology required improvement (cascade block N, reset protocol,
566:deep-dive N), this is documented as a methodological refinement,
567:not as a threshold change.
590:### 5.7 The non-stationarity finding and reset protocol
597:The fix is `homeostatic_reset(level=1.0)` — a method that
599:training state to canonical baseline. With reset between depth
601:+3.1pp lift (without reset, on a state-drifted substrate) to +40.6pp
602:lift (with reset, far exceeding the preregistered +15pp floor).
605:Implementation: `kernel/dimensional_monitor.py:DimensionalMonitor.homeostatic_reset`.
607:This is a separate methodological finding: ARIA's substrate is a
609:specify state-reset protocol**.
624:**Method.** Run the 600-cell substrate with all four mechanisms (D, C,
635:| v4 WAKE consciousness chain | 2.252 | [1.82, 2.86] | 0.956 | 58 |
639:range. The v4 consciousness-chain WAKE α is **inside both** the
645:and the consciousness-chain produce α values in the SOC band at
648:### 6.2 Six drug/sleep EEG signatures reproduced (consciousness chain v4)
651:bounded top-K thresholding and IIT-style Φ, reproduces six independent
654:**Method.** Four conditions × 800 ticks at seed = 42, k_threshold = 12.
673:| 2 | Propofol regime-switching ratio | OpenNeuro ds005620 (n=8, 2.96×) | ∈ [1.5, 5.0] | **1.83×** | ✓ |
679:All six signatures pass at preregistered thresholds. The wake cascade-α
689:2.96× empirically); the NREM-N3 variance collapse magnitude is
707:C main:  +0.621  (≥ +0.30 prereg threshold)        ✅ P2
733:P(synergy ≤ 0) = 0.0000; P(synergy < +0.10) = 0.0000.
766:  order statistics to HCP n=1003 ICA-50 group-averaged connectivity
767:  (density-matched threshold = 0.101).
769:**Chess result (with `homeostatic_reset` between depth measurements):**
776:P13 — LOO substrate lift (raw 53.1% → 93.8%):  +40.6pp ≥ +15pp  ✅
778:Depth sweep (with reset, fresh seed):
784:  n=100:  78.1%
795:**HCP result (n=1003 subjects, ICA-50):**
797:| Metric | ARIA | HCP n=1003 mean | σ from HCP |
808:Zero of 1003 HCP subjects have degree std below 2.0; ARIA is far
813:(i) **Selective amplification.** The contrast between chess (+40.6pp
835:### 6.5 The eighteen preregistered predictions: 17/18 standard, 18/18 with N=20 P4
838:block + `homeostatic_reset` wired in. Run `demo_p4_cxp_deep_dive.py`
839:at N=20 for the residual P4. Tally pass/fail per preregistered threshold.
857:| P13 | Chess LOO lift (with reset) | ≥ +15pp | +40.6pp | ✅ |
864:**Tally: 17/18 at standard validation; 18/18 with N=20 deep-dive on P4.**
866:**Comparison to the original 2026-04-20 run (15/18):**
874:- **P13** (chess LOO lift): +3.1pp without reset → +40.6pp with reset.
876:  resolved by `homeostatic_reset(level=1.0)` between measurements.
878:**No threshold has been modified.** The original predictions are
879:confirmed in their original form, with two methodological refinements
880:(adequate N for high-variance interactions; reset protocol for multi-
894:without learned parameters.** The 600-cell + H₄ symmetry comes from
896:tolerance; six drug/sleep signatures pass at preregistered thresholds.
908:**(3) The 18/18 preregistered claim with no threshold modification.**
910:thresholds. The two interaction tests (P3, P4) required higher N
912:documented reset protocol; we report this honestly as methodology
913:refinement, not as a post-hoc threshold change.
927:selection; the active observer frame plays the role of a temporary
940:context rotation or partial emission. The 600-cell substrate is
968:We document, as a methodological contribution to preregistration
974:threshold modification.
990:This is a methodological contribution to comparative connectomics:
1012:1. **Single substrate (the 600-cell).** We have not tested whether
1014:   produce comparable correspondences. The 600-cell was chosen
1041:   integration but not yet verified end-to-end in the consciousness
1044:4. **Sig 2 ratio (1.83×) is below empirical point estimate (2.96×)**
1064:   is the methodological strength of the cross-domain comparison.
1086:1. **The 600-cell choice is post-hoc justified by biology.** While
1088:   theory), the choice of *this* polytope as the consciousness
1122:For the consciousness chain (`demo_drug_sleep_v4.py`):
1125:- k_threshold = 12 (cortical band; bounded_topk nonlinearity)
1140:- HCP: deterministic (n=100 ICA-50 group average)
1148:# Run six-signature consciousness chain
1159:overlaps, P-value thresholds) should be unaffected.
1170:| `dimensional_monitor.py` | Pressure-field cascade dynamics; the four mechanisms (D, C, P, E); homeostatic_reset |
1172:| `consciousness_binding.py` | bind_phenomenal_field; phi_iit_trajectory; spectral cache |
1182:| `demo_drug_sleep_v4.py` | Six-signature consciousness chain (§6.2) |
1208:The 600-cell polytope under H₄ Coxeter symmetry, decomposed into a
1215:on the 600-cell.
1223:underpowered detection as a methodological contribution to
1227:top-K thresholding and an IIT-style integrated information proxy,
1234:classification tasks (chess +40.6pp lift; conversation correctly null
1236:cortical functional connectivity (HCP n=1003: ARIA at −11.58σ on

 succeeded in 363ms:
1:# Cross-Domain Validation: Chess, Conversation, and HCP Connectivity
8:> when raw features are ambiguous (chess: +40.6 percentage points on
9:> leave-one-out, raw 53.1% → substrate-routed 93.8%) and is correctly
10:> null when raw features already saturate (conversation: 87.5% raw,
13:> transitivity); HCP n=1003 degree std = 3.28 ± 0.28; ARIA is
14:> −11.58σ on degree homogeneity and +79.78σ on participation ratio,
27:1. **Chess pattern recognition** (P9–P13 in the preregistered set):
40:3. **HCP brain connectivity** (P17–P18): compare ARIA's vertex-graph
42:   the Human Connectome Project (n=1003 subjects, ICA-50
47:preregistered tests on chess + conversation pass at fresh seeds; both
48:HCP tests pass deterministically (P17 from theorem; P18 from data).
79:is reset to canonical state via `mon.homeostatic_reset(level=1.0)`.
91:Per-seed accuracies:  81.2%, 81.2%, 84.4%, 87.5%, 81.2%
92:Mean:                 83.1%
96:83.1% on the 32-position × 4-category task, well above the 70%
97:threshold. Per-seed variance is small (range 81.2%–87.5%).
100:the fresh-seed mean of 83.1% replicates discovery within expected
113:**Result:** 65.4% mean across 15 permutations.
117:substrate retains 65.4% classification power — well above the 25%
121:(83.1% − 65.4%) is the semantic alignment bonus.
143:(23.4% ≈ 25% chance). This confirms the 83.1% raw and 65.4% null are
153:depth, with `homeostatic_reset(level=1.0)` between measurements.
159:   5     53.1%
161:  25     93.8%   ← peak
168:n=25, with a roll-off both at shallower depth (insufficient
175:### 2.6 P13 — Substrate lift on LOO with reset protocol
181:(b) substrate-routed patterns at n=25, with reset between depth
187:Raw features (LOO, 1-NN cosine):       53.1%
188:Substrate-routed (n=25, with reset):   93.8%
189:Lift:                                  +40.6 percentage points
193:discrimination from chance-level on raw features (53.1% on 4 categories
194:is just above chance-25%) to near-perfect (93.8%) when routed through
195:the substrate's 600-cell graph. This is **+40.6pp of geometric
199:failure of the reset protocol (substrate state drifted toward
201:classification structure). With the reset protocol now wired in, the
202:lift is restored to +40.6pp. See `NON_EQUILIBRIUM_FINDING.md` for the
208:- 53.1% raw → 93.8% substrate-routed at canonical depth (n=25)
209:- 65.4% null mapping (architecture-invariant geometric floor)
210:- 83.1% 5-fold CV at fresh seeds
211:- Goldilocks optimum at n=25 ticks of substrate evolution
213:The +40.6pp lift is roughly an order of magnitude above the +15pp
214:preregistered floor. The 65.4% null mapping shows two-thirds of the
238:**Result (fresh seeds 30220–30224):** **87.5%** mean.
241:discriminative — 87.5% raw classification at 5-fold CV exceeds the
242:chess raw rate (53.1% LOO) by ~34pp. There is little headroom for
253:Raw 5-fold CV:               87.5%
254:Substrate 5-fold CV (n=25):  83.1%
262:preregistered window, and the negative sign suggests minor noise
277:**Result:** 70.6% mean across 15 permutations.
279:**Interpretation:** Conversation null mapping (70.6%) is slightly
280:higher than chess null mapping (65.4%), consistent with conversation
289:| Chess (LOO) | 53.1% | 93.8% | n/a | n/a | +40.6pp lift |
290:| Chess (5-fold CV) | n/a | 83.1% | 65.4% | 65.4% | +17.7pp |
291:| Conversation (5-fold CV) | 87.5% | 83.1% | 70.6% | 70.6% | +12.5pp (raw vs null) |
300:selective amplification. Raw features at 87.5% leave little headroom;
301:substrate routing at 83.1% (lift −4.4pp) is within preregistered
302:neutrality bounds. The null permutation at 70.6% confirms geometric
307:## 4. HCP brain connectivity (P17–P18)
311:**Reference cohort:** Human Connectome Project (HCP), n=1003 subjects.
312:For preregistered tests, n=100 subjects (computational tractability)
313:in ICA-50 parcellation. The full-cohort effects (n=1003) match the
336:### 4.3 P18 — HCP degree std (hub-spoke structure)
338:**Threshold:** HCP ICA-50 degree std > 2.0.
340:**Result (n=100 subjects, density 0.101):** **3.388**.
347:**ARIA is at −11.58σ** below the HCP cohort mean on this metric:
348:ARIA's degree std is 0; HCP n=1003 mean is 3.28 ± 0.28; the gap is
349:(0 − 3.28) / 0.28 = −11.7σ. **Zero of 1003 HCP subjects** have
352:### 4.4 Higher-order graph statistics (full cohort, n=1003)
354:Three metrics computed across the full HCP cohort, with ARIA's value
358:Metric                 ARIA     HCP n=1003 mean   σ from HCP
360:Degree std             0.000    3.28 ± 0.28        −11.58σ
361:Participation ratio    68.54    19.72 ± 0.61       +79.78σ
362:Clustering coefficient 0.455    0.220              +6.80σ
369:  hub-concentrated). ARIA at 68.54 vs HCP at 19.72 — ARIA is
371:  Real cortex is hub-concentrated; ARIA is uniform. +79.78σ.
373:  ARIA at 0.455 vs HCP at 0.220 — ARIA has more local clustering
375:  +6.80σ.
379:The HCP comparison places ARIA as a **principled maximum-symmetry
383:quantitatively measurable as the σ-distance between ARIA and HCP on
390:giving precise effect-size statements like "real cortex is +79.78σ
394:induced noise envelope — the gap between ARIA and HCP is robust to
416:### 4.7 HCP summary
418:ARIA's degree std = 0 (theorem); HCP n=1003 degree std = 3.28 ± 0.28,
419:range [2.55, 4.16], with zero of 1003 subjects below 2.0. ARIA is
420:−11.58σ on degree homogeneity, +79.78σ on participation ratio, and
421:+6.80σ on clustering coefficient. The substrate functions as a
433:hand-features is at chance-class (53.1% raw LOO), substrate routing
434:amplifies to 93.8% LOO (+40.6pp lift) and 83.1% 5-fold CV across fresh
439:8-dimensional features are already 87.5% discriminative, the substrate
440:is correctly null (lift −4.4pp, well within preregistered neutrality
442:unconditional booster. On HCP brain functional connectivity (n=1003,
444:std = 0) is −11.58σ below the biological mean (3.28 ± 0.28); on
445:participation ratio ARIA at 68.54 is +79.78σ above HCP (19.72 ± 0.61),
446:and on clustering coefficient ARIA at 0.455 is +6.80σ above HCP (0.220).
459:The contrast between chess (+40.6pp lift) and conversation (−4.4pp
469:The 65.4% (chess) / 70.6% (conversation) null permutation accuracies
479:reference for biological cortex. The σ-distances (−11.58σ, +79.78σ,
480:+6.80σ) quantify the magnitude of biological symmetry-breaking, with
493:python3 run_preregistered_validation.py
502:- HCP n=100 ICA-50: deterministic from group average
507:- `run_hcp_registration.py` for HCP
509:JSON outputs land in `~/.aria/preregistered_validation/results_*.json`.
516:1. **Chess test is small (32 positions, 4 categories).** The ~93.8%
519:   at 83.1% is a more conservative readout (4-category random
527:3. **HCP comparison uses one parcellation (ICA-50).** Different
551:- `run_preregistered_validation.py` — full P1–P18 harness
555:- `run_hcp_registration.py` — HCP track
559:  with pressure-field dynamics; `homeostatic_reset(level=1.0)` is
560:  the reset method.
567:  preregistered tally
573:  state-drift diagnostic; rationale for `homeostatic_reset()`
582:- `project_hcp_maxsymmetry_null.md` — HCP comparison detail
583:- `project_preregistered_validation_17_of_18.md` — re-run summary

exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md\" | sed -n '1,80p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md\" | sed -n '195,290p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md\" | sed -n '340,424p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md\" | sed -n '100,230p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 261ms:
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

 succeeded in 232ms:
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

 succeeded in 252ms:
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

 succeeded in 322ms:
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

exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md\" | sed -n '1,105p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md\" | sed -n '130,200p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md\" | sed -n '225,295p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md\" | sed -n '145,215p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 289ms:
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

 succeeded in 305ms:
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

 succeeded in 321ms:
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

 succeeded in 307ms:
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

exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md\" | sed -n '307,425p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md\" | sed -n '433,481p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md\" | sed -n '1,120p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md\" | sed -n '300,414p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 388ms:
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

 succeeded in 416ms:
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

 succeeded in 423ms:
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

 succeeded in 445ms:
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

codex
The headline numerics mostly match the local source docs. One important inconsistency is emerging: P13 is reported in the paper as a preregistered LOO lift, while the preregistration file describes P13 as a 5-fold CV lift test. I’m doing a final pass for notation, citations, and scope language before writing the review.
  ✓ Read WO context and map required scope constraints
  ✓ Read paper LaTeX and bibliography with line numbers
  ✓ Read source documents and verify headline numerics
  → Cross-check claims, consistency, and LaTeX surface issues
  • Write structured referee review with file-line citations
exec
/bin/bash -lc 'rg -n "unique|selection theorem|Lyapunov|is consciousness|is cortex|proves|derive|forced|decisive|decisively|first|to our knowledge|correctly null|only when|far exceed|robust to|preregistered thresholds|exact-match|exactly|methodology-limited|content failure|Type II|false negative" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\[A-Za-z]+\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"citep\\{|citet\\{|bibliography\\{|bibitem\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "P13|LOO|5-fold|fresh seeds|with reset|threshold" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 267ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:16:\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:27:or leave-one-out (LOO).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:58:\caption{Chess preregistered tests (with reset, $n=25$ canonical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:65:P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:69:\textbf{P13} & LOO substrate lift (with reset) & $\geq +15$pp & $\mathbf{+40.6}$pp & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:77:lift at the same threshold the preregistered prediction set
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:110:P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:137:connectivity matrix; thresholded at the same density as ARIA's
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:206:Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:207:Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:208:Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (raw vs null) \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:7:the validation script, the seed range, the threshold, and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:17:falsifiable threshold, (iii) the validation test (script + seed range),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:35:\textbf{No threshold has been modified post-hoc.} Where the original
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:36:2026-04-20 validation reported failures (P3, P4, P13), the documented
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:42:measurements for the chess LOO test (P13). None of these touched a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:43:preregistered threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:49:\text{threshold}, \text{result})$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:68:P9 (chess 5-fold) & same & 30200--30204 & 32 positions, 4 cat. & $\geq 70\%$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:71:P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:72:\textbf{P13 (chess LOO lift)} & same & with reset & same & $\geq +15$pp \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:73:P14 (conv 5-fold) & same & 30220--30224 & 64 utt., 8 cat. & $\geq 75\%$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:168:LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:169:substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:196:verdicts (CI overlaps, $P$-value thresholds) are unaffected.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:10:$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:75:All six signatures pass at preregistered thresholds on the same
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:87:$32000$--$32019$). \emph{No preregistered threshold has been modified.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:107:P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:111:\textbf{P13} & Chess LOO lift (with reset)   & $\geq +15$pp     & $+40.6$pp & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:112:P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:122:methodology refinement (no threshold change).}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:132:\item P13 (chess LOO lift) failed at $+3.1$pp without state reset on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:136:  lift is restored to $+40.6$pp at the same $\geq +15$pp threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:140:all pass at preregistered thresholds, with two interaction tests
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:10:- a **pass threshold** (interval, inequality, or categorical match)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:29:- **Claim**: On 3 fresh seeds (30010-30012), main effect of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:33:- **Run**: Conditions `----` vs `-C--` on fresh seeds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:52:  **|effect| < 0.15** on 3 fresh seeds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:88:### P9. Chess 5-fold CV ≥ chance + substantial margin
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:89:- **Claim**: 5-fold CV on v2 features at n=25 ticks, 5 fresh seeds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:92:  < 70% would mean our 84.4% LOO number was misleadingly inflated.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:93:- **Run**: `run_chess_pattern_readout.py` + 5-fold with fresh seeds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:115:### P13. Substrate lift on chess v2 is positive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:116:- **Claim**: At n=25, substrate ≥ raw **+ 15pp** on 5-fold CV (fresh
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:127:- **Claim**: Raw conversation 5-fold CV accuracy **≥ 75%** on fresh
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:129:- **Rationale**: Discovery gave 87.5% LOO. If much lower, the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:138:- **Run**: 5-fold CV raw vs substrate on fresh seeds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:160:  density-matched threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:184:## Success thresholds

 exited 1 in 310ms:
 succeeded in 292ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:61:preprint~\citep{SmartAdaptiveClosureTransport2026} provides the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:157:We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:158:OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:159:the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:160:the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:161:HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:163:methodology follows~\citep{BeggsPlenz2003}; the integrated-information
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:164:$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:166:al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:167:follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:169:repository~\citep{ariaChessRepo}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:175:from the project repository~\citep{ariaChessRepo} via the included
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:183:\bibliography{references}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:52:   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:55:   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:58:   EEG microstate~\citep{Brodbeck2012Microstates} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:61:   Tononi 2008~\citep{Tononi2008} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:67:   Sleep-EDFx $n=30$ CI~$[2.50, 2.86]$~\citep{BeggsPlenz2003,SleepEDFx} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:162:Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:173:band $\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The shared
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:134:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:17:$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:77:kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:79:flavour physics~\citep{SmartBAnomaly2026}, where the same operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:110:in companion preprints~\citep{SmartAriaClosureKernel2026}, the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:9:preprint~\citep{SmartAdaptiveClosureTransport2026}. We do not claim a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:44:\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:79:preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:113:document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:115:anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:81:kernel doc~\citep{SmartAriaClosureKernel2026} explicitly does not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:84:witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:105:2008~\citep{BalduzziTononi2008} on the substrate; not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:65:P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:77:P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:87:recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:91:methodology~\citep{BeggsPlenz2003}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:94:consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:100:EEG~\citep{OpenNeuroDS004902},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:105:release~\citep{ZenodoDMT3992359},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:109:S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:117:methodology of Brodbeck et al.~\citep{Brodbeck2012Microstates} is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:6:(Integrated Information Theory~\citep{Tononi2008,BalduzziTononi2008},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:21:over a century~\citep{CoxeterRegularPolytopes,Weisstein600Cell}; to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:85:  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:103:  document~\citep{SmartAriaClosureKernel2026} discusses its role.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:86:machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:70:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:86:flavour anomaly~\citep{SmartBAnomaly2026} on the same response

 succeeded in 326ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:59:selection theorem, nor a uniqueness claim for the 600-cell among regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:97:drug/sleep signatures pass at preregistered thresholds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:103:decisively at adequate replication: $N\!=\!20$ fresh seeds give a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:107:underestimate ($+0.044$) as a Type II false negative and contribute
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:128:We do not claim the 600-cell is the unique substrate consistent with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:130:have been ruled out. We do not derive the $\Ph^{-2}$ floor from
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:131:first principles; it is a design-level stability clamp on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:169:substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:41:  are forced by H$_4$ transitivity, the Laplacian eigenvalues
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:43:  their irrep multiplicities are forced by character theory, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:74:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:75:  the unique substrate consistent with these signatures. Other regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:79:  observables; it is not an a-priori derivation from first principles.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:84:\item \emph{Not a selection theorem.} The companion adaptive-closure-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:89:  non-load-bearing here. We do not deliver a Lyapunov function on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:101:  bounds the Green response). It is not derived as a theorem from a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:118:We never write `the substrate \emph{is} cortex' or `derives consciousness'.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:122:$+15$pp floor) licenses `decisively above prereg', not `proves'. A
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:137:\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:138:selection theorem on the 4-tuple bridge; circuit-level mechanistic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:139:identification; first-principles derivation of $\Ph^{-2}$ shift;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:159:ACT bridge (without claiming a selection theorem).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:75:All six signatures pass at preregistered thresholds on the same
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:126:  $N\!=\!5$ ($-0.183$). Diagnosis: classical Type II false negative
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:131:  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:140:all pass at preregistered thresholds, with two interaction tests
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:144:result was a methodology-limited tally, not a content failure.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:78:$\Phi > 0$ only when the dynamics break symmetry and transport
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:95:A composite first-person continuity score over a 64-tick rolling
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:151:not a derived theorem.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:13:Type II false negative, (b) confirming the trend across $N$, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:45:       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:110:threshold} on a fresh-seed sample. The synergy is decisively positive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:112:resamples) and decisively above prereg ($P(\Delta_{CP}\!<\!+0.10)$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:141:\item It does not establish a Lyapunov function on the reduced flow.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:142:\item It does not establish that the substrate is uniquely selected by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:159:preregistered validation hit Type II false negatives on both
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:7:H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:38:vertex has degree exactly $12$, and the unweighted graph Laplacian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:76:\emph{not} a derived theorem; it is a stability choice. The companion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:82:This paper imports $\Cph$ from that line; we do not re-derive it.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:93:The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:132:remaining operator structure is exactly preserved. We do not claim
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:133:the cascade itself is forced by physics on a pre-substrate level; the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:92:bonus. We do not claim this decomposition is unique; it is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:120:$|\cdot|\!<\!10$pp. The substrate is correctly null on conversation.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:124:amplifies only when raw features are ambiguous. This is the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:177:clustering) far exceed any preprocessing-induced noise envelope on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:21:  overlap; six drug/sleep signatures pass at preregistered thresholds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:35:  passes at the preregistered thresholds. The two interaction tests
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:48:group-symmetric, and $\Phi > 0$ only when dynamics break symmetry.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:100:\item A Lyapunov function $V(W)$ on the reduced flow whose
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:101:  monotonicity proves selection — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:133:targets — exactly what strong synergy predicts. We position this as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:147:  was the source of two Type II false negatives in this work.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:19:\emph{Disclosure:} substrate-witness scope, no uniqueness claim
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:48:replication on stimulus models derived from anatomically-grounded
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:59:derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:71:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:76:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:78:strictly positive definite (\S\ref{ssec:cphi}); it is not derived
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:82:derive it. \emph{Evidence:} the same operator (with the same shift)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:85:derive the $\Ph^{-2}$ shift as the unique stability clamp under a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:118:$N\!=\!20$. We document this transparently as a Type II
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:147:\textbf{Single condition-dependent parameter $\eta$ is not derived
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:164:\item Lyapunov derivation $V(W)$ from a closure functional
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:183:selection theorem on the ACT bridge. We do not claim uniqueness for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:21:drug/sleep EEG signatures pass at preregistered thresholds:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:34:preregistered thresholds, with two interaction tests requiring
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:39:$15/18$ tally was a methodology-limited reading, not a content
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:51:was a Type II false negative on a high-per-seed-variance interaction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:68:derivation of consciousness, not a selection theorem on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:71:uniqueness claim for the 600-cell among regular 4-polytopes. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:75:HCP replication, a Lyapunov function on the reduced flow,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:79:We propose this is the first deterministic geometric architecture, to

exec
/bin/bash -lc "rg -o \"\\\\[[:alpha:]]+\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\" | sort | uniq -c" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"Ph|varphi|Lop|Cph|C_\\{|Rsixhundred|V_\\{600\\}|V600|sixhundred|600-cell|H\\"'$_4'"\\"'$|H4" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"P\\(|P=0|P\\s*=\\s*0|p = 0|p=0|0/2000|0\\.0000\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "600-cell is|the substrate is|is a deterministic|is the first|substrate functions as|correctly null|far exceed|Type II false negative|methodology-limited|content failure|only when|with no fitted|no fitted" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 339ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:14:\newcommand{\Ph}{\varphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:15:\newcommand{\Lop}{L_{V_{600}}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:21:       signatures from the 600-cell under H$_4$ Coxeter symmetry}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:39:Once the 600-cell substrate is chosen, its graph structure is fixed by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:41:eigenvalues $\{0, 3, 4\Ph, 6\Ph, 12\!-\!4\Ph, 12\!-\!6\Ph, 12\!-\!3, 12\}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:42:in their H$_4$-irrep multiplicities, with $\Ph=(1+\sqrt 5)/2$. Treated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:44:response $\Cph = \Lop + \Ph^{-2} I$ and a small dynamical layer above
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:59:selection theorem, nor a uniqueness claim for the 600-cell among regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:63:sits as the $L_M$ instance; the selection of the 600-cell as the active
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:67:We test whether a geometry-fixed substrate — the 600-cell regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:68:4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:69:shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:95:information $\Phi$ collapse to $0.33\!\times$ wake (IIT direction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:128:We do not claim the 600-cell is the unique substrate consistent with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:130:have been ruled out. We do not derive the $\Ph^{-2}$ floor from
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:157:We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:164:$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:166:al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:19:  600-cell + H$_4$ symmetry is fixed by group theory; cascade-$\alpha$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:45:IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:47:(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:48:group-symmetric, and $\Phi > 0$ only when dynamics break symmetry.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:72:circuits implement context rotation or partial emission. The 600-cell
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:88:(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:113:document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:135:The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:171:$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$ by character
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:139:higher-order graph statistics. ARIA reference: $G_{V_{600}}$ with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:140:$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:2:\section{The 600-cell response substrate}\label{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:8:operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:16:The 600-cell $\Rsixhundred$ has $120$ vertices in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:18:With $\Ph = (1+\sqrt 5)/2$ the canonical vertex set is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:24:  $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:33:The substrate graph $G_{V_{600}} = (V, E)$ is built by connecting each
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:36:\begin{lemma}[600-cell graph facts]\label{lem:600cell}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:37:The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, every
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:39:$\Lop = D - A$ has spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:41:\sigma(\Lop) \;=\;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:42:\bigl\{0^{1}, 3^{4}, 4\Ph^{9}, 6\Ph^{16}, (12\!-\!4\Ph)^{9},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:43:       (12\!-\!6\Ph)^{16}, 9^{4}, 12^{1}\bigr\},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:54:$\mathbb{Z}[\Ph]$, the exponents become $\{7, 13, 17, 23\}$. We label
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:63:\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:68:\Cph \;=\; \Lop + \Ph^{-2} I,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:70:\psi \;=\; \Cph^{-1} f.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:72:The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:73:clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:74:$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:75:inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:78:$\Cph$ as the basis for an independent passive-regime witness in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:82:This paper imports $\Cph$ from that line; we do not re-derive it.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:84:The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:89:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:93:The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:112:$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:113:collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:134:cascade is a decomposition of operators on $\Rsixhundred$, and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:135:choice of $\Rsixhundred$ as the active substrate is post-hoc justified
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:141:\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:144:\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:147:\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:14:\textbf{Single substrate (the 600-cell).} We have not tested whether
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:16:comparable correspondences. The 600-cell was chosen because its
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:21:on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:53:\textbf{The 600-cell choice is post-hoc justified by empirical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:54:observables.} While the construction of $\Rsixhundred$ is theorem-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:76:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:77:$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:85:derive the $\Ph^{-2}$ shift as the unique stability clamp under a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:100:\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:102:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:138:are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:166:\item Selection theorem for $\Rsixhundred$ over alternative regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:184:$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:22:\Phi_{\mathrm{traj}}, \mathrm{cont})$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:32:condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:60:4 & Propofol $\Phi$ collapse (IIT) &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:181:(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:5:The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:7:$\Cph = \Lop + \Ph^{-2} I$ ($\Ph=(1+\sqrt 5)/2$), is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:13:$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$) is fixed by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:24:drop $+0.066$; propofol integrated-information $\Phi$ collapse to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:71:uniqueness claim for the 600-cell among regular 4-polytopes. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:87:operator $\Cph$ — is sketched in the companion preprints and remains
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:22:in \texttt{docs/brain\_mapping/PREREG\_H4\_FINGERPRINT.md} and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:30:propofol switching ratio, propofol continuity drop, propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:86:\textbf{Sleep-EDFx (PhysioNet).} Public polysomnography
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:87:recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:19:600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:23:consciousness substrate. We construct $\Rsixhundred$, fix its response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:24:operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:40:  $\Rsixhundred$ is selected, $120$ vertices of uniform degree $12$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:42:  $\{0, 3, 4\Ph, 6\Ph, 12\!-\!4\Ph, 12\!-\!6\Ph, 12\!-\!3, 12\}$ in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:44:  the response operator $\Cph$ is fully fixed up to the single
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:45:  parameter $\Ph^{-2}$ (a stability shift for the inverse map).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:55:  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:74:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:77:  build, not a discharged comparison. The 600-cell choice is post-hoc
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:87:  this substrate fills the $L_M$ slot. The selection of the 600-cell
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:98:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:99:  Laplacian floor $\Ph^{-2} \approx 0.382$ is a design-level
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:100:  stability clamp (it makes $\Cph$ strictly positive definite and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:111:$\mathcal C_{\mathrm{admissible}}$ by the rule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:113:q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow \mathcal C_{\mathrm{admissible}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:115:\mathcal C_{\mathrm{admissible}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:139:identification; first-principles derivation of $\Ph^{-2}$ shift;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:140:that cortex \emph{is} the 600-cell.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:148:constructs $\Rsixhundred$ and the response operator $\Cph$, with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:149:$\Ph^{-2}$ shift disclosed as a design-level stability clamp.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:8:regime-switching, propofol $\Phi$ collapse — we add a recurrent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:25:\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:34:prior snapshot). The substrate response operator $\Cph$ is unchanged
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:57:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:64:            \texorpdfstring{$\Phi$}{Phi}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:74:\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:76:By construction $\Phi\to 0$ under H$_{4}$-equivariant dynamics, since
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:78:$\Phi > 0$ only when the dynamics break symmetry and transport
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:83:We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:86:machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$

 succeeded in 350ms:
 succeeded in 445ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:105:(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:106:below zero, reported as $0.0000$. We document the original $N\!=\!3$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:115:P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:96:\item $0/2000$ bootstrap resamples were at or below zero, reported as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:97:      $0.0000$;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:98:\item $0/2000$ bootstrap resamples were below the preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:99:      $+0.10$ floor, reported as $0.0000$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:111:($P(\Delta_{CP}\!\leq\!0)$ reported as $0.0000$ on $0/2000$ bootstrap
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:112:resamples) and decisively above prereg ($P(\Delta_{CP}\!<\!+0.10)$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:113:reported as $0.0000$ on $0/2000$ bootstrap resamples).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:48:($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples at or
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:49:below zero, reported as $0.0000$) is comparable in magnitude to the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:164:  $0.0000$, $\checkmark$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:140:deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:141:$0/2000$ were below the preregistered floor $+0.10$; we report these
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:142:as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact

 succeeded in 436ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:49:are no fitted shape parameters and no learned weights; only one
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:107:underestimate ($+0.044$) as a Type II false negative and contribute
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:128:We do not claim the 600-cell is the unique substrate consistent with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:169:substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:138:\subsection{What the substrate is fixed-by, and what it is not}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:126:  $N\!=\!5$ ($-0.183$). Diagnosis: classical Type II false negative
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:144:result was a methodology-limited tally, not a content failure.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:179:no fitted parameter on neural data. The bounded-top-$K$ at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:62:\item \textbf{Cross-domain selectivity.} The substrate functions as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:74:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:48:group-symmetric, and $\Phi > 0$ only when dynamics break symmetry.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:147:  was the source of two Type II false negatives in this work.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:163:magnitude of biological symmetry-breaking with no fitted parameters.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:78:$\Phi > 0$ only when the dynamics break symmetry and transport
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:13:Type II false negative, (b) confirming the trend across $N$, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:142:\item It does not establish that the substrate is uniquely selected by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:159:preregistered validation hit Type II false negatives on both
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:30:measurements the substrate is reset to canonical state via
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:120:$|\cdot|\!<\!10$pp. The substrate is correctly null on conversation.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:124:amplifies only when raw features are ambiguous. This is the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:171:structure is a deterministic group-theoretic null reference for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:177:clustering) far exceed any preprocessing-induced noise envelope on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:183:  the substrate is a useful a-priori null whose deviation from real
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:11:the substrate is chosen, its graph structure
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:39:$15/18$ tally was a methodology-limited reading, not a content
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:51:was a Type II false negative on a high-per-seed-variance interaction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:55:\textbf{Cross-domain selectivity.} The substrate functions as a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:79:We propose this is the first deterministic geometric architecture, to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:82:structure with no fitted shape parameters. The empirical material

exec
/bin/bash -lc "rg -n \"label\\{|ref\\{\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "Global Workspace|predictive processing|Predictive Processing|GWT|Thorpe|Kiani|propofol|microstate|anaesthesia|anesthesia" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"2\\.50, 2\\.86|2\\.50, 2\\.53|2\\.51|2\\.513|2\\.85|2\\.73, 3\\.25|1\\.82, 2\\.86\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"n=1003|n\\"'!='"\\"'!1003|n=100|n'"\\"'!='"\\"'!100|preregistered|full-cohort|descriptive|3'"\\.388|3\\.28|79\\.78|6\\.80|-11\\.58\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 425ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:92:(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:93:ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$); propofol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:94:continuity drop $+0.066$ (threshold $>\!0.020$); propofol integrated-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:158:OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:165:the propofol microstate comparison uses Brodbeck et
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib:53:  title   = {{EEG} microstates of wakefulness and {NREM} sleep},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib:93:  title        = {{OpenNeuro Dataset ds005620}: propofol-induced loss of consciousness {EEG}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:58:   EEG microstate~\citep{Brodbeck2012Microstates} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:64:   clinical anaesthesia &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:45:IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:51:observable consequence on the propofol--wake state contrast. This is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:54:\textbf{vs Global Workspace Theory.} The $S^{7}$ context-rotation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:58:not commit to the GWT broadcast/access distinction at the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:61:\textbf{vs Predictive Processing.} ARIA does not implement
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:130:This matches clinical observations: anaesthesia (which targets
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:102:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:168:\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:23:propofol modality-switching $1.83\!\times$ wake; propofol continuity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:24:drop $+0.066$; propofol integrated-information $\Phi$ collapse to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:30:propofol switching ratio, propofol continuity drop, propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:96:empirical reference for the propofol switching ratio
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:116:\textbf{Brodbeck microstate baseline.} EEG microstate analysis
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:118:used as the reference for the propofol continuity-drop signature
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:7:To test high-level signatures — NREM-N3 variance collapse, propofol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:8:regime-switching, propofol $\Phi$ collapse — we add a recurrent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:86:machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:88:of effect on the propofol-vs-wake state contrast; it is not a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:104:This composite produces the propofol continuity-drop signature
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:7:Global Workspace, predictive processing) and structure-driven
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:53:  collapse to $0.463\!\times$ wake; propofol modality-switching
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:54:  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol

 succeeded in 438ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:2:\section{Methods and provenance}\label{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:25:listed as future strengthening builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:55:\label{tab:provenance}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:172:generalisable lesson is recorded in \S\ref{sec:limitations}: any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:2:\section{The recurrent layer}\label{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:5:The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:6:cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:17:signatures in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:57:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:87:collapse in~\S\ref{sec:results} is consistent with the IIT direction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:158:the C$\times$P stress test in~\S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:187:choices. Their causal effects are reported in~\S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:92:  builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:127:and applied throughout~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:146:\S\ref{sec:method} gives the provenance ledger (preregistration date,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:147:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:150:\S\ref{sec:chain} adds the recurrent self-model layer above the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:152:\S\ref{sec:results} reports the empirical tables: six drug/sleep
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:154:$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:156:$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:157:selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:160:\S\ref{sec:limitations} enumerates limitations and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:161:hostile-review guard matrix. \S\ref{sec:conclusion} concludes.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:2:\section{Results}\label{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:7:(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:20:(\S\ref{sec:chain}). Per-condition trajectory observables are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:29:\label{tab:per_condition}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:46:\label{tab:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:79:disclosure: \S\ref{sec:limitations} item~3.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:81:\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:93:\label{tab:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:130:  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:135:  (\S\ref{sec:method}, \texttt{NON\_EQUILIBRIUM\_FINDING.md}), the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:146:\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:156:\label{tab:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:181:(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:182:stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:184:any specific subject (\S\ref{sec:chain}). Three-way overlap on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:2:\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:88:\subsection{Interpretation}\label{ssec:interpretation}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:94:\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:96:\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:101:IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:110:\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:114:\subsection{Test/claim}\label{ssec:testclaim}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:120:\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:145:\subsection{State-drift / out-of-scope}\label{ssec:scope}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:167:  4-polytopes — see~\S\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:2:\section{Discussion}\label{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:47:(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:55:mechanism (\S\ref{sec:chain}) is functionally analogous to a workspace
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:76:\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:159:The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:181:  see \S\ref{sec:limitations}.)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:3:         replication}\label{sec:stress}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:20:(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:36:\label{tab:cxp_trend}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:70:\label{tab:cxp_means}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:137:\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:77:explicitly listed in~\S\ref{sec:limitations} and remain open.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:2:\section{The 600-cell response substrate}\label{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:5:This section constructs the substrate. \S\ref{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:6:gives the vertex set. \S\ref{ssec:graph} gives the graph and its
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:7:H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:9:\S\ref{ssec:shells} gives the 9-shell decomposition used for source
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:10:projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:11:descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:14:\subsection{Vertex construction}\label{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:31:\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:36:\begin{lemma}[600-cell graph facts]\label{lem:600cell}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:61:\S\ref{sec:chain}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:63:\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:67:\begin{equation}\label{eq:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:86:in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:89:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:98:varies between conditions in~\S\ref{sec:chain}; it is reported
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:101:\subsection{Shell decomposition}\label{ssec:shells}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:117:\subsection{Cascade descent (sketch)}\label{ssec:cascade}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:119:The recurrent layer in~\S\ref{sec:chain} references a cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:136:by the empirical correspondences in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:151:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:2:\section{Cross-domain selectivity}\label{sec:cross_domain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:5:This section reports three cross-domain witnesses. \S\ref{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:6:gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:8:\S\ref{ssec:hcp} gives the HCP brain-graph maximum-symmetry null.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:16:\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:40:\label{tab:chess_depth}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:60:\label{tab:chess_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:80:protocol (\S\ref{sec:method}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:95:\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:105:\label{tab:conv_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:131:            (P17--P18)}\label{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:140:$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:149:\label{tab:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:191:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:201:\label{tab:cross_domain_summary}

 succeeded in 475ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:84:$95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$, $n_{\mathrm{events}}=58$).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:86:subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:87:pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:34:WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:37:RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:67:   Sleep-EDFx $n=30$ CI~$[2.50, 2.86]$~\citep{BeggsPlenz2003,SleepEDFx} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:69:   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:104:P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:162:Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:163:ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:164:\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:169:The v4 WAKE 95\% CI $[1.82, 2.86]$ overlaps:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:170:(i) the real Sleep-EDFx EEG CI $[2.50, 2.53]$ (containing the upper
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:171:arm of the WAKE CI $[2.50, 2.86]$); (ii) the ARIA prior cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:172:pipeline CI $[2.73, 3.25]$; and (iii) the cortical-avalanche
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:87:| P6 | Real EEG α | ∈ [2.0, 3.0] | 2.513 ✅ | **2.513** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:219:- **P6**: Real EEG spindle α = 2.513 (n=30 subjects). Inside [2.0, 3.0].
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:37:| 6 | Cortical avalanche α | Sleep-EDFx n=30 (α=2.51 [2.50, 2.53]) | α ∈ [1.5, 3.5], R² > 0.85 | 2.252 [1.82, 2.86] R²=0.956 | ✓ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:40:**ARIA WAKE α CI [1.82, 2.86] overlaps real Sleep-EDFx EEG CI [2.50, 2.86]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:41:and the prior ARIA cascade-pipeline CI [2.73, 3.25] simultaneously.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:199:WAKE       58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:202:RECOVERY   58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:283:**Observed:** WAKE α = 2.252, 95% CI [1.82, 2.86], R² = 0.956 (n_events=58).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:286:- Real Sleep-EDFx EEG CI [2.50, 2.86] (n=30 subjects, prior preregistration)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:287:- ARIA prior cascade pipeline CI [2.73, 3.25]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:288:- v4 WAKE CI [1.82, 2.86]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:406:  (n=30 Sleep-EDFx, α=2.51 [2.50, 2.53])
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:416:power law in the wake-state band (passes with α = 2.252, 95% CI [1.82, 2.86]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:417:overlapping the real Sleep-EDFx CI [2.50, 2.86]), NREM-N3 variance collapse to

 succeeded in 484ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:20:       eighteen preregistered correspondences and six drug/sleep EEG\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:46:quantitative correspondences with neuroscience data — preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:57:neural dataset, is consistent with eighteen preregistered correspondences
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:72:preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:97:drug/sleep signatures pass at preregistered thresholds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:102:preregistered C$\times$P synergy prediction $\geq +0.10$ closes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:120:(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:121:descriptive statistics), the H$_4$-transitive substrate is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:123:$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:124:on degree homogeneity, $+79.78\sigma$ on participation ratio, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:125:$+6.80\sigma$ on clustering coefficient.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:137:is consistent with eighteen preregistered neuroscience
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:140:without modifying any preregistered threshold.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:174:preregistered validation, figure regeneration, this paper) is reproducible
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:179:$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:58:\caption{Chess preregistered tests (with reset, $n=25$ canonical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:77:lift at the same threshold the preregistered prediction set
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:104:\caption{Conversation preregistered tests.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:119:lift is $-4.4$pp, well within the preregistered neutrality band
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:125:selective-amplifier behaviour preregistered in 2026-04-18: a single
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:134:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:135:$n=100$ subjects for computational tractability, with full-cohort
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:136:$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:147:\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:148:$n=1003$ descriptive statistics.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:152:Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:154:Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:155:Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:156:Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:157:Clustering coefficient (descriptive)       & $0.455$ & $0.220$ & $+6.80\sigma$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:165:\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:166:  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:175:fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:176:homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:217:$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:21:predictions and rung observables — were preregistered on 2026-04-24
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:43:preregistered threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:60:P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:64:P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:71:P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:110:matrix. The preregistered test (P18) was on $n=100$ subjects for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:111:computational tractability; full-cohort $n=1003$ statistics
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:113:distances) are reported as descriptive statistics on top of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:114:preregistered test.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:135:preregistered cascade-$\alpha$ tests, 2000 resamples for the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:137:preregistered; 42 for the deep-dive.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:141:$0/2000$ were below the preregistered floor $+0.10$; we report these
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:156:on the full $n=1003$ subject distribution.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:170:preregistered floor). The reset protocol is documented in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:185:\item Eighteen preregistered:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:186:  \texttt{python3 run\_preregistered\_validation.py}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:13:> transitivity); HCP n=1003 degree std = 3.28 ± 0.28; ARIA is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:14:> −11.58σ on degree homogeneity and +79.78σ on participation ratio,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:27:1. **Chess pattern recognition** (P9–P13 in the preregistered set):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:42:   the Human Connectome Project (n=1003 subjects, ICA-50
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:47:preregistered tests on chess + conversation pass at fresh seeds; both
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:214:preregistered floor. The 65.4% null mapping shows two-thirds of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:262:preregistered window, and the negative sign suggests minor noise
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:301:substrate routing at 83.1% (lift −4.4pp) is within preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:311:**Reference cohort:** Human Connectome Project (HCP), n=1003 subjects.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:312:For preregistered tests, n=100 subjects (computational tractability)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:313:in ICA-50 parcellation. The full-cohort effects (n=1003) match the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:314:n=100 subset within standard error.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:340:**Result (n=100 subjects, density 0.101):** **3.388**.
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:418:ARIA's degree std = 0 (theorem); HCP n=1003 degree std = 3.28 ± 0.28,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:420:−11.58σ on degree homogeneity, +79.78σ on participation ratio, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:421:+6.80σ on clustering coefficient. The substrate functions as a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:440:is correctly null (lift −4.4pp, well within preregistered neutrality
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:442:unconditional booster. On HCP brain functional connectivity (n=1003,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:444:std = 0) is −11.58σ below the biological mean (3.28 ± 0.28); on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:445:participation ratio ARIA at 68.54 is +79.78σ above HCP (19.72 ± 0.61),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:446:and on clustering coefficient ARIA at 0.455 is +6.80σ above HCP (0.220).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:479:reference for biological cortex. The σ-distances (−11.58σ, +79.78σ,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:480:+6.80σ) quantify the magnitude of biological symmetry-breaking, with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:493:python3 run_preregistered_validation.py
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:502:- HCP n=100 ICA-50: deterministic from group average
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:509:JSON outputs land in `~/.aria/preregistered_validation/results_*.json`.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:551:- `run_preregistered_validation.py` — full P1–P18 harness
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:567:  preregistered tally
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:583:- `project_preregistered_validation_17_of_18.md` — re-run summary

codex
Line citations below use the filenames under the paths you supplied.

**1. Claim Audit**
- Fixed 600-cell graph facts: mostly established. `03_substrate.tex:36-48` states 120 vertices, 720 edges, degree 12, spectrum. This is fine as a construction/computation claim, but `03_substrate.tex:35` over-attributes it to transitivity; transitivity gives uniformity, not the whole spectrum by itself.
- `\Cph = \Lop + \Ph^{-2}I`: correctly scoped as a design-level stability shift at `03_substrate.tex:72-82`; no Lyapunov/first-principles derivation is claimed.
- “No fitted shape parameters / only eta and bounded_topk”: too strong in `main.tex:49-52`. The recurrent signatures also depend on condition-specific stimulus models and constants (`04_consciousness_chain.tex:125-148`), and the source says v4 closed gaps by redesigning stimulus models (`CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:25-28`).
- Six drug/sleep signatures: numbers are supported (`05_results.tex:34-69`; source `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:197-203`, `:211-283`), but “independent” and “preregistered thresholds” are too strong unless a dated preregistration for these six exists. The paper itself says they are not part of P1-P18 (`02_method.tex:27-33`).
- 18/18 preregistered tally: supported numerically by `VALIDATION_RESULTS_2026-04-29.md:7-15`, `:262-265`, but the abstract should explicitly preserve “17/18 standard; 18/18 with N=20 P4” rather than only “all eighteen pass” (`main.tex:71-77`).
- P13: major issue. Paper calls P13 “Chess LOO lift” (`02_method.tex:72`, `05_results.tex:111`, `07_cross_domain.tex:69`), but the preregistration says “+15pp on 5-fold CV” (`PAPER_PREDICTIONS.md:115-120`). Threshold matches; validation estimator does not.
- C×P synergy: point estimate/CI match source (`06_stress_tests.tex:92-99`; `P4_SYNERGY_FINDING.md:162-168`). But “trend is monotone-increasing” is false: +0.044 at N=3, +0.039 at N=5, +0.088 at N=10, +0.190 at N=20 (`06_stress_tests.tex:50`; source `P4_SYNERGY_FINDING.md:203-206`).
- Chess +40.6pp: correct against source (`07_cross_domain.tex:74-80`; `CROSS_DOMAIN_RESULTS.md:187-189`), with reset correctly disclosed.
- HCP: n=100 preregistered and n=1003 descriptive are correctly separated (`02_method.tex:108-114`, `07_cross_domain.tex:133-157`; source `CROSS_DOMAIN_RESULTS.md:311-314`, `:340`, `:360-362`). However participation ratio comparability between 120-node ARIA and ICA-50 HCP needs an explicit normalization/justification.
- Novelty claims are not established: `08_discussion.tex:21-24` and `10_conclusion.tex:79-82` require a literature audit or softening.

**2. Internal Consistency**
- Abstract does not explicitly state the required headline split: “17/18 standard; 18/18 with N=20 deep-dive” (`main.tex:71-77`). Section 5 does (`05_results.tex:83-87`).
- Bootstrap wording is mostly correct: `02_method.tex:139-143`, `06_stress_tests.tex:96-99`, `10_conclusion.tex:48-49`. But `06_stress_tests.tex:111-113` reintroduces P-notation; safer to use only “0/2000 resamples..., reported as 0.0000.”
- Real Sleep-EDFx CI is inconsistent. `05_results.tex:67` says `[2.50, 2.86]`, but the paper elsewhere says `[2.50, 2.53]` (`main.tex:85-87`, `05_results.tex:162`, `:170`) and the source table gives `[2.50, 2.53]` (`CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:37`, `:406`).
- P16 in the preregistration is “null mapping ≥50% on BOTH chess AND conversation” (`PAPER_PREDICTIONS.md:140-144`); the paper splits chess into P10 and conversation into P16. That is defensible, but note it explicitly.

**3. External Consistency / Numerics**
- 6/6 v4 signatures: match source for 0.463, 1.83x, +0.066, 0.33x, 0 diff, 2.252 `[1.82, 2.86]` (`CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:30-37`, `:211-283`; paper `05_results.tex:51-69`).
- Propofol switching: paper correctly uses 1.83x and treats 2.96x as empirical reference (`05_results.tex:54-56`; source `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:222-228`).
- 18/18: matches source (`VALIDATION_RESULTS_2026-04-29.md:80-99`, `:262-265`).
- C×P: +0.190 / `[+0.143,+0.239]` matches source (`P4_SYNERGY_FINDING.md:165-168`). Source uses finite-bootstrap P text; paper should keep the improved 0/2000 wording.
- Chess: +40.6pp at n=25 with reset matches source (`CROSS_DOMAIN_RESULTS.md:175-189`).
- HCP: -11.58σ / +79.78σ / +6.80σ match source (`CROSS_DOMAIN_RESULTS.md:360-362`).

**4. Substrate-Witness Scope Discipline**
Good overall. I found no direct claim that the substrate is consciousness, no delivered Lyapunov claim, no ACT selection theorem claim, and no uniqueness claim. The ACT bridge is explicitly non-load-bearing (`08_discussion.tex:91-117`). The main scope risks are indirect: “first deterministic geometric architecture” (`10_conclusion.tex:79-82`), “only when raw features are ambiguous” (`07_cross_domain.tex:122-128`), and HCP “far exceed any preprocessing-induced noise envelope” (`07_cross_domain.tex:175-178`).

**5. Tightness**
Suggested one-line edits:
- `main.tex:77`: “pass at empirical thresholds” -> “pass their preregistered thresholds after documented methodology refinements.”
- `05_results.tex:75`: “preregistered thresholds” -> “pre-specified signature thresholds” unless a dated preregistration exists.
- `06_stress_tests.tex:50`: replace monotone claim with “the estimate remains small at N=3/5 and rises at N=10/20.”
- `06_stress_tests.tex:13`, `10_conclusion.tex:51`: “Type II false negative” -> “consistent with an underpowered interaction estimate.”
- `07_cross_domain.tex:124`: “amplifies only when” -> “in these two tasks, amplifies when.”
- `07_cross_domain.tex:177`: replace preprocessing-noise claim with “large on the ICA-50 pipeline; cross-parcellation remains open.”

**6. Surface Issues**
- Macro usage for `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` is broadly consistent.
- Add citations for Global Workspace and predictive processing (`01_introduction.tex:5-8`, `08_discussion.tex:54-68`).
- Brodbeck 2012 is wake/NREM microstates (`references.bib:51-59`), not a propofol-specific microstate citation; add an anaesthesia/propofol microstate reference or soften (`02_method.tex:116-119`, `main.tex:165-166`).
- Several tables are likely overfull in two-column-like prose width, especially `02_method.tex:51-81`, `05_results.tex:42-73`, `07_cross_domain.tex:144-159`.
- Normalize capitalization: WAKE/SLEEP_N3/PROPOFOL vs Wake/NREM-N3/propofol.

**7. Top Three Fixes**
1. Fix P13 preregistration mismatch: either show that LOO was preregistered elsewhere, or report P13 as a validation-protocol refinement rather than “preregistered LOO” (`PAPER_PREDICTIONS.md:115-120`; paper `05_results.tex:111`).
2. Soften the six-signature claim: disclose stimulus-model redesign and single-seed status in the abstract/results, and avoid “independent/preregistered” unless documented (`main.tex:78-80`, `05_results.tex:75-79`, source `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:25-28`, `:371-376`).
3. Correct statistical overstatements: P4 monotone trend, Type II certainty, finite-bootstrap wording, Sleep-EDFx CI typo, and HCP noise/parcellation claims (`06_stress_tests.tex:50`, `:111-113`; `05_results.tex:67`; `07_cross_domain.tex:175-178`).

**8. Verdict**
Publication ready: no — must-fix list above. The paper is close in scope discipline, but P13 provenance, six-signature framing, and several statistical overstatements must be corrected before it is hostile-review-ready.
tokens used
153,569
Line citations below use the filenames under the paths you supplied.

**1. Claim Audit**
- Fixed 600-cell graph facts: mostly established. `03_substrate.tex:36-48` states 120 vertices, 720 edges, degree 12, spectrum. This is fine as a construction/computation claim, but `03_substrate.tex:35` over-attributes it to transitivity; transitivity gives uniformity, not the whole spectrum by itself.
- `\Cph = \Lop + \Ph^{-2}I`: correctly scoped as a design-level stability shift at `03_substrate.tex:72-82`; no Lyapunov/first-principles derivation is claimed.
- “No fitted shape parameters / only eta and bounded_topk”: too strong in `main.tex:49-52`. The recurrent signatures also depend on condition-specific stimulus models and constants (`04_consciousness_chain.tex:125-148`), and the source says v4 closed gaps by redesigning stimulus models (`CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:25-28`).
- Six drug/sleep signatures: numbers are supported (`05_results.tex:34-69`; source `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:197-203`, `:211-283`), but “independent” and “preregistered thresholds” are too strong unless a dated preregistration for these six exists. The paper itself says they are not part of P1-P18 (`02_method.tex:27-33`).
- 18/18 preregistered tally: supported numerically by `VALIDATION_RESULTS_2026-04-29.md:7-15`, `:262-265`, but the abstract should explicitly preserve “17/18 standard; 18/18 with N=20 P4” rather than only “all eighteen pass” (`main.tex:71-77`).
- P13: major issue. Paper calls P13 “Chess LOO lift” (`02_method.tex:72`, `05_results.tex:111`, `07_cross_domain.tex:69`), but the preregistration says “+15pp on 5-fold CV” (`PAPER_PREDICTIONS.md:115-120`). Threshold matches; validation estimator does not.
- C×P synergy: point estimate/CI match source (`06_stress_tests.tex:92-99`; `P4_SYNERGY_FINDING.md:162-168`). But “trend is monotone-increasing” is false: +0.044 at N=3, +0.039 at N=5, +0.088 at N=10, +0.190 at N=20 (`06_stress_tests.tex:50`; source `P4_SYNERGY_FINDING.md:203-206`).
- Chess +40.6pp: correct against source (`07_cross_domain.tex:74-80`; `CROSS_DOMAIN_RESULTS.md:187-189`), with reset correctly disclosed.
- HCP: n=100 preregistered and n=1003 descriptive are correctly separated (`02_method.tex:108-114`, `07_cross_domain.tex:133-157`; source `CROSS_DOMAIN_RESULTS.md:311-314`, `:340`, `:360-362`). However participation ratio comparability between 120-node ARIA and ICA-50 HCP needs an explicit normalization/justification.
- Novelty claims are not established: `08_discussion.tex:21-24` and `10_conclusion.tex:79-82` require a literature audit or softening.

**2. Internal Consistency**
- Abstract does not explicitly state the required headline split: “17/18 standard; 18/18 with N=20 deep-dive” (`main.tex:71-77`). Section 5 does (`05_results.tex:83-87`).
- Bootstrap wording is mostly correct: `02_method.tex:139-143`, `06_stress_tests.tex:96-99`, `10_conclusion.tex:48-49`. But `06_stress_tests.tex:111-113` reintroduces P-notation; safer to use only “0/2000 resamples..., reported as 0.0000.”
- Real Sleep-EDFx CI is inconsistent. `05_results.tex:67` says `[2.50, 2.86]`, but the paper elsewhere says `[2.50, 2.53]` (`main.tex:85-87`, `05_results.tex:162`, `:170`) and the source table gives `[2.50, 2.53]` (`CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:37`, `:406`).
- P16 in the preregistration is “null mapping ≥50% on BOTH chess AND conversation” (`PAPER_PREDICTIONS.md:140-144`); the paper splits chess into P10 and conversation into P16. That is defensible, but note it explicitly.

**3. External Consistency / Numerics**
- 6/6 v4 signatures: match source for 0.463, 1.83x, +0.066, 0.33x, 0 diff, 2.252 `[1.82, 2.86]` (`CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:30-37`, `:211-283`; paper `05_results.tex:51-69`).
- Propofol switching: paper correctly uses 1.83x and treats 2.96x as empirical reference (`05_results.tex:54-56`; source `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:222-228`).
- 18/18: matches source (`VALIDATION_RESULTS_2026-04-29.md:80-99`, `:262-265`).
- C×P: +0.190 / `[+0.143,+0.239]` matches source (`P4_SYNERGY_FINDING.md:165-168`). Source uses finite-bootstrap P text; paper should keep the improved 0/2000 wording.
- Chess: +40.6pp at n=25 with reset matches source (`CROSS_DOMAIN_RESULTS.md:175-189`).
- HCP: -11.58σ / +79.78σ / +6.80σ match source (`CROSS_DOMAIN_RESULTS.md:360-362`).

**4. Substrate-Witness Scope Discipline**
Good overall. I found no direct claim that the substrate is consciousness, no delivered Lyapunov claim, no ACT selection theorem claim, and no uniqueness claim. The ACT bridge is explicitly non-load-bearing (`08_discussion.tex:91-117`). The main scope risks are indirect: “first deterministic geometric architecture” (`10_conclusion.tex:79-82`), “only when raw features are ambiguous” (`07_cross_domain.tex:122-128`), and HCP “far exceed any preprocessing-induced noise envelope” (`07_cross_domain.tex:175-178`).

**5. Tightness**
Suggested one-line edits:
- `main.tex:77`: “pass at empirical thresholds” -> “pass their preregistered thresholds after documented methodology refinements.”
- `05_results.tex:75`: “preregistered thresholds” -> “pre-specified signature thresholds” unless a dated preregistration exists.
- `06_stress_tests.tex:50`: replace monotone claim with “the estimate remains small at N=3/5 and rises at N=10/20.”
- `06_stress_tests.tex:13`, `10_conclusion.tex:51`: “Type II false negative” -> “consistent with an underpowered interaction estimate.”
- `07_cross_domain.tex:124`: “amplifies only when” -> “in these two tasks, amplifies when.”
- `07_cross_domain.tex:177`: replace preprocessing-noise claim with “large on the ICA-50 pipeline; cross-parcellation remains open.”

**6. Surface Issues**
- Macro usage for `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` is broadly consistent.
- Add citations for Global Workspace and predictive processing (`01_introduction.tex:5-8`, `08_discussion.tex:54-68`).
- Brodbeck 2012 is wake/NREM microstates (`references.bib:51-59`), not a propofol-specific microstate citation; add an anaesthesia/propofol microstate reference or soften (`02_method.tex:116-119`, `main.tex:165-166`).
- Several tables are likely overfull in two-column-like prose width, especially `02_method.tex:51-81`, `05_results.tex:42-73`, `07_cross_domain.tex:144-159`.
- Normalize capitalization: WAKE/SLEEP_N3/PROPOFOL vs Wake/NREM-N3/propofol.

**7. Top Three Fixes**
1. Fix P13 preregistration mismatch: either show that LOO was preregistered elsewhere, or report P13 as a validation-protocol refinement rather than “preregistered LOO” (`PAPER_PREDICTIONS.md:115-120`; paper `05_results.tex:111`).
2. Soften the six-signature claim: disclose stimulus-model redesign and single-seed status in the abstract/results, and avoid “independent/preregistered” unless documented (`main.tex:78-80`, `05_results.tex:75-79`, source `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:25-28`, `:371-376`).
3. Correct statistical overstatements: P4 monotone trend, Type II certainty, finite-bootstrap wording, Sleep-EDFx CI typo, and HCP noise/parcellation claims (`06_stress_tests.tex:50`, `:111-113`; `05_results.tex:67`; `07_cross_domain.tex:175-178`).

**8. Verdict**
Publication ready: no — must-fix list above. The paper is close in scope discipline, but P13 provenance, six-signature framing, and several statistical overstatements must be corrected before it is hostile-review-ready.
