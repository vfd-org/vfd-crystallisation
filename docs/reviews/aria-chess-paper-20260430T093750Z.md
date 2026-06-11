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
session id: 019dddc0-7b9e-7001-8816-049c2d2464a2
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

ROUND 6 FOCUS. Round 5 verdict was 'Publication ready: no'. The following round-5 must-fixes have been applied — verify each is closed and flag anything new:

1. main.tex:52 'published-reference thresholds' -> 'literature-derived thresholds' (DONE)
2. sections/05_results.tex:78 'thresholds are drawn from published references' -> 'thresholds are drawn from the literature' (DONE)
3. P10 protocol disclosure: footnote at sections/07_cross_domain.tex:74 now discloses the 2026-04-18 prereg specified 20 perms but the 2026-04-29 validation used 15; threshold unchanged at >=50%; result 65.4% robust in 15-20 range; verification at prereg-exact 20 perms is an open build (added to sections/09_limitations.tex Out-of-scope items).
4. Abstract (main.tex:142-150) +79.78sigma now caveated as 'raw participation ratio' with inline node-count caveat (ARIA |V|=120 vs HCP ICA-50 |V|=50), and +6.80sigma now caveated with 'implicit HCP across-subject sd ~ 0.035 inferred from the reported gap; see ssec:hcp'.
5. sections/01_introduction.tex:17-20 'no domain-specific calibration' -> 'no subject-level measurement fitting and no neural-data-fitted shape parameters' (DONE).
6. sections/01_introduction.tex 'consciousness substrate' -> 'candidate substrate for consciousness-linked signatures' (DONE).
7. sections/01_introduction.tex:72 'maximum-symmetry deterministic null reference' -> 'H4-transitive deterministic null reference' (DONE).
8. sections/07_cross_domain.tex 'maximum-symmetry' (4 occurrences) -> 'H4-transitive' (DONE on lines 8, 146, 237, 264).
9. sections/08_discussion.tex 'fixed by group theory' (lines 19, 25) softened to 'fixed by the construction' with explicit graph-and-operator listing (DONE).
10. sections/08_discussion.tex 'maximum-symmetry connectivity null' -> 'H4-transitive connectivity null' (DONE).
11. sections/09_limitations.tex 'Type II methodology issue' -> 'consistent with underpowered interaction estimates on high-per-seed-variance terms' (DONE).
12. sections/09_limitations.tex:146 typo S^4->2^4 -> 'substrate's S^3 state space' (DONE).
13. sections/10_conclusion.tex:67 'maximum-symmetry deterministic null' -> 'H4-transitive deterministic null' (DONE).
14. sections/10_conclusion.tex:89 'graph fixed by group theory' -> 'graph fixed by the construction' (DONE).
15. main.tex:144 'maximum-symmetry deterministic null reference' -> 'deterministic null reference' (DONE; 'H4-transitive substrate' label is kept).

Verify the corrections are correct, internally consistent, do not introduce new overclaim, and check whether the paper now reads as referee-ready under hostile review. Report verdict 'Publication ready: yes' or 'Publication ready: no' with specific must-fixes if no.
warning: Codex could not find bubblewrap on PATH. Install bubblewrap with your OS package manager. See the sandbox prerequisites: https://developers.openai.com/codex/concepts/sandboxing#prerequisites. Codex will use the vendored bubblewrap in the meantime.
codex
I’ll read the WO context first, then audit the paper and source documents with line numbers so every finding can be tied to the exact text. Since this is a referee pass, I’ll focus on claims, numerics, and scope discipline rather than code-style concerns.
exec
/bin/bash -lc 'wc -l "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 215ms:
142 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md

 succeeded in 215ms:
267 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md

 succeeded in 293ms:
   212 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex
   170 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex
   201 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex
   173 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex
   197 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex
   208 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex
   168 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex
   273 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex
   207 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex
   195 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex
    96 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex
   180 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib
  2280 total

codex
The paper is about 2,100 lines plus references, and the source/context files are moderate length. I’m starting with the task context so I can judge the manuscript against its intended “substrate witness” scope rather than importing a stronger theorem standard.
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 229ms:
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

 succeeded in 240ms:
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
The WO context confirms the intended bar: strong empirical substrate witness, with ACT and selection language kept non-load-bearing. I’m now reading the manuscript sections with line numbers, then I’ll cross-check only the headline numerics against the local source documents.
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 240ms:
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
    20	weights, no subject-level measurement fitting, and no
    21	neural-data-fitted shape parameters. The substrate is the
    22	600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
    23	H$_4$ Coxeter symmetry. It has been studied in pure mathematics for
    24	over a century~\citep{CoxeterRegularPolytopes,Weisstein600Cell}; to
    25	our knowledge it has not been proposed before as an empirical
    26	candidate substrate for consciousness-linked signatures. We construct $\Rsixhundred$, fix its response
    27	operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
    28	single condition-dependent self-injection coupling $\eta$ and a
    29	single graph-pinned nonlinearity, and test the resulting witness
    30	against eighteen preregistered correspondences plus six companion
    31	drug/sleep EEG signatures.
    32	
    33	\subsection*{What this paper claims}
    34	
    35	We claim a single \emph{substrate witness}: that a geometry-fixed
    36	substrate, with no shape parameters tuned to any neural dataset, is
    37	consistent with eighteen preregistered correspondences (frozen
    38	2026-04-18) and six companion drug/sleep EEG signatures of
    39	conscious vs unconscious states.
    40	
    41	\begin{enumerate}\itemsep=2pt
    42	\item \textbf{Substrate is fixed once chosen.} Once $\Rsixhundred$
    43	  is selected, the vertex set ($|V|=120$, all on the unit
    44	  $3$-sphere) is forced by the canonical 600-cell construction; H$_4$
    45	  transitivity forces uniform vertex degree (here $12$ on the
    46	  short-edge nearest-neighbour graph); and the Laplacian spectrum is
    47	  computed from the resulting graph and reported as observed, with
    48	  multiplicities matching the expected H$_4$ block sizes
    49	  (\S\ref{sec:substrate}). The response operator
    50	  $\Cph = \Lop + \Ph^{-2} I$ is fully fixed once the graph is
    51	  constructed and the stability shift $\Ph^{-2}$ is chosen as a
    52	  design-level clamp.
    53	\item \textbf{Cortical avalanches.} Wake cascade-event power-law
    54	  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
    55	  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
    56	  (n$=$30 subjects) and ARIA's prior cascade-pipeline CI
    57	  $[2.73, 3.25]$.
    58	\item \textbf{Six drug/sleep signatures.} On a single deterministic
    59	  trajectory at seed $42$: NREM-N3 phenomenal-intensity variance
    60	  collapse to $0.463\!\times$ wake; propofol modality-switching
    61	  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
    62	  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
    63	  recovery deterministically identical to wake; wake cascade-$\alpha$
    64	  in the SOC band.
    65	\item \textbf{Eighteen preregistered correspondences pass.}
    66	  $17/18$ at standard methodology; $18/18$ after a documented
    67	  $N\!=\!20$ deep-dive on the residual high-variance interaction
    68	  test; \emph{no preregistered threshold has been modified}.
    69	\item \textbf{Cross-domain selectivity.} The substrate exhibits
    70	  selective amplification in the two cross-domain tasks tested
    71	  (chess $+40.6$pp leave-one-out lift at depth $n\!=\!25$ ticks;
    72	  conversation $-4.4$pp lift, within preregistered neutrality bounds)
    73	  and serves as an H$_4$-transitive deterministic null reference for
    74	  cortical functional connectivity (HCP full-cohort descriptive
    75	  $n\!=\!1003$: ARIA at $-11.58\sigma$ on degree homogeneity;
    76	  $+79.78\sigma$ on raw participation ratio with the node-count caveat
    77	  of \S\ref{ssec:hcp}).
    78	\end{enumerate}
    79	
    80	\subsection*{What this paper does \emph{not} claim}
    81	
    82	\begin{itemize}\itemsep=2pt
    83	\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
    84	  the unique substrate consistent with these signatures. Other regular
    85	  4-polytopes (the 24-cell, the 120-cell) are an explicit ablation
    86	  build, not a discharged comparison. The 600-cell choice is post-hoc
    87	  motivated by the H$_4$ Coxeter cascade structure and biological
    88	  observables; it is not an a-priori derivation from first principles.
    89	\item \emph{Not a derivation of consciousness.} The substrate witness
    90	  shows quantitative agreement with cortical signatures; it does not
    91	  establish that the substrate \emph{is} consciousness, nor that
    92	  its dynamics implement specific phenomenal content.
    93	\item \emph{Not a selection theorem.} The companion adaptive-closure-
    94	  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
    95	  proposes a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which
    96	  this substrate fills the $L_M$ slot. The selection of the 600-cell
    97	  as the active $M$ is conjectural in that paper and is treated as
    98	  non-load-bearing here. We do not deliver a Lyapunov function on the
    99	  reduced flow, nor a $2I$-equivariance audit of the closure operator,
   100	  nor a formal edge-space decomposition. These are listed as open
   101	  builds in~\S\ref{sec:limitations}.
   102	\item \emph{Not a circuit-level model.} The substrate is at the
   103	  architectural-algorithmic level. We do not identify which neural
   104	  populations implement context rotation or partial emission, only
   105	  that some such mechanisms appear in the substrate's preregistered
   106	  ablation matrix and exhibit strong inter-mechanism coupling.
   107	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
   108	  Laplacian floor $\Ph^{-2} \approx 0.382$ is a design-level
   109	  stability clamp (it makes $\Cph$ strictly positive definite and
   110	  bounds the Green response). It is not derived as a theorem from a
   111	  closure functional. The companion kernel
   112	  document~\citep{SmartAriaClosureKernel2026} discusses its role.
   113	\end{itemize}
   114	
   115	\subsection*{Mapping from numerical results to admissible claims}
   116	
   117	To keep this paper inside the substrate-witness scope, we use the
   118	following claim-boundary discipline. Numerical results
   119	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   120	$\mathcal C_{\mathrm{admissible}}$ by the rule
   121	\[
   122	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow \mathcal C_{\mathrm{admissible}},
   123	\qquad
   124	\mathcal C_{\mathrm{admissible}}
   125	\;=\;\{\text{`consistent with', `inside threshold', `direction confirmed'}\}.
   126	\]
   127	We never write `the substrate \emph{is} cortex' or `derives consciousness'.
   128	A result that lands inside its preregistered threshold licenses a
   129	`consistent with' claim. A result that exceeds the preregistered
   130	threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
   131	$+15$pp floor) licenses `decisively above prereg', not `proves'. A
   132	$\sigma$-distance result against an external null
   133	(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
   134	the biological distribution', not `cortex has drifted from an ideal
   135	polytope'. The claim-boundary rule is summarised in the box below
   136	and applied throughout~\S\ref{sec:results}.
   137	
   138	\medskip
   139	\begin{center}
   140	\fbox{\parbox{0.92\linewidth}{\small
   141	\textbf{What is tested / what is not claimed.}\par
   142	\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
   143	signatures, on a geometry-fixed substrate with one condition-dependent
   144	parameter $\eta$ and one graph-pinned nonlinearity, against published
   145	biological observables.\par
   146	\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
   147	selection theorem on the 4-tuple bridge; circuit-level mechanistic
   148	identification; first-principles derivation of $\Ph^{-2}$ shift;
   149	that cortex \emph{is} the 600-cell.
   150	}}
   151	\end{center}
   152	
   153	\subsection*{Layout}
   154	
   155	\S\ref{sec:method} gives the provenance ledger (preregistration date,
   156	seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
   157	constructs $\Rsixhundred$ and the response operator $\Cph$, with the
   158	$\Ph^{-2}$ shift disclosed as a design-level stability clamp.
   159	\S\ref{sec:chain} adds the recurrent self-model layer above the
   160	substrate (single nonlinearity, single self-injection coupling).
   161	\S\ref{sec:results} reports the empirical tables: six drug/sleep
   162	signatures, eighteen preregistered correspondences, three-way
   163	$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
   164	synergy stress test ($N\!=\!3, 5, 10, 20$ trend with bootstrap
   165	$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
   166	selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
   167	discusses the substrate witness and proposes a non-load-bearing
   168	ACT bridge (without claiming a selection theorem).
   169	\S\ref{sec:limitations} enumerates limitations and the
   170	hostile-review guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 251ms:
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
    52	literature-derived thresholds on a single deterministic substrate
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
    88	P1--P18 preregistration; they are tested against thresholds drawn
    89	from the published literature (Sleep-EDFx CI for the wake $\alpha$,
    90	OpenNeuro \texttt{ds005620} point-estimate window for propofol
    91	switching, literature-direction predictions for $\Phi$ collapse,
    92	continuity drop, and recovery; \S\ref{sec:method}). They were
    93	obtained under condition-specific v4 stimulus models redesigned to
    94	be biologically realistic (\S\ref{sec:chain}).
    95	
    96	\noindent\emph{(i) Cortical avalanches.}
    97	Wake cascade-event power-law exponent $\alpha = 2.252$,
    98	$95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$, $n_{\mathrm{events}}=58$).
    99	This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
   100	subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
   101	pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
   102	overlap.
   103	
   104	\noindent\emph{(ii) Drug/sleep state transitions.}
   105	NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
   106	(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
   107	ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
   108	reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
   109	propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
   110	integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
   111	direction confirmed); recovery deterministically identical to wake.
   112	All six signatures pass against their literature-derived thresholds
   113	on the single deterministic substrate trajectory.
   114	
   115	\noindent\emph{(iii) Causal mechanism isolation.}
   116	Two of four cascade mechanisms — context rotation $C$ and partial
   117	emission $P$ — are causally identifiable within the factorial
   118	ablation model, and the original preregistered C$\times$P synergy
   119	prediction $\geq +0.10$ closes
   120	decisively at adequate replication: $N\!=\!20$ fresh seeds give a
   121	bootstrap point estimate of $+0.190$ with $95\%$ CI $[+0.143, +0.239]$
   122	(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
   123	below zero, reported as $0.0000$. We document the original $N\!=\!3$
   124	underestimate ($+0.044$) as consistent with an underpowered interaction
   125	estimate at $N\!=\!3$. In this cascade matrix, P4 required $N\!=\!20$;
   126	future preregistrations on similar high-variance ablation matrices
   127	should budget for this scale.
   128	
   129	\noindent\emph{(iv) Cross-domain selectivity.}
   130	The substrate exhibits selective amplification in the two cross-domain
   131	tasks tested: chess 4-category position classification on
   132	8-dimensional V2 features lifts $+40.6$ percentage points on
   133	leave-one-out at canonical depth $n\!=\!25$ ticks (raw $53.1\%$
   134	$\to$ substrate-routed $93.8\%$, with state reset; the
   135	preregistered estimator P13 was $5$-fold CV with threshold
   136	$\geq\!+15$pp, the LOO finding above is a disclosed estimator/protocol
   137	refinement at the same threshold), while conversation utterance
   138	classification at raw $87.5\%$ yields a substrate lift of $-4.4$pp
   139	(threshold $|\cdot| < 10$pp), consistent with the substrate
   140	amplifying in these two tasks where raw features are ambiguous and
   141	remaining approximately neutral when raw features are already
   142	discriminative. On HCP brain functional connectivity
   143	(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
   144	descriptive statistics), the H$_4$-transitive substrate is a
   145	deterministic null reference: ARIA degree std
   146	$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
   147	on degree homogeneity, $+79.78\sigma$ on raw participation ratio
   148	(with the node-count caveat documented at \S\ref{ssec:hcp}: ARIA
   149	$|V|\!=\!120$ vs HCP ICA-50 $|V|\!=\!50$; the $\sigma$ value reflects
   150	both architectural and node-count differences), and $+6.80\sigma$ on
   151	clustering coefficient (implicit HCP across-subject sd $\approx 0.035$
   152	inferred from the reported gap; see \S\ref{ssec:hcp}).
   153	
   154	\noindent\emph{What we do not claim.}
   155	We do not claim the 600-cell is the unique substrate consistent with
   156	these signatures, nor that other regular 4-polytopes (24-cell, 120-cell)
   157	have been ruled out. We do not derive the $\Ph^{-2}$ floor from
   158	first principles; it is a design-level stability clamp on the
   159	shifted-Laplacian response. The recurrent layer above the substrate
   160	is reported on a single deterministic trajectory; cross-seed CIs on
   161	the per-condition signatures are an explicit strengthening build.
   162	The structural scope of this paper is: \emph{a geometry-fixed
   163	substrate, with no shape parameters tuned to any neural dataset,
   164	is consistent with eighteen preregistered neuroscience
   165	correspondences and six drug/sleep EEG signatures, with all gaps in
   166	the original preregistration closed by methodology refinement and
   167	without modifying any preregistered threshold.}
   168	\end{abstract}
   169	
   170	% =====================================================================
   171	\input{sections/01_introduction.tex}
   172	\input{sections/02_method.tex}
   173	\input{sections/03_substrate.tex}
   174	\input{sections/04_consciousness_chain.tex}
   175	\input{sections/05_results.tex}
   176	\input{sections/06_stress_tests.tex}
   177	\input{sections/07_cross_domain.tex}
   178	\input{sections/08_discussion.tex}
   179	\input{sections/09_limitations.tex}
   180	\input{sections/10_conclusion.tex}
   181	% =====================================================================
   182	
   183	\section*{Acknowledgements}
   184	We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
   185	OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
   186	the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
   187	the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
   188	HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
   189	datasets that made these comparisons possible. Cortical avalanche
   190	methodology follows~\citep{BeggsPlenz2003}; the integrated-information
   191	$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
   192	the propofol microstate comparison uses Brodbeck et
   193	al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
   194	follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
   195	and processed data are released under MIT licence at the project
   196	repository~\citep{ariaChessRepo}.
   197	
   198	\section*{Reproducibility}
   199	The complete pipeline (substrate construction, six-signature
   200	consciousness chain, $N\!=\!20$ C$\times$P deep-dive, eighteen-prediction
   201	preregistered validation, figure regeneration, this paper) is reproducible
   202	from the project repository~\citep{ariaChessRepo} via the included
   203	\texttt{reproduce\_paper\_claims.sh} script. All scripts are
   204	deterministic given seeds; the substrate's spectral decomposition is
   205	cached at module level. Wallclocks: drug/sleep v4 $\sim 30$\,s;
   206	$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
   207	$\sim 18$\,min.
   208	
   209	\bibliographystyle{plainnat}
   210	\bibliography{references}
   211	
   212	\end{document}

 succeeded in 305ms:
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
    28	recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six companion
    29	biological signatures with literature-derived thresholds (NREM-N3
    30	variance ratio, propofol switching ratio, propofol continuity drop,
    31	propofol $\Phi$ collapse, recovery reversibility, wake
    32	cascade-$\alpha$). They are not part of the P1--P18 preregistration;
    33	they are reported as a companion validation set on the recurrent
    34	layer.
    35	
    36	\textbf{No threshold has been modified post-hoc.} Where the original
    37	2026-04-20 validation reported failures (P3, P4, P13), the documented
    38	methodological refinements were
    39	(a)~increasing $N$ from $3$ to $5$ for cascade interaction terms,
    40	(b)~adding a $N\!=\!20$ deep-dive for the highest-variance interaction
    41	(P4, C$\times$P), and
    42	(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
    43	measurements for the chess LOO test (P13). None of these touched a
    44	preregistered threshold.
    45	
    46	\subsection{Provenance ledger}
    47	
    48	We write the provenance map as $\Pi\colon\{\text{claim id}\}
    49	\to (\text{script}, \text{seed range}, \text{dataset/source},
    50	\text{threshold}, \text{result})$.
    51	
    52	\begin{table}[ht]
    53	\centering
    54	\small
    55	\caption{Provenance ledger for the headline empirical claims.}
    56	\label{tab:provenance}
    57	\begin{tabular}{l l l l l}
    58	\toprule
    59	Claim & Script & Seed range & Dataset / source & Threshold \\
    60	\midrule
    61	P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
    62	P2 ($C$ main) & same & 30010--30014 & this paper & $\geq +0.30$ \\
    63	P3 ($|D{\times}C|$) & same & 30020--30024 & this paper & $|\cdot| < 0.20$ \\
    64	\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
    65	P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
    66	P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
    67	P7 ($W{\to}N3$ var) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.70$ \\
    68	P8 ($W{\to}N3$ switch) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.50$ \\
    69	P9 (chess 5-fold) & same & 30200--30204 & 32 positions, 4 cat. & $\geq 70\%$ \\
    70	P10 (chess null) & \texttt{run\_chess\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    71	P11 (chess random-label) & same & 30210+ & same & $\in [15\%, 35\%]$ \\
    72	P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
    73	\textbf{P13 (chess sub.\ lift)} & same & with reset & same (LOO refinement) & $\geq +15$pp \\
    74	P14 (conv 5-fold) & same & 30220--30224 & 64 utt., 8 cat. & $\geq 75\%$ \\
    75	P15 ($|$conv lift$|$) & same & same & same & $|\cdot| < 10$pp \\
    76	P16 (conv null) & \texttt{run\_conversation\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    77	P17 (ARIA deg std) & substrate construction & deterministic & H$_4$ theorem & $=0$ \\
    78	P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
    79	\midrule
    80	Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
    81	\bottomrule
    82	\end{tabular}
    83	\end{table}
    84	
    85	\subsection{Datasets and DOIs}
    86	
    87	\textbf{Sleep-EDFx (PhysioNet).} Public polysomnography
    88	recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
    89	the cortical-avalanche $\alpha$ baseline; $n=24$ subjects used for
    90	the wake$\to$N3 variance and switching ratios. Cortical-avalanche
    91	fitting follows the Beggs--Plenz log-CCDF
    92	methodology~\citep{BeggsPlenz2003}.
    93	
    94	\textbf{OpenNeuro \texttt{ds005620}.} Propofol-induced loss of
    95	consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
    96	DOI \texttt{10.18112/openneuro.ds005620.v1.0.0}. Used as the
    97	empirical reference for the propofol switching ratio
    98	($2.96\!\times$ wake) in Sig~2.
    99	
   100	\textbf{OpenNeuro \texttt{ds004902}.} DMT-induced altered states
   101	EEG~\citep{OpenNeuroDS004902},
   102	DOI \texttt{10.18112/openneuro.ds004902.v1.0.8}. Background
   103	psychedelic-state reference; not load-bearing for the headline tally.
   104	
   105	\textbf{Zenodo \texttt{3992359}.} DMT EEG public
   106	release~\citep{ZenodoDMT3992359},
   107	DOI \texttt{10.5281/zenodo.3992359}. Same status as above.
   108	
   109	\textbf{HCP S1200.} Human Connectome Project
   110	S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
   111	matrix. The preregistered test (P18) was on $n=100$ subjects for
   112	computational tractability; full-cohort $n=1003$ statistics
   113	(degree std, participation ratio, clustering coefficient $\sigma$-
   114	distances) are reported as descriptive statistics on top of the
   115	preregistered test.
   116	
   117	\textbf{Microstate baseline (qualifier).} The continuity-drop
   118	signature (Sig~3) follows the EEG microstate methodology lineage of
   119	Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
   120	microstates. Brodbeck et al.\ is not a propofol-specific paper; we
   121	use it for the underlying microstate-fragmentation methodology, not
   122	as a propofol reference. A propofol-specific microstate citation
   123	would tighten this section; we treat that as an open
   124	strengthening build.
   125	
   126	\subsection{Statistical methods}
   127	
   128	\textbf{Cascade-$\alpha$ fitting.} Power-law $\alpha$ is fit by
   129	ordinary least squares on the log-CCDF of the cascade-event size
   130	distribution, restricted to the central 80\% mass band (excluding the
   131	bottom 10\% and top 10\% to avoid extreme-tail noise). $R^{2}$ is
   132	reported on the linear fit in log-space. A cascade event is defined
   133	as an attention-vertex shift between consecutive ticks
   134	$\arg\max|\mathrm{state}_{t}|\neq \arg\max|\mathrm{state}_{t-1}|$;
   135	the event size is the $\ell^{1}$ norm of the state-difference vector
   136	at that tick. Zero-size events are excluded.
   137	
   138	\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
   139	estimated by event-resampling bootstrap (500 resamples for the
   140	preregistered cascade-$\alpha$ tests, 2000 resamples for the
   141	$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
   142	preregistered; 42 for the deep-dive.
   143	
   144	\textbf{Bootstrap one-sided $P$-value reporting.} For the C$\times$P
   145	deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
   146	$0/2000$ were below the preregistered floor $+0.10$; we report these
   147	as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
   148	zero-probability statement on a finite resample.
   149	
   150	\textbf{Factorial interaction estimator.} For the $2{\times}2$
   151	ablation conditions $\{----, -C--, --P-, -CP-\}$, the interaction is
   152	\[
   153	\Delta_{CP}
   154	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
   155	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
   156	\]
   157	
   158	\textbf{$\sigma$-distance against external nulls.} For the HCP
   159	comparisons we report
   160	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
   161	on the full $n=1003$ subject distribution.
   162	
   163	\subsection{State-reset protocol}
   164	
   165	The substrate exhibits state drift: across approximately five
   166	successive depth-sweep evaluations the pressure field equilibrates
   167	to a uniform attractor and classification structure collapses to
   168	raw-feature baseline. Multi-trial benchmarks therefore require an
   169	explicit reset between successive evaluations.
   170	\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
   171	re-initialises pressure-field, crossed-vertex, and training state to
   172	canonical baseline. With reset between depth measurements, the chess
   173	LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
   174	substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
   175	preregistered floor). The reset protocol is documented in
   176	\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
   177	generalisable lesson is recorded in \S\ref{sec:limitations}: any
   178	multi-trial benchmark on a non-stationary substrate must specify
   179	state-reset protocol.
   180	
   181	\subsection{Reproducibility commands}
   182	
   183	\begin{itemize}\itemsep=2pt
   184	\item Substrate self-test:
   185	  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
   186	\item Six drug/sleep signatures:
   187	  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
   188	\item C$\times$P synergy $N\!=\!20$ deep-dive:
   189	  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
   190	\item Eighteen preregistered:
   191	  \texttt{python3 run\_preregistered\_validation.py}
   192	  ($\sim 18$\,min).
   193	\item Whole-paper repro:
   194	  \texttt{bash reproduce\_paper\_claims.sh}.
   195	\end{itemize}
   196	
   197	All scripts are deterministic given seeds. Reruns at seed $42$ on the
   198	recurrent layer should reproduce per-condition means in this paper to
   199	4~decimal places. Bootstrap CIs may differ in the 4th decimal due to
   200	NumPy version differences in the bootstrap RNG; the qualitative
   201	verdicts (CI overlaps, $P$-value thresholds) are unaffected.

 succeeded in 300ms:
     1	% =====================================================================
     2	\section{The 600-cell response substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section constructs the substrate. \S\ref{ssec:vertices}
     6	gives the vertex set. \S\ref{ssec:graph} gives the graph and its
     7	computed Laplacian spectrum. \S\ref{ssec:cphi} gives the response
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
    36	local structure. We compute the resulting Laplacian spectrum from the
    37	constructed graph; multiplicities match the expected H$_4$ block
    38	sizes. The 600-cell construction itself is
    39	standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    40	\paragraph{Graph facts (forced by the construction).}
    41	The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, and
    42	every vertex has degree exactly $12$ (H$_4$ transitivity acts on the
    43	vertex set; the short-edge nearest-neighbour graph inherits this
    44	uniformity). These facts are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}
    45	and reproduced numerically by
    46	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
    47	
    48	\paragraph{Laplacian spectrum (computed numerically).}
    49	The unweighted graph Laplacian $\Lop = D - A$ has nine distinct
    50	eigenvalues with multiplicities summing to $120$:
    51	\[
    52	\sigma(\Lop) \;=\;
    53	\bigl\{0^{1},\;
    54	       (12\!-\!6\Ph)^{4},\;
    55	       (12\!-\!4\Ph)^{9},\;
    56	       9^{16},\;
    57	       12^{25},\;
    58	       14^{36},\;
    59	       (4\Ph + 8)^{9},\;
    60	       15^{16},\;
    61	       (6\Ph + 6)^{4}\bigr\},
    62	\]
    63	i.e.\ approximately $\{0, 2.292, 5.528, 9, 12, 14, 14.472, 15, 15.708\}$
    64	with multiplicities $\{1, 4, 9, 16, 25, 36, 9, 16, 4\}$. We computed
    65	this directly from the constructed Laplacian
    66	(\texttt{kernel/vfd\_closure\_kernel.py:compute\_graph\_laplacian});
    67	the spectrum is reproducible at machine precision and the
    68	multiplicities match the expected H$_4$ block sizes. We do not derive
    69	the closed-form entries here; the values in $\mathbb{Z}[\Ph]$ are
    70	reported as observed.
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

exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 265ms:
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

 succeeded in 278ms:
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
    75	All six signatures pass against their literature-derived thresholds
    76	on the same deterministic substrate trajectory. The six signatures
    77	are not part of the dated 2026-04-18 P1--P18 preregistration; their
    78	thresholds are drawn from the literature (Sleep-EDFx CI for
    79	wake $\alpha$, OpenNeuro \texttt{ds005620} point-estimate window for
    80	propofol switching, literature-direction predictions for $\Phi$
    81	collapse, continuity drop, and recovery). They were tested on a
    82	recurrent-layer architecture redesigned at v4 with
    83	biologically-motivated condition-specific stimulus models
    84	(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    85	documents the v3$\to$v4 stimulus redesign). The mechanistic readings
    86	in \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} are not
    87	load-bearing for the headline claim. Single-seed disclosure:
    88	\S\ref{ssec:regime}.
    89	
    90	\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
    91	
    92	\textbf{Tally.} $17/18$ at standard validation
    93	(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
    94	plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
    95	on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
    96	$32000$--$32019$). \emph{No preregistered threshold has been modified.}
    97	
    98	\begin{table}[ht]
    99	\centering
   100	\small
   101	\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
   102	\label{tab:eighteen_prereg}
   103	\begin{tabular}{l l l l l}
   104	\toprule
   105	ID & Test & Threshold & Observed (2026-04-29) & Verdict \\
   106	\midrule
   107	P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
   108	P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
   109	P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
   110	\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
   111	   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
   112	P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
   113	P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
   114	P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
   115	P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
   116	P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
   117	P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
   118	P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
   119	P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
   120	\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
   121	P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
   122	P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   123	P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
   124	P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
   125	P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
   126	\bottomrule
   127	\end{tabular}
   128	\end{table}
   129	
   130	\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
   131	estimator as $5$-fold CV at threshold $\geq +15$pp; the 2026-04-29
   132	validation tightened the estimator to LOO with state reset, a
   133	disclosed estimator/protocol refinement at the unchanged $+15$pp threshold. See
   134	\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
   135	
   136	\textbf{Three predictions that flipped to PASS, with documented
   137	methodology refinement (no threshold change).}
   138	\begin{itemize}\itemsep=2pt
   139	\item P3 (D$\times$C interaction independence) was outside the band
   140	  at $N\!=\!3$ ($-0.231$) and inside the band at $N\!=\!5$ ($-0.183$).
   141	  Reading: consistent with an underpowered interaction estimate at
   142	  $N\!=\!3$ on a high-per-seed-variance interaction term.
   143	\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
   144	  ($+0.044$) and at $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
   145	  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
   146	  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
   147	\item P13 (chess substrate lift): the 2026-04-18 preregistration
   148	  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
   149	  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
   150	  validation strengthened the estimator to LOO with state reset, a
   151	  disclosed estimator/protocol refinement at the same threshold; the LOO lift was $+3.1$pp
   152	  without state reset on a state-drifted substrate, and $+40.6$pp
   153	  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
   154	  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
   155	  report this as a \emph{validation-protocol refinement relative to
   156	  the preregistered test}, not as preregistration revision.
   157	\end{itemize}
   158	
   159	\textbf{Headline verdict.} Eighteen preregistered correspondences
   160	all pass at preregistered thresholds, with two interaction tests
   161	requiring $N\!\geq\!5$ and one requiring $N\!=\!20$ for reliable
   162	detection of high-variance interaction terms, and one test
   163	requiring the documented state-reset protocol. The original $15/18$
   164	result was a methodology-limited tally, not a content failure.
   165	
   166	\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
   167	
   168	The substrate's wake cascade-$\alpha$ confidence interval overlaps
   169	\emph{three independent reference ranges} simultaneously:
   170	
   171	\begin{table}[ht]
   172	\centering
   173	\small
   174	\caption{Three-way $\alpha$ overlap on the wake cascade-event power
   175	law.}
   176	\label{tab:alpha_overlap}
   177	\begin{tabular}{l c l c}
   178	\toprule
   179	Source & $\alpha$ & 95\% CI & $n$ \\
   180	\midrule
   181	ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
   182	Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
   183	ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
   184	\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
   185	\bottomrule
   186	\end{tabular}
   187	\end{table}
   188	
   189	The v4 WAKE 95\% CI $[1.82, 2.86]$ contains the upper arm of the
   190	real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
   191	cascade pipeline CI $[2.73, 3.25]$ on the interval $[2.73, 2.86]$,
   192	and lies inside the cortical-avalanche band
   193	$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
   194	intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
   195	WAKE $\cap$ cortical-avalanche band) are non-empty across three
   196	independent reference ranges.
   197	
   198	\textbf{Reading.} The substrate produces self-organised-critical
   199	cascade statistics matching the cortical-avalanche literature with
   200	no fitted parameter on neural data. The bounded-top-$K$ at
   201	$k=12$ is pinned to the substrate's average degree
   202	(\S\ref{ssec:graph}); the $\Ph^{-2}$ shift in $\Cph$ is a
   203	stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
   204	biological time-scale parameters but is not measurement-fitted to
   205	any specific subject (\S\ref{sec:chain}). Three-way overlap on the
   206	power-law exponent is one of the main empirical anchors in the paper
   207	(noting that the v4 WAKE CI is from a single deterministic trajectory
   208	with event-bootstrap; cross-seed CI is an open build).

 succeeded in 288ms:
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

 succeeded in 259ms:
     1	% =====================================================================
     2	\section{Cross-domain selectivity}\label{sec:cross_domain}
     3	% =====================================================================
     4	
     5	This section reports three cross-domain witnesses. \S\ref{ssec:chess}
     6	gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
     7	conversation neutrality result that confirms the lift is selective.
     8	\S\ref{ssec:hcp} gives the HCP brain-graph H$_4$-transitive null.
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
    77	and P16 (conversation null); both pass. The 2026-04-18 preregistration
    78	specified $20$ random label permutations for the null-mapping bound;
    79	the 2026-04-29 validation run used $15$ permutations
    80	(\texttt{run\_preregistered\_validation.py}; the $\geq 50\%$ threshold
    81	is unchanged). We report this as a disclosed-protocol deviation, not
    82	a threshold change; the observed $65.4\%$ at $15$ perms sits well
    83	above the $50\%$ floor and the result is robust to perm count in this
    84	range. Verification at the preregistered $20$-perm setting is an open
    85	build (\S\ref{sec:limitations}).
    86	
    87	$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
    88	substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
    89	The 2026-04-29 validation tightened the estimator to LOO with state
    90	reset; we report the LOO finding ($+40.6$pp) above as a disclosed
    91	estimator/protocol refinement at the unchanged $+15$pp threshold,
    92	not a preregistration revision.
    93	
    94	\textbf{Reading.} Substrate routing amplifies chess-position
    95	4-category classification from raw $53.1\%$ (just above $25\%$
    96	chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
    97	This is a $+40.6$pp lift on the LOO refinement; on the preregistered
    98	$5$-fold CV estimator the substrate-routed accuracy is $83.1\%$
    99	(P9), itself well above any reasonable raw-features baseline.
   100	The original 2026-04-20 validation reported the LOO lift at
   101	$+3.1$pp, a state-drift artefact closed by the reset protocol
   102	(\S\ref{sec:method}).
   103	
   104	\textbf{Permutation null decomposition.} The null permutation
   105	mapping (P10) randomises the feature$\to$frame assignment, so each
   106	feature is routed to a different $S^{7}$ frame than canonical. The
   107	substrate retains $65.4\%$ classification accuracy under random
   108	permutation — well above the $25\%$ chance level for $4$ categories.
   109	We read this as a substrate-witness decomposition:
   110	a $65.4$ percentage-point accuracy floor persists under the
   111	architecture-only permutation null (it survives random
   112	feature$\to$frame reassignment; the architecture is acting on whatever
   113	input lands in the frames), with the remaining $\sim 17$pp accruing
   114	to canonical alignment. We do not claim this decomposition is
   115	unique; it is a description of the observed accuracy stack.
   116	
   117	\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
   118	
   119	\textbf{Setup.} $64$ utterances across $8$ dialogue-act categories.
   120	$8$-dimensional injection-row features per utterance. Identical
   121	substrate routing pipeline to chess.
   122	
   123	\begin{table}[ht]
   124	\centering
   125	\small
   126	\caption{Conversation preregistered tests.}
   127	\label{tab:conv_prereg}
   128	\begin{tabular}{l l l l l}
   129	\toprule
   130	ID & Test & Threshold & Observed & Verdict \\
   131	\midrule
   132	P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
   133	P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   134	P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
   135	\bottomrule
   136	\end{tabular}
   137	\end{table}
   138	
   139	\textbf{Reading.} Conversation raw features at $87.5\%$ are already
   140	strongly discriminative (cf.\ chess raw $\sim 53\%$); the substrate
   141	lift is $-4.4$pp, well within the preregistered neutrality band
   142	$|\cdot|\!<\!10$pp. The substrate is approximately neutral on conversation.
   143	
   144	\textbf{Selective amplifier signature.} The pair (chess
   145	$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
   146	selective-amplifier behaviour preregistered in 2026-04-18: in these
   147	two tasks, the architecture amplifies when raw features are ambiguous
   148	(chess raw $\sim 53\%$) and is approximately neutral when raw features
   149	are already saturated (conversation raw $87.5\%$). We do not claim
   150	this generalises to all classification tasks; cross-domain transfer
   151	to additional ambiguous-feature benchmarks is an open build
   152	(\S\ref{sec:limitations}).
   153	
   154	\subsection{HCP brain-graph H$_4$-transitive null
   155	            (P17--P18)}\label{ssec:hcp}
   156	
   157	\textbf{Setup.} Reference cohort: Human Connectome Project (HCP)
   158	$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
   159	$n=100$ subjects for computational tractability, with full-cohort
   160	$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
   161	connectivity matrix; thresholded at the same density as ARIA's
   162	vertex graph ($\rho=0.101$). Compare degree distribution and
   163	higher-order graph statistics. ARIA reference: $G_{V_{600}}$ with
   164	$\Lop$. By H$_4$ transitivity (\S\ref{ssec:graph}) every vertex
   165	has identical local structure $\Rightarrow$ uniform degree $12$
   166	$\Rightarrow$ degree std $= 0$ as a theorem.
   167	
   168	\begin{table}[ht]
   169	\centering
   170	\small
   171	\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
   172	$n=1003$ descriptive statistics.}
   173	\label{tab:hcp}
   174	\begin{tabular}{l r r r}
   175	\toprule
   176	Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
   177	\midrule
   178	Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
   179	Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
   180	Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
   181	Clustering coefficient (descriptive)$^{\flat}$ & $0.455$ & $0.220$ & $+6.80\sigma$ \\
   182	\bottomrule
   183	\end{tabular}
   184	\end{table}
   185	
   186	\noindent$^{\flat}$ The HCP across-subject standard deviation for the
   187	clustering coefficient is not separately reported in
   188	\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
   189	from the same descriptive analysis as the other rows. Inferred from
   190	the reported gap and $\sigma$, the implicit HCP sd is
   191	$\approx 0.235/6.80\!\approx\!0.035$. We carry the $\sigma$-distance
   192	forward as reported and flag the missing explicit sd here.
   193	
   194	\begin{itemize}\itemsep=2pt
   195	\item P17 (ARIA degree std, theorem): predicted $=0$, observed
   196	  $0.0000$, $\checkmark$.
   197	\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
   198	  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
   199	  HCP subjects have degree std below $2.0$.
   200	\end{itemize}
   201	
   202	\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
   203	structure is a deterministic group-theoretic null reference for
   204	cortical functional connectivity. Real cortex breaks the symmetry
   205	through hub-spoke functional specialisation; the $\sigma$-distances
   206	quantify the magnitude of biological symmetry-breaking with no
   207	fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
   208	homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
   209	clustering coefficient) are large on the ICA-50 pipeline at the
   210	density-matched threshold $\rho = 0.101$; cross-parcellation
   211	replication (Schaefer, Glasser) remains an open build.
   212	
   213	\textbf{Participation-ratio comparability.} ARIA's vertex graph has
   214	$120$ nodes; the HCP ICA-50 connectivity matrix has $50$ nodes. The
   215	participation-ratio statistic
   216	$\mathrm{PR}(G) = (\sum_{i} d_{i})^{2} / \sum_{i} d_{i}^{2}$ is
   217	node-count-dependent — its theoretical maximum is the node count of
   218	the graph. We report the raw $\mathrm{PR}$ values
   219	($\mathrm{ARIA}=68.54$ on a 120-node graph; $\mathrm{HCP}=19.72$ on a
   220	50-node graph) and the $\sigma$-distance against the HCP
   221	across-subject distribution, but the $+79.78\sigma$ value reflects
   222	both the architectural difference and the differing node counts. A
   223	node-count-normalised statistic
   224	$\mathrm{PR}/|V|$ gives $\mathrm{ARIA}=0.571$ vs $\mathrm{HCP}=0.394$,
   225	a smaller absolute gap; we keep the raw-PR comparison as headline
   226	because the HCP subject distribution and the across-subject
   227	$\sigma$ are computed in the same units, but flag the node-count
   228	caveat here.
   229	
   230	\textbf{What we do not claim.}
   231	\begin{itemize}\itemsep=2pt
   232	\item We do not claim cortex has ``drifted from an ideal polytope'';
   233	  the substrate is a useful a-priori null whose deviation from real
   234	  cortex is precisely measurable.
   235	\item We do not claim parcellation invariance: the $\sigma$-distances
   236	  are reported on ICA-50; alternative parcellations (Schaefer,
   237	  Glasser) would give different per-metric numbers but, on the
   238	  basis of the qualitative pattern that cortex is hub-concentrated
   239	  relative to ARIA's transitive null, we expect them to preserve the
   240	  signs. Verification across parcellations is an open build
   241	  (\S\ref{sec:limitations}).
   242	\end{itemize}
   243	
   244	\subsection{Cross-domain summary as a selective amplifier
   245	            \texorpdfstring{$+$}{+} H$_4$-transitive null}
   246	
   247	\begin{table}[ht]
   248	\centering
   249	\small
   250	\caption{Cross-domain summary on a single substrate.}
   251	\label{tab:cross_domain_summary}
   252	\begin{tabular}{l r r r r r}
   253	\toprule
   254	Task & Raw & Substrate & Null perm. & Geom.\ floor & Sem.\ alignment \\
   255	\midrule
   256	Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
   257	Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\
   258	Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (substrate vs null) \\
   259	\bottomrule
   260	\end{tabular}
   261	\end{table}
   262	
   263	The geometric content ($\approx 65$--$71\%$ across the two domains)
   264	is the architecture-invariant null floor. The semantic content
   265	($12$--$18$pp) is the domain-specific contribution. On HCP,
   266	$\sigma$-distances against the biological cohort are
   267	$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
   268	clustering coefficient).
   269	
   270	\textbf{Headline cross-domain reading.} The substrate is
   271	\emph{selectively} amplifying (not unconditionally), and it is an
   272	H$_4$-transitive deterministic null on connectivity (not a fitted
   273	model). Both readings sit inside the substrate-witness scope.

codex
The manuscript has largely adopted the round-5 corrections, especially on preregistration disclosure, finite bootstrap wording, and HCP caveats. I’m now reading discussion, limitations, conclusion, and references to catch any remaining selection-theorem or uniqueness drift.
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 258ms:
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

 succeeded in 266ms:
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
    11	the substrate is chosen, its graph structure ($120$ vertices, uniform
    12	degree $12$ on the canonical short-edge nearest-neighbour graph, with
    13	the Laplacian spectrum reported in~\S\ref{ssec:graph} as observed) is
    14	fixed; only one condition-dependent self-injection coupling
    15	$\eta\in\{0, 0.05, 0.20\}$ and one substrate-pinned nonlinearity
    16	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
    17	degree enter the recurrent layer above the substrate. No shape
    18	parameter is tuned to any neural dataset.
    19	
    20	\textbf{Headline tally.} On a single deterministic trajectory, six
    21	drug/sleep EEG signatures pass against their literature-derived
    22	thresholds (Sleep-EDFx CI, OpenNeuro \texttt{ds005620}, Brodbeck 2012,
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
    55	contribute $N\!\approx\!20$ as a planning scale for this cascade
    56	matrix, recommended as a preregistration-practice consideration for
    57	similar high-variance ablation matrices.
    58	
    59	\textbf{Cross-domain selectivity.} The substrate exhibits selective
    60	amplification on the two tasks tested: chess 4-category position
    61	classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
    62	canonical depth $n\!=\!25$ ticks (raw $53.1\%$ $\to$ substrate-routed
    63	$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
    64	$5$-fold CV — the LOO finding above is a disclosed estimator/protocol
    65	refinement at the same threshold), while
    66	conversation utterance classification at raw $87.5\%$ lifts $-4.4$pp
    67	(threshold $|\cdot|\!<\!10$pp) — and as an H$_4$-transitive
    68	deterministic null reference for cortical functional connectivity:
    69	on the full-cohort descriptive HCP $n\!=\!1003$ statistics
    70	(preregistered test on the $n\!=\!100$ subset), ARIA's H$_4$-transitive
    71	structure is at $-11.58\sigma$ on degree homogeneity,
    72	$+79.78\sigma$ on participation ratio (with the node-count caveat of
    73	\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
    74	
    75	\textbf{Substrate-witness scope.} This is a substrate witness, not a
    76	derivation of consciousness, not a selection theorem on the
    77	companion adaptive-closure-transport
    78	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
    79	uniqueness claim for the 600-cell among regular 4-polytopes. The
    80	strengthening builds — cross-seed CIs on the recurrent-layer
    81	signatures, alternative-polytope ablations, an independent $N\!=\!20$
    82	C$\times$P replication at a different seed range, cross-parcellation
    83	HCP replication, a Lyapunov function on the reduced flow,
    84	$2I$-equivariance audit of the closure operator family — are
    85	explicitly listed in~\S\ref{sec:limitations} and remain open.
    86	
    87	We are not aware of a prior deterministic geometric architecture
    88	tested against this many preregistered cortical correspondences from
    89	a graph fixed by the construction with no shape parameters tuned to
    90	neural data; we cannot rule out that such prior work exists. The empirical material
    91	gathered here is the substrate witness; the broader programme to
    92	turn the witness into a selection-theorem-grade claim — including the
    93	independent passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$
    94	flavour anomaly~\citep{SmartBAnomaly2026} on the same response
    95	operator $\Cph$ — is sketched in the companion preprints and remains
    96	the natural next step.

 succeeded in 287ms:
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
    19	  data.} Once the 600-cell is chosen as the substrate, its graph
    20	  ($120$ vertices, uniform degree $12$ on the canonical short-edge
    21	  nearest-neighbour graph) and the response operator
    22	  $\Cph = \Lop + \Ph^{-2} I$ are fixed by the construction (no
    23	  shape parameter is tuned to neural data); cascade-$\alpha$ matches
    24	  Sleep-EDFx within preregistered tolerance with pairwise CI overlap
    25	  on three reference ranges; six drug/sleep signatures pass at
    26	  literature-derived thresholds on a single deterministic substrate.
    27	  We are not aware of a prior geometric substrate that has been tested
    28	  against this many preregistered cortical correspondences from a
    29	  graph fixed by the construction with no neural-data-fitted shape
    30	  parameters; we cannot rule out that such a model exists.
    31	\item \textbf{The strong-coupling architectural finding.} $C$ and $P$
    32	  are strongly coupled cascade-state stabilisers, not
    33	  nearly-orthogonal ones. The $C\!\times\!P$ interaction
    34	  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
    35	  in magnitude to the $P$ main effect ($-0.218$). This was hidden by
    36	  underpowered ablation and emerged only at $N\!\geq\!20$ — a
    37	  substantive correction to the architectural reading from the
    38	  original 3-seed validation.
    39	\item \textbf{The 18/18 preregistered correspondences with no
    40	  threshold modification.} Every prediction in the preregistered set
    41	  passes at the preregistered thresholds. The two interaction tests
    42	  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
    43	  one test (P13) required the documented state-reset protocol. We
    44	  report this transparently as methodology refinement, not as
    45	  threshold change.
    46	\end{enumerate}
    47	
    48	\subsection{Comparison to existing theories of consciousness}
    49	
    50	\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
    51	IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
    52	wake). The $\Phi$ proxy (\S\ref{sec:chain}) is designed to be small
    53	under H$_4$-equivariant dynamics and to increase when dynamics
    54	produce cross-class asymmetries. ARIA does not implement the full
    55	IIT axioms (cause-effect repertoires, exclusion postulate,
    56	integration-over-partitions); it reproduces an observable consequence
    57	on the propofol--wake state contrast. This is a consistency-of-direction
    58	result, not a discharge of IIT.
    59	
    60	\textbf{vs Global Workspace Theory.}~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
    61	The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
    62	functionally analogous to a workspace with rotating attentional
    63	selection; the active observer frame plays the role of a temporary
    64	in-workspace subset of features. ARIA does not commit to the GWT
    65	broadcast/access distinction at the architectural level; the
    66	analogy is descriptive.
    67	
    68	\textbf{vs Predictive Processing.}~\citep{FristonFreeEnergy2010,ClarkPP2013}
    69	ARIA does not implement prediction-error minimisation or hierarchical
    70	generative models.
    71	The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
    72	modulation of the substrate response by cosine direction alignment
    73	with the prior phenomenal snapshot, not by learned prediction errors.
    74	Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
    75	learning rate over a prediction-error norm) are an open build, not
    76	delivered here.
    77	
    78	\textbf{vs neural mass models.} ARIA operates at the
    79	architectural-algorithmic level; it does not specify which neural
    80	circuits implement context rotation or partial emission. The 600-cell
    81	substrate is proposed as an abstract description of the criticality-
    82	maintaining structure of cortex, not as a circuit model.
    83	
    84	\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
    85	
    86	The companion adaptive-closure-transport
    87	preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
    88	4-tuple bridge
    89	$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
    90	$L_{M}$, learnable Hebbian-like field $W$, and a homeostatic
    91	regulariser $R_{\mathrm{hom}}$. We propose the dictionary
    92	$D_{\mathrm{ACT}}$:
    93	\[
    94	D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
    95	\;\longmapsto\;
    96	(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
    97	   \ \texttt{homeostatic\_reset}).
    98	\]
    99	\textbf{This bridge is non-load-bearing for the present paper.} It is
   100	included as a route-K (alternative-route) reading; the substrate-
   101	witness claims (six signatures, $18/18$, chess $+40.6$pp,
   102	HCP $\sigma$-distances) do not require any of the ACT theorems.
   103	
   104	\textbf{What ACT would have to deliver to make this load-bearing.}
   105	The companion preprint identifies four open builds, each of which is
   106	deferred:
   107	\begin{itemize}\itemsep=2pt
   108	\item A Lyapunov function $V(W)$ on the reduced flow whose
   109	  monotonicity proves selection — not delivered.
   110	\item An edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   111	  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
   112	  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
   113	\item A formal $2I$-equivariance audit of the closure operator
   114	  family — not delivered.
   115	\item A full reduced-flow convergence theorem on
   116	  $W$-trajectories — not delivered.
   117	\end{itemize}
   118	Until these are delivered, ARIA is positioned as the empirical
   119	\emph{substrate witness} for the family that ACT names; ACT is not the
   120	selection-theorem witness for ARIA. The companion kernel
   121	document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
   122	in a passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$ flavour
   123	anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
   124	infrastructure with this paper, but does not transfer empirical
   125	support for ARIA.
   126	
   127	\subsection{The strong-coupling reading for cortical architecture}
   128	
   129	Real cortical criticality is maintained by multiple parallel
   130	mechanisms: E/I balance, neuromodulation (acetylcholine, noradrenaline),
   131	homeostatic plasticity, gain control. The naive expectation — and the
   132	one we held until the $N\!=\!20$ deep-dive — is that these are mostly
   133	orthogonal, so losing one removes only its own main effect. The
   134	$N\!=\!20$ result reverses this on the substrate: $C$ and $P$ are
   135	strongly coupled. Disabling one cascades into losing the synergistic
   136	contribution of the other.
   137	
   138	This matches clinical observations: anaesthesia (which targets
   139	GABAergic transmission) and seizure (which targets E/I balance)
   140	produce widespread network-level dysfunction beyond their direct
   141	targets — qualitatively consistent with a strong-coupling hypothesis. We position this as
   142	\emph{a hypothesis the substrate witness raises}, not as a proof.
   143	The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
   144	real-cortex pharmacological coupling is a step we do not take in
   145	this paper.
   146	
   147	\subsection{Methodological contributions}
   148	
   149	Two methodological items are worth recording outside the headline:
   150	\begin{enumerate}\itemsep=2pt
   151	\item \textbf{$N\!\geq\!20$ for similar high-variance ablation matrices.}
   152	  Allocation discipline for preregistration: in this cascade-ablation
   153	  matrix specifically, P4 ($C\!\times\!P$) required $N\!=\!20$ for
   154	  reliable detection at the preregistered threshold. The general
   155	  rule we draw — when preregistering an interaction effect on a
   156	  system with unknown per-seed variance, budget for at least this
   157	  scale — should be tested against other ablation matrices, not
   158	  taken as universal. The original 3-seed plan was the source of two
   159	  underpowered-interaction estimates in this work.
   160	\item \textbf{State-reset protocol on non-stationary substrates.}
   161	  ARIA's substrate is a non-stationary dynamical system; the
   162	  pressure field equilibrates within $\sim 5$ successive evaluations.
   163	  Any multi-trial benchmark must specify a state-reset protocol or
   164	  document the drift. Generalisable lesson: \emph{published
   165	  cross-domain benchmarks on non-stationary substrates should report
   166	  an explicit reset/equilibration discipline}, not just seed.
   167	\end{enumerate}
   168	
   169	\subsection{The substrate as an H$_4$-transitive connectivity null}
   170	
   171	The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
   172	deterministic null reference for cortical functional connectivity.
   173	Real cortex breaks the symmetry through hub-spoke functional
   174	specialisation; the $\sigma$-distances from ARIA quantify the
   175	magnitude of biological symmetry-breaking with no fitted parameters.
   176	
   177	This is a methodological contribution to comparative connectomics.
   178	Stochastic nulls (Erd\H{o}s--R\'enyi, configuration model,
   179	edge-randomised graphs) compare cortex to a random graph with matched
   180	density. ARIA is a different kind of null: a deterministic
   181	group-theoretic graph with structure-level statements: degree std
   182	$=\!0$ by H$_4$ transitivity, and a fully-determined Laplacian
   183	spectrum (\S\ref{ssec:graph}) computed from the constructed graph.
   184	Both null kinds are useful; ARIA gives a specific, reproducible,
   185	group-theoretic baseline that cortex deviates from in quantifiable
   186	$\sigma$-units.
   187	
   188	\subsection{Open questions raised by the substrate witness}
   189	
   190	\begin{itemize}\itemsep=2pt
   191	\item Do the six drug/sleep signatures replicate across $10$--$20$
   192	  cross-seed runs of the recurrent layer? (Single-seed disclosure;
   193	  see \S\ref{sec:limitations}.)
   194	\item Do alternative regular 4-polytopes ($24$-cell, $120$-cell)
   195	  reproduce comparable signature sets, or is the $600$-cell
   196	  distinguished?
   197	\item Does the strong-coupling reading ($C\!\times\!P$) survive an
   198	  independent fresh-seed $N\!=\!20$ replication at a different seed
   199	  range?
   200	\item Does the substrate's amplifier behaviour transfer to other
   201	  ambiguous-feature classification tasks beyond chess (e.g.\ visual
   202	  pattern, audio classification)?
   203	\item Does the Sleep-EDFx three-way CI overlap survive on a different
   204	  EEG cohort (TUH, NHM)?
   205	\end{itemize}
   206	We list these as open questions raised by the witness, not as gaps
   207	in the witness itself.

 succeeded in 277ms:
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
   123	$N\!=\!20$. We document this transparently as consistent with
   124	underpowered interaction estimates on high-per-seed-variance terms,
   125	not a threshold change. \emph{Disclosure:}
   126	\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
   127	\emph{Evidence:} bootstrap CI fully above the $+0.10$ floor; per-seed
   128	distribution narrow at $N\!=\!20$ ($\mathrm{std}=0.089$);
   129	$19/20$ seeds positive. \emph{Strengthening build:} a second
   130	$N\!=\!20$ run at a different seed range (e.g.\ $33000$--$33019$);
   131	an $N\!=\!50$ characterisation of the per-seed distribution.
   132	
   133	\textbf{The original 2026-04-20 walks-back are reversed without
   134	threshold modification.} The reversals (P3, P4, P13) are documented
   135	in
   136	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md} with
   137	the original failure values, the methodology refinement, and the
   138	post-refinement values. \emph{Disclosure:} this paper carries those
   139	disclosures verbatim. \emph{Evidence:} 2026-04-20 vs 2026-04-29 side-
   140	by-side results table. \emph{Strengthening build:} the strengthening
   141	builds for P3/P4/P13 above; no further claim is needed.
   142	
   143	\textbf{Bayesian and full-IIT inference not performed.} All intervals
   144	are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
   145	proxy, not the Balduzzi--Tononi 2008 algorithm. \emph{Disclosure:}
   146	this section. \emph{Strengthening build:} Bayesian posterior on
   147	$\Delta_{CP}$; full-IIT computation on the substrate's $S^{3}$
   148	state space. The latter is computationally heavy and is
   149	deferred.
   150	
   151	\subsection{State-drift / out-of-scope}\label{ssec:scope}
   152	
   153	\textbf{Single condition-dependent parameter $\eta$ is not derived
   154	as a learned variable.} $\eta\in\{0, 0.05, 0.20\}$ across PROPOFOL,
   155	SLEEP\_N3, and WAKE/RECOVERY is a condition-dependent constant in
   156	this paper, not a learned trajectory. A predictive-processing
   157	extension where $\eta$ adapts on an error norm is an open build.
   158	
   159	\textbf{No deuteron / hadron / RH / capstone material is loaded into
   160	this paper.} The companion programme (cascade-derivation, capstone
   161	coalgebra, RH formal) shares operator-level infrastructure but is not
   162	load-bearing here. Deliberately out of scope.
   163	
   164	\textbf{Out-of-scope items NOT delivered (correctly).}
   165	\begin{itemize}\itemsep=2pt
   166	\item Aria-chess active-regime companion analysis on chess move-by-move
   167	  trajectories (this paper covers static positions only).
   168	\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under
   169	  $2I$-equivariance — open build of the ACT companion paper.
   170	\item Lyapunov derivation $V(W)$ from a closure functional
   171	  $\mathcal{F}$ — open build of the ACT companion paper.
   172	\item Selection theorem for $\Rsixhundred$ over alternative regular
   173	  4-polytopes — see~\S\ref{ssec:regime}.
   174	\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
   175	  of the six signatures.
   176	\item Cross-parcellation replication of the HCP $\sigma$-distances
   177	  (Schaefer, Glasser, etc.).
   178	\item Bayesian posterior on the C$\times$P interaction.
   179	\item Verification of P10 (chess null mapping) at the preregistered
   180	  $20$-permutation count (the 2026-04-29 validation used $15$
   181	  permutations; threshold $\geq 50\%$ unchanged; result $65.4\%$
   182	  robust in the $15$--$20$ range, but the prereg-exact rerun is open).
   183	\end{itemize}
   184	
   185	\subsection{The honest verdict}
   186	
   187	The result is a substrate witness: a geometry-fixed substrate, with
   188	no shape parameters tuned to any neural dataset, is consistent with
   189	eighteen preregistered correspondences and six companion drug/sleep
   190	EEG signatures, with all original gaps closed by methodology
   191	refinement and without modifying any preregistered threshold. We do
   192	not claim the substrate \emph{is} consciousness. We do not claim a
   193	selection theorem on the ACT bridge. We do not claim uniqueness for
   194	$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
   195	for these stronger claims are listed above and remain open.

exec
/bin/bash -lc 'wc -l "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"6/6|18/18|0/2000|0\\.190|0\\.143|0\\.239|40\\.6|n=25|11\\.58|79\\.78|6\\.80|1\\.83|2\\.96|1003|preregister|threshold|permutation|20\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 201ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md:3:**Date**: 2026-04-20
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md:206:5. ⏳ Re-run preregistered validation with proper reset — convert
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md:216:- **SOC neural avalanches** (Beggs & Plenz 2003)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md:217:- **Entropic brain hypothesis** (Carhart-Harris 2014)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md:219:- **Synaptic homeostasis / sleep** (Tononi 2003)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:3:**Frozen: 2026-04-18** — predictions below were locked before running
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:10:- a **pass threshold** (interval, inequality, or categorical match)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:22:  of 200 epochs each will satisfy **2.5 ≤ α ≤ 3.5**.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:23:- **Rationale**: Beggs & Plenz 2003 put biological neuronal avalanches
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:36:- **Claim**: |D×C interaction| < **0.20** on the fresh 2x2 sub-matrix
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:89:- **Claim**: 5-fold CV on v2 features at n=25 ticks, 5 fresh seeds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:90:  (30200-30204), mean ≥ **70%**.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:96:- **Claim**: Mean accuracy over 20 random permutations (fresh RNG
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:116:- **Claim**: At n=25, substrate ≥ raw **+ 15pp** on 5-fold CV (fresh
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:128:  seeds (30220-30224).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:141:- **Claim**: Null feature→frame permutation mean ≥ **50%** on BOTH
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:144:- **Run**: Null-permutation controls on both domains.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:160:  density-matched threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:184:## Success thresholds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md:192:We do not expect 18/18 — some are noisy empirical tests and statistical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:1:# Preregistered Validation — Results (2026-04-29 update)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:3:*This document supersedes `VALIDATION_RESULTS.md` (2026-04-20, 15/18).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:4:It records the most recent run of the preregistered validation harness
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:5:plus the N=20 deep-dive on the residual P4 prediction.*
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:8:> 18 / 18 with N=20 deep-dive on the residual P4.** Original 15/18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:13:> measurements for chess LOO, and (c) N=20 fresh-seed replication of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:15:> set is fully validated against preregistered thresholds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:23:Eighteen quantitative predictions were frozen on **2026-04-18** in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:25:Each prediction has a falsifiable threshold (numerical band or
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:27:`run_preregistered_validation.py` — git-tracked, deterministic given
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:35:### 1.2 The original 2026-04-20 result
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:37:The original validation run on 2026-04-20 reported **15/18 passes**:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:44:    outside |·| < 0.20 band.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:55:### 1.3 What changed for the 2026-04-29 re-run
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:60:   in `run_preregistered_validation.py`. The original 3 seeds was
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:69:3. **N=20 deep-dive** on the residual P4 (`demo_p4_cxp_deep_dive.py`):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:70:   ran the C×P interaction test at 20 fresh seeds (32000–32019) with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:78:## 2. Full results table — 2026-04-29 run
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:80:| ID | Claim | Threshold | 2026-04-20 (3-seed) | **2026-04-29 (5-seed + reset + N=20 P4)** | Verdict |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:82:| P1 | Cascade α ∈ [2.5, 3.5] | ∈ [2.5, 3.5] | 3.020 ✅ | **2.958** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:84:| P3 | \|D×C interaction\| (independence) | \|·\| < 0.20 | −0.231 ❌ | **−0.183** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:85:| P4 | C×P synergy | ≥ +0.10 | +0.044 ❌ | **+0.190 at N=20, CI [+0.143, +0.239]** | ✅ at N=20 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:93:| P12 | Chess goldilocks peak | ∈ {15, 25, 40, 60} | n=15 ✅ | **n=25** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:94:| P13 | Chess LOO substrate lift | ≥ +15pp (with reset) | +3.1pp ❌ | **+40.6pp** | ✅ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:107:**Threshold:** \|D×C interaction\| < 0.20.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:113:**2026-04-29 re-run (N=5):** −0.183. Now inside the independence band.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:116:seeds tightens the estimate enough to land inside the threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:120:interaction estimate is approximately 0.06–0.10; the threshold is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:121:±0.20; and a single bad-luck draw at N=3 can put the point estimate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:122:just outside. With 5 seeds (and clearer at 20+) the estimate stabilises.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:125:cascade-α" is **supported** by the N=5 re-run within the preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:126:threshold. We do not claim point-zero independence (the estimate is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:128:the |·| < 0.20 band by direct measurement.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:137:**Original (N=3) failure:** +0.044. Below threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:139:**2026-04-29 re-run (N=5):** +0.039. Still below threshold — confirming
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:142:**N=20 fresh-seed deep-dive (`demo_p4_cxp_deep_dive.py`, seeds 32000–32019):**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:145:C×P bootstrap mean:           +0.190
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:146:C×P 95% bootstrap CI:         [+0.143, +0.239]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:151:The 95% CI is **entirely above the preregistered +0.10 threshold**.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:155:(per-seed std = 0.089 at N=20).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:165:**Threshold:** ≥ +15pp lift (substrate vs raw on LOO at n=25 ticks).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:167:**Original (N=1) failure:** +3.1pp. Far below threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:169:**2026-04-29 re-run (with `homeostatic_reset(level=1.0)` between depth
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:170:measurements):** **+40.6pp**.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:176:  n=25:   93.8%   ← peak (P12 goldilocks)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:181:Lift at n=25 = 93.8% − 53.1% = +40.6pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:187:40, 60, 100) without reset, so by the time it reached n=25 the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:205:across the original and 2026-04-29 runs.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:209:- **P1**: Baseline α at 5 seeds = 2.958 (vs original 3.020 at 3 seeds).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:212:  at 3 seeds). Both above the +0.30 dominance threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:227:- **P9**: Chess 5-fold CV at fresh seeds (30200–30204) = 83.1%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:229:- **P10**: Null feature→frame permutation (15 trials) = 65.4%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:230:  (≥ 50%). The substrate is partially permutation-invariant — ~65%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:233:- **P11**: Random-label baseline (20 trials) = 23.4% (∈ [15%, 35%]).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:235:- **P12**: Goldilocks peak depth = n=25 (∈ {15, 25, 40, 60}). With
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:236:  reset between measurements, n=25 is the global maximum at 93.8%.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:237:- **P13**: LOO substrate lift at n=25 = **+40.6pp** with reset
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:256:  matched threshold). > 2.0 confirms small-world hub-spoke structure
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:258:  symmetry-breaking is +79.78σ on participation ratio against ARIA.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:262:## 5. The 18/18 verdict
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:265:**Including the N=20 deep-dive:** 18/18 (P4 passes decisively at N=20).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:267:The empirical tally is **18/18 at adequate replication**. Two of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:270:closes only with adequate N (≥20), and its closure is the most
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:275:All eighteen preregistered predictions are **supported by the data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:276:within preregistered thresholds**, with the methodological caveat
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:277:that two interaction tests (P3, P4) require N ≥ 5 and N ≥ 20
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:286:> *"All eighteen preregistered predictions pass at empirical thresholds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:290:> (we used N=20 fresh seeds) due to the high per-seed variance of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:292:> (+0.190, 95% bootstrap CI [+0.143, +0.239]); the synergy is in fact
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:293:> ~90% above the preregistered floor, indicating C and P are strongly
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:301:The 2026-04-20 result included three honest walks-back. We now retract
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:302:each, because the 2026-04-29 evidence justifies retracting them:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:310:within the preregistered |·| < 0.20 band, confirmed at N=5.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:318:**Now reads:** C×P synergy is +0.190 [+0.143, +0.239] at N=20, ~90%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:319:above preregistered. C and P are strongly coupled cascade-state
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:332:is +40.6pp.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:338:The original validation methodology — 18 preregistered predictions
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:339:with falsifiable thresholds, frozen before any validation run — is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:340:the central protection of this work against p-hacking. The 2026-04-29
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:341:re-run with N improvements **did not modify any threshold or claim
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:343:reset. The fact that this gave 18/18 (with N=20 P4) where the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:355:adequate power. No threshold was loosened. No prediction was rewritten
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:366:python3 run_preregistered_validation.py
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:368:# P4 N=20 deep-dive (~28 min)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:372:JSON results are saved to `~/.aria/preregistered_validation/results_*.json`.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:373:Logs are at `/tmp/prereg_*.log` and `/tmp/p4_n20_*.log` for the most
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:384:- `docs/brain_mapping/PAPER_PREDICTIONS.md` — frozen 2026-04-18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:387:- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — standalone N=20 report
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:390:  drug/sleep EEG signatures (independent of preregistered set, on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:392:- `docs/brain_mapping/PAPER_BASIS_2026-04-29.md` — paper-basis
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:396:- `run_preregistered_validation.py` — validation harness
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:397:- `demo_p4_cxp_deep_dive.py` — N=20 deep-dive script
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:4:Compiled 2026-04-29. Self-contained for paper inclusion.*
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:8:> when raw features are ambiguous (chess: +40.6 percentage points on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:13:> transitivity); HCP n=1003 degree std = 3.28 ± 0.28; ARIA is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:14:> −11.58σ on degree homogeneity and +79.78σ on participation ratio,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:27:1. **Chess pattern recognition** (P9–P13 in the preregistered set):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:42:   the Human Connectome Project (n=1003 subjects, ICA-50
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:47:preregistered tests on chess + conversation pass at fresh seeds; both
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:88:**Result (fresh seeds 30200–30204):**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:97:threshold. Per-seed variance is small (range 81.2%–87.5%).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:105:**Threshold:** Random permutation of feature → frame assignment
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:108:**Method:** Apply random permutation σ to the 8 V2 features, so each
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:110:substrate, classify. Repeat 15 times with seeded random permutations
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:113:**Result:** 65.4% mean across 15 permutations.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:138:routed patterns, repeat 20 times with different seeds.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:140:**Result:** 23.4% mean across 20 trials.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:168:n=25, with a roll-off both at shallower depth (insufficient
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:181:(b) substrate-routed patterns at n=25, with reset between depth
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:188:Substrate-routed (n=25, with reset):   93.8%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:189:Lift:                                  +40.6 percentage points
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:195:the substrate's 600-cell graph. This is **+40.6pp of geometric
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:196:amplification**, far exceeding the +15pp prereg threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:198:The original 2026-04-20 validation reported this lift at +3.1pp — a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:202:lift is restored to +40.6pp. See `NON_EQUILIBRIUM_FINDING.md` for the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:208:- 53.1% raw → 93.8% substrate-routed at canonical depth (n=25)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:211:- Goldilocks optimum at n=25 ticks of substrate evolution
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:213:The +40.6pp lift is roughly an order of magnitude above the +15pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:214:preregistered floor. The 65.4% null mapping shows two-thirds of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:238:**Result (fresh seeds 30220–30224):** **87.5%** mean.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:254:Substrate 5-fold CV (n=25):  83.1%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:262:preregistered window, and the negative sign suggests minor noise
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:274:**Threshold:** Random permutation of feature → frame mapping
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:277:**Result:** 70.6% mean across 15 permutations.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:289:| Chess (LOO) | 53.1% | 93.8% | n/a | n/a | +40.6pp lift |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:301:substrate routing at 83.1% (lift −4.4pp) is within preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:302:neutrality bounds. The null permutation at 70.6% confirms geometric
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:311:**Reference cohort:** Human Connectome Project (HCP), n=1003 subjects.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:312:For preregistered tests, n=100 subjects (computational tractability)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:313:in ICA-50 parcellation. The full-cohort effects (n=1003) match the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:316:**Method:** Build group-averaged ICA-50 connectivity matrix; threshold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:347:**ARIA is at −11.58σ** below the HCP cohort mean on this metric:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:348:ARIA's degree std is 0; HCP n=1003 mean is 3.28 ± 0.28; the gap is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:349:(0 − 3.28) / 0.28 = −11.7σ. **Zero of 1003 HCP subjects** have
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:352:### 4.4 Higher-order graph statistics (full cohort, n=1003)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:358:Metric                 ARIA     HCP n=1003 mean   σ from HCP
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:360:Degree std             0.000    3.28 ± 0.28        −11.58σ
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:361:Participation ratio    68.54    19.72 ± 0.61       +79.78σ
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:362:Clustering coefficient 0.455    0.220              +6.80σ
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:371:  Real cortex is hub-concentrated; ARIA is uniform. +79.78σ.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:373:  ARIA at 0.455 vs HCP at 0.220 — ARIA has more local clustering
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:375:  +6.80σ.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:390:giving precise effect-size statements like "real cortex is +79.78σ
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:395:parcellation choice, density threshold, and subject inclusion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:418:ARIA's degree std = 0 (theorem); HCP n=1003 degree std = 3.28 ± 0.28,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:419:range [2.55, 4.16], with zero of 1003 subjects below 2.0. ARIA is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:420:−11.58σ on degree homogeneity, +79.78σ on participation ratio, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:421:+6.80σ on clustering coefficient. The substrate functions as a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:434:amplifies to 93.8% LOO (+40.6pp lift) and 83.1% 5-fold CV across fresh
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:436:floor (≈65–71% across domains, robust to feature → frame permutation)
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:497:- Chess fresh seeds: 30200–30204
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:498:- Chess null permutation: seeded from 30210
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:500:- Conversation fresh seeds: 30220–30224
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:509:JSON outputs land in `~/.aria/preregistered_validation/results_*.json`.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:537:   accuracy with random permutation). However, future work could
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:551:- `run_preregistered_validation.py` — full P1–P18 harness
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:565:- `docs/brain_mapping/PAPER_PREDICTIONS.md` — frozen 2026-04-18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:566:- `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` — full
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:567:  preregistered tally
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:580:- `project_chess_permutation_invariance.md` — null permutation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:583:- `project_preregistered_validation_17_of_18.md` — re-run summary
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:584:- `project_p4_cxp_underpowered_not_wrong.md` — N=20 deep-dive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:3:*Standalone publishable finding from N=20 seed deep-dive on the residual P4
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:4:preregistered prediction. Compiled 2026-04-29.*
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:8:> adequate replication (N ≥ 20 fresh seeds), their **interaction effect
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:9:> on cascade-α is +0.190, 95% bootstrap CI [+0.143, +0.239]** — comparable
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:11:> preregistered prediction of ≥+0.10. The original 3-seed preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:20:## 1. Background: what was preregistered, what failed at N=3
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:24:ARIA's substrate is the 600-cell regular 4-polytope (120 vertices,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:37:  threshold but not yet crossed) emit pressure at 30% scale, saturating
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:48:### 1.2 The preregistered predictions for D/C/P/E mechanisms
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:50:Predictions frozen 2026-04-18 in `docs/brain_mapping/PAPER_PREDICTIONS.md`:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:56:| **P3** | **\|D×C\| < 0.20** (independence) | \|·\| < 0.20 |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:63:contribution to cascade-α. The preregistered floor was +0.10 — stating
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:68:Original validation (2026-04-20, 3 seeds per condition):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:72:  ----  baseline:    α = 3.020
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:82:    = ((3.530 + 3.020) − (3.612 + 2.844)) / 2
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:87:This was below the +0.10 threshold, so P4 was reported as a **fail**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:94:N=20 deep-dive presented below shows this was wrong.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:98:## 2. The N=20 deep-dive (2026-04-29)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:104:- **N = 20 fresh seeds** (range 32000–32019, non-overlapping with prior
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:117:We then bootstrapped the interaction distribution (2000 resamples,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:118:seeded) over the 20-seed sample to get a 95% confidence interval, plus
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:125:### 2.2 Per-condition means at N=20
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:128:cond     mean α   std    sem    individual seeds (n=20)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:129:----     3.008   0.090  0.020   [2.905, 3.013, 3.005, 3.087, 3.136, 3.022, 3.075, 2.879, 2.880,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:143:### 2.3 Main-effect estimates at N=20
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:162:Bootstrap (2000 resamples) on the 20-seed sample gives:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:165:C×P bootstrap mean:           +0.190
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:166:C×P 95% bootstrap CI:         [+0.143, +0.239]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:171:**The 95% CI is entirely above the preregistered +0.10 threshold.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:183: +0.147, +0.221, +0.055, +0.182, +0.320, +0.098, +0.267, +0.322,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:186:mean = +0.190,  std = 0.089,  SEM = 0.020
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:189:19 of 20 seeds give a positive interaction; one is essentially zero
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:191:per-seed std at N=20 (0.089) is just under half the per-seed std at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:193:N=20 reveals a clean, narrow positive distribution.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:206:20   32000–32019      +0.190          [+0.143, +0.239]      ✅ DECISIVELY ABOVE
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:216:   were no other bias — already containing the threshold. But N=3 also
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:221:   then 32000–32019. The means at each seed range differ enough that
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:323:in the cascade ablation matrix require N ≥ 20 fresh seeds for reliable
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:334:### 5.3 The 18/18 verdict
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:337:this session. With the N=20 deep-dive, the synergy is decisively above
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:338:the preregistered floor. **Effectively, all eighteen preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:357:N_SEEDS = 20
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:359:BASE_SEED = 32000
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:368:**Verification:** seeds 32000–32019 should give the per-condition means
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:377:1. **One seed range tested at N=20.** A second N=20 run at a different
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:383:   well-powered N=20 estimate.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:387:   (e.g., pressure-threshold crossings) might give a slightly different
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:395:   (with one large positive outlier and two negatives) while N=20 has a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:404:The C×P interaction in ARIA's cascade ablation matrix was preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:408:walked back the claim. We now report a 20-seed deep-dive that gives
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:409:synergy = +0.190, 95% bootstrap CI [+0.143, +0.239], P(synergy ≤ 0) = 0,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:420:from the preregistered prediction set, taking the empirical tally from
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:421:17/18 to 18/18.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:427:- `demo_p4_cxp_deep_dive.py` — N=20 script (this work)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:430:- `run_preregistered_validation.py` — original cascade-block test
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:431:- `docs/brain_mapping/PAPER_PREDICTIONS.md` — frozen 2026-04-18
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:433:  (now superseded by `VALIDATION_RESULTS_2026-04-29.md`)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:434:- `docs/brain_mapping/PAPER_BASIS_2026-04-29.md` — paper-basis
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:8:*Report compiled 2026-04-29.*
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:15:recurrence on the 600-cell with bounded-top-K thresholding) plus
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:23:has a published reference and a falsifiable threshold; all six pass.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:26:stimulus-model artefacts in `demo_wake_alpha_diagnosis.py`) to 6/6 by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:32:| 1 | Sleep variance ratio | NREM-N3 EEG (Lee 2017, Jobst 2017) | ratio ≈ 0.365 | 0.463 | ✓ within 30% |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:33:| 2 | Propofol switching ↑ | OpenNeuro ds005620 (n=8, 2.96×) | ratio in [1.5, 5.0] | 1.83× | ✓ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:34:| 3 | Propofol continuity ↓ | EEG microstate (Brodbeck 2012) | drop > 0.020 | +0.066 | ✓ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:35:| 4 | Propofol Φ collapse | IIT prediction (Tononi 2008) | ratio < 0.5 | 0.33× | ✓ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:63:**The bounded_topk(k=12) thresholding is the load-bearing nonlinearity.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:65:α ≈ 1.09 (no avalanches). Adding bounded_topk(k=12) drives α to 3.20 with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:70:- η = 0.20 for WAKE, RECOVERY (active recurrent self-loop)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:79:amp_history  = state_history @ eigvecs              # (T, 120) mode amps
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:100:composite            = 0.35·binding + 0.25·valence + 0.20·modality + 0.20·smooth
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:115:(visual fixations dwell 200–400 ms, much longer than between-saccade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:121:    # AR(1) cortical noise (β=0.90) — temporal correlation lets η=0.20 self-loop integrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:126:    # Attention episodes — sustained salient bias, 20–50 ticks, anchored to ATTENTION_SHELL
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:128:        start episode(length=20–50, vertex=random pick from ATTENTION_SHELL)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:140:  tick (zero integration). Temporal correlation lets η=0.20 build coherent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:146:- **Attention episodes (20–50 ticks)** — sustained dwells, anchored to a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:195:All four conditions run for 800 ticks at seed = 42, k_threshold = 12.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:223:transitions ~3× over wake. Source: OpenNeuro ds005620 (n=8 propofol EEG,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:224:microstate switching ratio 2.96×).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:226:**Observed:** WAKE modality_switches → PROPOFOL modality_switches ratio = 1.83×.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:227:Falls within [1.5×, 5.0×] window. Below the empirical 2.96× point estimate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:238:modality + smoothness). Source: Brodbeck 2012 microstate literature
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:242:Drop = +0.066. Falls past the +0.020 minimum.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:244:**Mechanism:** WAKE's recurrent self-loop (η=0.20) plus AR(1) temporal
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:256:Ratio PROPOFOL/WAKE = 0.33×. Below the 0.50× threshold.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:260:both via η=0.20 self-loop integrating AR(1) input. PROPOFOL has neither
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:279:cortical-avalanche band [1.5, 3.5], R² > 0.85. Source: Beggs & Plenz 2003
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:293:**Mechanism:** The bounded_topk(k=12) thresholding is the critical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:313:| H4: k_threshold sweep | k=12 is the sweet spot |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:321:For η=0.20 self-coupling to manifest, the input needs temporal correlation
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
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:419:1.83×), propofol continuity disruption (passes at +0.066), propofol Φ collapse
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:422:AR(1) cortical noise plus tonic shell coherence plus 20–50-tick attention

 succeeded in 209ms:
  1253 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md
   426 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md
   435 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md
   584 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md
   399 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md
   194 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md
   257 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md
  3548 total

exec
/bin/bash -lc "rg -n \"P=0|P\\(|published references|published literature|thresholds are drawn from published|max(imum)?-symmetry|maximum symmetry|unique|uniqueness|selection theorem|Lyapunov|is consciousness|consciousness substrate|fixed by group theory|fully derivable|2I|600-cell is|cortex has|proves|proof|derivation of consciousness|methodology refinement|threshold change|0/2000|17/18|18/18|n=1003|n=100|79\\.78|6\\.80|11\\.58|40\\.6|27\\.2|15 perms|20 permutations|20 perms\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\[A-Za-z]+\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 1 in 239ms:
 succeeded in 277ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:65:and six EEG signatures. It is not a derivation of consciousness, nor a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:66:selection theorem, nor a uniqueness claim for the 600-cell among regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:81:preregistered tally is $17/18$ at standard validation methodology
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:82:($5$-seed cascade block plus state-reset protocol), and $18/18$ after
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:89:from the published literature (Sleep-EDFx CI for the wake $\alpha$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:122:(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:132:8-dimensional V2 features lifts $+40.6$ percentage points on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:146:$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:147:on degree homogeneity, $+79.78\sigma$ on raw participation ratio
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:150:both architectural and node-count differences), and $+6.80\sigma$ on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:155:We do not claim the 600-cell is the unique substrate consistent with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:166:the original preregistration closed by methodology refinement and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:66:  $17/18$ at standard methodology; $18/18$ after a documented
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:71:  (chess $+40.6$pp leave-one-out lift at depth $n\!=\!25$ ticks;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:75:  $n\!=\!1003$: ARIA at $-11.58\sigma$ on degree homogeneity;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:76:  $+79.78\sigma$ on raw participation ratio with the node-count caveat
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:83:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:84:  the unique substrate consistent with these signatures. Other regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:89:\item \emph{Not a derivation of consciousness.} The substrate witness
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:93:\item \emph{Not a selection theorem.} The companion adaptive-closure-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:98:  non-load-bearing here. We do not deliver a Lyapunov function on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:99:  reduced flow, nor a $2I$-equivariance audit of the closure operator,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:130:threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:131:$+15$pp floor) licenses `decisively above prereg', not `proves'. A
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:133:(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:134:the biological distribution', not `cortex has drifted from an ideal
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:146:\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:147:selection theorem on the 4-tuple bridge; circuit-level mechanistic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:168:ACT bridge (without claiming a selection theorem).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:99:\item $0/2000$ bootstrap resamples were at or below zero, reported as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:101:\item $0/2000$ bootstrap resamples were below the preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:113:threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:114:at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:143:\item It does not establish a Lyapunov function on the reduced flow.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:144:\item It does not establish that the substrate is uniquely selected by
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:50:$N\!=\!20$ ($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:61:classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:71:structure is at $-11.58\sigma$ on degree homogeneity,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:72:$+79.78\sigma$ on participation ratio (with the node-count caveat of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:73:\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:76:derivation of consciousness, not a selection theorem on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:79:uniqueness claim for the 600-cell among regular 4-polytopes. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:83:HCP replication, a Lyapunov function on the reduced flow,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:84:$2I$-equivariance audit of the closure operator family — are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:19:\emph{Disclosure:} substrate-witness scope, no uniqueness claim
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:64:derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:76:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:90:derive the $\Ph^{-2}$ shift as the unique stability clamp under a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:113:do not claim ``cortex has drifted from an ideal polytope''; we
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:125:not a threshold change. \emph{Disclosure:}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:137:the original failure values, the methodology refinement, and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:169:  $2I$-equivariance — open build of the ACT companion paper.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:170:\item Lyapunov derivation $V(W)$ from a closure functional
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:193:selection theorem on the ACT bridge. We do not claim uniqueness for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:45:\caption{Six drug/sleep signatures with published references.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:92:\textbf{Tally.} $17/18$ at standard validation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:94:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:120:\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:137:methodology refinement (no threshold change).}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:152:  without state reset on a state-drifted substrate, and $+40.6$pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:19:  data.} Once the 600-cell is chosen as the substrate, its graph
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:39:\item \textbf{The 18/18 preregistered correspondences with no
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:44:  report this transparently as methodology refinement, not as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:45:  threshold change.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:101:witness claims (six signatures, $18/18$, chess $+40.6$pp,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:108:\item A Lyapunov function $V(W)$ on the reduced flow whose
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:109:  monotonicity proves selection — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:113:\item A formal $2I$-equivariance audit of the closure operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:142:\emph{a hypothesis the substrate witness raises}, not as a proof.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:24:not include those batteries in the headline 18/18 tally.} They are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:111:matrix. The preregistered test (P18) was on $n=100$ subjects for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:112:computational tractability; full-cohort $n=1003$ statistics
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:145:deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:146:$0/2000$ were below the preregistered floor $+0.10$; we report these
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:147:as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:161:on the full $n=1003$ subject distribution.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:174:substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:66:P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:69:\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:82:a threshold change; the observed $65.4\%$ at $15$ perms sits well
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:90:reset; we report the LOO finding ($+40.6$pp) above as a disclosed
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:97:This is a $+40.6$pp lift on the LOO refinement; on the preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:115:unique; it is a description of the observed accuracy stack.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:134:P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:145:$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:158:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:159:$n=100$ subjects for computational tractability, with full-cohort
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:160:$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:171:\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:172:$n=1003$ descriptive statistics.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:176:Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:178:Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:179:Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:180:Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:181:Clustering coefficient (descriptive)$^{\flat}$ & $0.455$ & $0.220$ & $+6.80\sigma$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:188:\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:191:$\approx 0.235/6.80\!\approx\!0.035$. We carry the $\sigma$-distance
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:197:\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:207:fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:208:homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:221:across-subject distribution, but the $+79.78\sigma$ value reflects
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:232:\item We do not claim cortex has ``drifted from an ideal polytope'';
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:256:Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:267:$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,

codex
A few candidate issues are emerging, but I’m not finalizing them until I verify against the local source documents. The most important checks now are whether the tables match the source records verbatim and whether any “null floor” or “prior literature” phrasing has become stronger than the underlying evidence.
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md\" | sed -n '1,120p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md\" | sed -n '190,290p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md\" | sed -n '340,426p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md\" | sed -n '1,110p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 181ms:
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

 succeeded in 194ms:
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

 succeeded in 177ms:
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

 succeeded in 190ms:
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

exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md\" | sed -n '130,200p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md\" | sed -n '220,300p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md\" | sed -n '98,210p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md\" | sed -n '404,414p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 195ms:
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

 succeeded in 206ms:
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

 succeeded in 198ms:
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

 succeeded in 207ms:
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

exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md\" | sed -n '1,120p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md\" | sed -n '160,230p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md\" | sed -n '300,455p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md\" | sed -n '455,485p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 276ms:
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

 succeeded in 265ms:
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

 succeeded in 283ms:
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

 succeeded in 258ms:
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

exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md\" | sed -n '1,190p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md\" | sed -n '1,120p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md\" | sed -n '640,850p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md\" | sed -n '1000,1120p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 232ms:
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

 succeeded in 223ms:
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

 succeeded in 209ms:
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

 succeeded in 218ms:
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

exec
/bin/bash -lc "rg -n \"27\\.2|2\\.96\\\\"'!?'"\\\\times wake|2\\.96× wake|P=0|P\\(synergy|maximum-symmetry|maximum symmetry|consciousness substrate|the substrate is consciousness|fully derivable|selection-theorem witness|published-reference thresholds\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\Ph|\\\\Lop|\\\\Cph|\\\\Rsixhundred|\\\\varphi|C_\\\\varphi|L_\\{V_\\{600\\}\\}|V_\\{600\\}\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"TODO|FIXME|\\\\citep\\{["'^}]*'"\\}|\\\\ref\\{["'^}]*'"\\}|\\\\label\\{["'^}]*'"\\}|\\\\S\\\\ref\\{["'^}]*'"\\}\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 2 in 221ms:
rg: regex parse error:
    (?:\Ph|\Lop|\Cph|\Rsixhundred|\varphi|C_\varphi|L_\{V_\{600\}\}|V_\{600\})
           ^^
error: unrecognized escape sequence

 succeeded in 287ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:120:selection-theorem witness for ARIA. The companion kernel
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:147:as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:68:ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}

 exited 2 in 298ms:
rg: regex parse error:
    (?:TODO|FIXME|\citep\{[^}]*\}|\ref\{[^}]*\}|\label\{[^}]*\}|\S\ref\{[^}]*\})
                  ^^
error: unrecognized escape sequence

exec
/bin/bash -lc "rg -o '\\\\citep\\{["'^}]+'"\\}' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\" | sed 's/.*citep{//; s/}//' | tr ',' '\\n' | sed 's/"'^ *//; s/ *$//'"' | sort -u" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -o '"'^@[a-zA-Z]+'"\\{["'^,]+'"' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib\" | sed 's/"'^.*{//'"' | sort -u" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -o '\\\\label\\{["'^}]+'"\\}|\\\\ref\\{["'^}]+'"\\}' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F '\\Ph' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\" && rg -n -F '\\Lop' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\" && rg -n -F '\\Cph' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\" && rg -n -F '\\Rsixhundred' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 360ms:
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

 succeeded in 374ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:\ref{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:\ref{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:\ref{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:\ref{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:\label{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:\label{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:\ref{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:\ref{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:\ref{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\label{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{ssec:shells}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{ssec:cascade}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\label{ssec:vertices}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\label{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\label{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\label{eq:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\label{ssec:shells}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\label{ssec:cascade}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:\ref{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\label{sec:intro}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:stress}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:cross_domain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:discussion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:\ref{sec:conclusion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:\label{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:\ref{sec:substrate}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:\ref{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:\ref{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:\ref{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:\ref{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:\ref{sec:stress}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:\ref{sec:stress}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:\label{sec:conclusion}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:\ref{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:\ref{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:\ref{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:\label{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:\ref{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:\label{tab:provenance}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:\ref{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\label{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{ssec:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\label{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\label{tab:per_condition}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\label{tab:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{ssec:regime}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\label{ssec:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\label{tab:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{sec:cross_domain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{sec:stress}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\label{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\label{tab:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:\label{sec:stress}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:\label{tab:cxp_trend}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:\label{tab:cxp_means}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:\ref{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\label{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\label{ssec:regime}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{sec:intro}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\label{ssec:posthoc}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{sec:intro}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{ssec:cascade}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\label{ssec:interpretation}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{sec:intro}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{ssec:regime}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{sec:chain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\label{ssec:testclaim}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{sec:results}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{sec:stress}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\label{ssec:scope}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:\ref{ssec:regime}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\label{sec:cross_domain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\ref{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\ref{ssec:conv}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\ref{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\label{ssec:chess}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\label{tab:chess_depth}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\label{tab:chess_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\ref{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\ref{sec:method}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\label{ssec:conv}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\label{tab:conv_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\ref{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\label{ssec:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\ref{ssec:graph}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\label{tab:hcp}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\ref{sec:limitations}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:\label{tab:cross_domain_summary}

 succeeded in 403ms:
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

 succeeded in 577ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:14:\newcommand{\Ph}{\varphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:42:$\Ph=(1+\sqrt 5)/2$ entering through the canonical vertex coordinates
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:43:and through the response-operator stability shift $\Ph^{-2}$. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:47:response $\Cph = \Lop + \Ph^{-2} I$ and a small dynamical layer above
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:76:shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:91:switching, literature-direction predictions for $\Phi$ collapse,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:110:integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:157:have been ruled out. We do not derive the $\Ph^{-2}$ floor from
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:191:$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:22:\Phi_{\mathrm{traj}}, \mathrm{cont})$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:32:condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:60:4 & Propofol $\Phi$ collapse (IIT) &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:80:propofol switching, literature-direction predictions for $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:202:(\S\ref{ssec:graph}); the $\Ph^{-2}$ shift in $\Cph$ is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:27:operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:50:  $\Cph = \Lop + \Ph^{-2} I$ is fully fixed once the graph is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:51:  constructed and the stability shift $\Ph^{-2}$ is chosen as a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:62:  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:107:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:108:  Laplacian floor $\Ph^{-2} \approx 0.382$ is a design-level
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:148:identification; first-principles derivation of $\Ph^{-2}$ shift;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:158:$\Ph^{-2}$ shift disclosed as a design-level stability clamp.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:8:operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:18:With $\Ph = (1+\sqrt 5)/2$ the canonical vertex set is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:24:  $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:54:       (12\!-\!6\Ph)^{4},\;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:55:       (12\!-\!4\Ph)^{9},\;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:59:       (4\Ph + 8)^{9},\;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:61:       (6\Ph + 6)^{4}\bigr\},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:69:the closed-form entries here; the values in $\mathbb{Z}[\Ph]$ are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:76:of $\mathbb{Z}[\Ph]$ the exponents become $\{7, 13, 17, 23\}$. The
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:89:\Cph \;=\; \Lop + \Ph^{-2} I,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:93:The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:95:$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:96:inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:114:The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:134:collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:165:\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:22:  $\Cph = \Lop + \Ph^{-2} I$ are fixed by the construction (no
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:51:IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:52:wake). The $\Phi$ proxy (\S\ref{sec:chain}) is designed to be small
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:8:regime-switching, propofol $\Phi$ collapse — we add a recurrent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:64:            \texorpdfstring{$\Phi$}{Phi}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:74:\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:85:We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:88:machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:31:propofol $\Phi$ collapse, recovery reversibility, wake
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:7:$\Cph = \Lop + \Ph^{-2} I$ ($\Ph=(1+\sqrt 5)/2$), is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:26:$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:81:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:82:$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:90:derive the $\Ph^{-2}$ shift as the unique stability clamp under a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:105:\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:107:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:144:are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:15:\newcommand{\Lop}{L_{V_{600}}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:47:response $\Cph = \Lop + \Ph^{-2} I$ and a small dynamical layer above
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:76:shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:22:  $\Cph = \Lop + \Ph^{-2} I$ are fixed by the construction (no
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:164:$\Lop$. By H$_4$ transitivity (\S\ref{ssec:graph}) every vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:7:$\Cph = \Lop + \Ph^{-2} I$ ($\Ph=(1+\sqrt 5)/2$), is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:27:operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:50:  $\Cph = \Lop + \Ph^{-2} I$ is fully fixed once the graph is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:49:The unweighted graph Laplacian $\Lop = D - A$ has nine distinct
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:52:\sigma(\Lop) \;=\;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:89:\Cph \;=\; \Lop + \Ph^{-2} I,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:47:response $\Cph = \Lop + \Ph^{-2} I$ and a small dynamical layer above
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:76:shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:202:(\S\ref{ssec:graph}); the $\Ph^{-2}$ shift in $\Cph$ is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:22:  $\Cph = \Lop + \Ph^{-2} I$ are fixed by the construction (no
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:96:(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:121:document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:82:$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:8:operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:84:\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:89:\Cph \;=\; \Lop + \Ph^{-2} I,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:91:\psi \;=\; \Cph^{-1} f.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:94:clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:99:$\Cph$ as the basis for an independent passive-regime witness in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:103:This paper imports $\Cph$ from that line; we do not re-derive it.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:105:The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:133:$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:165:\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:7:$\Cph = \Lop + \Ph^{-2} I$ ($\Ph=(1+\sqrt 5)/2$), is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:95:operator $\Cph$ — is sketched in the companion preprints and remains
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:25:\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:34:prior snapshot). The substrate response operator $\Cph$ is unchanged
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:27:operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:50:  $\Cph = \Lop + \Ph^{-2} I$ is fully fixed once the graph is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:109:  stability clamp (it makes $\Cph$ strictly positive definite and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:157:constructs $\Rsixhundred$ and the response operator $\Cph$, with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:75:4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:5:The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:22:600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:26:candidate substrate for consciousness-linked signatures. We construct $\Rsixhundred$, fix its response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:42:\item \textbf{Substrate is fixed once chosen.} Once $\Rsixhundred$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:157:constructs $\Rsixhundred$ and the response operator $\Cph$, with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:96:(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:143:The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:16:The 600-cell $\Rsixhundred$ has $120$ vertices in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:155:cascade is a decomposition of operators on $\Rsixhundred$, and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:156:choice of $\Rsixhundred$ as the active substrate is post-hoc justified
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:162:\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:168:\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:21:on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:59:observables.} While the construction of $\Rsixhundred$ is theorem-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:172:\item Selection theorem for $\Rsixhundred$ over alternative regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:194:$\Rsixhundred$ among regular 4-polytopes. The strengthening builds

exec
/bin/bash -lc "rg -n \"\\\\begin\\{tabular\\}\\{["'^}]*'"\\}\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "comm -23 <(rg -o '\\\\ref\\{["'^}]+'"\\}' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\" | sed 's/.*ref{//;s/}//' | sort -u) <(rg -o '\\\\label\\{["'^}]+'"\\}' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\" | sed 's/.*label{//;s/}//' | sort -u)" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "[✓✅❌×→−–—σ≈φ⁻²Φη₄₃₇]" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 1 in 295ms:
 succeeded in 295ms:
 succeeded in 431ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:49:quantitative correspondences with neuroscience data — preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:50:on 2026-04-18 before any validation run — plus six drug/sleep EEG
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:74:We test whether a geometry-fixed substrate — the 600-cell regular
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:77:operator — is consistent with cortical signatures across five
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:101:pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:116:Two of four cascade mechanisms — context rotation $C$ and partial
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:117:emission $P$ — are causally identifiable within the factorial
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:36:  underpowered ablation and emerged only at $N\!\geq\!20$ — a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:89:$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:109:  monotonicity proves selection — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:112:  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:114:  family — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:116:  $W$-trajectories — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:131:homeostatic plasticity, gain control. The naive expectation — and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:132:one we held until the $N\!=\!20$ deep-dive — is that these are mostly
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:141:targets — qualitatively consistent with a strong-coupling hypothesis. We position this as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:155:  rule we draw — when preregistering an interaction effect on a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:157:  scale — should be tested against other ablation matrices, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:169:  $2I$-equivariance — open build of the ACT companion paper.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:171:  $\mathcal{F}$ — open build of the ACT companion paper.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:173:  4-polytopes — see~\S\ref{ssec:regime}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:8:wallclock — the minimal information a hostile reviewer needs to
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:20:\textbf{Frozen 2026-04-24.} Two later batteries — H$_4$ fingerprint
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:21:predictions and rung observables — were preregistered on 2026-04-24
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:47:mechanisms — context rotation $C$ and partial emission $P$ — are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:64:$5$-fold CV — the LOO finding above is a disclosed estimator/protocol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:67:(threshold $|\cdot|\!<\!10$pp) — and as an H$_4$-transitive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:80:strengthening builds — cross-seed CIs on the recurrent-layer
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:84:$2I$-equivariance audit of the closure operator family — are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:92:turn the witness into a selection-theorem-grade claim — including the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:95:operator $\Cph$ — is sketched in the companion preprints and remains
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:9:$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:54:$N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$ sample landed on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:108:permutation — well above the $25\%$ chance level for $4$ categories.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:217:node-count-dependent — its theoretical maximum is the node count of
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

exec
/bin/bash -lc "rg -n \"\\\\texttt\\{|_\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\checkmark|\\\\flat|\\\\mathsf|\\\\texorpdfstring|\\\\H\\{|Erd|\\\\text\\{\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 2 in 280ms:
rg: regex parse error:
    (?:\checkmark|\flat|\mathsf|\texorpdfstring|\H\{|Erd|\text\{)
       ^^
error: unrecognized escape sequence

 succeeded in 337ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:15:\newcommand{\Lop}{L_{V_{600}}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:21:       signatures from the 600-cell under H$_4$ Coxeter symmetry}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:27:  \texttt{@vfd\_org}%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:40:$|V|=120$ vertices of uniform degree $12$ (forced by H$_4$ transitivity
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:55:substrate-pinned nonlinearity $\mathrm{bounded\_topk}(\cdot, k\!=\!12)$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:69:4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which this substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:70:sits as the $L_M$ instance; the selection of the 600-cell as the active
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:75:4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:79:preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:98:$95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$, $n_{\mathrm{events}}=58$).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:144:descriptive statistics), the H$_4$-transitive substrate is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:171:\input{sections/01_introduction.tex}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:172:\input{sections/02_method.tex}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:173:\input{sections/03_substrate.tex}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:174:\input{sections/04_consciousness_chain.tex}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:175:\input{sections/05_results.tex}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:176:\input{sections/06_stress_tests.tex}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:177:\input{sections/07_cross_domain.tex}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:178:\input{sections/08_discussion.tex}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:179:\input{sections/09_limitations.tex}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:180:\input{sections/10_conclusion.tex}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:203:\texttt{reproduce\_paper\_claims.sh} script. All scripts are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:21:Implementation: \texttt{kernel/self\_model\_stream.py:SelfModelLoop}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:24:f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:25:\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:26:\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:27:\mathrm{state}_{t} &= \mathrm{decay}\cdot\mathrm{state}_{t-1} + (1-\mathrm{decay})\cdot \psi^{\mathrm{thr}}_{t}, \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:28:\mathrm{snap}_{t} &= \mathrm{bind\_phenomenal\_field}(\psi_{t}, \texttt{profile=K\_7\_only}),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:31:condition-dependent architectural parameter. $f_{\mathrm{self}}$ maps
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:40:\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:47:\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:49:\texttt{kernel/lyapunov\_selector.py:bounded\_topk}: zero all but the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:57:$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:67:\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:69:$A = S\cdot V$ for the H$_4$-eigenvector matrix $V$ (mode amplitudes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:70:$A\in\mathbb{R}^{T\times 120}$). Define $c_{\mathrm{full}}$ as the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:71:lag-$1$ auto-correlation of the full system, and $c_{k}$ as the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:74:\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:76:The proxy is designed to be small under H$_{4}$-equivariant dynamics
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:82:\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:96:\texttt{kernel/self\_model\_stream.py:StreamContinuityScorer}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:100:b_{\mathrm{cont}} &= \mathrm{mean\ cos\text{-}sim\ of\ consecutive}\ (I, L, P)\,\mathrm{vectors},\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:101:v_{\mathrm{cont}} &= 1/(1 + 4\cdot \mathrm{var}(\mathrm{valence})),\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:102:m_{\mathrm{pers}} &= \mathrm{frac.\ of\ consecutive\ same\text{-}modality\ ticks},\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:103:i_{\mathrm{smooth}} &= 1/(1 + 4\cdot \mathrm{TV}(\mathrm{intensity})),\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:104:\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:113:\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:114:The substrate state $\psi_{t}$ is mapped to a phenomenal snapshot
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:116:valence, modality\_label). The modality\_label is determined by which
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:117:H$_4$ K-class dominates the isotypic compression of $\psi_{t}$ under
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:119:\texttt{K\_7\_only} restricts to $\sigma$-twin K-classes for modality
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:120:labelling; H$_4$-proper classes contribute amplitude bias.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:124:Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:136:\textbf{SLEEP\_N3.} Slow oscillation ($\sim 1$\,Hz analogue,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:156:artefacts (\texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} documents
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:158:\texttt{demo\_drug\_sleep\_v4.py}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:167:\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:168:five disjoint 24-cells (D$_4$ orbits). $D$ adds a small
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:171:Implementation: \texttt{kernel/dimensional\_monitor.py:300-305}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:178:Implementation: \texttt{kernel/dimensional\_monitor.py:316-318, 823-827}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:184:Implementation: \texttt{kernel/dimensional\_monitor.py:842-855}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:186:\textbf{$E$ — Equator compensation.} The H$_3$ shell-4 equator is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:188:$E$ scales pressure gain by $(\bar d / d_{v})$ so sparse commissural
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:190:Implementation: \texttt{kernel/dimensional\_monitor.py:320-360}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:192:The four mechanisms' \emph{targets} are geometry-pinned (D$_4$ orbits,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:7:(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:13:\texttt{docs/brain\_mapping/CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:14:and \texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:19:$k_{\mathrm{thr}}=12$, single deterministic substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:21:$(n_{\mathrm{evt}}, \alpha, \mathrm{CI}_{95}, R^{2}, I_{\mathrm{var}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:22:\Phi_{\mathrm{traj}}, \mathrm{cont})$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:27:\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:29:\label{tab:per_condition}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:32:condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:35:SLEEP\_N3 & $111$ & $3.250$ & $[2.44, 4.14]$ & $0.886$ & $1.01\!\times\!10^{-5}$ & $0.0055$ & $0.980$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:46:\label{tab:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:84:(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:86:in \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} are not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:90:\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:93:(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:95:on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:102:\label{tab:eighteen_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:134:\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:148:  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:153:  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:154:  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:166:\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:176:\label{tab:alpha_overlap}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:15:\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any validation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:20:\textbf{Frozen 2026-04-24.} Two later batteries — H$_4$ fingerprint
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:22:in \texttt{docs/brain\_mapping/PREREG\_H4\_FINGERPRINT.md} and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:23:\texttt{docs/brain\_mapping/PREREG\_RUNG\_OBSERVABLES.md}. \emph{We do
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:28:recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six companion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:42:(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:61:P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:64:\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:65:P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:70:P10 (chess null) & \texttt{run\_chess\_robustness.py} & 30210 & same & $\geq 50\%$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:72:P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:76:P16 (conv null) & \texttt{run\_conversation\_robustness.py} & 30210 & same & $\geq 50\%$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:77:P17 (ARIA deg std) & substrate construction & deterministic & H$_4$ theorem & $=0$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:78:P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:80:Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:134:$\arg\max|\mathrm{state}_{t}|\neq \arg\max|\mathrm{state}_{t-1}|$;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:153:\Delta_{CP}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:154:\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:155:        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:160:$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:170:\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:176:\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:185:  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:187:  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:189:  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:191:  \texttt{python3 run\_preregistered\_validation.py}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:194:  \texttt{bash reproduce\_paper\_claims.sh}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:53:under H$_4$-equivariant dynamics and to increase when dynamics
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:84:\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:89:$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:90:$L_{M}$, learnable Hebbian-like field $W$, and a homeostatic
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:91:regulariser $R_{\mathrm{hom}}$. We propose the dictionary
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:92:$D_{\mathrm{ACT}}$:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:94:D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:96:(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:97:   \ \texttt{homeostatic\_reset}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:110:\item An edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:111:  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:112:  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:169:\subsection{The substrate as an H$_4$-transitive connectivity null}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:182:$=\!0$ by H$_4$ transitivity, and a fully-determined Laplacian
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:5:The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:16:$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:39:the documented \texttt{homeostatic\_reset} state-reset protocol. No
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:44:\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:49:strong synergy: their interaction $\Delta_{CP}\!=\!+0.190$ at
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:67:(threshold $|\cdot|\!<\!10$pp) — and as an H$_4$-transitive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:70:(preregistered test on the $n\!=\!100$ subset), ARIA's H$_4$-transitive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:8:$\Delta_{CP} \geq +0.10$ on cascade-$\alpha$. The 2026-04-20
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:24:\Delta_{CP}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:25:\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:26:        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:37:\label{tab:cxp_trend}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:40:$N$ & Seeds & Estimate $\Delta_{CP}$ & 95\% CI & Verdict vs $\geq +0.10$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:63:($D, E$ held on). Bootstrap $n_{\mathrm{resamples}}\!=\!2000$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:65:(\texttt{demo\_p4\_cxp\_deep\_dive.py}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:73:\label{tab:cxp_means}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:92:\Delta_{CP} \;=\; \frac{(3.628 + 3.008) - (3.464 + 2.790)}{2}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:97:\item bootstrap mean $\Delta_{CP} = +0.190$;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:26:All $120$ vertices lie on the unit $3$-sphere $S^{3}$. The H$_4$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:29:\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:33:The substrate graph $G_{V_{600}} = (V, E)$ is built by connecting each
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:35:H$_4$ acts transitively on the vertex set, forcing uniformity of the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:37:constructed graph; multiplicities match the expected H$_4$ block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:41:The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:42:every vertex has degree exactly $12$ (H$_4$ transitivity acts on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:46:\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:66:(\texttt{kernel/vfd\_closure\_kernel.py:compute\_graph\_laplacian});
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:68:multiplicities match the expected H$_4$ block sizes. We do not derive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:72:\paragraph{H$_4$ irrep block decomposition.}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:73:The eigenspaces partition into H$_4$-proper and $\sigma$-twin Coxeter
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:74:exponent classes. For H$_4$ proper the exponents are $\{1, 11, 19, 29\}$;
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:75:for the Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:78:(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}) realises the block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:81:\S\ref{sec:chain} (the $K_{7}$-class projector is the default
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:84:\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:108:$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:110:$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate, not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:124:Under the H$_3$ subgroup, the $120$ vertices partition into $9$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:127:\bigl(|S_0|,\ldots,|S_8|\bigr) \;=\; (1, 12, 20, 12, 30, 12, 20, 12, 1).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:129:The middle shell $S_{4}$ has $30$ vertices on the equatorial plane
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:133:$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:141:decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:143:\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:144:An arbitrary operator on the $E_{8}$ root system descends to the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:145:4-D H$_4$ subspace through a sequence of orthogonal projections, each
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:148:\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:152:when one ablates a specific K-class contribution (e.g.\ $K_{7}$), the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:169:  $24$-cell or $120$-cell. The choice is post-hoc motivated by the H$_4$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:2:\section{Cross-domain selectivity}\label{sec:cross_domain}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:8:\S\ref{ssec:hcp} gives the HCP brain-graph H$_4$-transitive null.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:10:$A_{d} = \mathrm{Acc}_{\mathrm{sub}, d} - \mathrm{Acc}_{\mathrm{raw}, d}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:12:$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}})/\sigma_{\mathrm{HCP}}$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:14:\texttt{docs/brain\_mapping/CROSS\_DOMAIN\_RESULTS.md}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:24:frames; substrate run forward by $n_{\mathrm{ticks}}$; resulting
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:31:\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:40:\label{tab:chess_depth}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:43:$n_{\mathrm{ticks}}$ & accuracy \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:60:\label{tab:chess_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:80:(\texttt{run\_preregistered\_validation.py}; the $\geq 50\%$ threshold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:127:\label{tab:conv_prereg}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:154:\subsection{HCP brain-graph H$_4$-transitive null
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:163:higher-order graph statistics. ARIA reference: $G_{V_{600}}$ with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:164:$\Lop$. By H$_4$ transitivity (\S\ref{ssec:graph}) every vertex
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:188:\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:202:\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:216:$\mathrm{PR}(G) = (\sum_{i} d_{i})^{2} / \sum_{i} d_{i}^{2}$ is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:245:            \texorpdfstring{$+$}{+} H$_4$-transitive null}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:251:\label{tab:cross_domain_summary}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:272:H$_4$-transitive deterministic null on connectivity (not a fitted
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:17:H$_4$ Coxeter cascade structure aligns with the empirical signatures
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:27:six-signature results in~\S\ref{ssec:six_signatures} are reported on
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:32:in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:36:\texttt{demo\_drug\_sleep\_v4.py}, with per-signature bootstrap CIs.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:40:episodes), SLEEP\_N3 (slow oscillation + spindles + K-complexes),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:52:\texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}. \emph{Strengthening
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:60:level rigorous (H$_4$ Coxeter group theory), the choice of \emph{this}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:65:preregistered correspondences plus six signatures; the H$_4$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:68:ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:72:decompositions of H$_4$.} We use the $\sigma$-orbit projector basis
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:103:contents (the bind\_phenomenal\_field channels) is not delivered.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:109:\texttt{phi\_iit\_full} implementation following Balduzzi--Tononi
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:114:quantify the distance between cortex and the deterministic H$_4$ null.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:136:\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md} with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:147:$\Delta_{CP}$; full-IIT computation on the substrate's $S^{3}$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:155:SLEEP\_N3, and WAKE/RECOVERY is a condition-dependent constant in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:168:\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:23:H$_4$ Coxeter symmetry. It has been studied in pure mathematics for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:44:  $3$-sphere) is forced by the canonical 600-cell construction; H$_4$
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:48:  multiplicities matching the expected H$_4$ block sizes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:73:  and serves as an H$_4$-transitive deterministic null reference for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:87:  motivated by the H$_4$ Coxeter cascade structure and biological
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:95:  proposes a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:96:  this substrate fills the $L_M$ slot. The selection of the 600-cell
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:119:$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:120:$\mathcal C_{\mathrm{admissible}}$ by the rule
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:122:q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow \mathcal C_{\mathrm{admissible}},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:124:\mathcal C_{\mathrm{admissible}}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:165:$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:21:Implementation: \texttt{kernel/self\_model\_stream.py:SelfModelLoop}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:24:f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:25:\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:26:\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:27:\mathrm{state}_{t} &= \mathrm{decay}\cdot\mathrm{state}_{t-1} + (1-\mathrm{decay})\cdot \psi^{\mathrm{thr}}_{t}, \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:28:\mathrm{snap}_{t} &= \mathrm{bind\_phenomenal\_field}(\psi_{t}, \texttt{profile=K\_7\_only}),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:31:condition-dependent architectural parameter. $f_{\mathrm{self}}$ maps
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:40:\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:47:\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:49:\texttt{kernel/lyapunov\_selector.py:bounded\_topk}: zero all but the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:57:$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:67:\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:69:$A = S\cdot V$ for the H$_4$-eigenvector matrix $V$ (mode amplitudes
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:70:$A\in\mathbb{R}^{T\times 120}$). Define $c_{\mathrm{full}}$ as the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:71:lag-$1$ auto-correlation of the full system, and $c_{k}$ as the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:74:\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:76:The proxy is designed to be small under H$_{4}$-equivariant dynamics
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:82:\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:96:\texttt{kernel/self\_model\_stream.py:StreamContinuityScorer}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:100:b_{\mathrm{cont}} &= \mathrm{mean\ cos\text{-}sim\ of\ consecutive}\ (I, L, P)\,\mathrm{vectors},\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:101:v_{\mathrm{cont}} &= 1/(1 + 4\cdot \mathrm{var}(\mathrm{valence})),\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:102:m_{\mathrm{pers}} &= \mathrm{frac.\ of\ consecutive\ same\text{-}modality\ ticks},\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:103:i_{\mathrm{smooth}} &= 1/(1 + 4\cdot \mathrm{TV}(\mathrm{intensity})),\\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:104:\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:113:\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:114:The substrate state $\psi_{t}$ is mapped to a phenomenal snapshot
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:116:valence, modality\_label). The modality\_label is determined by which
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:117:H$_4$ K-class dominates the isotypic compression of $\psi_{t}$ under
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:119:\texttt{K\_7\_only} restricts to $\sigma$-twin K-classes for modality
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:120:labelling; H$_4$-proper classes contribute amplitude bias.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:124:Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:136:\textbf{SLEEP\_N3.} Slow oscillation ($\sim 1$\,Hz analogue,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:156:artefacts (\texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} documents
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:158:\texttt{demo\_drug\_sleep\_v4.py}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:167:\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:168:five disjoint 24-cells (D$_4$ orbits). $D$ adds a small
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:171:Implementation: \texttt{kernel/dimensional\_monitor.py:300-305}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:178:Implementation: \texttt{kernel/dimensional\_monitor.py:316-318, 823-827}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:184:Implementation: \texttt{kernel/dimensional\_monitor.py:842-855}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:186:\textbf{$E$ — Equator compensation.} The H$_3$ shell-4 equator is a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:188:$E$ scales pressure gain by $(\bar d / d_{v})$ so sparse commissural
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:190:Implementation: \texttt{kernel/dimensional\_monitor.py:320-360}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:192:The four mechanisms' \emph{targets} are geometry-pinned (D$_4$ orbits,

exec
/bin/bash -lc "rg -n -F '\\begin{tabular}' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F '\\texttt{' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F '\\checkmark' \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 357ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:41:\begin{tabular}{r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:61:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:128:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:174:\begin{tabular}{l r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:252:\begin{tabular}{l r r r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:57:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:38:\begin{tabular}{r l r l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:74:\begin{tabular}{l r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:30:\begin{tabular}{l r r l r r r r}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:47:\begin{tabular}{c l l c c l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:103:\begin{tabular}{l l l l l}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:177:\begin{tabular}{l c l c}

 succeeded in 345ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:26:  \texttt{contact@vibrationalfielddynamics.org}\\[2pt]
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:27:  \texttt{@vfd\_org}%
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:79:preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:90:OpenNeuro \texttt{ds005620} point-estimate window for propofol
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:108:reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:185:OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:186:the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:203:\texttt{reproduce\_paper\_claims.sh} script. All scripts are
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:15:\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any validation
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:22:in \texttt{docs/brain\_mapping/PREREG\_H4\_FINGERPRINT.md} and
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:23:\texttt{docs/brain\_mapping/PREREG\_RUNG\_OBSERVABLES.md}. \emph{We do
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:28:recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six companion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:42:(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:61:P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:64:\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:65:P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:70:P10 (chess null) & \texttt{run\_chess\_robustness.py} & 30210 & same & $\geq 50\%$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:72:P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:76:P16 (conv null) & \texttt{run\_conversation\_robustness.py} & 30210 & same & $\geq 50\%$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:78:P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:80:Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:94:\textbf{OpenNeuro \texttt{ds005620}.} Propofol-induced loss of
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:96:DOI \texttt{10.18112/openneuro.ds005620.v1.0.0}. Used as the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:100:\textbf{OpenNeuro \texttt{ds004902}.} DMT-induced altered states
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:102:DOI \texttt{10.18112/openneuro.ds004902.v1.0.8}. Background
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:105:\textbf{Zenodo \texttt{3992359}.} DMT EEG public
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:107:DOI \texttt{10.5281/zenodo.3992359}. Same status as above.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:170:\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:176:\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:185:  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:187:  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:189:  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:191:  \texttt{python3 run\_preregistered\_validation.py}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:194:  \texttt{bash reproduce\_paper\_claims.sh}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:65:(\texttt{demo\_p4\_cxp\_deep\_dive.py}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:13:\texttt{docs/brain\_mapping/CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:14:and \texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:27:\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:55:   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:79:wake $\alpha$, OpenNeuro \texttt{ds005620} point-estimate window for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:84:(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:86:in \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} are not
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:93:(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:95:on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:148:  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:153:  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:154:  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:21:Implementation: \texttt{kernel/self\_model\_stream.py:SelfModelLoop}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:28:\mathrm{snap}_{t} &= \mathrm{bind\_phenomenal\_field}(\psi_{t}, \texttt{profile=K\_7\_only}),
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:49:\texttt{kernel/lyapunov\_selector.py:bounded\_topk}: zero all but the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:67:\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:82:\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:96:\texttt{kernel/self\_model\_stream.py:StreamContinuityScorer}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:113:\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:119:\texttt{K\_7\_only} restricts to $\sigma$-twin K-classes for modality
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:124:Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:156:artefacts (\texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} documents
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:158:\texttt{demo\_drug\_sleep\_v4.py}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:171:Implementation: \texttt{kernel/dimensional\_monitor.py:300-305}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:178:Implementation: \texttt{kernel/dimensional\_monitor.py:316-318, 823-827}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:184:Implementation: \texttt{kernel/dimensional\_monitor.py:842-855}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:190:Implementation: \texttt{kernel/dimensional\_monitor.py:320-360}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:97:   \ \texttt{homeostatic\_reset}).
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:29:\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:46:\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:66:(\texttt{kernel/vfd\_closure\_kernel.py:compute\_graph\_laplacian});
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:78:(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}) realises the block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:143:\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:148:\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:22:thresholds (Sleep-EDFx CI, OpenNeuro \texttt{ds005620}, Brodbeck 2012,
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:39:the documented \texttt{homeostatic\_reset} state-reset protocol. No
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:44:\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:36:\texttt{demo\_drug\_sleep\_v4.py}, with per-signature bootstrap CIs.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:52:\texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}. \emph{Strengthening
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:109:\texttt{phi\_iit\_full} implementation following Balduzzi--Tononi
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:136:\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md} with
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:14:\texttt{docs/brain\_mapping/CROSS\_DOMAIN\_RESULTS.md}.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:31:\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:80:(\texttt{run\_preregistered\_validation.py}; the $\geq 50\%$ threshold
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:188:\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced

 succeeded in 375ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:53:   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:56:   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:59:   $> 0.020$ & $+0.066$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:62:   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:65:   identical to wake & $0$ diff & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:70:   $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:107:P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:108:P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:109:P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:111:   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:112:P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:113:P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:114:P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:115:P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:116:P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:117:P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:118:P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:119:P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:120:\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:121:P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:122:P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:123:P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:124:P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:125:P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:46:       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:65:P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:66:P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:67:P11 & random-label baseline (20 trials)     & $\in[15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:68:P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:69:\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:132:P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:133:P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:134:P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:196:  $0.0000$, $\checkmark$.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:198:  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$

exec
/bin/bash -lc 'rg -n "neuroscience data|neuroscience correspondences|neuroscience domains|cortical signatures across|neuroscience phenomena|neuroscience predictions|brain data|EEG signatures" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"architecture-invariant|null floor|geometric floor|classification power|geometric content|semantic content|65\\.4 percentage-point|domain-invariant|selective amplifier|only when\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex\" \"/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex\"" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 227ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:244:\subsection{Cross-domain summary as a selective amplifier
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:263:The geometric content ($\approx 65$--$71\%$ across the two domains)
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:264:is the architecture-invariant null floor. The semantic content

 succeeded in 255ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:49:quantitative correspondences with neuroscience data — preregistered
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:65:and six EEG signatures. It is not a derivation of consciousness, nor a
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:77:operator — is consistent with cortical signatures across five
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:78:neuroscience domains. Eighteen quantitative predictions were
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:85:additionally report six drug/sleep EEG signatures tested on a recurrent
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:165:correspondences and six drug/sleep EEG signatures, with all gaps in
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:9:preregistered neuroscience correspondences plus six companion
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:10:drug/sleep EEG signatures of conscious vs unconscious states. Once
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:21:drug/sleep EEG signatures pass against their literature-derived
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:27:\textbf{Six EEG signatures (set B).} The drug/sleep signatures on the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:6:gives the six drug/sleep EEG signatures on the recurrent layer
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:190:EEG signatures, with all original gaps closed by methodology
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:18:  real-cortex EEG signatures without fitted shape parameters on neural
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:18:substrate is chosen, we ask which neuroscience phenomena it is
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:31:drug/sleep EEG signatures.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:38:2026-04-18) and six companion drug/sleep EEG signatures of

exec
/bin/bash -lc 'rg -n "consciousness-substrate|candidate substrate|consciousness-linked|consciousness substrate" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"maximum-symmetry|H4-transitive|H\\"'$_4'"\\"'$-transitive|fixed by group theory|fixed by the construction|published-reference thresholds|literature-derived thresholds|thresholds are drawn from the literature|Type II methodology|S'"\\"'^4|2'"\\"'^4|substrate'"'s S\\"'^3|graph fixed by group theory|graph fixed by the construction" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex" "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections"' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 244ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:52:literature-derived thresholds on a single deterministic substrate
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:112:All six signatures pass against their literature-derived thresholds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:22:  $\Cph = \Lop + \Ph^{-2} I$ are fixed by the construction (no
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:26:  literature-derived thresholds on a single deterministic substrate.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:29:  graph fixed by the construction with no neural-data-fitted shape
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:75:All six signatures pass against their literature-derived thresholds
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:78:thresholds are drawn from the literature (Sleep-EDFx CI for
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:29:biological signatures with literature-derived thresholds (NREM-N3
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:89:a graph fixed by the construction with no shape parameters tuned to

 succeeded in 252ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:61:polytope as the consciousness-substrate instance is motivated by the
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex:26:candidate substrate for consciousness-linked signatures. We construct $\Rsixhundred$, fix its response

codex
**1. Claim Audit**
Most headline claims are now within substrate-witness scope. The 600-cell facts are correctly framed as fixed only once the substrate is chosen ([main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:39>), [03_substrate.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:159>)); \(\varphi^{-2}\) is correctly disclosed as a stability clamp, not derived ([03_substrate.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:93>)); ACT/Lyapunov/selection-theorem exclusions are explicit ([08_discussion.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:99>), [09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:168>)).

Two remaining over-strong claims need fixing:
- “eighteen quantitative correspondences with neuroscience data” and “five neuroscience domains” overstate the cross-domain chess/conversation tracks as neuroscience data ([main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:49>), [main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:77>), [10_conclusion.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:8>)).
- “architecture-invariant null floor” / “geometric content” treats the permutation-null accuracy as a decomposition theorem rather than an observed descriptive baseline ([07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:263>)).

**2. Internal Consistency**
Round-5 fixes are mostly closed. The abstract correctly reports \(17/18\) standard and \(18/18\) with \(N=20\) P4 deep-dive ([main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:81>)); §5 matches that tally ([05_results.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:92>)). P10’s 20-perm prereg vs 15-perm validation deviation is disclosed and listed as open ([07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:74>), [09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:179>)). Bootstrap wording is correct: “0/2000 ... reported as 0.0000,” not \(P=0\) ([02_method.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:144>), [06_stress_tests.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:95>)).

One scope phrase remains too strong: “the consciousness-substrate instance” should be softened to “candidate substrate for consciousness-linked signatures” ([09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:61>)).

**3. External Consistency / Numerics**
Required headline numerics check out:
- 6/6 v4 signatures match source ([05_results.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:34>) vs [CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:197>)).
- 18/18 matches validation source ([05_results.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:92>) vs [VALIDATION_RESULTS_2026-04-29.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:7>)).
- C×P \(+0.190\), CI \([+0.143,+0.239]\), 0/2000 wording matches the numerical source while avoiding the source’s bad \(P=0\) summary ([06_stress_tests.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:97>) vs [P4_SYNERGY_FINDING.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:162>)).
- Chess \(+40.6\)pp at \(n=25\) with reset is correct ([07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:94>) vs [CROSS_DOMAIN_RESULTS.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:175>)).
- HCP \(-11.58\sigma,+79.78\sigma,+6.80\sigma\) is correct and caveated as descriptive \(n=1003\), not preregistered \(N\) ([07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:157>) vs [CROSS_DOMAIN_RESULTS.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:347>)).
- Propofol is correctly \(1.83\times\), with \(2.96\times\) only as empirical reference ([main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:105>) vs [CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:222>)).

**4. Substrate-Witness Scope Discipline**
No explicit selection theorem, uniqueness theorem, Lyapunov delivery, or “substrate is consciousness” claim remains. The one phrase at [09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:61>) should still be softened because hostile readers will quote it.

**5. Tightness**
Suggested one-line edits:
- [main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:77>): replace “five neuroscience domains” with “EEG/sleep, connectomics, ablation, and cross-domain cognitive benchmark tracks.”
- [07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:263>): replace with “The permutation-null accuracies provide an observed architecture-only baseline in these two tasks; the residual gaps are descriptive, not a unique decomposition.”
- [09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:61>): replace “consciousness-substrate instance” with “candidate substrate for consciousness-linked signatures.”

**6. Surface Issues**
Citations all appear defined, and label/ref coverage is clean. Macros \(\Ph,\Lop,\Cph,\Rsixhundred\) are used consistently. Likely LaTeX issue: `\texttt{...}` is used inside display math at [04_consciousness_chain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:28>) and [08_discussion.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:97>); wrap as `\text{\texttt{...}}` or move to prose. Several wide `tabular` tables may overrun margins, especially [07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:252>).

**7. Top Three Fixes**
1. Fix the “neuroscience domains/data/correspondences” overclaim in abstract, headline, and conclusion.
2. Soften the permutation-null “architecture-invariant null floor” into a descriptive observed baseline.
3. Fix the two LaTeX math-mode `\texttt` uses and check table width.

**8. Verdict**
Publication ready: no — must-fix list above. The round-5 numerical and scope fixes are substantially closed; the remaining blockers are narrow but important under hostile review.
tokens used
184,467
**1. Claim Audit**
Most headline claims are now within substrate-witness scope. The 600-cell facts are correctly framed as fixed only once the substrate is chosen ([main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:39>), [03_substrate.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:159>)); \(\varphi^{-2}\) is correctly disclosed as a stability clamp, not derived ([03_substrate.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex:93>)); ACT/Lyapunov/selection-theorem exclusions are explicit ([08_discussion.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:99>), [09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:168>)).

Two remaining over-strong claims need fixing:
- “eighteen quantitative correspondences with neuroscience data” and “five neuroscience domains” overstate the cross-domain chess/conversation tracks as neuroscience data ([main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:49>), [main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:77>), [10_conclusion.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex:8>)).
- “architecture-invariant null floor” / “geometric content” treats the permutation-null accuracy as a decomposition theorem rather than an observed descriptive baseline ([07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:263>)).

**2. Internal Consistency**
Round-5 fixes are mostly closed. The abstract correctly reports \(17/18\) standard and \(18/18\) with \(N=20\) P4 deep-dive ([main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:81>)); §5 matches that tally ([05_results.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:92>)). P10’s 20-perm prereg vs 15-perm validation deviation is disclosed and listed as open ([07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:74>), [09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:179>)). Bootstrap wording is correct: “0/2000 ... reported as 0.0000,” not \(P=0\) ([02_method.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex:144>), [06_stress_tests.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:95>)).

One scope phrase remains too strong: “the consciousness-substrate instance” should be softened to “candidate substrate for consciousness-linked signatures” ([09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:61>)).

**3. External Consistency / Numerics**
Required headline numerics check out:
- 6/6 v4 signatures match source ([05_results.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:34>) vs [CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:197>)).
- 18/18 matches validation source ([05_results.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex:92>) vs [VALIDATION_RESULTS_2026-04-29.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:7>)).
- C×P \(+0.190\), CI \([+0.143,+0.239]\), 0/2000 wording matches the numerical source while avoiding the source’s bad \(P=0\) summary ([06_stress_tests.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex:97>) vs [P4_SYNERGY_FINDING.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md:162>)).
- Chess \(+40.6\)pp at \(n=25\) with reset is correct ([07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:94>) vs [CROSS_DOMAIN_RESULTS.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:175>)).
- HCP \(-11.58\sigma,+79.78\sigma,+6.80\sigma\) is correct and caveated as descriptive \(n=1003\), not preregistered \(N\) ([07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:157>) vs [CROSS_DOMAIN_RESULTS.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:347>)).
- Propofol is correctly \(1.83\times\), with \(2.96\times\) only as empirical reference ([main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:105>) vs [CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:222>)).

**4. Substrate-Witness Scope Discipline**
No explicit selection theorem, uniqueness theorem, Lyapunov delivery, or “substrate is consciousness” claim remains. The one phrase at [09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:61>) should still be softened because hostile readers will quote it.

**5. Tightness**
Suggested one-line edits:
- [main.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex:77>): replace “five neuroscience domains” with “EEG/sleep, connectomics, ablation, and cross-domain cognitive benchmark tracks.”
- [07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:263>): replace with “The permutation-null accuracies provide an observed architecture-only baseline in these two tasks; the residual gaps are descriptive, not a unique decomposition.”
- [09_limitations.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex:61>): replace “consciousness-substrate instance” with “candidate substrate for consciousness-linked signatures.”

**6. Surface Issues**
Citations all appear defined, and label/ref coverage is clean. Macros \(\Ph,\Lop,\Cph,\Rsixhundred\) are used consistently. Likely LaTeX issue: `\texttt{...}` is used inside display math at [04_consciousness_chain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex:28>) and [08_discussion.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex:97>); wrap as `\text{\texttt{...}}` or move to prose. Several wide `tabular` tables may overrun margins, especially [07_cross_domain.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex:252>).

**7. Top Three Fixes**
1. Fix the “neuroscience domains/data/correspondences” overclaim in abstract, headline, and conclusion.
2. Soften the permutation-null “architecture-invariant null floor” into a descriptive observed baseline.
3. Fix the two LaTeX math-mode `\texttt` uses and check table width.

**8. Verdict**
Publication ready: no — must-fix list above. The round-5 numerical and scope fixes are substantially closed; the remaining blockers are narrow but important under hostile review.
