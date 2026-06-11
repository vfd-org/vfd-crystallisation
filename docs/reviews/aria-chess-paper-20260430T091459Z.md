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
session id: 019dddab-9105-79c2-8ee4-baecf74683fa
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

ROUND 3 verdict was 'Publication ready: no'. Round-3 must-fixes addressed:
- 600-cell Laplacian spectrum: WRONG IN ROUND 3 (multiplicities sum to 60, not 120). FIXED in §3 — replaced with computed spectrum {0^1, 2.292^4, 5.528^9, 9^16, 12^25, 14^36, 14.472^9, 15^16, 15.708^4} (sum=120) lifted from kernel script output. Removed lemma environment; replaced Lemma~\ref{lem:600cell} cross-references with §\ref{ssec:graph}. Abstract and §1 now say 'reported as observed' for spectrum.
- §1 'six independent' → 'six companion' (every occurrence).
- §1 'domain-invariant selective amplifier' → 'selective amplification in the two cross-domain tasks tested'.
- §4 stimulus-model 'not tuned to specific signatures' → discloses v3→v4 redesign as condition-specific design choices.
- §4 mechanisms 'not free dynamical choices' → 'targets are geometry-pinned; gains are fixed design choices; causal effects within the factorial ablation model'.
- §6 N≥20 over-broad → narrowed to 'in this cascade matrix specifically'.
- §7 cross-domain summary table 'raw vs null' → 'substrate vs null' (correct label).
- §7 HCP clustering: footnote disclosing missing explicit sd; back-calculation from σ noted.
- §8 Φ→0 'makes' → 'is designed to be small'.
- §10 added 'within the factorial ablation model'; HCP framing → 'full-cohort descriptive HCP n=1003'.

Verify each prior round-3 must-fix is closed. The biggest fix to verify: the spectrum in §3 ssec:graph and the corresponding text in main.tex headline. Flag any remaining issues; give verdict.
warning: Codex could not find bubblewrap on PATH. Install bubblewrap with your OS package manager. See the sandbox prerequisites: https://developers.openai.com/codex/concepts/sandboxing#prerequisites. Codex will use the vendored bubblewrap in the meantime.
codex
I’ll read the WO context first, then the LaTeX sections and source documents with line numbers so the review can cite exact locations. After that I’ll cross-check the stated numerics against the local source docs.
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "wc -l '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 175ms:
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

 succeeded in 244ms:
   267 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md
   142 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md
   205 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex
   168 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex
   200 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex
   173 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex
   197 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex
   203 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex
   168 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex
   265 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex
   203 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex
   190 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex
    95 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex
   180 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib
  2656 total

codex
The WO context confirms the load-bearing frame: this is a substrate-witness paper only, with exact numerics and explicit limitations doing most of the credibility work. I’m moving through the paper now, checking the revised spectrum and the prior round fixes first, then the result tables.
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md' | sed -n '260,290p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' | sed -n '1,240p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 349ms:
   260	- post-hoc N=20 P4 retest
   261	- 600-cell as post-hoc choice
   262	
   263	**SECTION E.** Missing-content check: anything from MANUSCRIPT_V2 that's WORKING-NOTES quality and needs actual writing for paper-grade prose.
   264	
   265	**SECTION F.** Top-3 build priorities with file:line anchors.
   266	
   267	Hostile-review framing throughout. Do not propose to add content beyond what the substrate-witness framing supports.

 succeeded in 335ms:
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
    39	Once the 600-cell substrate is chosen, its graph structure is fixed:
    40	$|V|=120$ vertices of uniform degree $12$ (forced by H$_4$ transitivity
    41	on the canonical short-edge nearest-neighbour graph), with
    42	$\Ph=(1+\sqrt 5)/2$ entering through the canonical vertex coordinates
    43	and through the response-operator stability shift $\Ph^{-2}$. The
    44	Laplacian spectrum is computed numerically from this graph and is
    45	reported as observed (\S\ref{sec:substrate}). Treated
    46	as an architectural-level substrate with a fixed shifted-Laplacian
    47	response $\Cph = \Lop + \Ph^{-2} I$ and a small dynamical layer above
    48	it, this single deterministic structure is consistent with eighteen
    49	quantitative correspondences with neuroscience data — preregistered
    50	on 2026-04-18 before any validation run — plus six drug/sleep EEG
    51	signatures of conscious vs unconscious states tested against
    52	published-reference thresholds on a single deterministic substrate
    53	trajectory at seed~$42$. No shape parameter is tuned to any neural
    54	dataset. The recurrent layer above the substrate adds one
    55	substrate-pinned nonlinearity $\mathrm{bounded\_topk}(\cdot, k\!=\!12)$
    56	at the graph's average degree and one condition-dependent self-injection
    57	coupling $\eta\!\in\!\{0, 0.05, 0.20\}$; condition-specific stimulus
    58	models (\S\ref{sec:chain}) are biologically-motivated design choices,
    59	not measurement-fits.
    60	
    61	\noindent\emph{Scope.}
    62	This paper presents an empirical \emph{substrate witness}: it shows
    63	that a geometry-fixed substrate, with no shape parameters tuned to any
    64	neural dataset, is consistent with eighteen preregistered correspondences
    65	and six EEG signatures. It is not a derivation of consciousness, nor a
    66	selection theorem, nor a uniqueness claim for the 600-cell among regular
    67	4-polytopes. The companion adaptive-closure-transport
    68	preprint~\citep{SmartAdaptiveClosureTransport2026} provides the
    69	4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which this substrate
    70	sits as the $L_M$ instance; the selection of the 600-cell as the active
    71	$M$ is treated as conjectural and is not load-bearing here.
    72	
    73	\begin{abstract}
    74	We test whether a geometry-fixed substrate — the 600-cell regular
    75	4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
    76	shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
    77	operator — is consistent with cortical signatures across five
    78	neuroscience domains. Eighteen quantitative predictions were
    79	preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
    80	before any validation run; each has a falsifiable threshold. The
    81	preregistered tally is $17/18$ at standard validation methodology
    82	($5$-seed cascade block plus state-reset protocol), and $18/18$ after
    83	a documented $N\!=\!20$ deep-dive on the residual high-variance
    84	interaction (P4); no preregistered threshold has been modified. We
    85	additionally report six drug/sleep EEG signatures tested on a recurrent
    86	self-model layer above the substrate, on a single deterministic
    87	trajectory at seed~$42$. The six signatures are not part of the
    88	P1--P18 preregistration; they are tested against published-reference
    89	thresholds (Sleep-EDFx, OpenNeuro, Brodbeck, Tononi) and were obtained
    90	under condition-specific stimulus models redesigned at v4 to be
    91	biologically realistic (\S\ref{sec:chain}).
    92	
    93	\noindent\emph{(i) Cortical avalanches.}
    94	Wake cascade-event power-law exponent $\alpha = 2.252$,
    95	$95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$, $n_{\mathrm{events}}=58$).
    96	This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
    97	subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
    98	pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
    99	overlap.
   100	
   101	\noindent\emph{(ii) Drug/sleep state transitions.}
   102	NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
   103	(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
   104	ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
   105	reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
   106	propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
   107	integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
   108	direction confirmed); recovery deterministically identical to wake.
   109	All six signatures pass against their published-reference thresholds
   110	on the single deterministic substrate trajectory.
   111	
   112	\noindent\emph{(iii) Causal mechanism isolation.}
   113	Two of four cascade mechanisms — context rotation $C$ and partial
   114	emission $P$ — are causally identifiable within the factorial
   115	ablation model, and the original preregistered C$\times$P synergy
   116	prediction $\geq +0.10$ closes
   117	decisively at adequate replication: $N\!=\!20$ fresh seeds give a
   118	bootstrap point estimate of $+0.190$ with $95\%$ CI $[+0.143, +0.239]$
   119	(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
   120	below zero, reported as $0.0000$. We document the original $N\!=\!3$
   121	underestimate ($+0.044$) as consistent with an underpowered interaction
   122	estimate at $N\!=\!3$. In this cascade matrix, P4 required $N\!=\!20$;
   123	future preregistrations on similar high-variance ablation matrices
   124	should budget for this scale.
   125	
   126	\noindent\emph{(iv) Cross-domain selectivity.}
   127	The substrate exhibits selective amplification in the two cross-domain
   128	tasks tested: chess 4-category position classification on
   129	8-dimensional V2 features lifts $+40.6$ percentage points on
   130	leave-one-out at canonical depth $n\!=\!25$ ticks (raw $53.1\%$
   131	$\to$ substrate-routed $93.8\%$, with state reset; the
   132	preregistered estimator P13 was $5$-fold CV with threshold
   133	$\geq\!+15$pp, the LOO finding above is a stricter validation-protocol
   134	refinement at the same threshold), while conversation utterance
   135	classification at raw $87.5\%$ yields a substrate lift of $-4.4$pp
   136	(threshold $|\cdot| < 10$pp), consistent with the substrate
   137	amplifying in these two tasks where raw features are ambiguous and
   138	remaining approximately neutral when raw features are already
   139	discriminative. On HCP brain functional connectivity
   140	(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
   141	descriptive statistics), the H$_4$-transitive substrate is a
   142	maximum-symmetry deterministic null reference: ARIA degree std
   143	$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
   144	on degree homogeneity, $+79.78\sigma$ on participation ratio, and
   145	$+6.80\sigma$ on clustering coefficient.
   146	
   147	\noindent\emph{What we do not claim.}
   148	We do not claim the 600-cell is the unique substrate consistent with
   149	these signatures, nor that other regular 4-polytopes (24-cell, 120-cell)
   150	have been ruled out. We do not derive the $\Ph^{-2}$ floor from
   151	first principles; it is a design-level stability clamp on the
   152	shifted-Laplacian response. The recurrent layer above the substrate
   153	is reported on a single deterministic trajectory; cross-seed CIs on
   154	the per-condition signatures are an explicit strengthening build.
   155	The structural scope of this paper is: \emph{a geometry-fixed
   156	substrate, with no shape parameters tuned to any neural dataset,
   157	is consistent with eighteen preregistered neuroscience
   158	correspondences and six drug/sleep EEG signatures, with all gaps in
   159	the original preregistration closed by methodology refinement and
   160	without modifying any preregistered threshold.}
   161	\end{abstract}
   162	
   163	% =====================================================================
   164	\input{sections/01_introduction.tex}
   165	\input{sections/02_method.tex}
   166	\input{sections/03_substrate.tex}
   167	\input{sections/04_consciousness_chain.tex}
   168	\input{sections/05_results.tex}
   169	\input{sections/06_stress_tests.tex}
   170	\input{sections/07_cross_domain.tex}
   171	\input{sections/08_discussion.tex}
   172	\input{sections/09_limitations.tex}
   173	\input{sections/10_conclusion.tex}
   174	% =====================================================================
   175	
   176	\section*{Acknowledgements}
   177	We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
   178	OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
   179	the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
   180	the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
   181	HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
   182	datasets that made these comparisons possible. Cortical avalanche
   183	methodology follows~\citep{BeggsPlenz2003}; the integrated-information
   184	$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
   185	the propofol microstate comparison uses Brodbeck et
   186	al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
   187	follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
   188	and processed data are released under MIT licence at the project
   189	repository~\citep{ariaChessRepo}.
   190	
   191	\section*{Reproducibility}
   192	The complete pipeline (substrate construction, six-signature
   193	consciousness chain, $N\!=\!20$ C$\times$P deep-dive, eighteen-prediction
   194	preregistered validation, figure regeneration, this paper) is reproducible
   195	from the project repository~\citep{ariaChessRepo} via the included
   196	\texttt{reproduce\_paper\_claims.sh} script. All scripts are
   197	deterministic given seeds; the substrate's spectral decomposition is
   198	cached at module level. Wallclocks: drug/sleep v4 $\sim 30$\,s;
   199	$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
   200	$\sim 18$\,min.
   201	
   202	\bibliographystyle{plainnat}
   203	\bibliography{references}
   204	
   205	\end{document}

 succeeded in 328ms:
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
    39	\paragraph{Graph facts (forced by the construction).}
    40	The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, and
    41	every vertex has degree exactly $12$ (H$_4$ transitivity acts on the
    42	vertex set; the short-edge nearest-neighbour graph inherits this
    43	uniformity). These facts are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}
    44	and reproduced numerically by
    45	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
    46	
    47	\paragraph{Laplacian spectrum (computed numerically).}
    48	The unweighted graph Laplacian $\Lop = D - A$ has nine distinct
    49	eigenvalues with multiplicities summing to $120$:
    50	\[
    51	\sigma(\Lop) \;=\;
    52	\bigl\{0^{1},\;
    53	       (12\!-\!6\Ph)^{4},\;
    54	       (12\!-\!4\Ph)^{9},\;
    55	       9^{16},\;
    56	       12^{25},\;
    57	       14^{36},\;
    58	       (4\Ph + 8)^{9},\;
    59	       15^{16},\;
    60	       (6\Ph + 6)^{4}\bigr\},
    61	\]
    62	i.e.\ approximately $\{0, 2.292, 5.528, 9, 12, 14, 14.472, 15, 15.708\}$
    63	with multiplicities $\{1, 4, 9, 16, 25, 36, 9, 16, 4\}$. We computed
    64	this directly from the constructed Laplacian
    65	(\texttt{kernel/vfd\_closure\_kernel.py:compute\_graph\_laplacian});
    66	the spectrum is reproducible at machine precision and matches H$_4$
    67	irrep block sizes. The exact closed forms of the entries in
    68	$\mathbb{Z}[\Ph]$ follow from H$_4$ character theory; we report them
    69	as observed and refer the interested reader to standard 600-cell
    70	references for derivations.
    71	
    72	\paragraph{H$_4$ irrep block decomposition.}
    73	The eigenspaces partition into H$_4$-proper and $\sigma$-twin Coxeter
    74	exponent classes. For H$_4$ proper the exponents are $\{1, 11, 19, 29\}$;
    75	for the Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism
    76	of $\mathbb{Z}[\Ph]$ the exponents become $\{7, 13, 17, 23\}$. The
    77	$\sigma$-orbit projector basis
    78	(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}) realises the block
    79	decomposition with cross-block norm $<10^{-15}$, providing a
    80	machine-precise structural index used by the recurrent layer in
    81	\S\ref{sec:chain} (the $K_{7}$-class projector is the default
    82	phenomenal-binding profile).
    83	
    84	\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
    85	
    86	The substrate's linear response to an external source $f \in \mathbb{R}^{120}$
    87	is the discrete Green's function of the shifted Laplacian:
    88	\begin{equation}\label{eq:cphi}
    89	\Cph \;=\; \Lop + \Ph^{-2} I,
    90	\qquad
    91	\psi \;=\; \Cph^{-1} f.
    92	\end{equation}
    93	The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
    94	clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
    95	$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
    96	inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
    97	\emph{not} a derived theorem; it is a stability choice. The companion
    98	kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
    99	$\Cph$ as the basis for an independent passive-regime witness in
   100	flavour physics~\citep{SmartBAnomaly2026}, where the same operator
   101	form (without retuning the shift) describes the
   102	$B\to K^{*}\mu^{+}\mu^{-}$ angular anomaly across five public datasets.
   103	This paper imports $\Cph$ from that line; we do not re-derive it.
   104	
   105	The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
   106	not produce critical-state cascade statistics; the recurrent layer
   107	in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
   108	$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
   109	event distributions. The choice $k\!=\!12$ is the average degree of
   110	$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate, not
   111	fitted to any dataset.
   112	
   113	\paragraph{Disclosure (substrate-witness scope).}
   114	The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
   115	The bounded-top-$K$ nonlinearity uses $k\!=\!12$ pinned to the graph's
   116	average degree, not a fitted threshold. No other shape parameter
   117	enters. The condition-dependent self-injection coupling
   118	$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
   119	varies between conditions in~\S\ref{sec:chain}; it is reported
   120	explicitly per condition.
   121	
   122	\subsection{Shell decomposition}\label{ssec:shells}
   123	
   124	Under the H$_3$ subgroup, the $120$ vertices partition into $9$
   125	spherical shells indexed by Euclidean inner product with a chosen pole:
   126	\[
   127	\bigl(|S_0|,\ldots,|S_8|\bigr) \;=\; (1, 12, 20, 12, 30, 12, 20, 12, 1).
   128	\]
   129	The middle shell $S_{4}$ has $30$ vertices on the equatorial plane
   130	(the icosidodecahedral ring). When projecting onto a continuum kernel
   131	in companion preprints~\citep{SmartAriaClosureKernel2026}, the
   132	shell-mean projection of the equatorial-source response,
   133	$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
   134	collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
   135	This paper does not use that continuum projection; we work with the
   136	discrete operator throughout.
   137	
   138	\subsection{Cascade descent (sketch)}\label{ssec:cascade}
   139	
   140	The recurrent layer in~\S\ref{sec:chain} references a cascade
   141	decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
   142	\to S^{7}\to 0$, implemented in
   143	\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
   144	An arbitrary operator on the $E_{8}$ root system descends to the
   145	4-D H$_4$ subspace through a sequence of orthogonal projections, each
   146	preserving the Frobenius norm to within $10^{-15}$. The
   147	$\sigma$-orbit projector basis from
   148	\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
   149	decomposition at machine precision.
   150	
   151	The descent provides numerical stability for the cascade ablations:
   152	when one ablates a specific K-class contribution (e.g.\ $K_{7}$), the
   153	remaining operator structure is exactly preserved. We do not claim
   154	the cascade itself is forced by physics on a pre-substrate level; the
   155	cascade is a decomposition of operators on $\Rsixhundred$, and the
   156	choice of $\Rsixhundred$ as the active substrate is post-hoc justified
   157	by the empirical correspondences in~\S\ref{sec:results}.
   158	
   159	\subsection{What the substrate is fixed-by, and what it is not}
   160	
   161	\begin{itemize}\itemsep=2pt
   162	\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
   163	  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
   164	  irrep block structure, average degree $k\!=\!12$, $\sigma$-twin pairing.
   165	\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
   166	  is not a derivation; it is a design-level clamp that bounds the
   167	  response inverse.
   168	\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
   169	  $24$-cell or $120$-cell. The choice is post-hoc motivated by the H$_4$
   170	  cascade structure and the empirical correspondences. A formal
   171	  ablation against alternative regular 4-polytopes is an open build
   172	  (\S\ref{sec:limitations}).
   173	\end{itemize}

 succeeded in 337ms:
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
    29	against eighteen preregistered correspondences plus six companion
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
    41	\item \textbf{Substrate is fixed once chosen.} Once $\Rsixhundred$
    42	  is selected, the vertex set ($|V|=120$, all on the unit
    43	  $3$-sphere) is forced by the canonical 600-cell construction; H$_4$
    44	  transitivity forces uniform vertex degree (here $12$ on the
    45	  short-edge nearest-neighbour graph); and the H$_4$ irrep block
    46	  structure is forced by character theory. The Laplacian spectrum
    47	  is computed numerically from the resulting graph and is reported
    48	  as observed (\S\ref{sec:substrate}). The response operator
    49	  $\Cph = \Lop + \Ph^{-2} I$ is fully fixed once the graph is
    50	  constructed and the stability shift $\Ph^{-2}$ is chosen as a
    51	  design-level clamp.
    52	\item \textbf{Cortical avalanches.} Wake cascade-event power-law
    53	  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
    54	  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
    55	  (n$=$30 subjects) and ARIA's prior cascade-pipeline CI
    56	  $[2.73, 3.25]$.
    57	\item \textbf{Six drug/sleep signatures.} On a single deterministic
    58	  trajectory at seed $42$: NREM-N3 phenomenal-intensity variance
    59	  collapse to $0.463\!\times$ wake; propofol modality-switching
    60	  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
    61	  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
    62	  recovery deterministically identical to wake; wake cascade-$\alpha$
    63	  in the SOC band.
    64	\item \textbf{Eighteen preregistered correspondences pass.}
    65	  $17/18$ at standard methodology; $18/18$ after a documented
    66	  $N\!=\!20$ deep-dive on the residual high-variance interaction
    67	  test; \emph{no preregistered threshold has been modified}.
    68	\item \textbf{Cross-domain selectivity.} The substrate exhibits
    69	  selective amplification in the two cross-domain tasks tested
    70	  (chess $+40.6$pp leave-one-out lift at depth $n\!=\!25$ ticks;
    71	  conversation $-4.4$pp lift, within preregistered neutrality bounds)
    72	  and serves as a maximum-symmetry deterministic null reference for
    73	  cortical functional connectivity (HCP full-cohort descriptive
    74	  $n\!=\!1003$: ARIA at $-11.58\sigma$ on degree homogeneity;
    75	  $+79.78\sigma$ on participation ratio).
    76	\end{enumerate}
    77	
    78	\subsection*{What this paper does \emph{not} claim}
    79	
    80	\begin{itemize}\itemsep=2pt
    81	\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
    82	  the unique substrate consistent with these signatures. Other regular
    83	  4-polytopes (the 24-cell, the 120-cell) are an explicit ablation
    84	  build, not a discharged comparison. The 600-cell choice is post-hoc
    85	  motivated by the H$_4$ Coxeter cascade structure and biological
    86	  observables; it is not an a-priori derivation from first principles.
    87	\item \emph{Not a derivation of consciousness.} The substrate witness
    88	  shows quantitative agreement with cortical signatures; it does not
    89	  establish that the substrate \emph{is} consciousness, nor that
    90	  its dynamics implement specific phenomenal content.
    91	\item \emph{Not a selection theorem.} The companion adaptive-closure-
    92	  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
    93	  proposes a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which
    94	  this substrate fills the $L_M$ slot. The selection of the 600-cell
    95	  as the active $M$ is conjectural in that paper and is treated as
    96	  non-load-bearing here. We do not deliver a Lyapunov function on the
    97	  reduced flow, nor a $2I$-equivariance audit of the closure operator,
    98	  nor a formal edge-space decomposition. These are listed as open
    99	  builds in~\S\ref{sec:limitations}.
   100	\item \emph{Not a circuit-level model.} The substrate is at the
   101	  architectural-algorithmic level. We do not identify which neural
   102	  populations implement context rotation or partial emission, only
   103	  that some such mechanisms appear in the substrate's preregistered
   104	  ablation matrix and exhibit strong inter-mechanism coupling.
   105	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
   106	  Laplacian floor $\Ph^{-2} \approx 0.382$ is a design-level
   107	  stability clamp (it makes $\Cph$ strictly positive definite and
   108	  bounds the Green response). It is not derived as a theorem from a
   109	  closure functional. The companion kernel
   110	  document~\citep{SmartAriaClosureKernel2026} discusses its role.
   111	\end{itemize}
   112	
   113	\subsection*{Mapping from numerical results to admissible claims}
   114	
   115	To keep this paper inside the substrate-witness scope, we use the
   116	following claim-boundary discipline. Numerical results
   117	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   118	$\mathcal C_{\mathrm{admissible}}$ by the rule
   119	\[
   120	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow \mathcal C_{\mathrm{admissible}},
   121	\qquad
   122	\mathcal C_{\mathrm{admissible}}
   123	\;=\;\{\text{`consistent with', `inside threshold', `direction confirmed'}\}.
   124	\]
   125	We never write `the substrate \emph{is} cortex' or `derives consciousness'.
   126	A result that lands inside its preregistered threshold licenses a
   127	`consistent with' claim. A result that exceeds the preregistered
   128	threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
   129	$+15$pp floor) licenses `decisively above prereg', not `proves'. A
   130	$\sigma$-distance result against an external null
   131	(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
   132	the biological distribution', not `cortex has drifted from an ideal
   133	polytope'. The claim-boundary rule is summarised in the box below
   134	and applied throughout~\S\ref{sec:results}.
   135	
   136	\medskip
   137	\begin{center}
   138	\fbox{\parbox{0.92\linewidth}{\small
   139	\textbf{What is tested / what is not claimed.}\par
   140	\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
   141	signatures, on a geometry-fixed substrate with one condition-dependent
   142	parameter $\eta$ and one graph-pinned nonlinearity, against published
   143	biological observables.\par
   144	\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
   145	selection theorem on the 4-tuple bridge; circuit-level mechanistic
   146	identification; first-principles derivation of $\Ph^{-2}$ shift;
   147	that cortex \emph{is} the 600-cell.
   148	}}
   149	\end{center}
   150	
   151	\subsection*{Layout}
   152	
   153	\S\ref{sec:method} gives the provenance ledger (preregistration date,
   154	seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
   155	constructs $\Rsixhundred$ and the response operator $\Cph$, with the
   156	$\Ph^{-2}$ shift disclosed as a design-level stability clamp.
   157	\S\ref{sec:chain} adds the recurrent self-model layer above the
   158	substrate (single nonlinearity, single self-injection coupling).
   159	\S\ref{sec:results} reports the empirical tables: six drug/sleep
   160	signatures, eighteen preregistered correspondences, three-way
   161	$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
   162	synergy stress test ($N\!=\!3, 5, 10, 20$ trend with bootstrap
   163	$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
   164	selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
   165	discusses the substrate witness and proposes a non-load-bearing
   166	ACT bridge (without claiming a selection theorem).
   167	\S\ref{sec:limitations} enumerates limitations and the
   168	hostile-review guard matrix. \S\ref{sec:conclusion} concludes.

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex' | sed -n '1,240p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex' | sed -n '1,240p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 233ms:
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
    57	$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate
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
   149	The v4 stimulus models were redesigned after diagnostics on the
   150	v3 stimulus models (which produced 4/6 signatures) to use
   151	biologically-motivated stimulus components — AR(1) cortical noise,
   152	attention episodes, slow-wave drive, spindles, K-complexes — at
   153	amplitudes and durations matching published biological time scales.
   154	They are not fitted to subject-level measurements, but they are
   155	condition-specific design choices iterated to close v3 stimulus-model
   156	artefacts (\texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} documents
   157	the v3$\to$v4 redesign). The full stimulus code is
   158	\texttt{demo\_drug\_sleep\_v4.py}.
   159	
   160	\subsection{Cascade-mechanism ablation matrix}
   161	
   162	The cascade dynamics on the substrate use four mechanisms acting on
   163	the pressure field, each ablatable independently. The $2^{4}$
   164	ablation grid is the basis for the preregistered tests P1--P5 and
   165	the C$\times$P stress test in~\S\ref{sec:stress}.
   166	
   167	\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains
   168	five disjoint 24-cells (D$_4$ orbits). $D$ adds a small
   169	(coupling $0.05$) cross-orbit pressure averaging that prevents
   170	cascades from localising to one orbit.
   171	Implementation: \texttt{kernel/dimensional\_monitor.py:300-305}.
   172	
   173	\textbf{$C$ — Context rotation (S$^{7}$ observer frames).} The active
   174	observer frame on the S$^{7}$ rung rotates periodically based on
   175	which uncrossed vertices have accumulated pressure aligning with
   176	each frame's preferences. This creates churn in \emph{which}
   177	vertices are uncrossed at any tick.
   178	Implementation: \texttt{kernel/dimensional\_monitor.py:316-318, 823-827}.
   179	
   180	\textbf{$P$ — Partial emission.} High-pressure uncrossed vertices
   181	(above threshold but not yet crossed) emit pressure at $30\%$ scale,
   182	saturating at pressure $3.0$. Without this mechanism, only fully-
   183	crossed vertices emit.
   184	Implementation: \texttt{kernel/dimensional\_monitor.py:842-855}.
   185	
   186	\textbf{$E$ — Equator compensation.} The H$_3$ shell-4 equator is a
   187	30-vertex icosidodecahedral ring with split degree distribution.
   188	$E$ scales pressure gain by $(\bar d / d_{v})$ so sparse commissural
   189	vertices overcome their connectivity deficit.
   190	Implementation: \texttt{kernel/dimensional\_monitor.py:320-360}.
   191	
   192	The four mechanisms' \emph{targets} are geometry-pinned (D$_4$ orbits,
   193	$S^{7}$ rung, equatorial shell); their gains and coupling constants
   194	($D$ at $0.05$, $P$ at $30\%$ scale saturating at pressure $3.0$,
   195	$C$ rotation period, $E$ degree-ratio multiplier) are fixed design
   196	choices reported here, not learned from data. Their causal effects
   197	within the factorial ablation model are reported in~\S\ref{sec:stress}.

 succeeded in 248ms:
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

 succeeded in 283ms:
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
   198	(\S\ref{ssec:graph}); the $\Ph^{-2}$ shift in $\Cph$ is a
   199	stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
   200	biological time-scale parameters but is not measurement-fitted to
   201	any specific subject (\S\ref{sec:chain}). Three-way overlap on the
   202	power-law exponent is the strongest single empirical anchor in the
   203	paper.

 succeeded in 308ms:
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
   158	practice on this cascade-ablation matrix specifically: in this matrix,
   159	P4 ($C\times P$) required $N\!=\!20$ fresh seeds for reliable detection
   160	at the preregistered threshold; P3 ($D\times C$) closed at $N\!=\!5$.
   161	The original 3-seed preregistered validation gave estimates consistent
   162	with underpowered detection on both interaction tests; both close at
   163	higher $N$ without threshold modification. The general lesson: when
   164	preregistering an interaction effect on a system with unknown
   165	per-seed variance, budget the seed count from a power-analysis
   166	assumption that the per-seed std could be as large as the interaction
   167	effect itself. Future preregistrations on similar high-variance
   168	ablation matrices should plan for this scale.

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex' | sed -n '1,320p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex' | sed -n '1,240p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex' | sed -n '1,140p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 229ms:
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
    48	wake). The $\Phi$ proxy (\S\ref{sec:chain}) is designed to be small
    49	under H$_4$-equivariant dynamics and to increase when dynamics
    50	produce cross-class asymmetries. ARIA does not implement the full
    51	IIT axioms (cause-effect repertoires, exclusion postulate,
    52	integration-over-partitions); it reproduces an observable consequence
    53	on the propofol--wake state contrast. This is a consistency-of-direction
    54	result, not a discharge of IIT.
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
   147	\item \textbf{$N\!\geq\!20$ for similar high-variance ablation matrices.}
   148	  Allocation discipline for preregistration: in this cascade-ablation
   149	  matrix specifically, P4 ($C\!\times\!P$) required $N\!=\!20$ for
   150	  reliable detection at the preregistered threshold. The general
   151	  rule we draw — when preregistering an interaction effect on a
   152	  system with unknown per-seed variance, budget for at least this
   153	  scale — should be tested against other ablation matrices, not
   154	  taken as universal. The original 3-seed plan was the source of two
   155	  underpowered-interaction estimates in this work.
   156	\item \textbf{State-reset protocol on non-stationary substrates.}
   157	  ARIA's substrate is a non-stationary dynamical system; the
   158	  pressure field equilibrates within $\sim 5$ successive evaluations.
   159	  Any multi-trial benchmark must specify a state-reset protocol or
   160	  document the drift. Generalisable lesson: \emph{published
   161	  cross-domain benchmarks on non-stationary substrates should report
   162	  an explicit reset/equilibration discipline}, not just seed.
   163	\end{enumerate}
   164	
   165	\subsection{The substrate as a maximum-symmetry connectivity null}
   166	
   167	The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
   168	deterministic null reference for cortical functional connectivity.
   169	Real cortex breaks the symmetry through hub-spoke functional
   170	specialisation; the $\sigma$-distances from ARIA quantify the
   171	magnitude of biological symmetry-breaking with no fitted parameters.
   172	
   173	This is a methodological contribution to comparative connectomics.
   174	Stochastic nulls (Erd\H{o}s--R\'enyi, configuration model,
   175	edge-randomised graphs) compare cortex to a random graph with matched
   176	density. ARIA is a different kind of null: a deterministic
   177	group-theoretic graph with theorem-level statements of structure
   178	(degree std $=\!0$ by transitivity, eigenvalue spectrum
   179	$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$ by character
   180	theory). Both null kinds are useful; ARIA gives a specific,
   181	reproducible, group-theoretic baseline that cortex deviates from in
   182	quantifiable $\sigma$-units.
   183	
   184	\subsection{Open questions raised by the substrate witness}
   185	
   186	\begin{itemize}\itemsep=2pt
   187	\item Do the six drug/sleep signatures replicate across $10$--$20$
   188	  cross-seed runs of the recurrent layer? (Single-seed disclosure;
   189	  see \S\ref{sec:limitations}.)
   190	\item Do alternative regular 4-polytopes ($24$-cell, $120$-cell)
   191	  reproduce comparable signature sets, or is the $600$-cell
   192	  distinguished?
   193	\item Does the strong-coupling reading ($C\!\times\!P$) survive an
   194	  independent fresh-seed $N\!=\!20$ replication at a different seed
   195	  range?
   196	\item Does the substrate's amplifier behaviour transfer to other
   197	  ambiguous-feature classification tasks beyond chess (e.g.\ visual
   198	  pattern, audio classification)?
   199	\item Does the Sleep-EDFx three-way CI overlap survive on a different
   200	  EEG cohort (TUH, NHM)?
   201	\end{itemize}
   202	We list these as open questions raised by the witness, not as gaps
   203	in the witness itself.

 succeeded in 238ms:
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
   156	$\Lop$. By H$_4$ transitivity (\S\ref{ssec:graph}) every vertex
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
   173	Clustering coefficient (descriptive)$^{\flat}$ & $0.455$ & $0.220$ & $+6.80\sigma$ \\
   174	\bottomrule
   175	\end{tabular}
   176	\end{table}
   177	
   178	\noindent$^{\flat}$ The HCP across-subject standard deviation for the
   179	clustering coefficient is not separately reported in
   180	\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
   181	from the same descriptive analysis as the other rows. Inferred from
   182	the reported gap and $\sigma$, the implicit HCP sd is
   183	$\approx 0.235/6.80\!\approx\!0.035$. We carry the $\sigma$-distance
   184	forward as reported and flag the missing explicit sd here.
   185	
   186	\begin{itemize}\itemsep=2pt
   187	\item P17 (ARIA degree std, theorem): predicted $=0$, observed
   188	  $0.0000$, $\checkmark$.
   189	\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
   190	  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
   191	  HCP subjects have degree std below $2.0$.
   192	\end{itemize}
   193	
   194	\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
   195	structure is a deterministic group-theoretic null reference for
   196	cortical functional connectivity. Real cortex breaks the symmetry
   197	through hub-spoke functional specialisation; the $\sigma$-distances
   198	quantify the magnitude of biological symmetry-breaking with no
   199	fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
   200	homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
   201	clustering coefficient) are large on the ICA-50 pipeline at the
   202	density-matched threshold $\rho = 0.101$; cross-parcellation
   203	replication (Schaefer, Glasser) remains an open build.
   204	
   205	\textbf{Participation-ratio comparability.} ARIA's vertex graph has
   206	$120$ nodes; the HCP ICA-50 connectivity matrix has $50$ nodes. The
   207	participation-ratio statistic
   208	$\mathrm{PR}(G) = (\sum_{i} d_{i})^{2} / \sum_{i} d_{i}^{2}$ is
   209	node-count-dependent — its theoretical maximum is the node count of
   210	the graph. We report the raw $\mathrm{PR}$ values
   211	($\mathrm{ARIA}=68.54$ on a 120-node graph; $\mathrm{HCP}=19.72$ on a
   212	50-node graph) and the $\sigma$-distance against the HCP
   213	across-subject distribution, but the $+79.78\sigma$ value reflects
   214	both the architectural difference and the differing node counts. A
   215	node-count-normalised statistic
   216	$\mathrm{PR}/|V|$ gives $\mathrm{ARIA}=0.571$ vs $\mathrm{HCP}=0.394$,
   217	a smaller absolute gap; we keep the raw-PR comparison as headline
   218	because the HCP subject distribution and the across-subject
   219	$\sigma$ are computed in the same units, but flag the node-count
   220	caveat here.
   221	
   222	\textbf{What we do not claim.}
   223	\begin{itemize}\itemsep=2pt
   224	\item We do not claim cortex has ``drifted from an ideal polytope'';
   225	  the substrate is a useful a-priori null whose deviation from real
   226	  cortex is precisely measurable.
   227	\item We do not claim parcellation invariance: the $\sigma$-distances
   228	  are reported on ICA-50; alternative parcellations (Schaefer,
   229	  Glasser) would give different per-metric numbers but, on the
   230	  basis of the qualitative pattern that cortex is hub-concentrated
   231	  relative to ARIA's transitive null, we expect them to preserve the
   232	  signs. Verification across parcellations is an open build
   233	  (\S\ref{sec:limitations}).
   234	\end{itemize}
   235	
   236	\subsection{Cross-domain summary as a selective amplifier
   237	            \texorpdfstring{$+$}{+} maximum-symmetry null}
   238	
   239	\begin{table}[ht]
   240	\centering
   241	\small
   242	\caption{Cross-domain summary on a single substrate.}
   243	\label{tab:cross_domain_summary}
   244	\begin{tabular}{l r r r r r}
   245	\toprule
   246	Task & Raw & Substrate & Null perm. & Geom.\ floor & Sem.\ alignment \\
   247	\midrule
   248	Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
   249	Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\
   250	Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (substrate vs null) \\
   251	\bottomrule
   252	\end{tabular}
   253	\end{table}
   254	
   255	The geometric content ($\approx 65$--$71\%$ across the two domains)
   256	is the architecture-invariant null floor. The semantic content
   257	($12$--$18$pp) is the domain-specific contribution. On HCP,
   258	$\sigma$-distances against the biological cohort are
   259	$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
   260	clustering coefficient).
   261	
   262	\textbf{Headline cross-domain reading.} The substrate is
   263	\emph{selectively} amplifying (not unconditionally), and it is a
   264	maximum-symmetry deterministic null on connectivity (not a fitted
   265	model). Both readings sit inside the substrate-witness scope.

 succeeded in 219ms:
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
    48	causally identifiable within the factorial ablation model and exhibit
    49	strong synergy: their interaction $\Delta_{CP}\!=\!+0.190$ at
    50	$N\!=\!20$ ($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples
    51	at or below zero, reported as $0.0000$) is comparable in magnitude to
    52	the $P$ main effect $-0.218$. The original 3-seed estimate ($+0.044$)
    53	is consistent with an underpowered interaction estimate on a
    54	high-per-seed-variance term ($\mathrm{std}=0.089$ at $N\!=\!20$); we
    55	contribute the $N\!\geq\!20$ minimum as a preregistration-practice
    56	recommendation for similar high-variance ablation matrices.
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
    68	on the full-cohort descriptive HCP $n\!=\!1003$ statistics
    69	(preregistered test on the $n\!=\!100$ subset), ARIA's H$_4$-transitive
    70	structure is at $-11.58\sigma$ on degree homogeneity,
    71	$+79.78\sigma$ on participation ratio (with the node-count caveat of
    72	\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
    73	
    74	\textbf{Substrate-witness scope.} This is a substrate witness, not a
    75	derivation of consciousness, not a selection theorem on the
    76	companion adaptive-closure-transport
    77	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
    78	uniqueness claim for the 600-cell among regular 4-polytopes. The
    79	strengthening builds — cross-seed CIs on the recurrent-layer
    80	signatures, alternative-polytope ablations, an independent $N\!=\!20$
    81	C$\times$P replication at a different seed range, cross-parcellation
    82	HCP replication, a Lyapunov function on the reduced flow,
    83	$2I$-equivariance audit of the closure operator family — are
    84	explicitly listed in~\S\ref{sec:limitations} and remain open.
    85	
    86	We are not aware of a prior deterministic geometric architecture
    87	tested against this many preregistered cortical correspondences from
    88	a graph fixed by group theory with no shape parameters tuned to
    89	neural data; we cannot rule out that such prior work exists. The empirical material
    90	gathered here is the substrate witness; the broader programme to
    91	turn the witness into a selection-theorem-grade claim — including the
    92	independent passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$
    93	flavour anomaly~\citep{SmartBAnomaly2026} on the same response
    94	operator $\Cph$ — is sketched in the companion preprints and remains
    95	the natural next step.

 succeeded in 227ms:
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
    44	cortical input is much richer. The v4 stimulus models were redesigned
    45	after diagnostics on the v3 stimulus models to close v3 stimulus-model
    46	artefacts; v4 components are biologically-motivated and not fitted
    47	to subject-level measurements, but they are condition-specific
    48	design choices iterated to v4. \emph{Disclosure:}~\S\ref{sec:chain}
    49	explicitly frames v4 as a redesign. \emph{Evidence:} amplitudes and
    50	durations match published biological time scales; the v3$\to$v4
    51	diff is captured in
    52	\texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}. \emph{Strengthening
    53	build:} replication on stimulus models derived from anatomically-grounded
    54	input statistics (e.g.\ retinotopic, tonotopic).
    55	
    56	\subsection{Post-hoc}\label{ssec:posthoc}
    57	
    58	\textbf{The 600-cell choice is post-hoc justified by empirical
    59	observables.} While the construction of $\Rsixhundred$ is theorem-
    60	level rigorous (H$_4$ Coxeter group theory), the choice of \emph{this}
    61	polytope as the consciousness-substrate instance is motivated by the
    62	correspondences observed, not by an a-priori biological argument.
    63	\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
    64	derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
    65	preregistered correspondences plus six signatures; the H$_4$
    66	transitivity theorem ($P17$). \emph{Strengthening build:} comparison
    67	with the $24$-cell and $120$-cell on the same signatures; formal
    68	ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
    69	(deferred).
    70	
    71	\textbf{Cascade decomposition is one of several possible
    72	decompositions of H$_4$.} We use the $\sigma$-orbit projector basis
    73	because it is machine-precise and biologically informative, but other
    74	bases (character-theoretic, Galois-twin) give the same physical
    75	predictions through different intermediate variables. \emph{Disclosure:}
    76	\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
    77	\emph{Evidence:} block-diagonalisation at $<10^{-15}$ cross-block
    78	norm. \emph{Strengthening build:} catalogue and equivalence-prove the
    79	admissible decompositions.
    80	
    81	\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
    82	$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
    83	strictly positive definite (\S\ref{ssec:cphi}); it is not derived
    84	from a closure functional or symmetry argument. \emph{Disclosure:}
    85	\S\ref{ssec:cphi} marks this as a design-level choice; the companion
    86	kernel doc~\citep{SmartAriaClosureKernel2026} explicitly does not
    87	derive it. \emph{Evidence:} the same operator (with the same shift)
    88	serves as the basis for the b-anomaly passive-regime
    89	witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
    90	derive the $\Ph^{-2}$ shift as the unique stability clamp under a
    91	named regularity criterion.
    92	
    93	\subsection{Interpretation}\label{ssec:interpretation}
    94	
    95	\textbf{The recurrent layer is a method, not a metaphysics claim.}
    96	We do not claim the recurrent self-model layer ``is'' consciousness;
    97	we claim quantitative consistency with six published biological
    98	signatures on a deterministic trajectory. \emph{Disclosure:}
    99	\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
   100	\emph{Evidence:} six signatures vs published thresholds.
   101	\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
   102	formal account of which substrate observables map to which phenomenal
   103	contents (the bind\_phenomenal\_field channels) is not delivered.
   104	
   105	\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
   106	IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
   107	\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
   108	matches IIT direction. \emph{Strengthening build:} a
   109	\texttt{phi\_iit\_full} implementation following Balduzzi--Tononi
   110	2008~\citep{BalduzziTononi2008} on the substrate; not delivered.
   111	
   112	\textbf{HCP $\sigma$-distances are descriptive, not normative.} We
   113	do not claim ``cortex has drifted from an ideal polytope''; we
   114	quantify the distance between cortex and the deterministic H$_4$ null.
   115	\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
   116	$\sigma$-distances on three independent metrics. \emph{Strengthening
   117	build:} cross-parcellation replication (Schaefer, Glasser).
   118	
   119	\subsection{Test/claim}\label{ssec:testclaim}
   120	
   121	\textbf{Two preregistered interaction tests required higher $N$
   122	than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
   123	$N\!=\!20$. We document this transparently as a Type II
   124	methodology issue, not a threshold change. \emph{Disclosure:}
   125	\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
   126	\emph{Evidence:} bootstrap CI fully above the $+0.10$ floor; per-seed
   127	distribution narrow at $N\!=\!20$ ($\mathrm{std}=0.089$);
   128	$19/20$ seeds positive. \emph{Strengthening build:} a second
   129	$N\!=\!20$ run at a different seed range (e.g.\ $33000$--$33019$);
   130	an $N\!=\!50$ characterisation of the per-seed distribution.
   131	
   132	\textbf{The original 2026-04-20 walks-back are reversed without
   133	threshold modification.} The reversals (P3, P4, P13) are documented
   134	in
   135	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md} with
   136	the original failure values, the methodology refinement, and the
   137	post-refinement values. \emph{Disclosure:} this paper carries those
   138	disclosures verbatim. \emph{Evidence:} 2026-04-20 vs 2026-04-29 side-
   139	by-side results table. \emph{Strengthening build:} the strengthening
   140	builds for P3/P4/P13 above; no further claim is needed.
   141	
   142	\textbf{Bayesian and full-IIT inference not performed.} All intervals
   143	are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
   144	proxy, not the Balduzzi--Tononi 2008 algorithm. \emph{Disclosure:}
   145	this section. \emph{Strengthening build:} Bayesian posterior on
   146	$\Delta_{CP}$; full-IIT computation on the $S^{4}\!\to\!2^{4}$
   147	substrate state space. The latter is computationally heavy and is
   148	deferred.
   149	
   150	\subsection{State-drift / out-of-scope}\label{ssec:scope}
   151	
   152	\textbf{Single condition-dependent parameter $\eta$ is not derived
   153	as a learned variable.} $\eta\in\{0, 0.05, 0.20\}$ across PROPOFOL,
   154	SLEEP\_N3, and WAKE/RECOVERY is a condition-dependent constant in
   155	this paper, not a learned trajectory. A predictive-processing
   156	extension where $\eta$ adapts on an error norm is an open build.
   157	
   158	\textbf{No deuteron / hadron / RH / capstone material is loaded into
   159	this paper.} The companion programme (cascade-derivation, capstone
   160	coalgebra, RH formal) shares operator-level infrastructure but is not
   161	load-bearing here. Deliberately out of scope.
   162	
   163	\textbf{Out-of-scope items NOT delivered (correctly).}
   164	\begin{itemize}\itemsep=2pt
   165	\item Aria-chess active-regime companion analysis on chess move-by-move
   166	  trajectories (this paper covers static positions only).
   167	\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under
   168	  $2I$-equivariance — open build of the ACT companion paper.
   169	\item Lyapunov derivation $V(W)$ from a closure functional
   170	  $\mathcal{F}$ — open build of the ACT companion paper.
   171	\item Selection theorem for $\Rsixhundred$ over alternative regular
   172	  4-polytopes — see~\S\ref{ssec:regime}.
   173	\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
   174	  of the six signatures.
   175	\item Cross-parcellation replication of the HCP $\sigma$-distances
   176	  (Schaefer, Glasser, etc.).
   177	\item Bayesian posterior on the C$\times$P interaction.
   178	\end{itemize}
   179	
   180	\subsection{The honest verdict}
   181	
   182	The result is a substrate witness: a geometry-fixed substrate, with
   183	no shape parameters tuned to any neural dataset, is consistent with
   184	eighteen preregistered correspondences and six companion drug/sleep
   185	EEG signatures, with all original gaps closed by methodology
   186	refinement and without modifying any preregistered threshold. We do
   187	not claim the substrate \emph{is} consciousness. We do not claim a
   188	selection theorem on the ACT bridge. We do not claim uniqueness for
   189	$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
   190	for these stronger claims are listed above and remain open.

codex
The revised paper now has explicit disclaimers in the abstract, introduction, stress-test, ACT bridge, and limitations. I’ve found one visible carryover already: the conclusion still prints the old/incomplete spectrum set, so I’m checking all remaining numerics and wording for similar stale references.
exec
/bin/bash -lc "rg -n \"six independent|domain-invariant|not tuned to specific|not free dynamical|free dynamical|N\\\\s*\\\\\\\\geq\\\\s*20|N\\\\s*≥\\\\s*20|raw vs null|2\\.96|\\+27\\.2|n=15|P=0|P\\(.*0\\)|unique|selection theorem|Lyapunov|is consciousness|600-cell is|spectrum|\\{0, 3, 4\\\\Ph|18/18|17/18|threshold\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"Ph|Lop|Cph|Rsixhundred|\\\\varphi|V_\\{600\\}|C_\\{\\\\Ph\\}|C_\\\\varphi|L_\\{V_\\{600\\}\\}\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"undefined|TODO|FIXME|citation|citep\\{|cite\\{|ref\\{|label\\{|begin\\{|end\\{\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib' | sed -n '1,230p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 2 in 188ms:
rg: regex parse error:
    (?:six independent|domain-invariant|not tuned to specific|not free dynamical|free dynamical|N\s*\\geq\s*20|N\s*≥\s*20|raw vs null|2\.96|\+27\.2|n=15|P=0|P\(.*0\)|unique|selection theorem|Lyapunov|is consciousness|600-cell is|spectrum|\{0, 3, 4\Ph|18/18|17/18|threshold)
                                                                                                                                                                                                                                                       ^^^
error: Unicode property not found

 exited 2 in 181ms:
rg: regex parse error:
    (?:Ph|Lop|Cph|Rsixhundred|\varphi|V_\{600\}|C_\{\Ph\}|C_\varphi|L_\{V_\{600\}\})
                                                    ^^^
error: Unicode property not found

 succeeded in 182ms:
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

 succeeded in 244ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:32:\begin{document}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:45:reported as observed (\S\ref{sec:substrate}). Treated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:58:models (\S\ref{sec:chain}) are biologically-motivated design choices,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:68:preprint~\citep{SmartAdaptiveClosureTransport2026} provides the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:73:\begin{abstract}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:91:biologically realistic (\S\ref{sec:chain}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:161:\end{abstract}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:177:We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:178:OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:179:the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:180:the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:181:HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:183:methodology follows~\citep{BeggsPlenz2003}; the integrated-information
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:184:$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:186:al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:187:follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:189:repository~\citep{ariaChessRepo}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:195:from the project repository~\citep{ariaChessRepo} via the included
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:205:\end{document}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:2:\section{Discussion}\label{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:9:preprint~\citep{SmartAdaptiveClosureTransport2026}. We do not claim a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:16:\begin{enumerate}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:42:\end{enumerate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:46:\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:48:wake). The $\Phi$ proxy (\S\ref{sec:chain}) is designed to be small
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:56:\textbf{vs Global Workspace Theory.}~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:57:The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:64:\textbf{vs Predictive Processing.}~\citep{FristonFreeEnergy2010,ClarkPP2013}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:80:\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:83:preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:103:\begin{itemize}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:113:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:117:document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:119:anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:146:\begin{enumerate}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:163:\end{enumerate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:167:The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:186:\begin{itemize}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:189:  see \S\ref{sec:limitations}.)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:201:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:3:         replication}\label{sec:stress}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:21:(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:33:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:37:\label{tab:cxp_trend}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:38:\begin{tabular}{r l r l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:48:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:49:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:69:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:73:\label{tab:cxp_means}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:74:\begin{tabular}{l r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:83:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:84:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:96:\begin{itemize}\itemsep=1pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:103:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:139:\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:142:\begin{itemize}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:148:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:2:\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:12:\subsection{Regime}\label{ssec:regime}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:20:(\S\ref{sec:intro}). \emph{Evidence:} empirical correspondences hold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:27:six-signature results in~\S\ref{ssec:six_signatures} are reported on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:32:in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:48:design choices iterated to v4. \emph{Disclosure:}~\S\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:56:\subsection{Post-hoc}\label{ssec:posthoc}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:63:\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:68:ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:76:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:83:strictly positive definite (\S\ref{ssec:cphi}); it is not derived
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:85:\S\ref{ssec:cphi} marks this as a design-level choice; the companion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:86:kernel doc~\citep{SmartAriaClosureKernel2026} explicitly does not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:89:witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:93:\subsection{Interpretation}\label{ssec:interpretation}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:99:\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:101:\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:106:IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:110:2008~\citep{BalduzziTononi2008} on the substrate; not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:115:\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:119:\subsection{Test/claim}\label{ssec:testclaim}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:125:\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:150:\subsection{State-drift / out-of-scope}\label{ssec:scope}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:164:\begin{itemize}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:172:  4-polytopes — see~\S\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:178:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:2:\section{Cross-domain selectivity}\label{sec:cross_domain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:5:This section reports three cross-domain witnesses. \S\ref{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:6:gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:8:\S\ref{ssec:hcp} gives the HCP brain-graph maximum-symmetry null.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:16:\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:35:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:40:\label{tab:chess_depth}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:41:\begin{tabular}{r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:52:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:53:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:55:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:60:\label{tab:chess_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:61:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:71:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:72:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:94:(\S\ref{sec:method}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:109:\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:115:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:119:\label{tab:conv_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:120:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:128:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:129:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:144:(\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:147:            (P17--P18)}\label{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:150:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:156:$\Lop$. By H$_4$ transitivity (\S\ref{ssec:graph}) every vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:160:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:165:\label{tab:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:166:\begin{tabular}{l r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:175:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:176:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:186:\begin{itemize}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:192:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:223:\begin{itemize}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:233:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:234:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:239:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:243:\label{tab:cross_domain_summary}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:244:\begin{tabular}{l r r r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:252:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:253:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:2:\section{Results}\label{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:7:(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:20:(\S\ref{sec:chain}). Per-condition trajectory observables are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:24:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:29:\label{tab:per_condition}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:30:\begin{tabular}{l r r l r r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:39:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:40:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:42:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:46:\label{tab:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:47:\begin{tabular}{c l l c c l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:52:   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:55:   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:58:   EEG microstate~\citep{Brodbeck2012Microstates} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:61:   Tononi 2008~\citep{Tononi2008} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:67:   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:72:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:73:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:80:(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:84:\S\ref{sec:limitations}~\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:86:\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:94:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:98:\label{tab:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:99:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:123:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:124:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:130:\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:134:\begin{itemize}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:141:  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:150:  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:153:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:162:\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:167:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:172:\label{tab:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:173:\begin{tabular}{l c l c}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:178:Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:182:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:183:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:189:$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:198:(\S\ref{ssec:graph}); the $\Ph^{-2}$ shift in $\Cph$ is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:199:stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:201:any specific subject (\S\ref{sec:chain}). Three-way overlap on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:2:\section{The recurrent layer}\label{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:5:The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:6:cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:17:signatures in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:23:\begin{align}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:29:\end{align}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:38:\begin{itemize}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:43:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:57:$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:88:machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:89:collapse in~\S\ref{sec:results} is consistent with the IIT direction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:99:\begin{align*}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:105:\end{align*}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:165:the C$\times$P stress test in~\S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:197:within the factorial ablation model are reported in~\S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:2:\section{The 600-cell response substrate}\label{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:5:This section constructs the substrate. \S\ref{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:6:gives the vertex set. \S\ref{ssec:graph} gives the graph and its
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:7:H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:9:\S\ref{ssec:shells} gives the 9-shell decomposition used for source
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:10:projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:11:descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:14:\subsection{Vertex construction}\label{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:17:$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:19:\begin{itemize}\itemsep=1pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:25:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:31:\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:38:spectrum are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:43:uniformity). These facts are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:81:\S\ref{sec:chain} (the $K_{7}$-class projector is the default
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:84:\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:88:\begin{equation}\label{eq:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:92:\end{equation}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:98:kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:100:flavour physics~\citep{SmartBAnomaly2026}, where the same operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:107:in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:110:$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:119:varies between conditions in~\S\ref{sec:chain}; it is reported
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:122:\subsection{Shell decomposition}\label{ssec:shells}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:131:in companion preprints~\citep{SmartAriaClosureKernel2026}, the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:138:\subsection{Cascade descent (sketch)}\label{ssec:cascade}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:140:The recurrent layer in~\S\ref{sec:chain} references a cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:157:by the empirical correspondences in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:161:\begin{itemize}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:172:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:173:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:72:\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:77:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:84:explicitly listed in~\S\ref{sec:limitations} and remain open.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:93:flavour anomaly~\citep{SmartBAnomaly2026} on the same response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:6:(Integrated Information Theory~\citep{Tononi2008,BalduzziTononi2008},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:7:Global Workspace Theory~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:8:predictive processing~\citep{FristonFreeEnergy2010,ClarkPP2013}) and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:23:over a century~\citep{CoxeterRegularPolytopes,Weisstein600Cell}; to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:40:\begin{enumerate}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:48:  as observed (\S\ref{sec:substrate}). The response operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:76:\end{enumerate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:80:\begin{itemize}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:92:  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:99:  builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:110:  document~\citep{SmartAriaClosureKernel2026} discusses its role.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:111:\end{itemize}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:134:and applied throughout~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:137:\begin{center}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:149:\end{center}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:153:\S\ref{sec:method} gives the provenance ledger (preregistration date,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:154:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:157:\S\ref{sec:chain} adds the recurrent self-model layer above the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:159:\S\ref{sec:results} reports the empirical tables: six drug/sleep
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:161:$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:163:$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:164:selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:167:\S\ref{sec:limitations} enumerates limitations and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:168:hostile-review guard matrix. \S\ref{sec:conclusion} concludes.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:2:\section{Methods and provenance}\label{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:25:listed as future strengthening builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:51:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:55:\label{tab:provenance}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:56:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:65:P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:77:P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:81:\end{tabular}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:82:\end{table}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:87:recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:91:methodology~\citep{BeggsPlenz2003}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:94:consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:100:EEG~\citep{OpenNeuroDS004902},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:105:release~\citep{ZenodoDMT3992359},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:109:S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:118:Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:121:as a propofol reference. A propofol-specific microstate citation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:176:generalisable lesson is recorded in \S\ref{sec:limitations}: any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:182:\begin{itemize}\itemsep=2pt
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:194:\end{itemize}

exec
/bin/bash -lc "rg -n -F \"six independent\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"domain-invariant\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"not tuned to specific signatures\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"raw vs null\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"P=0\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"+27.2\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 333ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:146:as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact

 exited 1 in 371ms:
 exited 1 in 385ms:
 exited 1 in 321ms:
 exited 1 in 348ms:
 exited 1 in 361ms:
exec
/bin/bash -lc "rg -n -F \"N\\"'!'"\\geq\\"'!20" '"'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"N\\"'!='"\\"'!20" '"'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"2.96\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"n\\"'!='"\\"'!15" '"'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"spectrum\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"{0, 3, 4\\Ph\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 450ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:105:reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:55:   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:97:($2.96\!\times$ wake) in Sig~2.

 succeeded in 466ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:83:a documented $N\!=\!20$ deep-dive on the residual high-variance
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:117:decisively at adequate replication: $N\!=\!20$ fresh seeds give a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:122:estimate at $N\!=\!3$. In this cascade matrix, P4 required $N\!=\!20$;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:193:consciousness chain, $N\!=\!20$ C$\times$P deep-dive, eighteen-prediction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:199:$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:66:  $N\!=\!20$ deep-dive on the residual high-variance interaction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:30:  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:128:one we held until the $N\!=\!20$ deep-dive — is that these are mostly
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:130:$N\!=\!20$ result reverses this on the substrate: $C$ and $P$ are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:149:  matrix specifically, P4 ($C\!\times\!P$) required $N\!=\!20$ for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:194:  independent fresh-seed $N\!=\!20$ replication at a different seed
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:39:(b)~adding a $N\!=\!20$ deep-dive for the highest-variance interaction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:140:$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:187:\item C$\times$P synergy $N\!=\!20$ deep-dive:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:90:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:107:   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:140:  ($+0.044$) and at $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:157:requiring $N\!\geq\!5$ and one requiring $N\!=\!20$ for reliable
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:15:confidence interval on a fresh-seed $N\!=\!20$ sample. We did all
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:52:($+0.044, +0.039$) and rises at $N\!=\!10$ and $N\!=\!20$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:54:$N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$ sample landed on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:55:outliers; the $N\!=\!20$ sample reveals a clean narrow positive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:58:\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:67:\textbf{Per-condition means at \texorpdfstring{$N\!=\!20$}{N=20}.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:86:\textbf{Main effects at \texorpdfstring{$N\!=\!20$}{N=20}.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:130:\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:135:(i) a second independent $N\!=\!20$ run at a different seed range
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:159:P4 ($C\times P$) required $N\!=\!20$ fresh seeds for reliable detection
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:123:$N\!=\!20$. We document this transparently as a Type II
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:127:distribution narrow at $N\!=\!20$ ($\mathrm{std}=0.089$);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:129:$N\!=\!20$ run at a different seed range (e.g.\ $33000$--$33019$);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:37:$N\!\geq\!5$ and $N\!=\!20$ respectively for reliable detection of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:50:$N\!=\!20$ ($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:54:high-per-seed-variance term ($\mathrm{std}=0.089$ at $N\!=\!20$); we
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:80:signatures, alternative-polytope ablations, an independent $N\!=\!20$

 succeeded in 491ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:55:contribute the $N\!\geq\!20$ minimum as a preregistration-practice
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:32:  underpowered ablation and emerged only at $N\!\geq\!20$ — a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:38:  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:147:\item \textbf{$N\!\geq\!20$ for similar high-variance ablation matrices.}

 exited 1 in 500ms:
 succeeded in 476ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:179:$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$ by character
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:13:$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$) is fixed by

 succeeded in 489ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:44:Laplacian spectrum is computed numerically from this graph and is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/paper_summary.md:30:  spectrum-preserving (z=191-302) — a genuine phase-amplitude
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/paper_summary.md:46:| Paired-eigenvalue torus signature | **8 visible pairs** | `run_h4_lyapunov_spectrum.py` — PC1:PC2 = 0.99987, …, 8 paired modes |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/paper_summary.md:165:2. **Full Lyapunov spectrum** via QR/Gram-Schmidt (we have finite-diff only;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/paper_summary.md:177:run_artifacts/h4_lyapunov_spectrum.json — dynamical systems
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/results.json:980:        "experiment": "Lyapunov spectrum + velocity covariance eigenspectrum",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/results.json:1018:        "artifact_path": "run_artifacts/h4_lyapunov_spectrum.json",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/results.json:1022:        "experiment": "H\u2084 Oscillator power spectrum \u2014 1/f^\u03b1 scaling & Berry harmonics",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/results.json:1048:        "artifact_path": "run_artifacts/h4_power_spectrum.json",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/results.json:1052:        "experiment": "H\u2084 Oscillator power spectrum \u2014 1/f^\u03b1 scaling & Berry harmonics",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/results.json:1078:        "artifact_path": "run_artifacts/h4_power_spectrum.json",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/results.json:3885:        "interpretation": "H3 Berry deformation opens an orthogonal Phi-sensitive channel, producing a predeclared 22x lift at k=0.25 with paired-t p=3.4e-5 (Wilcoxon p=2e-4) over n=20 seeds, but does NOT close the cross-rung gap because Frobenius MI falls by 40% (0.046 -> 0.027). Codex verdict: publishable as mechanistic ablation, not headline. Non-monotonic k_h3 response (peak at 0.25, dip at 0.5, recovery at 1.0 with 3x variance) matches the predicted competition story: weak H3 forcing injects curvature; stronger H3 reorganises into its own dominant channel. k=1.0 outliers (seeds 100, 4001 at 10x median Phi) flag possible regime bistability, pending norms/spectrum diagnostics. First non-null endofunctor result in the arc (WO-001 and all post-hoc v1/v2/v3 were null on specificity). Demonstrates the product-vs-coherent-endofunctor hypothesis is testable and yields measurable effects, but the specific mechanism required to lift Phi WITHOUT Frob MI cost remains open.",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/results.json:4560:        "interpretation": "Methodological priority-1 gap closed per Codex consensus. Berry-forced Tort PAC (MI=0.044) survives all three standard PAC surrogate controls at p<0.01 across 5/5 seeds: phase-shuffle (z>165k, null=0), time-shift (z=16-59, null=2.6e-4), IAAFT-spectrum-preserving (z=191-302, null=2.3e-4). The cortical-range Tort PAC is a genuine phase-amplitude relationship, not filter leakage, waveform sharpness, shared-harmonic artefact, or narrowband resonance. Worst-case p=0.002 (time-shift seed 811). IAAFT is the gold-standard control (Schreiber & Schmitz 2000) because it preserves both power spectrum and amplitude distribution of the \u03b3-envelope while randomising phases \u2014 the most stringent test for phase-amplitude coupling.",
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:46:  structure is forced by character theory. The Laplacian spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:7:H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:31:\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:38:spectrum are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:47:\paragraph{Laplacian spectrum (computed numerically).}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:66:the spectrum is reproducible at machine precision and matches H$_4$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:163:  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:178:(degree std $=\!0$ by transitivity, eigenvalue spectrum
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:12:($120$ vertices, uniform degree $12$, Laplacian spectrum

exec
/bin/bash -lc "wc -l '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"6/6|SIGNATURE|WAKE|SLEEP_N3|PROPOFOL|RECOVERY|2\\.252|3\\.250|2\\.758|0\\.463|1\\.83|2\\.96|0\\.066|0\\.33|seed 42|v3|v4\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"18/18|17/18|P1|P2|P3|P4|P13|threshold|modified|0\\.190|0\\.143|0\\.239|40\\.6|3\\.388|1003|100\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"0\\.190|0\\.143|0\\.239|0/2000|P\\(|p_value|N=20|32000|32019|19/20|0\\.089|0\\.159|0\\.044|0\\.039|0\\.088|3\\.008|3\\.464|2\\.790|3\\.628\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 353ms:
1:# Consciousness Chain v4 — Six EEG Signatures Reproduced
5:single deterministic substrate; architecture is unchanged from v3 (the chain
20:The six signatures span four conditions (WAKE, SLEEP_N3, PROPOFOL, RECOVERY)
25:The result extends v3 (4/6, where the two partials were cleanly diagnosed as
26:stimulus-model artefacts in `demo_wake_alpha_diagnosis.py`) to 6/6 by
27:replacing v3's stylised stimulus models with biologically realistic ones —
32:| 1 | Sleep variance ratio | NREM-N3 EEG (Lee 2017, Jobst 2017) | ratio ≈ 0.365 | 0.463 | ✓ within 30% |
33:| 2 | Propofol switching ↑ | OpenNeuro ds005620 (n=8, 2.96×) | ratio in [1.5, 5.0] | 1.83× | ✓ |
34:| 3 | Propofol continuity ↓ | EEG microstate (Brodbeck 2012) | drop > 0.020 | +0.066 | ✓ |
35:| 4 | Propofol Φ collapse | IIT prediction (Tononi 2008) | ratio < 0.5 | 0.33× | ✓ |
37:| 6 | Cortical avalanche α | Sleep-EDFx n=30 (α=2.51 [2.50, 2.53]) | α ∈ [1.5, 3.5], R² > 0.85 | 2.252 [1.82, 2.86] R²=0.956 | ✓ |
40:**ARIA WAKE α CI [1.82, 2.86] overlaps real Sleep-EDFx EEG CI [2.50, 2.86]
46:## Architecture (unchanged from v3)
48:The chain has three modules. They were established in v3
49:(`project_consciousness_chain_v3_eeg_match.md`) and are fixed across v4:
67:`demo_diagnose_architecture.py` and is documented in v3 memory.
70:- η = 0.20 for WAKE, RECOVERY (active recurrent self-loop)
71:- η = 0.05 for SLEEP_N3 (attenuated self-loop)
72:- η = 0.00 for PROPOFOL (broken recurrence — preserves residual cortex)
105:## Stimulus models — biologically realistic (v4)
107:The architecture above is fixed; v4 replaces the v3 stylised stim models
109:`demo_drug_sleep_v4.py`.
111:### WAKE — AR(1) cortical noise + tonic shell + attention episodes
154:### SLEEP_N3 — slow waves + spindles + K-complexes
158:(sharp transients). All three are present in the v4 model:
174:The v3 model used `sparse weak pulses every 5th tick at amplitude 0.3` —
175:too quiet. v4's slow-wave amplitude (1.0) and K-complex amplitude (0.8) move
176:the variance ratio from v3's 0.23 (over-collapsed) into the predicted window.
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
300:## How the v4 stimulus model was derived
302:v3 (`demo_drug_sleep_v3.py`) reached 4/6. Two partials remained:
306:`demo_wake_alpha_diagnosis.py` tested four hypotheses against the v3 result:
315:The diagnostic settled the substrate question: pure-random WAKE drive lands
317:avalanches under realistic noise, and v3's "miss" was a stim-mixing artefact.
319:But pure-random WAKE alone fails the propofol contrast tests (sigs 2-4) —
320:WAKE looks identical to PROPOFOL because both are just random tonic noise.
324:The final v4 design was reached after five iterations:
325:- **v4.0**: AR(1) + salient single-tick events → attention shifts inflated WAKE switching past PROPOFOL (sig 2 fail)
326:- **v4.1**: Pure random WAKE → α clean but propofol contrast collapses (sigs 2,3,4 fail)
327:- **v4.2**: AR(1) + episodes 6-12 ticks amp 0.8 → 4/6, modality still hopping
328:- **v4.3**: Episodes 40-80 ticks amp 1.5 → too sticky, only 11 events for fit (sig 6 fail)
329:- **v4.final**: AR(1) β=0.90 + tonic shell + episodes 20-50 amp 0.8 anchored to shell + within-shell rotation → 6/6
340:python3 demo_drug_sleep_v4.py
350:- v3 PROPOFOL α should be 2.758 [2.52, 3.09] R²=0.931 — unchanged from v3 across this work.
356:**What v4 demonstrates:**
360:- Architecture established in v3 is sufficient; only stim realism was
361:  needed to close the v3 gap.
364:**What v4 does NOT demonstrate:**
368:- The Sig 2 ratio (1.83×) is below the empirical point estimate (2.96×)
371:- The model is single-seed at this point. v4 should be re-run with 5–10
386:| `demo_drug_sleep_v4.py` | The 6/6 demo script — single deterministic run |
387:| `demo_wake_alpha_diagnosis.py` | The diagnostic that proved v3 partials were stim artefacts |
388:| `demo_drug_sleep_v3.py` | Prior 4/6 result (kept for comparison) |
399:- `project_consciousness_chain_v4_six_of_six.md` — this work
400:- `project_consciousness_chain_v3_eeg_match.md` — v3 architecture (4/6)
404:- `project_propofol_empirical_5.md` — empirical anchor for Sig 2 (n=8, 2.96×)
416:power law in the wake-state band (passes with α = 2.252, 95% CI [1.82, 2.86]
419:1.83×), propofol continuity disruption (passes at +0.066), propofol Φ collapse
420:in the IIT direction (passes at 0.33× wake), and recovery reversibility (passes
421:exactly). The architecture is unchanged from v3; only the stimulus models —
426:and reproduced from `demo_drug_sleep_v4.py` at seed = 42.

 succeeded in 399ms:
  1253 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md
   426 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md
   435 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md
   584 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md
   399 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md
   194 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md
   257 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md
  3548 total

 succeeded in 427ms:
5:plus the N=20 deep-dive on the residual P4 prediction.*
8:> 18 / 18 with N=20 deep-dive on the residual P4.** Original 15/18
15:> set is fully validated against preregistered thresholds.
25:Each prediction has a falsifiable threshold (numerical band or
38:- All cascade main effects passed (P1, P2, P5).
40:- All cross-domain tests passed at fresh seeds (P9, P10, P11, P12,
41:  P14, P15, P16, P17, P18).
43:  - **P3** (D×C interaction independence): observed −0.231 at N=3,
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
83:| P2 | Context-rotation main effect | ≥ +0.30 | +0.588 ✅ | **+0.621** | ✅ |
84:| P3 | \|D×C interaction\| (independence) | \|·\| < 0.20 | −0.231 ❌ | **−0.183** | ✅ |
85:| P4 | C×P synergy | ≥ +0.10 | +0.044 ❌ | **+0.190 at N=20, CI [+0.143, +0.239]** | ✅ at N=20 |
91:| P10 | Chess null mapping | ≥ 50% | 65.4% ✅ | **65.4%** | ✅ |
92:| P11 | Chess random-label | ∈ [15%, 35%] | 23.4% ✅ | **23.4%** | ✅ |
93:| P12 | Chess goldilocks peak | ∈ {15, 25, 40, 60} | n=15 ✅ | **n=25** | ✅ |
94:| P13 | Chess LOO substrate lift | ≥ +15pp (with reset) | +3.1pp ❌ | **+40.6pp** | ✅ |
95:| P14 | Conv raw 5-fold CV | ≥ 75% | 87.5% ✅ | **87.5%** | ✅ |
96:| P15 | \|conv substrate lift\| | \|·\| < 10pp | −4.4pp ✅ | **−4.4pp** | ✅ |
97:| P16 | Conv null mapping | ≥ 50% | 70.6% ✅ | **70.6%** | ✅ |
98:| P17 | ARIA degree std (theorem) | = 0.00 | 0.0000 ✅ | **0.0000** | ✅ |
99:| P18 | HCP ICA-50 degree std | > 2.0 | 3.388 ✅ | **3.388** | ✅ |
105:### 3.1 P3 — D×C interaction independence
116:seeds tightens the estimate enough to land inside the threshold.
120:interaction estimate is approximately 0.06–0.10; the threshold is
126:threshold. We do not claim point-zero independence (the estimate is
130:### 3.2 P4 — C×P synergy
133:`P4_SYNERGY_FINDING.md` for the full story.
137:**Original (N=3) failure:** +0.044. Below threshold.
139:**2026-04-29 re-run (N=5):** +0.039. Still below threshold — confirming
145:C×P bootstrap mean:           +0.190
146:C×P 95% bootstrap CI:         [+0.143, +0.239]
151:The 95% CI is **entirely above the preregistered +0.10 threshold**.
161:`P4_SYNERGY_FINDING.md` for the mechanistic interpretation.
163:### 3.3 P13 — Chess LOO substrate lift
167:**Original (N=1) failure:** +3.1pp. Far below threshold.
170:measurements):** **+40.6pp**.
176:  n=25:   93.8%   ← peak (P12 goldilocks)
179:  n=100:  78.1%
181:Lift at n=25 = 93.8% − 53.1% = +40.6pp
187:40, 60, 100) without reset, so by the time it reached n=25 the substrate
207:### 4.1 Cascade geometry (P1, P2, P5)
209:- **P1**: Baseline α at 5 seeds = 2.958 (vs original 3.020 at 3 seeds).
211:- **P2**: Context-rotation main effect = +0.621 at 5 seeds (vs +0.588
212:  at 3 seeds). Both above the +0.30 dominance threshold.
225:### 4.3 Chess closed-loop (P9, P10, P11, P12, plus P13 fixed)
229:- **P10**: Null feature→frame permutation (15 trials) = 65.4%
233:- **P11**: Random-label baseline (20 trials) = 23.4% (∈ [15%, 35%]).
235:- **P12**: Goldilocks peak depth = n=25 (∈ {15, 25, 40, 60}). With
237:- **P13**: LOO substrate lift at n=25 = **+40.6pp** with reset
240:### 4.4 Conversation closed-loop (P14, P15, P16)
242:- **P14**: Conv raw 5-fold CV = 87.5% (≥ 75%). Already saturated at
244:- **P15**: Conv substrate lift = −4.4pp (\|·\| < 10pp). The substrate
248:- **P16**: Conv null feature→frame (15 trials) = 70.6% (≥ 50%).
252:### 4.5 HCP brain-graph comparison (P17, P18)
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
288:> homeostatic reset between LOO depth measurements) give 17/18; the
289:> residual prediction (P4 — C×P synergy) requires higher-N replication
291:> interaction-term estimates. With adequate N, P4 passes decisively
292:> (+0.190, 95% bootstrap CI [+0.143, +0.239]); the synergy is in fact
304:### 6.1 Original walk-back on P3 (D×C independence)
313:### 6.2 Original walk-back on P4 (C×P synergy)
318:**Now reads:** C×P synergy is +0.190 [+0.143, +0.239] at N=20, ~90%
323:### 6.3 Original walk-back on P13 (chess LOO lift)
332:is +40.6pp.
339:with falsifiable thresholds, frozen before any validation run — is
341:re-run with N improvements **did not modify any threshold or claim
343:reset. The fact that this gave 18/18 (with N=20 P4) where the
355:adequate power. No threshold was loosened. No prediction was rewritten
364:# Standard validation (17/18, ~18 min)
368:# P4 N=20 deep-dive (~28 min)
387:- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — standalone N=20 report

 succeeded in 421ms:
3:*Standalone publishable finding from N=20 seed deep-dive on the residual P4
9:> on cascade-α is +0.190, 95% bootstrap CI [+0.143, +0.239]** — comparable
94:N=20 deep-dive presented below shows this was wrong.**
98:## 2. The N=20 deep-dive (2026-04-29)
104:- **N = 20 fresh seeds** (range 32000–32019, non-overlapping with prior
119:one-sided P(interaction ≤ 0) and P(interaction < +0.10).
125:### 2.2 Per-condition means at N=20
129:----     3.008   0.090  0.020   [2.905, 3.013, 3.005, 3.087, 3.136, 3.022, 3.075, 2.879, 2.880,
132:-C--     3.464   0.097  0.022   [3.536, 3.444, 3.302, 3.613, 3.311, 3.503, 3.458, 3.540, 3.573,
135:--P-     2.790   0.086  0.019   [2.783, 2.873, 2.794, 2.749, 2.880, 2.791, 2.744, 2.845, 2.631,
138:-CP-     3.628   0.161  0.036   [3.932, 3.773, 3.557, 3.656, 3.325, 3.469, 3.617, 3.840, 3.617,
139:                                  3.714, 3.409, 3.733, 3.480, 3.628, 3.670, 3.840, 3.531, 3.724,
143:### 2.3 Main-effect estimates at N=20
157:C×P interaction = ((3.628 + 3.008) − (3.464 + 2.790)) / 2
165:C×P bootstrap mean:           +0.190
166:C×P 95% bootstrap CI:         [+0.143, +0.239]
167:P(interaction ≤ 0):           0.0000
168:P(interaction < +0.10):       0.0000
186:mean = +0.190,  std = 0.089,  SEM = 0.020
191:per-seed std at N=20 (0.089) is just under half the per-seed std at
192:N=10 (0.159) — the N=10 sample contained outliers (−0.165 and +0.417);
193:N=20 reveals a clean, narrow positive distribution.
203:3    30040–30042      +0.044          —                     ❌ original prereg
204:5    30040–30044      +0.039          —                     ❌ this session re-run
205:10   31000–31009      +0.088          [−0.002, +0.174]      borderline (CI contains)
206:20   32000–32019      +0.190          [+0.143, +0.239]      ✅ DECISIVELY ABOVE
214:   = 0.089 and a true synergy of +0.19, the SEM at N=3 is 0.089/√3 = 0.051.
221:   then 32000–32019. The means at each seed range differ enough that
226:The N=10 sample (31000–31009) had a per-seed std of 0.159 because it
227:landed on outliers; the N=20 sample (32000–32019) had std 0.089. **The
233:| Effect | N=3 / N=5 estimate | N=20 estimate | Shift |
281:the N=20 deep-dive — is that these are mostly orthogonal. Losing one
284:The N=20 result reverses this. **Strong inter-mechanism coupling is the
308:**New framing (2026-04-29, with N=20 result):**
311:> The original 3-seed estimate (+0.044) was a Type II false-negative
313:> interaction term. Replication at N=20 fresh seeds (32000–32019)
314:> gives synergy = +0.190, 95% bootstrap CI [+0.143, +0.239],
315:> P(synergy ≤ 0) = 0, P(synergy < +0.10) = 0. The architecture's
337:this session. With the N=20 deep-dive, the synergy is decisively above
359:BASE_SEED = 32000
368:**Verification:** seeds 32000–32019 should give the per-condition means
377:1. **One seed range tested at N=20.** A second N=20 run at a different
383:   well-powered N=20 estimate.
395:   (with one large positive outlier and two negatives) while N=20 has a
407:The original 3-seed validation reported +0.044 — a fail — and the paper
409:synergy = +0.190, 95% bootstrap CI [+0.143, +0.239], P(synergy ≤ 0) = 0,
410:P(synergy < +0.10) = 0. The architecture's prediction is exceeded by
427:- `demo_p4_cxp_deep_dive.py` — N=20 script (this work)

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md' | sed -n '1,90p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md' | sed -n '190,290p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md' | sed -n '300,380p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md' | sed -n '98,210p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 242ms:
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

 succeeded in 214ms:
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

 succeeded in 226ms:
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

 succeeded in 234ms:
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

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md' | sed -n '300,415p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md' | sed -n '1,110p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md' | sed -n '130,190p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md' | sed -n '252,295p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 202ms:
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

 succeeded in 194ms:
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

 succeeded in 261ms:
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

 succeeded in 259ms:
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

exec
/bin/bash -lc "rg -n \"40\\.6|93\\.8|53\\.1|n=25|83\\.1|65\\.4|87\\.5|70\\.6|79\\.78|11\\.58|6\\.80|1003|3\\.28|0\\.28|68\\.54|19\\.72|0\\.61|0\\.455|0\\.220|raw|substrate|reset\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md' | sed -n '1,120p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md' | sed -n '160,230p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md' | sed -n '300,430p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 250ms:
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

 succeeded in 269ms:
6:> **Headline.** The 600-cell substrate functions as a **selective
8:> when raw features are ambiguous (chess: +40.6 percentage points on
9:> leave-one-out, raw 53.1% → substrate-routed 93.8%) and is correctly
10:> null when raw features already saturate (conversation: 87.5% raw,
11:> substrate −4.4pp). On structural connectivity, ARIA is the **maximum-
13:> transitivity); HCP n=1003 degree std = 3.28 ± 0.28; ARIA is
14:> −11.58σ on degree homogeneity and +79.78σ on participation ratio,
24:Three tracks test ARIA's substrate against domains where it has no
30:   king safety, pawn structure, etc.). Test whether the substrate's
31:   geometry amplifies category structure beyond raw-feature
36:   Test whether the substrate is correctly **null** on a domain where
37:   raw features are already discriminative, validating that it is a
42:   the Human Connectome Project (n=1003 subjects, ICA-50
46:All three are deterministic given seeds and substrate state. All five
73:substrate's S⁷ observer frames; the substrate is run forward by
78:Critical detail: between successive depth measurements, the substrate
79:is reset to canonical state via `mon.homeostatic_reset(level=1.0)`.
86:**Threshold:** Chess substrate-routed 5-fold CV ≥ 70%.
91:Per-seed accuracies:  81.2%, 81.2%, 84.4%, 87.5%, 81.2%
92:Mean:                 83.1%
96:83.1% on the 32-position × 4-category task, well above the 70%
97:threshold. Per-seed variance is small (range 81.2%–87.5%).
100:the fresh-seed mean of 83.1% replicates discovery within expected
110:substrate, classify. Repeat 15 times with seeded random permutations
113:**Result:** 65.4% mean across 15 permutations.
117:substrate retains 65.4% classification power — well above the 25%
119:classification accuracy comes from the substrate's geometric structure
121:(83.1% − 65.4%) is the semantic alignment bonus.
123:This decomposes substrate classification into:
124:- **Geometric content (65%):** substrate amplifies category structure
137:**Method:** Shuffle category labels randomly, classify the substrate-
143:(23.4% ≈ 25% chance). This confirms the 83.1% raw and 65.4% null are
149:**Threshold:** Optimal substrate depth ∈ {15, 25, 40, 60} ticks.
151:**Method:** Run the substrate at six different `n_ticks` values
153:depth, with `homeostatic_reset(level=1.0)` between measurements.
159:   5     53.1%
161:  25     93.8%   ← peak
167:**Interpretation:** The substrate has a clear optimal depth around
168:n=25, with a roll-off both at shallower depth (insufficient
169:integration) and deeper depth (substrate equilibrates and loses
175:### 2.6 P13 — Substrate lift on LOO with reset protocol
177:**Threshold:** Substrate-routed LOO accuracy − raw-feature LOO
180:**Method:** Run LOO classification on (a) raw 8-dim V2 features and
181:(b) substrate-routed patterns at n=25, with reset between depth
187:Raw features (LOO, 1-NN cosine):       53.1%
188:Substrate-routed (n=25, with reset):   93.8%
189:Lift:                                  +40.6 percentage points
192:**Interpretation:** The substrate amplifies the chess-position
193:discrimination from chance-level on raw features (53.1% on 4 categories
194:is just above chance-25%) to near-perfect (93.8%) when routed through
195:the substrate's 600-cell graph. This is **+40.6pp of geometric
199:failure of the reset protocol (substrate state drifted toward
201:classification structure). With the reset protocol now wired in, the
202:lift is restored to +40.6pp. See `NON_EQUILIBRIUM_FINDING.md` for the
207:The substrate is a **strong geometric amplifier** on chess:
208:- 53.1% raw → 93.8% substrate-routed at canonical depth (n=25)
209:- 65.4% null mapping (architecture-invariant geometric floor)
210:- 83.1% 5-fold CV at fresh seeds
211:- Goldilocks optimum at n=25 ticks of substrate evolution
213:The +40.6pp lift is roughly an order of magnitude above the +15pp
214:preregistered floor. The 65.4% null mapping shows two-thirds of the
231:pressure into S⁷ frames, substrate run forward by `n_ticks`, vertex
236:**Threshold:** Conversation raw 5-fold CV ≥ 75%.
238:**Result (fresh seeds 30220–30224):** **87.5%** mean.
241:discriminative — 87.5% raw classification at 5-fold CV exceeds the
242:chess raw rate (53.1% LOO) by ~34pp. There is little headroom for
243:substrate amplification.
247:**Threshold:** \|conversation substrate lift\| < 10pp (the substrate
253:Raw 5-fold CV:               87.5%
254:Substrate 5-fold CV (n=25):  83.1%
259:ARIA's substrate amplifies chess (where raw features are ambiguous)
260:but is approximately null on conversation (where raw features are
266:classification booster: the substrate **selectively** lifts
267:classification only where raw features fail. This matches cortical
268:integration literature: substrate integration boosts performance on
277:**Result:** 70.6% mean across 15 permutations.
279:**Interpretation:** Conversation null mapping (70.6%) is slightly
280:higher than chess null mapping (65.4%), consistent with conversation
289:| Chess (LOO) | 53.1% | 93.8% | n/a | n/a | +40.6pp lift |
290:| Chess (5-fold CV) | n/a | 83.1% | 65.4% | 65.4% | +17.7pp |
291:| Conversation (5-fold CV) | 87.5% | 83.1% | 70.6% | 70.6% | +12.5pp (raw vs null) |
299:The substrate is **correctly null** on conversation, validating
300:selective amplification. Raw features at 87.5% leave little headroom;
301:substrate routing at 83.1% (lift −4.4pp) is within preregistered
302:neutrality bounds. The null permutation at 70.6% confirms geometric
311:**Reference cohort:** Human Connectome Project (HCP), n=1003 subjects.
313:in ICA-50 parcellation. The full-cohort effects (n=1003) match the
334:included to verify the substrate construction is correct.
347:**ARIA is at −11.58σ** below the HCP cohort mean on this metric:
348:ARIA's degree std is 0; HCP n=1003 mean is 3.28 ± 0.28; the gap is
349:(0 − 3.28) / 0.28 = −11.7σ. **Zero of 1003 HCP subjects** have
352:### 4.4 Higher-order graph statistics (full cohort, n=1003)
358:Metric                 ARIA     HCP n=1003 mean   σ from HCP
360:Degree std             0.000    3.28 ± 0.28        −11.58σ
361:Participation ratio    68.54    19.72 ± 0.61       +79.78σ
362:Clustering coefficient 0.455    0.220              +6.80σ
369:  hub-concentrated). ARIA at 68.54 vs HCP at 19.72 — ARIA is
371:  Real cortex is hub-concentrated; ARIA is uniform. +79.78σ.
373:  ARIA at 0.455 vs HCP at 0.220 — ARIA has more local clustering
375:  +6.80σ.
390:giving precise effect-size statements like "real cortex is +79.78σ
418:ARIA's degree std = 0 (theorem); HCP n=1003 degree std = 3.28 ± 0.28,
419:range [2.55, 4.16], with zero of 1003 subjects below 2.0. ARIA is
420:−11.58σ on degree homogeneity, +79.78σ on participation ratio, and
421:+6.80σ on clustering coefficient. The substrate functions as a
430:The substrate's geometric structure functions as a domain-invariant
433:hand-features is at chance-class (53.1% raw LOO), substrate routing
434:amplifies to 93.8% LOO (+40.6pp lift) and 83.1% 5-fold CV across fresh
438:geometric floor). On conversation utterance classification, where raw
439:8-dimensional features are already 87.5% discriminative, the substrate
441:band) — confirming the substrate is a selective amplifier, not an
442:unconditional booster. On HCP brain functional connectivity (n=1003,
444:std = 0) is −11.58σ below the biological mean (3.28 ± 0.28); on
445:participation ratio ARIA at 68.54 is +79.78σ above HCP (19.72 ± 0.61),
446:and on clustering coefficient ARIA at 0.455 is +6.80σ above HCP (0.220).
459:The contrast between chess (+40.6pp lift) and conversation (−4.4pp
460:lift) demonstrates the substrate amplifies **only when there is
464:integration adds noise). The substrate captures this selectivity
469:The 65.4% (chess) / 70.6% (conversation) null permutation accuracies
470:demonstrate the substrate carries ~65% classification power as
472:to which frame. This is the "raw geometric amplification" of the H₄
479:reference for biological cortex. The σ-distances (−11.58σ, +79.78σ,
480:+6.80σ) quantify the magnitude of biological symmetry-breaking, with
516:1. **Chess test is small (32 positions, 4 categories).** The ~93.8%
517:   substrate-routed accuracy is on a small evaluation set. A larger
519:   at 83.1% is a more conservative readout (4-category random
533:4. **No domain-specific tuning was applied to the substrate.** This
535:   the substrate's only domain-specific input is the feature → frame
558:- `kernel/dimensional_monitor.py:DimensionalMonitor` — substrate
559:  with pressure-field dynamics; `homeostatic_reset(level=1.0)` is
560:  the reset method.
571:  substrate; independent of cross-domain tracks)
572:- `docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md` — substrate
573:  state-drift diagnostic; rationale for `homeostatic_reset()`
576:- `project_substrate_selective_amplifier.md` — original selective-

 succeeded in 289ms:
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

 succeeded in 291ms:
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

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md' | sed -n '230,305p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 265ms:
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

exec
/bin/bash -lc "rg -n \"reset|homeostatic|40\\.6|3\\.1|drift|five|equilibrium|n=25|93\\.8|53\\.1|27\\.2|15\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md' | sed -n '1,120p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md' | sed -n '120,230p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 272ms:
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

 succeeded in 296ms:
13:The ARIA substrate is a **far-from-equilibrium thermodynamic engine**.
20:Only a **reset mechanism** analogous to biological sleep restores
21:non-equilibrium operation.
27:### E1 — Drift curve (30 consecutive classifications, no reset)
32:| 2 | 93.8% | 100 | 147.9 | 1.000 |
33:| 3 | 68.8% | 100 | 153.4 | 1.000 |
34:| 4 | 65.6% | 100 | 156.7 | 1.000 |
35:| **5** | **56.2%** | 100 | **156.96** | 1.000 |
36:| 6–30 | **56.2% locked** | 100 | 156.96 locked | 1.000 |
39:equilibrates at exactly 156.96 (emission = decay). Accuracy is
43:### E2 — Homeostatic reset
49:| **Full reset** | **87.5% (higher than fresh)** |
50:| Partial reset (50% decay) | 81.2% |
52:**Full reset restores AND improves on the fresh state**. Because
54:full reset clears those, leaving the substrate genuinely canonical.
69:**pressure field reaching thermodynamic equilibrium** — emission
82:system LITERALLY converges to a thermodynamic equilibrium of the
85:Once at equilibrium:
86:- Any fresh injection gets quickly absorbed into the equilibrium
99:| P13 preregistration fail | polytope drifted to equilibrium across evaluations |
101:| Variance expansion under ablation | mechanisms are **far-from-equilibrium maintainers** |
102:| 3-seed interaction instability | seeds sampled at different distances from equilibrium |
103:| DMT α-shift | 5HT2A agonism pushes system further from equilibrium |
104:| Fresh-polytope vs state-drifted +31pp vs +3pp | non-equilibrium vs equilibrium regimes |
108:## 5. Biological parallels — far-from-equilibrium theory
121:pre-loaded "ignited" state is SOC; steady operation without reset
124:### Non-equilibrium cortex (Chialvo, Deco, others)
126:non-equilibrium thermodynamic system. Our finding provides a
132:during wake. Our reset operation is a direct computational analogue.
134:synaptic downscaling — exactly what our `_homeostatic_reset` does
141:If sleep is the biological analogue of our reset operation:
149:  reset dynamics (higher or more variable, as the substrate is
173:"ARIA is a far-from-equilibrium computational substrate. Its
176:Biological cortex operates the same way: sleep and homeostatic
178:the cortex to a degenerate equilibrium. ARIA makes this mechanism
203:   to test the "SWS = substrate reset" prediction
204:3. ⏳ Reframe manuscript around non-equilibrium as organizing principle
205:4. ⏳ Add homeostatic reset API to DimensionalMonitor
206:5. ⏳ Re-run preregistered validation with proper reset — convert
218:- **Non-equilibrium brain** (Chialvo, Deco)
223:substrate theory ties them together. ARIA's non-equilibrium finding
228:- Mechanisms are the constraints that maintain far-from-equilibrium
229:- Sleep-like reset is the thermodynamic necessity
230:- SOC α is a steady-state signature of healthy non-equilibrium

 succeeded in 341ms:
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

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md' | sed -n '1,150p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md' | sed -n '150,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"P1|P2|P3|P4|P5|P6|P7|P8|P9|P10|P11|P12|P13|P14|P15|P16|P17|P18|threshold|falsified|>=|≥|<|>\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 290ms:
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

 succeeded in 289ms:
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

 succeeded in 297ms:
10:- a **pass threshold** (interval, inequality, or categorical match)
20:### P1. Cascade α is in the SOC range
28:### P2. Pairwise ablation — context rotation is the dominant mechanism
30:  `ablate_context_rotation` on α is **≥ +0.30**.
35:### P3. D×C interaction is near-zero (independence)
36:- **Claim**: |D×C interaction| < **0.20** on the fresh 2x2 sub-matrix
43:### P4. C×P synergy is positive and substantial
44:- **Claim**: C×P interaction **≥ +0.10** on the 2x2 (----/-C--/--P-/-CP-)
47:  redundant recovery mechanism" story depends on this being > 0.
50:### P5. Equator compensation is null (≤ small main effect)
52:  **|effect| < 0.15** on 3 fresh seeds.
61:### P6. Real EEG spindle α is in the SOC range
70:### P7. W→N3 coherence variance collapses
71:- **Claim**: Mean N3/W variance ratio across 24 subjects **< 0.70**.
72:- **Rationale**: Discovery gave 0.365. If the ratio is ≥ 0.70 it means
77:### P8. W→N3 regime switching drops (opposite to anaesthesia)
78:- **Claim**: Mean N3/W switching ratio **< 0.50**.
79:- **Rationale**: Discovery gave 0.058. If the ratio > 0.50 (near-unity
88:### P9. Chess 5-fold CV ≥ chance + substantial margin
90:  (30200-30204), mean ≥ **70%**.
92:  < 70% would mean our 84.4% LOO number was misleadingly inflated.
95:### P10. Null feature→frame mapping ≥ 50% (domain-invariant floor)
97:  seed 30210) **≥ 50%**.
102:### P11. Random-label baseline = chance
108:### P12. Diffusion-depth goldilocks peaks in [15, 60]
115:### P13. Substrate lift on chess v2 is positive
116:- **Claim**: At n=25, substrate ≥ raw **+ 15pp** on 5-fold CV (fresh
126:### P14. Conversation raw features already discriminative
127:- **Claim**: Raw conversation 5-fold CV accuracy **≥ 75%** on fresh
133:### P15. Substrate does NOT lift clean features much
134:- **Claim**: |substrate lift − raw| **< 10pp** on conversation (fresh
140:### P16. Architecture-invariant null mapping ≥ 50% on both domains
141:- **Claim**: Null feature→frame permutation mean ≥ **50%** on BOTH
150:### P17. ARIA degree std = 0 exactly (theorem-level)
157:### P18. HCP ICA-50 has non-trivial degree std
159:  same), group-averaged HCP graph has **degree std > 2.0** at
160:  density-matched threshold.
184:## Success thresholds
186:- **≥ 14/18 predictions pass**: paper claims are well-supported.
189:- **< 10/18**: substantial revision needed; multiple correspondences

exec
/bin/bash -lc "rg -n \"600-cell|Laplacian|spectrum|120|720|12|\\{0|2\\.292|5\\.528|14\\.472|15\\.708|18/18|15/18|6/6|0\\.190|40\\.6|27\\.2|2\\.96|1\\.83|11\\.58|79\\.78|6\\.80|1003|n=100\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"six|signature|WAKE|SLEEP_N3|PROPOFOL|RECOVERY|2\\.252|3\\.250|2\\.758|0\\.463|0\\.066|0\\.33\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md' | sed -n '1,130p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md' | sed -n '650,830p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 218ms:
16:on the 600-cell regular 4-polytope under its H₄ Coxeter symmetry. The
17:substrate is fully derivable from group theory: 120 vertices of uniform
18:degree 12, eigenvalues {12, 6φ, 4φ, 3} where φ is the golden ratio,
31:regime-switching elevates 1.83× wake; propofol continuity drops by
36:exhibit a strong synergistic interaction of +0.190 (95% bootstrap CI
42:recognition by +40.6 percentage points (raw 53.1% → substrate-routed
46:HCP brain functional connectivity (n=1003 subjects), ARIA serves as a
48:(theorem); HCP degree std = 3.28 ± 0.28; ARIA is at −11.58σ on degree
49:homogeneity and +79.78σ on participation ratio. With the N=20
50:deep-dive, the empirical tally is 18/18 preregistered predictions
51:plus 6/6 drug/sleep signatures; no claim is walked back. This is the
56:**Keywords**: 600-cell polytope, H₄ Coxeter symmetry, cortical
78:phenomena it reproduces. The substrate is the 600-cell regular
91:The 600-cell admits a 7-rung cascade decomposition that emerges from
99:H₃ (icosahedral 3-D Coxeter group, 120 elements; A₅ symmetry)
111:600-cell substrate has 120 vertices, each of uniform degree 12. The
112:graph Laplacian has eigenvalues {0, 3, 4φ, 6φ, 12} with multiplicities
158:The 600-cell vertices are the H₄ Coxeter group acting on the
166:Total: 120 vertices in 4-D Euclidean space, all on the unit 3-sphere.
167:This is the standard 600-cell construction (Schläfli {3, 3, 5}); see
174:exactly 12 neighbours (degree 12), uniform across all vertices —
178:The graph Laplacian L has eigenvalues:
186:| 12 − 4φ ≈ 5.528 | 9 | K_23 (σ-twin) |
187:| 12 − 6φ ≈ 2.292 | 16 | K_17 (σ-twin) |
188:| 12 − 3 = 9 | 4 | K_7 (σ-twin) |
189:| 12 | 1 | K_1 |
212:given by the shifted Laplacian Green function:
220:input across its 120 vertices through the graph's modal structure.
279:split degree distribution (12 vertices of effective cross-hemisphere
310:  point estimate:           +0.190
327:| **20** | **+0.190, CI [+0.143, +0.239]** | **decisively above** |
378:ψ_thresh = bounded_topk(ψ, k=12)             # critical nonlinearity
387:- `bounded_topk(ψ, k=12)` = critical nonlinearity (§4.2)
397:`bounded_topk(ψ, k=12)` (zeros all but the top-12 vertices, scales
401:The k = 12 value was chosen because k = 12 is the average degree of
402:the 600-cell graph (each vertex has 12 neighbours); this is a
415:amp_history  = state_history @ eigvecs               # mode amps (T, 120)
464:The 600-cell graph is built once from H₄ root coordinates. The graph
465:Laplacian's spectral decomposition is cached at module level
524:coherent shell, plus spindle bursts (12 ticks every 100 at amplitude
531:    if (t % 100) < 12:
583:−0.183, inside |·|<0.20 band). P4 closes only at N = 20 (C×P = +0.190,
601:+3.1pp lift (without reset, on a state-drifted substrate) to +40.6pp
624:**Method.** Run the 600-cell substrate with all four mechanisms (D, C,
654:**Method.** Four conditions × 800 ticks at seed = 42, k_threshold = 12.
673:| 2 | Propofol regime-switching ratio | OpenNeuro ds005620 (n=8, 2.96×) | ∈ [1.5, 5.0] | **1.83×** | ✓ |
674:| 3 | Propofol continuity drop | EEG microstate (Brodbeck 2012) | > 0.020 | **+0.066** | ✓ |
689:2.96× empirically); the NREM-N3 variance collapse magnitude is
722:| **C × P (P4)** | **20** | **+0.190** | **[+0.143, +0.239]** | **✅ strongly synergistic** |
731:| **20** | **32000–32019** | **+0.190** | **[+0.143, +0.239]** |
766:  order statistics to HCP n=1003 ICA-50 group-averaged connectivity
775:P12 — goldilocks peak depth:                   n=25   ∈ {15,25,40,60}  ✅
776:P13 — LOO substrate lift (raw 53.1% → 93.8%):  +40.6pp ≥ +15pp  ✅
784:  n=100:  78.1%
795:**HCP result (n=1003 subjects, ICA-50):**
797:| Metric | ARIA | HCP n=1003 mean | σ from HCP |
799:| Degree std | 0.000 (theorem) | 3.28 ± 0.28 | **−11.58σ** |
800:| Participation ratio | 68.54 | 19.72 ± 0.61 | **+79.78σ** |
801:| Clustering coefficient | 0.455 | 0.220 | +6.80σ |
808:Zero of 1003 HCP subjects have degree std below 2.0; ARIA is far
813:(i) **Selective amplification.** The contrast between chess (+40.6pp
824:~17pp (chess) / ~12pp (conversation) is the semantic alignment bonus.
830:symmetry-breaking. The σ-distances (−11.58σ on degree, +79.78σ on
835:### 6.5 The eighteen preregistered predictions: 17/18 standard, 18/18 with N=20 P4
848:| **P4** | **C×P synergy** | **≥ +0.10** | **+0.190 [+0.143, +0.239] (N=20)** | **✅** |
856:| P12 | Chess goldilocks peak | ∈ {15, 25, 40, 60} | n=25 | ✅ |
857:| P13 | Chess LOO lift (with reset) | ≥ +15pp | +40.6pp | ✅ |
864:**Tally: 17/18 at standard validation; 18/18 with N=20 deep-dive on P4.**
866:**Comparison to the original 2026-04-20 run (15/18):**
872:- **P4** (C×P synergy): +0.044 at N=3 → +0.190 at N=20. Same
874:- **P13** (chess LOO lift): +3.1pp without reset → +40.6pp with reset.
894:without learned parameters.** The 600-cell + H₄ symmetry comes from
908:**(3) The 18/18 preregistered claim with no threshold modification.**
940:context rotation or partial emission. The 600-cell substrate is
994:of structure (degree std = 0 by transitivity, eigenvalue spectrum
995:{12, 6φ, 4φ, 3} by character theory). The σ-distances (−11.58σ on
996:degree homogeneity, +79.78σ on participation ratio) far exceed any
1012:1. **Single substrate (the 600-cell).** We have not tested whether
1013:   other regular polytopes (e.g., the 24-cell, the 120-cell) would
1014:   produce comparable correspondences. The 600-cell was chosen
1044:4. **Sig 2 ratio (1.83×) is below empirical point estimate (2.96×)**
1072:   reproducibility of the +0.190 estimate.
1086:1. **The 600-cell choice is post-hoc justified by biology.** While
1125:- k_threshold = 12 (cortical band; bounded_topk nonlinearity)
1140:- HCP: deterministic (n=100 ICA-50 group average)
1208:The 600-cell polytope under H₄ Coxeter symmetry, decomposed into a
1215:on the 600-cell.
1219:(+0.190, 95% CI [+0.143, +0.239] at N=20) is comparable in magnitude
1234:classification tasks (chess +40.6pp lift; conversation correctly null
1236:cortical functional connectivity (HCP n=1003: ARIA at −11.58σ on
1237:degree homogeneity, +79.78σ on participation ratio).

 succeeded in 209ms:
6:of the work. This version incorporates the v4 consciousness chain (six
7:drug/sleep EEG signatures), the N=20 deep-dive on the C×P synergy
25:reproduces six independent drug/sleep EEG signatures of conscious
27:α = 2.252, 95% CI [1.82, 2.86] (R² = 0.956), with three-way confidence
32:0.066; propofol integrated information Φ collapses to 0.33× wake (IIT
51:plus 6/6 drug/sleep signatures; no claim is walked back. This is the
71:yielded quantitative signatures that survive preregistration on real
84:sufficient to reproduce a meaningful subset of cortical signatures —
134:Tests cover cascade statistics (P1–P5), real EEG signatures (P6–P8),
138:**Set B: Six drug/sleep EEG signatures** (`demo_drug_sleep_v4.py`)
149:estimates). All six Set B drug/sleep signatures pass on a single
367:statistics matching real EEG (§6.1). To test high-level signatures —
385:  0.20 for WAKE/RECOVERY, 0.05 for SLEEP_N3, 0.00 for PROPOFOL)
444:This is the source for the propofol continuity-collapse signature:
445:WAKE composite = 0.943; PROPOFOL composite = 0.877; drop = +0.066.
496:**WAKE.** AR(1) cortical noise (β = 0.90), tonic equator-shell
523:**SLEEP_N3.** Slow oscillation (~1 Hz analogue, amplitude 1.0) on a
538:**PROPOFOL.** Low-amplitude tonic noise (amplitude 0.05), η = 0.00
546:**RECOVERY.** Identical to WAKE — verifies determinism and
551:biological time scales but are not tuned to specific signatures.
635:| v4 WAKE consciousness chain | 2.252 | [1.82, 2.86] | 0.956 | 58 |
639:range. The v4 consciousness-chain WAKE α is **inside both** the
648:### 6.2 Six drug/sleep EEG signatures reproduced (consciousness chain v4)
651:bounded top-K thresholding and IIT-style Φ, reproduces six independent
652:drug/sleep EEG signatures of conscious vs unconscious states.
662:WAKE       58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
663:SLEEP_N3  111   3.250   [2.44, 4.14]   0.886  1.01e-05    0.0055   0.980
664:PROPOFOL  246   2.758   [2.52, 3.09]   0.931  5.37e-06    0.0003   0.877
665:RECOVERY   58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
668:**Six signatures:**
672:| 1 | NREM-N3 variance ratio (vs Wake) | Sleep-EDFx W→N3 (n=24) | ≈ 0.365 | **0.463** | ✓ |
674:| 3 | Propofol continuity drop | EEG microstate (Brodbeck 2012) | > 0.020 | **+0.066** | ✓ |
675:| 4 | Propofol Φ collapse (IIT) | Tononi 2008 | ratio < 0.50 | **0.33×** | ✓ |
677:| 6 | Wake cortical-avalanche α | n=30 Sleep-EDFx CI [2.50, 2.86] | α ∈ [1.5, 3.5], R²>0.85 | **2.252 [1.82, 2.86] R²=0.956** | ✓ |
679:All six signatures pass at preregistered thresholds. The wake cascade-α
684:stimulus model varying across conditions, reproduces six independent
685:drug/sleep signatures observed in real cortex. The IIT-direction-correct
686:Φ collapse on propofol (0.33× wake) is consistent with the Tononi
893:**(1) A geometric substrate that produces real-cortex EEG signatures
896:tolerance; six drug/sleep signatures pass at preregistered thresholds.
898:EEG signatures from a single deterministic substrate.
918:propofol (0.33× wake). The substrate's symmetry-breaking is what
1028:   per-signature claims. The wake cascade-α 95% CI [1.82, 2.86] is
1091:   reproduces signatures, not as a derivation from first principles.
1111:| Six drug/sleep signatures (§6.2) | `python3 demo_drug_sleep_v4.py` | ~30 s | stdout summary |
1148:# Run six-signature consciousness chain
1182:| `demo_drug_sleep_v4.py` | Six-signature consciousness chain (§6.2) |
1194:| `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` | Six-signature detail (this work) |
1211:preregistered neuroscience correspondences plus six independent
1212:drug/sleep EEG signatures of conscious vs unconscious states. The
1228:reproduces six drug/sleep EEG signatures on a single deterministic
1229:substrate. Wake cortical-avalanche power law has α = 2.252,

 succeeded in 194ms:
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

 succeeded in 202ms:
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

codex
The headline numerics match the local result docs for the five requested checks. The main issues I’m seeing are not the primary tables, but stale spectrum prose in later discussion/conclusion and a few claims whose wording is stronger than the paper’s own caveats support.
exec
/bin/bash -lc "pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper
 exited 127 in 476ms:
/bin/bash: pdflatex: command not found

exec
/bin/bash -lc "rg -oh \"\\\\citep\\{["'^}]+'"\\}\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections' | sed -E 's/.*\\{(["'^}]*)'"\\}/\\1/' | tr ',' '\\n' | sed 's/"'^ *//;s/ *$//'"' | sort -u" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -oh "''^@[a-zA-Z]+'"\\{["'^,]+" '"'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib' | sed -E 's/"'^@[a-zA-Z]+'"\\{//' | sort -u" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\ref\\{["'^}]+'"\\}|\\\\label\\{["'^}]+'"\\}\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\checkmark|texorpdfstring|Erd\\\\H|\\\\Phi|\\\\mathrm|\\\\mathsf|\\\\texttt|\\\\emph|\\\\S\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 227ms:

  --auto-hybrid-regex             (DEPRECATED) Use PCRE2 if appropriate.
  --binary                        Search binary files.
  --block-buffered                Force block buffering.
  --color=WHEN                    When to use color.
  --colors=COLOR_SPEC             Configure color settings and styles.
  --column                        Show column numbers.
  --context-separator=SEP         Set the separator for contextual chunks.
  --count-matches                 Show count of every match for each file.
  --crlf                          Use CRLF line terminators (nice for Windows).
  --debug                         Show debug messages.
  --dfa-size-limit=NUM            The upper size limit of the regex DFA.
  --engine=ENGINE                 Specify which regex engine to use.
  --field-context-separator=SEP   Set the field context separator.
  --field-match-separator=SEP     Set the field match separator.
  --files                         Print each file that would be searched.
  --files-without-match           Print the paths that contain zero matches.
  --generate=KIND                 Generate man pages and completion scripts.
  --glob-case-insensitive         Process all glob patterns case insensitively.
  --heading                       Print matches grouped by each file.
  --hostname-bin=COMMAND          Run a program to get this system's hostname.
  --hyperlink-format=FORMAT       Set the format of hyperlinks.
  --iglob=GLOB                    Include/exclude paths case insensitively.
  --ignore-file-case-insensitive  Process ignore files case insensitively.
  --ignore-file=PATH              Specify additional ignore files.
  --include-zero                  Include zero matches in summary output.
  --json                          Show search results in a JSON Lines format.
  --line-buffered                 Force line buffering.
  --max-columns-preview           Show preview for lines exceeding the limit.
  --max-filesize=NUM              Ignore files larger than NUM in size.
  --mmap                          Search with memory maps when possible.
  --multiline-dotall              Make '.' match line terminators.
  --no-config                     Never read configuration files.
  --no-ignore                     Don't use ignore files.
  --no-ignore-dot                 Don't use .ignore or .rgignore files.
  --no-ignore-exclude             Don't use local exclusion files.
  --no-ignore-files               Don't use --ignore-file arguments.
  --no-ignore-global              Don't use global ignore files.
  --no-ignore-messages            Suppress gitignore parse error messages.
  --no-ignore-parent              Don't use ignore files in parent directories.
  --no-ignore-vcs                 Don't use ignore files from source control.
  --no-messages                   Suppress some error messages.
  --no-pcre2-unicode              (DEPRECATED) Disable Unicode mode for PCRE2.
  --no-require-git                Use .gitignore outside of git repositories.
  --no-unicode                    Disable Unicode mode.
  --null-data                     Use NUL as a line terminator.
  --one-file-system               Skip directories on other file systems.
  --passthru                      Print both matching and non-matching lines.
  --path-separator=SEP            Set the path separator for printing paths.
  --pcre2-version                 Print the version of PCRE2 that ripgrep uses.
  --pre-glob=GLOB                 Include or exclude files from a preprocessor.
  --pre=COMMAND                   Search output of COMMAND for each PATH.
  --regex-size-limit=NUM          The size limit of the compiled regex.
  --sort-files                    (DEPRECATED) Sort results by file path.
  --sort=SORTBY                   Sort results in ascending order.
  --sortr=SORTBY                  Sort results in descending order.
  --stats                         Print statistics about the search.
  --stop-on-nonmatch              Stop searching after a non-match.
  --trace                         Show trace messages.
  --trim                          Trim prefix whitespace from matches.
  --type-add=TYPESPEC             Add a new glob for a file type.
  --type-clear=TYPE               Clear globs for a file type.
  --type-list                     Show all supported file types.
  --vimgrep                       Print results in a vim compatible format.
  -., --hidden                    Search hidden files and directories.
  -0, --null                      Print a NUL byte after file paths.
  -A, --after-context=NUM         Show NUM lines after each match.
  -B, --before-context=NUM        Show NUM lines before each match.
  -C, --context=NUM               Show NUM lines before and after each match.
  -E, --encoding=ENCODING         Specify the text encoding of files to search.
  -F, --fixed-strings             Treat all patterns as literals.
  -H, --with-filename             Print the file path with each matching line.
  -I, --no-filename               Never print the path with each matching line.
  -L, --follow                    Follow symbolic links.
  -M, --max-columns=NUM           Omit lines longer than this limit.
  -N, --no-line-number            Suppress line numbers.
  -P, --pcre2                     Enable PCRE2 matching.
  -S, --smart-case                Smart case search.
  -T, --type-not=TYPE             Do not search files matching TYPE.
  -U, --multiline                 Enable searching across multiple lines.
  -V, --version                   Print ripgrep's version.
  -a, --text                      Search binary files as if they were text.
  -b, --byte-offset               Print the byte offset for each matching line.
  -c, --count                     Show count of matching lines for each file.
  -d, --max-depth=NUM             Descend at most NUM directories.
  -e, --regexp=PATTERN            A pattern to search for.
  -f, --file=PATTERNFILE          Search for patterns from the given file.
  -g, --glob=GLOB                 Include or exclude file paths.
  -h, --help                      Show help output.
  -i, --ignore-case               Case insensitive search.
  -j, --threads=NUM               Set the approximate number of threads to use.
  -l, --files-with-matches        Print the paths with at least one match.
  -m, --max-count=NUM             Limit the number of matching lines.
  -n, --line-number               Show line numbers.
  -o, --only-matching             Print only matched parts of a line.
  -p, --pretty                    Alias for colors, headings and line numbers.
  -q, --quiet                     Do not print anything to stdout.
  -r, --replace=TEXT              Replace matches with the given text.
  -s, --case-sensitive            Search case sensitively (default).
  -t, --type=TYPE                 Only search files matching TYPE.
  -u, --unrestricted              Reduce the level of "smart" filtering.
  -v, --invert-match              Invert matching.
  -w, --word-regexp               Show matches surrounded by word boundaries.
  -x, --line-regexp               Show matches surrounded by line boundaries.
  -z, --search-zip                Search in compressed files.
  <PATH>...   A file or directory to search.
  <PATTERN>   A regular expression used for searching.
  rg [OPTIONS] PATTERN [PATH ...]
Andrew Gallant <jamslam@gmail.com>
FILTER OPTIONS:
INPUT OPTIONS:
LOGGING OPTIONS:
OTHER BEHAVIORS:
OUTPUT MODES:
OUTPUT OPTIONS:
POSITIONAL ARGUMENTS:
Project home page: https://github.com/BurntSushi/ripgrep
SEARCH OPTIONS:
USAGE:
Use -h for short descriptions and --help for more details.
a regex pattern. By default, ripgrep will respect gitignore rules and
automatically skip hidden files/directories and binary files.
ripgrep (rg) recursively searches the current directory for lines matching
ripgrep 15.1.0 (rev af60c2de9d)

 succeeded in 236ms:

--after-context=NUM         Show NUM lines after each match.
--auto-hybrid-regex             (DEPRECATED) Use PCRE2 if appropriate.
--before-context=NUM        Show NUM lines before each match.
--binary                        Search binary files.
--block-buffered                Force block buffering.
--byte-offset               Print the byte offset for each matching line.
--case-sensitive            Search case sensitively (default).
--color=WHEN                    When to use color.
--colors=COLOR_SPEC             Configure color settings and styles.
--column                        Show column numbers.
--context-separator=SEP         Set the separator for contextual chunks.
--context=NUM               Show NUM lines before and after each match.
--count                     Show count of matching lines for each file.
--count-matches                 Show count of every match for each file.
--crlf                          Use CRLF line terminators (nice for Windows).
--debug                         Show debug messages.
--dfa-size-limit=NUM            The upper size limit of the regex DFA.
--encoding=ENCODING         Specify the text encoding of files to search.
--engine=ENGINE                 Specify which regex engine to use.
--field-context-separator=SEP   Set the field context separator.
--field-match-separator=SEP     Set the field match separator.
--file=PATTERNFILE          Search for patterns from the given file.
--files                         Print each file that would be searched.
--files-with-matches        Print the paths with at least one match.
--files-without-match           Print the paths that contain zero matches.
--fixed-strings             Treat all patterns as literals.
--follow                    Follow symbolic links.
--generate=KIND                 Generate man pages and completion scripts.
--glob-case-insensitive         Process all glob patterns case insensitively.
--glob=GLOB                 Include or exclude file paths.
--heading                       Print matches grouped by each file.
--help                      Show help output.
--hidden                    Search hidden files and directories.
--hostname-bin=COMMAND          Run a program to get this system's hostname.
--hyperlink-format=FORMAT       Set the format of hyperlinks.
--iglob=GLOB                    Include/exclude paths case insensitively.
--ignore-case               Case insensitive search.
--ignore-file-case-insensitive  Process ignore files case insensitively.
--ignore-file=PATH              Specify additional ignore files.
--include-zero                  Include zero matches in summary output.
--invert-match              Invert matching.
--json                          Show search results in a JSON Lines format.
--line-buffered                 Force line buffering.
--line-number               Show line numbers.
--line-regexp               Show matches surrounded by line boundaries.
--max-columns-preview           Show preview for lines exceeding the limit.
--max-columns=NUM           Omit lines longer than this limit.
--max-count=NUM             Limit the number of matching lines.
--max-depth=NUM             Descend at most NUM directories.
--max-filesize=NUM              Ignore files larger than NUM in size.
--mmap                          Search with memory maps when possible.
--multiline                 Enable searching across multiple lines.
--multiline-dotall              Make '.' match line terminators.
--no-config                     Never read configuration files.
--no-filename               Never print the path with each matching line.
--no-ignore                     Don't use ignore files.
--no-ignore-dot                 Don't use .ignore or .rgignore files.
--no-ignore-exclude             Don't use local exclusion files.
--no-ignore-files               Don't use --ignore-file arguments.
--no-ignore-global              Don't use global ignore files.
--no-ignore-messages            Suppress gitignore parse error messages.
--no-ignore-parent              Don't use ignore files in parent directories.
--no-ignore-vcs                 Don't use ignore files from source control.
--no-line-number            Suppress line numbers.
--no-messages                   Suppress some error messages.
--no-pcre2-unicode              (DEPRECATED) Disable Unicode mode for PCRE2.
--no-require-git                Use .gitignore outside of git repositories.
--no-unicode                    Disable Unicode mode.
--null                      Print a NUL byte after file paths.
--null-data                     Use NUL as a line terminator.
--one-file-system               Skip directories on other file systems.
--only-matching             Print only matched parts of a line.
--passthru                      Print both matching and non-matching lines.
--path-separator=SEP            Set the path separator for printing paths.
--pcre2                     Enable PCRE2 matching.
--pcre2-version                 Print the version of PCRE2 that ripgrep uses.
--pre-glob=GLOB                 Include or exclude files from a preprocessor.
--pre=COMMAND                   Search output of COMMAND for each PATH.
--pretty                    Alias for colors
--quiet                     Do not print anything to stdout.
--regex-size-limit=NUM          The size limit of the compiled regex.
--regexp=PATTERN            A pattern to search for.
--replace=TEXT              Replace matches with the given text.
--search-zip                Search in compressed files.
--smart-case                Smart case search.
--sort-files                    (DEPRECATED) Sort results by file path.
--sort=SORTBY                   Sort results in ascending order.
--sortr=SORTBY                  Sort results in descending order.
--stats                         Print statistics about the search.
--stop-on-nonmatch              Stop searching after a non-match.
--text                      Search binary files as if they were text.
--threads=NUM               Set the approximate number of threads to use.
--trace                         Show trace messages.
--trim                          Trim prefix whitespace from matches.
--type-add=TYPESPEC             Add a new glob for a file type.
--type-clear=TYPE               Clear globs for a file type.
--type-list                     Show all supported file types.
--type-not=TYPE             Do not search files matching TYPE.
--type=TYPE                 Only search files matching TYPE.
--unrestricted              Reduce the level of "smart" filtering.
--version                   Print ripgrep's version.
--vimgrep                       Print results in a vim compatible format.
--with-filename             Print the file path with each matching line.
--word-regexp               Show matches surrounded by word boundaries.
-.
-0
-A
-B
-C
-E
-F
-H
-I
-L
-M
-N
-P
-S
-T
-U
-V
-a
-b
-c
-d
-e
-f
-g
-h
-i
-j
-l
-m
-n
-o
-p
-q
-r
-s
-t
-u
-v
-w
-x
-z
<PATH>...   A file or directory to search.
<PATTERN>   A regular expression used for searching.
Andrew Gallant <jamslam@gmail.com>
FILTER OPTIONS:
INPUT OPTIONS:
LOGGING OPTIONS:
OTHER BEHAVIORS:
OUTPUT MODES:
OUTPUT OPTIONS:
POSITIONAL ARGUMENTS:
Project home page: https://github.com/BurntSushi/ripgrep
SEARCH OPTIONS:
USAGE:
Use -h for short descriptions and --help for more details.
a regex pattern. By default
automatically skip hidden files/directories and binary files.
headings and line numbers.
rg [OPTIONS] PATTERN [PATH ...]
ripgrep (rg) recursively searches the current directory for lines matching
ripgrep 15.1.0 (rev af60c2de9d)
ripgrep will respect gitignore rules and

 exited 2 in 228ms:
rg: regex parse error:
    (?:\checkmark|texorpdfstring|Erd\H|\Phi|\mathrm|\mathsf|\texttt|\emph|\S)
       ^^
error: unrecognized escape sequence

 exited 2 in 247ms:
rg: regex parse error:
    (?:\ref\{[^}]+\}|\label\{[^}]+\})
                     ^^
error: unrecognized escape sequence

exec
/bin/bash -lc "rg -o -- '\\\\citep\\{["'^}]+'"\\}' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections' | sed -E 's/.*\\{(["'^}]*)'"\\}/\\1/' | tr ',' '\\n' | sed 's/"'^ *//;s/ *$//'"' | sort -u" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -o -- '"'^@[a-zA-Z]+'"\\{["'^,]+'"' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib' | sed -E 's/"'^@[a-zA-Z]+'"\\{//' | sort -u" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -- '\\\\ref\\{["'^}]+'"\\}|\\\\label\\{["'^}]+'"\\}' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -- '\\\\checkmark|texorpdfstring|Erd\\\\H|\\\\Phi|\\\\mathrm|\\\\mathsf|\\\\texttt|\\\\emph|\\\\S' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 244ms:
Baars1988GWT
BalduzziTononi2008
BeggsPlenz2003
Brodbeck2012Microstates
ClarkPP2013
CoxeterRegularPolytopes
Dehaene2014ConsciousAndBrain
FristonFreeEnergy2010
OpenNeuroDS004902
OpenNeuroDS005620
PhysioNet2000
SleepEDFx
SmartAdaptiveClosureTransport2026
SmartAriaClosureKernel2026
SmartBAnomaly2026
Tononi2008
VanEssen2013HCP
Weisstein600Cell
ZenodoDMT3992359
ariaChessRepo

 succeeded in 264ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:45:reported as observed (\S\ref{sec:substrate}). Treated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:58:models (\S\ref{sec:chain}) are biologically-motivated design choices,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:91:biologically realistic (\S\ref{sec:chain}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:48:  as observed (\S\ref{sec:substrate}). The response operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:99:  builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:134:and applied throughout~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:153:\S\ref{sec:method} gives the provenance ledger (preregistration date,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:154:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:157:\S\ref{sec:chain} adds the recurrent self-model layer above the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:159:\S\ref{sec:results} reports the empirical tables: six drug/sleep
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:161:$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:163:$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:164:selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:167:\S\ref{sec:limitations} enumerates limitations and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:168:hostile-review guard matrix. \S\ref{sec:conclusion} concludes.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:2:\section{Methods and provenance}\label{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:25:listed as future strengthening builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:55:\label{tab:provenance}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:176:generalisable lesson is recorded in \S\ref{sec:limitations}: any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:2:\section{The recurrent layer}\label{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:5:The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:6:cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:17:signatures in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:57:$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:89:collapse in~\S\ref{sec:results} is consistent with the IIT direction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:165:the C$\times$P stress test in~\S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:197:within the factorial ablation model are reported in~\S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:2:\section{Discussion}\label{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:48:wake). The $\Phi$ proxy (\S\ref{sec:chain}) is designed to be small
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:57:The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:80:\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:167:The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:189:  see \S\ref{sec:limitations}.)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:3:         replication}\label{sec:stress}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:21:(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:37:\label{tab:cxp_trend}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:73:\label{tab:cxp_means}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:139:\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:2:\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:12:\subsection{Regime}\label{ssec:regime}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:20:(\S\ref{sec:intro}). \emph{Evidence:} empirical correspondences hold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:27:six-signature results in~\S\ref{ssec:six_signatures} are reported on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:32:in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:48:design choices iterated to v4. \emph{Disclosure:}~\S\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:56:\subsection{Post-hoc}\label{ssec:posthoc}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:63:\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:68:ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:76:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:83:strictly positive definite (\S\ref{ssec:cphi}); it is not derived
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:85:\S\ref{ssec:cphi} marks this as a design-level choice; the companion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:93:\subsection{Interpretation}\label{ssec:interpretation}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:99:\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:101:\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:106:IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:115:\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:119:\subsection{Test/claim}\label{ssec:testclaim}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:125:\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:150:\subsection{State-drift / out-of-scope}\label{ssec:scope}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:172:  4-polytopes — see~\S\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:72:\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:84:explicitly listed in~\S\ref{sec:limitations} and remain open.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:2:\section{The 600-cell response substrate}\label{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:5:This section constructs the substrate. \S\ref{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:6:gives the vertex set. \S\ref{ssec:graph} gives the graph and its
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:7:H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:9:\S\ref{ssec:shells} gives the 9-shell decomposition used for source
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:10:projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:11:descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:14:\subsection{Vertex construction}\label{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:31:\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:81:\S\ref{sec:chain} (the $K_{7}$-class projector is the default
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:84:\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:88:\begin{equation}\label{eq:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:107:in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:110:$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:119:varies between conditions in~\S\ref{sec:chain}; it is reported
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:122:\subsection{Shell decomposition}\label{ssec:shells}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:138:\subsection{Cascade descent (sketch)}\label{ssec:cascade}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:140:The recurrent layer in~\S\ref{sec:chain} references a cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:157:by the empirical correspondences in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:172:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:2:\section{Results}\label{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:7:(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:20:(\S\ref{sec:chain}). Per-condition trajectory observables are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:29:\label{tab:per_condition}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:46:\label{tab:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:80:(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:84:\S\ref{sec:limitations}~\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:86:\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:98:\label{tab:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:130:\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:141:  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:150:  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:162:\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:172:\label{tab:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:198:(\S\ref{ssec:graph}); the $\Ph^{-2}$ shift in $\Cph$ is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:199:stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:201:any specific subject (\S\ref{sec:chain}). Three-way overlap on the
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:156:$\Lop$. By H$_4$ transitivity (\S\ref{ssec:graph}) every vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:165:\label{tab:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:233:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:243:\label{tab:cross_domain_summary}

 succeeded in 283ms:
Baars1988GWT
BalduzziTononi2008
BeggsPlenz2003
Brodbeck2012Microstates
ClarkPP2013
CoxeterRegularPolytopes
Dehaene2014ConsciousAndBrain
FristonFreeEnergy2010
OpenNeuroDS004902
OpenNeuroDS005620
PhysioNet2000
SleepEDFx
SmartAdaptiveClosureTransport2026
SmartAriaClosureKernel2026
SmartBAnomaly2026
Tononi2008
VanEssen2013HCP
Weisstein600Cell
ZenodoDMT3992359
ariaChessRepo

 succeeded in 328ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:26:  \texttt{contact@vibrationalfielddynamics.org}\\[2pt]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:27:  \texttt{@vfd\_org}%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:38:\noindent\emph{Headline.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:45:reported as observed (\S\ref{sec:substrate}). Treated
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:55:substrate-pinned nonlinearity $\mathrm{bounded\_topk}(\cdot, k\!=\!12)$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:58:models (\S\ref{sec:chain}) are biologically-motivated design choices,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:61:\noindent\emph{Scope.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:62:This paper presents an empirical \emph{substrate witness}: it shows
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:69:4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which this substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:79:preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:91:biologically realistic (\S\ref{sec:chain}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:93:\noindent\emph{(i) Cortical avalanches.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:95:$95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$, $n_{\mathrm{events}}=58$).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:101:\noindent\emph{(ii) Drug/sleep state transitions.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:105:reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:107:integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:112:\noindent\emph{(iii) Causal mechanism isolation.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:126:\noindent\emph{(iv) Cross-domain selectivity.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:147:\noindent\emph{What we do not claim.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:155:The structural scope of this paper is: \emph{a geometry-fixed
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:178:OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:179:the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:184:$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:196:\texttt{reproduce\_paper\_claims.sh} script. All scripts are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:7:(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:13:\texttt{docs/brain\_mapping/CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:14:and \texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:19:$k_{\mathrm{thr}}=12$, single deterministic substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:20:(\S\ref{sec:chain}). Per-condition trajectory observables are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:21:$(n_{\mathrm{evt}}, \alpha, \mathrm{CI}_{95}, R^{2}, I_{\mathrm{var}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:22:\Phi_{\mathrm{traj}}, \mathrm{cont})$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:27:\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:32:condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:53:   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:55:   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:56:   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:59:   $> 0.020$ & $+0.066$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:60:4 & Propofol $\Phi$ collapse (IIT) &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:62:   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:65:   identical to wake & $0$ diff & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:70:   $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:80:(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:82:in \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} are not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:84:\S\ref{sec:limitations}~\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:89:(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:91:on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:92:$32000$--$32019$). \emph{No preregistered threshold has been modified.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:103:P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:104:P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:105:P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:107:   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:108:P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:109:P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:110:P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:111:P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:112:P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:113:P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:114:P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:115:P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:116:\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:117:P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:118:P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:119:P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:120:P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:121:P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:130:\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:141:  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:144:  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:149:  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:150:  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:151:  report this as a \emph{validation-protocol refinement relative to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:162:\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:165:\emph{three independent reference ranges} simultaneously:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:198:(\S\ref{ssec:graph}); the $\Ph^{-2}$ shift in $\Cph$ is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:199:stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:201:any specific subject (\S\ref{sec:chain}). Three-way overlap on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:15:\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any validation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:22:in \texttt{docs/brain\_mapping/PREREG\_H4\_FINGERPRINT.md} and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:23:\texttt{docs/brain\_mapping/PREREG\_RUNG\_OBSERVABLES.md}. \emph{We do
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:25:listed as future strengthening builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:28:recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:30:propofol switching ratio, propofol continuity drop, propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:41:(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:60:P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:63:\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:64:P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:69:P10 (chess null) & \texttt{run\_chess\_robustness.py} & 30210 & same & $\geq 50\%$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:71:P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:75:P16 (conv null) & \texttt{run\_conversation\_robustness.py} & 30210 & same & $\geq 50\%$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:77:P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:79:Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:93:\textbf{OpenNeuro \texttt{ds005620}.} Propofol-induced loss of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:95:DOI \texttt{10.18112/openneuro.ds005620.v1.0.0}. Used as the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:99:\textbf{OpenNeuro \texttt{ds004902}.} DMT-induced altered states
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:101:DOI \texttt{10.18112/openneuro.ds004902.v1.0.8}. Background
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:104:\textbf{Zenodo \texttt{3992359}.} DMT EEG public
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:106:DOI \texttt{10.5281/zenodo.3992359}. Same status as above.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:133:$\arg\max|\mathrm{state}_{t}|\neq \arg\max|\mathrm{state}_{t-1}|$;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:159:$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:169:\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:175:\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:176:generalisable lesson is recorded in \S\ref{sec:limitations}: any
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:184:  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:186:  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:188:  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:190:  \texttt{python3 run\_preregistered\_validation.py}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:193:  \texttt{bash reproduce\_paper\_claims.sh}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:19:consistent with under \emph{no} shape parameter tuning, no learned
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:34:We claim a single \emph{substrate witness}: that a geometry-fixed
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:48:  as observed (\S\ref{sec:substrate}). The response operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:61:  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:67:  test; \emph{no preregistered threshold has been modified}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:78:\subsection*{What this paper does \emph{not} claim}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:81:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:87:\item \emph{Not a derivation of consciousness.} The substrate witness
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:89:  establish that the substrate \emph{is} consciousness, nor that
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:91:\item \emph{Not a selection theorem.} The companion adaptive-closure-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:93:  proposes a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:99:  builds in~\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:100:\item \emph{Not a circuit-level model.} The substrate is at the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:105:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:117:$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:118:$\mathcal C_{\mathrm{admissible}}$ by the rule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:120:q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow \mathcal C_{\mathrm{admissible}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:122:\mathcal C_{\mathrm{admissible}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:125:We never write `the substrate \emph{is} cortex' or `derives consciousness'.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:134:and applied throughout~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:140:\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:144:\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:147:that cortex \emph{is} the 600-cell.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:153:\S\ref{sec:method} gives the provenance ledger (preregistration date,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:154:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:157:\S\ref{sec:chain} adds the recurrent self-model layer above the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:159:\S\ref{sec:results} reports the empirical tables: six drug/sleep
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:161:$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:163:$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:164:selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:167:\S\ref{sec:limitations} enumerates limitations and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:168:hostile-review guard matrix. \S\ref{sec:conclusion} concludes.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:16:$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:22:thresholds (Sleep-EDFx, OpenNeuro \texttt{ds005620}, Brodbeck 2012,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:26:$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:39:the documented \texttt{homeostatic\_reset} state-reset protocol. No
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:44:\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:54:high-per-seed-variance term ($\mathrm{std}=0.089$ at $N\!=\!20$); we
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:72:\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:84:explicitly listed in~\S\ref{sec:limitations} and remain open.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:5:This section constructs the substrate. \S\ref{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:6:gives the vertex set. \S\ref{ssec:graph} gives the graph and its
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:7:H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:9:\S\ref{ssec:shells} gives the 9-shell decomposition used for source
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:10:projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:11:descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:29:\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:45:\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:65:(\texttt{kernel/vfd\_closure\_kernel.py:compute\_graph\_laplacian});
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:75:for the Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:78:(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}) realises the block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:81:\S\ref{sec:chain} (the $K_{7}$-class projector is the default
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:84:\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:97:\emph{not} a derived theorem; it is a stability choice. The companion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:107:in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:108:$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:110:$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:119:varies between conditions in~\S\ref{sec:chain}; it is reported
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:133:$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:140:The recurrent layer in~\S\ref{sec:chain} references a cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:141:decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:143:\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:148:\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:157:by the empirical correspondences in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:172:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:5:This section reports three cross-domain witnesses. \S\ref{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:6:gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:8:\S\ref{ssec:hcp} gives the HCP brain-graph maximum-symmetry null.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:10:$A_{d} = \mathrm{Acc}_{\mathrm{sub}, d} - \mathrm{Acc}_{\mathrm{raw}, d}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:12:$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}})/\sigma_{\mathrm{HCP}}$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:14:\texttt{docs/brain\_mapping/CROSS\_DOMAIN\_RESULTS.md}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:24:frames; substrate run forward by $n_{\mathrm{ticks}}$; resulting
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:31:\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:43:$n_{\mathrm{ticks}}$ & accuracy \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:65:P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:66:P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:67:P11 & random-label baseline (20 trials)     & $\in[15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:68:P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:69:\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:94:(\S\ref{sec:method}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:124:P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:125:P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:126:P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:144:(\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:156:$\Lop$. By H$_4$ transitivity (\S\ref{ssec:graph}) every vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:180:\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:188:  $0.0000$, $\checkmark$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:190:  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:208:$\mathrm{PR}(G) = (\sum_{i} d_{i})^{2} / \sum_{i} d_{i}^{2}$ is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:210:the graph. We report the raw $\mathrm{PR}$ values
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:211:($\mathrm{ARIA}=68.54$ on a 120-node graph; $\mathrm{HCP}=19.72$ on a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:216:$\mathrm{PR}/|V|$ gives $\mathrm{ARIA}=0.571$ vs $\mathrm{HCP}=0.394$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:233:  (\S\ref{sec:limitations}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:237:            \texorpdfstring{$+$}{+} maximum-symmetry null}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:263:\emph{selectively} amplifying (not unconditionally), and it is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:47:IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:48:wake). The $\Phi$ proxy (\S\ref{sec:chain}) is designed to be small
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:57:The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:85:$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:87:regulariser $R_{\mathrm{hom}}$. We propose the dictionary
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:88:$D_{\mathrm{ACT}}$:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:90:D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:92:(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:93:   \ \texttt{homeostatic\_reset}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:107:  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:108:  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:115:\emph{substrate witness} for the family that ACT names; ACT is not the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:138:\emph{a hypothesis the substrate witness raises}, not as a proof.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:160:  document the drift. Generalisable lesson: \emph{published
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:167:The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:174:Stochastic nulls (Erd\H{o}s--R\'enyi, configuration model,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:189:  see \S\ref{sec:limitations}.)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:2:\section{Stress test: the C\texorpdfstring{$\times$}{x}P synergy at adequate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:21:(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:31:\subsection{The trend across \texorpdfstring{$N$}{N}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:46:       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:58:\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:63:($D, E$ held on). Bootstrap $n_{\mathrm{resamples}}\!=\!2000$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:65:(\texttt{demo\_p4\_cxp\_deep\_dive.py}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:67:\textbf{Per-condition means at \texorpdfstring{$N\!=\!20$}{N=20}.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:86:\textbf{Main effects at \texorpdfstring{$N\!=\!20$}{N=20}.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:118:in \emph{which} vertices are uncrossed (frame rotation churns the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:125:so $C$ and $P$ are \emph{strongly coupled} cascade-state stabilisers
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:131:was conducted \emph{after} the original $N\!=\!3$ failure
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:139:\S\ref{sec:limitations}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:141:\textbf{What this stress test does \emph{not} establish.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:152:is a \emph{description} of what $C$ and $P$ do on the substrate, not a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:9:$G\colon \mathrm{risk} \to (\mathrm{disclosure}, \mathrm{evidence},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:10:\mathrm{strengthening\ build})$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:19:\emph{Disclosure:} substrate-witness scope, no uniqueness claim
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:20:(\S\ref{sec:intro}). \emph{Evidence:} empirical correspondences hold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:21:on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:27:six-signature results in~\S\ref{ssec:six_signatures} are reported on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:31:WAKE 95\% CI $[1.82, 2.86]$. \emph{Disclosure:} explicitly single-seed
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:32:in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:33:\emph{Evidence:} bootstrap CI on the wake 58 events, plus three-way
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:35:\emph{Strengthening build:} 10--20 cross-seed runs of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:36:\texttt{demo\_drug\_sleep\_v4.py}, with per-signature bootstrap CIs.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:48:design choices iterated to v4. \emph{Disclosure:}~\S\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:49:explicitly frames v4 as a redesign. \emph{Evidence:} amplitudes and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:52:\texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}. \emph{Strengthening
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:60:level rigorous (H$_4$ Coxeter group theory), the choice of \emph{this}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:63:\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:64:derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:66:transitivity theorem ($P17$). \emph{Strengthening build:} comparison
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:68:ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:75:predictions through different intermediate variables. \emph{Disclosure:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:76:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:77:\emph{Evidence:} block-diagonalisation at $<10^{-15}$ cross-block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:78:norm. \emph{Strengthening build:} catalogue and equivalence-prove the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:83:strictly positive definite (\S\ref{ssec:cphi}); it is not derived
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:84:from a closure functional or symmetry argument. \emph{Disclosure:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:85:\S\ref{ssec:cphi} marks this as a design-level choice; the companion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:87:derive it. \emph{Evidence:} the same operator (with the same shift)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:89:witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:98:signatures on a deterministic trajectory. \emph{Disclosure:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:99:\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:100:\emph{Evidence:} six signatures vs published thresholds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:101:\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:105:\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:106:IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:107:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:108:matches IIT direction. \emph{Strengthening build:} a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:109:\texttt{phi\_iit\_full} implementation following Balduzzi--Tononi
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:115:\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:116:$\sigma$-distances on three independent metrics. \emph{Strengthening
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:124:methodology issue, not a threshold change. \emph{Disclosure:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:125:\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:126:\emph{Evidence:} bootstrap CI fully above the $+0.10$ floor; per-seed
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:127:distribution narrow at $N\!=\!20$ ($\mathrm{std}=0.089$);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:128:$19/20$ seeds positive. \emph{Strengthening build:} a second
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:135:\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md} with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:137:post-refinement values. \emph{Disclosure:} this paper carries those
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:138:disclosures verbatim. \emph{Evidence:} 2026-04-20 vs 2026-04-29 side-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:139:by-side results table. \emph{Strengthening build:} the strengthening
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:143:are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:144:proxy, not the Balduzzi--Tononi 2008 algorithm. \emph{Disclosure:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:145:this section. \emph{Strengthening build:} Bayesian posterior on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:172:  4-polytopes — see~\S\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:187:not claim the substrate \emph{is} consciousness. We do not claim a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:5:The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:6:cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:8:regime-switching, propofol $\Phi$ collapse — we add a recurrent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:17:signatures in~\S\ref{sec:results}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:21:Implementation: \texttt{kernel/self\_model\_stream.py:SelfModelLoop}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:24:f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:25:\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:26:\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:27:\mathrm{state}_{t} &= \mathrm{decay}\cdot\mathrm{state}_{t-1} + (1-\mathrm{decay})\cdot \psi^{\mathrm{thr}}_{t}, \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:28:\mathrm{snap}_{t} &= \mathrm{bind\_phenomenal\_field}(\psi_{t}, \texttt{profile=K\_7\_only}),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:30:with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:31:condition-dependent architectural parameter. $f_{\mathrm{self}}$ maps
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:47:\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:49:\texttt{kernel/lyapunov\_selector.py:bounded\_topk}: zero all but the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:57:$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:64:            \texorpdfstring{$\Phi$}{Phi}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:67:\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:70:$A\in\mathbb{R}^{T\times 120}$). Define $c_{\mathrm{full}}$ as the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:74:\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:82:\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:85:We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:88:machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:89:collapse in~\S\ref{sec:results} is consistent with the IIT direction
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:96:\texttt{kernel/self\_model\_stream.py:StreamContinuityScorer}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:100:b_{\mathrm{cont}} &= \mathrm{mean\ cos\text{-}sim\ of\ consecutive}\ (I, L, P)\,\mathrm{vectors},\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:101:v_{\mathrm{cont}} &= 1/(1 + 4\cdot \mathrm{var}(\mathrm{valence})),\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:102:m_{\mathrm{pers}} &= \mathrm{frac.\ of\ consecutive\ same\text{-}modality\ ticks},\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:103:i_{\mathrm{smooth}} &= 1/(1 + 4\cdot \mathrm{TV}(\mathrm{intensity})),\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:104:\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:113:\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:119:\texttt{K\_7\_only} restricts to $\sigma$-twin K-classes for modality
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:124:Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:156:artefacts (\texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} documents
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:158:\texttt{demo\_drug\_sleep\_v4.py}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:165:the C$\times$P stress test in~\S\ref{sec:stress}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:171:Implementation: \texttt{kernel/dimensional\_monitor.py:300-305}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:176:each frame's preferences. This creates churn in \emph{which}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:178:Implementation: \texttt{kernel/dimensional\_monitor.py:316-318, 823-827}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:184:Implementation: \texttt{kernel/dimensional\_monitor.py:842-855}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:190:Implementation: \texttt{kernel/dimensional\_monitor.py:320-360}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:192:The four mechanisms' \emph{targets} are geometry-pinned (D$_4$ orbits,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:197:within the factorial ablation model are reported in~\S\ref{sec:stress}.

exec
/bin/bash -lc 'LC_ALL=C rg -n "[''^'"\\x00-\\x7F]\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"\\begin{table}\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"\\begin{tabular}\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"undefined|TODO|FIXME|TBD|??|\\\\cite\\{|\\\\citep\\{\\}|\\\\ref\\{\\}\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 271ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:51:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:33:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:69:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:24:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:42:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:94:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:167:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:35:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:55:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:115:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:160:\begin{table}[ht]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:239:\begin{table}[ht]

 succeeded in 282ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:49:quantitative correspondences with neuroscience data — preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:50:on 2026-04-18 before any validation run — plus six drug/sleep EEG
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:74:We test whether a geometry-fixed substrate — the 600-cell regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:77:operator — is consistent with cortical signatures across five
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:98:pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:113:Two of four cascade mechanisms — context rotation $C$ and partial
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:114:emission $P$ — are causally identifiable within the factorial
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:32:  underpowered ablation and emerged only at $N\!\geq\!20$ — a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:85:$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:105:  monotonicity proves selection — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:108:  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:110:  family — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:112:  $W$-trajectories — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:127:homeostatic plasticity, gain control. The naive expectation — and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:128:one we held until the $N\!=\!20$ deep-dive — is that these are mostly
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:137:targets — exactly what strong synergy predicts. We position this as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:151:  rule we draw — when preregistering an interaction effect on a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:153:  scale — should be tested against other ablation matrices, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:8:wallclock — the minimal information a hostile reviewer needs to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:20:\textbf{Frozen 2026-04-24.} Two later batteries — H$_4$ fingerprint
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:21:predictions and rung observables — were preregistered on 2026-04-24
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:168:  $2I$-equivariance — open build of the ACT companion paper.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:170:  $\mathcal{F}$ — open build of the ACT companion paper.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:172:  4-polytopes — see~\S\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:9:$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:54:$N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$ sample landed on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:7:To test high-level signatures — NREM-N3 variance collapse, propofol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:8:regime-switching, propofol $\Phi$ collapse — we add a recurrent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:52:gives smooth dynamics with cascade $\alpha\approx 1.09$ — no
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:145:\textbf{RECOVERY.} Identical to WAKE — verifies deterministic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:151:biologically-motivated stimulus components — AR(1) cortical noise,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:152:attention episodes, slow-wave drive, spindles, K-complexes — at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:167:\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:173:\textbf{$C$ — Context rotation (S$^{7}$ observer frames).} The active
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:180:\textbf{$P$ — Partial emission.} High-pressure uncrossed vertices
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:186:\textbf{$E$ — Equator compensation.} The H$_3$ shell-4 equator is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:47:mechanisms — context rotation $C$ and partial emission $P$ — are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:63:$5$-fold CV — the LOO finding above is a stricter validation-protocol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:66:(threshold $|\cdot|\!<\!10$pp) — and as a maximum-symmetry
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:79:strengthening builds — cross-seed CIs on the recurrent-layer
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:83:$2I$-equivariance audit of the closure operator family — are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:91:turn the witness into a selection-theorem-grade claim — including the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:94:operator $\Cph$ — is sketched in the companion preprints and remains
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:100:permutation — well above the $25\%$ chance level for $4$ categories.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:209:node-count-dependent — its theoretical maximum is the node count of

 exited 2 in 270ms:
rg: regex parse error:
    (?:undefined|TODO|FIXME|TBD|??|\cite\{|\citep\{\}|\ref\{\})
                                ^
error: repetition operator missing expression

 succeeded in 315ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:30:\begin{tabular}{l r r l r r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:47:\begin{tabular}{c l l c c l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:99:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:173:\begin{tabular}{l c l c}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:41:\begin{tabular}{r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:61:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:120:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:166:\begin{tabular}{l r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:244:\begin{tabular}{l r r r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:56:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:38:\begin{tabular}{r l r l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:74:\begin{tabular}{l r r r}

exec
/bin/bash -lc "rg -n -F \"600-cell is\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"is consciousness\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"unique\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"selection theorem\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"Lyapunov function\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F \"P(synergy\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 305ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:148:We do not claim the 600-cell is the unique substrate consistent with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:81:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is

 exited 1 in 302ms:
 succeeded in 327ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:66:selection theorem, nor a uniqueness claim for the 600-cell among regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:148:We do not claim the 600-cell is the unique substrate consistent with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:144:\item It does not establish that the substrate is uniquely selected by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:81:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:82:  the unique substrate consistent with these signatures. Other regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:144:\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:19:\emph{Disclosure:} substrate-witness scope, no uniqueness claim
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:64:derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:76:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:90:derive the $\Ph^{-2}$ shift as the unique stability clamp under a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:188:selection theorem on the ACT bridge. We do not claim uniqueness for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:78:uniqueness claim for the 600-cell among regular 4-polytopes. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:107:unique; it is a description of the observed accuracy stack.

 succeeded in 307ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:143:\item It does not establish a Lyapunov function on the reduced flow.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:96:  non-load-bearing here. We do not deliver a Lyapunov function on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:82:HCP replication, a Lyapunov function on the reduced flow,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:104:\item A Lyapunov function $V(W)$ on the reduced flow whose

 succeeded in 316ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:66:selection theorem, nor a uniqueness claim for the 600-cell among regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:188:selection theorem on the ACT bridge. We do not claim uniqueness for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:91:\item \emph{Not a selection theorem.} The companion adaptive-closure-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:145:selection theorem on the 4-tuple bridge; circuit-level mechanistic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:166:ACT bridge (without claiming a selection theorem).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:75:derivation of consciousness, not a selection theorem on the

 exited 1 in 378ms:
exec
/bin/bash -lc "rg -n -F \"0/2000\" '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections' '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 287ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:119:(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:144:deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:145:$0/2000$ were below the preregistered floor $+0.10$; we report these
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:99:\item $0/2000$ bootstrap resamples were at or below zero, reported as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:101:\item $0/2000$ bootstrap resamples were below the preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:113:threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:114:at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:50:$N\!=\!20$ ($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples

codex
Path shorthand: `paper/` = `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper`; `docs/` = `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping`.

**1. Claim Audit**
Most headline empirical claims are now within substrate-witness scope, but not all theorem/narrative claims are publication-ready.

- **Needs fix:** stale spectrum survives outside §3. `paper/sections/03_substrate.tex:47-64` has the corrected 9-eigenvalue spectrum summing to 120, and `paper/main.tex:44-45` correctly says “reported as observed.” But `paper/sections/08_discussion.tex:178-180` and `paper/sections/10_conclusion.tex:12-13` still give the old incomplete spectrum `{0, 3, 4\Ph, 6\Ph, 12-4\Ph, 12-6\Ph, 9, 12}`. This directly reopens the Round-3 spectrum error.
- **Needs softening:** `paper/sections/03_substrate.tex:7`, `:36-38`, `:66-69` still frame the spectrum as “H4-symmetry-forced,” “standard,” and following from character theory. The paper establishes a computed spectrum; it does not provide the derivation. Use “computed from the graph; multiplicities match the expected H4 block sizes.”
- **Mostly established:** 18/18 claim is supported only with disclosed methodology refinement. The abstract and §5 do disclose 17/18 standard and 18/18 with N=20 P4 (`paper/main.tex:81-84`, `paper/sections/05_results.tex:88-92`).
- **Needs softening:** P13 is repeatedly called a “stricter” LOO refinement (`paper/main.tex:132-134`, `paper/sections/05_results.tex:126-129`, `paper/sections/07_cross_domain.tex:79-84`, `paper/sections/10_conclusion.tex:62-64`). The source preregistered P13 as 5-fold CV (`docs/PAPER_PREDICTIONS.md:115-120`). LOO is a different estimator, not automatically stricter.
- **Established within model:** C×P synergy is established within the factorial ablation model, not beyond it. The paper mostly gets this right (`paper/main.tex:112-124`, `paper/sections/06_stress_tests.tex:117-153`).
- **Needs softening:** six-signature language overstates “published-reference thresholds.” Several thresholds are literature-motivated, not directly published numeric thresholds, especially Φ ratio, continuity drop, and exact recovery (`paper/main.tex:85-91`, `paper/sections/05_results.tex:42-75`).

**2. Internal Consistency**
- Abstract headline tally is internally consistent: 17/18 standard, 18/18 after N=20 P4, no threshold change (`paper/main.tex:81-84`).
- Thresholds in §5 match preregistration for P1-P18, with the important caveat that P13 changed estimator/protocol (`docs/PAPER_PREDICTIONS.md:20-160`; `paper/sections/05_results.tex:103-121`).
- Bootstrap wording is correct in the paper: `0/2000 ... reported as 0.0000`, not `P=0` (`paper/main.tex:119-120`, `paper/sections/02_method.tex:143-147`, `paper/sections/06_stress_tests.tex:99-102`).
- Remaining inconsistency: §3 corrected spectrum vs stale spectrum in §8/§10.
- Prior Round-3 fixes are mostly closed. The remaining misses are stale spectrum in §8/§10 and a residual “six independent” formulation split across lines in methods: “test six / independent published biological signatures” (`paper/sections/02_method.tex:27-31`).

**3. External Consistency / Numerics**
Requested numerics check out against local sources.

- 6/6 v4 signatures: paper table `paper/sections/05_results.tex:24-70` matches `docs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:30-37` and `:195-202`.
- 18/18: paper `paper/sections/05_results.tex:88-121` matches `docs/VALIDATION_RESULTS_2026-04-29.md:7-15`, `:80-99`, `:262-265`.
- C×P: paper `+0.190`, `[+0.143,+0.239]`, finite bootstrap wording matches source numerics at `docs/P4_SYNERGY_FINDING.md:117-119`, `:162-168`; note source prose still has stale `P(...)=0` at `docs/P4_SYNERGY_FINDING.md:314-315` and `:408-410`, but paper correctly avoids it.
- Chess: paper `+40.6pp`, raw `53.1%`, routed `93.8%`, `n=25`, reset matches `docs/CROSS_DOMAIN_RESULTS.md:175-190`.
- HCP: paper `-11.58σ / +79.78σ / +6.80σ` matches `docs/CROSS_DOMAIN_RESULTS.md:347-362` and `:418-421`.

**4. Substrate-Witness Scope Discipline**
No sentence I found claims the substrate *is* consciousness, that the 600-cell is unique, that ACT delivers selection, or that a Lyapunov function is delivered. The scope discipline is substantially improved (`paper/main.tex:61-71`, `paper/sections/01_introduction.tex:78-111`, `paper/sections/08_discussion.tex:80-121`, `paper/sections/09_limitations.tex:180-190`).

The closest stray is future-facing: “turn the witness into a selection-theorem-grade claim” (`paper/sections/10_conclusion.tex:90-95`). It is acceptable because it says this remains future work.

**5. Tightness**
One-line edits:

- `paper/sections/05_results.tex:202-203`: replace “strongest single empirical anchor” with “one of the main empirical anchors,” because the v4 chain is single-seed and event-bootstrap only.
- `paper/sections/07_cross_domain.tex:101-106`: replace “65.4% of the observed accuracy persists” with “a 65.4 percentage-point accuracy floor persists.”
- `paper/sections/08_discussion.tex:134-138`: replace “exactly what strong synergy predicts” with “qualitatively consistent with a strong-coupling hypothesis.”
- `paper/sections/10_conclusion.tex:55-56`: replace “N≥20 minimum” with “N≈20 planning scale in this cascade matrix.”

**6. Surface Issues**
- I could not compile: `pdflatex` is not installed in this environment.
- Citation keys used in TeX all exist in `references.bib`.
- The macros `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` are used consistently.
- Likely overfull tables: several `tabular` environments have long text columns without wrapping, especially `paper/sections/02_method.tex:51-82`, `paper/sections/05_results.tex:42-73`, `:94-124`, and `paper/sections/07_cross_domain.tex:239-253`.
- Awkward reference: `paper/sections/05_results.tex:84` has `\S\ref{sec:limitations}~\ref{ssec:regime}`; use one section ref.

**7. Top Three Fixes**
1. Replace stale spectrum in `paper/sections/08_discussion.tex:178-180` and `paper/sections/10_conclusion.tex:12-13`; optionally soften §3 derivation wording at `paper/sections/03_substrate.tex:36-38`, `:66-69`.
2. Remove “stricter” from P13 LOO wording and call it a disclosed validation-protocol/estimator refinement: `paper/main.tex:132-134`, `paper/sections/05_results.tex:126-129`, `paper/sections/07_cross_domain.tex:79-84`, `paper/sections/10_conclusion.tex:62-64`.
3. Soften six-signature threshold/independence language: `paper/main.tex:85-91`, `paper/sections/02_method.tex:27-31`, `paper/sections/05_results.tex:75-84`.

**8. Verdict**
Publication ready: no — must-fix list above. The empirical numerics are now mostly correct, but the stale spectrum recurrence is a direct publication blocker, and the P13 / six-signature wording still gives a referee avoidable leverage.
tokens used
180,326
Path shorthand: `paper/` = `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper`; `docs/` = `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping`.

**1. Claim Audit**
Most headline empirical claims are now within substrate-witness scope, but not all theorem/narrative claims are publication-ready.

- **Needs fix:** stale spectrum survives outside §3. `paper/sections/03_substrate.tex:47-64` has the corrected 9-eigenvalue spectrum summing to 120, and `paper/main.tex:44-45` correctly says “reported as observed.” But `paper/sections/08_discussion.tex:178-180` and `paper/sections/10_conclusion.tex:12-13` still give the old incomplete spectrum `{0, 3, 4\Ph, 6\Ph, 12-4\Ph, 12-6\Ph, 9, 12}`. This directly reopens the Round-3 spectrum error.
- **Needs softening:** `paper/sections/03_substrate.tex:7`, `:36-38`, `:66-69` still frame the spectrum as “H4-symmetry-forced,” “standard,” and following from character theory. The paper establishes a computed spectrum; it does not provide the derivation. Use “computed from the graph; multiplicities match the expected H4 block sizes.”
- **Mostly established:** 18/18 claim is supported only with disclosed methodology refinement. The abstract and §5 do disclose 17/18 standard and 18/18 with N=20 P4 (`paper/main.tex:81-84`, `paper/sections/05_results.tex:88-92`).
- **Needs softening:** P13 is repeatedly called a “stricter” LOO refinement (`paper/main.tex:132-134`, `paper/sections/05_results.tex:126-129`, `paper/sections/07_cross_domain.tex:79-84`, `paper/sections/10_conclusion.tex:62-64`). The source preregistered P13 as 5-fold CV (`docs/PAPER_PREDICTIONS.md:115-120`). LOO is a different estimator, not automatically stricter.
- **Established within model:** C×P synergy is established within the factorial ablation model, not beyond it. The paper mostly gets this right (`paper/main.tex:112-124`, `paper/sections/06_stress_tests.tex:117-153`).
- **Needs softening:** six-signature language overstates “published-reference thresholds.” Several thresholds are literature-motivated, not directly published numeric thresholds, especially Φ ratio, continuity drop, and exact recovery (`paper/main.tex:85-91`, `paper/sections/05_results.tex:42-75`).

**2. Internal Consistency**
- Abstract headline tally is internally consistent: 17/18 standard, 18/18 after N=20 P4, no threshold change (`paper/main.tex:81-84`).
- Thresholds in §5 match preregistration for P1-P18, with the important caveat that P13 changed estimator/protocol (`docs/PAPER_PREDICTIONS.md:20-160`; `paper/sections/05_results.tex:103-121`).
- Bootstrap wording is correct in the paper: `0/2000 ... reported as 0.0000`, not `P=0` (`paper/main.tex:119-120`, `paper/sections/02_method.tex:143-147`, `paper/sections/06_stress_tests.tex:99-102`).
- Remaining inconsistency: §3 corrected spectrum vs stale spectrum in §8/§10.
- Prior Round-3 fixes are mostly closed. The remaining misses are stale spectrum in §8/§10 and a residual “six independent” formulation split across lines in methods: “test six / independent published biological signatures” (`paper/sections/02_method.tex:27-31`).

**3. External Consistency / Numerics**
Requested numerics check out against local sources.

- 6/6 v4 signatures: paper table `paper/sections/05_results.tex:24-70` matches `docs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:30-37` and `:195-202`.
- 18/18: paper `paper/sections/05_results.tex:88-121` matches `docs/VALIDATION_RESULTS_2026-04-29.md:7-15`, `:80-99`, `:262-265`.
- C×P: paper `+0.190`, `[+0.143,+0.239]`, finite bootstrap wording matches source numerics at `docs/P4_SYNERGY_FINDING.md:117-119`, `:162-168`; note source prose still has stale `P(...)=0` at `docs/P4_SYNERGY_FINDING.md:314-315` and `:408-410`, but paper correctly avoids it.
- Chess: paper `+40.6pp`, raw `53.1%`, routed `93.8%`, `n=25`, reset matches `docs/CROSS_DOMAIN_RESULTS.md:175-190`.
- HCP: paper `-11.58σ / +79.78σ / +6.80σ` matches `docs/CROSS_DOMAIN_RESULTS.md:347-362` and `:418-421`.

**4. Substrate-Witness Scope Discipline**
No sentence I found claims the substrate *is* consciousness, that the 600-cell is unique, that ACT delivers selection, or that a Lyapunov function is delivered. The scope discipline is substantially improved (`paper/main.tex:61-71`, `paper/sections/01_introduction.tex:78-111`, `paper/sections/08_discussion.tex:80-121`, `paper/sections/09_limitations.tex:180-190`).

The closest stray is future-facing: “turn the witness into a selection-theorem-grade claim” (`paper/sections/10_conclusion.tex:90-95`). It is acceptable because it says this remains future work.

**5. Tightness**
One-line edits:

- `paper/sections/05_results.tex:202-203`: replace “strongest single empirical anchor” with “one of the main empirical anchors,” because the v4 chain is single-seed and event-bootstrap only.
- `paper/sections/07_cross_domain.tex:101-106`: replace “65.4% of the observed accuracy persists” with “a 65.4 percentage-point accuracy floor persists.”
- `paper/sections/08_discussion.tex:134-138`: replace “exactly what strong synergy predicts” with “qualitatively consistent with a strong-coupling hypothesis.”
- `paper/sections/10_conclusion.tex:55-56`: replace “N≥20 minimum” with “N≈20 planning scale in this cascade matrix.”

**6. Surface Issues**
- I could not compile: `pdflatex` is not installed in this environment.
- Citation keys used in TeX all exist in `references.bib`.
- The macros `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` are used consistently.
- Likely overfull tables: several `tabular` environments have long text columns without wrapping, especially `paper/sections/02_method.tex:51-82`, `paper/sections/05_results.tex:42-73`, `:94-124`, and `paper/sections/07_cross_domain.tex:239-253`.
- Awkward reference: `paper/sections/05_results.tex:84` has `\S\ref{sec:limitations}~\ref{ssec:regime}`; use one section ref.

**7. Top Three Fixes**
1. Replace stale spectrum in `paper/sections/08_discussion.tex:178-180` and `paper/sections/10_conclusion.tex:12-13`; optionally soften §3 derivation wording at `paper/sections/03_substrate.tex:36-38`, `:66-69`.
2. Remove “stricter” from P13 LOO wording and call it a disclosed validation-protocol/estimator refinement: `paper/main.tex:132-134`, `paper/sections/05_results.tex:126-129`, `paper/sections/07_cross_domain.tex:79-84`, `paper/sections/10_conclusion.tex:62-64`.
3. Soften six-signature threshold/independence language: `paper/main.tex:85-91`, `paper/sections/02_method.tex:27-31`, `paper/sections/05_results.tex:75-84`.

**8. Verdict**
Publication ready: no — must-fix list above. The empirical numerics are now mostly correct, but the stale spectrum recurrence is a direct publication blocker, and the P13 / six-signature wording still gives a referee avoidable leverage.
