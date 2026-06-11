Read-only audit completed. I did not edit or commit anything.

**SECTION A. Insight / External Relevance**

**Already in cascade / companion papers**
- Substrate-witness framing is explicit in `TASK-aria-paper-completion.md:42-57`: use substrate witness, not ACT selection witness; no Lyapunov \(V(W)\), no \(2I\)-equivariance check as deliverables.
- Fixed response kernel is already defined in `docs/aria-closure-kernel.md:11-23`, with 600-cell facts at `:49-60`.
- b-anomaly is the passive-regime companion witness: fixed \(C_\varphi\)-derived kernel, no shape retuning, one amplitude per dataset, at `docs/aria-closure-kernel.md:76-90`, with caveats at `:127-143`.
- ACT supplies only the non-load-bearing 4-tuple bridge: selection is conditional on Lyapunov/timescale hypotheses in `adaptive-closure-transport.tex:222-228`; ARIA dictionary is proposed, not proved, at `:303-328`; programme bridge is explicitly non-load-bearing at `:394-449`.

**Only in `insight.md`, not suitable as load-bearing ARIA paper content**
- Fine-structure / two-600-cell material: `insight.md:47-64`, `:176-234`. Interesting programme background, but not relevant to ARIA neuroscience claims.
- Crystallisation triplet / \(\alpha\) as selection coupling: `insight.md:361-407`, `:410-450`. Do not import into ARIA except as future programme language.
- RH, god-prime, QMS-3, prime-locus material: `insight.md:601-717`, `:724-827`. Not relevant to this paper.
- Pentagonal holonomy connection: `insight.md:830-892`. Potential future route for selection dynamics, but outside substrate-witness scope.

**External literature directly needed**
- 600-cell/H4 facts: Coxeter/MathWorld 600-cell reference.
- EEG/SOC: Beggs & Plenz 2003.
- Dataset citations: Sleep-EDFx/PhysioNet, OpenNeuro `ds005620`, OpenNeuro `ds004902`, Zenodo DMT `10.5281/zenodo.3992359`, HCP S1200.
- Consciousness theory comparison: Tononi/IIT, Balduzzi & Tononi, Global Workspace, predictive processing.
- Microstates: Brodbeck et al. 2012 for wake/NREM; propofol microstate/anesthesia papers for drug-state support.

**SECTION B. Priority Gaps / Build List**

B1. `01_introduction.tex`: claim-boundary definition  
Object: \(q:\mathcal R_{\rm numeric}\to\mathcal C_{\rm admissible}\), prose map from results to allowed claims.  
Bridges: strong manuscript claims to substrate-witness scope.  
Route: new writing from task discipline.  
First step: “What is tested / not claimed” box.  
Sources: `TASK:44-57`, `TASK:203-226`, `MANUSCRIPT_V2.md:75-87`, `:1086-1091`. AC2, AC9.

B2. `02_method.tex`: provenance ledger  
Object: \(\Pi:\{P1..P18,S1..S6\}\to\)(script, seed, dataset, threshold, result).  
Bridges: preregistration, deterministic scripts, hostile reproducibility.  
Route: lift from validation docs.  
First step: one table for dates, seeds, scripts, wallclock.  
Sources: `TASK:22-33`, `MANUSCRIPT_V2.md:554-609`, `PAPER_PREDICTIONS.md:1-14`, `VALIDATION_RESULTS_2026-04-29.md:19-75`. AC1, AC8.

B3. `03_substrate.tex`: 600-cell response substrate  
Object: \(V_{600}=(V,E)\), \(L:\mathbb R^{120}\to\mathbb R^{120}\), \(C_\varphi=L+\varphi^{-2}I\).  
Bridges: classical geometry to empirical substrate.  
Route: classical literature plus local kernel doc.  
First step: lemma stating 120 vertices, 720 edges, degree 12, H4 transitivity, 9 shells, shifted Green response.  
Sources: `MANUSCRIPT_V2.md:158-224`, `aria-closure-kernel.md:11-60`. AC4.

B4. `04_consciousness_chain.tex`: recurrent substrate observables  
Object: \(T_\eta:\mathbb R^{120}\times F_t\to\mathbb R^{120}\); observables \(O(\tau)=(\alpha,I_{\rm var},\Phi,{\rm cont})\).  
Bridges: substrate response to six EEG signatures.  
Route: lift implementation narrative, rewrite as method not metaphysics.  
First step: define `bounded_topk(k=12)`, \(\Phi\) proxy, continuity score.  
Sources: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:51-102`, `:195-288`; `consciousness_tensor.py:340-359` for \(\varphi^{-2}\) floor caveat. AC4.

B5. `05_results.tex`: exact empirical tables  
Object: result map \(R:\) condition/test id \(\to\) scalar plus threshold verdict.  
Bridges: source numerics to paper claims.  
Route: verbatim lift, no recomputation.  
First step: tables for 6/6 v4, 18/18, three-way \(\alpha\) overlap.  
Sources: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:30-42`, `:197-288`; `VALIDATION_RESULTS_2026-04-29.md:78-99`, `:262-295`. AC1.

B6. `06_stress_tests.tex`: C×P interaction proof block  
Object: \(\Delta_{CP}=((\alpha_{CP}+\alpha_0)-(\alpha_C+\alpha_P))/2\).  
Bridges: original P4 fail to strong-coupling result without threshold change.  
Route: existing N=20 derivation plus bootstrap.  
First step: include N=3/5/10/20 trend, finite-bootstrap wording.  
Sources: `P4_SYNERGY_FINDING.md:102-173`, `:175-193`, `:197-229`, `:375-398`. AC1, AC9.

B7. `07_cross_domain.tex`: selective amplifier and HCP null  
Object: \(A_d={\rm Acc}_{sub,d}-{\rm Acc}_{raw,d}\); \(Z_m=(m_{\rm ARIA}-\mu_{\rm HCP})/\sigma_{\rm HCP}\).  
Bridges: chess/conversation/HCP into one substrate-witness result.  
Route: lift latest cross-domain report, not older Paper Basis numbers.  
First step: use +40.6pp, n=25, 93.8% as authoritative.  
Sources: `CROSS_DOMAIN_RESULTS.md:52-216`, `:234-303`, `:307-424`. AC1, AC5.

B8. `08_discussion.tex`: non-load-bearing ACT bridge  
Object: dictionary \(D_{\rm ACT}:(M,L_M,W,R_{\rm hom})\to\) ARIA components.  
Bridges: empirical ARIA to ACT without claiming selection theorem.  
Route: alternative route K, explicitly non-load-bearing.  
First step: one closing subsection mapping the 4-tuple and deferring Lyapunov, edge-space lift, \(2I\)-equivariance.  
Sources: `TASK:44-57`, `ACT:303-328`, `ACT:394-449`, `aria-closure-kernel.md:216-257`. AC2, AC6, AC7.

B9. `09_limitations.tex`: hostile-review guard matrix  
Object: \(G:{\rm risk}\to({\rm disclosure},{\rm evidence},{\rm build})\).  
Bridges: evidence to credible scope.  
Route: b-anomaly five-move template.  
First step: regime, post-hoc, interpretation, test/claim, state-drift moves.  
Sources: `TASK:172-191`, `MANUSCRIPT_V2.md:1012-1098`, `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:354-379`, `NON_EQUILIBRIUM_FINDING.md:11-21`, `:97-105`. AC3, AC5.

B10. `main.tex`, `README.md`, `references.bib`: paper shell  
Object: deliverable graph \(D=(sections,bib,repro)\).  
Bridges: source docs to BANOMALY-style paper.  
Route: mirror template.  
First step: scaffold exact 10-section structure.  
Sources: `TASK:61-83`, `b-anomaly/paper/main.tex:136-171`, `MANUSCRIPT_V2.md:1101-1159`. AC7.

**SECTION C. Reversals / Corrections**

Apply these when lifting prose:

- at `PAPER_BASIS_2026-04-29.md:48` replace `chess pattern recognition (84.4% LOO with reset; 83.1% 5-fold CV)` with `chess pattern recognition (93.8% LOO with reset at n=25; 83.1% 5-fold CV)`.
- at `PAPER_BASIS_2026-04-29.md:550` replace `Chess goldilocks peak:                   n=15` with `Chess goldilocks peak:                   n=25`.
- at `PAPER_BASIS_2026-04-29.md:551` replace `Chess substrate lift on LOO (with reset): +27.2pp` with `Chess substrate lift on LOO (with reset): +40.6pp`.
- at `PAPER_BASIS_2026-04-29.md:562` replace `substrate **lifts chess by +27pp**` with `substrate **lifts chess by +40.6pp on LOO at n=25**`.
- at `PAPER_BASIS_2026-04-29.md:602` replace `| P12 | Goldilocks peak ∈ {15, 25, 40, 60} | ✅ | 15 |` with `| P12 | Goldilocks peak ∈ {15, 25, 40, 60} | ✅ | 25 |`.
- at `PAPER_BASIS_2026-04-29.md:603` replace `| P13 | Chess LOO lift ≥ +15pp (with reset) | ✅ | +27.2pp |` with `| P13 | Chess LOO lift ≥ +15pp (with reset) | ✅ | +40.6pp |`.
- at `MANUSCRIPT_V2.md:17` replace `The substrate is fully derivable from group theory:` with `Once the 600-cell substrate is chosen, its graph structure is fixed by group theory:`.
- at `PAPER_BASIS_2026-04-29.md:27` replace `The substrate is fully derivable from group theory;` with `Once the 600-cell substrate is chosen, its graph structure is fixed by group theory;`.
- at `MANUSCRIPT_V2.md:795` replace `**HCP result (n=1003 subjects, ICA-50):**` with `**HCP result (preregistered n=100 ICA-50 plus full-cohort n=1003 descriptive statistics):**`.
- in any new paper text replace `P(synergy ≤ 0) = 0` with `0/2000 bootstrap resamples were at or below zero, reported as 0.0000`.

**SECTION D. Route Discipline / Citation Audit**

Route S, load-bearing: substrate-witness paper. It needs exact numerics, prereg provenance, substrate construction, limitations.

Route K, non-load-bearing only: ACT-selection witness. It would require Lyapunov \(V(W)\), edge-space decomposition, \(2I\)-equivariance, and full reduced-flow convergence. Do not present this as delivered.

Required bibtex groups:
- Geometry: Coxeter / 600-cell reference, e.g. MathWorld 600-cell.
- EEG avalanche: Beggs & Plenz 2003, DOI `10.1523/JNEUROSCI.23-35-11167.2003`.
- Datasets: Sleep-EDFx/PhysioNet; OpenNeuro `ds005620` DOI `10.18112/openneuro.ds005620.v1.0.0`; OpenNeuro `ds004902` DOI `10.18112/openneuro.ds004902.v1.0.8`; DMT Zenodo `10.5281/zenodo.3992359`; HCP S1200 plus Van Essen 2013 DOI `10.1016/j.neuroimage.2013.05.041`.
- Consciousness theory: Tononi 2008, Balduzzi & Tononi 2008, Global Workspace, predictive processing.
- Microstates/anesthesia: Brodbeck et al. 2012 DOI `10.1016/j.neuroimage.2012.05.060`; add a propofol-specific microstate citation if claiming anesthesia fragmentation.

**SECTION E. Top-5 Risk Register**

1. \(\varphi^{-2}\) floor not derived. Guard: disclose as design-level stability clamp, not theorem. Anchor: `consciousness_tensor.py:348-359`.
2. Preregistration date ambiguity. Guard: separate Apr 18 P1-P18 from Apr 24 H4/rung batteries. Anchors: `PAPER_PREDICTIONS.md:1-14`, `PREREG_H4_FINGERPRINT.md:1-11`, `PREREG_RUNG_OBSERVABLES.md:1-7`.
3. v4 single-seed chain. Guard: state deterministic seed 42 and event bootstrap; name cross-seed replication as strengthening build. Anchor: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:195-203`, `:371-376`.
4. P4 N=20 was data-second after N=3 fail. Guard: report ordering, original fail, same threshold, high-variance rationale. Anchors: `P4_SYNERGY_FINDING.md:68-95`, `:102-123`, `VALIDATION_RESULTS_2026-04-29.md:267-280`.
5. 600-cell chosen post-hoc. Guard: substrate-witness framing, no uniqueness claim, future ablation against 24-cell/120-cell. Anchors: `TASK:46-50`, `MANUSCRIPT_V2.md:1086-1091`.

Missing-content check: `MANUSCRIPT_V2` is paper-shaped, but §1 and abstract need overclaim tightening; §5 needs exact dataset DOIs; §6 needs finite-bootstrap wording; §8 limits must become target §9 five-move limitations.

**SECTION F. Top 3 Next Builds**

1. Build `paper/sections/05_results.tex`: insert exact 6/6, 18/18, and \(\alpha\)-overlap tables. Anchors: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:197-288`, `VALIDATION_RESULTS_2026-04-29.md:78-99`, `CROSS_DOMAIN_RESULTS.md:184-196`.

2. Build `paper/sections/03_substrate.tex` plus limitation hooks: define \(V_{600}\), \(L\), \(C_\varphi\), shells, and \(\varphi^{-2}\) disclosure. Anchors: `aria-closure-kernel.md:11-60`, `MANUSCRIPT_V2.md:158-224`, `consciousness_tensor.py:348-359`.

3. Build `paper/sections/06_stress_tests.tex` and `07_cross_domain.tex`: P4 factorial derivation, reset protocol, +40.6pp chess lift, HCP null. Anchors: `P4_SYNERGY_FINDING.md:125-173`, `VALIDATION_RESULTS_2026-04-29.md:163-194`, `CROSS_DOMAIN_RESULTS.md:175-216`, `:307-424`.

External sources used: MathWorld 600-cell, PhysioNet Sleep-EDFx, EEGDash/OpenNeuro DS005620 and DS004902, Zenodo DMT record 3992359, PubMed/PMC entries for Beggs & Plenz, Tononi, Balduzzi & Tononi, Brodbeck, and Van Essen/HCP.
