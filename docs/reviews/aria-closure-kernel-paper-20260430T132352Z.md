OpenAI Codex v0.124.0 (research preview)
--------
workdir: /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
model: gpt-5.5
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019dde8f-6783-7411-b829-1ce732a2f036
--------
user
You are reviewing a physics/mathematical preprint in LaTeX. Treat this like a careful
journal-referee pass, not a code review.

Paper path:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/main.tex

Section files (read all 10):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/01_introduction.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/02_definition.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/03_substrate.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/04_spectrum.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/05_agreement.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/06_passive_witness.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/07_active_witness.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/08_programme_home.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/09_limitations.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/sections/10_conclusion.tex

Bibliography:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/paper/references.bib

Verification script and results (the paper lifts numbers from these):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/verify_kernel.py
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-closure-kernel/repro/results.json

Companion preprint to validate inherited claims against:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/paper/main.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/paper/sections/

Source documents the kernel paper draws from:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/aria-closure-kernel.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md

This paper is an OPERATOR WITNESS, not a derivation. Hard discipline:
- never claim φ⁻² is derived (it is a design-level shift)
- never claim 600-cell uniqueness
- never claim the operator IS the unique kernel on either empirical landing
- never claim a Lyapunov / 2I-equivariance / selection theorem is delivered
- never inherit b-anomaly claims beyond what b-anomaly itself claims (AIC tie + Mode-B drift caveats inherited verbatim)
- never inherit aria-chess claims beyond substrate-witness scope
- per-vertex correlation is 0.976 unweighted, 0.888 φ-geometric, 0.884 φ-arithmetic
- shell-mean correlation is 0.923 unweighted (the per-vertex test is the headline)
- operator-norm ‖C_φ⁻¹‖ = φ² ≈ 2.618 (computed) matches closed-form
- Laplacian spectrum: {0, 12-6φ, 12-4φ, 9, 12, 14, 4φ+8, 15, 6φ+6} with multiplicities {1, 4, 9, 16, 25, 36, 9, 16, 4}, sum 120

Read the file in full, then produce a structured review with the following
sections:

1. **Claim audit** For every non-trivial claim (theorem, proposition,
   numerical result, headline statement), say whether the stated argument
   actually establishes the stated claim. Flag over-claims, hidden assumptions,
   missing hypotheses, or cases where the prose needs softening. Quote the
   specific claim and cite the file:line.

2. **Internal consistency** Identify any place where definitions,
   assumptions, or notation conflict across sections. Check that the abstract
   matches the headline numbers; that the inherited b-anomaly numbers in §6
   match what b-anomaly's README states; that the inherited aria-chess numbers
   in §7 match the aria-chess paper.

3. **External consistency / numerics** For each headline numeric verify against
   `repro/results.json` by reading it locally:
   - 120 vertices, 720 edges, degree 12 uniform
   - shell sizes {1, 12, 20, 12, 30, 12, 20, 12, 1}
   - Laplacian spectrum (closed-form Z[φ] values matching numerics)
   - operator norm ‖C_φ⁻¹‖ = φ²
   - per-vertex correlation 0.976 (unweighted) vs 0.888 (φ-geom) vs 0.884 (φ-arith)
   If you find any disagreement, flag with file:line in both source and paper.

4. **Operator-witness scope discipline** Identify any sentence that strays into
   selection-theorem territory, derivation-of-φ⁻² territory, or kernel-uniqueness
   territory. The paper must stay strictly inside operator-witness scope.

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
I’ll read the kernel paper and the cited local source material, then cross-check every numeric headline against `results.json` and inherited claims against the companion files. I’m starting by mapping the file set and line numbers so the review can cite exact locations.
exec
/bin/bash -lc "pwd && rg --files papers/aria-closure-kernel/paper papers/aria-closure-kernel/repro papers/aria-chess-paper/paper docs | sed -n '1,160p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'wc -l papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex papers/aria-closure-kernel/paper/references.bib papers/aria-closure-kernel/repro/verify_kernel.py papers/aria-closure-kernel/repro/results.json docs/aria-closure-kernel.md ../BANOMALY-001/vfd-b-anomaly/README.md papers/aria-chess-paper/paper/main.tex papers/aria-chess-paper/paper/sections/*.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'git status --short' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 319ms:
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
docs/papers.md
docs/overview.md
docs/one-page-explainer.tex
docs/observer-instance-definition.md
docs/legacy-master-math-consolidation.md
docs/index.md
docs/glossary.md
docs/gaps.md
docs/fractal-cascade-projection.md
docs/figures.md
docs/closure-cosmogenesis.md
docs/cascade-helix-hypothesis.md
docs/capstone-session-checkpoint.md
docs/aria-closure-kernel.md
docs/architecture.md
docs/reproduce.md
docs/rh-projection-class.md
docs/report.tex
docs/substrate-indexing-programme-final.md
docs/report.md
docs/recovery-manifest.md
docs/proof-sheet.md
docs/projection-narrative.md
docs/programme-plan.md
docs/preregistration-juno.md
docs/phi-irrep-ym-bridge-finding.md
docs/pentagonal-torsion-derivation.md
docs/session-checkpoint.md
docs/soul-prime-as-pi0.md
docs/summary-for-physicists.md
docs/why.md
docs/consistency.md
docs/rh-cascade-closure-dynamics.md
docs/convergence-with-smart.md
docs/reproducibility.md
docs/revision-protocol.md
docs/codex-work/TASK-h-grad-1-r2-20260423T223917Z.md
docs/codex-work/TASK-h-grad-1-b1b2-sim-20260423T225925Z.md
docs/codex-work/TASK-icosian-coord-20260423T222530Z.md
docs/figures/relative_error_bars.svg
docs/figures/relative_error_bars.png
docs/figures/form_factor_curves.svg
docs/figures/form_factor_curves.png
papers/aria-closure-kernel/paper/main.tex
papers/aria-closure-kernel/paper/main.pdf
papers/aria-closure-kernel/paper/references.bib
papers/aria-closure-kernel/paper/README.md
docs/figures/spectrum_histogram.svg
docs/figures/spectrum_histogram.png
docs/figures/vfd_vs_experiment.png
docs/figures/vfd_vs_experiment.svg
docs/reviews/biology-rung-capsid-20260423T081021Z.md
docs/reviews/biology-rung-capsid-20260423T080603Z.md
docs/reviews/biology-rung-capsid-20260423T080131Z.md
docs/reviews/biology-rung-bioelectric-20260423T094549Z.md
docs/reviews/biology-rung-bioelectric-20260423T093803Z.md
docs/reviews/aria-closure-kernel-paper-20260430T132352Z.md
docs/reviews/aria-closure-kernel-paper-20260430T131518Z.md
docs/reviews/aria-closure-kernel-paper-20260430T130620Z.md
docs/reviews/aria-closure-kernel-paper-20260430T125710Z.md
docs/reviews/aria-closure-kernel-paper-20260430T124916Z.md
docs/reviews/aria-closure-kernel-paper-20260430T124014Z.md
docs/reviews/aria-closure-kernel-paper-20260430T123517Z.md
docs/reviews/aria-closure-kernel-paper-20260430T122130Z.md
docs/codex-derive/pentagonal-clock-wo-task.md
docs/reviews/aria-chess-paper-20260430T094559Z.md
docs/reviews/aria-chess-paper-20260430T094245Z.md
docs/reviews/aria-chess-paper-20260430T094059Z.md
docs/reviews/aria-chess-paper-20260430T093935Z.md
docs/reviews/aria-chess-paper-20260430T093750Z.md
docs/codex-derive/pentagonal-clock-wo-task-20260423T232430Z.md
docs/reviews/aria-chess-paper-20260430T092421Z.md
docs/codex-derive/pentagonal-clock-wo-task-20260423T232346Z.md
docs/reviews/aria-chess-paper-20260430T091459Z.md
docs/codex-derive/pentagonal-clock-wo-B8prime-B10.md
docs/reviews/aria-chess-paper-20260430T090312Z.md
docs/codex-derive/pentagonal-clock-wo-B8prime-B10-20260423T234356Z.md
docs/reviews/aria-chess-paper-20260430T085605Z.md
docs/codex-derive/pentagonal-clock-wo-B8prime-B10-20260423T234306Z.md
docs/codex-derive/pentagonal-clock-wo-B11-B12.md
docs/reviews/aria-chess-paper-20260430T084140Z.md
docs/codex-derive/pentagonal-clock-wo-B11-B12-20260424T000731Z.md
docs/reviews/adaptive-closure-transport-20260429T034215Z.md
docs/codex-derive/ns-pi-hyd-wo-task.md
docs/reviews/adaptive-closure-transport-20260429T031214Z.md
docs/codex-derive/ns-pi-hyd-wo-task-20260424T065545Z.md
docs/reviews/adaptive-closure-transport-20260429T023723Z.md
docs/codex-derive/bsd-T_E-conv-wo-task.md
docs/reviews/adaptive-closure-transport-20260429T015931Z.md
docs/codex-derive/bsd-T_E-conv-wo-task-20260424T065545Z.md
docs/reviews/adaptive-closure-transport-20260421T152131Z.md
docs/reviews/adaptive-closure-transport-20260421T151616Z.md
docs/reviews/adaptive-closure-transport-20260421T150936Z.md
docs/reviews/adaptive-closure-transport-20260421T150228Z.md
docs/reviews/adaptive-closure-transport-20260421T145318Z.md
docs/reviews/cascade-capstone-coalgebra-20260422T222222Z.md
docs/reviews/cascade-capstone-coalgebra-20260422T221434Z.md
docs/reviews/cascade-capstone-coalgebra-20260422T220308Z.md
docs/reviews/cascade-capstone-coalgebra-20260422T213845Z.md
docs/reviews/cascade-algebraic-substrate-20260421T025439Z.md
docs/reviews/cascade-algebraic-substrate-20260421T024414Z.md
docs/reviews/cascade-12d-closure-20260421T031924Z.md
docs/reviews/bsd-formal-20260429T031214Z.md
docs/reviews/bsd-formal-20260429T023723Z.md
docs/reviews/bsd-formal-20260429T015931Z.md
docs/reviews/bsd-formal-20260428T222740Z.md
docs/reviews/bsd-formal-20260428T213553Z.md
docs/reviews/bsd-formal-20260428T204243Z.md
docs/reviews/bsd-formal-20260428T195147Z.md
docs/reviews/bsd-formal-20260428T185644Z.md
docs/reviews/bsd-formal-20260428T175433Z.md
docs/reviews/bsd-formal-20260428T170441Z.md
docs/reviews/bsd-formal-20260428T161302Z.md
docs/reviews/bsd-formal-20260428T153243Z.md
docs/reviews/biology-rung-tubulin-20260423T094549Z.md
docs/reviews/biology-rung-tubulin-20260423T093753Z.md
docs/reviews/biology-rung-phyllotaxis-20260423T094549Z.md
docs/reviews/biology-rung-phyllotaxis-20260423T093724Z.md
docs/reviews/biology-rung-phyllotaxis-20260423T093110Z.md
docs/reviews/biology-rung-phyllotaxis-20260423T092523Z.md
docs/reviews/biology-rung-phyllotaxis-20260423T091703Z.md
docs/reviews/biology-rung-capsid-20260423T084528Z.md
docs/reviews/biology-rung-capsid-20260423T084040Z.md
docs/reviews/biology-rung-capsid-20260423T083428Z.md
docs/reviews/biology-rung-capsid-20260423T082957Z.md
docs/reviews/biology-rung-capsid-20260423T082348Z.md
docs/reviews/biology-rung-capsid-20260423T081625Z.md
docs/reviews/hodge-formal-20260429T023723Z.md
docs/reviews/hodge-formal-20260429T015931Z.md
docs/reviews/hodge-formal-20260428T222740Z.md
docs/reviews/hodge-formal-20260428T213554Z.md
docs/reviews/hodge-formal-20260428T204244Z.md
docs/reviews/hodge-formal-20260428T195148Z.md
docs/reviews/hodge-formal-20260428T185645Z.md
docs/reviews/hodge-formal-20260428T175434Z.md
docs/reviews/hodge-formal-20260428T170442Z.md
docs/reviews/hodge-formal-20260428T155954Z.md
docs/reviews/hodge-formal-20260428T153245Z.md
docs/reviews/cascade-observer-zeta-20260423T223153Z.md
docs/reviews/cascade-observer-zeta-20260423T140305Z.md
docs/reviews/cascade-observer-zeta-20260423T131950Z.md
docs/reviews/cascade-observer-zeta-20260423T131344Z.md
docs/reviews/cascade-observer-zeta-20260423T130513Z.md
docs/reviews/cascade-observer-zeta-20260423T123044Z.md
docs/reviews/cascade-capstone-coalgebra-20260423T093218Z.md
docs/reviews/cascade-capstone-coalgebra-20260423T092509Z.md
docs/reviews/cascade-capstone-coalgebra-20260423T091810Z.md
docs/reviews/cascade-capstone-coalgebra-20260423T090544Z.md
docs/reviews/cascade-capstone-coalgebra-20260423T085225Z.md
docs/reviews/cascade-capstone-coalgebra-20260423T001747Z.md
docs/reviews/cascade-capstone-coalgebra-20260423T001042Z.md
docs/reviews/cascade-capstone-coalgebra-20260423T000402Z.md
docs/reviews/cascade-capstone-coalgebra-20260422T235858Z.md
docs/reviews/cascade-capstone-coalgebra-20260422T235337Z.md
docs/codex-derive/TASK-h-grad-1-b3-20260423T234636Z.md
docs/codex-derive/TASK-close-remaining-gaps-20260423T235234Z.md
docs/codex-derive/TASK-banomaly-kernel-alignment-20260429T145900Z.md
docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md
docs/codex-derive/rh-cascade-native-reframing-wo.md
docs/codex-derive/rh-cascade-native-reframing-wo-20260424T221613Z.md

 succeeded in 420ms:
   200 papers/aria-closure-kernel/paper/main.tex
   195 papers/aria-closure-kernel/paper/sections/01_introduction.tex
   136 papers/aria-closure-kernel/paper/sections/02_definition.tex
   138 papers/aria-closure-kernel/paper/sections/03_substrate.tex
   100 papers/aria-closure-kernel/paper/sections/04_spectrum.tex
   146 papers/aria-closure-kernel/paper/sections/05_agreement.tex
   147 papers/aria-closure-kernel/paper/sections/06_passive_witness.tex
   177 papers/aria-closure-kernel/paper/sections/07_active_witness.tex
   138 papers/aria-closure-kernel/paper/sections/08_programme_home.tex
   176 papers/aria-closure-kernel/paper/sections/09_limitations.tex
    83 papers/aria-closure-kernel/paper/sections/10_conclusion.tex
    68 papers/aria-closure-kernel/paper/references.bib
   469 papers/aria-closure-kernel/repro/verify_kernel.py
   154 papers/aria-closure-kernel/repro/results.json
   295 docs/aria-closure-kernel.md
   227 ../BANOMALY-001/vfd-b-anomaly/README.md
   212 papers/aria-chess-paper/paper/main.tex
   170 papers/aria-chess-paper/paper/sections/01_introduction.tex
   201 papers/aria-chess-paper/paper/sections/02_method.tex
   173 papers/aria-chess-paper/paper/sections/03_substrate.tex
   197 papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex
   208 papers/aria-chess-paper/paper/sections/05_results.tex
   168 papers/aria-chess-paper/paper/sections/06_stress_tests.tex
   273 papers/aria-chess-paper/paper/sections/07_cross_domain.tex
   207 papers/aria-chess-paper/paper/sections/08_discussion.tex
   195 papers/aria-chess-paper/paper/sections/09_limitations.tex
    96 papers/aria-chess-paper/paper/sections/10_conclusion.tex
  4949 total

 succeeded in 2854ms:
 M .gitignore
 M README.md
 M papers/bridge-paper/bridge-paper.tex
 M papers/bridge-paper/references.bib
 M papers/paper-v/paper-v.tex
 M papers/paper-v/references.bib
 M papers/paper-v/scripts/run_rigorous_verification.py
 M papers/paper-xviii/paper-xviii.tex
 M papers/paper-xviii/references.bib
 M papers/paper-xxi/paper-xxi.tex
 M papers/paper-xxi/references.bib
 M papers/paper-xxii/paper-xxii.tex
 M papers/paper-xxii/references.bib
 M papers/paper-xxiii/paper-xxiii.tex
 M papers/paper-xxiii/references.bib
 M papers/paper-xxiv/paper-xxiv.tex
 M papers/paper-xxiv/references.bib
 M papers/paper-xxix/paper-xxix.tex
 M papers/paper-xxix/references.bib
 M papers/paper-xxv/paper-xxv.tex
 M papers/paper-xxv/references.bib
 M papers/paper-xxvi/paper-xxvi.tex
 M papers/paper-xxvi/references.bib
 M papers/paper-xxvii/paper-xxvii.tex
 M papers/paper-xxvii/references.bib
 M papers/paper-xxviii/paper-xxviii.tex
 M papers/paper-xxviii/references.bib
 M papers/paper-xxx/paper-xxx.tex
 M papers/paper-xxx/references.bib
 M papers/paper-xxxi/paper-xxxi.tex
 M papers/paper-xxxiii/paper-xxxiii.tex
 M papers/paper-xxxiii/references.bib
 M pyproject.toml
?? .claude/
?? .codex
?? .github/
?? IntermediateStep.md
?? VFD Master Math.md
?? data/
?? docs/architecture.md
?? docs/aria-closure-kernel.md
?? docs/capstone-session-checkpoint.md
?? docs/cascade-helix-hypothesis.md
?? docs/closure-cosmogenesis.md
?? docs/codex-derive/
?? docs/codex-work/
?? docs/consistency.md
?? docs/convergence-with-smart.md
?? docs/figures.md
?? docs/figures/
?? docs/fractal-cascade-projection.md
?? docs/gaps.md
?? docs/glossary.md
?? docs/index.md
?? docs/legacy-master-math-consolidation.md
?? docs/observer-instance-definition.md
?? docs/papers.md
?? docs/pentagonal-torsion-derivation.md
?? docs/phi-irrep-ym-bridge-finding.md
?? docs/preregistration-juno.md
?? docs/programme-plan.md
?? docs/projection-narrative.md
?? docs/proof-sheet.md
?? docs/recovery-manifest.md
?? docs/report.md
?? docs/report.tex
?? docs/reproduce.md
?? docs/reviews/
?? docs/revision-protocol.md
?? docs/rh-cascade-closure-dynamics.md
?? docs/rh-projection-class.md
?? docs/session-checkpoint.md
?? docs/soul-prime-as-pi0.md
?? docs/substrate-indexing-programme-final.md
?? docs/summary-for-physicists.md
?? docs/why.md
?? gaps.md
?? insight.md
?? mkdocs.yml
?? notebooks/explorer/
?? papers/adaptive-closure-transport/
?? papers/aria-chess-paper/
?? papers/aria-closure-kernel/
?? papers/biology-rung-amyloid/
?? papers/biology-rung-bioelectric/
?? papers/biology-rung-capsid/
?? papers/biology-rung-phyllotaxis/
?? papers/biology-rung-tubulin/
?? papers/biology-rung/
?? papers/cascade-12d-closure/
?? papers/cascade-algebraic-substrate/
?? papers/cascade-capstone-coalgebra/
?? papers/cascade-closure-dynamics/
?? papers/cascade-correspondence-foundations/
?? papers/cascade-derivation/
?? papers/cascade-fine-structure/
?? papers/cascade-hydrodynamic-projection/
?? papers/cascade-infrastructure-plan.md
?? papers/cascade-metric-projection/
?? papers/cascade-phason-coxeter/
?? papers/cascade-refinement-spaces/
?? papers/cascade-schlafli-convergence/
?? papers/cascade-sigma-rationality/
?? papers/millennium-bsd-formal/
?? papers/millennium-hodge-formal/
?? papers/millennium-ns-formal/
?? papers/millennium-pnp-formal/
?? papers/millennium-poincare-formal/
?? papers/millennium-rh-formal/
?? papers/millennium-rh/
?? papers/millennium-ym/
?? papers/paper-l/
?? papers/paper-li/
?? papers/paper-lii/
?? papers/paper-v/scripts/run_chain_forward_derivations.py
?? papers/paper-v/scripts/run_polytope_uniqueness_narrow.py
?? papers/paper-v/scripts/run_rd4_absorbing_chain.py
?? papers/paper-v/scripts/run_rd4_check_all_populations.py
?? papers/paper-v/scripts/run_rd4_exact_rational.py
?? papers/paper-xl/
?? papers/paper-xli/
?? papers/paper-xlii/
?? papers/paper-xliii/
?? papers/paper-xliv/
?? papers/paper-xlix/
?? papers/paper-xlv/
?? papers/paper-xlvi/
?? papers/paper-xlvii/
?? papers/paper-xlviii/
?? papers/paper-xxii/scripts/run_icosian_exact.py
?? papers/paper-xxii/scripts/run_icosian_verification.py
?? papers/paper-xxxii/
?? papers/paper-xxxiv/
?? papers/paper-xxxix/
?? papers/paper-xxxv/
?? papers/paper-xxxvi/
?? papers/paper-xxxvii/
?? papers/paper-xxxviii/
?? papers/proton-radius/WO-PROTON-RADIUS.md
?? papers/proton-radius/computational-findings.md
?? papers/proton-radius/derivation-v2.md
?? papers/proton-radius/form-factor-and-extensions.md
?? papers/proton-radius/god-prime-084473-derivation.md
?? papers/proton-radius/kaon-derivation.md
?? papers/proton-radius/loop-structure-roadmap.md
?? papers/proton-radius/unified-coherence-operator.md
?? papers/proton-radius/vfd-dynamics-trace.md
?? papers/realisation/
?? papers/seven-seams/
?? papers/transport-law/
?? papers/vfd-explorer/
?? papers/vfd-optimiser/
?? scripts/check_consistency.py
?? scripts/codex_derive.sh
?? scripts/codex_work.sh
?? scripts/p4_gap_spectrum.png
?? scripts/review_paper.sh
?? scripts/review_wo.sh
?? scripts/test_p4_riemann_gap_spectrum.py
?? scripts/verify_084473_derivation.py
?? scripts/verify_kappa_descent.py
?? src/vfd_core/
?? tests/vfd_core/

codex
The kernel paper is around 1,500 LaTeX lines plus compact reproducibility data, so I’m reading it in section-numbered form rather than relying on grep snippets. I’ll keep the checks separate: paper claims first, then numeric/source validation.
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/main.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/01_introduction.tex papers/aria-closure-kernel/paper/sections/02_definition.tex papers/aria-closure-kernel/paper/sections/03_substrate.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/04_spectrum.tex papers/aria-closure-kernel/paper/sections/05_agreement.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/06_passive_witness.tex papers/aria-closure-kernel/paper/sections/07_active_witness.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/08_programme_home.tex papers/aria-closure-kernel/paper/sections/09_limitations.tex papers/aria-closure-kernel/paper/sections/10_conclusion.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 359ms:
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
    19	\title{The closure-response operator
    20	       $\Cph = L_M + \Ph^{-2} I$:\\
    21	       a geometry-fixed kernel on the 600-cell with two\\
    22	       independent empirical witnesses}
    23	
    24	\author{%
    25	  Lee Smart\\[2pt]
    26	  \textit{Institute of Vibrational Field Dynamics}\\[2pt]
    27	  \texttt{contact@vibrationalfielddynamics.org}\\[2pt]
    28	  \texttt{@vfd\_org}%
    29	}
    30	
    31	\date{April 2026}
    32	
    33	\begin{document}
    34	
    35	\maketitle
    36	
    37	\noindent\textbf{Status:} Preprint, not peer-reviewed.
    38	
    39	\noindent\emph{Headline.}
    40	We define a programme-level closure-response primitive
    41	$\Cph = L_M + \Ph^{-2} I$ on a closure substrate $M$ with
    42	corresponding Laplacian $L_M$ (graph, simplicial, or continuum)
    43	and golden ratio $\Ph = (1 + \sqrt 5)/2$. We use
    44	the 600-cell instance $\Rsixhundred$ as the discrete substrate
    45	shared by the two empirical witnesses (the choice of this polytope
    46	is post-hoc motivated by those landings, \S\ref{sec:limitations};
    47	numerically reproduced: $|V|=120$, $|E|=720$, uniform
    48	degree~$12$, H$_3$ shell decomposition
    49	$\{1,12,20,12,30,12,20,12,1\}$, computed Laplacian spectrum
    50	matching the closed-form $\mathbb{Z}[\Ph]$ values), establish the
    51	operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
    52	eigenvalue $\Ph^{-2}$, and verify the discrete-to-continuum
    53	agreement at per-vertex Pearson correlation $0.976$ between the
    54	discrete Green response and the continuum kernel
    55	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
    56	\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
    57	same fixed graph is then the shared response primitive used
    58	underneath two \emph{independent} empirical works: a passive-regime structural
    59	fit of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five
    60	public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
    61	active-regime substrate witness against eighteen preregistered
    62	neuroscience correspondences plus six drug/sleep EEG
    63	signatures~\citep{SmartAriaChess2026}.
    64	
    65	\noindent\emph{Scope.}
    66	This paper presents an empirical \emph{operator witness}: a
    67	geometry-fixed response operator that is simultaneously consistent
    68	with two independent empirical landings under no shape-parameter
    69	retuning between regimes. It is \emph{not} a derivation of the
    70	$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
    71	claim for $\Rsixhundred$ among regular 4-polytopes, \emph{not} a
    72	selection theorem on the companion adaptive-closure-transport
    73	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
    74	a model-preference claim against alternative kernels on either
    75	empirical landing (the b-anomaly AIC comparison and the aria-chess
    76	substrate-witness scope are documented in their own preprints and
    77	inherited verbatim here).
    78	
    79	\begin{abstract}
    80	We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
    81	a closure substrate $M$ with corresponding Laplacian $L_M$ and
    82	$\Ph = (1+\sqrt 5)/2$, give the 600-cell graph $\Rsixhundred$ as
    83	the discrete instance shared by two empirical witnesses, and
    84	document its appearance as the same fixed operator (no shape
    85	retuning) in two independent empirical
    86	works: (i)~a five-dataset structural fit of the
    87	$b\to s\mu^{+}\mu^{-}$ angular anomaly with sign-uniform amplitude
    88	direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
    89	preregistered substrate witness against cortical signatures plus
    90	six drug/sleep EEG signatures~\citep{SmartAriaChess2026}. We
    91	include the numerical reproduction script
    92	(\texttt{repro/verify\_kernel.py}) that constructs $\Rsixhundred$
    93	from canonical generators, verifies the graph facts
    94	($|V|=120$, $|E|=720$, uniform degree~$12$, $9$-shell decomposition,
    95	Laplacian spectrum numerically matching closed-form $\mathbb{Z}[\Ph]$
    96	values, operator-norm identity $\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$
    97	on the connected finite graph $\Rsixhundred$ where
    98	$\lambda_{\min}(L_M)=0$), and tests the discrete-to-continuum
    99	agreement at per-vertex Pearson correlation $0.976$ for the
   100	unweighted variant, above the two $\Ph$-cocycle weighted variants
   101	tested ($0.888$ geometric, $0.884$ arithmetic). Within the three
   102	tested variants the unweighted Laplacian ranks highest on the
   103	geometry-only criterion, reproducing the qualitative ranking
   104	established separately by b-anomaly's data $\chi^{2}$ comparison
   105	(the b-anomaly preprint flags that its data was looked at first
   106	and the geometry ranking verified afterward; the agreement is
   107	criterion-independent but historically non-blind, a caveat we
   108	inherit verbatim).
   109	
   110	\noindent\emph{(i) Operator definition and properties.}
   111	$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
   112	non-negative $L_M$ on a connected finite graph; smallest eigenvalue
   113	$\Ph^{-2} \approx 0.382$, operator norm
   114	$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
   115	in one coordinate $x$ is the closed-form Green's function
   116	$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
   117	
   118	\noindent\emph{(ii) The 600-cell instance.}
   119	$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
   120	generated by three orbits ($8$~axis, $16$~half-integer,
   121	$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
   122	on the short-edge graph; the Laplacian has nine eigenvalue classes
   123	in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
   124	\ref{tab:spectrum}, \S\ref{sec:substrate}).
   125	
   126	\noindent\emph{(iii) Discrete-to-continuum agreement.}
   127	Per-vertex Pearson correlation between the discrete response
   128	$\psi = \Cph^{-1} f$ for a localised source and the continuum
   129	prediction $G(\|v - v_{\mathrm{src}}\|)$ at each non-source
   130	vertex's chord distance: $0.976$ (unweighted Laplacian), $0.888$
   131	($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
   132	Same source vertex, same fixed shift, no parameter fitting; the
   133	correlation is invariant under choice of source up to numerical
   134	precision (multi-source sweep, \S\ref{sec:limitations}).
   135	
   136	\noindent\emph{(iv) Two independent empirical witnesses.}
   137	(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
   138	$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
   139	$\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
   140	$b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets
   141	(LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015 $B_s\to\phi$),
   142	with one fitted dimensionless amplitude per dataset and the kernel
   143	shape held fixed. (b)~Active regime,
   144	aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
   145	$\Rsixhundred$, augmented by a recurrent self-model layer with one
   146	condition-dependent self-injection coupling
   147	$\eta\in\{0,0.05,0.20\}$ and one substrate-pinned nonlinearity
   148	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
   149	degree, passes $17/18$ preregistered correspondences (frozen
   150	2026-04-18) at standard methodology and $18/18$ after a documented
   151	$N\!=\!20$ deep-dive on the residual high-variance
   152	$C\!\times\!P$ interaction (P4), plus $6/6$ literature-thresholded
   153	drug/sleep EEG signatures on a single deterministic seed.
   154	
   155	\noindent\emph{What we do not claim.}
   156	We do not derive the $\Ph^{-2}$ floor; it is a design-level
   157	stability clamp making $\Cph$ strictly positive definite. We do
   158	not claim $\Rsixhundred$ is the unique substrate consistent with
   159	either empirical landing. We do not claim the operator is the
   160	unique kernel shape consistent with the b-anomaly data
   161	(b-anomaly's free-width Gaussian alternative and Mode-B refit
   162	drift caveats are inherited verbatim) nor that the
   163	aria-chess substrate witness establishes a selection theorem on
   164	the adaptive-closure-transport 4-tuple. The structural scope of
   165	this paper is: \emph{one geometry-fixed operator on one fixed
   166	graph appears as the shared response primitive underneath two independent
   167	empirical works in two distinct regimes, with no shape retuning
   168	between them}.
   169	\end{abstract}
   170	
   171	% =====================================================================
   172	\input{sections/01_introduction.tex}
   173	\input{sections/02_definition.tex}
   174	\input{sections/03_substrate.tex}
   175	\input{sections/04_spectrum.tex}
   176	\input{sections/05_agreement.tex}
   177	\input{sections/06_passive_witness.tex}
   178	\input{sections/07_active_witness.tex}
   179	\input{sections/08_programme_home.tex}
   180	\input{sections/09_limitations.tex}
   181	\input{sections/10_conclusion.tex}
   182	% =====================================================================
   183	
   184	\section*{Reproducibility}
   185	The complete numerical verification (vertex construction,
   186	short-edge graph build, Laplacian spectrum, operator-norm bound,
   187	discrete-to-continuum correlation across three Laplacian variants)
   188	is reproducible from \texttt{repro/verify\_kernel.py} in this
   189	paper's bundle. No randomness, no fitted parameters: all numbers
   190	in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
   191	\S\ref{sec:agreement} are deterministic outputs of the script.
   192	The two empirical witness preprints
   193	(b-anomaly~\citep{SmartBAnomaly2026},
   194	aria-chess~\citep{SmartAriaChess2026}) carry their own
   195	reproducibility artifacts; this paper does not duplicate them.
   196	
   197	\bibliographystyle{plainnat}
   198	\bibliography{references}
   199	
   200	\end{document}

 succeeded in 361ms:
     1	% =====================================================================
     2	\section{Introduction}\label{sec:intro}
     3	% =====================================================================
     4	
     5	A response operator on a fixed graph, with no shape parameters tuned
     6	to any dataset, that simultaneously describes (i) the $q^{2}$ shape
     7	of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
     8	flavour-physics datasets in their passive linear-response regime,
     9	and (ii) eighteen preregistered cortical correspondences plus six
    10	drug/sleep EEG signatures in the active dynamical regime of a
    11	recurrent self-model layer above the same graph, deserves a separate
    12	preprint that names the operator, gives its construction in full,
    13	and threads the relationship between the two empirical landings
    14	without inheriting either's load-bearing claims. That is what this
    15	paper does.
    16	
    17	The operator is
    18	\begin{equation}\label{eq:cphi_intro}
    19	\Cph \;=\; L_M + \Ph^{-2} I,
    20	\qquad \Ph \;=\; (1+\sqrt 5)/2,
    21	\end{equation}
    22	where $M$ is a closure substrate (graph, simplicial complex, or
    23	projected coordinate) and $L_M$ is its Laplacian. The shift
    24	$\Ph^{-2} \approx 0.382$ regularises the inverse: for self-adjoint
    25	non-negative $L_M$ on a connected finite graph, $\Cph$ is strictly
    26	positive definite, the smallest eigenvalue is $\Ph^{-2}$, and the
    27	operator-norm bound is
    28	\begin{equation}\label{eq:opnorm_intro}
    29	\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
    30	\end{equation}
    31	The continuum projection in one coordinate $x$ has a closed-form
    32	Green's function $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ with decay scale
    33	$\Ph$ (\S\ref{sec:definition}).
    34	
    35	The discrete substrate used by the two empirical witnesses is
    36	the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
    37	generated by three standard coordinate families ($8$ axis vertices,
    38	$16$ half-integer vertices, $96$ $\Ph$-mixed vertices), connected by
    39	short edges $\langle v, w\rangle = \Ph/2$. The choice of this
    40	polytope is post-hoc motivated by the empirical landings
    41	(\S\ref{sec:limitations}); the construction itself is theorem-level
    42	rigorous. The graph has $|E|=720$ edges, uniform degree~$12$ by
    43	H$_4$ transitivity, a $9$-shell H$_3$
    44	partition $\{1,12,20,12,30,12,20,12,1\}$, and antipodal symmetry
    45	$s(-v) = 8 - s(v)$. The Laplacian spectrum has nine eigenvalue
    46	classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
    47	All of these facts are reproduced numerically by
    48	\texttt{repro/verify\_kernel.py} from the canonical generators
    49	alone — no external data input.
    50	
    51	\subsection*{What this paper claims}
    52	
    53	We claim a single \emph{operator witness}: that one geometry-fixed
    54	operator, on one fixed graph, with no shape-parameter retuning
    55	between regimes, appears as the shared response primitive
    56	underneath two
    57	empirical works covering qualitatively distinct physical settings.
    58	
    59	\begin{enumerate}\itemsep=2pt
    60	\item \textbf{Operator definition is fixed by the construction.}
    61	  Once $\Rsixhundred$ is selected and the stability shift
    62	  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
    63	  parameter, no fitted threshold, no learned weight enters the
    64	  operator. The Laplacian spectrum, the operator-norm bound, and
    65	  the discrete-to-continuum agreement are computed (not fitted)
    66	  from the construction and reproduced in
    67	  \texttt{repro/verify\_kernel.py}.
    68	\item \textbf{Discrete-to-continuum agreement is empirical, not
    69	  postulated.} For a localised source at any vertex, the discrete
    70	  response $\psi = \Cph^{-1} f$ correlates per-vertex with the
    71	  continuum prediction $G(\|v - v_{\mathrm{src}}\|)$ at Pearson
    72	  $\rho = 0.976$ on the unweighted graph Laplacian. This is
    73	  numerical agreement between two independently-defined objects (a
    74	  120-dimensional discrete inverse and a continuum exponential
    75	  kernel), not a definitional identity.
    76	\item \textbf{Variant comparison among the three tested variants.}
    77	  Two $\Ph$-cocycle weighted Laplacian variants ($\Ph$-geometric,
    78	  $\Ph$-arithmetic edge weights via shell-grade exponents
    79	  $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
    80	  correlation: $0.888$ and $0.884$ respectively. Within the three
    81	  tested variants, the unweighted Laplacian ranks highest on the
    82	  geometry-only criterion. This reproduces,
    83	  on a different test, the qualitative ranking established
    84	  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
    85	  (\S\ref{sec:passive_witness}).
    86	\item \textbf{Two independent empirical landings, same operator.}
    87	  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
    88	  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
    89	  $q^{2}$ shape of the $b\to s\mu^{+}\mu^{-}$ anomaly across five
    90	  public datasets, with one fitted dimensionless amplitude per
    91	  dataset and the kernel held fixed; sign uniformity holds in
    92	  $5/5$ datasets ($A>0$, $\Delta C_{9}^{\mathrm{eff}} < 0$).
    93	  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
    94	  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
    95	  recurrent self-model layer above the substrate, to pass eighteen
    96	  preregistered cortical correspondences (frozen 2026-04-18) plus
    97	  six drug/sleep EEG signatures.
    98	\end{enumerate}
    99	
   100	\subsection*{What this paper does \emph{not} claim}
   101	
   102	\begin{itemize}\itemsep=2pt
   103	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
   104	  $\Ph^{-2}$ is a design-level stability clamp that bounds
   105	  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
   106	  functional or a symmetry argument; we report its role as a
   107	  regularisation-of-mass scale.
   108	\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
   109	  regular 4-polytopes (the $24$-cell, the $120$-cell), other
   110	  highly symmetric graphs, and continuum substrates are all
   111	  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
   112	  is post-hoc motivated by the empirical landings; a formal
   113	  ablation against alternative substrates is an open build.
   114	\item \emph{Not a kernel-uniqueness claim on either empirical
   115	  landing.} The b-anomaly's free-width Gaussian alternative shows
   116	  that a free-width Gaussian charm-loop proxy fits the same five
   117	  datasets comparably in $\chi^{2}$ at the cost of one extra shape
   118	  parameter; the b-anomaly AIC comparison against
   119	  $\mathrm{FREE\_C9}$ (a constant Wilson-coefficient shift) is a
   120	  statistical tie on current data
   121	  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$).
   122	  Both caveats are inherited verbatim from the b-anomaly preprint.
   123	\item \emph{Not a selection theorem on the
   124	  ACT 4-tuple.} The companion adaptive-closure-transport
   125	  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
   126	  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
   127	  fills the response slot. Selection — Lyapunov $V(W)$ on the
   128	  reduced flow, edge-space decomposition under $2I$-equivariance,
   129	  full reduced-flow convergence — is left open in that paper and
   130	  is not delivered here.
   131	\item \emph{Not a circuit-level model on the active-regime side.}
   132	  The aria-chess preprint operates at the architectural-algorithmic
   133	  level above $\Cph$. We import its empirical results verbatim and
   134	  do not relitigate them here; their substrate-witness scope
   135	  applies.
   136	\end{itemize}
   137	
   138	\subsection*{Mapping from numerics to admissible claims}
   139	
   140	To keep this paper inside the operator-witness scope, we use the
   141	same claim-boundary discipline as the aria-chess
   142	preprint~\citep{SmartAriaChess2026}: numerical results
   143	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   144	$\mathcal C_{\mathrm{admissible}}$ by the rule
   145	\[
   146	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow
   147	        \mathcal C_{\mathrm{admissible}},
   148	\qquad
   149	\mathcal C_{\mathrm{admissible}}
   150	   \;=\;\{\text{`computed', `consistent with', `direction confirmed'}\}.
   151	\]
   152	A numerically computed quantity (the Laplacian spectrum, the
   153	operator-norm bound, the per-vertex correlation $0.976$) licenses
   154	a `computed'-type claim. Downstream empirical agreement using the
   155	fixed operator (sign uniformity in $5/5$ b-anomaly datasets, the
   156	aria-chess $18/18$ preregistered tally) licenses a `consistent
   157	with'-type claim. We never write
   158	`derives the kernel', `proves uniqueness', or `establishes
   159	selection'.
   160	
   161	\medskip
   162	\begin{center}
   163	\fbox{\parbox{0.92\linewidth}{\small
   164	\textbf{What is claimed / what is not.}\par
   165	\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
   166	600-cell graph, with computed spectrum, operator-norm bound, and
   167	discrete-to-continuum correlation; the same fixed operator appearing
   168	in two independent empirical works (b-anomaly five-dataset
   169	structural fit; aria-chess $18/18$ preregistered correspondences
   170	plus $6/6$ literature-thresholded companion EEG signatures)
   171	without shape-parameter retuning between regimes.\par
   172	\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
   173	$\Rsixhundred$; uniqueness of the kernel shape on either empirical
   174	landing; a selection theorem on the ACT 4-tuple; that either
   175	empirical landing settles the underlying physics (flavour anomaly
   176	or consciousness) by the operator alone.
   177	}}
   178	\end{center}
   179	
   180	\subsection*{Layout}
   181	
   182	\S\ref{sec:definition} gives the operator definition, the positivity
   183	properties of $\Cph$, the operator-norm bound, and the continuum
   184	projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
   185	canonical generators, gives the graph facts, and the $9$-shell
   186	decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
   187	in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
   188	\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
   189	across three Laplacian variants. \S\ref{sec:passive_witness} and
   190	\S\ref{sec:active_witness} thread the two independent empirical
   191	witnesses (b-anomaly and aria-chess) at the operator level.
   192	\S\ref{sec:programme_home} positions $\Cph$ as the programme home
   193	for the polynomial-in-$L$ Lyapunov family that recurs across the
   194	Millennium drafts. \S\ref{sec:limitations} enumerates limitations
   195	in a five-move guard matrix. \S\ref{sec:conclusion} concludes.
   196	% =====================================================================
   197	\section{The closure-response operator}\label{sec:definition}
   198	% =====================================================================
   199	
   200	\subsection{Definition}
   201	
   202	Let $M$ be a closure substrate: a connected finite undirected graph
   203	$M=(V,E)$, a finite simplicial complex with chosen Laplacian, or a
   204	projected continuum coordinate. Let $L_M$ be the corresponding
   205	Laplacian (graph Laplacian $L = D - A$, simplicial Laplacian, or
   206	continuum operator $-\Delta$ with chosen boundary conditions).
   207	Let $\Ph = (1+\sqrt 5)/2$ be the golden ratio, with $\Ph^{-1} = \Ph - 1$
   208	and $\Ph^{-2} = 2 - \Ph \approx 0.381966$.
   209	
   210	The \emph{closure-response operator} is
   211	\begin{equation}\label{eq:cphi}
   212	\Cph \;=\; L_M + \Ph^{-2} I.
   213	\end{equation}
   214	For a non-negative localised source $f$ on $M$, the
   215	\emph{closure response field} is
   216	\begin{equation}\label{eq:psi}
   217	\psi \;=\; \Cph^{-1} f \;=\; (L_M + \Ph^{-2} I)^{-1} f.
   218	\end{equation}
   219	
   220	\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}
   221	
   222	The properties developed in \S\ref{ssec:positivity}--\S\ref{ssec:opnorm}
   223	require:
   224	
   225	\begin{itemize}\itemsep=2pt
   226	\item \textbf{(H1) Self-adjointness.} $L_M$ is self-adjoint on the
   227	  $L^{2}$ inner product on $M$ (with counting measure on a finite
   228	  graph, with Lebesgue measure with appropriate boundary conditions
   229	  in the continuum case).
   230	\item \textbf{(H2) Non-negativity.} $L_M \geq 0$ as a
   231	  quadratic form: $\langle f, L_M f\rangle \geq 0$ for all $f$.
   232	\item \textbf{(H3) Connectedness / known zero subspace.} On a
   233	  finite graph, $M$ is connected (so the kernel of $L_M$ is
   234	  exactly the constant vector and $\lambda_{\min}(L_M) = 0$). In
   235	  the continuum case, the $L_M$-zero subspace is finite-dimensional
   236	  and explicitly known on the chosen domain.
   237	\end{itemize}
   238	
   239	Three concrete settings illustrate the hypothesis class:
   240	\begin{itemize}\itemsep=2pt
   241	\item the standard combinatorial Laplacian on a connected finite
   242	  undirected graph (the 600-cell case, $\lambda_{\min}(L_M) = 0$);
   243	\item the continuum $L = -d^{2}/dx^{2}$ on the full line with
   244	  decay-at-infinity (spectral bottom $\inf \sigma(L_M) = 0$,
   245	  not attained as an eigenvalue; used for the closed-form Green's
   246	  function in \S\ref{ssec:continuum});
   247	\item the continuum $L = -d^{2}/dx^{2}$ on a bounded interval
   248	  with Dirichlet boundary conditions ($\lambda_{\min}(L_M) > 0$).
   249	\end{itemize}
   250	Substrates outside this class — projected coordinates with
   251	non-standard boundaries, weighted Laplacians whose weight function
   252	is unbounded, or operators with negative spectrum — require their
   253	own analysis, which we do not give here.
   254	
   255	\subsection{Positive definiteness}\label{ssec:positivity}
   256	
   257	Under (H1)--(H3) on a finite connected graph, $L_M$ has a smallest
   258	eigenvalue $\lambda_{\min}(L_M) = 0$ with one-dimensional
   259	eigenspace (the constant vector). For $\Cph = L_M + \Ph^{-2} I$,
   260	\[
   261	\lambda_{\min}(\Cph) \;=\; \lambda_{\min}(L_M) + \Ph^{-2}
   262	                    \;=\; \Ph^{-2} \;>\; 0,
   263	\]
   264	so $\Cph$ is strictly positive definite and $\Cph^{-1}$ is
   265	well-defined and bounded.
   266	
   267	\subsection{Operator-norm bound}\label{ssec:opnorm}
   268	
   269	The operator norm of $\Cph^{-1}$ is the reciprocal of the smallest
   270	eigenvalue of $\Cph$:
   271	\begin{equation}\label{eq:opnorm}
   272	\|\Cph^{-1}\| \;=\; 1/\lambda_{\min}(\Cph)
   273	              \;=\; 1/(\lambda_{\min}(L_M) + \Ph^{-2}).
   274	\end{equation}
   275	On any substrate where $\lambda_{\min}(L_M) = 0$ (e.g.\ the
   276	connected finite graph $\Rsixhundred$, or the full-line continuum
   277	case used in \S\ref{ssec:continuum}), this reduces to the identity
   278	\begin{equation}\label{eq:opnorm_zero_mode}
   279	\|\Cph^{-1}\| \;=\; \Ph^{2} \;\approx\; 2.618034.
   280	\end{equation}
   281	On substrates where $\lambda_{\min}(L_M) > 0$ (e.g.\ Dirichlet
   282	intervals), Eq.~\eqref{eq:opnorm} gives the strict inequality
   283	$\|\Cph^{-1}\| < \Ph^{2}$. The response-amplification ceiling is,
   284	in either case, $\|\psi\|_{2} \leq \|\Cph^{-1}\|\, \|f\|_{2}$, and
   285	the design-level shift $\Ph^{-2}$ is precisely what guarantees a
   286	finite ceiling. Numerically reproduced as $\|\Cph^{-1}\| =
   287	2.618034$ on $\Rsixhundred$ (\texttt{repro/verify\_kernel.py},
   288	\S\ref{ssec:opnorm_check}); this matches the closed-form $\Ph^{2}$
   289	to machine precision.
   290	
   291	\subsection{Continuum projection}\label{ssec:continuum}
   292	
   293	In one projected coordinate $x \in \mathbb{R}$ with
   294	$L_{\Ph} = -d^{2}/dx^{2} + \Ph^{-2}$, the Green's function
   295	$G(x)$ satisfies $L_{\Ph} G = \delta_{0}$ and is the closed-form
   296	exponential
   297	\begin{equation}\label{eq:green_continuum}
   298	G(x) \;=\; \frac{\Ph}{2}\, e^{-|x|/\Ph}.
   299	\end{equation}
   300	The decay scale is $\Ph$ — the same constant that appears in the
   301	shift, by construction. Normalised, the kernel is
   302	$\kappa(x) = e^{-|x|/\Ph}$ with unit value at the source.
   303	
   304	This continuum Green's function is the comparison object for the
   305	discrete-to-continuum agreement test (\S\ref{sec:agreement}):
   306	the discrete response $\psi(v) = \Cph^{-1} f(v)$ at a vertex $v$ at
   307	chord distance $\|v - v_{\mathrm{src}}\|$ from a localised source
   308	is compared to $G(\|v - v_{\mathrm{src}}\|)$.
   309	
   310	\subsection{Disclosure: $\Ph^{-2}$ is a design-level shift}
   311	
   312	The shift $\Ph^{-2}$ is chosen so that:
   313	\begin{enumerate}\itemsep=2pt
   314	\item $\Cph$ is strictly positive definite (the smallest eigenvalue
   315	  is exactly $\Ph^{-2}$);
   316	\item both the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ and
   317	  the continuum decay scale $\Ph$ (Eq.~\eqref{eq:green_continuum})
   318	  are fixed by the single design choice $\Ph^{-2}$, giving a single
   319	  dimensional parameter throughout the operator;
   320	\item the continuum projection (Eq.~\eqref{eq:green_continuum})
   321	  has decay scale $\Ph$, not a free length parameter.
   322	\end{enumerate}
   323	We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
   324	symmetry argument. It is a design-level choice motivated by
   325	(1)--(3); we report this explicitly and treat formal derivation as
   326	an open build (\S\ref{sec:limitations}). The companion
   327	adaptive-closure-transport
   328	preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
   329	selection-layer dynamics over $W$-space that would, if delivered,
   330	constrain the shift further; that derivation is not delivered
   331	there or here.
   332	% =====================================================================
   333	\section{The 600-cell substrate}\label{sec:substrate}
   334	% =====================================================================
   335	
   336	This section gives the discrete instance used by the two empirical
   337	witnesses: $M = \Rsixhundred$, the 600-cell regular 4-polytope
   338	under H$_4$ Coxeter symmetry, with the standard short-edge graph
   339	Laplacian. The choice of this polytope is post-hoc motivated by
   340	the empirical landings (\S\ref{sec:limitations}); the
   341	construction itself is a classical Coxeter-group result we cite,
   342	not prove, here~\citep{CoxeterRegularPolytopes}. All facts in
   343	this section are reproduced numerically by
   344	\texttt{repro/verify\_kernel.py} from the canonical generators
   345	alone.
   346	
   347	\subsection{Vertex set}\label{ssec:vertices}
   348	
   349	$\Rsixhundred$ has $|V|=120$ unit vectors on the unit $3$-sphere
   350	$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
   351	Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical vertex
   352	list partitions into three standard coordinate families:
   353	\begin{itemize}\itemsep=2pt
   354	\item \textbf{Axis family} ($8$ vertices): all permutations of
   355	  $(\pm 1, 0, 0, 0)$;
   356	\item \textbf{Half-integer family} ($16$ vertices): all sign
   357	  combinations of $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
   358	\item \textbf{$\Ph$-mixed family} ($96$ vertices): all even
   359	  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
   360	  $\Ph^{2} = \Ph + 1$ identity, equivalently
   361	  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
   362	\end{itemize}
   363	The total is $8 + 16 + 96 = 120$ unit vectors. These are coordinate
   364	families, not H$_4$ orbits: H$_4$ acts transitively on the full
   365	$120$-vertex set, so the three families lie in a single H$_4$
   366	orbit. Reproduced by \texttt{repro/verify\_kernel.py:build\_v600};
   367	the numerical check $\max_{v} |\,\|v\| - 1\,| < 10^{-10}$ confirms
   368	all vertices on $S^{3}$.
   369	
   370	The H$_4$ Coxeter group (order $14400$) acts transitively on the
   371	$120$ vertices. Every vertex therefore has \emph{identical} local
   372	structure under $H_{4}$; in particular, every vertex has the same
   373	degree in the short-edge graph defined below.
   374	
   375	\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
   376	
   377	For two unit vectors $v, w \in \Rsixhundred$ on $S^{3}$, the
   378	Euclidean chord distance is
   379	\[
   380	\|v - w\| \;=\; \sqrt{2 - 2\,\langle v, w\rangle}.
   381	\]
   382	The \emph{short-edge graph} $G_{V_{600}}=(V,E)$ connects two vertices
   383	if their inner product equals the canonical short-edge value
   384	\begin{equation}\label{eq:short_edge}
   385	\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
   386	\end{equation}
   387	equivalently chord distance
   388	$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
   389	nearest-neighbour adjacency on the canonical 600-cell embedding
   390	into $S^{3}$~\citep{CoxeterRegularPolytopes}.
   391	
   392	\paragraph{Graph facts (forced by the construction).}
   393	The graph $G_{V_{600}}$ has:
   394	\begin{itemize}\itemsep=2pt
   395	\item $|V|=120$ vertices,
   396	\item $|E|=720$ edges,
   397	\item every vertex has degree exactly $12$ (H$_4$ transitivity on
   398	  the vertex set forces \emph{uniformity} of the local structure;
   399	  the short-edge nearest-neighbour construction gives the
   400	  numerical degree $12$, verified by
   401	  \texttt{repro/verify\_kernel.py}),
   402	\item the graph is connected (verified numerically by counting
   403	  connected components of the short-edge adjacency matrix; the
   404	  classical 600-cell connectivity result is well known
   405	  in~\citep{CoxeterRegularPolytopes}).
   406	\end{itemize}
   407	All four facts are reproduced numerically:
   408	\texttt{repro/verify\_kernel.py} reports $|V|=120$, $|E|=720$,
   409	degree-min/max $=12/12$ (uniform), and one connected component.
   410	
   411	\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
   412	
   413	Choose any vertex $v_{0}$ as the pole; the H$_3$ subgroup of H$_4$
   414	fixing $v_{0}$ partitions the remaining $119$ vertices into shells
   415	of constant inner product with $v_{0}$. The nine canonical inner
   416	products are
   417	\begin{equation}\label{eq:shell_inner}
   418	\langle v, v_{0}\rangle
   419	\;\in\;
   420	\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
   421	       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
   422	\end{equation}
   423	indexing shells $s = 0, 1, \ldots, 8$ from the pole to the
   424	antipode. The shell-size sequence is
   425	\begin{equation}\label{eq:shell_sizes}
   426	(|S_{0}|, |S_{1}|, \ldots, |S_{8}|)
   427	\;=\;
   428	(1,\ 12,\ 20,\ 12,\ 30,\ 12,\ 20,\ 12,\ 1).
   429	\end{equation}
   430	The middle shell $S_{4}$ has $30$ equatorial vertices forming the
   431	icosidodecahedral ring. The total is
   432	$1+12+20+12+30+12+20+12+1 = 120$, matching $|V|$. Reproduced
   433	verbatim by \texttt{repro/verify\_kernel.py:shell\_indices}.
   434	
   435	\paragraph{Antipodal symmetry.} The map $v \mapsto -v$ takes the
   436	shell-$s$ vertices to the shell-$(8-s)$ vertices: $s(-v) = 8 - s(v)$.
   437	The antipode $-v_{0}$ is the unique shell-$8$ vertex.
   438	
   439	\subsection{Inner-product check}\label{ssec:inner_product_check}
   440	
   441	The canonical short-edge criterion (Eq.~\eqref{eq:short_edge}) and
   442	the canonical shell inner products (Eq.~\eqref{eq:shell_inner})
   443	are jointly consistent: a vertex in shell $s_{1}$ is connected to a
   444	vertex in shell $s_{2}$ if and only if their pairwise inner product
   445	is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
   446	adjacency types to those compatible with the H$_3$ orbit structure.
   447	The numerically constructed graph respects this: every edge has
   448	inner product exactly $\Ph/2$ within machine precision (tolerance
   449	$10^{-10}$ in \texttt{repro/verify\_kernel.py:build\_short\_edge\_graph}).
   450	
   451	\subsection{What the substrate fixes, and what it does not}
   452	
   453	\begin{itemize}\itemsep=2pt
   454	\item \textbf{Fixed by the construction once $\Rsixhundred$ is
   455	  chosen}: $|V|=120$, uniform degree $12$, $9$-shell partition
   456	  $\{1,12,20,12,30,12,20,12,1\}$, antipodal symmetry, and the
   457	  Laplacian spectrum (\S\ref{sec:spectrum}).
   458	\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
   459	  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
   460	  (\S\ref{ssec:opnorm}); the operator-norm bound
   461	  $\|\Cph^{-1}\| = \Ph^{2}$.
   462	\item \textbf{Not fixed by this paper}: the choice of
   463	  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other regular
   464	  4-polytopes / Coxeter substrates. The 600-cell choice is
   465	  post-hoc motivated by the empirical landings
   466	  (\S\ref{sec:passive_witness}, \S\ref{sec:active_witness}). A
   467	  formal substrate ablation is an
   468	  open build (\S\ref{sec:limitations}).
   469	\end{itemize}

 succeeded in 376ms:
     1	% =====================================================================
     2	\section{The Laplacian spectrum}\label{sec:spectrum}
     3	% =====================================================================
     4	
     5	The unweighted graph Laplacian $\Lop = D - A$ on $\Rsixhundred$
     6	numerically resolves into nine distinct eigenvalue classes whose
     7	values match the closed-form $\mathbb{Z}[\Ph]$ list given in
     8	Table~\ref{tab:spectrum} to machine precision; multiplicities sum
     9	to $|V| = 120$. The spectrum is computed numerically by
    10	\texttt{repro/verify\_kernel.py:laplacian\_spectrum} (a single
    11	$120\times 120$ symmetric eigendecomposition, deterministic at
    12	machine precision); the closed-form identification is made by
    13	algebraic recognition of the displayed values, not by an exact
    14	arithmetic derivation in this paper.
    15	
    16	\begin{table}[ht]
    17	\centering
    18	\small
    19	\caption{Computed Laplacian spectrum of $\Lop$ on $\Rsixhundred$.
    20	Closed-form values in $\mathbb{Z}[\Ph]$ alongside the numerical
    21	values returned by \texttt{repro/verify\_kernel.py}; multiplicities
    22	sum to $120$.}
    23	\label{tab:spectrum}
    24	\begin{tabular}{c c c}
    25	\toprule
    26	Closed-form eigenvalue & Numerical value & Multiplicity \\
    27	\midrule
    28	$0$            & $-3\!\times\!10^{-15}$ (machine zero) & $1$ \\
    29	$12 - 6\Ph$    & $2.2918$  & $4$ \\
    30	$12 - 4\Ph$    & $5.5279$  & $9$ \\
    31	$9$            & $9.0000$  & $16$ \\
    32	$12$           & $12.0000$ & $25$ \\
    33	$14$           & $14.0000$ & $36$ \\
    34	$4\Ph + 8$     & $14.4721$ & $9$ \\
    35	$15$           & $15.0000$ & $16$ \\
    36	$6\Ph + 6$     & $15.7082$ & $4$ \\
    37	\midrule
    38	\multicolumn{2}{r}{\textbf{Total multiplicity:}} & $\mathbf{120}$ \\
    39	\bottomrule
    40	\end{tabular}
    41	\end{table}
    42	
    43	\paragraph{Closed-form check.} Using $\Ph = (1+\sqrt 5)/2$:
    44	\begin{align*}
    45	12 - 6\Ph &= 12 - 3(1+\sqrt 5) = 9 - 3\sqrt 5 \approx 2.2918, \\
    46	12 - 4\Ph &= 12 - 2(1+\sqrt 5) = 10 - 2\sqrt 5 \approx 5.5279, \\
    47	4\Ph + 8 &= 2(1+\sqrt 5) + 8 = 10 + 2\sqrt 5 \approx 14.4721, \\
    48	6\Ph + 6 &= 3(1+\sqrt 5) + 6 = 9 + 3\sqrt 5 \approx 15.7082.
    49	\end{align*}
    50	The eigenvalue pairs $\{12 - 6\Ph,\ 6\Ph+6\}$ (both with multiplicity
    51	$4$) and $\{12 - 4\Ph,\ 4\Ph+8\}$ (both with multiplicity $9$)
    52	are conjugate under the Galois automorphism
    53	$\sigma\colon \sqrt 5 \mapsto -\sqrt 5$ on $\mathbb{Z}[\Ph]$. The
    54	fixed-point eigenvalues $\{0, 9, 12, 14, 15\}$ are rational and
    55	have multiplicities $\{1, 16, 25, 36, 16\}$ (sum $94$); the
    56	$\sigma$-paired eigenvalues have total multiplicity $4+4+9+9 = 26$.
    57	
    58	\paragraph{$\sigma$-fix vs $\sigma$-paired multiplicity split.}
    59	$94/120 = 78.3\%$ of the spectrum is $\sigma$-fixed (rational); the
    60	remaining $26/120 = 21.7\%$ is $\sigma$-paired. The companion RH
    61	artifact (forthcoming) uses this pairing shape in a $\sigma$-attractor
    62	reformulation; that reading is not imported here. We report only
    63	that the spectrum has this structure.
    64	
    65	\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
    66	
    67	The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
    68	\[
    69	\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
    70	\;\approx\; 0.381966,
    71	\]
    72	and the operator-norm bound is
    73	\[
    74	\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
    75	\]
    76	\texttt{repro/verify\_kernel.py:operator\_norm\_check} reports
    77	$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
    78	(predicted) — match to six decimal places. The largest eigenvalue
    79	of $\Cph$ is
    80	$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
    81	= 9 + 3\sqrt 5 + (2 - \Ph) \approx 16.0902$.
    82	
    83	\subsection{H$_4$ irrep block decomposition (imported context)}
    84	\label{ssec:irrep}
    85	
    86	The eigenspaces of $\Lop$ partition into H$_4$-proper and
    87	$\sigma$-twin Coxeter exponent classes. For H$_4$ proper the
    88	exponents are $\{1, 11, 19, 29\}$; under the
    89	$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
    90	$\{7, 13, 17, 23\}$. The $\sigma$-orbit projector basis used in the
    91	aria-chess companion's recurrent
    92	layer~\citep{SmartAriaChess2026} realises this block decomposition
    93	at machine precision and provides a spectrally clean
    94	H$_4$-equivariant basis there.
    95	
    96	This subsection is imported context from the aria-chess companion;
    97	the irrep block decomposition is \emph{not} verified by
    98	\texttt{repro/verify\_kernel.py} of this paper and is not used as
    99	a load-bearing fact for any operator-witness claim made here. We
   100	include the labelling for orientation only.
   101	% =====================================================================
   102	\section{Discrete-to-continuum agreement}\label{sec:agreement}
   103	% =====================================================================
   104	
   105	This is the central geometric diagnostic of the paper: the
   106	discrete response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a
   107	localised source has high per-vertex Pearson correlation in radial
   108	shape with the continuum kernel
   109	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
   110	the source. Pearson correlation is a shape similarity statistic, not
   111	an equality claim. We give the test, the numerical result, and a variant
   112	comparison in which the unweighted Laplacian ranks highest among
   113	the three tested variants (unweighted, $\Ph$-geometric weighted,
   114	$\Ph$-arithmetic weighted).
   115	
   116	\subsection{The test}\label{ssec:test}
   117	
   118	Pick a pole vertex $v_{0}$ (we use the canonical $+x_{0}$ axis
   119	vertex). Set $f = e_{v_{0}}$ (the unit vector at $v_{0}$, all
   120	other entries zero). Compute
   121	\[
   122	\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
   123	\]
   124	by direct linear solve (no eigenmode truncation). For each vertex
   125	$v \in V$, compute the Euclidean chord distance
   126	$x(v) = \|v - v_{0}\|$ and the continuum prediction
   127	\[
   128	G(x(v)) \;=\; (\Ph/2)\,\exp(-\,x(v)/\Ph).
   129	\]
   130	The agreement criterion is the Pearson correlation between
   131	$\psi(v)$ and $G(x(v))$ across $v \in V \setminus \{v_{0}\}$ (the
   132	source itself is excluded, since the discrete response there is
   133	trivially the diagonal of $\Cph^{-1}$ and the chord distance is
   134	zero, both degenerate for the comparison).
   135	
   136	\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
   137	
   138	\texttt{repro/verify\_kernel.py:variant\_correlation} returns:
   139	\begin{itemize}\itemsep=2pt
   140	\item \textbf{Per-vertex Pearson correlation}: $\rho = 0.976$.
   141	\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
   142	  (averaging $\psi(v)$ over each H$_3$ shell first, then
   143	  correlating the $9$-point shell-mean trajectory with the
   144	  continuum prediction at the shell mean radius).
   145	\end{itemize}
   146	The two correlations measure the same fact at different
   147	resolutions and with different source-vertex conventions:
   148	\begin{itemize}\itemsep=2pt
   149	\item Per-vertex test: $|V|-1 = 119$ data points (every
   150	  non-source vertex), source $v_{0}$ \emph{excluded} (the discrete
   151	  response there is the diagonal of $\Cph^{-1}$ and the chord
   152	  distance is $0$, both degenerate for the comparison).
   153	\item Shell-mean test: $9$ data points (one per H$_3$ shell);
   154	  shell $0$ contains only the source vertex, so it is included
   155	  on the shell-mean side and contributes a single
   156	  ($\psi(v_{0}), G(0)$) point.
   157	\end{itemize}
   158	On the unweighted 600-cell graph with an H$_3$-fixed source,
   159	$\psi$ is shell-constant up to numerical precision — the
   160	within-shell standard deviations are at machine precision
   161	($\sim 10^{-16}$). The two tests therefore differ in weighting and
   162	source convention, not in noise content: the per-vertex test
   163	weights each shell by its multiplicity
   164	($\{12, 20, 12, 30, 12, 20, 12, 1\}$ for the non-source shells)
   165	and excludes the source vertex, while the shell-mean test gives
   166	equal weight to every shell and includes the source. The
   167	per-vertex test is the headline agreement criterion in this paper.
   168	
   169	\subsection{Variant comparison}\label{ssec:variant_comparison}
   170	
   171	Two $\Ph$-cocycle weighted Laplacian variants are tested as
   172	controls:
   173	
   174	\begin{itemize}\itemsep=2pt
   175	\item \textbf{$\Ph$-geometric weights}: edge weight
   176	  $w_{vw} = \sqrt{\omega_{+}(v)\,\omega_{+}(w)}$ with vertex weight
   177	  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
   178	  is the shell index of $v$.
   179	\item \textbf{$\Ph$-arithmetic weights}: edge weight
   180	  $w_{vw} = \tfrac12[\omega_{+}(v) + \omega_{+}(w)]$ with the same
   181	  $\omega_{+}$.
   182	\end{itemize}
   183	The weighted Laplacian is then
   184	$L_{w} = D_{w} - A_{w}$ where $A_{w}$ is the weighted adjacency.
   185	We re-run the discrete-to-continuum test on each variant.
   186	
   187	\begin{table}[ht]
   188	\centering
   189	\small
   190	\caption{Per-vertex and shell-mean Pearson correlations between the
   191	discrete response $\psi = (L_{w} + \Ph^{-2} I)^{-1} e_{v_{0}}$
   192	and the continuum prediction $G(\|v - v_{0}\|)$ for three
   193	Laplacian variants ($L_{w}$ unweighted or $\Ph$-cocycle weighted).
   194	Computed by \texttt{repro/verify\_kernel.py:variant\_correlation}.}
   195	\label{tab:variant_correlation}
   196	\begin{tabular}{l c c}
   197	\toprule
   198	Variant            & Per-vertex correlation & Shell-mean correlation \\
   199	\midrule
   200	\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
   201	$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
   202	$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
   203	\bottomrule
   204	\end{tabular}
   205	\end{table}
   206	
   207	\textbf{Reading.} Among the three tested variants, the unweighted
   208	Laplacian ranks highest on both reported criteria
   209	($+0.088$ per-vertex over the next variant, $+0.044$ shell-mean).
   210	This reproduces, on a different test, the qualitative ranking the
   211	b-anomaly paper~\citep{SmartBAnomaly2026} established
   212	independently against its data-$\chi^{2}$ criterion
   213	on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
   214	b-anomaly numbers). Two independent criteria — geometry-only
   215	correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
   216	agree on which of the three tested variants ranks highest. We do not claim
   217	this is a uniqueness result; we report it as a two-criterion
   218	convergence (the b-anomaly paper's own caveat that the data was
   219	looked at first and the geometry criterion verified afterward is
   220	inherited verbatim).
   221	
   222	\subsection{What the agreement does and does not establish}
   223	
   224	\paragraph{Does establish.} A geometric agreement: the discrete
   225	response of a fixed-shift Green operator on a fixed graph
   226	correlates per-vertex in radial shape, at Pearson $0.976$, with
   227	the closed-form continuum exponential at the same length scale
   228	$\Ph$. This is a non-trivial Pearson correlation between
   229	separately evaluated discrete and continuum Green responses
   230	sharing the same design-level scale $\Ph^{-2}$: (i) the discrete
   231	inverse of a $120\times 120$ Laplacian-plus-shift matrix; and
   232	(ii) a one-dimensional continuum exponential. The $\Ph$-mediated
   233	agreement is an empirical fact about the chosen substrate and
   234	shift, computed (not fitted) by the verification script.
   235	
   236	\paragraph{Does not establish.} Operator uniqueness on either
   237	empirical landing — the b-anomaly paper documents a free-width
   238	Gaussian alternative that fits comparably in $\chi^{2}$ at the
   239	cost of one extra shape parameter, and the aria-chess preprint
   240	does not run a substrate ablation; both caveats are inherited
   241	verbatim. The agreement also does not establish that
   242	$\Rsixhundred$ is the unique discrete substrate with this
   243	property; the $24$-cell, $120$-cell, and other H$_n$ Coxeter
   244	graphs would need to be tested on the same correlation criterion
   245	to make any comparative claim, and a formal substrate ablation is
   246	an open build (\S\ref{sec:limitations}).

 succeeded in 413ms:
     1	% =====================================================================
     2	\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
     3	% =====================================================================
     4	
     5	This section threads the first independent empirical landing of
     6	$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
     7	summarise here only what the operator-witness narrative requires
     8	and inherit the preprint's caveats verbatim.
     9	
    10	\subsection{What b-anomaly tests}\label{ssec:banomaly_setup}
    11	
    12	The Wilson-coefficient Hamiltonian for $b\to s\mu^{+}\mu^{-}$
    13	contains a $C_{9}^{(\prime)}$ contribution that, in the Standard
    14	Model, is approximately $q^{2}$-independent in the relevant
    15	kinematic range. The b-anomaly preprint tests a fixed
    16	$q^{2}$-dependent effective shift on top of the SM backend, of the
    17	form
    18	\begin{equation}\label{eq:banomaly_kernel}
    19	\Delta C_{9}^{\mathrm{eff}}(q^{2})
    20	\;=\;
    21	-\,A \cdot \kappa_{V_{600}}(q^{2}),
    22	\end{equation}
    23	where $\kappa_{V_{600}}(q^{2}) > 0$ on the LHCb $q^{2}$ window is
    24	the projection of $\Cph$ on $\Rsixhundred$ to the flavour-physics
    25	$q^{2}$ axis (the b-anomaly preprint's §3 projection construction,
    26	which we do not relitigate here; this is a projection of the
    27	operator, not a derivation of $\Ph^{-2}$), and $A$ is a single
    28	fitted dimensionless amplitude per dataset. The explicit minus
    29	sign in Eq.~\eqref{eq:banomaly_kernel} reflects the b-anomaly
    30	preprint's sign convention: a positive fitted $A>0$ produces a
    31	negative $\Delta C_{9}^{\mathrm{eff}}<0$, the established
    32	direction of the angular anomaly. The kernel shape
    33	$\kappa_{V_{600}}$ is held fixed across all five datasets.
    34	This is a \emph{structural} test: same fixed $\Cph$ on the same
    35	$\Rsixhundred$, no shape retuning between datasets.
    36	
    37	\subsection{The five-dataset structural fit}
    38	
    39	The b-anomaly preprint reports the following per-dataset table
    40	(verbatim from~\citep{SmartBAnomaly2026}, also at
    41	\texttt{BANOMALY-001/vfd-b-anomaly/README.md}):
    42	
    43	\begin{table}[ht]
    44	\centering
    45	\small
    46	\caption{b-anomaly five-dataset structural fit. Verbatim
    47	from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
    48	dataset, kernel shape held fixed.}
    49	\label{tab:banomaly}
    50	\begin{tabular}{l l r r r r}
    51	\toprule
    52	Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
    53	   Best-fit $A$ & $\Delta C_{9}^{\mathrm{eff}}$ \\
    54	\midrule
    55	LHCb 2015 & $B^{0}\!\to\!K^{*0}$ & $32$ & $-0.24$ & $+1.24$ & $-0.96$ \\
    56	LHCb 2021 & $B^{+}\!\to\!K^{*+}$ & $32$ & $+0.17$ & $+2.06$ & $-1.59$ \\
    57	CMS 2025 (no $P_{4}'$) & $B^{0}\!\to\!K^{*0}$ & $18$ & $+0.47$ & $+1.05$ & $-0.81$ \\
    58	LHCb 2025 & $B^{0}\!\to\!K^{*0}$ & $32$ & $+1.09$ & $+1.14$ & $-0.86$ \\
    59	LHCb 2015 & $B_{s}\!\to\!\phi$ ($S$-basis) & $24$ & $-0.24$ & $+4.98$ & $-3.85$ \\
    60	\bottomrule
    61	\end{tabular}
    62	\end{table}
    63	
    64	\subsection{What the structural fit establishes}
    65	
    66	\begin{itemize}\itemsep=2pt
    67	\item \textbf{Universality (5/5).} The same fixed kernel shape
    68	  can be fit to all five datasets with one amplitude $A$ per
    69	  dataset and no shape retuning. The kernel never moves between
    70	  datasets.
    71	\item \textbf{Sign uniformity (5/5).} $A > 0$ in $5/5$ fits;
    72	  $\Delta C_{9}^{\mathrm{eff}} < 0$ in $5/5$ fits. The kernel
    73	  reproduces the established direction of the
    74	  anomaly~\citep{LHCbAngular2020} across all five independent
    75	  measurements.
    76	\item \textbf{Cross-channel ratio.} The $B\to K^{*}$ vs
    77	  $B_{s}\!\to\!\phi$ amplitudes differ by a factor partly explained
    78	  by the predicted Krüger--Matias $P$-basis vs $S$-basis
    79	  amplification ($\sim 2.2$~\citep{KrugerMatias2005}). The
    80	  basis amplification accounts for about half the observed
    81	  $B_{s}\!\to\!\phi$ amplitude; a residual factor of about two
    82	  remains. The b-anomaly preprint reports this residual as an open
    83	  item, not a discharge.
    84	\item \textbf{Geometry-first variant test.} Of three discrete
    85	  Laplacian variants on $\Rsixhundred$ (unweighted,
    86	  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
    87	  unweighted choice wins on both a pure-geometry criterion
    88	  (correlation $0.997$ with the continuum kernel, b-anomaly
    89	  preprint §3.4) and the LHCb~2025 data $\chi^{2}$
    90	  ($\chi^{2}=13.555$). The two criteria agree on the variant
    91	  ranking — a two-criterion convergence on the same fixed
    92	  operator.
    93	\end{itemize}
    94	
    95	\subsection{What the structural fit does \emph{not} establish}
    96	
    97	The b-anomaly preprint is explicit about the following caveats,
    98	which we inherit verbatim:
    99	
   100	\begin{itemize}\itemsep=2pt
   101	\item \textbf{AIC tie on current data.} On Akaike model comparison,
   102	  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
   103	  shift ($\mathrm{FREE\_C9}$, also $k=1$) are statistically
   104	  indistinguishable: stacked AIC weights
   105	  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
   106	  Current data cannot resolve the model comparison. AIC is blind
   107	  to the universality / shape-prediction claim itself, but it is
   108	  decisive about whether the shape is forced by data: it is not.
   109	\item \textbf{Free-width Gaussian alternative.} A free-width
   110	  Gaussian charm-loop proxy fits the same five datasets comparably
   111	  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
   112	  is not the unique $q^{2}$ shape consistent with the anomaly.
   113	\item \textbf{Mode-B drift (linearised-to-non-linear refit).} An
   114	  earlier analysis the b-anomaly project labels Mode-B
   115	  (linearised) gave a stronger preference
   116	  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
   117	  the subsequent non-linear refit; the $+2.77$-AIC-unit drift
   118	  between Mode-B (linearised) and the non-linear refit is the
   119	  largest single methodological uncertainty in the b-anomaly
   120	  project.
   121	\item \textbf{Look-elsewhere on the variant test.} The b-anomaly
   122	  preprint's limitations section~\citep{SmartBAnomaly2026}
   123	  acknowledges that the LHCb~2025 data was looked at first, and
   124	  only later was the agreement of the data-$\chi^{2}$ ranking with
   125	  the pure-geometry ranking verified. (The b-anomaly README
   126	  emphasises that the geometry-only criterion is independent of
   127	  the LHCb data; the historical non-blindness is in the project's
   128	  ordering, not in the criterion.) The two-criterion agreement is
   129	  criterion-independent but not historically blind.
   130	\end{itemize}
   131	
   132	\subsection{Reading at the operator level}
   133	
   134	The b-anomaly result is the \emph{passive-regime} empirical
   135	witness for $\Cph$ on $\Rsixhundred$: a single linear response
   136	$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
   137	fixed discrete-to-momentum projection, gives a sign-uniform
   138	description of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across
   139	five independent measurements without shape retuning. This does
   140	not establish the kernel as theorem-grade physics on the flavour
   141	side (the AIC tie, the free-width Gaussian alternative, and the
   142	Mode-B linearised-to-non-linear refit drift prevent that). It
   143	does support, at the operator-witness level, the inherited reading
   144	that the same fixed $\Cph$ on the same fixed $\Rsixhundred$ is
   145	consistent with one of two independent empirical landings without
   146	parameter retuning. The
   147	second landing is in \S\ref{sec:active_witness}.
   148	% =====================================================================
   149	\section{Active-regime witness: aria-chess}\label{sec:active_witness}
   150	% =====================================================================
   151	
   152	This section threads the second independent empirical landing of
   153	$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
   154	summarise here only what the operator-witness narrative requires
   155	and inherit the preprint's substrate-witness scope verbatim.
   156	
   157	\subsection{What aria-chess tests}\label{ssec:aria_setup}
   158	
   159	The aria-chess preprint adds a recurrent self-model layer above
   160	the same $\Cph$ on the same $\Rsixhundred$. The architecture
   161	introduces:
   162	\begin{itemize}\itemsep=2pt
   163	\item One \emph{condition-dependent} self-injection coupling
   164	  $\eta \in \{0, 0.05, 0.20\}$ (PROPOFOL, SLEEP\_N3,
   165	  WAKE/RECOVERY) that controls the strength of the recurrent
   166	  feedback;
   167	\item One \emph{substrate-pinned} nonlinearity
   168	  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
   169	  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
   170	  $k=12$ is not a free hyperparameter; it is the substrate's
   171	  average degree.
   172	\item Condition-specific \emph{biologically-motivated} stimulus
   173	  models (slow oscillation + spindles + K-complexes for SLEEP\_N3,
   174	  AR(1) noise + tonic shell + attention episodes for WAKE,
   175	  low-amplitude tonic noise for PROPOFOL). These are
   176	  biologically-motivated design choices, not measurement-fits to
   177	  subject-level EEG data.
   178	\end{itemize}
   179	The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
   180	b-anomaly and aria-chess; the same fixed shift used in the
   181	flavour-physics structural fit is used in the cortical substrate
   182	witness.
   183	
   184	\subsection{Eighteen preregistered correspondences}
   185	
   186	Eighteen quantitative predictions (P1--P18) were locked on
   187	2026-04-18 in the aria-chess preprint's
   188	\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any
   189	validation run. Each prediction has a specific numerical claim, a
   190	falsifiable threshold, and a named validation script. The
   191	preregistered tally as reported in~\citep{SmartAriaChess2026}:
   192	
   193	\begin{itemize}\itemsep=2pt
   194	\item $17/18$ at standard validation methodology ($5$-seed
   195	  cascade block plus state-reset protocol);
   196	\item $18/18$ after a documented $N\!=\!20$ deep-dive on the
   197	  residual high-variance interaction $C\!\times\!P$ (P4: bootstrap
   198	  point estimate $+0.190$, $95\%$ CI $[+0.143, +0.239]$,
   199	  $0/2000$ resamples at-or-below zero, reported as $0.0000$).
   200	\item No preregistered threshold has been modified.
   201	\end{itemize}
   202	The aria-chess preprint reports this as methodology refinement
   203	(documented seed-count increase on a high-per-seed-variance
   204	interaction term), \emph{not} as a threshold change. We inherit the
   205	reading verbatim.
   206	
   207	\subsection{Six drug/sleep EEG signatures}
   208	
   209	On a single deterministic substrate trajectory at seed~$42$, the
   210	aria-chess preprint reports six biological signatures testing
   211	against literature-derived thresholds:
   212	
   213	\begin{itemize}\itemsep=2pt
   214	\item \textbf{Wake cortical-avalanche $\alpha$}: $\alpha = 2.252$,
   215	  $95\%$ CI $[1.82, 2.86]$, $R^{2}=0.956$ — the WAKE confidence
   216	  interval overlaps both the Sleep-EDFx EEG CI $[2.50, 2.53]$
   217	  ($n=30$ subjects) and aria-chess's prior cascade pipeline CI
   218	  $[2.73, 3.25]$ pairwise (the Sleep-EDFx and prior-pipeline
   219	  intervals do not overlap each other; the WAKE interval is the
   220	  pairwise common ground).
   221	\item \textbf{NREM-N3 phenomenal-intensity variance ratio}:
   222	  $0.463\!\times$ wake (predicted $\sim 0.365$, threshold $<0.70$).
   223	\item \textbf{Propofol modality-switching ratio}: $1.83\!\times$
   224	  wake (threshold $\in [1.5, 5.0]$, empirical reference
   225	  $2.96\!\times$ from OpenNeuro \texttt{ds005620}).
   226	\item \textbf{Propofol continuity drop}: $+0.066$
   227	  (threshold $> 0.020$).
   228	\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
   229	  direction confirmed; $\Phi$-proxy not full IIT).
   230	\item \textbf{Recovery deterministic identity to wake}: under the
   231	  WAKE stimulus protocol, the RECOVERY trajectory is bit-identical
   232	  to the WAKE trajectory.
   233	\end{itemize}
   234	
   235	\subsection{Cross-domain selectivity}
   236	
   237	\begin{itemize}\itemsep=2pt
   238	\item \textbf{Chess pattern recognition (P9--P13)}: $32$ chess
   239	  positions across $4$ categories on $8$-D V2 features; substrate
   240	  routing lifts leave-one-out classification at canonical depth
   241	  $n=25$ ticks from raw $53.1\%$ to substrate-routed $93.8\%$
   242	  ($+40.6$pp), well above the preregistered $\geq +15$pp floor.
   243	\item \textbf{Conversation pattern recognition (P14--P16)}:
   244	  $64$ utterances, $8$ categories; raw classification $87.5\%$,
   245	  substrate-routed lift $-4.4$pp (within the preregistered
   246	  neutrality band $|\cdot| < 10$pp). The substrate is selectively
   247	  amplifying in tasks where raw features are ambiguous and
   248	  approximately neutral when raw features are already
   249	  discriminative.
   250	\item \textbf{HCP brain functional connectivity (P17--P18)}:
   251	  full-cohort descriptive statistics on $n=1003$ subjects show
   252	  ARIA's $H_4$-transitive structure at $-11.58\sigma$ on degree
   253	  homogeneity, $+79.78\sigma$ on raw participation ratio (with
   254	  node-count caveat: ARIA $|V|=120$ vs HCP ICA-50 $|V|=50$), and
   255	  $+6.80\sigma$ on clustering coefficient. ARIA's degree std is
   256	  $0$ by H$_4$ transitivity (a theorem), $11.58$ standard
   257	  deviations below the HCP biological cohort.
   258	\end{itemize}
   259	
   260	\subsection{Reading at the operator level}
   261	
   262	The aria-chess result is the \emph{active-regime} empirical
   263	witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
   264	layer above $\Cph$ uses one condition-dependent coupling and one
   265	substrate-pinned nonlinearity at the graph's average degree
   266	$k=12$; no other \emph{kernel-shape} parameter enters. Above the
   267	operator, aria-chess inherits its own dynamical and stimulus
   268	constants (e.g.\ a fixed dynamical decay, fixed cascade gains,
   269	condition-specific biologically-motivated stimulus models); these
   270	are documented in the aria-chess preprint and are not retuned in
   271	this paper. The kernel shift $\Ph^{-2}$ is not retuned between
   272	b-anomaly and aria-chess. Under those design choices, the same
   273	fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
   274	preregistered cortical correspondences (frozen 2026-04-18) and six
   275	literature-thresholded EEG drug/sleep signatures.
   276	
   277	The aria-chess preprint stays inside substrate-witness scope: it
   278	does not claim the substrate \emph{is} consciousness, does not
   279	claim 600-cell uniqueness among regular 4-polytopes, and does not
   280	deliver a selection theorem on the ACT 4-tuple. We inherit the
   281	scope verbatim. What we add at the operator level is the
   282	observation that the same fixed $\Cph$ — under no shape-parameter
   283	retuning between regimes — is the shared response primitive
   284	underneath both empirical landings (the b-anomaly $q^{2}$
   285	projection above $\Cph$ and the aria-chess recurrent self-model
   286	layer above $\Cph$ are distinct above-operator constructions; the
   287	operator below them is the same).
   288	
   289	\subsection{Two-witness structure}
   290	
   291	\begin{table}[ht]
   292	\centering
   293	\small
   294	\caption{Two independent empirical landings of $\Cph$ on
   295	$\Rsixhundred$, with no shape retuning between regimes.}
   296	\label{tab:two_witness}
   297	\begin{tabular}{p{0.22\linewidth} p{0.36\linewidth} p{0.36\linewidth}}
   298	\toprule
   299	& Passive regime & Active regime \\
   300	\midrule
   301	Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
   302	Domain             & flavour physics                    & cortical neuroscience \\
   303	Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) & prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
   304	Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
   305	Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
   306	Shift $\Ph^{-2}$   & not retuned                        & not retuned \\
   307	Headline           & $5/5$ sign uniformity              & $18/18$ prereg + $6/6$ EEG \\
   308	Kernel-shape free params & 0                            & 0 \\
   309	Other free params  & 1 amplitude $A$ per dataset        & 1 coupling $\eta$ per condition; v4 stimulus protocols \\
   310	Caveat             & AIC tie; free-width Gaussian alt.\ & single-seed EEG; no polytope ablation \\
   311	\bottomrule
   312	\end{tabular}
   313	\end{table}
   314	
   315	The two witnesses share, by design, exactly the geometry-fixed
   316	operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
   317	the same shift $\Ph^{-2}$. They share no fitted parameter,
   318	threshold, dataset, or methodological choice above the operator
   319	level. The b-anomaly amplitude $A$ is fitted to flavour-physics
   320	$q^{2}$ shape, dataset by dataset; the aria-chess coupling $\eta$
   321	is fixed by experimental condition (PROPOFOL/SLEEP/WAKE), not by
   322	neural data; the v4 stimulus protocols are biologically motivated,
   323	not subject-fit. Independence in this paper is independence at
   324	the empirical layer above the shared operator.

 succeeded in 405ms:
     1	% =====================================================================
     2	\section{Programme home and the open selection layer}\label{sec:programme_home}
     3	% =====================================================================
     4	
     5	This section positions $\Cph$ within the broader cascade programme
     6	and identifies what the operator does not deliver. The framing
     7	matters for the hostile-review reading: $\Cph$ is the
     8	\emph{response} primitive; \emph{selection} (which response
     9	configuration the system picks under dynamics) is a separate layer
    10	that this paper does not close.
    11	
    12	\subsection{Programme home: polynomial-in-$L$ Lyapunov family}
    13	
    14	Several constructions across the cascade-programme drafts are
    15	$L$-symmetric polynomial-in-$L$ functionals on a finite-dimensional
    16	substrate. They are programme-positioned as members of the same
    17	family as $\Cph$:
    18	
    19	\begin{itemize}\itemsep=2pt
    20	\item \textbf{RH polynomial filter} (forthcoming RH artifact in
    21	  this programme). Cascade closure functional on $\mathbb{R}^{120}$:
    22	  $F_{\mathrm{filt}}(x) = \tfrac12 \langle x, p_{\mathrm{fix}}(L)^{2} x\rangle$
    23	  with $\Psi_{t} = e^{-t\, p_{\mathrm{fix}}(L)^{2}}$. Programme-positioned
    24	  as the $\sigma$-fix-annihilator instance of the family: a
    25	  degree-$10$ positive functional vanishing exactly on
    26	  $V_{\mathrm{fix}}$. The artifact itself is not load-bearing for
    27	  any claim made in this paper.
    28	\item \textbf{YM cascade gap operator} (forthcoming YM artifact in
    29	  this programme). Discrete cascade gap Hamiltonian,
    30	  programme-positioned as a $\Cph$-style mass-regularised Laplacian
    31	  on $\Rsixhundred$. The artifact itself is not load-bearing for
    32	  any claim made in this paper.
    33	\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
    34	  The homeostatic regulariser
    35	  $R_{\mathrm{hom}}$ in the 4-tuple $(M, L_M, W, R_{\mathrm{hom}})$,
    36	  programme-positioned as a member of the same polynomial-in-$L$
    37	  family.
    38	\end{itemize}
    39	
    40	We list the family-membership claim as \emph{programme-positioned},
    41	not formally proved. Each named operator is in a
    42	polynomial-in-$L$ form with positivity and self-adjointness
    43	properties matching the family description; we do not claim a
    44	formal classification theorem identifying the family.
    45	
    46	\subsection{Response vs selection}
    47	
    48	The closure response $\psi = \Cph^{-1} f$ is determined by the
    49	chosen substrate plus the design-level shift: $\Cph$ is fixed by
    50	the substrate $\Rsixhundred$ and the design-level choice
    51	$\Ph^{-2}$, and the response is the resulting linear inverse.
    52	This is a \emph{response} primitive. It does \emph{not} answer:
    53	\begin{itemize}\itemsep=2pt
    54	\item Why this substrate? (Selection across regular 4-polytopes
    55	  $\{24\text{-cell}, 600\text{-cell}, 120\text{-cell}\}$.)
    56	\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
    57	  positive constant.)
    58	\item How does the system pick a response configuration over
    59	  time? (Crystallisation / Lyapunov descent dynamics on a
    60	  $W$-trajectory.)
    61	\end{itemize}
    62	
    63	The selection layer is open. It appears as an open hypothesis in
    64	three independent frames:
    65	\begin{enumerate}\itemsep=2pt
    66	\item \textbf{Forthcoming RH artifact}: the closure-flow suppression
    67	  hypothesis $\textup{H}_{\mathrm{attr}}$ at the level of the
    68	  original cascade closure functional. The polynomial filter
    69	  $\Psi_{t}$ is a finite-dimensional analogue, by design.
    70	\item \textbf{Adaptive Closure
    71	  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
    72	  4-tuple $(M, L_M, W, R_{\mathrm{hom}})$ proposes a Lyapunov
    73	  $V(W)$ on the reduced flow, an edge-space decomposition under
    74	  $2I$-equivariance, and a full reduced-flow convergence theorem
    75	  on $W$-trajectories — \emph{none delivered} in that paper.
    76	\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
    77	  the substrate-witness scope explicitly does \emph{not} deliver
    78	  a selection theorem; ACT is positioned as the future
    79	  selection-theorem witness.
    80	\end{enumerate}
    81	
    82	The recurrence of an open selection gap across these three frames
    83	is a programme-level reading: the gap may be a single mathematical
    84	problem rather than three independent ones, but the present paper
    85	gives no proof of equivalence. The two empirical witnesses landed
    86	in this paper strengthen external confidence in the \emph{response}
    87	primitive without reducing or addressing the selection gap.
    88	
    89	\subsection{What this paper closes vs leaves open}
    90	
    91	\paragraph{Closes (at the operator-witness level).}
    92	\begin{itemize}\itemsep=2pt
    93	\item The operator $\Cph$ is well-defined and positive definite
    94	  on any $(M, L_M)$ satisfying (H1)--(H3); the operator-norm
    95	  identity $\|\Cph^{-1}\| = \Ph^{2}$ holds whenever
    96	  $\lambda_{\min}(L_M) = 0$ (e.g.\ on a connected finite graph
    97	  with the standard combinatorial Laplacian). On substrates where
    98	  $\lambda_{\min}(L_M) > 0$ (e.g.\ Dirichlet-boundary continuum
    99	  cases) the bound $\|\Cph^{-1}\| \leq \Ph^{2}$ holds and is
   100	  generally strict (\S\ref{sec:definition}).
   101	\item The 600-cell instance $\Rsixhundred$ has the construction
   102	  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
   103	  Table~\ref{tab:spectrum}, both reproduced numerically
   104	  (\texttt{repro/verify\_kernel.py}).
   105	\item Discrete-to-continuum agreement at per-vertex Pearson
   106	  correlation $0.976$ on the unweighted variant, with the unweighted
   107	  variant winning the geometry-only criterion against two
   108	  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
   109	\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
   110	  the shared response primitive underneath two independent empirical works in
   111	  qualitatively distinct regimes (\S\ref{sec:passive_witness},
   112	  \S\ref{sec:active_witness}).
   113	\end{itemize}
   114	
   115	\paragraph{Leaves open.}
   116	\begin{itemize}\itemsep=2pt
   117	\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
   118	  as a design-level shift; not derived from a closure functional
   119	  or symmetry argument.
   120	\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
   121	  post-hoc motivated by the empirical landings; alternative regular
   122	  4-polytopes are an explicit ablation build, not a discharged
   123	  comparison.
   124	\item \emph{Kernel-uniqueness on either empirical landing.} The
   125	  b-anomaly free-width Gaussian alternative (fits comparably with
   126	  one extra shape parameter) and the AIC tie
   127	  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$) are
   128	  inherited verbatim from~\citep{SmartBAnomaly2026}.
   129	\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
   130	  decomposition under $2I$-equivariance, full reduced-flow
   131	  convergence — all explicitly not delivered
   132	  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
   133	  here.
   134	\item \emph{Family-membership theorem.} The programme-home
   135	  positioning of cascade Lyapunov functionals as members of the
   136	  same polynomial-in-$L$ family is reported as
   137	  \emph{programme-positioned}, not formally classified.
   138	\end{itemize}
   139	% =====================================================================
   140	\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
   141	% =====================================================================
   142	
   143	This section enumerates limitations transparently, organised as a
   144	five-move guard matrix following the b-anomaly preprint
   145	template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
   146	test/claim, state-drift. For each guard we record
   147	$G\colon \mathrm{risk} \to (\mathrm{disclosure}, \mathrm{evidence},
   148	\mathrm{strengthening\ build})$.
   149	
   150	\subsection{Regime}\label{ssec:regime}
   151	
   152	\textbf{Single substrate (the 600-cell).} We have not tested
   153	whether $\Cph$ on the $24$-cell, the $120$-cell, or other H$_n$
   154	Coxeter graphs would give comparable per-vertex correlations on
   155	the discrete-to-continuum agreement test, or comparable structural
   156	fits on either empirical landing. The 600-cell choice is post-hoc
   157	motivated by the empirical landings, not from an a-priori
   158	derivation. \emph{Disclosure:} \S\ref{sec:intro},
   159	\S\ref{sec:substrate}, \S\ref{sec:programme_home}.
   160	\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
   161	empirical landings of \S\ref{sec:passive_witness} and
   162	\S\ref{sec:active_witness}. \emph{Strengthening build:}
   163	\texttt{repro/verify\_kernel.py} extension to the $24$-cell and
   164	$120$-cell, with the same per-vertex correlation criterion
   165	applied; verbatim re-run of the b-anomaly fit on alternative
   166	substrates from~\citep{SmartBAnomaly2026}; the aria-chess
   167	preprint's regime section already lists alternative-polytope
   168	ablation as an open build.
   169	
   170	\textbf{Single shift ($\Ph^{-2}$).} We have not tested whether
   171	nearby shifts ($\Ph^{-2} \pm \epsilon$ for small $\epsilon$) give
   172	comparable per-vertex correlation, or whether the empirical
   173	landings tolerate a shift sweep. The shift is held fixed across
   174	both regimes; perturbation analysis is an open build.
   175	\emph{Strengthening build:} sweep $\Ph^{-2} \cdot (1 \pm \delta)$
   176	for $\delta \in \{0.01, 0.05, 0.10, 0.25\}$ on the discrete-to-
   177	continuum correlation; report sensitivity envelope.
   178	
   179	\subsection{Post-hoc}\label{ssec:posthoc}
   180	
   181	\textbf{The 600-cell choice is post-hoc justified by empirical
   182	observables.} While the construction of $\Rsixhundred$ is
   183	theorem-level rigorous (H$_4$ Coxeter group theory), the choice
   184	of \emph{this} polytope as the discrete substrate instance is
   185	motivated by the empirical landings observed, not by an a-priori
   186	geometric or algebraic argument selecting it over the $24$-cell
   187	or $120$-cell. \emph{Disclosure:} \S\ref{sec:intro}.
   188	\emph{Evidence:} two independent empirical witnesses on
   189	$\Rsixhundred$. \emph{Strengthening build:} formal substrate
   190	ablation (above).
   191	
   192	\textbf{The geometry-first variant agreement is not historically
   193	blind on b-anomaly.} Per the b-anomaly preprint's limitations
   194	section, the LHCb 2025 data was inspected first and the
   195	pure-geometry ranking was verified afterward to agree with the
   196	data-$\chi^{2}$ ranking. The two-criterion convergence is
   197	\emph{criterion-independent} (geometry-only correlation here is a
   198	different test from b-anomaly's data $\chi^{2}$) but not
   199	historically pre-registered. \emph{Disclosure:} we inherit the
   200	caveat verbatim. \emph{Strengthening build:} a future blind variant
   201	test would freeze the variant choice before observing the data
   202	$\chi^{2}$.
   203	
   204	\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
   205	$\Ph^{-2} \approx 0.382$ is a stability clamp making $\Cph$
   206	strictly positive definite; it is not derived from a closure
   207	functional or symmetry argument. \emph{Disclosure:}
   208	\S\ref{ssec:opnorm}, \S\ref{sec:definition}. \emph{Evidence:} the
   209	same operator with the same shift serves as the basis for two
   210	independent empirical witnesses across qualitatively distinct
   211	regimes (\S\ref{sec:passive_witness},
   212	\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
   213	or justify a distinguished shift under a named criterion (e.g.\
   214	minimum-amplitude amplification on a specified function class);
   215	uniqueness is not assumed and is itself an open problem.
   216	
   217	\subsection{Interpretation}\label{ssec:interpretation}
   218	
   219	\textbf{The discrete-to-continuum agreement is descriptive, not
   220	causal.} The per-vertex correlation $0.976$ between $\psi$ on
   221	$\Rsixhundred$ and the continuum kernel
   222	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the same chord radii is a
   223	\emph{computed agreement} between two independently-defined
   224	objects, not a derivation that the discrete operator equals the
   225	continuum kernel. \emph{Disclosure:} \S\ref{sec:agreement} marks
   226	this explicitly. \emph{Evidence:} the agreement is at machine
   227	precision in the operator-norm bound and at $\rho = 0.976$ in the
   228	per-vertex correlation. \emph{Strengthening build:} a formal
   229	discrete-continuum convergence proof under a specified large-graph
   230	limit; a continuum limit theorem on H$_n$ Coxeter substrates as
   231	$n \to \infty$.
   232	
   233	\textbf{Variant ranking is criterion-dependent.} The unweighted
   234	variant wins on both the geometry-only criterion of this paper
   235	and b-anomaly's data $\chi^{2}$, but neither criterion is the
   236	\emph{unique} natural ranking. Edge-weighted variants outside the
   237	$\Ph$-cocycle family ($\sqrt{\deg}$-weighted, normalised
   238	Laplacian) are not tested here. \emph{Strengthening build:}
   239	extend \texttt{repro/verify\_kernel.py} to a wider variant
   240	catalogue.
   241	
   242	\subsection{Test/claim}\label{ssec:testclaim}
   243	
   244	\textbf{Two independent empirical landings, not formal physics.}
   245	The b-anomaly result is a structural fit (kernel shape held fixed)
   246	under an AIC tie with $\mathrm{FREE\_C9}$ on current data; the
   247	aria-chess result is a substrate witness (no claim that the
   248	substrate \emph{is} consciousness). Neither lands a theorem-grade
   249	physics claim on its own domain; both are appropriately
   250	hedged in their own preprints, and we inherit those hedges
   251	verbatim. \emph{Disclosure:} \S\ref{sec:passive_witness},
   252	\S\ref{sec:active_witness}. \emph{Evidence:} the witnesses pass
   253	their own preregistered or literature-derived thresholds.
   254	\emph{Strengthening build:} more flavour-physics datasets
   255	(LHCb Run~3, Belle~II) for the passive-regime witness;
   256	cross-cohort EEG (TUH, NHM) and cross-parcellation HCP
   257	(Schaefer, Glasser) for the active-regime witness; both already
   258	listed in the respective preprints.
   259	
   260	\textbf{Discrete-to-continuum correlation reported on a single pole,
   261	verified across all $|V|$.} The headline per-vertex correlation
   262	$0.976$ is reported with the canonical pole ($+x_{0}$ axis) as
   263	source. H$_4$ transitivity predicts the correlation is invariant
   264	under choice of source vertex. \texttt{repro/verify\_kernel.py}
   265	sweeps over all $120$ vertices: every source returns the same
   266	per-vertex correlation $0.976202$ to within $\sim 10^{-15}$
   267	(\texttt{multi\_source\_sweep.max\_minus\_min} in
   268	\texttt{results.json}). The single-pole headline is therefore a
   269	representative, not a sample, of the operator's behaviour under
   270	H$_4$ transitivity.
   271	
   272	\subsection{State-drift / out-of-scope}\label{ssec:scope}
   273	
   274	\textbf{Selection layer not delivered.} As enumerated in
   275	\S\ref{sec:programme_home}, the selection-layer constructions
   276	(Lyapunov $V(W)$, edge-space decomposition under $2I$-equivariance,
   277	full reduced-flow convergence) are open in the companion ACT
   278	preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
   279	delivered here. The two empirical witnesses strengthen confidence
   280	in the response primitive without addressing the selection gap.
   281	
   282	\textbf{No deuteron / hadron / RH / capstone material is loaded
   283	into this paper.} The cascade-derivation programme, the capstone
   284	coalgebra paper, and the Millennium drafts share operator-level
   285	infrastructure with this paper but are not load-bearing here.
   286	Deliberately out of scope.
   287	
   288	\textbf{Out-of-scope items NOT delivered (correctly).}
   289	\begin{itemize}\itemsep=2pt
   290	\item Lyapunov function $V(W)$ on the reduced flow — open build
   291	  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
   292	\item $2I$-equivariance audit of the closure operator family —
   293	  open build of ACT.
   294	\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   295	  Hodge edge Laplacian — open build of ACT.
   296	\item Selection theorem identifying $\Rsixhundred$ over alternative
   297	  regular 4-polytopes — see \S\ref{ssec:regime}.
   298	\item Formal discrete-to-continuum convergence theorem under a
   299	  specified large-graph limit — see \S\ref{ssec:interpretation}.
   300	\item First-principles derivation of the $\Ph^{-2}$ shift — see
   301	  \S\ref{ssec:posthoc}.
   302	\item Family-membership classification theorem for the
   303	  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
   304	\end{itemize}
   305	
   306	\subsection{The honest verdict}
   307	
   308	The result is an \emph{operator witness}: a geometry-fixed response
   309	operator on a fixed graph, with no shape parameters tuned to any
   310	dataset, is consistent with two independent empirical landings in
   311	qualitatively distinct regimes. We do not claim the operator is
   312	the unique kernel for either landing. We do not claim selection is
   313	delivered. We do not claim 600-cell uniqueness. The strengthening
   314	builds for stronger claims are listed above and remain open.
   315	% =====================================================================
   316	\section{Conclusion}\label{sec:conclusion}
   317	% =====================================================================
   318	
   319	The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
   320	600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
   321	geometry-fixed response primitive: positive definite under
   322	(H1)--(H3) on the substrate $(M, L_M)$, and on the connected
   323	finite graph $\Rsixhundred$ where $\lambda_{\min}(L_M) = 0$ it has
   324	smallest eigenvalue $\Ph^{-2}$ and operator-norm identity
   325	$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$ (general substrates with
   326	$\lambda_{\min}(L_M) > 0$ give the strict inequality
   327	$\|\Cph^{-1}\| < \Ph^{2}$).
   328	The 600-cell instance has $|V|=120$, $|E|=720$, uniform degree
   329	$12$, $9$-shell partition $\{1,12,20,12,30,12,20,12,1\}$, and a
   330	Laplacian spectrum that numerically resolves to the closed-form
   331	$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
   332	discrete-to-continuum agreement between $\psi = \Cph^{-1} f$ and
   333	the continuum kernel $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex
   334	chord distances (non-source vertices) is Pearson $\rho = 0.976$ on
   335	the unweighted Laplacian, above the two $\Ph$-cocycle weighted
   336	variants tested ($0.888$ geometric, $0.884$ arithmetic). All numbers are reproduced from canonical
   337	generators by \texttt{repro/verify\_kernel.py}; no parameter is
   338	fitted.
   339	
   340	\textbf{Two independent empirical landings.} The same fixed
   341	$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
   342	retuning between regimes, appears as the shared response
   343	primitive underneath:
   344	\begin{enumerate}\itemsep=2pt
   345	\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
   346	  fitted dimensionless amplitude $A$ per dataset (kernel shape
   347	  held fixed) gives a sign-uniform
   348	  $\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
   349	  $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
   350	  datasets (LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015
   351	  $B_s\to\phi$).
   352	\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
   353	  recurrent self-model layer above the same operator (one
   354	  condition-dependent self-injection coupling
   355	  $\eta\in\{0,0.05,0.20\}$, one substrate-pinned nonlinearity
   356	  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
   357	  degree) passes eighteen preregistered cortical correspondences
   358	  (frozen 2026-04-18) and six drug/sleep EEG signatures.
   359	\end{enumerate}
   360	By design, the two witnesses share exactly the geometry-fixed
   361	operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
   362	$\Ph^{-2}$. Above that operator level, they share no fitted
   363	parameter, threshold, or dataset, and the empirical claims are
   364	tested on disjoint physical domains (flavour physics vs cortical
   365	neuroscience). Independence here is
   366	independence at the empirical layer above the shared operator,
   367	not statistical independence of the operator itself.
   368	
   369	\textbf{Operator-witness scope.} This is an operator witness, not
   370	a derivation of physics on either landing. We do not derive the
   371	$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
   372	claim 600-cell uniqueness; alternative regular 4-polytopes are an
   373	explicit ablation build. We do not claim kernel uniqueness on
   374	either empirical landing; the b-anomaly's free-width Gaussian
   375	alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
   376	$w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim, and the
   377	aria-chess substrate-witness scope is inherited verbatim. We do
   378	not deliver a selection theorem on the ACT
   379	4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
   380	open builds (Lyapunov $V(W)$, edge-space decomposition under
   381	$2I$-equivariance, full reduced-flow convergence) remain open and
   382	are not delivered here.
   383	
   384	\textbf{Programme position.} The cascade-programme home for the
   385	polynomial-in-$L$ Lyapunov family — RH polynomial filter
   386	($p_{\mathrm{fix}}(L)^{2}$, $\sigma$-fix-annihilator instance), YM
   387	cascade gap operator, ACT regulariser $R_{\mathrm{hom}}$ — is
   388	identified in \S\ref{sec:programme_home}. Family-membership is
   389	\emph{programme-positioned}, not formally classified. The two
   390	empirical landings strengthen external confidence in the
   391	\emph{response} primitive without reducing or addressing the
   392	selection gap.
   393	
   394	The empirical material gathered here is the operator witness; the
   395	broader programme to convert the witness into a selection-theorem-
   396	grade claim is sketched in the companion preprints and remains
   397	the natural next step.

codex
I have the kernel paper line-numbered. Next I’m checking the reproducibility artifact and the two source documents that the paper says it inherits from, because most publication-risk here is mismatched scope or mismatched numbers rather than the linear algebra itself.
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/repro/results.json' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/repro/verify_kernel.py' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba docs/aria-closure-kernel.md' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba ../BANOMALY-001/vfd-b-anomaly/README.md' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 249ms:
     1	{
     2	  "phi": 1.618033988749895,
     3	  "phi_inv_sq": 0.3819660112501051,
     4	  "n_vertices": 120,
     5	  "n_edges": 720,
     6	  "degree_sequence": {
     7	    "min": 12,
     8	    "max": 12,
     9	    "mean": 12.0
    10	  },
    11	  "connectivity": {
    12	    "n_connected_components": 1,
    13	    "connected": true
    14	  },
    15	  "shell_sizes": {
    16	    "0": 1,
    17	    "1": 12,
    18	    "2": 20,
    19	    "3": 12,
    20	    "4": 30,
    21	    "5": 12,
    22	    "6": 20,
    23	    "7": 12,
    24	    "8": 1
    25	  },
    26	  "shell_inner_products": [
    27	    1.0,
    28	    0.8090169943749475,
    29	    0.5,
    30	    0.3090169943749474,
    31	    0.0,
    32	    -0.3090169943749474,
    33	    -0.5,
    34	    -0.8090169943749475,
    35	    -1.0
    36	  ],
    37	  "antipodal_check": {
    38	    "pole_idx": 119,
    39	    "antipode_idx": 0,
    40	    "expected_shell_8_size": 1,
    41	    "observed_shell_8_size": 1
    42	  },
    43	  "laplacian_spectrum_grouped": [
    44	    {
    45	      "eigenvalue": -0.0,
    46	      "multiplicity": 1
    47	    },
    48	    {
    49	      "eigenvalue": 2.291796067500629,
    50	      "multiplicity": 4
    51	    },
    52	    {
    53	      "eigenvalue": 5.527864045000407,
    54	      "multiplicity": 9
    55	    },
    56	    {
    57	      "eigenvalue": 8.999999999999993,
    58	      "multiplicity": 16
    59	    },
    60	    {
    61	      "eigenvalue": 11.999999999999984,
    62	      "multiplicity": 25
    63	    },
    64	    {
    65	      "eigenvalue": 13.999999999999977,
    66	      "multiplicity": 36
    67	    },
    68	    {
    69	      "eigenvalue": 14.472135954999567,
    70	      "multiplicity": 9
    71	    },
    72	    {
    73	      "eigenvalue": 14.999999999999988,
    74	      "multiplicity": 16
    75	    },
    76	    {
    77	      "eigenvalue": 15.708203932499362,
    78	      "multiplicity": 4
    79	    }
    80	  ],
    81	  "operator_norm": {
    82	    "lambda_min_L": -1.01103545984405e-15,
    83	    "lambda_min_C_phi": 0.3819660112501041,
    84	    "operator_norm_C_phi_inv": 2.618033988749902,
    85	    "predicted_phi_squared": 2.618033988749895
    86	  },
    87	  "discrete_continuum_test": {
    88	    "shell_radii": [
    89	      0.0,
    90	      0.6180339887498948,
    91	      1.0,
    92	      1.1755705045849465,
    93	      1.4142135623730947,
    94	      1.618033988749895,
    95	      1.7320508075688772,
    96	      1.902113032590307,
    97	      2.0
    98	    ],
    99	    "shell_count": [
   100	      1,
   101	      12,
   102	      20,
   103	      12,
   104	      30,
   105	      12,
   106	      20,
   107	      12,
   108	      1
   109	    ],
   110	    "shell_psi_mean": [
   111	      0.11466009151487011,
   112	      0.034976446331995696,
   113	      0.024335208435661275,
   114	      0.021858804323929084,
   115	      0.019268782150762213,
   116	      0.01765857292134354,
   117	      0.016902552852001883,
   118	      0.015932370381507646,
   119	      0.01544087945358437
   120	    ],
   121	    "continuum_prediction": [
   122	      0.8090169943749475,
   123	      0.5521688638304681,
   124	      0.43606265394423777,
   125	      0.3912228691703586,
   126	      0.33757505628626344,
   127	      0.29762071978885557,
   128	      0.2773703603621507,
   129	      0.24969730865080123,
   130	      0.23503911473677247
   131	    ],
   132	    "pearson_correlation": 0.9232082699765517
   133	  },
   134	  "variant_correlation": {
   135	    "UNWEIGHTED": {
   136	      "shell_mean_correlation": 0.9232082699765517,
   137	      "per_vertex_correlation": 0.9762022978516623
   138	    },
   139	    "PHI_GEOMETRIC": {
   140	      "shell_mean_correlation": 0.879553132802029,
   141	      "per_vertex_correlation": 0.8883800503732451
   142	    },
   143	    "PHI_ARITHMETIC": {
   144	      "shell_mean_correlation": 0.8784315463215415,
   145	      "per_vertex_correlation": 0.8843640031310793
   146	    }
   147	  },
   148	  "multi_source_sweep": {
   149	    "n_sources": 120,
   150	    "min_correlation": 0.9762022978516617,
   151	    "mean_correlation": 0.9762022978516628,
   152	    "max_correlation": 0.9762022978516637,
   153	    "max_minus_min": 1.9984014443252818e-15
   154	  }
   155	}

 succeeded in 237ms:
     1	#!/usr/bin/env python3
     2	"""
     3	Aria closure kernel — numerical verification.
     4	
     5	Constructs V_600 from canonical generators, builds the short-edge
     6	nearest-neighbour graph, computes the Laplacian spectrum, builds
     7	C_phi = L + phi^-2 I, runs the discrete <-> continuum agreement
     8	test as a per-vertex Pearson correlation between psi(v) and
     9	(phi/2) exp(-|x|/phi) at each non-source vertex's chord radius
    10	(plus a shell-mean cross-check), tests the unweighted vs
    11	phi-cocycle-weighted Laplacian variants on the same geometry-only
    12	correlation criterion, sweeps the per-vertex correlation across
    13	all 120 source vertices to verify H_4 transitivity, checks
    14	graph connectedness, and writes results.json.
    15	
    16	All constants (phi, the 600-cell vertex generators, the short-edge
    17	inner product phi/2) are mathematically determined by the choice of
    18	substrate; no parameter is fitted to any dataset.
    19	
    20	Determinism: numpy RNG is seeded only for the localised-source
    21	positions (seed 42); the eigendecomposition is deterministic.
    22	
    23	Run: python3 verify_kernel.py
    24	"""
    25	
    26	from __future__ import annotations
    27	
    28	import json
    29	import itertools
    30	import math
    31	from pathlib import Path
    32	
    33	import numpy as np
    34	from numpy.linalg import eigh, norm
    35	from scipy.spatial.distance import pdist, squareform
    36	from scipy.sparse import csr_matrix
    37	from scipy.sparse.csgraph import connected_components
    38	
    39	
    40	PHI = (1.0 + math.sqrt(5.0)) / 2.0          # golden ratio
    41	INV_PHI = 1.0 / PHI                          # = phi - 1
    42	INV_PHI2 = INV_PHI * INV_PHI                 # = 2 - phi ~ 0.381966
    43	
    44	
    45	# ---------------------------------------------------------------------------
    46	# 1. 600-cell vertex construction (120 vertices on S^3)
    47	# ---------------------------------------------------------------------------
    48	
    49	def even_perms(seq):
    50	    """Return the 12 even permutations of a 4-tuple (alternating group A_4)."""
    51	    n = len(seq)
    52	    out = []
    53	    for p in itertools.permutations(range(n)):
    54	        # signature
    55	        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
    56	        if inv % 2 == 0:
    57	            out.append(tuple(seq[p[i]] for i in range(n)))
    58	    return out
    59	
    60	
    61	def build_v600():
    62	    """
    63	    Canonical 600-cell vertex set: 8 + 16 + 96 = 120 unit vectors on S^3.
    64	
    65	    - 8 vertices: all permutations of (+/- 1, 0, 0, 0)
    66	    - 16 vertices: all sign combinations of (+/- 1/2)^4
    67	    - 96 vertices: all even permutations of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0),
    68	      with all sign assignments
    69	    """
    70	    verts = set()
    71	
    72	    # 8 axis vertices
    73	    for sign in (-1, 1):
    74	        for i in range(4):
    75	            v = [0.0] * 4
    76	            v[i] = float(sign)
    77	            verts.add(tuple(v))
    78	
    79	    # 16 half-integer vertices
    80	    for signs in itertools.product((-1, 1), repeat=4):
    81	        v = tuple(0.5 * s for s in signs)
    82	        verts.add(v)
    83	
    84	    # 96 phi-mixed vertices: even perms of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0)
    85	    base = (PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0)
    86	    for signs in itertools.product((-1, 1), repeat=4):
    87	        # apply signs componentwise to (PHI/2, 1/2, 1/(2 PHI), 0); the 0 sign is irrelevant
    88	        signed = tuple(s * b for s, b in zip(signs, base))
    89	        for p in even_perms(signed):
    90	            verts.add(p)
    91	
    92	    V = np.array(sorted(verts), dtype=np.float64)
    93	    # Sanity check: all on the unit 3-sphere
    94	    radii = np.linalg.norm(V, axis=1)
    95	    assert np.allclose(radii, 1.0, atol=1e-10), \
    96	        f"vertices not on unit S^3: max |r-1| = {np.max(np.abs(radii - 1.0)):.3e}"
    97	    return V
    98	
    99	
   100	# ---------------------------------------------------------------------------
   101	# 2. Short-edge nearest-neighbour graph
   102	# ---------------------------------------------------------------------------
   103	
   104	def build_short_edge_graph(V, tol=1e-10):
   105	    """
   106	    Two vertices are connected iff <v, w> = phi/2 (the canonical short-edge
   107	    criterion on the unit 3-sphere). For the 600-cell this gives a
   108	    12-regular graph on 120 vertices with 720 edges.
   109	    """
   110	    G = V @ V.T  # Gram matrix of inner products
   111	    short = PHI / 2.0
   112	    A = (np.abs(G - short) < tol).astype(np.float64)
   113	    np.fill_diagonal(A, 0.0)  # no self-loops
   114	    return A
   115	
   116	
   117	# ---------------------------------------------------------------------------
   118	# 3. Laplacian spectrum
   119	# ---------------------------------------------------------------------------
   120	
   121	def laplacian_spectrum(A):
   122	    """L = D - A; return sorted eigenvalues + eigenvectors."""
   123	    D = np.diag(A.sum(axis=1))
   124	    L = D - A
   125	    w, U = eigh(L)  # ascending order
   126	    return L, w, U
   127	
   128	
   129	def round_spectrum(w, decimals=6):
   130	    """Group eigenvalues into multiplicity classes (within numerical tol)."""
   131	    classes = []
   132	    seen = []
   133	    for val in w:
   134	        placed = False
   135	        for idx, ref in enumerate(seen):
   136	            if abs(val - ref) < 10 ** (-decimals):
   137	                classes[idx] = (ref, classes[idx][1] + 1)
   138	                placed = True
   139	                break
   140	        if not placed:
   141	            seen.append(val)
   142	            classes.append((round(float(val), decimals), 1))
   143	    return classes
   144	
   145	
   146	# ---------------------------------------------------------------------------
   147	# 4. Closure operator and discrete Green's function
   148	# ---------------------------------------------------------------------------
   149	
   150	def build_C_phi(L):
   151	    """C_phi = L + phi^-2 I."""
   152	    return L + INV_PHI2 * np.eye(L.shape[0])
   153	
   154	
   155	def green_response(C_phi, source_idx):
   156	    """psi = C_phi^-1 e_source. Solves the linear system, no explicit inverse."""
   157	    n = C_phi.shape[0]
   158	    f = np.zeros(n)
   159	    f[source_idx] = 1.0
   160	    psi = np.linalg.solve(C_phi, f)
   161	    return psi
   162	
   163	
   164	# ---------------------------------------------------------------------------
   165	# 5. Shell decomposition (9-shell H_3 partition)
   166	# ---------------------------------------------------------------------------
   167	
   168	def shell_indices(V, pole_idx):
   169	    """
   170	    Group vertices by their inner product with V[pole_idx]. The 600-cell's
   171	    H_3 subgroup partitions the 120 vertices into 9 shells of sizes
   172	    {1, 12, 20, 12, 30, 12, 20, 12, 1} indexed by inner-product class.
   173	    """
   174	    pole = V[pole_idx]
   175	    inner = V @ pole
   176	    # The 9 canonical inner-product values:
   177	    canonical = np.array([
   178	        1.0,                # shell 0: pole itself
   179	        PHI / 2.0,          # shell 1
   180	        0.5,                # shell 2
   181	        1.0 / (2.0 * PHI),  # shell 3
   182	        0.0,                # shell 4 (equator)
   183	        -1.0 / (2.0 * PHI), # shell 5
   184	        -0.5,               # shell 6
   185	        -PHI / 2.0,         # shell 7
   186	        -1.0,               # shell 8: antipode
   187	    ])
   188	    shells = {k: [] for k in range(9)}
   189	    for i, val in enumerate(inner):
   190	        # snap to nearest canonical
   191	        k = int(np.argmin(np.abs(canonical - val)))
   192	        shells[k].append(i)
   193	    sizes = {k: len(shells[k]) for k in shells}
   194	    return shells, sizes, canonical
   195	
   196	
   197	# ---------------------------------------------------------------------------
   198	# 6. Discrete <-> continuum agreement test
   199	# ---------------------------------------------------------------------------
   200	
   201	def discrete_continuum_test(V, C_phi, source_idx):
   202	    """
   203	    Compute psi(v) = C_phi^-1 e_{source}, then average over each shell. The
   204	    shell radial coordinate x is the chord distance |v - v_source|. The
   205	    continuum prediction is G(x) = (phi/2) exp(-|x|/phi) (up to a normalisation).
   206	
   207	    Returns the per-shell discrete mean, the continuum prediction at each
   208	    shell radius, and the Pearson correlation between them.
   209	    """
   210	    psi = green_response(C_phi, source_idx)
   211	    shells, sizes, _ = shell_indices(V, source_idx)
   212	    pole = V[source_idx]
   213	
   214	    shell_means = []
   215	    shell_radii = []
   216	    shell_count = []
   217	    for k in range(9):
   218	        idxs = shells[k]
   219	        if not idxs:
   220	            continue
   221	        mean_psi = float(np.mean(psi[idxs]))
   222	        # mean chord radius from pole
   223	        chord = float(np.mean(np.linalg.norm(V[idxs] - pole, axis=1)))
   224	        shell_means.append(mean_psi)
   225	        shell_radii.append(chord)
   226	        shell_count.append(len(idxs))
   227	
   228	    shell_means = np.array(shell_means)
   229	    shell_radii = np.array(shell_radii)
   230	    continuum = (PHI / 2.0) * np.exp(-shell_radii / PHI)
   231	
   232	    # Pearson correlation of (discrete shell mean) with (continuum prediction)
   233	    if len(shell_means) > 1 and np.std(shell_means) > 0 and np.std(continuum) > 0:
   234	        corr = float(np.corrcoef(shell_means, continuum)[0, 1])
   235	    else:
   236	        corr = float("nan")
   237	
   238	    return {
   239	        "shell_radii": shell_radii.tolist(),
   240	        "shell_count": shell_count,
   241	        "shell_psi_mean": shell_means.tolist(),
   242	        "continuum_prediction": continuum.tolist(),
   243	        "pearson_correlation": corr,
   244	    }
   245	
   246	
   247	# ---------------------------------------------------------------------------
   248	# 7. Variant comparison: unweighted vs phi-cocycle weighted Laplacian
   249	# ---------------------------------------------------------------------------
   250	
   251	def cocycle_weights(V, source_idx):
   252	    """
   253	    phi-cocycle vertex weights omega_+(v) = phi^kappa(v), where kappa(v) is
   254	    the shell index of v with respect to a chosen pole. For the variant
   255	    test we compare the unweighted graph Laplacian to two weighted variants
   256	    discussed in the b-anomaly paper.
   257	    """
   258	    shells, _, _ = shell_indices(V, source_idx)
   259	    kappa = np.zeros(V.shape[0])
   260	    for k, idxs in shells.items():
   261	        for i in idxs:
   262	            kappa[i] = float(k)
   263	    return PHI ** kappa
   264	
   265	
   266	def weighted_laplacian(A, weights, mode="geometric"):
   267	    """
   268	    Weighted graph Laplacian. mode='geometric': w_{vw} = sqrt(omega(v) omega(w)).
   269	    mode='arithmetic': w_{vw} = (omega(v) + omega(w))/2.
   270	    """
   271	    n = A.shape[0]
   272	    if mode == "geometric":
   273	        W = np.sqrt(np.outer(weights, weights))
   274	    elif mode == "arithmetic":
   275	        W = 0.5 * (weights[:, None] + weights[None, :])
   276	    else:
   277	        raise ValueError(mode)
   278	    A_w = A * W
   279	    D_w = np.diag(A_w.sum(axis=1))
   280	    return D_w - A_w
   281	
   282	
   283	def variant_correlation(V, A, source_idx, variant):
   284	    if variant == "UNWEIGHTED":
   285	        L_v = np.diag(A.sum(axis=1)) - A
   286	    else:
   287	        weights = cocycle_weights(V, source_idx)
   288	        mode = "geometric" if variant == "PHI_GEOMETRIC" else "arithmetic"
   289	        L_v = weighted_laplacian(A, weights, mode=mode)
   290	    C_v = L_v + INV_PHI2 * np.eye(L_v.shape[0])
   291	    test = discrete_continuum_test(V, C_v, source_idx)
   292	    psi = green_response(C_v, source_idx)
   293	    pole = V[source_idx]
   294	    chord = np.linalg.norm(V - pole, axis=1)
   295	    # Continuum kernel at each vertex's chord radius
   296	    cont = (PHI / 2.0) * np.exp(-chord / PHI)
   297	    # Per-vertex correlation (excluding the source itself, which is degenerate)
   298	    mask = np.arange(V.shape[0]) != source_idx
   299	    if np.std(psi[mask]) > 0 and np.std(cont[mask]) > 0:
   300	        per_vertex_corr = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
   301	    else:
   302	        per_vertex_corr = float("nan")
   303	    return {
   304	        "shell_mean_correlation": test["pearson_correlation"],
   305	        "per_vertex_correlation": per_vertex_corr,
   306	        "test": test,
   307	    }
   308	
   309	
   310	# ---------------------------------------------------------------------------
   311	# 8. Operator-norm bound: ||C_phi^-1|| = 1 / lambda_min(C_phi) = phi^2
   312	# ---------------------------------------------------------------------------
   313	
   314	def connectivity_check(A):
   315	    """
   316	    Numerical connectedness verification: count connected components of the
   317	    short-edge adjacency matrix. Connectedness is reported, not derived from
   318	    a structural argument.
   319	    """
   320	    n_components, _ = connected_components(csr_matrix(A), directed=False)
   321	    return {
   322	        "n_connected_components": int(n_components),
   323	        "connected": bool(n_components == 1),
   324	    }
   325	
   326	
   327	def multi_source_sweep(V, C_phi):
   328	    """
   329	    Per-vertex correlation between psi = C_phi^-1 e_v and the continuum kernel
   330	    G(x) = (phi/2) exp(-x/phi) for every source vertex v in V. H_4 transitivity
   331	    predicts the correlation is invariant under choice of source vertex; this
   332	    function verifies the prediction numerically across all 120 sources and
   333	    reports the min/mean/max envelope.
   334	    """
   335	    n = V.shape[0]
   336	    corrs = np.zeros(n)
   337	    for source_idx in range(n):
   338	        psi = green_response(C_phi, source_idx)
   339	        chord = np.linalg.norm(V - V[source_idx], axis=1)
   340	        cont = (PHI / 2.0) * np.exp(-chord / PHI)
   341	        mask = np.arange(n) != source_idx
   342	        corrs[source_idx] = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
   343	    return {
   344	        "n_sources": int(n),
   345	        "min_correlation": float(corrs.min()),
   346	        "mean_correlation": float(corrs.mean()),
   347	        "max_correlation": float(corrs.max()),
   348	        "max_minus_min": float(corrs.max() - corrs.min()),
   349	    }
   350	
   351	
   352	def operator_norm_check(L, w):
   353	    lam_min_L = float(w[0])           # 0
   354	    lam_min_C = lam_min_L + INV_PHI2  # phi^-2
   355	    op_norm = 1.0 / lam_min_C         # phi^2
   356	    return {
   357	        "lambda_min_L": lam_min_L,
   358	        "lambda_min_C_phi": lam_min_C,
   359	        "operator_norm_C_phi_inv": op_norm,
   360	        "predicted_phi_squared": PHI ** 2,
   361	    }
   362	
   363	
   364	# ---------------------------------------------------------------------------
   365	# 9. Run everything and write results.json
   366	# ---------------------------------------------------------------------------
   367	
   368	def main():
   369	    out_path = Path(__file__).parent / "results.json"
   370	
   371	    V = build_v600()
   372	    n = V.shape[0]
   373	    A = build_short_edge_graph(V)
   374	    deg = A.sum(axis=1)
   375	    n_edges = int(A.sum() // 2)
   376	
   377	    L, w, U = laplacian_spectrum(A)
   378	    spectrum = round_spectrum(w, decimals=4)
   379	
   380	    C_phi = build_C_phi(L)
   381	    op_norm = operator_norm_check(L, w)
   382	    connectivity = connectivity_check(A)
   383	    multi_source = multi_source_sweep(V, C_phi)
   384	
   385	    # Pick the +x_0 axis vertex as canonical pole/source.
   386	    pole_idx = int(np.argmax(V @ np.array([1.0, 0.0, 0.0, 0.0])))
   387	    pole = V[pole_idx]
   388	
   389	    shells, shell_sizes, canonical_inner = shell_indices(V, pole_idx)
   390	
   391	    test = discrete_continuum_test(V, C_phi, pole_idx)
   392	
   393	    # Variant comparison on the same source
   394	    variants = {}
   395	    for variant in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
   396	        out = variant_correlation(V, A, pole_idx, variant)
   397	        variants[variant] = {
   398	            "shell_mean_correlation": out["shell_mean_correlation"],
   399	            "per_vertex_correlation": out["per_vertex_correlation"],
   400	        }
   401	
   402	    result = {
   403	        "phi": PHI,
   404	        "phi_inv_sq": INV_PHI2,
   405	        "n_vertices": n,
   406	        "n_edges": n_edges,
   407	        "degree_sequence": {
   408	            "min": int(deg.min()),
   409	            "max": int(deg.max()),
   410	            "mean": float(deg.mean()),
   411	        },
   412	        "connectivity": connectivity,
   413	        "shell_sizes": shell_sizes,
   414	        "shell_inner_products": canonical_inner.tolist(),
   415	        "antipodal_check": {
   416	            "pole_idx": pole_idx,
   417	            "antipode_idx": int(np.argmin(V @ pole)),
   418	            "expected_shell_8_size": 1,
   419	            "observed_shell_8_size": shell_sizes.get(8, 0),
   420	        },
   421	        "laplacian_spectrum_grouped": [
   422	            {"eigenvalue": ev, "multiplicity": m} for ev, m in spectrum
   423	        ],
   424	        "operator_norm": op_norm,
   425	        "discrete_continuum_test": test,
   426	        "variant_correlation": variants,
   427	        "multi_source_sweep": multi_source,
   428	    }
   429	
   430	    with open(out_path, "w") as f:
   431	        json.dump(result, f, indent=2)
   432	
   433	    # Headline summary
   434	    print("=" * 60)
   435	    print("ARIA Closure Kernel — verification")
   436	    print("=" * 60)
   437	    print(f"|V|           = {n}  (expected 120)")
   438	    print(f"|E|           = {n_edges}  (expected 720)")
   439	    print(f"degree min/max = {int(deg.min())}/{int(deg.max())}  (expected 12/12)")
   440	    print(f"connected      = {connectivity['connected']}  "
   441	          f"(components = {connectivity['n_connected_components']})")
   442	    print(f"shell sizes   = {[shell_sizes[k] for k in range(9)]}")
   443	    print(f"               (expected [1, 12, 20, 12, 30, 12, 20, 12, 1])")
   444	    print()
   445	    print("Laplacian spectrum (eigenvalue, multiplicity):")
   446	    for ev, m in spectrum:
   447	        print(f"  {ev:>8.4f}   x {m}")
   448	    print()
   449	    print(f"||C_phi^-1||  = {op_norm['operator_norm_C_phi_inv']:.6f}")
   450	    print(f"   phi^2       = {op_norm['predicted_phi_squared']:.6f}  (predicted)")
   451	    print()
   452	    print("Discrete <-> continuum agreement (Pearson correlation):")
   453	    print(f"  variant         | shell-mean  | per-vertex")
   454	    for v in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
   455	        sm = variants[v]["shell_mean_correlation"]
   456	        pv = variants[v]["per_vertex_correlation"]
   457	        print(f"  {v:<15} | {sm:>10.6f}  | {pv:>10.6f}")
   458	    print()
   459	    print(f"Multi-source sweep over all {multi_source['n_sources']} vertices:")
   460	    print(f"  per-vertex correlation min  = {multi_source['min_correlation']:.6f}")
   461	    print(f"  per-vertex correlation mean = {multi_source['mean_correlation']:.6f}")
   462	    print(f"  per-vertex correlation max  = {multi_source['max_correlation']:.6f}")
   463	    print(f"  max - min                   = {multi_source['max_minus_min']:.2e}")
   464	    print()
   465	    print(f"Wrote {out_path}")
   466	
   467	
   468	if __name__ == "__main__":
   469	    main()

 succeeded in 258ms:
     1	# vfd-b-anomaly
     2	
     3	**A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit.**
     4	
     5	[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
     6	[![Paper](https://img.shields.io/badge/paper-PDF-blue)](paper/main.pdf)
     7	
     8	This repository accompanies the preprint **[paper/main.pdf](paper/main.pdf)**. It contains all source code, processed data, intermediate result tables, and figures needed to reproduce every number in the paper from a clean checkout.
     9	
    10	---
    11	
    12	## Headline result
    13	
    14	A single fixed response kernel $\kappa(q^{2})$ — derived from the 600-cell $V_{600}$ graph regularised by the golden ratio $\varphi^{-2}$ as a discrete mass scale, **with no shape parameters tuned to data** — provides a consistent description of the $q^{2}$ behaviour of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets covering two collaborations, two isospin partners, and three decay channels. Predictions are evaluated with `flavio.np_prediction` (non-linear in $\Delta C_{9}$). Only **one dimensionless amplitude $A$** is fitted per dataset; the kernel shape itself never moves.
    15	
    16	| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
    17	|---|---|---:|---:|---:|---:|
    18	| LHCb 2015            | $B^{0}\!\to\!K^{*0}$           | 32 | $-0.24$ | $+1.24$ | $-0.96$ |
    19	| LHCb 2021            | $B^{+}\!\to\!K^{*+}$           | 32 | $+0.17$ | $+2.06$ | $-1.59$ |
    20	| CMS 2025 (no $P_{4}'$) | $B^{0}\!\to\!K^{*0}$           | 18 | $+0.47$ | $+1.05$ | $-0.81$ |
    21	| LHCb 2025            | $B^{0}\!\to\!K^{*0}$           | 32 | $+1.09$ | $+1.14$ | $-0.86$ |
    22	| LHCb 2015            | $B_{s}\!\to\!\phi$ ($S$-basis) | 24 | $-0.24$ | $+4.98$ | $-3.85$ |
    23	
    24	**What the data shows:**
    25	- **Universality.** The same fixed kernel describes all five datasets with one amplitude each — no shape retuning across datasets, channels, or isospin partners.
    26	- **Sign uniformity.** $A>0$ in **5/5** fits; $\Delta C_{9}^{\mathrm{eff}}<0$ in **5/5** fits. The kernel reproduces the established direction of the anomaly across all five independent measurements.
    27	- **Cross-channel ratio.** The $B\to K^{*}$ vs $B_{s}\!\to\!\phi$ amplitudes differ by a factor consistent with the predicted Krüger–Matias $P$-basis vs $S$-basis amplification ($\sim 2.2$), with a residual $\sim 50\%$ overshoot.
    28	- **Geometry-first variant test.** Of three discrete Laplacian variants, the unweighted choice wins on a *pure-geometry* criterion (correlation $0.997$ with the continuum kernel) decided **independently of the LHCb data**. The same variant later wins on the data $\chi^{2}$ — independent geometry and data criteria agree.
    29	
    30	**Statistical caveat (what the paper does not claim):**
    31	- On Akaike model comparison, the kernel and a constant Wilson-coefficient shift $\mathrm{FREE\_C9}$ (also $k=1$) are statistically indistinguishable on current data: stacked Akaike weight $w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$. AIC compares per-parameter goodness-of-fit and is blind to the universality/shape-prediction claim itself.
    32	- A free-width Gaussian charm-loop proxy fits comparably in $\chi^{2}$ at the cost of one extra shape parameter; the kernel is not the unique $q^{2}$ shape consistent with the anomaly.
    33	- An earlier linearised analysis (the project's "Mode B") gave a stronger numerical preference for the kernel ($\Delta\mathrm{AIC}=-1.67$ on LHCb 2025) that **did not survive the non-linear refit**. The $+2.77$-AIC-unit drift is the largest single methodological uncertainty in the project. See §2 and §4 of [the paper](paper/main.pdf) and [`reports/wo016c_nonlinear_refit.md`](reports/wo016c_nonlinear_refit.md). Linearised numbers are retained in the paper as a methodology diagnostic.
    34	
    35	The structural test the project was designed to run — *can a fixed geometry-derived shape describe the anomaly across multiple independent datasets without retuning?* — is satisfied. Whether the kernel is statistically *preferred* over a constant shift is a question current data cannot resolve and will require future $b\to s\ell\ell$ measurements.
    36	
    37	---
    38	
    39	## Figures from the paper
    40	
    41	| | |
    42	|---|---|
    43	| ![kernel shape](paper/figures/fig_F1_kernel_shape.png) | ![bin pulls](paper/figures/fig_F2_bin_pulls.png) |
    44	| **F1** Geometry-derived kernel $\kappa(q^{2})$ on the LHCb $q^{2}$ window. Solid blue: discrete $V_{600}$ shell-mean (Layer 3, used in fits). Dashed grey: continuum $e^{-|x|/\varphi}$ (Layer 1). Red points: LHCb 2025 bin centres. | **F2** Per-bin pulls on the LHCb 2025 four-observable joint fit under the non-linear FREE\_C9 ($\Delta C_{9}=-1.00$) and VFD ($A=+1.14$) fits. |
    45	
    46	![cross-dataset](paper/figures/fig_F3_cross_dataset_A.png)
    47	
    48	**F3** Non-linear best-fit amplitudes across the five fits. Green = kernel marginally favoured (LHCb 2015, $B_{s}\!\to\!\phi$); orange = constant shift marginally favoured. Right panel: $S$-basis cross-channel; grey dashed line is the basis-corrected prediction $A_{P}^{\mathrm{LHCb 2025}}\times 2.2 \approx 2.5$.
    49	
    50	---
    51	
    52	## Repository contents
    53	
    54	```
    55	vfd-b-anomaly/
    56	├── README.md                      # this file
    57	├── LICENSE                        # MIT
    58	├── CITATION.cff                   # citation metadata
    59	├── CHANGELOG.md                   # findings history (linearisation drift, etc.)
    60	├── pyproject.toml                 # Python package definition
    61	├── .gitignore
    62	│
    63	├── paper/                         # the preprint
    64	│   ├── main.pdf                   # camera-ready PDF
    65	│   ├── main.tex                   # LaTeX source
    66	│   ├── sections/                  # 10 section files
    67	│   ├── figures/                   # F1, F2, F3 (PDF + PNG)
    68	│   ├── references.bib
    69	│   └── README.md                  # how to recompile
    70	│
    71	├── src/vfd_b_anomaly/             # core library (importable as `vfd_b_anomaly`)
    72	│   ├── flavio_predictor.py        # cached flavio.sm_prediction / np_prediction wrapper
    73	│   ├── hepdata_ingest.py          # HEPData JSON loader
    74	│   ├── wo009_full_lift.py         # 600-cell V_600 graph and discrete Green's response
    75	│   ├── wo010_universality.py      # frozen kernel evaluated at bin centres
    76	│   ├── wo014_cross_dataset.py     # cross-dataset dataset loaders + linearised fit
    77	│   ├── wo015_cross_channel.py     # Bs->phi cross-channel loader + linearised fit
    78	│   └── ...                        # see src/ for the full list
    79	│
    80	├── scripts/                       # paper-headline drivers
    81	│   ├── wo016a_akaike_stack.py     # Akaike weight stacking across 5 fits
    82	│   ├── wo016b_variant_geometry.py # variant choice on pure-geometry criterion
    83	│   ├── wo016c_nonlinear_refit.py  # non-linear LHCb 2025 refit (drift diagnostic)
    84	│   ├── wo016d_nonlinear_xdataset.py  # non-linear refit across all 5 datasets
    85	│   └── wo017_paper_figures.py     # F1, F2, F3 generation
    86	│
    87	├── reports/                       # paper-headline outputs (regenerated by run_all.sh)
    88	│   ├── wo009_full_lift.{json,csv,md}  # 600-cell graph spectral data
    89	│   ├── wo016a_akaike_stack.md         # paper §6 Akaike-weight stack
    90	│   ├── wo016b_variant_geometry.md     # paper §3 variant-selection table
    91	│   ├── wo016c_nonlinear_refit.md      # paper §4 LHCb 2025 non-linear headline
    92	│   └── wo016d_nonlinear_xdataset.md   # paper §6 non-linear cross-dataset table
    93	│
    94	├── data/
    95	│   ├── raw/                       # cached HEPData submissions (CC BY 4.0)
    96	│   └── processed/                 # flavio_cache.json (regeneratable)
    97	│
    98	├── tests/                         # pytest suite
    99	├── repro/                         # reproduction driver
   100	│   └── run_all.sh
   101	└── archive/                       # superseded scripts and reports cited as
   102	                                   # supporting evidence in §5; not on the
   103	                                   # path of run_all.sh
   104	```
   105	
   106	---
   107	
   108	## Reproduce in 5 steps (clean checkout)
   109	
   110	### 1. Install the package
   111	
   112	```bash
   113	git clone https://github.com/vfd-org/b-anomaly-reproduction.git vfd-b-anomaly
   114	cd vfd-b-anomaly
   115	pip install -e ".[dev,plotting]"
   116	```
   117	
   118	This pulls in `flavio` (2.4), `wilson` (2.5), `numpy`, `scipy`, `matplotlib`, `pytest`. flavio brings the BSZ form-factor parameterisation as a transitive dependency.
   119	
   120	### 2. Cache the HEPData archives
   121	
   122	The five datasets in the paper draw from five HEPData records. The first four are bundled in `data/raw/hepdata*/` (modest size, CC BY 4.0). For LHCb 2025 (the largest), download with:
   123	
   124	```bash
   125	mkdir -p data/raw/hepdata
   126	curl -L "https://www.hepdata.net/download/submission/ins3094698/original" \
   127	     -o data/raw/hepdata/HEPData-ins3094698-v1.zip
   128	python -c "import zipfile; zipfile.ZipFile('data/raw/hepdata/HEPData-ins3094698-v1.zip').extractall('data/raw/hepdata/extracted')"
   129	```
   130	
   131	### 3. Run all paper-headline experiments
   132	
   133	```bash
   134	bash repro/run_all.sh
   135	```
   136	
   137	This runs (in order):
   138	1. The non-linear LHCb 2025 refit (`scripts/wo016c_nonlinear_refit.py`).
   139	2. The full five-dataset non-linear refit (`scripts/wo016d_nonlinear_xdataset.py`).
   140	3. The Akaike-weight stack (`scripts/wo016a_akaike_stack.py`).
   141	4. The pure-geometry variant test (`scripts/wo016b_variant_geometry.py`).
   142	5. Paper figures F1, F2, F3 (`scripts/wo017_paper_figures.py`).
   143	
   144	Total wall time: ~5 minutes on a laptop, dominated by the non-linear flavio calls. A persistent on-disk cache (`data/processed/flavio_cache.json`) ensures subsequent runs are near-instant.
   145	
   146	### 4. Recompile the paper (optional)
   147	
   148	The PDF at `paper/main.pdf` is shipped pre-built. To regenerate from source:
   149	
   150	```bash
   151	# install tectonic once (~50 MB, single static binary, no sudo needed)
   152	curl -L https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.15.0/tectonic-0.15.0-x86_64-unknown-linux-musl.tar.gz | tar -xz -C ~/.local/bin/
   153	
   154	# compile
   155	~/.local/bin/tectonic -X compile paper/main.tex
   156	```
   157	
   158	See `paper/README.md` for compile alternatives (TeX Live, Overleaf).
   159	
   160	### 5. Run tests
   161	
   162	```bash
   163	pytest -q
   164	```
   165	
   166	---
   167	
   168	## Contents of the paper
   169	
   170	The 25-page preprint (`paper/main.pdf`) has 10 sections:
   171	
   172	| § | content |
   173	|---|---|
   174	| 1 | Introduction; scope and epistemic status |
   175	| 2 | Datasets, SM backend (non-linear flavio + linearised Mode B), reproducibility ledger |
   176	| 3 | Three-layer kernel construction: continuum $\varphi$-tuned Green's function → bounded Dirichlet eigenmode → discrete 2I-equivariant lift on $V_{600}$. Variant-selection table on pure-geometry vs LHCb-data criteria. |
   177	| 4 | Results on LHCb 2025: non-linear vs linearised, drift table, leave-one-observable-out |
   178	| 5 | Stress tests on LHCb 2025 under Mode B (bin bootstrap, region splits, alternative Wilson-coefficient models, charm-loop Gaussian, BSZ form-factor MC) |
   179	| 6 | Cross-dataset non-linear fit across five datasets; Akaike-weight stack; sign-uniformity test |
   180	| 7 | Cross-channel fit on $B_{s}\!\to\!\phi$; basis-effect explanation of the amplitude gap |
   181	| 8 | Discussion: why the linearisation breaks; three readings of sign uniformity |
   182	| 9 | Limitations (linearisation issue is the lead) |
   183	| 10 | Conclusion; falsification programme; reproducibility |
   184	
   185	The paper went through three rounds of internal hostile review. The major finding from Round 2 was that the linearised fit's $\Delta\mathrm{AIC}=-1.67$ on LHCb 2025 flipped to $+1.09$ under a non-linear refit; the paper was rewritten around that negative finding and accepted as preprint-ready in Round 3.
   186	
   187	---
   188	
   189	## License and data attribution
   190	
   191	- **Project code** (everything under `src/`, `scripts/`, `tests/`, `repro/`, `paper/`): MIT licence — see [`LICENSE`](LICENSE).
   192	- **Cached HEPData supplementary archives** under `data/raw/`: © CERN for the benefit of the LHCb and CMS collaborations, distributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The canonical citation for each archive is the corresponding HEPData record:
   193	  - LHCb 2025: [HEPData ins3094698](https://www.hepdata.net/record/ins3094698) (DOI [10.17182/hepdata.167733.v1](https://doi.org/10.17182/hepdata.167733.v1))
   194	  - LHCb 2015 $K^{*}$: [HEPData ins1409497](https://www.hepdata.net/record/ins1409497)
   195	  - LHCb 2021 $B^{+}\!\to\!K^{*+}$: [HEPData ins1838196](https://www.hepdata.net/record/ins1838196)
   196	  - CMS 2025: [HEPData ins2850101](https://www.hepdata.net/record/ins2850101)
   197	  - LHCb 2015 $B_{s}\!\to\!\phi$: [HEPData ins1380188](https://www.hepdata.net/record/ins1380188)
   198	- **flavio** ([arXiv:1810.08132](https://arxiv.org/abs/1810.08132)) and **wilson** ([arXiv:1804.05033](https://arxiv.org/abs/1804.05033)) provide the SM and non-linear new-physics predictions used as the headline backend; their licences are upstream.
   199	
   200	## Citation
   201	
   202	If you use this software or the accompanying paper, see [`CITATION.cff`](CITATION.cff). Suggested BibTeX:
   203	
   204	```bibtex
   205	@misc{Smart2026vfdBAnomaly,
   206	  author       = {Smart, Lee},
   207	  title        = {A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit},
   208	  year         = {2026},
   209	  url          = {https://github.com/vfd-org/b-anomaly-reproduction/blob/main/paper/main.pdf},
   210	  note         = {Preprint, Institute of Vibrational Field Dynamics}
   211	}
   212	```
   213	
   214	For the LHCb 2025 dataset the project rests on, also cite:
   215	
   216	```bibtex
   217	@article{LHCb:2025BKstmumuComp,
   218	  author       = {{LHCb Collaboration}},
   219	  title        = {A comprehensive analysis of the $B^0\to K^{*0}\mu^+\mu^-$ decay},
   220	  eprint       = {2512.18053},
   221	  archivePrefix= {arXiv},
   222	  primaryClass = {hep-ex},
   223	  year         = {2025},
   224	  reportNumber = {LHCb-PAPER-2025-041, CERN-EP-2025-278},
   225	  doi          = {10.17182/hepdata.167733.v1}
   226	}
   227	```

 succeeded in 271ms:
     1	# ARIA Closure-Response Green Kernel and the Cascade Programme
     2	
     3	**Status (2026-04-29).** Programme-level vocabulary: response
     4	primitive defined; externally witnessed by a structural sign-uniform
     5	test (b-anomaly paper, §4 below) without a model-preference claim;
     6	selection / crystallisation dynamics still open. This note is
     7	non-load-bearing for any individual Millennium paper; it documents
     8	the programme-wide home for the polynomial-in-$L$ Lyapunov family
     9	that recurs across the Millennium drafts.
    10	
    11	## 1. The closure-response operator
    12	
    13	Let $M$ be a closure substrate (graph, simplicial complex, or
    14	projected coordinate). Let $L_M$ be its Laplacian. Define the
    15	**$\varphi$-regularised closure operator**
    16	$$
    17	C_\varphi \;=\; L_M + \varphi^{-2} I.
    18	$$
    19	For a non-negative localised source $f$ on $M$, the **closure
    20	response field** is
    21	$$
    22	\psi \;=\; C_\varphi^{-1} f \;=\; (L_M + \varphi^{-2} I)^{-1} f.
    23	$$
    24	This is a Green's-function inverse. For self-adjoint non-negative
    25	$L_M$ on $M$ (e.g. the standard graph Laplacian on a connected
    26	finite graph, or the standard continuum Laplace operator with
    27	free-space / decay-at-infinity boundary conditions), $C_\varphi$
    28	is positive definite and $\varphi^{-2}$ acts as a coherence-length /
    29	mass regularisation; for a non-negative source $f$ on such an $M$,
    30	$\psi$ is non-oscillatory and centred on the support of $f$. In
    31	the continuum case with smooth $f$, $\psi$ is regular away from
    32	the singular support of $f$. (On a finite graph, "smoothness" is
    33	not directly meaningful; the regularity statement is a discrete
    34	exponential-decay envelope around the source, not a derivative
    35	condition.) Substrates outside this hypothesis class (e.g.
    36	projected coordinates with non-standard boundary conditions, or
    37	Laplacians with negative spectrum) require their own analysis.
    38	
    39	## 2. Continuum projection
    40	
    41	In one projected coordinate $x$, $L_\varphi = -d^2/dx^2 + \varphi^{-2}$,
    42	$L_\varphi G = \delta$, with closed-form Green's function
    43	$$
    44	G(x) \;=\; \frac{\varphi}{2}\, e^{-|x|/\varphi}.
    45	$$
    46	Normalised, this is the practical kernel
    47	$\kappa(x) = e^{-|x|/\varphi}$. The decay scale is $\varphi$.
    48	
    49	## 3. Discrete substrate: the 600-cell
    50	
    51	The discrete VFD lift uses the 600-cell graph $V_{600}$:
    52	- 120 vertices, 720 edges, each vertex degree 12;
    53	- edges defined by $\langle v, w \rangle = \varphi/2$;
    54	- 9-shell decomposition emerging intrinsically as
    55	  $\{1, 12, 20, 12, 30, 12, 20, 12, 1\}$;
    56	- antipodal symmetry $s(-v) = 8 - s(v)$.
    57	
    58	The discrete response is
    59	$\psi(v) = (L_{V_{600}} + \varphi^{-2} I)^{-1} f(v)$.
    60	
    61	**Compression diagnostic.** The b-anomaly headline fits use the
    62	full Green response on $V_{600}$. A spectral truncation diagnostic
    63	(`archive/reports/wo011_spectral.csv`) reports the relative
    64	reconstruction error stepping from $0.076$ (modes 1-8, with
    65	$\lambda_{\max}$ reaching $5.528$ at mode 6) to $0.040$ (modes
    66	9-14) and remaining at $0.040$ through mode 30; mode 15 marks the
    67	entry of the truncation into the $\lambda = 9$ block, not an
    68	additional error drop. This is a *spectral diagnostic of
    69	compression depth*, not a rank-1 projection map; the b-anomaly
    70	fits do not use the truncation. (The canonical full spectrum of
    71	the $V_{600}$ Laplacian has eigenvalue $9$ with multiplicity $16$;
    72	the multiplicity-6 figure originally reported in some prose is
    73	not consistent with the canonical spectrum or with the b-anomaly's
    74	own wo011 CSV and is dropped here.)
    75	
    76	## 4. Empirical validation: shipped five-dataset b-anomaly structural test
    77	
    78	Independent passive-regime witness for $C_\varphi$ ships in the
    79	b-anomaly repository (`/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/`,
    80	preprint `paper/main.pdf`, repro `repro/run_all.sh`). The witness is
    81	a **structural** test, not a detection claim or AIC preference:
    82	
    83	> A single fixed response kernel $\kappa(q^{2})$ — derived from the
    84	> 600-cell $V_{600}$ graph regularised by $\varphi^{-2}$ as a
    85	> discrete mass scale, with no shape parameters tuned to data —
    86	> provides a consistent description of the $q^{2}$ behaviour of the
    87	> $b\to s\mu^{+}\mu^{-}$ angular anomaly across **five public
    88	> datasets covering two collaborations, two isospin partners, and
    89	> three decay channels**. Only one dimensionless amplitude $A$ is
    90	> fitted per dataset; the kernel shape itself never moves.
    91	
    92	**Per-dataset table** (verbatim from `BANOMALY-001/vfd-b-anomaly/README.md`):
    93	
    94	| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
    95	|---|---|---:|---:|---:|---:|
    96	| LHCb 2015            | $B^{0}\!\to\!K^{*0}$           | 32 | $-0.24$ | $+1.24$ | $-0.96$ |
    97	| LHCb 2021            | $B^{+}\!\to\!K^{*+}$           | 32 | $+0.17$ | $+2.06$ | $-1.59$ |
    98	| CMS 2025 (no $P_{4}'$) | $B^{0}\!\to\!K^{*0}$           | 18 | $+0.47$ | $+1.05$ | $-0.81$ |
    99	| LHCb 2025            | $B^{0}\!\to\!K^{*0}$           | 32 | $+1.09$ | $+1.14$ | $-0.86$ |
   100	| LHCb 2015            | $B_{s}\!\to\!\phi$ ($S$-basis) | 24 | $-0.24$ | $+4.98$ | $-3.85$ |
   101	
   102	**What the b-anomaly paper claims (source scope; bullets summarise from `README.md:24-28` plus paper §§6-7 detail):**
   103	
   104	- **Universality.** Same fixed kernel for all five datasets, one
   105	  amplitude per dataset, no shape retuning.
   106	- **Sign uniformity.** $A>0$ in **5/5** fits;
   107	  $\Delta C_{9}^{\mathrm{eff}}<0$ in **5/5** fits. The kernel
   108	  reproduces the established direction of the anomaly across all
   109	  five independent measurements.
   110	- **Cross-channel ratio.** $B\to K^{*}$ vs $B_{s}\!\to\!\phi$
   111	  amplitudes differ by a factor partly explained by the predicted
   112	  Krüger–Matias $P$/$S$-basis amplification ($\sim 2.2$). The
   113	  detailed cross-channel section reports a predicted amplitude of
   114	  $+2.5$ vs the observed $+4.98$, leaving a factor $\sim 2$
   115	  residual gap that the basis-amplification prediction does not
   116	  account for.
   117	- **Geometry-first variant test.** Of three discrete Laplacian
   118	  variants, the unweighted choice wins on a pure-geometry criterion
   119	  (correlation $0.997$ with the continuum kernel); the same variant
   120	  also wins on the data $\chi^{2}$ — independent geometry and data
   121	  criteria agree. The two-criterion agreement is criterion-independent
   122	  but not historically blind: the b-anomaly limitations section
   123	  (`paper/sections/09_limitations.tex`) acknowledges that the data
   124	  was looked at first and only later verified to agree with the
   125	  pure-geometry ranking.
   126	
   127	**Statistical caveat (what the b-anomaly paper does NOT claim):**
   128	
   129	- On Akaike model comparison, the kernel and a constant
   130	  Wilson-coefficient shift ($\mathrm{FREE\_C9}$, also $k=1$) are
   131	  statistically indistinguishable on current data: stacked
   132	  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
   133	  Current data cannot resolve the model comparison. AIC is blind to
   134	  the universality/shape-prediction claim itself.
   135	- In the Mode-B stress test, a free-width Gaussian charm-loop
   136	  proxy fits comparably in $\chi^{2}$ at the cost of one extra
   137	  shape parameter; the kernel is *not* the unique $q^{2}$ shape
   138	  consistent with the anomaly.
   139	- An earlier linearised "Mode B" analysis gave a stronger
   140	  numerical preference for the kernel
   141	  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that **did not
   142	  survive the non-linear refit**. The $+2.77$-AIC-unit drift is the
   143	  largest single methodological uncertainty in the project.
   144	
   145	**Cocycle convergence (operator-level, not edge-weight-level).**
   146	The b-anomaly geometry-first variant test compares three discrete
   147	edge-weighting schemes on $V_{600}$ — `UNWEIGHTED`,
   148	`PHI_GEOMETRIC` ($w_{vw} = \sqrt{\omega_+(v)\,\omega_+(w)}$ with
   149	$\omega_+(v) = \varphi^{\kappa(v)}$), and `PHI_ARITHMETIC`
   150	($w_{vw} = \tfrac{1}{2}[\omega_+(v) + \omega_+(w)]$) — under
   151	both a pure-geometry criterion (correlation with the continuum
   152	kernel) and a data criterion (LHCb 2025 $\chi^2$). The
   153	`UNWEIGHTED` Laplacian variant wins on both criteria
   154	(correlation $0.9968$ with the continuum kernel, data
   155	$\chi^2 = 13.555$; b-anomaly paper §3.4 Table 1, also
   156	`reports/wo016b_variant_geometry.md`). The φ-cocycle-weighted
   157	variants ($\omega_+(v) = \varphi^{\kappa(v)}$) are tested and
   158	**lose** on both criteria. So the b-anomaly result empirically
   159	strengthens the **unweighted** $L_{V_{600}} + \varphi^{-2} I$
   160	response operator and the 9-shell projection (which enters at the
   161	shell-mean step, not as an edge weight); it does **not**
   162	empirically strengthen the κ cocycle as an operative edge
   163	weighting.
   164	
   165	The cocycle convergence with the RH paper's pentagonal-clock
   166	$\kappa(v) = (s(v) - 4)^2$ (`papers/millennium-rh-formal/rh-formal.tex`,
   167	Definition `def:kappa`) is therefore **structural**: the same
   168	shell-grade pattern $\varphi^{0,1,4,9,16}$ shows up in both the
   169	discrete VFD lift's variant catalogue and the RH paper's cocycle.
   170	This is a theoretical convergence on a shared algebraic shell-grade
   171	infrastructure, not an empirical claim. ẑ **shares operator-level
   172	infrastructure** with the b-anomaly response operator (the same
   173	$V_{600} + \varphi^{-2} I$, the same 9-shell decomposition, the
   174	same shell-grade pattern $\varphi^{0,1,4,9,16}$); ẑ does **not**
   175	inherit any empirical claim about classical RH or the critical
   176	line.
   177	
   178	## 5. Programme home for cascade Lyapunov / projector functionals
   179	
   180	Several cascade-internal constructions are $L$-symmetric
   181	polynomial-in-$L$ functionals on a finite-dimensional substrate.
   182	They are positioned as programme-proposed members of the same
   183	family as $C_\varphi$ (the family-membership claim is not formally
   184	canonical and is not proved in any of the cited Millennium drafts):
   185	
   186	- **RH polynomial filter** (`rh-formal.tex`,
   187	  `def:closure_flow`): $F_{\mathrm{filt}}(x)
   188	  = \tfrac{1}{2}\langle x, p_{\mathrm{fix}}(L)^2 x\rangle$ with
   189	  $\Psi_t = e^{-t\,p_{\mathrm{fix}}(L)^2}$. Programme-positioned
   190	  as the **σ-fix-annihilator** instance of the family: a
   191	  degree-$10$ positive functional on $\R^{120}$ vanishing exactly
   192	  on $V_{\mathrm{fix}}$.
   193	- **YM cascade gap operator** (`ym-mass-gap.tex`,
   194	  Section~\ref{sec:cascade-gap}): the discrete cascade gap
   195	  Hamiltonian is programme-positioned as a $C_\varphi$-style
   196	  mass-regularised Laplacian on the 600-cell substrate.
   197	- **NS regularity functional** (`ns-formal.tex`): the cascade
   198	  hydrodynamic projector is programme-positioned in the same
   199	  Lyapunov-of-polynomial-in-$L$ family.
   200	- **BSD operator** (`bsd-formal.tex`): $T_E$ on the enlarged
   201	  Hecke module is programme-positioned as a
   202	  response-operator-family member.
   203	- **Hodge $\sigma$-projector** (`hodge-formal.tex`): the cascade
   204	  $\sigma$-projector is programme-positioned as a rank-1 /
   205	  spectral-projection limit of the same family.
   206	- **PNP cascade refinement** (`pnp-formal.tex`): the cascade
   207	  refinement on the restricted model class is programme-positioned
   208	  as a response-kernel projection in the bounded-resource regime.
   209	
   210	In each case the cascade construction is positioned as a
   211	programme-proposed family instance, selected by the structural role
   212	it plays in the corresponding Millennium reduction. These are not
   213	arbitrary constructions, but the family-membership claim is not
   214	formally canonical and is not proved in any of the cited papers.
   215	
   216	## 6. Response vs selection: the open layer
   217	
   218	The closure response primitive now has a **shipped passive-regime
   219	empirical landing**: the b-anomaly paper (§4 above) tests the fixed
   220	$C_\varphi$-derived $V_{600}$ kernel without shape retuning across
   221	five public flavour-physics datasets covering two collaborations,
   222	two isospin partners, and three decay channels. This **does not
   223	close the selection layer**. The active-regime companion remains
   224	the ARIA / aria-chess selection paper: a learning-rule / Lyapunov /
   225	coherence-descent construction for $W$-space, *not supplied* by
   226	b-anomaly.
   227	
   228	The closure response $\psi = C_\varphi^{-1} f$ is derived from
   229	geometry. It is *not* a selection rule. Crystallisation
   230	additionally requires a selection dynamic — a Lyapunov / coherence
   231	descent rule
   232	$$
   233	dW/dt \;=\; -\nabla V(W)
   234	$$
   235	or equivalent — that selects which response is the stable
   236	attractor.
   237	
   238	This selection layer is **open**. The same gap appears in three
   239	independent frames:
   240	- **RH paper**: open $\textup{H}_{\mathrm{attr}}$ at the level of
   241	  the original cascade closure functional (the polynomial filter
   242	  $\Psi_t$ is only a finite-dimensional analogue, by design).
   243	- **Adaptive Closure Transport** (`papers/adaptive-closure-transport/`):
   244	  edge-space lift / Lyapunov mechanism for the selection programme,
   245	  explicitly left open (lines 327--328, 377--382 of that paper).
   246	- **ARIA framework**: crystallisation / coherence-descent rule,
   247	  named as the next layer above response. The aria-chess paper
   248	  (active-regime empirical companion to adaptive-closure-transport)
   249	  is **named, not yet written**.
   250	
   251	The convergence of the gap across these three frames is the
   252	strongest programme-level indication that the gap is a single
   253	mathematical problem rather than three independent ones (a
   254	programme-level reading, not a proof of equivalence). The
   255	passive-regime b-anomaly landing strengthens external confidence
   256	in the *response* primitive without reducing or addressing the
   257	selection gap.
   258	
   259	## 7. Canonical references in this repository
   260	
   261	- `papers/millennium-rh-formal/rh-formal.tex` — polynomial filter
   262	  $F_{\mathrm{filt}}$ as σ-fix-annihilator family member (closing
   263	  subsection).
   264	- `papers/millennium-ym/ym-mass-gap.tex` — cascade gap operator as
   265	  $C_\varphi$-style member.
   266	- `papers/millennium-ns-formal/ns-formal.tex` — regularity
   267	  functional as family member.
   268	- `papers/millennium-bsd-formal/bsd-formal.tex` — $T_E$ as
   269	  family member.
   270	- `papers/millennium-hodge-formal/hodge-formal.tex` — σ-projector
   271	  as rank-1 limit.
   272	- `papers/millennium-pnp-formal/pnp-formal.tex` — cascade
   273	  refinement as response-kernel projection.
   274	- `papers/adaptive-closure-transport/adaptive-closure-transport.tex` —
   275	  selection layer, open.
   276	- `docs/convergence-with-smart.md` — programme-level architectural
   277	  consilience between cascade and Smart frames.
   278	- `docs/projection-narrative.md` (and related) — Layer 1 mainstream
   279	  coherence earning Layer 2 realisation.
   280	- `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.pdf` —
   281	  primary shipped passive-regime empirical witness for the fixed
   282	  $C_\varphi$-derived $V_{600}$ kernel; five-dataset sign-uniform
   283	  structural test (LHCb + CMS, $K^{*0}/K^{*+}/\phi$ channels) with
   284	  honest AIC tie ($w_{\mathrm{VFD}} = 0.348$ vs
   285	  $w_{\mathrm{FREE\_C9}} = 0.652$) and Mode-B $+2.77$ drift caveat.
   286	- `BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md` —
   287	  Layer 1 + Layer 2 derivation (supporting).
   288	- `BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md` —
   289	  Layer 3 numerical bridge (supporting).
   290	- `BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md` —
   291	  variant-selection table; the unweighted Laplacian wins on both
   292	  pure-geometry and data $\chi^2$ criteria.
   293	- `BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md` —
   294	  Mode-B drift documentation; the largest single methodological
   295	  uncertainty in the project.

codex
The reproducibility JSON matches the paper’s main graph and correlation numbers at first pass. I’m now reading the aria-chess paper itself, because the active-witness paragraph imports many specific tallies and the phrasing has to stay at substrate-witness scope.
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/main.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/01_introduction.tex papers/aria-chess-paper/paper/sections/02_method.tex papers/aria-chess-paper/paper/sections/03_substrate.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex papers/aria-chess-paper/paper/sections/05_results.tex papers/aria-chess-paper/paper/sections/06_stress_tests.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/07_cross_domain.tex papers/aria-chess-paper/paper/sections/08_discussion.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/sections/09_limitations.tex papers/aria-chess-paper/paper/sections/10_conclusion.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 337ms:
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

 succeeded in 335ms:
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
   171	% =====================================================================
   172	\section{Methods and provenance}\label{sec:method}
   173	% =====================================================================
   174	
   175	This section is a provenance ledger. It records, for each empirical
   176	claim downstream, the dataset, the preregistration date and document,
   177	the validation script, the seed range, the threshold, and the
   178	wallclock — the minimal information a hostile reviewer needs to
   179	reproduce or refute the claim.
   180	
   181	\subsection{Preregistration discipline}
   182	
   183	\textbf{Frozen 2026-04-18.} Eighteen quantitative predictions
   184	(P1--P18) were locked on 2026-04-18 in
   185	\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any validation
   186	run. Each prediction has (i) a specific numerical claim, (ii) a
   187	falsifiable threshold, (iii) the validation test (script + seed range),
   188	and (iv) a rationale identifying what would falsify it.
   189	
   190	\textbf{Frozen 2026-04-24.} Two later batteries — H$_4$ fingerprint
   191	predictions and rung observables — were preregistered on 2026-04-24
   192	in \texttt{docs/brain\_mapping/PREREG\_H4\_FINGERPRINT.md} and
   193	\texttt{docs/brain\_mapping/PREREG\_RUNG\_OBSERVABLES.md}. \emph{We do
   194	not include those batteries in the headline 18/18 tally.} They are
   195	listed as future strengthening builds in~\S\ref{sec:limitations}.
   196	
   197	\textbf{Six EEG signatures (set B).} The drug/sleep signatures on the
   198	recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six companion
   199	biological signatures with literature-derived thresholds (NREM-N3
   200	variance ratio, propofol switching ratio, propofol continuity drop,
   201	propofol $\Phi$ collapse, recovery reversibility, wake
   202	cascade-$\alpha$). They are not part of the P1--P18 preregistration;
   203	they are reported as a companion validation set on the recurrent
   204	layer.
   205	
   206	\textbf{No threshold has been modified post-hoc.} Where the original
   207	2026-04-20 validation reported failures (P3, P4, P13), the documented
   208	methodological refinements were
   209	(a)~increasing $N$ from $3$ to $5$ for cascade interaction terms,
   210	(b)~adding a $N\!=\!20$ deep-dive for the highest-variance interaction
   211	(P4, C$\times$P), and
   212	(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
   213	measurements for the chess LOO test (P13). None of these touched a
   214	preregistered threshold.
   215	
   216	\subsection{Provenance ledger}
   217	
   218	We write the provenance map as $\Pi\colon\{\text{claim id}\}
   219	\to (\text{script}, \text{seed range}, \text{dataset/source},
   220	\text{threshold}, \text{result})$.
   221	
   222	\begin{table}[ht]
   223	\centering
   224	\small
   225	\caption{Provenance ledger for the headline empirical claims.}
   226	\label{tab:provenance}
   227	\begin{tabular}{l l l l l}
   228	\toprule
   229	Claim & Script & Seed range & Dataset / source & Threshold \\
   230	\midrule
   231	P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
   232	P2 ($C$ main) & same & 30010--30014 & this paper & $\geq +0.30$ \\
   233	P3 ($|D{\times}C|$) & same & 30020--30024 & this paper & $|\cdot| < 0.20$ \\
   234	\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
   235	P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
   236	P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
   237	P7 ($W{\to}N3$ var) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.70$ \\
   238	P8 ($W{\to}N3$ switch) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.50$ \\
   239	P9 (chess 5-fold) & same & 30200--30204 & 32 positions, 4 cat. & $\geq 70\%$ \\
   240	P10 (chess null) & \texttt{run\_chess\_robustness.py} & 30210 & same & $\geq 50\%$ \\
   241	P11 (chess random-label) & same & 30210+ & same & $\in [15\%, 35\%]$ \\
   242	P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
   243	\textbf{P13 (chess sub.\ lift)} & same & with reset & same (LOO refinement) & $\geq +15$pp \\
   244	P14 (conv 5-fold) & same & 30220--30224 & 64 utt., 8 cat. & $\geq 75\%$ \\
   245	P15 ($|$conv lift$|$) & same & same & same & $|\cdot| < 10$pp \\
   246	P16 (conv null) & \texttt{run\_conversation\_robustness.py} & 30210 & same & $\geq 50\%$ \\
   247	P17 (ARIA deg std) & substrate construction & deterministic & H$_4$ theorem & $=0$ \\
   248	P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
   249	\midrule
   250	Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
   251	\bottomrule
   252	\end{tabular}
   253	\end{table}
   254	
   255	\subsection{Datasets and DOIs}
   256	
   257	\textbf{Sleep-EDFx (PhysioNet).} Public polysomnography
   258	recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
   259	the cortical-avalanche $\alpha$ baseline; $n=24$ subjects used for
   260	the wake$\to$N3 variance and switching ratios. Cortical-avalanche
   261	fitting follows the Beggs--Plenz log-CCDF
   262	methodology~\citep{BeggsPlenz2003}.
   263	
   264	\textbf{OpenNeuro \texttt{ds005620}.} Propofol-induced loss of
   265	consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
   266	DOI \texttt{10.18112/openneuro.ds005620.v1.0.0}. Used as the
   267	empirical reference for the propofol switching ratio
   268	($2.96\!\times$ wake) in Sig~2.
   269	
   270	\textbf{OpenNeuro \texttt{ds004902}.} DMT-induced altered states
   271	EEG~\citep{OpenNeuroDS004902},
   272	DOI \texttt{10.18112/openneuro.ds004902.v1.0.8}. Background
   273	psychedelic-state reference; not load-bearing for the headline tally.
   274	
   275	\textbf{Zenodo \texttt{3992359}.} DMT EEG public
   276	release~\citep{ZenodoDMT3992359},
   277	DOI \texttt{10.5281/zenodo.3992359}. Same status as above.
   278	
   279	\textbf{HCP S1200.} Human Connectome Project
   280	S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
   281	matrix. The preregistered test (P18) was on $n=100$ subjects for
   282	computational tractability; full-cohort $n=1003$ statistics
   283	(degree std, participation ratio, clustering coefficient $\sigma$-
   284	distances) are reported as descriptive statistics on top of the
   285	preregistered test.
   286	
   287	\textbf{Microstate baseline (qualifier).} The continuity-drop
   288	signature (Sig~3) follows the EEG microstate methodology lineage of
   289	Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
   290	microstates. Brodbeck et al.\ is not a propofol-specific paper; we
   291	use it for the underlying microstate-fragmentation methodology, not
   292	as a propofol reference. A propofol-specific microstate citation
   293	would tighten this section; we treat that as an open
   294	strengthening build.
   295	
   296	\subsection{Statistical methods}
   297	
   298	\textbf{Cascade-$\alpha$ fitting.} Power-law $\alpha$ is fit by
   299	ordinary least squares on the log-CCDF of the cascade-event size
   300	distribution, restricted to the central 80\% mass band (excluding the
   301	bottom 10\% and top 10\% to avoid extreme-tail noise). $R^{2}$ is
   302	reported on the linear fit in log-space. A cascade event is defined
   303	as an attention-vertex shift between consecutive ticks
   304	$\arg\max|\mathrm{state}_{t}|\neq \arg\max|\mathrm{state}_{t-1}|$;
   305	the event size is the $\ell^{1}$ norm of the state-difference vector
   306	at that tick. Zero-size events are excluded.
   307	
   308	\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
   309	estimated by event-resampling bootstrap (500 resamples for the
   310	preregistered cascade-$\alpha$ tests, 2000 resamples for the
   311	$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
   312	preregistered; 42 for the deep-dive.
   313	
   314	\textbf{Bootstrap one-sided $P$-value reporting.} For the C$\times$P
   315	deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
   316	$0/2000$ were below the preregistered floor $+0.10$; we report these
   317	as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
   318	zero-probability statement on a finite resample.
   319	
   320	\textbf{Factorial interaction estimator.} For the $2{\times}2$
   321	ablation conditions $\{----, -C--, --P-, -CP-\}$, the interaction is
   322	\[
   323	\Delta_{CP}
   324	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
   325	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
   326	\]
   327	
   328	\textbf{$\sigma$-distance against external nulls.} For the HCP
   329	comparisons we report
   330	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
   331	on the full $n=1003$ subject distribution.
   332	
   333	\subsection{State-reset protocol}
   334	
   335	The substrate exhibits state drift: across approximately five
   336	successive depth-sweep evaluations the pressure field equilibrates
   337	to a uniform attractor and classification structure collapses to
   338	raw-feature baseline. Multi-trial benchmarks therefore require an
   339	explicit reset between successive evaluations.
   340	\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
   341	re-initialises pressure-field, crossed-vertex, and training state to
   342	canonical baseline. With reset between depth measurements, the chess
   343	LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
   344	substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
   345	preregistered floor). The reset protocol is documented in
   346	\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
   347	generalisable lesson is recorded in \S\ref{sec:limitations}: any
   348	multi-trial benchmark on a non-stationary substrate must specify
   349	state-reset protocol.
   350	
   351	\subsection{Reproducibility commands}
   352	
   353	\begin{itemize}\itemsep=2pt
   354	\item Substrate self-test:
   355	  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
   356	\item Six drug/sleep signatures:
   357	  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
   358	\item C$\times$P synergy $N\!=\!20$ deep-dive:
   359	  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
   360	\item Eighteen preregistered:
   361	  \texttt{python3 run\_preregistered\_validation.py}
   362	  ($\sim 18$\,min).
   363	\item Whole-paper repro:
   364	  \texttt{bash reproduce\_paper\_claims.sh}.
   365	\end{itemize}
   366	
   367	All scripts are deterministic given seeds. Reruns at seed $42$ on the
   368	recurrent layer should reproduce per-condition means in this paper to
   369	4~decimal places. Bootstrap CIs may differ in the 4th decimal due to
   370	NumPy version differences in the bootstrap RNG; the qualitative
   371	verdicts (CI overlaps, $P$-value thresholds) are unaffected.
   372	% =====================================================================
   373	\section{The 600-cell response substrate}\label{sec:substrate}
   374	% =====================================================================
   375	
   376	This section constructs the substrate. \S\ref{ssec:vertices}
   377	gives the vertex set. \S\ref{ssec:graph} gives the graph and its
   378	computed Laplacian spectrum. \S\ref{ssec:cphi} gives the response
   379	operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
   380	\S\ref{ssec:shells} gives the 9-shell decomposition used for source
   381	projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
   382	descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
   383	of these objects depend on neural data.
   384	
   385	\subsection{Vertex construction}\label{ssec:vertices}
   386	
   387	The 600-cell $\Rsixhundred$ has $120$ vertices in
   388	$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
   389	With $\Ph = (1+\sqrt 5)/2$ the canonical vertex set is
   390	\begin{itemize}\itemsep=1pt
   391	\item $8$ vertices: all permutations of $(\pm 1, 0, 0, 0)$;
   392	\item $16$ vertices: all sign combinations of
   393	  $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
   394	\item $96$ vertices: all even permutations of
   395	  $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$.
   396	\end{itemize}
   397	All $120$ vertices lie on the unit $3$-sphere $S^{3}$. The H$_4$
   398	Coxeter group acts transitively on the vertex set; in particular,
   399	every vertex has identical local structure. Implementation:
   400	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
   401	
   402	\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
   403	
   404	The substrate graph $G_{V_{600}} = (V, E)$ is built by connecting each
   405	vertex to its nearest neighbours under the Euclidean metric on $S^{3}$.
   406	H$_4$ acts transitively on the vertex set, forcing uniformity of the
   407	local structure. We compute the resulting Laplacian spectrum from the
   408	constructed graph; multiplicities match the expected H$_4$ block
   409	sizes. The 600-cell construction itself is
   410	standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
   411	\paragraph{Graph facts (forced by the construction).}
   412	The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, and
   413	every vertex has degree exactly $12$ (H$_4$ transitivity acts on the
   414	vertex set; the short-edge nearest-neighbour graph inherits this
   415	uniformity). These facts are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}
   416	and reproduced numerically by
   417	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
   418	
   419	\paragraph{Laplacian spectrum (computed numerically).}
   420	The unweighted graph Laplacian $\Lop = D - A$ has nine distinct
   421	eigenvalues with multiplicities summing to $120$:
   422	\[
   423	\sigma(\Lop) \;=\;
   424	\bigl\{0^{1},\;
   425	       (12\!-\!6\Ph)^{4},\;
   426	       (12\!-\!4\Ph)^{9},\;
   427	       9^{16},\;
   428	       12^{25},\;
   429	       14^{36},\;
   430	       (4\Ph + 8)^{9},\;
   431	       15^{16},\;
   432	       (6\Ph + 6)^{4}\bigr\},
   433	\]
   434	i.e.\ approximately $\{0, 2.292, 5.528, 9, 12, 14, 14.472, 15, 15.708\}$
   435	with multiplicities $\{1, 4, 9, 16, 25, 36, 9, 16, 4\}$. We computed
   436	this directly from the constructed Laplacian
   437	(\texttt{kernel/vfd\_closure\_kernel.py:compute\_graph\_laplacian});
   438	the spectrum is reproducible at machine precision and the
   439	multiplicities match the expected H$_4$ block sizes. We do not derive
   440	the closed-form entries here; the values in $\mathbb{Z}[\Ph]$ are
   441	reported as observed.
   442	
   443	\paragraph{H$_4$ irrep block decomposition.}
   444	The eigenspaces partition into H$_4$-proper and $\sigma$-twin Coxeter
   445	exponent classes. For H$_4$ proper the exponents are $\{1, 11, 19, 29\}$;
   446	for the Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism
   447	of $\mathbb{Z}[\Ph]$ the exponents become $\{7, 13, 17, 23\}$. The
   448	$\sigma$-orbit projector basis
   449	(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}) realises the block
   450	decomposition with cross-block norm $<10^{-15}$, providing a
   451	machine-precise structural index used by the recurrent layer in
   452	\S\ref{sec:chain} (the $K_{7}$-class projector is the default
   453	phenomenal-binding profile).
   454	
   455	\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
   456	
   457	The substrate's linear response to an external source $f \in \mathbb{R}^{120}$
   458	is the discrete Green's function of the shifted Laplacian:
   459	\begin{equation}\label{eq:cphi}
   460	\Cph \;=\; \Lop + \Ph^{-2} I,
   461	\qquad
   462	\psi \;=\; \Cph^{-1} f.
   463	\end{equation}
   464	The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
   465	clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
   466	$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
   467	inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
   468	\emph{not} a derived theorem; it is a stability choice. The companion
   469	kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
   470	$\Cph$ as the basis for an independent passive-regime witness in
   471	flavour physics~\citep{SmartBAnomaly2026}, where the same operator
   472	form (without retuning the shift) describes the
   473	$B\to K^{*}\mu^{+}\mu^{-}$ angular anomaly across five public datasets.
   474	This paper imports $\Cph$ from that line; we do not re-derive it.
   475	
   476	The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
   477	not produce critical-state cascade statistics; the recurrent layer
   478	in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
   479	$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
   480	event distributions. The choice $k\!=\!12$ is the average degree of
   481	$G_{V_{600}}$ (\S\ref{ssec:graph}), pinned by the substrate, not
   482	fitted to any dataset.
   483	
   484	\paragraph{Disclosure (substrate-witness scope).}
   485	The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
   486	The bounded-top-$K$ nonlinearity uses $k\!=\!12$ pinned to the graph's
   487	average degree, not a fitted threshold. No other shape parameter
   488	enters. The condition-dependent self-injection coupling
   489	$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
   490	varies between conditions in~\S\ref{sec:chain}; it is reported
   491	explicitly per condition.
   492	
   493	\subsection{Shell decomposition}\label{ssec:shells}
   494	
   495	Under the H$_3$ subgroup, the $120$ vertices partition into $9$
   496	spherical shells indexed by Euclidean inner product with a chosen pole:
   497	\[
   498	\bigl(|S_0|,\ldots,|S_8|\bigr) \;=\; (1, 12, 20, 12, 30, 12, 20, 12, 1).
   499	\]
   500	The middle shell $S_{4}$ has $30$ vertices on the equatorial plane
   501	(the icosidodecahedral ring). When projecting onto a continuum kernel
   502	in companion preprints~\citep{SmartAriaClosureKernel2026}, the
   503	shell-mean projection of the equatorial-source response,
   504	$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
   505	collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
   506	This paper does not use that continuum projection; we work with the
   507	discrete operator throughout.
   508	
   509	\subsection{Cascade descent (sketch)}\label{ssec:cascade}
   510	
   511	The recurrent layer in~\S\ref{sec:chain} references a cascade
   512	decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
   513	\to S^{7}\to 0$, implemented in
   514	\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
   515	An arbitrary operator on the $E_{8}$ root system descends to the
   516	4-D H$_4$ subspace through a sequence of orthogonal projections, each
   517	preserving the Frobenius norm to within $10^{-15}$. The
   518	$\sigma$-orbit projector basis from
   519	\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
   520	decomposition at machine precision.
   521	
   522	The descent provides numerical stability for the cascade ablations:
   523	when one ablates a specific K-class contribution (e.g.\ $K_{7}$), the
   524	remaining operator structure is exactly preserved. We do not claim
   525	the cascade itself is forced by physics on a pre-substrate level; the
   526	cascade is a decomposition of operators on $\Rsixhundred$, and the
   527	choice of $\Rsixhundred$ as the active substrate is post-hoc justified
   528	by the empirical correspondences in~\S\ref{sec:results}.
   529	
   530	\subsection{What the substrate is fixed-by, and what it is not}
   531	
   532	\begin{itemize}\itemsep=2pt
   533	\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
   534	  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
   535	  irrep block structure, average degree $k\!=\!12$, $\sigma$-twin pairing.
   536	\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
   537	  is not a derivation; it is a design-level clamp that bounds the
   538	  response inverse.
   539	\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
   540	  $24$-cell or $120$-cell. The choice is post-hoc motivated by the H$_4$
   541	  cascade structure and the empirical correspondences. A formal
   542	  ablation against alternative regular 4-polytopes is an open build
   543	  (\S\ref{sec:limitations}).
   544	\end{itemize}

 succeeded in 315ms:
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
   274	% =====================================================================
   275	\section{Discussion}\label{sec:discussion}
   276	% =====================================================================
   277	
   278	This section reads the substrate-witness result against existing
   279	theories of consciousness, identifies what is novel here that is not
   280	a re-statement of an earlier theory, and proposes a non-load-bearing
   281	ACT bridge to the companion adaptive-closure-transport
   282	preprint~\citep{SmartAdaptiveClosureTransport2026}. We do not claim a
   283	selection theorem, we do not claim a Lyapunov derivation, and we do
   284	not claim the recurrent layer ``is'' consciousness.
   285	
   286	\subsection{What is novel in this work}
   287	
   288	Three things are claimed novel as a substrate witness:
   289	\begin{enumerate}\itemsep=2pt
   290	\item \textbf{A geometry-fixed substrate that is consistent with
   291	  real-cortex EEG signatures without fitted shape parameters on neural
   292	  data.} Once the 600-cell is chosen as the substrate, its graph
   293	  ($120$ vertices, uniform degree $12$ on the canonical short-edge
   294	  nearest-neighbour graph) and the response operator
   295	  $\Cph = \Lop + \Ph^{-2} I$ are fixed by the construction (no
   296	  shape parameter is tuned to neural data); cascade-$\alpha$ matches
   297	  Sleep-EDFx within preregistered tolerance with pairwise CI overlap
   298	  on three reference ranges; six drug/sleep signatures pass at
   299	  literature-derived thresholds on a single deterministic substrate.
   300	  We are not aware of a prior geometric substrate that has been tested
   301	  against this many preregistered cortical correspondences from a
   302	  graph fixed by the construction with no neural-data-fitted shape
   303	  parameters; we cannot rule out that such a model exists.
   304	\item \textbf{The strong-coupling architectural finding.} $C$ and $P$
   305	  are strongly coupled cascade-state stabilisers, not
   306	  nearly-orthogonal ones. The $C\!\times\!P$ interaction
   307	  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
   308	  in magnitude to the $P$ main effect ($-0.218$). This was hidden by
   309	  underpowered ablation and emerged only at $N\!\geq\!20$ — a
   310	  substantive correction to the architectural reading from the
   311	  original 3-seed validation.
   312	\item \textbf{The 18/18 preregistered correspondences with no
   313	  threshold modification.} Every prediction in the preregistered set
   314	  passes at the preregistered thresholds. The two interaction tests
   315	  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
   316	  one test (P13) required the documented state-reset protocol. We
   317	  report this transparently as methodology refinement, not as
   318	  threshold change.
   319	\end{enumerate}
   320	
   321	\subsection{Comparison to existing theories of consciousness}
   322	
   323	\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
   324	IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
   325	wake). The $\Phi$ proxy (\S\ref{sec:chain}) is designed to be small
   326	under H$_4$-equivariant dynamics and to increase when dynamics
   327	produce cross-class asymmetries. ARIA does not implement the full
   328	IIT axioms (cause-effect repertoires, exclusion postulate,
   329	integration-over-partitions); it reproduces an observable consequence
   330	on the propofol--wake state contrast. This is a consistency-of-direction
   331	result, not a discharge of IIT.
   332	
   333	\textbf{vs Global Workspace Theory.}~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
   334	The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
   335	functionally analogous to a workspace with rotating attentional
   336	selection; the active observer frame plays the role of a temporary
   337	in-workspace subset of features. ARIA does not commit to the GWT
   338	broadcast/access distinction at the architectural level; the
   339	analogy is descriptive.
   340	
   341	\textbf{vs Predictive Processing.}~\citep{FristonFreeEnergy2010,ClarkPP2013}
   342	ARIA does not implement prediction-error minimisation or hierarchical
   343	generative models.
   344	The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
   345	modulation of the substrate response by cosine direction alignment
   346	with the prior phenomenal snapshot, not by learned prediction errors.
   347	Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
   348	learning rate over a prediction-error norm) are an open build, not
   349	delivered here.
   350	
   351	\textbf{vs neural mass models.} ARIA operates at the
   352	architectural-algorithmic level; it does not specify which neural
   353	circuits implement context rotation or partial emission. The 600-cell
   354	substrate is proposed as an abstract description of the criticality-
   355	maintaining structure of cortex, not as a circuit model.
   356	
   357	\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
   358	
   359	The companion adaptive-closure-transport
   360	preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
   361	4-tuple bridge
   362	$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
   363	$L_{M}$, learnable Hebbian-like field $W$, and a homeostatic
   364	regulariser $R_{\mathrm{hom}}$. We propose the dictionary
   365	$D_{\mathrm{ACT}}$:
   366	\[
   367	D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
   368	\;\longmapsto\;
   369	(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
   370	   \ \texttt{homeostatic\_reset}).
   371	\]
   372	\textbf{This bridge is non-load-bearing for the present paper.} It is
   373	included as a route-K (alternative-route) reading; the substrate-
   374	witness claims (six signatures, $18/18$, chess $+40.6$pp,
   375	HCP $\sigma$-distances) do not require any of the ACT theorems.
   376	
   377	\textbf{What ACT would have to deliver to make this load-bearing.}
   378	The companion preprint identifies four open builds, each of which is
   379	deferred:
   380	\begin{itemize}\itemsep=2pt
   381	\item A Lyapunov function $V(W)$ on the reduced flow whose
   382	  monotonicity proves selection — not delivered.
   383	\item An edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   384	  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
   385	  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
   386	\item A formal $2I$-equivariance audit of the closure operator
   387	  family — not delivered.
   388	\item A full reduced-flow convergence theorem on
   389	  $W$-trajectories — not delivered.
   390	\end{itemize}
   391	Until these are delivered, ARIA is positioned as the empirical
   392	\emph{substrate witness} for the family that ACT names; ACT is not the
   393	selection-theorem witness for ARIA. The companion kernel
   394	document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
   395	in a passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$ flavour
   396	anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
   397	infrastructure with this paper, but does not transfer empirical
   398	support for ARIA.
   399	
   400	\subsection{The strong-coupling reading for cortical architecture}
   401	
   402	Real cortical criticality is maintained by multiple parallel
   403	mechanisms: E/I balance, neuromodulation (acetylcholine, noradrenaline),
   404	homeostatic plasticity, gain control. The naive expectation — and the
   405	one we held until the $N\!=\!20$ deep-dive — is that these are mostly
   406	orthogonal, so losing one removes only its own main effect. The
   407	$N\!=\!20$ result reverses this on the substrate: $C$ and $P$ are
   408	strongly coupled. Disabling one cascades into losing the synergistic
   409	contribution of the other.
   410	
   411	This matches clinical observations: anaesthesia (which targets
   412	GABAergic transmission) and seizure (which targets E/I balance)
   413	produce widespread network-level dysfunction beyond their direct
   414	targets — qualitatively consistent with a strong-coupling hypothesis. We position this as
   415	\emph{a hypothesis the substrate witness raises}, not as a proof.
   416	The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
   417	real-cortex pharmacological coupling is a step we do not take in
   418	this paper.
   419	
   420	\subsection{Methodological contributions}
   421	
   422	Two methodological items are worth recording outside the headline:
   423	\begin{enumerate}\itemsep=2pt
   424	\item \textbf{$N\!\geq\!20$ for similar high-variance ablation matrices.}
   425	  Allocation discipline for preregistration: in this cascade-ablation
   426	  matrix specifically, P4 ($C\!\times\!P$) required $N\!=\!20$ for
   427	  reliable detection at the preregistered threshold. The general
   428	  rule we draw — when preregistering an interaction effect on a
   429	  system with unknown per-seed variance, budget for at least this
   430	  scale — should be tested against other ablation matrices, not
   431	  taken as universal. The original 3-seed plan was the source of two
   432	  underpowered-interaction estimates in this work.
   433	\item \textbf{State-reset protocol on non-stationary substrates.}
   434	  ARIA's substrate is a non-stationary dynamical system; the
   435	  pressure field equilibrates within $\sim 5$ successive evaluations.
   436	  Any multi-trial benchmark must specify a state-reset protocol or
   437	  document the drift. Generalisable lesson: \emph{published
   438	  cross-domain benchmarks on non-stationary substrates should report
   439	  an explicit reset/equilibration discipline}, not just seed.
   440	\end{enumerate}
   441	
   442	\subsection{The substrate as an H$_4$-transitive connectivity null}
   443	
   444	The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
   445	deterministic null reference for cortical functional connectivity.
   446	Real cortex breaks the symmetry through hub-spoke functional
   447	specialisation; the $\sigma$-distances from ARIA quantify the
   448	magnitude of biological symmetry-breaking with no fitted parameters.
   449	
   450	This is a methodological contribution to comparative connectomics.
   451	Stochastic nulls (Erd\H{o}s--R\'enyi, configuration model,
   452	edge-randomised graphs) compare cortex to a random graph with matched
   453	density. ARIA is a different kind of null: a deterministic
   454	group-theoretic graph with structure-level statements: degree std
   455	$=\!0$ by H$_4$ transitivity, and a fully-determined Laplacian
   456	spectrum (\S\ref{ssec:graph}) computed from the constructed graph.
   457	Both null kinds are useful; ARIA gives a specific, reproducible,
   458	group-theoretic baseline that cortex deviates from in quantifiable
   459	$\sigma$-units.
   460	
   461	\subsection{Open questions raised by the substrate witness}
   462	
   463	\begin{itemize}\itemsep=2pt
   464	\item Do the six drug/sleep signatures replicate across $10$--$20$
   465	  cross-seed runs of the recurrent layer? (Single-seed disclosure;
   466	  see \S\ref{sec:limitations}.)
   467	\item Do alternative regular 4-polytopes ($24$-cell, $120$-cell)
   468	  reproduce comparable signature sets, or is the $600$-cell
   469	  distinguished?
   470	\item Does the strong-coupling reading ($C\!\times\!P$) survive an
   471	  independent fresh-seed $N\!=\!20$ replication at a different seed
   472	  range?
   473	\item Does the substrate's amplifier behaviour transfer to other
   474	  ambiguous-feature classification tasks beyond chess (e.g.\ visual
   475	  pattern, audio classification)?
   476	\item Does the Sleep-EDFx three-way CI overlap survive on a different
   477	  EEG cohort (TUH, NHM)?
   478	\end{itemize}
   479	We list these as open questions raised by the witness, not as gaps
   480	in the witness itself.

 succeeded in 343ms:
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
   198	% =====================================================================
   199	\section{Results}\label{sec:results}
   200	% =====================================================================
   201	
   202	This section is the empirical core. \S\ref{ssec:six_signatures}
   203	gives the six drug/sleep EEG signatures on the recurrent layer
   204	(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
   205	preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
   206	gives the three-way $\alpha$ overlap. We lift the result map
   207	$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
   208	verdict)}$ verbatim from the validation outputs without
   209	recomputation; sources are
   210	\texttt{docs/brain\_mapping/CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
   211	and \texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
   212	
   213	\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
   214	
   215	\textbf{Setup.} Four conditions $\times$ $800$ ticks at seed $42$,
   216	$k_{\mathrm{thr}}=12$, single deterministic substrate
   217	(\S\ref{sec:chain}). Per-condition trajectory observables are
   218	$(n_{\mathrm{evt}}, \alpha, \mathrm{CI}_{95}, R^{2}, I_{\mathrm{var}},
   219	\Phi_{\mathrm{traj}}, \mathrm{cont})$.
   220	
   221	\begin{table}[ht]
   222	\centering
   223	\small
   224	\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
   225	seed 42).}
   226	\label{tab:per_condition}
   227	\begin{tabular}{l r r l r r r r}
   228	\toprule
   229	condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
   230	\midrule
   231	WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
   232	SLEEP\_N3 & $111$ & $3.250$ & $[2.44, 4.14]$ & $0.886$ & $1.01\!\times\!10^{-5}$ & $0.0055$ & $0.980$ \\
   233	PROPOFOL  & $246$ & $2.758$ & $[2.52, 3.09]$ & $0.931$ & $5.37\!\times\!10^{-6}$ & $0.0003$ & $0.877$ \\
   234	RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
   235	\bottomrule
   236	\end{tabular}
   237	\end{table}
   238	
   239	\begin{table}[ht]
   240	\centering
   241	\small
   242	\caption{Six drug/sleep signatures with literature references.}
   243	\label{tab:six_signatures}
   244	\begin{tabular}{c l l c c l}
   245	\toprule
   246	\# & Signature & Reference & Predicted & Observed & Verdict \\
   247	\midrule
   248	1 & NREM-N3 var ratio (vs Wake) &
   249	   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
   250	   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
   251	2 & Propofol switching ratio &
   252	   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
   253	   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
   254	3 & Propofol continuity drop &
   255	   EEG microstate~\citep{Brodbeck2012Microstates} &
   256	   $> 0.020$ & $+0.066$ & $\checkmark$ \\
   257	4 & Propofol $\Phi$ collapse (IIT) &
   258	   Tononi 2008~\citep{Tononi2008} &
   259	   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
   260	5 & Recovery reversibility &
   261	   clinical anaesthesia &
   262	   identical to wake & $0$ diff & $\checkmark$ \\
   263	6 & Wake cortical-avalanche $\alpha$ &
   264	   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
   265	   $\alpha\!\in\![1.5, 3.5]$, $R^{2}\!>\!0.85$ &
   266	   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
   267	   $\checkmark$ \\
   268	\bottomrule
   269	\end{tabular}
   270	\end{table}
   271	
   272	All six signatures pass against their literature-derived thresholds
   273	on the same deterministic substrate trajectory. The six signatures
   274	are not part of the dated 2026-04-18 P1--P18 preregistration; their
   275	thresholds are drawn from the literature (Sleep-EDFx CI for
   276	wake $\alpha$, OpenNeuro \texttt{ds005620} point-estimate window for
   277	propofol switching, literature-direction predictions for $\Phi$
   278	collapse, continuity drop, and recovery). They were tested on a
   279	recurrent-layer architecture redesigned at v4 with
   280	biologically-motivated condition-specific stimulus models
   281	(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
   282	documents the v3$\to$v4 stimulus redesign). The mechanistic readings
   283	in \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} are not
   284	load-bearing for the headline claim. Single-seed disclosure:
   285	\S\ref{ssec:regime}.
   286	
   287	\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
   288	
   289	\textbf{Tally.} $17/18$ at standard validation
   290	(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
   291	plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
   292	on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
   293	$32000$--$32019$). \emph{No preregistered threshold has been modified.}
   294	
   295	\begin{table}[ht]
   296	\centering
   297	\small
   298	\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
   299	\label{tab:eighteen_prereg}
   300	\begin{tabular}{l l l l l}
   301	\toprule
   302	ID & Test & Threshold & Observed (2026-04-29) & Verdict \\
   303	\midrule
   304	P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
   305	P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
   306	P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
   307	\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
   308	   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
   309	P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
   310	P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
   311	P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
   312	P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
   313	P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
   314	P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
   315	P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
   316	P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
   317	\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
   318	P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
   319	P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   320	P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
   321	P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
   322	P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
   323	\bottomrule
   324	\end{tabular}
   325	\end{table}
   326	
   327	\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
   328	estimator as $5$-fold CV at threshold $\geq +15$pp; the 2026-04-29
   329	validation tightened the estimator to LOO with state reset, a
   330	disclosed estimator/protocol refinement at the unchanged $+15$pp threshold. See
   331	\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
   332	
   333	\textbf{Three predictions that flipped to PASS, with documented
   334	methodology refinement (no threshold change).}
   335	\begin{itemize}\itemsep=2pt
   336	\item P3 (D$\times$C interaction independence) was outside the band
   337	  at $N\!=\!3$ ($-0.231$) and inside the band at $N\!=\!5$ ($-0.183$).
   338	  Reading: consistent with an underpowered interaction estimate at
   339	  $N\!=\!3$ on a high-per-seed-variance interaction term.
   340	\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
   341	  ($+0.044$) and at $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
   342	  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
   343	  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
   344	\item P13 (chess substrate lift): the 2026-04-18 preregistration
   345	  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
   346	  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
   347	  validation strengthened the estimator to LOO with state reset, a
   348	  disclosed estimator/protocol refinement at the same threshold; the LOO lift was $+3.1$pp
   349	  without state reset on a state-drifted substrate, and $+40.6$pp
   350	  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
   351	  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
   352	  report this as a \emph{validation-protocol refinement relative to
   353	  the preregistered test}, not as preregistration revision.
   354	\end{itemize}
   355	
   356	\textbf{Headline verdict.} Eighteen preregistered correspondences
   357	all pass at preregistered thresholds, with two interaction tests
   358	requiring $N\!\geq\!5$ and one requiring $N\!=\!20$ for reliable
   359	detection of high-variance interaction terms, and one test
   360	requiring the documented state-reset protocol. The original $15/18$
   361	result was a methodology-limited tally, not a content failure.
   362	
   363	\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
   364	
   365	The substrate's wake cascade-$\alpha$ confidence interval overlaps
   366	\emph{three independent reference ranges} simultaneously:
   367	
   368	\begin{table}[ht]
   369	\centering
   370	\small
   371	\caption{Three-way $\alpha$ overlap on the wake cascade-event power
   372	law.}
   373	\label{tab:alpha_overlap}
   374	\begin{tabular}{l c l c}
   375	\toprule
   376	Source & $\alpha$ & 95\% CI & $n$ \\
   377	\midrule
   378	ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
   379	Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
   380	ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
   381	\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
   382	\bottomrule
   383	\end{tabular}
   384	\end{table}
   385	
   386	The v4 WAKE 95\% CI $[1.82, 2.86]$ contains the upper arm of the
   387	real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
   388	cascade pipeline CI $[2.73, 3.25]$ on the interval $[2.73, 2.86]$,
   389	and lies inside the cortical-avalanche band
   390	$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
   391	intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
   392	WAKE $\cap$ cortical-avalanche band) are non-empty across three
   393	independent reference ranges.
   394	
   395	\textbf{Reading.} The substrate produces self-organised-critical
   396	cascade statistics matching the cortical-avalanche literature with
   397	no fitted parameter on neural data. The bounded-top-$K$ at
   398	$k=12$ is pinned to the substrate's average degree
   399	(\S\ref{ssec:graph}); the $\Ph^{-2}$ shift in $\Cph$ is a
   400	stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
   401	biological time-scale parameters but is not measurement-fitted to
   402	any specific subject (\S\ref{sec:chain}). Three-way overlap on the
   403	power-law exponent is one of the main empirical anchors in the paper
   404	(noting that the v4 WAKE CI is from a single deterministic trajectory
   405	with event-bootstrap; cross-seed CI is an open build).
   406	% =====================================================================
   407	\section{Stress test: the C\texorpdfstring{$\times$}{x}P synergy at adequate
   408	         replication}\label{sec:stress}
   409	% =====================================================================
   410	
   411	This section is the C$\times$P interaction stress test. The original
   412	preregistered prediction was P4: $C\times P$ interaction
   413	$\Delta_{CP} \geq +0.10$ on cascade-$\alpha$. The 2026-04-20
   414	$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
   415	architectural claim ``C and P synergise on cascade-state stability''
   416	was walked back. Closing this gap without modifying the preregistered
   417	threshold required (a) re-evaluating the $N\!=\!3$ point estimate as
   418	consistent with an underpowered interaction estimate, (b) tracking
   419	the estimate's behaviour across $N$, and (c) bootstrapping a
   420	confidence interval on a fresh-seed $N\!=\!20$ sample. We did all
   421	three.
   422	
   423	\subsection{The factorial estimator}
   424	
   425	For the four ablation conditions $\{----, -C--, --P-, -CP-\}$
   426	(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
   427	standard $2\times 2$ factorial difference:
   428	\[
   429	\Delta_{CP}
   430	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
   431	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
   432	\]
   433	Per-seed paired estimates use the same formula on a single seed's
   434	four conditions.
   435	
   436	\subsection{The trend across \texorpdfstring{$N$}{N}}
   437	
   438	\begin{table}[ht]
   439	\centering
   440	\small
   441	\caption{$C\times P$ interaction estimate as a function of $N$.}
   442	\label{tab:cxp_trend}
   443	\begin{tabular}{r l r l l}
   444	\toprule
   445	$N$ & Seeds & Estimate $\Delta_{CP}$ & 95\% CI & Verdict vs $\geq +0.10$ \\
   446	\midrule
   447	$3$  & $30040$--$30042$ & $+0.044$ & --- & $\times$ original prereg \\
   448	$5$  & $30040$--$30044$ & $+0.039$ & --- & $\times$ this session re-run \\
   449	$10$ & $31000$--$31009$ & $+0.088$ & $[-0.002, +0.174]$ & borderline \\
   450	$\mathbf{20}$ & $\mathbf{32000\text{--}32019}$ & $\mathbf{+0.190}$
   451	       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
   452	\bottomrule
   453	\end{tabular}
   454	\end{table}
   455	
   456	The estimate remains small at $N\!=\!3$ and $N\!=\!5$
   457	($+0.044, +0.039$) and rises at $N\!=\!10$ and $N\!=\!20$
   458	($+0.088, +0.190$). Per-seed std at $N\!=\!10$ was $0.159$; at
   459	$N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$ sample landed on
   460	outliers; the $N\!=\!20$ sample reveals a clean narrow positive
   461	distribution.
   462	
   463	\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
   464	
   465	\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
   466	$32000$--$32019$, non-overlapping with original validation seeds in
   467	the $30000$s), $150$ epochs per run. All other ablation flags off
   468	($D, E$ held on). Bootstrap $n_{\mathrm{resamples}}\!=\!2000$,
   469	seed $42$. Wallclock $1706$\,s on a single CPU
   470	(\texttt{demo\_p4\_cxp\_deep\_dive.py}).
   471	
   472	\textbf{Per-condition means at \texorpdfstring{$N\!=\!20$}{N=20}.}
   473	
   474	\begin{table}[ht]
   475	\centering
   476	\small
   477	\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
   478	\label{tab:cxp_means}
   479	\begin{tabular}{l r r r}
   480	\toprule
   481	condition & mean $\alpha$ & std & sem \\
   482	\midrule
   483	$----$ baseline    & $3.008$ & $0.090$ & $0.020$ \\
   484	$-C--$ (C off)     & $3.464$ & $0.097$ & $0.022$ \\
   485	$--P-$ (P off)     & $2.790$ & $0.086$ & $0.019$ \\
   486	$-CP-$ (both off)  & $3.628$ & $0.161$ & $0.036$ \\
   487	\bottomrule
   488	\end{tabular}
   489	\end{table}
   490	
   491	\textbf{Main effects at \texorpdfstring{$N\!=\!20$}{N=20}.}
   492	$C$ main effect $= +0.456$ (turning $C$ off raises $\alpha$);
   493	$P$ main effect $= -0.218$ (turning $P$ off lowers $\alpha$).
   494	
   495	\textbf{Interaction estimate.} Direct calculation from means:
   496	\[
   497	\Delta_{CP} \;=\; \frac{(3.628 + 3.008) - (3.464 + 2.790)}{2}
   498	            \;=\; +0.191.
   499	\]
   500	Bootstrap on the 20-seed sample (2000 resamples):
   501	\begin{itemize}\itemsep=1pt
   502	\item bootstrap mean $\Delta_{CP} = +0.190$;
   503	\item 95\% bootstrap CI $[+0.143, +0.239]$;
   504	\item $0/2000$ bootstrap resamples were at or below zero, reported as
   505	      $0.0000$;
   506	\item $0/2000$ bootstrap resamples were below the preregistered
   507	      $+0.10$ floor, reported as $0.0000$.
   508	\end{itemize}
   509	
   510	\textbf{Per-seed paired distribution.}
   511	$19/20$ seeds give a positive paired-interaction estimate (range
   512	$+0.055$ to $+0.322$); a single seed gives $-0.009$. No seed gives a
   513	strongly negative interaction.
   514	
   515	\subsection{Reading and disclosure}
   516	
   517	\textbf{The 95\% CI is entirely above the preregistered $+0.10$
   518	threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
   519	at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
   520	were below the preregistered $+0.10$ floor, reported as $0.0000$.
   521	
   522	\textbf{Architectural reading (substrate witness).} $C$ creates churn
   523	in \emph{which} vertices are uncrossed (frame rotation churns the
   524	uncrossed pool). $P$ promotes the high-pressure subset of the
   525	uncrossed pool to mini-emitters. The product is a non-additive
   526	novel-event-generation pathway: with both on, the uncrossed pool
   527	churns and $P$ amplifies new vertices entering the high-pressure
   528	region; with either off, the measured interaction collapses. The interaction
   529	$+0.19$ is comparable in magnitude to the $P$ main effect $-0.22$,
   530	so $C$ and $P$ are \emph{strongly coupled} cascade-state stabilisers
   531	on this substrate, not nearly-orthogonal ones. This reverses an
   532	architectural claim from the original 3-seed validation that held $C$
   533	and $P$ approximately orthogonal.
   534	
   535	\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
   536	was conducted \emph{after} the original $N\!=\!3$ failure
   537	(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
   538	selected to be non-overlapping with the original $30000$s seeds.
   539	Two strengthening builds we have not delivered:
   540	(i) a second independent $N\!=\!20$ run at a different seed range
   541	(e.g.\ $33000$--$33019$), and
   542	(ii) an $N\!=\!50$ characterisation of the per-seed sample
   543	distribution. Both are recorded as open builds in
   544	\S\ref{sec:limitations}.
   545	
   546	\textbf{What this stress test does \emph{not} establish.}
   547	\begin{itemize}\itemsep=2pt
   548	\item It does not establish a Lyapunov function on the reduced flow.
   549	\item It does not establish that the substrate is uniquely selected by
   550	  $C\times P$ coupling among regular 4-polytopes.
   551	\item It does not establish an $\eta$-trajectory derivation; $\eta$
   552	  is treated as a condition-dependent constant in this paper.
   553	\end{itemize}
   554	The stress test is what its name says: a high-replication factorial
   555	test of one preregistered interaction prediction, on a fresh-seed
   556	sample, with bootstrap confidence intervals. The architectural reading
   557	is a \emph{description} of what $C$ and $P$ do on the substrate, not a
   558	theorem about why they do it.
   559	
   560	\subsection{Methodological contribution}
   561	
   562	We document, as a methodological contribution to preregistration
   563	practice on this cascade-ablation matrix specifically: in this matrix,
   564	P4 ($C\times P$) required $N\!=\!20$ fresh seeds for reliable detection
   565	at the preregistered threshold; P3 ($D\times C$) closed at $N\!=\!5$.
   566	The original 3-seed preregistered validation gave estimates consistent
   567	with underpowered detection on both interaction tests; both close at
   568	higher $N$ without threshold modification. The general lesson: when
   569	preregistering an interaction effect on a system with unknown
   570	per-seed variance, budget the seed count from a power-analysis
   571	assumption that the per-seed std could be as large as the interaction
   572	effect itself. Future preregistrations on similar high-variance
   573	ablation matrices should plan for this scale.

 succeeded in 390ms:
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
   147	$\Delta_{CP}$; full-IIT computation on the
   148	substrate's $S^{3}$ state space. The latter is computationally
   149	heavy and is deferred.
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
   166	\item Active-regime extension of the chess pattern-recognition test to
   167	  move-by-move game trajectories (this paper covers static positions only).
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
   196	% =====================================================================
   197	\section{Conclusion}\label{sec:conclusion}
   198	% =====================================================================
   199	
   200	The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
   201	symmetry, with the shifted-Laplacian response operator
   202	$\Cph = \Lop + \Ph^{-2} I$ ($\Ph=(1+\sqrt 5)/2$), is a
   203	geometry-fixed substrate that is consistent with eighteen
   204	preregistered neuroscience correspondences plus six companion
   205	drug/sleep EEG signatures of conscious vs unconscious states. Once
   206	the substrate is chosen, its graph structure ($120$ vertices, uniform
   207	degree $12$ on the canonical short-edge nearest-neighbour graph, with
   208	the Laplacian spectrum reported in~\S\ref{ssec:graph} as observed) is
   209	fixed; only one condition-dependent self-injection coupling
   210	$\eta\in\{0, 0.05, 0.20\}$ and one substrate-pinned nonlinearity
   211	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
   212	degree enter the recurrent layer above the substrate. No shape
   213	parameter is tuned to any neural dataset.
   214	
   215	\textbf{Headline tally.} On a single deterministic trajectory, six
   216	drug/sleep EEG signatures pass against their literature-derived
   217	thresholds (Sleep-EDFx CI, OpenNeuro \texttt{ds005620}, Brodbeck 2012,
   218	Tononi 2008): NREM-N3 phenomenal-intensity variance ratio
   219	$0.463\!\times$ wake; propofol modality-switching $1.83\!\times$ wake;
   220	propofol continuity drop $+0.066$; propofol integrated-information
   221	$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
   222	recovery deterministically identical to wake under the WAKE stimulus
   223	protocol; wake cortical-avalanche power law $\alpha\!=\!2.252$,
   224	$95\%$ CI $[1.82, 2.86]$, $R^{2}\!=\!0.956$. The wake $95\%$ CI
   225	overlaps the real Sleep-EDFx EEG
   226	$95\%$ CI ($n\!=\!30$ subjects, $\alpha\!=\!2.51$,
   227	CI $[2.50, 2.53]$) and ARIA's prior cascade pipeline CI
   228	$[2.73, 3.25]$.
   229	
   230	\textbf{Eighteen preregistered correspondences.} All eighteen pass at
   231	preregistered thresholds, with two interaction tests requiring
   232	$N\!\geq\!5$ and $N\!=\!20$ respectively for reliable detection of
   233	high-variance interaction terms, and one cross-domain test requiring
   234	the documented \texttt{homeostatic\_reset} state-reset protocol. No
   235	preregistered threshold has been modified. The original 2026-04-20
   236	$15/18$ tally was a methodology-limited reading, not a content
   237	failure; the closure of the three gaps (P3, P4, P13) is documented
   238	transparently in
   239	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
   240	
   241	\textbf{Strong-coupling architectural finding.} Two cascade
   242	mechanisms — context rotation $C$ and partial emission $P$ — are
   243	causally identifiable within the factorial ablation model and exhibit
   244	strong synergy: their interaction $\Delta_{CP}\!=\!+0.190$ at
   245	$N\!=\!20$ ($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples
   246	at or below zero, reported as $0.0000$) is comparable in magnitude to
   247	the $P$ main effect $-0.218$. The original 3-seed estimate ($+0.044$)
   248	is consistent with an underpowered interaction estimate on a
   249	high-per-seed-variance term ($\mathrm{std}=0.089$ at $N\!=\!20$); we
   250	contribute $N\!\approx\!20$ as a planning scale for this cascade
   251	matrix, recommended as a preregistration-practice consideration for
   252	similar high-variance ablation matrices.
   253	
   254	\textbf{Cross-domain selectivity.} The substrate exhibits selective
   255	amplification on the two tasks tested: chess 4-category position
   256	classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
   257	canonical depth $n\!=\!25$ ticks (raw $53.1\%$ $\to$ substrate-routed
   258	$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
   259	$5$-fold CV — the LOO finding above is a disclosed estimator/protocol
   260	refinement at the same threshold), while
   261	conversation utterance classification at raw $87.5\%$ lifts $-4.4$pp
   262	(threshold $|\cdot|\!<\!10$pp) — and as an H$_4$-transitive
   263	deterministic null reference for cortical functional connectivity:
   264	on the full-cohort descriptive HCP $n\!=\!1003$ statistics
   265	(preregistered test on the $n\!=\!100$ subset), ARIA's H$_4$-transitive
   266	structure is at $-11.58\sigma$ on degree homogeneity,
   267	$+79.78\sigma$ on participation ratio (with the node-count caveat of
   268	\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
   269	
   270	\textbf{Substrate-witness scope.} This is a substrate witness, not a
   271	derivation of consciousness, not a selection theorem on the
   272	companion adaptive-closure-transport
   273	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
   274	uniqueness claim for the 600-cell among regular 4-polytopes. The
   275	strengthening builds — cross-seed CIs on the recurrent-layer
   276	signatures, alternative-polytope ablations, an independent $N\!=\!20$
   277	C$\times$P replication at a different seed range, cross-parcellation
   278	HCP replication, a Lyapunov function on the reduced flow,
   279	$2I$-equivariance audit of the closure operator family — are
   280	explicitly listed in~\S\ref{sec:limitations} and remain open.
   281	
   282	We are not aware of a prior deterministic geometric architecture
   283	tested against this many preregistered cortical correspondences from
   284	a graph fixed by the construction with no shape parameters tuned to
   285	neural data; we cannot rule out that such prior work exists. The empirical material
   286	gathered here is the substrate witness; the broader programme to
   287	turn the witness into a selection-theorem-grade claim — including the
   288	independent passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$
   289	flavour anomaly~\citep{SmartBAnomaly2026} on the same response
   290	operator $\Cph$ — is sketched in the companion preprints and remains
   291	the natural next step.

codex
The aria-chess import is mostly aligned, but there are two wording risks around “18/18” versus “17/18 standard + 18/18 after deep-dive,” and around the chess lift estimator. I’m doing a static LaTeX/reference pass next so the surface section catches compilation and macro issues too.
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/references.bib' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"\\\\citep\\{|\\\\cite\\{|\\\\ref\\{|\\\\label\\{|\\\\Ph|\\\\Lop|\\\\Cph|\\\\Rsixhundred|V_\\{600\\}|C_\\{\\\\Ph\\}|C_\\\\varphi|L_\\{V_\\{600\\}\\}\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"derive|derived|unique|uniqueness|selection|Lyapunov|2I|equivariance|theorem|forced|fixed by|post-hoc|AIC|Mode-B|Mode B|Gaussian|17/18|18/18|0\\.997|0\\.976|0\\.923|0\\.888|0\\.884|phi|Ph\\"'^-2|Ph'"\\"'^{-2}|φ|varphi" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "SmartBAnomaly2026|SmartAriaChess2026|SmartAdaptiveClosureTransport2026|CoxeterRegularPolytopes|Weisstein600Cell|KrugerMatias2005|LHCbAngular2020" papers/aria-closure-kernel/paper/references.bib papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 exited 2 in 387ms:
rg: regex parse error:
    (?:\citep\{|\cite\{|\ref\{|\label\{|\Ph|\Lop|\Cph|\Rsixhundred|V_\{600\}|C_\{\Ph\}|C_\varphi|L_\{V_\{600\}\})
       ^^
error: unrecognized escape sequence

 succeeded in 400ms:
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
    15	  note         = {Accessed 2026-04-30}
    16	}
    17	
    18	% Companion VFD preprints (the two empirical witnesses + selection-layer paper).
    19	
    20	@unpublished{SmartBAnomaly2026,
    21	  author = {Smart, Lee},
    22	  title  = {A geometry-derived response kernel for the $B \to K^*\mu^+\mu^-$
    23	            angular anomaly: sign-uniform cross-dataset and cross-channel fit},
    24	  year   = {2026},
    25	  note   = {VFD preprint}
    26	}
    27	
    28	@unpublished{SmartAriaChess2026,
    29	  author = {Smart, Lee},
    30	  title  = {A geometry-fixed substrate witness for cortical signatures:
    31	            eighteen preregistered correspondences and six drug/sleep EEG
    32	            signatures from the 600-cell under H$_4$ Coxeter symmetry},
    33	  year   = {2026},
    34	  note   = {VFD preprint, papers/aria-chess-paper/}
    35	}
    36	
    37	@unpublished{SmartAdaptiveClosureTransport2026,
    38	  author = {Smart, Lee},
    39	  title  = {Adaptive Closure Transport: a 4-tuple bridge
    40	            $(M, L_M, W, R_{\mathrm{hom}})$ from substrate response to
    41	            selection},
    42	  year   = {2026},
    43	  note   = {VFD preprint, papers/adaptive-closure-transport/}
    44	}
    45	
    46	% External flavour-physics literature (b-anomaly context, cited in §6).
    47	
    48	@article{KrugerMatias2005,
    49	  author  = {Kr\"uger, Frank and Matias, Joaquim},
    50	  title   = {Probing new physics via the transverse amplitudes of
    51	             $B^0 \to K^{*0} (\to K^- \pi^+) l^+ l^-$ at low recoil},
    52	  journal = {Phys. Rev. D},
    53	  volume  = {71},
    54	  pages   = {094009},
    55	  year    = {2005},
    56	  doi     = {10.1103/PhysRevD.71.094009}
    57	}
    58	
    59	@article{LHCbAngular2020,
    60	  author  = {{LHCb Collaboration}},
    61	  title   = {Measurement of $\mathit{CP}$-averaged observables in the
    62	             $B^0 \to K^{*0} \mu^+ \mu^-$ decay},
    63	  journal = {Phys. Rev. Lett.},
    64	  volume  = {125},
    65	  pages   = {011802},
    66	  year    = {2020},
    67	  doi     = {10.1103/PhysRevLett.125.011802}
    68	}

 exited 2 in 377ms:
rg: regex parse error:
    (?:derive|derived|unique|uniqueness|selection|Lyapunov|2I|equivariance|theorem|forced|fixed by|post-hoc|AIC|Mode-B|Mode B|Gaussian|17/18|18/18|0\.997|0\.976|0\.923|0\.888|0\.884|phi|Ph\^-2|Ph\^{-2}|φ|varphi)
                                                                                                                                                                                                      ^
error: repetition quantifier expects a valid decimal

 succeeded in 427ms:
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:31:\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:38:\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:65:4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
papers/aria-closure-kernel/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:28:substrates from~\citep{SmartBAnomaly2026}; the aria-chess
papers/aria-closure-kernel/paper/sections/09_limitations.tex:140:preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
papers/aria-closure-kernel/paper/sections/09_limitations.tex:153:  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:33:\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:71:  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:76:\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:128:  inherited verbatim from~\citep{SmartBAnomaly2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:132:  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:44:preregistered tally as reported in~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:154:Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:40:(verbatim from~\citep{SmartBAnomaly2026}, also at
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:47:from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:74:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:79:  amplification ($\sim 2.2$~\citep{KrugerMatias2005}). The
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:122:  preprint's limitations section~\citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:92:layer~\citep{SmartAriaChess2026} realises this block decomposition
papers/aria-closure-kernel/paper/sections/03_substrate.tex:11:not prove, here~\citep{CoxeterRegularPolytopes}. All facts in
papers/aria-closure-kernel/paper/sections/03_substrate.tex:19:$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:20:Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical vertex
papers/aria-closure-kernel/paper/sections/03_substrate.tex:59:into $S^{3}$~\citep{CoxeterRegularPolytopes}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:74:  in~\citep{CoxeterRegularPolytopes}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:87:  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:93:  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:125:  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:142:preprint~\citep{SmartAriaChess2026}: numerical results
papers/aria-closure-kernel/paper/sections/05_agreement.tex:111:b-anomaly paper~\citep{SmartBAnomaly2026} established
papers/aria-closure-kernel/paper/references.bib:1:@book{CoxeterRegularPolytopes,
papers/aria-closure-kernel/paper/references.bib:10:@misc{Weisstein600Cell,
papers/aria-closure-kernel/paper/references.bib:20:@unpublished{SmartBAnomaly2026,
papers/aria-closure-kernel/paper/references.bib:28:@unpublished{SmartAriaChess2026,
papers/aria-closure-kernel/paper/references.bib:37:@unpublished{SmartAdaptiveClosureTransport2026,
papers/aria-closure-kernel/paper/references.bib:48:@article{KrugerMatias2005,
papers/aria-closure-kernel/paper/references.bib:59:@article{LHCbAngular2020,
papers/aria-closure-kernel/paper/sections/02_definition.tex:133:preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
papers/aria-closure-kernel/paper/main.tex:60:public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
papers/aria-closure-kernel/paper/main.tex:63:signatures~\citep{SmartAriaChess2026}.
papers/aria-closure-kernel/paper/main.tex:73:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
papers/aria-closure-kernel/paper/main.tex:88:direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
papers/aria-closure-kernel/paper/main.tex:90:six drug/sleep EEG signatures~\citep{SmartAriaChess2026}. We
papers/aria-closure-kernel/paper/main.tex:137:(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
papers/aria-closure-kernel/paper/main.tex:144:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:193:(b-anomaly~\citep{SmartBAnomaly2026},
papers/aria-closure-kernel/paper/main.tex:194:aria-chess~\citep{SmartAriaChess2026}) carry their own

exec
/bin/bash -lc "rg -n '\\\\(citep|cite|ref|label)\\{' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F '\\Ph' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex && rg -n -F '\\Lop' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex && rg -n -F '\\Cph' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex && rg -n -F '\\Rsixhundred' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -i 'derive|derived|unique|uniqueness|selection|Lyapunov|2I|equivariance|theorem|forced|fixed by|post-hoc|AIC|Mode-B|Mode B|Gaussian|17/18|18/18|0\\.997|0\\.976|0\\.923|0\\.888|0\\.884|varphi' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n -F 'φ' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex papers/aria-closure-kernel/repro/verify_kernel.py papers/aria-closure-kernel/repro/results.json" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 333ms:
papers/aria-closure-kernel/paper/sections/05_agreement.tex:2:\section{Discrete-to-continuum agreement}\label{sec:agreement}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:16:\subsection{The test}\label{ssec:test}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:36:\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:69:\subsection{Variant comparison}\label{ssec:variant_comparison}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:95:\label{tab:variant_correlation}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:111:b-anomaly paper~\citep{SmartBAnomaly2026} established
papers/aria-closure-kernel/paper/sections/05_agreement.tex:113:on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:146:an open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/sections/09_limitations.tex:2:\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:12:\subsection{Regime}\label{ssec:regime}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:20:derivation. \emph{Disclosure:} \S\ref{sec:intro},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:21:\S\ref{sec:substrate}, \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:23:empirical landings of \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/09_limitations.tex:24:\S\ref{sec:active_witness}. \emph{Strengthening build:}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:28:substrates from~\citep{SmartBAnomaly2026}; the aria-chess
papers/aria-closure-kernel/paper/sections/09_limitations.tex:41:\subsection{Post-hoc}\label{ssec:posthoc}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:49:or $120$-cell. \emph{Disclosure:} \S\ref{sec:intro}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:70:\S\ref{ssec:opnorm}, \S\ref{sec:definition}. \emph{Evidence:} the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:73:regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:74:\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
papers/aria-closure-kernel/paper/sections/09_limitations.tex:79:\subsection{Interpretation}\label{ssec:interpretation}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:87:continuum kernel. \emph{Disclosure:} \S\ref{sec:agreement} marks
papers/aria-closure-kernel/paper/sections/09_limitations.tex:104:\subsection{Test/claim}\label{ssec:testclaim}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:113:verbatim. \emph{Disclosure:} \S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:114:\S\ref{sec:active_witness}. \emph{Evidence:} the witnesses pass
papers/aria-closure-kernel/paper/sections/09_limitations.tex:134:\subsection{State-drift / out-of-scope}\label{ssec:scope}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:137:\S\ref{sec:programme_home}, the selection-layer constructions
papers/aria-closure-kernel/paper/sections/09_limitations.tex:140:preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
papers/aria-closure-kernel/paper/sections/09_limitations.tex:153:  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:159:  regular 4-polytopes — see \S\ref{ssec:regime}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:161:  specified large-graph limit — see \S\ref{ssec:interpretation}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:163:  \S\ref{ssec:posthoc}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:17:$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:31:\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:38:\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:65:4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:74:identified in \S\ref{sec:programme_home}. Family-membership is
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:2:\section{Active-regime witness: aria-chess}\label{sec:active_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:10:\subsection{What aria-chess tests}\label{ssec:aria_setup}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:22:  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:44:preregistered tally as reported in~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:149:\label{tab:two_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:154:Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:2:\section{Programme home and the open selection layer}\label{sec:programme_home}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:33:\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:71:  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:76:\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:100:  generally strict (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:102:  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:103:  Table~\ref{tab:spectrum}, both reproduced numerically
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:108:  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:111:  qualitatively distinct regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:112:  \S\ref{sec:active_witness}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:128:  inherited verbatim from~\citep{SmartBAnomaly2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:132:  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:2:\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:10:\subsection{What b-anomaly tests}\label{ssec:banomaly_setup}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:18:\begin{equation}\label{eq:banomaly_kernel}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:40:(verbatim from~\citep{SmartBAnomaly2026}, also at
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:47:from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:49:\label{tab:banomaly}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:74:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:79:  amplification ($\sim 2.2$~\citep{KrugerMatias2005}). The
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:122:  preprint's limitations section~\citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:147:second landing is in \S\ref{sec:active_witness}.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:2:\section{The Laplacian spectrum}\label{sec:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:8:Table~\ref{tab:spectrum} to machine precision; multiplicities sum
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:23:\label{tab:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:65:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:84:\label{ssec:irrep}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:92:layer~\citep{SmartAriaChess2026} realises this block decomposition
papers/aria-closure-kernel/paper/sections/02_definition.tex:2:\section{The closure-response operator}\label{sec:definition}
papers/aria-closure-kernel/paper/sections/02_definition.tex:16:\begin{equation}\label{eq:cphi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:21:\begin{equation}\label{eq:psi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:25:\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}
papers/aria-closure-kernel/paper/sections/02_definition.tex:27:The properties developed in \S\ref{ssec:positivity}--\S\ref{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:51:  function in \S\ref{ssec:continuum});
papers/aria-closure-kernel/paper/sections/02_definition.tex:60:\subsection{Positive definiteness}\label{ssec:positivity}
papers/aria-closure-kernel/paper/sections/02_definition.tex:72:\subsection{Operator-norm bound}\label{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:76:\begin{equation}\label{eq:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:82:case used in \S\ref{ssec:continuum}), this reduces to the identity
papers/aria-closure-kernel/paper/sections/02_definition.tex:83:\begin{equation}\label{eq:opnorm_zero_mode}
papers/aria-closure-kernel/paper/sections/02_definition.tex:93:\S\ref{ssec:opnorm_check}); this matches the closed-form $\Ph^{2}$
papers/aria-closure-kernel/paper/sections/02_definition.tex:96:\subsection{Continuum projection}\label{ssec:continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:102:\begin{equation}\label{eq:green_continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:110:discrete-to-continuum agreement test (\S\ref{sec:agreement}):
papers/aria-closure-kernel/paper/sections/02_definition.tex:131:an open build (\S\ref{sec:limitations}). The companion
papers/aria-closure-kernel/paper/sections/02_definition.tex:133:preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:2:\section{The 600-cell substrate}\label{sec:substrate}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:9:the empirical landings (\S\ref{sec:limitations}); the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:11:not prove, here~\citep{CoxeterRegularPolytopes}. All facts in
papers/aria-closure-kernel/paper/sections/03_substrate.tex:16:\subsection{Vertex set}\label{ssec:vertices}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:19:$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:44:\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:53:\begin{equation}\label{eq:short_edge}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:59:into $S^{3}$~\citep{CoxeterRegularPolytopes}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:74:  in~\citep{CoxeterRegularPolytopes}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:80:\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:86:\begin{equation}\label{eq:shell_inner}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:94:\begin{equation}\label{eq:shell_sizes}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:108:\subsection{Inner-product check}\label{ssec:inner_product_check}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:126:  Laplacian spectrum (\S\ref{sec:spectrum}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:129:  (\S\ref{ssec:opnorm}); the operator-norm bound
papers/aria-closure-kernel/paper/sections/03_substrate.tex:135:  (\S\ref{sec:passive_witness}, \S\ref{sec:active_witness}). A
papers/aria-closure-kernel/paper/sections/03_substrate.tex:137:  open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/main.tex:46:is post-hoc motivated by those landings, \S\ref{sec:limitations};
papers/aria-closure-kernel/paper/main.tex:55:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
papers/aria-closure-kernel/paper/main.tex:60:public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
papers/aria-closure-kernel/paper/main.tex:63:signatures~\citep{SmartAriaChess2026}.
papers/aria-closure-kernel/paper/main.tex:73:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
papers/aria-closure-kernel/paper/main.tex:88:direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
papers/aria-closure-kernel/paper/main.tex:90:six drug/sleep EEG signatures~\citep{SmartAriaChess2026}. We
papers/aria-closure-kernel/paper/main.tex:124:\ref{tab:spectrum}, \S\ref{sec:substrate}).
papers/aria-closure-kernel/paper/main.tex:134:precision (multi-source sweep, \S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/main.tex:137:(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
papers/aria-closure-kernel/paper/main.tex:144:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:190:in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
papers/aria-closure-kernel/paper/main.tex:191:\S\ref{sec:agreement} are deterministic outputs of the script.
papers/aria-closure-kernel/paper/main.tex:193:(b-anomaly~\citep{SmartBAnomaly2026},
papers/aria-closure-kernel/paper/main.tex:194:aria-chess~\citep{SmartAriaChess2026}) carry their own
papers/aria-closure-kernel/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:18:\begin{equation}\label{eq:cphi_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:28:\begin{equation}\label{eq:opnorm_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:33:$\Ph$ (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:41:(\S\ref{sec:limitations}); the construction itself is theorem-level
papers/aria-closure-kernel/paper/sections/01_introduction.tex:85:  (\S\ref{sec:passive_witness}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:87:  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:93:  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:125:  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:142:preprint~\citep{SmartAriaChess2026}: numerical results
papers/aria-closure-kernel/paper/sections/01_introduction.tex:182:\S\ref{sec:definition} gives the operator definition, the positivity
papers/aria-closure-kernel/paper/sections/01_introduction.tex:184:projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
papers/aria-closure-kernel/paper/sections/01_introduction.tex:186:decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:188:\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
papers/aria-closure-kernel/paper/sections/01_introduction.tex:189:across three Laplacian variants. \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:190:\S\ref{sec:active_witness} thread the two independent empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:192:\S\ref{sec:programme_home} positions $\Cph$ as the programme home
papers/aria-closure-kernel/paper/sections/01_introduction.tex:194:Millennium drafts. \S\ref{sec:limitations} enumerates limitations
papers/aria-closure-kernel/paper/sections/01_introduction.tex:195:in a five-move guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 317ms:
papers/aria-closure-kernel/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:18:fits on either empirical landing. The 600-cell choice is post-hoc
papers/aria-closure-kernel/paper/sections/09_limitations.tex:22:\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
papers/aria-closure-kernel/paper/sections/09_limitations.tex:41:\subsection{Post-hoc}\label{ssec:posthoc}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:43:\textbf{The 600-cell choice is post-hoc justified by empirical
papers/aria-closure-kernel/paper/sections/09_limitations.tex:45:theorem-level rigorous (H$_4$ Coxeter group theory), the choice
papers/aria-closure-kernel/paper/sections/09_limitations.tex:48:geometric or algebraic argument selecting it over the $24$-cell
papers/aria-closure-kernel/paper/sections/09_limitations.tex:66:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
papers/aria-closure-kernel/paper/sections/09_limitations.tex:68:strictly positive definite; it is not derived from a closure
papers/aria-closure-kernel/paper/sections/09_limitations.tex:74:\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
papers/aria-closure-kernel/paper/sections/09_limitations.tex:77:uniqueness is not assumed and is itself an open problem.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:82:causal.} The per-vertex correlation $0.976$ between $\psi$ on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:89:precision in the operator-norm bound and at $\rho = 0.976$ in the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:92:limit; a continuum limit theorem on H$_n$ Coxeter substrates as
papers/aria-closure-kernel/paper/sections/09_limitations.tex:98:\emph{unique} natural ranking. Edge-weighted variants outside the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:108:under an AIC tie with $\mathrm{FREE\_C9}$ on current data; the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:110:substrate \emph{is} consciousness). Neither lands a theorem-grade
papers/aria-closure-kernel/paper/sections/09_limitations.tex:115:their own preregistered or literature-derived thresholds.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:124:$0.976$ is reported with the canonical pole ($+x_{0}$ axis) as
papers/aria-closure-kernel/paper/sections/09_limitations.tex:128:per-vertex correlation $0.976202$ to within $\sim 10^{-15}$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:136:\textbf{Selection layer not delivered.} As enumerated in
papers/aria-closure-kernel/paper/sections/09_limitations.tex:137:\S\ref{sec:programme_home}, the selection-layer constructions
papers/aria-closure-kernel/paper/sections/09_limitations.tex:138:(Lyapunov $V(W)$, edge-space decomposition under $2I$-equivariance,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:142:in the response primitive without addressing the selection gap.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:152:\item Lyapunov function $V(W)$ on the reduced flow — open build
papers/aria-closure-kernel/paper/sections/09_limitations.tex:154:\item $2I$-equivariance audit of the closure operator family —
papers/aria-closure-kernel/paper/sections/09_limitations.tex:158:\item Selection theorem identifying $\Rsixhundred$ over alternative
papers/aria-closure-kernel/paper/sections/09_limitations.tex:160:\item Formal discrete-to-continuum convergence theorem under a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:164:\item Family-membership classification theorem for the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:174:the unique kernel for either landing. We do not claim selection is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:175:delivered. We do not claim 600-cell uniqueness. The strengthening
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:20:chord distances (non-source vertices) is Pearson $\rho = 0.976$ on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:22:variants tested ($0.888$ geometric, $0.884$ arithmetic). All numbers are reproduced from canonical
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:56:a derivation of physics on either landing. We do not derive the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:58:claim 600-cell uniqueness; alternative regular 4-polytopes are an
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:59:explicit ablation build. We do not claim kernel uniqueness on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:60:either empirical landing; the b-anomaly's free-width Gaussian
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:61:alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:64:not deliver a selection theorem on the ACT
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:66:open builds (Lyapunov $V(W)$, edge-space decomposition under
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:67:$2I$-equivariance, full reduced-flow convergence) remain open and
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:71:polynomial-in-$L$ Lyapunov family — RH polynomial filter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:78:selection gap.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:81:broader programme to convert the witness into a selection-theorem-
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:2:\section{Programme home and the open selection layer}\label{sec:programme_home}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:8:\emph{response} primitive; \emph{selection} (which response
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:12:\subsection{Programme home: polynomial-in-$L$ Lyapunov family}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:44:formal classification theorem identifying the family.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:46:\subsection{Response vs selection}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:49:chosen substrate plus the design-level shift: $\Cph$ is fixed by
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:54:\item Why this substrate? (Selection across regular 4-polytopes
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:56:\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:59:  time? (Crystallisation / Lyapunov descent dynamics on a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:63:The selection layer is open. It appears as an open hypothesis in
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:72:  4-tuple $(M, L_M, W, R_{\mathrm{hom}})$ proposes a Lyapunov
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:74:  $2I$-equivariance, and a full reduced-flow convergence theorem
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:78:  a selection theorem; ACT is positioned as the future
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:79:  selection-theorem witness.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:82:The recurrence of an open selection gap across these three frames
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:87:primitive without reducing or addressing the selection gap.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:106:  correlation $0.976$ on the unweighted variant, with the unweighted
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:118:  as a design-level shift; not derived from a closure functional
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:120:\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:121:  post-hoc motivated by the empirical landings; alternative regular
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:124:\item \emph{Kernel-uniqueness on either empirical landing.} The
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:125:  b-anomaly free-width Gaussian alternative (fits comparably with
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:126:  one extra shape parameter) and the AIC tie
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:129:\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:130:  decomposition under $2I$-equivariance, full reduced-flow
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:134:\item \emph{Family-membership theorem.} The programme-home
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:135:  positioning of cascade Lyapunov functionals as members of the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:47:\item $17/18$ at standard validation methodology ($5$-seed
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:49:\item $18/18$ after a documented $N\!=\!20$ deep-dive on the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:64:against literature-derived thresholds:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:109:  $0$ by H$_4$ transitivity (a theorem), $11.58$ standard
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:126:fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:132:claim 600-cell uniqueness among regular 4-polytopes, and does not
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:133:deliver a selection theorem on the ACT 4-tuple. We inherit the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:160:Headline           & $5/5$ sign uniformity              & $18/18$ prereg + $6/6$ EEG \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:163:Caveat             & AIC tie; free-width Gaussian alt.\ & single-seed EEG; no polytope ablation \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:174:is fixed by experimental condition (PROPOFOL/SLEEP/WAKE), not by
papers/aria-closure-kernel/paper/sections/05_agreement.tex:40:\item \textbf{Per-vertex Pearson correlation}: $\rho = 0.976$.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:41:\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:100:\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:101:$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:102:$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:117:this is a uniqueness result; we report it as a two-criterion
papers/aria-closure-kernel/paper/sections/05_agreement.tex:126:correlates per-vertex in radial shape, at Pearson $0.976$, with
papers/aria-closure-kernel/paper/sections/05_agreement.tex:136:\paragraph{Does not establish.} Operator uniqueness on either
papers/aria-closure-kernel/paper/sections/05_agreement.tex:138:Gaussian alternative that fits comparably in $\chi^{2}$ at the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:142:$\Rsixhundred$ is the unique discrete substrate with this
papers/aria-closure-kernel/paper/sections/03_substrate.tex:8:Laplacian. The choice of this polytope is post-hoc motivated by
papers/aria-closure-kernel/paper/sections/03_substrate.tex:61:\paragraph{Graph facts (forced by the construction).}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:106:The antipode $-v_{0}$ is the unique shell-$8$ vertex.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:123:\item \textbf{Fixed by the construction once $\Rsixhundred$ is
papers/aria-closure-kernel/paper/sections/03_substrate.tex:127:\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
papers/aria-closure-kernel/paper/sections/03_substrate.tex:131:\item \textbf{Not fixed by this paper}: the choice of
papers/aria-closure-kernel/paper/sections/03_substrate.tex:134:  post-hoc motivated by the empirical landings
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:13:algebraic recognition of the displayed values, not by an exact
papers/aria-closure-kernel/paper/sections/01_introduction.tex:40:polytope is post-hoc motivated by the empirical landings
papers/aria-closure-kernel/paper/sections/01_introduction.tex:41:(\S\ref{sec:limitations}); the construction itself is theorem-level
papers/aria-closure-kernel/paper/sections/01_introduction.tex:60:\item \textbf{Operator definition is fixed by the construction.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:72:  $\rho = 0.976$ on the unweighted graph Laplacian. This is
papers/aria-closure-kernel/paper/sections/01_introduction.tex:80:  correlation: $0.888$ and $0.884$ respectively. Within the three
papers/aria-closure-kernel/paper/sections/01_introduction.tex:105:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:108:\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:112:  is post-hoc motivated by the empirical landings; a formal
papers/aria-closure-kernel/paper/sections/01_introduction.tex:114:\item \emph{Not a kernel-uniqueness claim on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:115:  landing.} The b-anomaly's free-width Gaussian alternative shows
papers/aria-closure-kernel/paper/sections/01_introduction.tex:116:  that a free-width Gaussian charm-loop proxy fits the same five
papers/aria-closure-kernel/paper/sections/01_introduction.tex:118:  parameter; the b-anomaly AIC comparison against
papers/aria-closure-kernel/paper/sections/01_introduction.tex:123:\item \emph{Not a selection theorem on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:126:  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:127:  fills the response slot. Selection — Lyapunov $V(W)$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:128:  reduced flow, edge-space decomposition under $2I$-equivariance,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:153:operator-norm bound, the per-vertex correlation $0.976$) licenses
papers/aria-closure-kernel/paper/sections/01_introduction.tex:156:aria-chess $18/18$ preregistered tally) licenses a `consistent
papers/aria-closure-kernel/paper/sections/01_introduction.tex:158:`derives the kernel', `proves uniqueness', or `establishes
papers/aria-closure-kernel/paper/sections/01_introduction.tex:159:selection'.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:169:structural fit; aria-chess $18/18$ preregistered correspondences
papers/aria-closure-kernel/paper/sections/01_introduction.tex:172:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:173:$\Rsixhundred$; uniqueness of the kernel shape on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:174:landing; a selection theorem on the ACT 4-tuple; that either
papers/aria-closure-kernel/paper/sections/01_introduction.tex:193:for the polynomial-in-$L$ Lyapunov family that recurs across the
papers/aria-closure-kernel/paper/main.tex:14:\newcommand{\Ph}{\varphi}
papers/aria-closure-kernel/paper/main.tex:46:is post-hoc motivated by those landings, \S\ref{sec:limitations};
papers/aria-closure-kernel/paper/main.tex:53:agreement at per-vertex Pearson correlation $0.976$ between the
papers/aria-closure-kernel/paper/main.tex:70:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:72:selection theorem on the companion adaptive-closure-transport
papers/aria-closure-kernel/paper/main.tex:75:empirical landing (the b-anomaly AIC comparison and the aria-chess
papers/aria-closure-kernel/paper/main.tex:99:agreement at per-vertex Pearson correlation $0.976$ for the
papers/aria-closure-kernel/paper/main.tex:101:tested ($0.888$ geometric, $0.884$ arithmetic). Within the three
papers/aria-closure-kernel/paper/main.tex:130:vertex's chord distance: $0.976$ (unweighted Laplacian), $0.888$
papers/aria-closure-kernel/paper/main.tex:131:($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
papers/aria-closure-kernel/paper/main.tex:149:degree, passes $17/18$ preregistered correspondences (frozen
papers/aria-closure-kernel/paper/main.tex:150:2026-04-18) at standard methodology and $18/18$ after a documented
papers/aria-closure-kernel/paper/main.tex:156:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/main.tex:158:not claim $\Rsixhundred$ is the unique substrate consistent with
papers/aria-closure-kernel/paper/main.tex:160:unique kernel shape consistent with the b-anomaly data
papers/aria-closure-kernel/paper/main.tex:161:(b-anomaly's free-width Gaussian alternative and Mode-B refit
papers/aria-closure-kernel/paper/main.tex:163:aria-chess substrate witness establishes a selection theorem on
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:52:Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:88:  (correlation $0.997$ with the continuum kernel, b-anomaly
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:101:\item \textbf{AIC tie on current data.} On Akaike model comparison,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:102:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:104:  indistinguishable: stacked AIC weights
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:106:  Current data cannot resolve the model comparison. AIC is blind
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:108:  decisive about whether the shape is forced by data: it is not.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:109:\item \textbf{Free-width Gaussian alternative.} A free-width
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:110:  Gaussian charm-loop proxy fits the same five datasets comparably
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:112:  is not the unique $q^{2}$ shape consistent with the anomaly.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:113:\item \textbf{Mode-B drift (linearised-to-non-linear refit).} An
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:114:  earlier analysis the b-anomaly project labels Mode-B
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:116:  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:117:  the subsequent non-linear refit; the $+2.77$-AIC-unit drift
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:118:  between Mode-B (linearised) and the non-linear refit is the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:140:not establish the kernel as theorem-grade physics on the flavour
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:141:side (the AIC tie, the free-width Gaussian alternative, and the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:142:Mode-B linearised-to-non-linear refit drift prevent that). It
papers/aria-closure-kernel/paper/sections/02_definition.tex:123:  are fixed by the single design choice $\Ph^{-2}$, giving a single
papers/aria-closure-kernel/paper/sections/02_definition.tex:128:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/sections/02_definition.tex:134:selection-layer dynamics over $W$-space that would, if delivered,

 exited 1 in 313ms:
 succeeded in 433ms:
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:5:The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:6:600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:10:smallest eigenvalue $\Ph^{-2}$ and operator-norm identity
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:11:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$ (general substrates with
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:13:$\|\Cph^{-1}\| < \Ph^{2}$).
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:17:$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:19:the continuum kernel $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:21:the unweighted Laplacian, above the two $\Ph$-cocycle weighted
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:48:$\Ph^{-2}$. Above that operator level, they share no fitted
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:57:$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
papers/aria-closure-kernel/paper/sections/09_limitations.tex:32:\textbf{Single shift ($\Ph^{-2}$).} We have not tested whether
papers/aria-closure-kernel/paper/sections/09_limitations.tex:33:nearby shifts ($\Ph^{-2} \pm \epsilon$ for small $\epsilon$) give
papers/aria-closure-kernel/paper/sections/09_limitations.tex:37:\emph{Strengthening build:} sweep $\Ph^{-2} \cdot (1 \pm \delta)$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:66:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
papers/aria-closure-kernel/paper/sections/09_limitations.tex:67:$\Ph^{-2} \approx 0.382$ is a stability clamp making $\Cph$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:84:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the same chord radii is a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:99:$\Ph$-cocycle family ($\sqrt{\deg}$-weighted, normalised
papers/aria-closure-kernel/paper/sections/09_limitations.tex:162:\item First-principles derivation of the $\Ph^{-2}$ shift — see
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:32:The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:81:\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:82:  direction confirmed; $\Phi$-proxy not full IIT).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:124:this paper. The kernel shift $\Ph^{-2}$ is not retuned between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:159:Shift $\Ph^{-2}$   & not retuned                        & not retuned \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:170:the same shift $\Ph^{-2}$. They share no fitted parameter,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:27:operator, not a derivation of $\Ph^{-2}$), and $A$ is a single
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:86:  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:51:$\Ph^{-2}$, and the response is the resulting linear inverse.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:56:\item Why this shift? (Selection of $\Ph^{-2}$ over an arbitrary
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:95:  identity $\|\Cph^{-1}\| = \Ph^{2}$ holds whenever
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:99:  cases) the bound $\|\Cph^{-1}\| \leq \Ph^{2}$ holds and is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:108:  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:117:\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
papers/aria-closure-kernel/paper/sections/05_agreement.tex:9:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
papers/aria-closure-kernel/paper/sections/05_agreement.tex:13:the three tested variants (unweighted, $\Ph$-geometric weighted,
papers/aria-closure-kernel/paper/sections/05_agreement.tex:14:$\Ph$-arithmetic weighted).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:22:\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:28:G(x(v)) \;=\; (\Ph/2)\,\exp(-\,x(v)/\Ph).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:71:Two $\Ph$-cocycle weighted Laplacian variants are tested as
papers/aria-closure-kernel/paper/sections/05_agreement.tex:75:\item \textbf{$\Ph$-geometric weights}: edge weight
papers/aria-closure-kernel/paper/sections/05_agreement.tex:77:  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:79:\item \textbf{$\Ph$-arithmetic weights}: edge weight
papers/aria-closure-kernel/paper/sections/05_agreement.tex:91:discrete response $\psi = (L_{w} + \Ph^{-2} I)^{-1} e_{v_{0}}$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:93:Laplacian variants ($L_{w}$ unweighted or $\Ph$-cocycle weighted).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:101:$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:102:$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:128:$\Ph$. This is a non-trivial Pearson correlation between
papers/aria-closure-kernel/paper/sections/05_agreement.tex:130:sharing the same design-level scale $\Ph^{-2}$: (i) the discrete
papers/aria-closure-kernel/paper/sections/05_agreement.tex:132:(ii) a one-dimensional continuum exponential. The $\Ph$-mediated
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:7:values match the closed-form $\mathbb{Z}[\Ph]$ list given in
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:20:Closed-form values in $\mathbb{Z}[\Ph]$ alongside the numerical
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:29:$12 - 6\Ph$    & $2.2918$  & $4$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:30:$12 - 4\Ph$    & $5.5279$  & $9$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:34:$4\Ph + 8$     & $14.4721$ & $9$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:36:$6\Ph + 6$     & $15.7082$ & $4$ \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:43:\paragraph{Closed-form check.} Using $\Ph = (1+\sqrt 5)/2$:
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:45:12 - 6\Ph &= 12 - 3(1+\sqrt 5) = 9 - 3\sqrt 5 \approx 2.2918, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:46:12 - 4\Ph &= 12 - 2(1+\sqrt 5) = 10 - 2\sqrt 5 \approx 5.5279, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:47:4\Ph + 8 &= 2(1+\sqrt 5) + 8 = 10 + 2\sqrt 5 \approx 14.4721, \\
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:48:6\Ph + 6 &= 3(1+\sqrt 5) + 6 = 9 + 3\sqrt 5 \approx 15.7082.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:50:The eigenvalue pairs $\{12 - 6\Ph,\ 6\Ph+6\}$ (both with multiplicity
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:51:$4$) and $\{12 - 4\Ph,\ 4\Ph+8\}$ (both with multiplicity $9$)
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:53:$\sigma\colon \sqrt 5 \mapsto -\sqrt 5$ on $\mathbb{Z}[\Ph]$. The
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:67:The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:69:\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:74:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:77:$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:80:$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:81:= 9 + 3\sqrt 5 + (2 - \Ph) \approx 16.0902$.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:89:$\sigma$-automorphism of $\mathbb{Z}[\Ph]$ the exponents become
papers/aria-closure-kernel/paper/sections/03_substrate.tex:20:Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical vertex
papers/aria-closure-kernel/paper/sections/03_substrate.tex:27:\item \textbf{$\Ph$-mixed family} ($96$ vertices): all even
papers/aria-closure-kernel/paper/sections/03_substrate.tex:28:  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:29:  $\Ph^{2} = \Ph + 1$ identity, equivalently
papers/aria-closure-kernel/paper/sections/03_substrate.tex:30:  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:54:\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:57:$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:89:\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
papers/aria-closure-kernel/paper/sections/03_substrate.tex:90:       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
papers/aria-closure-kernel/paper/sections/03_substrate.tex:114:is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:117:inner product exactly $\Ph/2$ within machine precision (tolerance
papers/aria-closure-kernel/paper/sections/03_substrate.tex:127:\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
papers/aria-closure-kernel/paper/sections/03_substrate.tex:128:  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:130:  $\|\Cph^{-1}\| = \Ph^{2}$.
papers/aria-closure-kernel/paper/sections/02_definition.tex:12:Let $\Ph = (1+\sqrt 5)/2$ be the golden ratio, with $\Ph^{-1} = \Ph - 1$
papers/aria-closure-kernel/paper/sections/02_definition.tex:13:and $\Ph^{-2} = 2 - \Ph \approx 0.381966$.
papers/aria-closure-kernel/paper/sections/02_definition.tex:17:\Cph \;=\; L_M + \Ph^{-2} I.
papers/aria-closure-kernel/paper/sections/02_definition.tex:22:\psi \;=\; \Cph^{-1} f \;=\; (L_M + \Ph^{-2} I)^{-1} f.
papers/aria-closure-kernel/paper/sections/02_definition.tex:64:eigenspace (the constant vector). For $\Cph = L_M + \Ph^{-2} I$,
papers/aria-closure-kernel/paper/sections/02_definition.tex:66:\lambda_{\min}(\Cph) \;=\; \lambda_{\min}(L_M) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/02_definition.tex:67:                    \;=\; \Ph^{-2} \;>\; 0,
papers/aria-closure-kernel/paper/sections/02_definition.tex:78:              \;=\; 1/(\lambda_{\min}(L_M) + \Ph^{-2}).
papers/aria-closure-kernel/paper/sections/02_definition.tex:84:\|\Cph^{-1}\| \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/02_definition.tex:88:$\|\Cph^{-1}\| < \Ph^{2}$. The response-amplification ceiling is,
papers/aria-closure-kernel/paper/sections/02_definition.tex:90:the design-level shift $\Ph^{-2}$ is precisely what guarantees a
papers/aria-closure-kernel/paper/sections/02_definition.tex:93:\S\ref{ssec:opnorm_check}); this matches the closed-form $\Ph^{2}$
papers/aria-closure-kernel/paper/sections/02_definition.tex:99:$L_{\Ph} = -d^{2}/dx^{2} + \Ph^{-2}$, the Green's function
papers/aria-closure-kernel/paper/sections/02_definition.tex:100:$G(x)$ satisfies $L_{\Ph} G = \delta_{0}$ and is the closed-form
papers/aria-closure-kernel/paper/sections/02_definition.tex:103:G(x) \;=\; \frac{\Ph}{2}\, e^{-|x|/\Ph}.
papers/aria-closure-kernel/paper/sections/02_definition.tex:105:The decay scale is $\Ph$ — the same constant that appears in the
papers/aria-closure-kernel/paper/sections/02_definition.tex:107:$\kappa(x) = e^{-|x|/\Ph}$ with unit value at the source.
papers/aria-closure-kernel/paper/sections/02_definition.tex:115:\subsection{Disclosure: $\Ph^{-2}$ is a design-level shift}
papers/aria-closure-kernel/paper/sections/02_definition.tex:117:The shift $\Ph^{-2}$ is chosen so that:
papers/aria-closure-kernel/paper/sections/02_definition.tex:120:  is exactly $\Ph^{-2}$);
papers/aria-closure-kernel/paper/sections/02_definition.tex:121:\item both the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ and
papers/aria-closure-kernel/paper/sections/02_definition.tex:122:  the continuum decay scale $\Ph$ (Eq.~\eqref{eq:green_continuum})
papers/aria-closure-kernel/paper/sections/02_definition.tex:123:  are fixed by the single design choice $\Ph^{-2}$, giving a single
papers/aria-closure-kernel/paper/sections/02_definition.tex:126:  has decay scale $\Ph$, not a free length parameter.
papers/aria-closure-kernel/paper/sections/02_definition.tex:128:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/sections/01_introduction.tex:19:\Cph \;=\; L_M + \Ph^{-2} I,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:20:\qquad \Ph \;=\; (1+\sqrt 5)/2,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:24:$\Ph^{-2} \approx 0.382$ regularises the inverse: for self-adjoint
papers/aria-closure-kernel/paper/sections/01_introduction.tex:26:positive definite, the smallest eigenvalue is $\Ph^{-2}$, and the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:29:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:32:Green's function $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ with decay scale
papers/aria-closure-kernel/paper/sections/01_introduction.tex:33:$\Ph$ (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:38:$16$ half-integer vertices, $96$ $\Ph$-mixed vertices), connected by
papers/aria-closure-kernel/paper/sections/01_introduction.tex:39:short edges $\langle v, w\rangle = \Ph/2$. The choice of this
papers/aria-closure-kernel/paper/sections/01_introduction.tex:46:classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:62:  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
papers/aria-closure-kernel/paper/sections/01_introduction.tex:77:  Two $\Ph$-cocycle weighted Laplacian variants ($\Ph$-geometric,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:78:  $\Ph$-arithmetic edge weights via shell-grade exponents
papers/aria-closure-kernel/paper/sections/01_introduction.tex:79:  $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
papers/aria-closure-kernel/paper/sections/01_introduction.tex:103:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:104:  $\Ph^{-2}$ is a design-level stability clamp that bounds
papers/aria-closure-kernel/paper/sections/01_introduction.tex:105:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:111:  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
papers/aria-closure-kernel/paper/sections/01_introduction.tex:172:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:187:in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
papers/aria-closure-kernel/paper/main.tex:14:\newcommand{\Ph}{\varphi}
papers/aria-closure-kernel/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
papers/aria-closure-kernel/paper/main.tex:20:       $\Cph = L_M + \Ph^{-2} I$:\\
papers/aria-closure-kernel/paper/main.tex:41:$\Cph = L_M + \Ph^{-2} I$ on a closure substrate $M$ with
papers/aria-closure-kernel/paper/main.tex:43:and golden ratio $\Ph = (1 + \sqrt 5)/2$. We use
papers/aria-closure-kernel/paper/main.tex:50:matching the closed-form $\mathbb{Z}[\Ph]$ values), establish the
papers/aria-closure-kernel/paper/main.tex:51:operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
papers/aria-closure-kernel/paper/main.tex:52:eigenvalue $\Ph^{-2}$, and verify the discrete-to-continuum
papers/aria-closure-kernel/paper/main.tex:55:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
papers/aria-closure-kernel/paper/main.tex:70:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:80:We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
papers/aria-closure-kernel/paper/main.tex:82:$\Ph = (1+\sqrt 5)/2$, give the 600-cell graph $\Rsixhundred$ as
papers/aria-closure-kernel/paper/main.tex:95:Laplacian spectrum numerically matching closed-form $\mathbb{Z}[\Ph]$
papers/aria-closure-kernel/paper/main.tex:96:values, operator-norm identity $\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$
papers/aria-closure-kernel/paper/main.tex:100:unweighted variant, above the two $\Ph$-cocycle weighted variants
papers/aria-closure-kernel/paper/main.tex:111:$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
papers/aria-closure-kernel/paper/main.tex:113:$\Ph^{-2} \approx 0.382$, operator norm
papers/aria-closure-kernel/paper/main.tex:114:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
papers/aria-closure-kernel/paper/main.tex:116:$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
papers/aria-closure-kernel/paper/main.tex:121:$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
papers/aria-closure-kernel/paper/main.tex:123:in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
papers/aria-closure-kernel/paper/main.tex:131:($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
papers/aria-closure-kernel/paper/main.tex:156:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/sections/05_agreement.tex:22:\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:5:The unweighted graph Laplacian $\Lop = D - A$ on $\Rsixhundred$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:19:\caption{Computed Laplacian spectrum of $\Lop$ on $\Rsixhundred$.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:67:The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:80:$\lambda_{\max}(\Lop) + \Ph^{-2} = (6\Ph + 6) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:86:The eigenspaces of $\Lop$ partition into H$_4$-proper and
papers/aria-closure-kernel/paper/main.tex:15:\newcommand{\Lop}{L_{V_{600}}}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:5:The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:11:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$ (general substrates with
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:13:$\|\Cph^{-1}\| < \Ph^{2}$).
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:18:discrete-to-continuum agreement between $\psi = \Cph^{-1} f$ and
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:27:$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:47:operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:5:This section positions $\Cph$ within the broader cascade programme
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:7:matters for the hostile-review reading: $\Cph$ is the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:17:family as $\Cph$:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:30:  programme-positioned as a $\Cph$-style mass-regularised Laplacian
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:48:The closure response $\psi = \Cph^{-1} f$ is determined by the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:49:chosen substrate plus the design-level shift: $\Cph$ is fixed by
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:93:\item The operator $\Cph$ is well-defined and positive definite
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:95:  identity $\|\Cph^{-1}\| = \Ph^{2}$ holds whenever
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:99:  cases) the bound $\|\Cph^{-1}\| \leq \Ph^{2}$ holds and is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:109:\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
papers/aria-closure-kernel/paper/sections/09_limitations.tex:15:whether $\Cph$ on the $24$-cell, the $120$-cell, or other H$_n$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:67:$\Ph^{-2} \approx 0.382$ is a stability clamp making $\Cph$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:13:the same $\Cph$ on the same $\Rsixhundred$. The architecture
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:116:witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:117:layer above $\Cph$ uses one condition-dependent coupling and one
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:126:fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:135:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:138:projection above $\Cph$ and the aria-chess recurrent self-model
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:139:layer above $\Cph$ are distinct above-operator constructions; the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:147:\caption{Two independent empirical landings of $\Cph$ on
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:157:Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:169:operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
papers/aria-closure-kernel/paper/sections/05_agreement.tex:6:discrete response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a
papers/aria-closure-kernel/paper/sections/05_agreement.tex:22:\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:33:trivially the diagonal of $\Cph^{-1}$ and the chord distance is
papers/aria-closure-kernel/paper/sections/05_agreement.tex:51:  response there is the diagonal of $\Cph^{-1}$ and the chord
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:65:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:67:The smallest eigenvalue of $\Cph = \Lop + \Ph^{-2} I$ is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:69:\lambda_{\min}(\Cph) \;=\; 0 + \Ph^{-2} \;=\; \Ph^{-2}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:74:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:77:$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:79:of $\Cph$ is
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:24:the projection of $\Cph$ on $\Rsixhundred$ to the flavour-physics
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:34:This is a \emph{structural} test: same fixed $\Cph$ on the same
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:102:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111:  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:135:witness for $\Cph$ on $\Rsixhundred$: a single linear response
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:136:$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:144:that the same fixed $\Cph$ on the same fixed $\Rsixhundred$ is
papers/aria-closure-kernel/paper/sections/03_substrate.tex:128:  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
papers/aria-closure-kernel/paper/sections/03_substrate.tex:130:  $\|\Cph^{-1}\| = \Ph^{2}$.
papers/aria-closure-kernel/paper/sections/02_definition.tex:17:\Cph \;=\; L_M + \Ph^{-2} I.
papers/aria-closure-kernel/paper/sections/02_definition.tex:22:\psi \;=\; \Cph^{-1} f \;=\; (L_M + \Ph^{-2} I)^{-1} f.
papers/aria-closure-kernel/paper/sections/02_definition.tex:64:eigenspace (the constant vector). For $\Cph = L_M + \Ph^{-2} I$,
papers/aria-closure-kernel/paper/sections/02_definition.tex:66:\lambda_{\min}(\Cph) \;=\; \lambda_{\min}(L_M) + \Ph^{-2}
papers/aria-closure-kernel/paper/sections/02_definition.tex:69:so $\Cph$ is strictly positive definite and $\Cph^{-1}$ is
papers/aria-closure-kernel/paper/sections/02_definition.tex:74:The operator norm of $\Cph^{-1}$ is the reciprocal of the smallest
papers/aria-closure-kernel/paper/sections/02_definition.tex:75:eigenvalue of $\Cph$:
papers/aria-closure-kernel/paper/sections/02_definition.tex:77:\|\Cph^{-1}\| \;=\; 1/\lambda_{\min}(\Cph)
papers/aria-closure-kernel/paper/sections/02_definition.tex:84:\|\Cph^{-1}\| \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/02_definition.tex:88:$\|\Cph^{-1}\| < \Ph^{2}$. The response-amplification ceiling is,
papers/aria-closure-kernel/paper/sections/02_definition.tex:89:in either case, $\|\psi\|_{2} \leq \|\Cph^{-1}\|\, \|f\|_{2}$, and
papers/aria-closure-kernel/paper/sections/02_definition.tex:91:finite ceiling. Numerically reproduced as $\|\Cph^{-1}\| =
papers/aria-closure-kernel/paper/sections/02_definition.tex:111:the discrete response $\psi(v) = \Cph^{-1} f(v)$ at a vertex $v$ at
papers/aria-closure-kernel/paper/sections/02_definition.tex:119:\item $\Cph$ is strictly positive definite (the smallest eigenvalue
papers/aria-closure-kernel/paper/sections/02_definition.tex:121:\item both the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:19:\Cph \;=\; L_M + \Ph^{-2} I,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:25:non-negative $L_M$ on a connected finite graph, $\Cph$ is strictly
papers/aria-closure-kernel/paper/sections/01_introduction.tex:29:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:62:  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
papers/aria-closure-kernel/paper/sections/01_introduction.tex:70:  response $\psi = \Cph^{-1} f$ correlates per-vertex with the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:88:  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:94:  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:105:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:111:  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
papers/aria-closure-kernel/paper/sections/01_introduction.tex:126:  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
papers/aria-closure-kernel/paper/sections/01_introduction.tex:133:  level above $\Cph$. We import its empirical results verbatim and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:165:\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:183:properties of $\Cph$, the operator-norm bound, and the continuum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:192:\S\ref{sec:programme_home} positions $\Cph$ as the programme home
papers/aria-closure-kernel/paper/main.tex:16:\newcommand{\Cph}{C_{\Ph}}
papers/aria-closure-kernel/paper/main.tex:20:       $\Cph = L_M + \Ph^{-2} I$:\\
papers/aria-closure-kernel/paper/main.tex:41:$\Cph = L_M + \Ph^{-2} I$ on a closure substrate $M$ with
papers/aria-closure-kernel/paper/main.tex:51:operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
papers/aria-closure-kernel/paper/main.tex:56:\texttt{repro/verify\_kernel.py}). The same fixed $\Cph$ on the
papers/aria-closure-kernel/paper/main.tex:80:We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
papers/aria-closure-kernel/paper/main.tex:96:values, operator-norm identity $\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$
papers/aria-closure-kernel/paper/main.tex:111:$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
papers/aria-closure-kernel/paper/main.tex:114:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
papers/aria-closure-kernel/paper/main.tex:128:$\psi = \Cph^{-1} f$ for a localised source and the continuum
papers/aria-closure-kernel/paper/main.tex:138:$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
papers/aria-closure-kernel/paper/main.tex:144:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:157:stability clamp making $\Cph$ strictly positive definite. We do
papers/aria-closure-kernel/paper/sections/09_limitations.tex:22:\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
papers/aria-closure-kernel/paper/sections/09_limitations.tex:44:observables.} While the construction of $\Rsixhundred$ is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:51:$\Rsixhundred$. \emph{Strengthening build:} formal substrate
papers/aria-closure-kernel/paper/sections/09_limitations.tex:83:$\Rsixhundred$ and the continuum kernel
papers/aria-closure-kernel/paper/sections/09_limitations.tex:158:\item Selection theorem identifying $\Rsixhundred$ over alternative
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:6:600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:9:finite graph $\Rsixhundred$ where $\lambda_{\min}(L_M) = 0$ it has
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:27:$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:47:operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:31:  on $\Rsixhundred$. The artifact itself is not load-bearing for
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:50:the substrate $\Rsixhundred$ and the design-level choice
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:101:\item The 600-cell instance $\Rsixhundred$ has the construction
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:109:\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:13:the same $\Cph$ on the same $\Rsixhundred$. The architecture
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:116:witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:126:fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:148:$\Rsixhundred$, with no shape retuning between regimes.}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:158:Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:169:operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:24:the projection of $\Cph$ on $\Rsixhundred$ to the flavour-physics
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:35:$\Rsixhundred$, no shape retuning between datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:85:  Laplacian variants on $\Rsixhundred$ (unweighted,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:135:witness for $\Cph$ on $\Rsixhundred$: a single linear response
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:144:that the same fixed $\Cph$ on the same fixed $\Rsixhundred$ is
papers/aria-closure-kernel/paper/sections/05_agreement.tex:6:discrete response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a
papers/aria-closure-kernel/paper/sections/05_agreement.tex:142:$\Rsixhundred$ is the unique discrete substrate with this
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:5:The unweighted graph Laplacian $\Lop = D - A$ on $\Rsixhundred$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:19:\caption{Computed Laplacian spectrum of $\Lop$ on $\Rsixhundred$.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:6:witnesses: $M = \Rsixhundred$, the 600-cell regular 4-polytope
papers/aria-closure-kernel/paper/sections/03_substrate.tex:18:$\Rsixhundred$ has $|V|=120$ unit vectors on the unit $3$-sphere
papers/aria-closure-kernel/paper/sections/03_substrate.tex:46:For two unit vectors $v, w \in \Rsixhundred$ on $S^{3}$, the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:123:\item \textbf{Fixed by the construction once $\Rsixhundred$ is
papers/aria-closure-kernel/paper/sections/03_substrate.tex:132:  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other regular
papers/aria-closure-kernel/paper/sections/02_definition.tex:81:connected finite graph $\Rsixhundred$, or the full-line continuum
papers/aria-closure-kernel/paper/sections/02_definition.tex:92:2.618034$ on $\Rsixhundred$ (\texttt{repro/verify\_kernel.py},
papers/aria-closure-kernel/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
papers/aria-closure-kernel/paper/main.tex:44:the 600-cell instance $\Rsixhundred$ as the discrete substrate
papers/aria-closure-kernel/paper/main.tex:71:claim for $\Rsixhundred$ among regular 4-polytopes, \emph{not} a
papers/aria-closure-kernel/paper/main.tex:82:$\Ph = (1+\sqrt 5)/2$, give the 600-cell graph $\Rsixhundred$ as
papers/aria-closure-kernel/paper/main.tex:92:(\texttt{repro/verify\_kernel.py}) that constructs $\Rsixhundred$
papers/aria-closure-kernel/paper/main.tex:97:on the connected finite graph $\Rsixhundred$ where
papers/aria-closure-kernel/paper/main.tex:119:$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
papers/aria-closure-kernel/paper/main.tex:138:$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
papers/aria-closure-kernel/paper/main.tex:145:$\Rsixhundred$, augmented by a recurrent self-model layer with one
papers/aria-closure-kernel/paper/main.tex:158:not claim $\Rsixhundred$ is the unique substrate consistent with
papers/aria-closure-kernel/paper/sections/01_introduction.tex:36:the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:61:  Once $\Rsixhundred$ is selected and the stability shift
papers/aria-closure-kernel/paper/sections/01_introduction.tex:88:  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:94:  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:108:\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:173:$\Rsixhundred$; uniqueness of the kernel shape on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:184:projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from

exec
/bin/bash -lc "perl -ne 'while(/\\\\label\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex | sort > /tmp/k_labels && perl -ne 'while(/\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex | sort | uniq > /tmp/k_refs && echo 'UNDEFINED REFS:' && comm -13 /tmp/k_labels /tmp/k_refs && echo 'UNUSED LABELS:' && comm -23 /tmp/k_labels /tmp/k_refs" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "perl -ne 'while(/\\\\citep\\{(["'^}]+)'"\\}/g){for "'$k (split /,/, $1){$k =~ s/''^'"\\s+|\\s+"'$//g; print "$k'"\\n\"}}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex | sort | uniq > /tmp/k_cites && perl -ne 'if(/"'^@'"\\w+\\{(["'^,]+)/){print "$1'"\\n\"}' papers/aria-closure-kernel/paper/references.bib | sort > /tmp/k_bib && echo 'UNDEFINED CITES:' && comm -23 /tmp/k_cites /tmp/k_bib && echo 'UNUSED BIB:' && comm -13 /tmp/k_cites /tmp/k_bib" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n '\\\\begin\\{(equation|align|align\\*|table|tabular|itemize|enumerate|center)\\}|\\\\end\\{(equation|align|align\\*|table|tabular|itemize|enumerate|center)\\}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n '\\\\[A-Za-z]+|[{}"'$]'"' papers/aria-closure-kernel/paper/sections/10_conclusion.tex papers/aria-closure-kernel/paper/sections/06_passive_witness.tex papers/aria-closure-kernel/paper/sections/07_active_witness.tex | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 272ms:
papers/aria-closure-kernel/paper/sections/09_limitations.tex:151:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/09_limitations.tex:166:\end{itemize}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:30:\begin{enumerate}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:45:\end{enumerate}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:18:\begin{equation}\label{eq:banomaly_kernel}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:22:\end{equation}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:43:\begin{table}[ht]
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:50:\begin{tabular}{l l r r r r}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:61:\end{tabular}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:62:\end{table}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:66:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:93:\end{itemize}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:100:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:130:\end{itemize}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:19:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:38:\end{itemize}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:53:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:61:\end{itemize}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:65:\begin{enumerate}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:80:\end{enumerate}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:92:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:113:\end{itemize}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:116:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:138:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:15:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:31:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:46:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:54:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:66:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:86:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:90:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:111:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:144:\begin{table}[ht]
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:150:\begin{tabular}{p{0.22\linewidth} p{0.36\linewidth} p{0.36\linewidth}}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:165:\end{tabular}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:166:\end{table}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:16:\begin{table}[ht]
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:24:\begin{tabular}{c c c}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:40:\end{tabular}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:41:\end{table}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:44:\begin{align*}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:49:\end{align*}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:39:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/05_agreement.tex:45:\end{itemize}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:48:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/05_agreement.tex:57:\end{itemize}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:74:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/05_agreement.tex:82:\end{itemize}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:87:\begin{table}[ht]
papers/aria-closure-kernel/paper/sections/05_agreement.tex:96:\begin{tabular}{l c c}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:104:\end{tabular}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:105:\end{table}
papers/aria-closure-kernel/paper/sections/02_definition.tex:16:\begin{equation}\label{eq:cphi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:18:\end{equation}
papers/aria-closure-kernel/paper/sections/02_definition.tex:21:\begin{equation}\label{eq:psi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:23:\end{equation}
papers/aria-closure-kernel/paper/sections/02_definition.tex:30:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/02_definition.tex:42:\end{itemize}
papers/aria-closure-kernel/paper/sections/02_definition.tex:45:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/02_definition.tex:54:\end{itemize}
papers/aria-closure-kernel/paper/sections/02_definition.tex:76:\begin{equation}\label{eq:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:79:\end{equation}
papers/aria-closure-kernel/paper/sections/02_definition.tex:83:\begin{equation}\label{eq:opnorm_zero_mode}
papers/aria-closure-kernel/paper/sections/02_definition.tex:85:\end{equation}
papers/aria-closure-kernel/paper/sections/02_definition.tex:102:\begin{equation}\label{eq:green_continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:104:\end{equation}
papers/aria-closure-kernel/paper/sections/02_definition.tex:118:\begin{enumerate}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/02_definition.tex:127:\end{enumerate}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:22:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/03_substrate.tex:31:\end{itemize}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:53:\begin{equation}\label{eq:short_edge}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:55:\end{equation}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:63:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/03_substrate.tex:75:\end{itemize}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:86:\begin{equation}\label{eq:shell_inner}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:91:\end{equation}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:94:\begin{equation}\label{eq:shell_sizes}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:98:\end{equation}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:122:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/03_substrate.tex:138:\end{itemize}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:18:\begin{equation}\label{eq:cphi_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:21:\end{equation}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:28:\begin{equation}\label{eq:opnorm_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:30:\end{equation}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:59:\begin{enumerate}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/01_introduction.tex:98:\end{enumerate}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:102:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/01_introduction.tex:136:\end{itemize}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:162:\begin{center}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:178:\end{center}

 succeeded in 313ms:
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:2:\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:10:\subsection{What b-anomaly tests}\label{ssec:banomaly_setup}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:12:The Wilson-coefficient Hamiltonian for $b\to s\mu^{+}\mu^{-}$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:13:contains a $C_{9}^{(\prime)}$ contribution that, in the Standard
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:14:Model, is approximately $q^{2}$-independent in the relevant
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:16:$q^{2}$-dependent effective shift on top of the SM backend, of the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:18:\begin{equation}\label{eq:banomaly_kernel}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:19:\Delta C_{9}^{\mathrm{eff}}(q^{2})
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:21:-\,A \cdot \kappa_{V_{600}}(q^{2}),
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:22:\end{equation}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:23:where $\kappa_{V_{600}}(q^{2}) > 0$ on the LHCb $q^{2}$ window is
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:24:the projection of $\Cph$ on $\Rsixhundred$ to the flavour-physics
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:25:$q^{2}$ axis (the b-anomaly preprint's §3 projection construction,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:27:operator, not a derivation of $\Ph^{-2}$), and $A$ is a single
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:29:sign in Eq.~\eqref{eq:banomaly_kernel} reflects the b-anomaly
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:30:preprint's sign convention: a positive fitted $A>0$ produces a
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:31:negative $\Delta C_{9}^{\mathrm{eff}}<0$, the established
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:33:$\kappa_{V_{600}}$ is held fixed across all five datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:34:This is a \emph{structural} test: same fixed $\Cph$ on the same
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:35:$\Rsixhundred$, no shape retuning between datasets.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:37:\subsection{The five-dataset structural fit}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:40:(verbatim from~\citep{SmartBAnomaly2026}, also at
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:41:\texttt{BANOMALY-001/vfd-b-anomaly/README.md}):
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:43:\begin{table}[ht]
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:44:\centering
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:45:\small
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:46:\caption{b-anomaly five-dataset structural fit. Verbatim
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:47:from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:48:dataset, kernel shape held fixed.}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:49:\label{tab:banomaly}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:50:\begin{tabular}{l l r r r r}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:51:\toprule
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:52:Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:53:   Best-fit $A$ & $\Delta C_{9}^{\mathrm{eff}}$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:54:\midrule
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:55:LHCb 2015 & $B^{0}\!\to\!K^{*0}$ & $32$ & $-0.24$ & $+1.24$ & $-0.96$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:56:LHCb 2021 & $B^{+}\!\to\!K^{*+}$ & $32$ & $+0.17$ & $+2.06$ & $-1.59$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:57:CMS 2025 (no $P_{4}'$) & $B^{0}\!\to\!K^{*0}$ & $18$ & $+0.47$ & $+1.05$ & $-0.81$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:58:LHCb 2025 & $B^{0}\!\to\!K^{*0}$ & $32$ & $+1.09$ & $+1.14$ & $-0.86$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:59:LHCb 2015 & $B_{s}\!\to\!\phi$ ($S$-basis) & $24$ & $-0.24$ & $+4.98$ & $-3.85$ \\
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:60:\bottomrule
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:61:\end{tabular}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:62:\end{table}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:64:\subsection{What the structural fit establishes}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:66:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:67:\item \textbf{Universality (5/5).} The same fixed kernel shape
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:68:  can be fit to all five datasets with one amplitude $A$ per
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:71:\item \textbf{Sign uniformity (5/5).} $A > 0$ in $5/5$ fits;
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:72:  $\Delta C_{9}^{\mathrm{eff}} < 0$ in $5/5$ fits. The kernel
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:74:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:76:\item \textbf{Cross-channel ratio.} The $B\to K^{*}$ vs
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:77:  $B_{s}\!\to\!\phi$ amplitudes differ by a factor partly explained
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:78:  by the predicted Krüger--Matias $P$-basis vs $S$-basis
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:79:  amplification ($\sim 2.2$~\citep{KrugerMatias2005}). The
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:81:  $B_{s}\!\to\!\phi$ amplitude; a residual factor of about two
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:84:\item \textbf{Geometry-first variant test.} Of three discrete
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:85:  Laplacian variants on $\Rsixhundred$ (unweighted,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:86:  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:88:  (correlation $0.997$ with the continuum kernel, b-anomaly
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:89:  preprint §3.4) and the LHCb~2025 data $\chi^{2}$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:90:  ($\chi^{2}=13.555$). The two criteria agree on the variant
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:93:\end{itemize}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:95:\subsection{What the structural fit does \emph{not} establish}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:100:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:101:\item \textbf{AIC tie on current data.} On Akaike model comparison,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:102:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:103:  shift ($\mathrm{FREE\_C9}$, also $k=1$) are statistically
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:105:  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:109:\item \textbf{Free-width Gaussian alternative.} A free-width
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111:  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:112:  is not the unique $q^{2}$ shape consistent with the anomaly.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:113:\item \textbf{Mode-B drift (linearised-to-non-linear refit).} An
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:116:  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:117:  the subsequent non-linear refit; the $+2.77$-AIC-unit drift
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:121:\item \textbf{Look-elsewhere on the variant test.} The b-anomaly
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:122:  preprint's limitations section~\citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:124:  only later was the agreement of the data-$\chi^{2}$ ranking with
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:130:\end{itemize}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:132:\subsection{Reading at the operator level}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:134:The b-anomaly result is the \emph{passive-regime} empirical
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:135:witness for $\Cph$ on $\Rsixhundred$: a single linear response
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:136:$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:138:description of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:144:that the same fixed $\Cph$ on the same fixed $\Rsixhundred$ is
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:147:second landing is in \S\ref{sec:active_witness}.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:5:The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:6:600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:8:(H1)--(H3) on the substrate $(M, L_M)$, and on the connected
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:9:finite graph $\Rsixhundred$ where $\lambda_{\min}(L_M) = 0$ it has
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:10:smallest eigenvalue $\Ph^{-2}$ and operator-norm identity
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:11:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$ (general substrates with
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:12:$\lambda_{\min}(L_M) > 0$ give the strict inequality
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:13:$\|\Cph^{-1}\| < \Ph^{2}$).
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:14:The 600-cell instance has $|V|=120$, $|E|=720$, uniform degree
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:15:$12$, $9$-shell partition $\{1,12,20,12,30,12,20,12,1\}$, and a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:17:$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:18:discrete-to-continuum agreement between $\psi = \Cph^{-1} f$ and
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:19:the continuum kernel $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:20:chord distances (non-source vertices) is Pearson $\rho = 0.976$ on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:21:the unweighted Laplacian, above the two $\Ph$-cocycle weighted
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:22:variants tested ($0.888$ geometric, $0.884$ arithmetic). All numbers are reproduced from canonical
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:23:generators by \texttt{repro/verify\_kernel.py}; no parameter is
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:26:\textbf{Two independent empirical landings.} The same fixed
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:27:$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:30:\begin{enumerate}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:31:\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:32:  fitted dimensionless amplitude $A$ per dataset (kernel shape
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:34:  $\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:35:  $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:37:  $B_s\to\phi$).
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:38:\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:41:  $\eta\in\{0,0.05,0.20\}$, one substrate-pinned nonlinearity
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:42:  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:45:\end{enumerate}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:47:operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:48:$\Ph^{-2}$. Above that operator level, they share no fitted
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:55:\textbf{Operator-witness scope.} This is an operator witness, not
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:57:$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:61:alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:62:$w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim, and the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:65:4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:66:open builds (Lyapunov $V(W)$, edge-space decomposition under
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:67:$2I$-equivariance, full reduced-flow convergence) remain open and
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:70:\textbf{Programme position.} The cascade-programme home for the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:71:polynomial-in-$L$ Lyapunov family — RH polynomial filter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:72:($p_{\mathrm{fix}}(L)^{2}$, $\sigma$-fix-annihilator instance), YM
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:73:cascade gap operator, ACT regulariser $R_{\mathrm{hom}}$ — is
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:74:identified in \S\ref{sec:programme_home}. Family-membership is
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:75:\emph{programme-positioned}, not formally classified. The two
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:77:\emph{response} primitive without reducing or addressing the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:2:\section{Active-regime witness: aria-chess}\label{sec:active_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:10:\subsection{What aria-chess tests}\label{ssec:aria_setup}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:13:the same $\Cph$ on the same $\Rsixhundred$. The architecture
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:15:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:16:\item One \emph{condition-dependent} self-injection coupling
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:17:  $\eta \in \{0, 0.05, 0.20\}$ (PROPOFOL, SLEEP\_N3,
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:20:\item One \emph{substrate-pinned} nonlinearity
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:21:  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:22:  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:23:  $k=12$ is not a free hyperparameter; it is the substrate's
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:25:\item Condition-specific \emph{biologically-motivated} stimulus
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:31:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:32:The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:37:\subsection{Eighteen preregistered correspondences}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:41:\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:44:preregistered tally as reported in~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:46:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:47:\item $17/18$ at standard validation methodology ($5$-seed
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:49:\item $18/18$ after a documented $N\!=\!20$ deep-dive on the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:50:  residual high-variance interaction $C\!\times\!P$ (P4: bootstrap
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:51:  point estimate $+0.190$, $95\%$ CI $[+0.143, +0.239]$,
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:52:  $0/2000$ resamples at-or-below zero, reported as $0.0000$).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:53:\item No preregistered threshold has been modified.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:54:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:57:interaction term), \emph{not} as a threshold change. We inherit the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:60:\subsection{Six drug/sleep EEG signatures}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:62:On a single deterministic substrate trajectory at seed~$42$, the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:66:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:67:\item \textbf{Wake cortical-avalanche $\alpha$}: $\alpha = 2.252$,
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:68:  $95\%$ CI $[1.82, 2.86]$, $R^{2}=0.956$ — the WAKE confidence
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:69:  interval overlaps both the Sleep-EDFx EEG CI $[2.50, 2.53]$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:70:  ($n=30$ subjects) and aria-chess's prior cascade pipeline CI
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:71:  $[2.73, 3.25]$ pairwise (the Sleep-EDFx and prior-pipeline
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:74:\item \textbf{NREM-N3 phenomenal-intensity variance ratio}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:75:  $0.463\!\times$ wake (predicted $\sim 0.365$, threshold $<0.70$).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:76:\item \textbf{Propofol modality-switching ratio}: $1.83\!\times$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:77:  wake (threshold $\in [1.5, 5.0]$, empirical reference
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:78:  $2.96\!\times$ from OpenNeuro \texttt{ds005620}).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:79:\item \textbf{Propofol continuity drop}: $+0.066$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:80:  (threshold $> 0.020$).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:81:\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:82:  direction confirmed; $\Phi$-proxy not full IIT).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:83:\item \textbf{Recovery deterministic identity to wake}: under the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:86:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:88:\subsection{Cross-domain selectivity}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:90:\begin{itemize}\itemsep=2pt
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:91:\item \textbf{Chess pattern recognition (P9--P13)}: $32$ chess
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:92:  positions across $4$ categories on $8$-D V2 features; substrate
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:94:  $n=25$ ticks from raw $53.1\%$ to substrate-routed $93.8\%$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:95:  ($+40.6$pp), well above the preregistered $\geq +15$pp floor.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:96:\item \textbf{Conversation pattern recognition (P14--P16)}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:97:  $64$ utterances, $8$ categories; raw classification $87.5\%$,
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:98:  substrate-routed lift $-4.4$pp (within the preregistered
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:99:  neutrality band $|\cdot| < 10$pp). The substrate is selectively
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:103:\item \textbf{HCP brain functional connectivity (P17--P18)}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:104:  full-cohort descriptive statistics on $n=1003$ subjects show
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:105:  ARIA's $H_4$-transitive structure at $-11.58\sigma$ on degree
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:106:  homogeneity, $+79.78\sigma$ on raw participation ratio (with
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:107:  node-count caveat: ARIA $|V|=120$ vs HCP ICA-50 $|V|=50$), and
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:108:  $+6.80\sigma$ on clustering coefficient. ARIA's degree std is
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:109:  $0$ by H$_4$ transitivity (a theorem), $11.58$ standard
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:111:\end{itemize}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:113:\subsection{Reading at the operator level}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:115:The aria-chess result is the \emph{active-regime} empirical
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:116:witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:117:layer above $\Cph$ uses one condition-dependent coupling and one
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:119:$k=12$; no other \emph{kernel-shape} parameter enters. Above the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:124:this paper. The kernel shift $\Ph^{-2}$ is not retuned between
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:126:fixed $\Cph$ on the same $\Rsixhundred$ is consistent with $18/18$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:131:does not claim the substrate \emph{is} consciousness, does not
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:135:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:137:underneath both empirical landings (the b-anomaly $q^{2}$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:138:projection above $\Cph$ and the aria-chess recurrent self-model
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:139:layer above $\Cph$ are distinct above-operator constructions; the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:142:\subsection{Two-witness structure}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:144:\begin{table}[ht]
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:145:\centering
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:146:\small
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:147:\caption{Two independent empirical landings of $\Cph$ on
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:148:$\Rsixhundred$, with no shape retuning between regimes.}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:149:\label{tab:two_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:150:\begin{tabular}{p{0.22\linewidth} p{0.36\linewidth} p{0.36\linewidth}}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:151:\toprule
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:153:\midrule
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:154:Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:156:Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) & prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:157:Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\

 exited 1 in 341ms:
/bin/bash: /tmp/k_labels: Read-only file system
Unable to flush stdout: Broken pipe

 exited 1 in 331ms:
/bin/bash: /tmp/k_cites: Read-only file system
sort: fflush failed: 'standard output': Broken pipe
sort: write error

exec
/bin/bash -lc "comm -13 <(perl -ne 'while(/\\\\label\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex | sort -u) <(perl -ne 'while(/\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex | sort -u) | sed 's/"'^/UNDEFINED REF: /'"'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "comm -23 <(perl -ne 'while(/\\\\label\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex | sort -u) <(perl -ne 'while(/\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex | sort -u) | sed 's/"'^/UNUSED LABEL: /'"'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "comm -23 <(perl -ne 'while(/\\\\citep\\{(["'^}]+)'"\\}/g){for "'$k (split /,/, $1){$k =~ s/''^'"\\s+|\\s+"'$//g; print "$k'"\\n\"}}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex | sort -u) <(perl -ne 'if(/"'^@'"\\w+\\{(["'^,]+)/){print "$1'"\\n\"}' papers/aria-closure-kernel/paper/references.bib | sort -u) | sed 's/"'^/UNDEFINED CITE: /'"'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "comm -13 <(perl -ne 'while(/\\\\citep\\{(["'^}]+)'"\\}/g){for "'$k (split /,/, $1){$k =~ s/''^'"\\s+|\\s+"'$//g; print "$k'"\\n\"}}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex | sort -u) <(perl -ne 'if(/"'^@'"\\w+\\{(["'^,]+)/){print "$1'"\\n\"}' papers/aria-closure-kernel/paper/references.bib | sort -u) | sed 's/"'^/UNUSED BIB: /'"'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 333ms:
UNUSED LABEL: eq:cphi
UNUSED LABEL: eq:cphi_intro
UNUSED LABEL: eq:opnorm_intro
UNUSED LABEL: eq:opnorm_zero_mode
UNUSED LABEL: eq:psi
UNUSED LABEL: eq:shell_sizes
UNUSED LABEL: ssec:aria_setup
UNUSED LABEL: ssec:banomaly_setup
UNUSED LABEL: ssec:hypotheses
UNUSED LABEL: ssec:inner_product_check
UNUSED LABEL: ssec:irrep
UNUSED LABEL: ssec:result_unweighted
UNUSED LABEL: ssec:scope
UNUSED LABEL: ssec:shells
UNUSED LABEL: ssec:test
UNUSED LABEL: ssec:testclaim
UNUSED LABEL: ssec:variant_comparison
UNUSED LABEL: ssec:vertices
UNUSED LABEL: tab:banomaly
UNUSED LABEL: tab:two_witness
UNUSED LABEL: tab:variant_correlation

 succeeded in 345ms:
 succeeded in 398ms:
 succeeded in 411ms:
UNUSED BIB: Weisstein600Cell

codex
The static label/citation pass did not find undefined refs or missing bib keys. I cannot run a LaTeX compile in this read-only sandbox because even `/tmp` is not writable, so the surface check will be static rather than compile-backed.
exec
/bin/bash -lc "rg -n \"looked|historical|blind|variant|geometry|residual|overshoot|2\\.2|Mode-B|Mode B|AIC|Gaussian|0\\.348|0\\.652|\\+2\\.77|13\\.555|0\\.997|0\\.9968|free-width|FREE_C9|Cross-channel|Kruger|Krüger|Matias\" ../BANOMALY-001/vfd-b-anomaly/paper/main.tex ../BANOMALY-001/vfd-b-anomaly/paper/sections/*.tex ../BANOMALY-001/vfd-b-anomaly/README.md" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "wc -l ../BANOMALY-001/vfd-b-anomaly/paper/main.tex ../BANOMALY-001/vfd-b-anomaly/paper/sections/*.tex && rg --files ../BANOMALY-001/vfd-b-anomaly/paper | sed -n '1,80p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"18/18|17/18|P4|P13|\\+40\\.6|LOO|5-fold|single deterministic|seed 42|not part|threshold|selection theorem|unique|Ph\\"'^'"\\{-2\\}|Phi collapse|0\\.33|1\\.83|0\\.463|2\\.252|0\\.190|\\[\\+0\\.143, \\+0\\.239\\]|79\\.78|11\\.58|6\\.80\" papers/aria-chess-paper/paper/main.tex papers/aria-chess-paper/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "jq -r '\"V=\\(.n_vertices) E=\\(.n_edges) deg=\\(.degree_sequence.min)/\\(.degree_sequence.max)/\\(.degree_sequence.mean)\", \"shells=\\([.shell_sizes[\"0\"],.shell_sizes[\"1\"],.shell_sizes[\"2\"],.shell_sizes[\"3\"],.shell_sizes[\"4\"],.shell_sizes[\"5\"],.shell_sizes[\"6\"],.shell_sizes[\"7\"],.shell_sizes[\"8\"]] | @json)\", \"spectrum=\\(.laplacian_spectrum_grouped | map([.eigenvalue,.multiplicity]) | @json)\", \"opnorm=\\(.operator_norm.operator_norm_C_phi_inv) phi2=\\(.operator_norm.predicted_phi_squared)\", \"corrs unweighted pv=\\(.variant_correlation.UNWEIGHTED.per_vertex_correlation) sm=\\(.variant_correlation.UNWEIGHTED.shell_mean_correlation)\", \"corrs geom pv=\\(.variant_correlation.PHI_GEOMETRIC.per_vertex_correlation) arith pv=\\(.variant_correlation.PHI_ARITHMETIC.per_vertex_correlation)\", \"multi=\\(.multi_source_sweep.min_correlation)/\\(.multi_source_sweep.mean_correlation)/\\(.multi_source_sweep.max_correlation) spread=\\(.multi_source_sweep.max_minus_min)\"' papers/aria-closure-kernel/repro/results.json" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 362ms:
../BANOMALY-001/vfd-b-anomaly/README.md:3:**A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit.**
../BANOMALY-001/vfd-b-anomaly/README.md:16:| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
../BANOMALY-001/vfd-b-anomaly/README.md:27:- **Cross-channel ratio.** The $B\to K^{*}$ vs $B_{s}\!\to\!\phi$ amplitudes differ by a factor consistent with the predicted Krüger–Matias $P$-basis vs $S$-basis amplification ($\sim 2.2$), with a residual $\sim 50\%$ overshoot.
../BANOMALY-001/vfd-b-anomaly/README.md:28:- **Geometry-first variant test.** Of three discrete Laplacian variants, the unweighted choice wins on a *pure-geometry* criterion (correlation $0.997$ with the continuum kernel) decided **independently of the LHCb data**. The same variant later wins on the data $\chi^{2}$ — independent geometry and data criteria agree.
../BANOMALY-001/vfd-b-anomaly/README.md:31:- On Akaike model comparison, the kernel and a constant Wilson-coefficient shift $\mathrm{FREE\_C9}$ (also $k=1$) are statistically indistinguishable on current data: stacked Akaike weight $w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$. AIC compares per-parameter goodness-of-fit and is blind to the universality/shape-prediction claim itself.
../BANOMALY-001/vfd-b-anomaly/README.md:32:- A free-width Gaussian charm-loop proxy fits comparably in $\chi^{2}$ at the cost of one extra shape parameter; the kernel is not the unique $q^{2}$ shape consistent with the anomaly.
../BANOMALY-001/vfd-b-anomaly/README.md:33:- An earlier linearised analysis (the project's "Mode B") gave a stronger numerical preference for the kernel ($\Delta\mathrm{AIC}=-1.67$ on LHCb 2025) that **did not survive the non-linear refit**. The $+2.77$-AIC-unit drift is the largest single methodological uncertainty in the project. See §2 and §4 of [the paper](paper/main.pdf) and [`reports/wo016c_nonlinear_refit.md`](reports/wo016c_nonlinear_refit.md). Linearised numbers are retained in the paper as a methodology diagnostic.
../BANOMALY-001/vfd-b-anomaly/README.md:35:The structural test the project was designed to run — *can a fixed geometry-derived shape describe the anomaly across multiple independent datasets without retuning?* — is satisfied. Whether the kernel is statistically *preferred* over a constant shift is a question current data cannot resolve and will require future $b\to s\ell\ell$ measurements.
../BANOMALY-001/vfd-b-anomaly/README.md:48:**F3** Non-linear best-fit amplitudes across the five fits. Green = kernel marginally favoured (LHCb 2015, $B_{s}\!\to\!\phi$); orange = constant shift marginally favoured. Right panel: $S$-basis cross-channel; grey dashed line is the basis-corrected prediction $A_{P}^{\mathrm{LHCb 2025}}\times 2.2 \approx 2.5$.
../BANOMALY-001/vfd-b-anomaly/README.md:82:│   ├── wo016b_variant_geometry.py # variant choice on pure-geometry criterion
../BANOMALY-001/vfd-b-anomaly/README.md:90:│   ├── wo016b_variant_geometry.md     # paper §3 variant-selection table
../BANOMALY-001/vfd-b-anomaly/README.md:141:4. The pure-geometry variant test (`scripts/wo016b_variant_geometry.py`).
../BANOMALY-001/vfd-b-anomaly/README.md:175:| 2 | Datasets, SM backend (non-linear flavio + linearised Mode B), reproducibility ledger |
../BANOMALY-001/vfd-b-anomaly/README.md:176:| 3 | Three-layer kernel construction: continuum $\varphi$-tuned Green's function → bounded Dirichlet eigenmode → discrete 2I-equivariant lift on $V_{600}$. Variant-selection table on pure-geometry vs LHCb-data criteria. |
../BANOMALY-001/vfd-b-anomaly/README.md:178:| 5 | Stress tests on LHCb 2025 under Mode B (bin bootstrap, region splits, alternative Wilson-coefficient models, charm-loop Gaussian, BSZ form-factor MC) |
../BANOMALY-001/vfd-b-anomaly/README.md:180:| 7 | Cross-channel fit on $B_{s}\!\to\!\phi$; basis-effect explanation of the amplitude gap |
../BANOMALY-001/vfd-b-anomaly/README.md:185:The paper went through three rounds of internal hostile review. The major finding from Round 2 was that the linearised fit's $\Delta\mathrm{AIC}=-1.67$ on LHCb 2025 flipped to $+1.09$ under a non-linear refit; the paper was rewritten around that negative finding and accepted as preprint-ready in Round 3.
../BANOMALY-001/vfd-b-anomaly/README.md:207:  title        = {A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit},
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:6:The section is reorganised relative to the Mode-B-era version to put
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:15:  validation, and the cross-channel validation) used a Mode-B
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:21:  residuals reach $4\sigma$ on LHCb 2025, and the headline
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:22:  $\Delta\mathrm{AIC}$ shifts from $-1.67$ (linearised) to $+1.09$
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:25:  evaluation throughout for the headline numbers; Mode-B values are
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:29:\item \textbf{Variant choice is geometry-confirmed but data-discovered.}
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:31:  the best LHCb-data $\chi^{2}$ among the three admissible variants
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:32:  (\S\ref{sec:derivation}, Table~\ref{tab:variant_selection}).
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:33:  We subsequently verified that the same variant wins on a pure
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:34:  geometry criterion (correlation with the Layer-1 continuum kernel,
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:35:  no LHCb data), and we now defend the AIC counting $k=1$ for VFD on
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:36:  this basis. The variant choice therefore does not consume an
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:37:  effective fit parameter, but the historical contingency that the
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:38:  data was looked at first is acknowledged.
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:44:  The Mode-B stress test (\S\ref{sec:stress}) ruled out $C_{10}$ at
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:51:  2I-equivariant graph but is not derived from a first-principles
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:59:  \delta_{1}^{\mathsf T}\delta_{1}$ with 2I-equivariant boundary maps
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:122:  ($\Delta\chi^{2}=1$ Gaussian approximation or non-parametric
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:143:The geometry-derived kernel describes the angular anomaly with one
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:147:on AIC; the stacked Akaike weight is $\approx 1.9{:}1$ in favour of
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:149:\emph{a single geometry-derived $q^{2}$-shape with no fitted shape
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex:152:the stronger ``it beats the constant shift on AIC'' claim of the
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:10:geometry-derived kernel imposes a fixed centre-peaked $q^{2}$ shape
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:14:Under the Mode-B linearised response, the kernel's centre-peaked
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:17:better $\chi^{2}$ ($\Delta\mathrm{AIC}=-1.67$). Under the headline
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:22:$\Delta\mathrm{AIC}=+1.09$. Across five fits the non-linear stacked
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:33:preferred explanation under AIC.
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:44:Empirically the per-bin linearisation residual on LHCb 2025 reaches
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:57:operator $L_{V_{600}} + \varphi^{-2}I$ to the 2I-equivariant cocycle
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:66:Table~\ref{tab:variant_selection}); the unweighted Laplacian wins on
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:67:both the pure-geometry and LHCb-data criteria, with the rankings
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:77:Krüger--Matias $P_{i}$ basis amplifies the per-observable $C_{9}$
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:78:sensitivity by $\langle 1/\sqrt{F_{L}(1-F_{L})}\rangle\approx 2.2$
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:81:is $+4.98$, a factor-of-2 unexplained residual. We do \emph{not}
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:82:characterise this as a clean basis-effect victory: the residual is
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:103:\item \emph{The kernel is the right object.} The 2I-equivariant graph
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:122:The Mode-B stress tests (\S\ref{sec:stress}) rule out specific
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:127:  $A\in[+1.36, +1.85]$ in Mode B.
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:130:  in Mode B, worse than the $+2$ AIC penalty for the extra parameter.
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:133:  $A=+1.57\pm 0.16$, $100\,\%$ positive, in Mode B.
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:140:centre-peaked Gaussian
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:141:($\Delta\mathrm{AIC}=-1.91$ vs FREE\_C9 in Mode B; vs $-1.67$ for
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex:143:parameter. The geometric kernel and the free Gaussian capture the
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:6:$\kappa(q^{2})$ from a finite 2I-equivariant graph (the 600-cell
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:24:  $k=1$). On AIC the kernel and a constant-$\Delta C_{9}$ shift at
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:26:  ($\Delta\mathrm{AIC}=+1.09$, mild preference for the constant
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:29:  collaborations and 3 channels):} $\Delta\mathrm{AIC}\in
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:40:  $\langle 1/\sqrt{F_{L}(1-F_{L})}\rangle\approx 2.2$, with a
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:41:  factor-of-$2$ unexplained residual.
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:43:  $\Delta\mathrm{AIC}$ shifts by $+2.77$ between the linearised and
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:49:  pure-geometry-confirmed discrete variant choice
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:50:  (\S\ref{sec:derivation}, Table~\ref{tab:variant_selection}).
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:57:  any luminosity, any energy) gives $A<0$ on the geometry-derived kernel
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:70:$\Delta\mathrm{AIC}_{\mathrm{VFD\,vs\,FREE\_C9}}\geq 0$ on the LHCb
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:75:listed above are independent of, and unaffected by, this AIC tie.
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:78:This is a structural test of whether a single fixed, geometry-derived
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:85:is consistent with the predicted Krüger--Matias basis-correction
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:86:factor; and the unweighted Laplacian variant is selected by a
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:87:pure-geometry criterion (correlation $0.997$ with the continuum
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex:90:over a constant Wilson-coefficient shift. AIC compares per-parameter
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:2:\section{Cross-channel test: $B_{s}\to\phi\mu\mu$}\label{sec:cross-channel}
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:30:model & $k$ & $\chi^{2}$ & AIC & $\Delta\mathrm{AIC}$ & params \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:39:AIC by $0.24$ unit at equal $k=1$. Both fits give a sign-uniform
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:40:negative $\Delta C_{9}^{\mathrm{eff}}$. Mode-B linearised fit gave
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:41:$\Delta\mathrm{AIC}=-0.08$; values are essentially equivalent at this
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:46:The 500-trial bootstrap on bins (run under Mode B, retained as a
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:49:poorly constrained. Region splits under Mode B give $A=+5.31$ in the
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:101:\paragraph{Krüger--Matias amplification.} The optimised $P_{i}$ basis
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:102:\citep{Kruger2005Pbasis,Descotes2013P5p} is constructed to absorb the
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:135:\;\approx\; A_{P\text{-basis}}\times 2.2,
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:142:A^{\mathrm{Bs}\to\phi}_{S, \text{predicted}} \;\approx\; +1.14 \times 2.2 \;\approx\; +2.5.
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:151:best-fit. We attribute the residual gap to:
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:156:\item the per-bin scaling factor scatter $\pm 20\,\%$ around $2.2$;
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:163:residual that is at least as large as the basis-correction itself;
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:178:VFD AIC competitive with FREE\_C9   & \textsc{observed} (marginal $\Delta\mathrm{AIC}=-0.24$, $w_{\mathrm{VFD}}\approx 0.53$) \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex:186:four $B\to K^{*}$ fits and AIC-degenerate with FREE\_C9; the
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:13:linearised Mode-B response (Eq.~\ref{eq:modeB}). The headline non-linear
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:16:$\Delta\mathrm{AIC}$ of opposite sign vs $\mathrm{FREE\_C9}$ (see
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:17:Table~\ref{tab:joint_fit_modes}). What the Mode-B stress tests
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:21:non-linear $\Delta\mathrm{AIC}$ result. Numbers below are quoted
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:22:under Mode B and should be read accordingly.
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:64:   VFD $A$ & $\Delta\mathrm{AIC}$ \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:81:SM theory is least reliable — is the region where VFD's AIC advantage
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:95:model & $k$ & $\chi^{2}$ & AIC & $\Delta\mathrm{AIC}$ & params \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:100:charm-loop Gaussian            & 2 & 35.41 & 39.41 & $-1.91$ & $A=+1.83$, $\sigma=8.96\,\mathrm{GeV}^{2}$ \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:104:Adding $C_{10}$ does not help. The free centre-peaked Gaussian
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:105:(charm-loop nuisance proxy) achieves a slightly lower AIC than the
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:112:$+2$ AIC penalty for the extra parameter; the data does not want
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:113:$\Delta C_{10}$ at this level. The charm-loop Gaussian — a
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:116:($\Delta\mathrm{AIC}=-1.91$ vs FREE\_C9, vs $-1.67$ for VFD), at the
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:118:for the cost of $1$ AIC unit, $\Delta\mathrm{AIC}_{\mathrm{charm\,vs\,VFD}}=-0.24$:
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:165:test (Mode B) & criterion & result \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:168:                                & \textsc{pass} (Mode B; $99.8\,\%$ positive, CI $\pm 15\,\%$) \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:170:                                & \textsc{pass} (Mode B; 3/3 regions $\Delta\mathrm{AIC}<0$, all $A>0$) \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:172:                                & \textsc{pass} (Mode B; $\Delta\mathrm{AIC}=+1.73$ vs FREE\_C9) \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:173:3b. charm-loop Gaussian         & VFD competitive at same shape level
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:174:                                & \textsc{partial} (Mode B; $\Delta\mathrm{AIC}_{\mathrm{charm\,vs\,VFD}}=-0.24$, charm $k=2$) \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:176:                                & \textsc{pass} (Mode B; $100\,\%$ positive, CI $\pm 15\,\%$) \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:181:the linearised $\Delta\mathrm{AIC}$ values quoted above do not
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:186:multi-observable joint fit, all under the linearised Mode-B response.
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex:188:to the non-linear regime, but Mode-B AIC numbers do not.}
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:53:        $\Delta\mathrm{AIC}$ \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:65:$B_{s}\!\to\!\phi$, both by $\Delta\mathrm{AIC}=-0.24$) and disfavoured
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:67:$\Delta\mathrm{AIC}=+1.09$). $A>0$ in every fit;
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:83:$A_{P}^{\mathrm{LHCb 2025}}\times 2.2 \approx 2.5$;
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:86:non-linear $\Delta\mathrm{AIC}$ marginally favours VFD and orange
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:94:To convert the per-dataset $\Delta\mathrm{AIC}$ values into a single
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:96:dataset, $w_{M,d} = e^{-\Delta\mathrm{AIC}_{M,d}/2} / \sum_{M'}
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:97:e^{-\Delta\mathrm{AIC}_{M',d}/2}$, and stack across datasets under the
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:107:dataset & non-linear $\Delta\mathrm{AIC}$ &
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:117:\textbf{0.652} & \textbf{0.348} & \textbf{FREE\_C9 (mild)} \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:149:basis effect (Krüger--Matias $P_{i}$ vs CP-averaged $S_{i}$).
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:160:\textbf{$\mathrm{VFD\ AIC} \leq \mathrm{FREE\_C9\ AIC}$ on every dataset}
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:161:   & \textbf{\textsc{fail}} (passes on $2/5$; max $\Delta\mathrm{AIC}=+1.09$) \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:163:   & \textbf{\textsc{fail}} ($w_{\mathrm{VFD}} = 0.348$) \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:172:analysis. The two strict AIC-preference gates (top) \textsc{fail}
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:176:preferred model on AIC.}
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:182:Mode-B fit produced $\chi^{2}=169$ over 24 data points — about
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:183:$7\times$ per data point. The residuals are dominated by $P_{4}'$
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:189:the convention mismatch. Both $\Delta\mathrm{AIC}$ values agree
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:190:qualitatively (FREE\_C9 favoured by $\sim 0.5$ AIC unit either way)
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:196:The same geometry-derived kernel, with one fitted amplitude per
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex:202:AIC criterion at equal parameter cost, the kernel does not improve
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:9:result first; the linearised Mode-B numbers are then quoted as a
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:27:Model & $k$ & $\chi^{2}$ & AIC & $\Delta\mathrm{AIC}$ & best fit \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:37:AIC by $1.09$ units, a marginal preference (Akaike weight ratio
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:38:$\approx 1.7$). The geometry-derived kernel produces a comparable
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:51:$\pm 1\sigma$ bands. Both models leave residuals of $\lesssim 2\sigma$
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:58:\subsection{Mode-B linearised fit (diagnostic only)}
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:60:The earlier project iteration used the Mode-B linearised response of
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:71:Model & $k$ & $\chi^{2}$ & AIC & $\Delta\mathrm{AIC}$ & best fit \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:74:FREE\_C9 (Mode B)           & 1 &  39.30 &  41.30 & $0.00$  & $\Delta C_{9}=-1.34$ \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:75:VFD\_GREEN\_600CELL (Mode B)& 1 &  37.63 &  39.63 & $-1.67$ & $A=+1.59$, $\Delta C_{9}^{\mathrm{eff}}=-1.37$ \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:78:\caption{Linearised Mode-B fit on the same data. Under the linear
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:79:model $\mathrm{VFD\_GREEN\_600CELL}$ has lower AIC by $1.67$ units.
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:92:quantity & linearised (Mode B) & non-linear refit & drift \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:96:$\Delta\mathrm{AIC}$ (VFD vs FREE) & $-1.67$ & $+1.09$ & $\mathbf{+2.77}$ \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:99:max per-bin linearisation residual & --  & $4.27\sigma$ & -- \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:100:mean per-bin linearisation residual & -- & $0.71\sigma$ & -- \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:103:\caption{Comparison of the same fit under Mode-B linearisation vs
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:105:$\Delta\mathrm{AIC}$ is $2.77$ units, larger than the Mode-B
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:107:evaluation. Per-bin linearisation residuals reach $4\sigma$,
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:118:single-observable $P_{5}'$ fit under the linearised Mode-B response.
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:124:($\Delta\mathrm{AIC}=-7.00$ vs FREE\_C9), reflecting that $P_{5}'$ is
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:134:Refitting the shared kernel under Mode B after removing one of the
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:142:dropped & $n$ remaining & $A$ (Mode B) & $\Delta C_{9}^{\mathrm{eff}}$ mean & $\chi^{2}$ \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:149:all (reference, Mode B)  & 32 & 1.594 & $-1.367$ & 37.63 \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:153:Mode B (linearised). $A$ varies within $\pm 3\,\%$ across the four
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:169:\item $\mathrm{VFD\_GREEN\_600CELL}\ \mathrm{AIC} \leq \mathrm{FREE\_C9}\ \mathrm{AIC}$:
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:170:  \textsc{fail} (non-linear $\Delta\mathrm{AIC}=+1.09$, marginal in
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex:183:indistinguishable from a constant Wilson-coefficient shift on AIC.
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:3:\usepackage[a4paper, margin=2.5cm]{geometry}
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:14:\title{A geometry-derived response kernel for the\\
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:44:is consistent with the predicted Krüger--Matias basis-correction
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:51:$\Delta\mathrm{AIC}$ values span $[-0.24, +1.09]$ around zero, with
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:53:$w_{\mathrm{FREE\_C9}}=0.65$. AIC compares per-parameter
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:56:geometry-derived shape can describe heterogeneous datasets is
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:57:independent of, and complementary to, the AIC tie. An earlier
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:58:linearised analysis (Mode B, linear in $\Delta C_{9}$ via
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:65:derived from a finite 2I-equivariant graph substrate (the 600-cell
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:76:edge-weighting variants, the unweighted Laplacian is selected by a
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:77:\emph{pure-geometry criterion} (correlation $0.997$ with the continuum
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:104:\noindent\emph{(iii) Cross-channel ratio.}
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:106:fitted amplitudes differ by a factor consistent with the Krüger--Matias
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:107:basis-correction factor $\sim 2.2$, with a residual $\sim 50\,\%$
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:108:overshoot of the basis-corrected prediction that the published
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:111:\noindent\emph{(iv) AIC comparison.}
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:113:$\mathrm{FREE\_C9}$ (also $k=1$), the per-dataset $\Delta\mathrm{AIC}$
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:117:data the two models are statistically indistinguishable on AIC.
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:120:geometry-derived form across heterogeneous datasets — a structural
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:121:claim independent of the AIC tie. AIC measures per-parameter
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:124:unique $q^{2}$ shape consistent with the anomaly: a free-width
../BANOMALY-001/vfd-b-anomaly/paper/main.tex:125:Gaussian charm-loop proxy fits marginally better in $\chi^{2}$ at the
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:8:2I-equivariant graph realisation on the 600-cell $V_{600}$
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:11:kernel; the continuum and bounded variants are reported as theoretical
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:63:$\Delta\mathrm{AIC}\approx -7$ vs $\mathrm{FREE\_C9}$ on $P_{5}'$ alone
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:67:AIC penalty: $c_{3}/c_{1} = 0.18$, well below any $\varphi$-rational
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:70:\subsection{Layer 3 — discrete 2I-equivariant lift on $V_{600}$}\label{subsec:layer3}
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:130:\eqref{eq:kappa_lift} on the LHCb 2025 bin centres is $r=0.997$. The
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:139:\caption{The geometry-derived response kernel $\kappa(q^{2})$
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:143:$e^{-|x|/\varphi}$ from Layer 1, with empirical correlation $r=0.997$
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:151:\paragraph{Cocycle, edge weighting, and variant selection.} The
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:160:for each variant; the shell-mean profile is then compared to the
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:162:on the LHCb bin grid. Two criteria are used: a \emph{pure-geometry}
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:172:variant & $\mathrm{corr}(\overline{\psi}, e^{-|x|/\varphi})$ &
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:176:unweighted Laplacian          & $\mathbf{0.9968}$ & $\mathbf{13.555}$ & $1$ on both \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:182:pure-geometry criterion (correlation with the Layer-1 continuum
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:184:variant choice is consistent with selection on geometric grounds
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:186:Reproducible from \texttt{scripts/wo016b\_variant\_geometry.py}
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:187:(reports/wo016b\_variant\_geometry.csv).}
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:188:\label{tab:variant_selection}
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:192:two-criterion agreement means the variant choice does not consume an
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:193:extra effective fit parameter: the variant choice would have been the
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:194:same if only the geometric criterion had been applied, and the AIC
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:196:throughout this paper. The historical sequence is acknowledged in
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:197:\S\ref{sec:limitations}: the data was looked at first, and only later
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:198:verified to agree with the pure-geometry ranking.
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:215:(Eq.~\ref{eq:Lphi}), and the variant table
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:216:(Table~\ref{tab:variant_selection}). A reader unfamiliar with the
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex:221:with 2I-equivariant boundary maps from the 1200 triangular faces,
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:70:\subsection{Linearised response (Mode B; reported as diagnostic)}
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:87:This `Mode B' analysis is retained for two reasons: (i) it
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:90:(ii) the difference between linearised and non-linear $\Delta\mathrm{AIC}$
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:92:linearisation residual reaches $4.3\sigma$ (mean $0.7\sigma$ across
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:94:$\Delta\mathrm{AIC}$ drifts from $-1.67$ (linearised) to $+1.09$
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:95:(non-linear refit), a $2.77$-AIC-unit shift that flips the sign of
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:115:We use a Gaussian $\chi^{2}$ likelihood
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:125:$\mathrm{AIC}=\chi^{2}+2k$ \citep{Akaike1974} and
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:133:\item $\mathrm{VFD\_GREEN\_600CELL}$ — the geometry-derived kernel of
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:138:\item Charm-loop Gaussian — a free-amplitude, free-width Gaussian
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:150:$\mathrm{xtol}=5\times 10^{-4}$; for Mode B the optimiser is Powell
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex:180:linearised optimiser (Mode B) & \texttt{scipy.minimize} Powell, tol $10^{-7}$ \\
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:34:of a finite 2I-equivariant graph (the 600-cell $V_{600}$, vertices and
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:75:\item On the LHCb 2025 dataset, the geometry-derived kernel and a
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:77:  parameter cost ($k=1$ each), with $\Delta\mathrm{AIC}=+1.09$
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:83:  $B_{s}\!\to\!\phi\mu\mu$ — the non-linear $\Delta\mathrm{AIC}$
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:94:  basis rather than the Krüger--Matias $P_{i}$ basis). After basis
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:95:  correction a residual $\sim 50\,\%$ overshoot remains, attributable
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:102:\item That the kernel beats $\mathrm{FREE\_C9}$ on AIC. It does not,
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:103:  on the headline non-linear analysis. A free-width charm-loop
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:104:  Gaussian also fits comparably (\S\ref{sec:stress}).
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:106:  prefers the kernel because of the geometry, or because the
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:107:  geometry reproduces a centre-peaked shape, is not decided here.
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:114:The surviving structural claim is: \emph{one geometry-derived
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex:116:amplitude per dataset is consistent (sign-uniform; AIC-degenerate

 succeeded in 401ms:
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:7:preregistered prediction was P4: $C\times P$ interaction
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:9:$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:12:threshold required (a) re-evaluating the $N\!=\!3$ point estimate as
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:45:$\mathbf{20}$ & $\mathbf{32000\text{--}32019}$ & $\mathbf{+0.190}$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:46:       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:53:($+0.088, +0.190$). Per-seed std at $N\!=\!10$ was $0.159$; at
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:97:\item bootstrap mean $\Delta_{CP} = +0.190$;
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:98:\item 95\% bootstrap CI $[+0.143, +0.239]$;
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:113:threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:144:\item It does not establish that the substrate is uniquely selected by
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:159:P4 ($C\times P$) required $N\!=\!20$ fresh seeds for reliable detection
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:160:at the preregistered threshold; P3 ($D\times C$) closed at $N\!=\!5$.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:163:higher $N$ without threshold modification. The general lesson: when
papers/aria-chess-paper/paper/sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
papers/aria-chess-paper/paper/sections/08_discussion.tex:22:  $\Cph = \Lop + \Ph^{-2} I$ are fixed by the construction (no
papers/aria-chess-paper/paper/sections/08_discussion.tex:26:  literature-derived thresholds on a single deterministic substrate.
papers/aria-chess-paper/paper/sections/08_discussion.tex:34:  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
papers/aria-chess-paper/paper/sections/08_discussion.tex:39:\item \textbf{The 18/18 preregistered correspondences with no
papers/aria-chess-paper/paper/sections/08_discussion.tex:40:  threshold modification.} Every prediction in the preregistered set
papers/aria-chess-paper/paper/sections/08_discussion.tex:41:  passes at the preregistered thresholds. The two interaction tests
papers/aria-chess-paper/paper/sections/08_discussion.tex:42:  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
papers/aria-chess-paper/paper/sections/08_discussion.tex:43:  one test (P13) required the documented state-reset protocol. We
papers/aria-chess-paper/paper/sections/08_discussion.tex:45:  threshold change.
papers/aria-chess-paper/paper/sections/08_discussion.tex:51:IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
papers/aria-chess-paper/paper/sections/08_discussion.tex:101:witness claims (six signatures, $18/18$, chess $+40.6$pp,
papers/aria-chess-paper/paper/sections/08_discussion.tex:153:  matrix specifically, P4 ($C\!\times\!P$) required $N\!=\!20$ for
papers/aria-chess-paper/paper/sections/08_discussion.tex:154:  reliable detection at the preregistered threshold. The general
papers/aria-chess-paper/paper/sections/10_conclusion.tex:7:$\Cph = \Lop + \Ph^{-2} I$ ($\Ph=(1+\sqrt 5)/2$), is a
papers/aria-chess-paper/paper/sections/10_conclusion.tex:20:\textbf{Headline tally.} On a single deterministic trajectory, six
papers/aria-chess-paper/paper/sections/10_conclusion.tex:22:thresholds (Sleep-EDFx CI, OpenNeuro \texttt{ds005620}, Brodbeck 2012,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:24:$0.463\!\times$ wake; propofol modality-switching $1.83\!\times$ wake;
papers/aria-chess-paper/paper/sections/10_conclusion.tex:26:$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/10_conclusion.tex:28:protocol; wake cortical-avalanche power law $\alpha\!=\!2.252$,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:36:preregistered thresholds, with two interaction tests requiring
papers/aria-chess-paper/paper/sections/10_conclusion.tex:40:preregistered threshold has been modified. The original 2026-04-20
papers/aria-chess-paper/paper/sections/10_conclusion.tex:42:failure; the closure of the three gaps (P3, P4, P13) is documented
papers/aria-chess-paper/paper/sections/10_conclusion.tex:49:strong synergy: their interaction $\Delta_{CP}\!=\!+0.190$ at
papers/aria-chess-paper/paper/sections/10_conclusion.tex:50:$N\!=\!20$ ($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples
papers/aria-chess-paper/paper/sections/10_conclusion.tex:61:classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
papers/aria-chess-paper/paper/sections/10_conclusion.tex:63:$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
papers/aria-chess-paper/paper/sections/10_conclusion.tex:64:$5$-fold CV — the LOO finding above is a disclosed estimator/protocol
papers/aria-chess-paper/paper/sections/10_conclusion.tex:65:refinement at the same threshold), while
papers/aria-chess-paper/paper/sections/10_conclusion.tex:67:(threshold $|\cdot|\!<\!10$pp) — and as an H$_4$-transitive
papers/aria-chess-paper/paper/sections/10_conclusion.tex:71:structure is at $-11.58\sigma$ on degree homogeneity,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:72:$+79.78\sigma$ on participation ratio (with the node-count caveat of
papers/aria-chess-paper/paper/sections/10_conclusion.tex:73:\S\ref{ssec:hcp}), and $+6.80\sigma$ on clustering coefficient.
papers/aria-chess-paper/paper/sections/10_conclusion.tex:76:derivation of consciousness, not a selection theorem on the
papers/aria-chess-paper/paper/sections/10_conclusion.tex:79:uniqueness claim for the 600-cell among regular 4-polytopes. The
papers/aria-chess-paper/paper/sections/09_limitations.tex:19:\emph{Disclosure:} substrate-witness scope, no uniqueness claim
papers/aria-chess-paper/paper/sections/09_limitations.tex:23:battery and the eighteen preregistered tests, with thresholds
papers/aria-chess-paper/paper/sections/09_limitations.tex:28:a single deterministic trajectory at seed $42$. Empirical CIs across
papers/aria-chess-paper/paper/sections/09_limitations.tex:64:derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
papers/aria-chess-paper/paper/sections/09_limitations.tex:76:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
papers/aria-chess-paper/paper/sections/09_limitations.tex:81:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
papers/aria-chess-paper/paper/sections/09_limitations.tex:82:$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
papers/aria-chess-paper/paper/sections/09_limitations.tex:90:derive the $\Ph^{-2}$ shift as the unique stability clamp under a
papers/aria-chess-paper/paper/sections/09_limitations.tex:100:\emph{Evidence:} six signatures vs published thresholds.
papers/aria-chess-paper/paper/sections/09_limitations.tex:107:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
papers/aria-chess-paper/paper/sections/09_limitations.tex:122:than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
papers/aria-chess-paper/paper/sections/09_limitations.tex:125:not a threshold change. \emph{Disclosure:}
papers/aria-chess-paper/paper/sections/09_limitations.tex:134:threshold modification.} The reversals (P3, P4, P13) are documented
papers/aria-chess-paper/paper/sections/09_limitations.tex:141:builds for P3/P4/P13 above; no further claim is needed.
papers/aria-chess-paper/paper/sections/09_limitations.tex:181:  permutations; threshold $\geq 50\%$ unchanged; result $65.4\%$
papers/aria-chess-paper/paper/sections/09_limitations.tex:191:refinement and without modifying any preregistered threshold. We do
papers/aria-chess-paper/paper/sections/09_limitations.tex:193:selection theorem on the ACT bridge. We do not claim uniqueness for
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:16:\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:27:or leave-one-out (LOO).
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:65:P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:69:\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:80:(\texttt{run\_preregistered\_validation.py}; the $\geq 50\%$ threshold
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:82:a threshold change; the observed $65.4\%$ at $15$ perms sits well
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:87:$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:88:substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:89:The 2026-04-29 validation tightened the estimator to LOO with state
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:90:reset; we report the LOO finding ($+40.6$pp) above as a disclosed
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:91:estimator/protocol refinement at the unchanged $+15$pp threshold,
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:97:This is a $+40.6$pp lift on the LOO refinement; on the preregistered
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:100:The original 2026-04-20 validation reported the LOO lift at
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:115:unique; it is a description of the observed accuracy stack.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:132:P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:145:$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:161:connectivity matrix; thresholded at the same density as ARIA's
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:179:Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:180:Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:181:Clustering coefficient (descriptive)$^{\flat}$ & $0.455$ & $0.220$ & $+6.80\sigma$ \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:188:\texttt{CROSS\_DOMAIN\_RESULTS.md}; the $+6.80\sigma$ value is sourced
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:191:$\approx 0.235/6.80\!\approx\!0.035$. We carry the $\sigma$-distance
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:207:fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:208:homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:210:density-matched threshold $\rho = 0.101$; cross-parcellation
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:221:across-subject distribution, but the $+79.78\sigma$ value reflects
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:256:Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:257:Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:258:Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (substrate vs null) \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:267:$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
papers/aria-chess-paper/paper/sections/05_results.tex:10:$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
papers/aria-chess-paper/paper/sections/05_results.tex:19:$k_{\mathrm{thr}}=12$, single deterministic substrate
papers/aria-chess-paper/paper/sections/05_results.tex:28:seed 42).}
papers/aria-chess-paper/paper/sections/05_results.tex:34:WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:37:RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:53:   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:56:   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:62:   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:69:   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
papers/aria-chess-paper/paper/sections/05_results.tex:75:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/sections/05_results.tex:77:are not part of the dated 2026-04-18 P1--P18 preregistration; their
papers/aria-chess-paper/paper/sections/05_results.tex:78:thresholds are drawn from the literature (Sleep-EDFx CI for
papers/aria-chess-paper/paper/sections/05_results.tex:92:\textbf{Tally.} $17/18$ at standard validation
papers/aria-chess-paper/paper/sections/05_results.tex:94:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
papers/aria-chess-paper/paper/sections/05_results.tex:95:on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
papers/aria-chess-paper/paper/sections/05_results.tex:96:$32000$--$32019$). \emph{No preregistered threshold has been modified.}
papers/aria-chess-paper/paper/sections/05_results.tex:110:\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
papers/aria-chess-paper/paper/sections/05_results.tex:111:   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:116:P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:120:\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:121:P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:130:\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
papers/aria-chess-paper/paper/sections/05_results.tex:131:estimator as $5$-fold CV at threshold $\geq +15$pp; the 2026-04-29
papers/aria-chess-paper/paper/sections/05_results.tex:132:validation tightened the estimator to LOO with state reset, a
papers/aria-chess-paper/paper/sections/05_results.tex:133:disclosed estimator/protocol refinement at the unchanged $+15$pp threshold. See
papers/aria-chess-paper/paper/sections/05_results.tex:137:methodology refinement (no threshold change).}
papers/aria-chess-paper/paper/sections/05_results.tex:143:\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
papers/aria-chess-paper/paper/sections/05_results.tex:145:  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
papers/aria-chess-paper/paper/sections/05_results.tex:146:  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
papers/aria-chess-paper/paper/sections/05_results.tex:147:\item P13 (chess substrate lift): the 2026-04-18 preregistration
papers/aria-chess-paper/paper/sections/05_results.tex:149:  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
papers/aria-chess-paper/paper/sections/05_results.tex:150:  validation strengthened the estimator to LOO with state reset, a
papers/aria-chess-paper/paper/sections/05_results.tex:151:  disclosed estimator/protocol refinement at the same threshold; the LOO lift was $+3.1$pp
papers/aria-chess-paper/paper/sections/05_results.tex:152:  without state reset on a state-drifted substrate, and $+40.6$pp
papers/aria-chess-paper/paper/sections/05_results.tex:160:all pass at preregistered thresholds, with two interaction tests
papers/aria-chess-paper/paper/sections/05_results.tex:184:\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
papers/aria-chess-paper/paper/sections/05_results.tex:202:(\S\ref{ssec:graph}); the $\Ph^{-2}$ shift in $\Cph$ is a
papers/aria-chess-paper/paper/sections/05_results.tex:207:(noting that the v4 WAKE CI is from a single deterministic trajectory
papers/aria-chess-paper/paper/sections/02_method.tex:7:the validation script, the seed range, the threshold, and the
papers/aria-chess-paper/paper/sections/02_method.tex:17:falsifiable threshold, (iii) the validation test (script + seed range),
papers/aria-chess-paper/paper/sections/02_method.tex:24:not include those batteries in the headline 18/18 tally.} They are
papers/aria-chess-paper/paper/sections/02_method.tex:29:biological signatures with literature-derived thresholds (NREM-N3
papers/aria-chess-paper/paper/sections/02_method.tex:32:cascade-$\alpha$). They are not part of the P1--P18 preregistration;
papers/aria-chess-paper/paper/sections/02_method.tex:36:\textbf{No threshold has been modified post-hoc.} Where the original
papers/aria-chess-paper/paper/sections/02_method.tex:37:2026-04-20 validation reported failures (P3, P4, P13), the documented
papers/aria-chess-paper/paper/sections/02_method.tex:41:(P4, C$\times$P), and
papers/aria-chess-paper/paper/sections/02_method.tex:43:measurements for the chess LOO test (P13). None of these touched a
papers/aria-chess-paper/paper/sections/02_method.tex:44:preregistered threshold.
papers/aria-chess-paper/paper/sections/02_method.tex:50:\text{threshold}, \text{result})$.
papers/aria-chess-paper/paper/sections/02_method.tex:64:\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:69:P9 (chess 5-fold) & same & 30200--30204 & 32 positions, 4 cat. & $\geq 70\%$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:73:\textbf{P13 (chess sub.\ lift)} & same & with reset & same (LOO refinement) & $\geq +15$pp \\
papers/aria-chess-paper/paper/sections/02_method.tex:74:P14 (conv 5-fold) & same & 30220--30224 & 64 utt., 8 cat. & $\geq 75\%$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:80:Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
papers/aria-chess-paper/paper/sections/02_method.tex:173:LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
papers/aria-chess-paper/paper/sections/02_method.tex:174:substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
papers/aria-chess-paper/paper/sections/02_method.tex:201:verdicts (CI overlaps, $P$-value thresholds) are unaffected.
papers/aria-chess-paper/paper/sections/03_substrate.tex:8:operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
papers/aria-chess-paper/paper/sections/03_substrate.tex:89:\Cph \;=\; \Lop + \Ph^{-2} I,
papers/aria-chess-paper/paper/sections/03_substrate.tex:93:The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
papers/aria-chess-paper/paper/sections/03_substrate.tex:95:$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
papers/aria-chess-paper/paper/sections/03_substrate.tex:114:The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
papers/aria-chess-paper/paper/sections/03_substrate.tex:116:average degree, not a fitted threshold. No other shape parameter
papers/aria-chess-paper/paper/sections/03_substrate.tex:165:\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:181:(above threshold but not yet crossed) emit pressure at $30\%$ scale,
papers/aria-chess-paper/paper/sections/01_introduction.tex:27:operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
papers/aria-chess-paper/paper/sections/01_introduction.tex:50:  $\Cph = \Lop + \Ph^{-2} I$ is fully fixed once the graph is
papers/aria-chess-paper/paper/sections/01_introduction.tex:51:  constructed and the stability shift $\Ph^{-2}$ is chosen as a
papers/aria-chess-paper/paper/sections/01_introduction.tex:54:  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
papers/aria-chess-paper/paper/sections/01_introduction.tex:58:\item \textbf{Six drug/sleep signatures.} On a single deterministic
papers/aria-chess-paper/paper/sections/01_introduction.tex:60:  collapse to $0.463\!\times$ wake; propofol modality-switching
papers/aria-chess-paper/paper/sections/01_introduction.tex:61:  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
papers/aria-chess-paper/paper/sections/01_introduction.tex:62:  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/01_introduction.tex:66:  $17/18$ at standard methodology; $18/18$ after a documented
papers/aria-chess-paper/paper/sections/01_introduction.tex:68:  test; \emph{no preregistered threshold has been modified}.
papers/aria-chess-paper/paper/sections/01_introduction.tex:71:  (chess $+40.6$pp leave-one-out lift at depth $n\!=\!25$ ticks;
papers/aria-chess-paper/paper/sections/01_introduction.tex:75:  $n\!=\!1003$: ARIA at $-11.58\sigma$ on degree homogeneity;
papers/aria-chess-paper/paper/sections/01_introduction.tex:76:  $+79.78\sigma$ on raw participation ratio with the node-count caveat
papers/aria-chess-paper/paper/sections/01_introduction.tex:83:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
papers/aria-chess-paper/paper/sections/01_introduction.tex:84:  the unique substrate consistent with these signatures. Other regular
papers/aria-chess-paper/paper/sections/01_introduction.tex:93:\item \emph{Not a selection theorem.} The companion adaptive-closure-
papers/aria-chess-paper/paper/sections/01_introduction.tex:107:\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
papers/aria-chess-paper/paper/sections/01_introduction.tex:108:  Laplacian floor $\Ph^{-2} \approx 0.382$ is a design-level
papers/aria-chess-paper/paper/sections/01_introduction.tex:125:\;=\;\{\text{`consistent with', `inside threshold', `direction confirmed'}\}.
papers/aria-chess-paper/paper/sections/01_introduction.tex:128:A result that lands inside its preregistered threshold licenses a
papers/aria-chess-paper/paper/sections/01_introduction.tex:130:threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
papers/aria-chess-paper/paper/sections/01_introduction.tex:133:(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
papers/aria-chess-paper/paper/sections/01_introduction.tex:146:\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
papers/aria-chess-paper/paper/sections/01_introduction.tex:147:selection theorem on the 4-tuple bridge; circuit-level mechanistic
papers/aria-chess-paper/paper/sections/01_introduction.tex:148:identification; first-principles derivation of $\Ph^{-2}$ shift;
papers/aria-chess-paper/paper/sections/01_introduction.tex:156:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
papers/aria-chess-paper/paper/sections/01_introduction.tex:158:$\Ph^{-2}$ shift disclosed as a design-level stability clamp.
papers/aria-chess-paper/paper/sections/01_introduction.tex:168:ACT bridge (without claiming a selection theorem).
papers/aria-chess-paper/paper/main.tex:43:and through the response-operator stability shift $\Ph^{-2}$. The
papers/aria-chess-paper/paper/main.tex:47:response $\Cph = \Lop + \Ph^{-2} I$ and a small dynamical layer above
papers/aria-chess-paper/paper/main.tex:48:it, this single deterministic structure is consistent with eighteen
papers/aria-chess-paper/paper/main.tex:52:literature-derived thresholds on a single deterministic substrate
papers/aria-chess-paper/paper/main.tex:66:selection theorem, nor a uniqueness claim for the 600-cell among regular
papers/aria-chess-paper/paper/main.tex:76:shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
papers/aria-chess-paper/paper/main.tex:80:before any validation run; each has a falsifiable threshold. The
papers/aria-chess-paper/paper/main.tex:81:preregistered tally is $17/18$ at standard validation methodology
papers/aria-chess-paper/paper/main.tex:82:($5$-seed cascade block plus state-reset protocol), and $18/18$ after
papers/aria-chess-paper/paper/main.tex:84:interaction (P4); no preregistered threshold has been modified. We
papers/aria-chess-paper/paper/main.tex:86:self-model layer above the substrate, on a single deterministic
papers/aria-chess-paper/paper/main.tex:87:trajectory at seed~$42$. The six signatures are not part of the
papers/aria-chess-paper/paper/main.tex:88:P1--P18 preregistration; they are tested against thresholds drawn
papers/aria-chess-paper/paper/main.tex:97:Wake cascade-event power-law exponent $\alpha = 2.252$,
papers/aria-chess-paper/paper/main.tex:105:NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
papers/aria-chess-paper/paper/main.tex:106:(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
papers/aria-chess-paper/paper/main.tex:107:ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
papers/aria-chess-paper/paper/main.tex:109:propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
papers/aria-chess-paper/paper/main.tex:110:integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
papers/aria-chess-paper/paper/main.tex:112:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/main.tex:113:on the single deterministic substrate trajectory.
papers/aria-chess-paper/paper/main.tex:121:bootstrap point estimate of $+0.190$ with $95\%$ CI $[+0.143, +0.239]$
papers/aria-chess-paper/paper/main.tex:122:(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
papers/aria-chess-paper/paper/main.tex:125:estimate at $N\!=\!3$. In this cascade matrix, P4 required $N\!=\!20$;
papers/aria-chess-paper/paper/main.tex:132:8-dimensional V2 features lifts $+40.6$ percentage points on
papers/aria-chess-paper/paper/main.tex:135:preregistered estimator P13 was $5$-fold CV with threshold
papers/aria-chess-paper/paper/main.tex:136:$\geq\!+15$pp, the LOO finding above is a disclosed estimator/protocol
papers/aria-chess-paper/paper/main.tex:137:refinement at the same threshold), while conversation utterance
papers/aria-chess-paper/paper/main.tex:139:(threshold $|\cdot| < 10$pp), consistent with the substrate
papers/aria-chess-paper/paper/main.tex:146:$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
papers/aria-chess-paper/paper/main.tex:147:on degree homogeneity, $+79.78\sigma$ on raw participation ratio
papers/aria-chess-paper/paper/main.tex:150:both architectural and node-count differences), and $+6.80\sigma$ on
papers/aria-chess-paper/paper/main.tex:155:We do not claim the 600-cell is the unique substrate consistent with
papers/aria-chess-paper/paper/main.tex:157:have been ruled out. We do not derive the $\Ph^{-2}$ floor from
papers/aria-chess-paper/paper/main.tex:160:is reported on a single deterministic trajectory; cross-seed CIs on
papers/aria-chess-paper/paper/main.tex:167:without modifying any preregistered threshold.}

 succeeded in 494ms:
  173 ../BANOMALY-001/vfd-b-anomaly/paper/main.tex
  119 ../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex
  191 ../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex
  232 ../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex
  188 ../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex
  190 ../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex
  208 ../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex
  208 ../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex
  145 ../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex
  153 ../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex
  119 ../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex
 1926 total
../BANOMALY-001/vfd-b-anomaly/paper/main.pdf
../BANOMALY-001/vfd-b-anomaly/paper/references.bib
../BANOMALY-001/vfd-b-anomaly/paper/README.md
../BANOMALY-001/vfd-b-anomaly/paper/main.tex
../BANOMALY-001/vfd-b-anomaly/paper/figures/fig_F2_bin_pulls.pdf
../BANOMALY-001/vfd-b-anomaly/paper/figures/fig_F1_kernel_shape.png
../BANOMALY-001/vfd-b-anomaly/paper/figures/fig_F1_kernel_shape.pdf
../BANOMALY-001/vfd-b-anomaly/paper/figures/fig_F3_cross_dataset_A.pdf
../BANOMALY-001/vfd-b-anomaly/paper/figures/fig_F2_bin_pulls.png
../BANOMALY-001/vfd-b-anomaly/paper/figures/fig_F3_cross_dataset_A.png
../BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex
../BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex
../BANOMALY-001/vfd-b-anomaly/paper/sections/03_derivation.tex
../BANOMALY-001/vfd-b-anomaly/paper/sections/02_method.tex
../BANOMALY-001/vfd-b-anomaly/paper/sections/01_introduction.tex
../BANOMALY-001/vfd-b-anomaly/paper/sections/08_discussion.tex
../BANOMALY-001/vfd-b-anomaly/paper/sections/07_cross_channel.tex
../BANOMALY-001/vfd-b-anomaly/paper/sections/06_cross_dataset.tex
../BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex
../BANOMALY-001/vfd-b-anomaly/paper/sections/10_conclusion.tex

 exited 127 in 520ms:
/bin/bash: jq: command not found

exec
/bin/bash -lc "perl -0777 -ne 'while(/\\\\citep\\{(["'^}]+)'"\\}/g){for "'$k (split /,/, $1){$k =~ s/''^'"\\s+|\\s+"'$//g; print "$k'"\\n\"}}' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex | sort -u" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "perl -ne 'if(/"'^@'"\\w+\\{(["'^,]+)/){print "$1'"\\n\"}' papers/aria-closure-kernel/paper/references.bib | sort -u" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n '\\\\(section|subsection|subsubsection)\\{["'^}]*'"\\"'$|'"\\\\(section|subsection|subsubsection)\\{["'^}]*H'"\\"'$_|'"\\\\(section|subsection|subsubsection)\\{["'^}]*'"\\\\Cph|\\\\title\\{' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n '[—–φẑü≈≤≥×σκψηΦΔα]' papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex papers/aria-closure-kernel/paper/references.bib" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 199ms:
CoxeterRegularPolytopes
KrugerMatias2005
LHCbAngular2020
SmartAdaptiveClosureTransport2026
SmartAriaChess2026
SmartBAnomaly2026
Weisstein600Cell

 succeeded in 251ms:
CoxeterRegularPolytopes
KrugerMatias2005
LHCbAngular2020
SmartAdaptiveClosureTransport2026
SmartAriaChess2026
SmartBAnomaly2026
Weisstein600Cell

 succeeded in 235ms:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:12:\subsection{Programme home: polynomial-in-$L$ Lyapunov family}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:65:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:83:\subsection{H$_4$ irrep block decomposition (imported context)}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:80:\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
papers/aria-closure-kernel/paper/sections/02_definition.tex:25:\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}
papers/aria-closure-kernel/paper/sections/02_definition.tex:115:\subsection{Disclosure: $\Ph^{-2}$ is a design-level shift}
papers/aria-closure-kernel/paper/main.tex:19:\title{The closure-response operator

 succeeded in 227ms:
papers/aria-closure-kernel/paper/sections/09_limitations.tex:152:\item Lyapunov function $V(W)$ on the reduced flow — open build
papers/aria-closure-kernel/paper/sections/09_limitations.tex:154:\item $2I$-equivariance audit of the closure operator family —
papers/aria-closure-kernel/paper/sections/09_limitations.tex:157:  Hodge edge Laplacian — open build of ACT.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:159:  regular 4-polytopes — see \S\ref{ssec:regime}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:161:  specified large-graph limit — see \S\ref{ssec:interpretation}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:162:\item First-principles derivation of the $\Ph^{-2}$ shift — see
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:71:polynomial-in-$L$ Lyapunov family — RH polynomial filter
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:73:cascade gap operator, ACT regulariser $R_{\mathrm{hom}}$ — is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:75:  on $W$-trajectories — \emph{none delivered} in that paper.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:131:  convergence — all explicitly not delivered
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:68:  $95\%$ CI $[1.82, 2.86]$, $R^{2}=0.956$ — the WAKE confidence
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:135:observation that the same fixed $\Cph$ — under no shape-parameter
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:136:retuning between regimes — is the shared response primitive
papers/aria-closure-kernel/paper/sections/05_agreement.tex:59:$\psi$ is shell-constant up to numerical precision — the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:114:b-anomaly numbers). Two independent criteria — geometry-only
papers/aria-closure-kernel/paper/sections/05_agreement.tex:115:correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
papers/aria-closure-kernel/paper/sections/05_agreement.tex:137:empirical landing — the b-anomaly paper documents a free-width
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:78:  by the predicted Krüger--Matias $P$-basis vs $S$-basis
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:91:  ranking — a two-criterion convergence on the same fixed
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:78:(predicted) — match to six decimal places. The largest eigenvalue
papers/aria-closure-kernel/paper/sections/02_definition.tex:55:Substrates outside this class — projected coordinates with
papers/aria-closure-kernel/paper/sections/02_definition.tex:57:is unbounded, or operators with negative spectrum — require their
papers/aria-closure-kernel/paper/sections/02_definition.tex:105:The decay scale is $\Ph$ — the same constant that appears in the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:49:alone — no external data input.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:127:  fills the response slot. Selection — Lyapunov $V(W)$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:129:  full reduced-flow convergence — is left open in that paper and

codex
**1. Claim Audit**
References are repo-relative unless noted.

- “operator-norm bound `\|\Cph^{-1}\| = \Ph^{2}`” (`main.tex:51`, `02_definition.tex:72-93`, `04_spectrum.tex:65-78`): established for the connected 600-cell graph and any case with spectral bottom `0`. The paper correctly weakens this to `< \Ph^2` when `\lambda_{\min}(L_M)>0` (`02_definition.tex:86-89`).
- “continuum Green’s function `G(x)=(\Ph/2)e^{-|x|/\Ph}`” (`02_definition.tex:96-108`): correct for `-d^2/dx^2+\Ph^{-2}` on `R`. The paper does not overstate this as a continuum-limit theorem.
- “600-cell graph facts: `|V|=120`, `|E|=720`, degree 12, shells `{1,12,20,12,30,12,20,12,1}`” (`03_substrate.tex:18-37`, `03_substrate.tex:61-78`, `03_substrate.tex:80-107`): established numerically and classically cited.
- “Laplacian spectrum has nine eigenvalue classes in `Z[\Ph]`” (`04_spectrum.tex:5-14`, `04_spectrum.tex:28-38`): numerics support the values and multiplicities. The closed forms are explicitly “recognition,” not an exact derivation, which is the right scope.
- “per-vertex Pearson correlation `0.976`; shell-mean `0.923`; weighted variants `0.888`, `0.884`” (`05_agreement.tex:136-145`, `05_agreement.tex:187-204`): established by `results.json`. The paper correctly says “among the three tested variants,” not uniqueness.
- “b-anomaly five-dataset structural fit” (`06_passive_witness.tex:37-62`): table matches `../BANOMALY-001/vfd-b-anomaly/README.md:16-22`.
- “AIC tie / Gaussian alternative / Mode-B drift” (`06_passive_witness.tex:101-120`): matches README caveats at `README.md:31-33`.
- “cross-channel ratio … residual factor about two remains” (`06_passive_witness.tex:76-83`): supported by b-anomaly paper (`sections/08_discussion.tex:77-82`, `sections/10_conclusion.tex:40-41`), but not worded like the README’s “residual ~50% overshoot” (`README.md:27`). Harmonise the wording.
- “aria-chess `17/18` standard, `18/18` after `N=20` P4 deep-dive” (`main.tex:149-152`, `07_active_witness.tex:47-53`): matches aria-chess (`main.tex:81-84`, `sections/05_results.tex:92-96`). However, later shorthand “`18/18` preregistered” is too compressed (`07_active_witness.tex:126`, `07_active_witness.tex:160`, `10_conclusion.tex:43-44`).
- “chess lift `+40.6`pp” (`07_active_witness.tex:91-95`): number matches aria-chess, but the kernel summary omits that this is a disclosed LOO/state-reset refinement of a preregistered 5-fold-CV estimator (`aria-chess sections/07_cross_domain.tex:87-91`).
- “programme home: polynomial-in-`L` Lyapunov family” (`08_programme_home.tex:12-44`): safely marked programme-positioned, not classified. But the RH/YM bullets contain theorem-like detail about forthcoming artifacts (`08_programme_home.tex:20-31`) not established here; make them less specific or cite the exact source.

**2. Internal Consistency**
- Abstract/headline numbers are consistent with §5 and `results.json`: per-vertex `0.976`, weighted `0.888/0.884`, norm `2.618`, graph facts.
- Main scope discipline is strong: no derivation of `\Ph^{-2}`, no 600-cell uniqueness, no kernel uniqueness, no ACT theorem (`main.tex:65-77`, `main.tex:155-168`).
- Main inconsistency: active-witness shorthand. Some places preserve “17/18 standard, 18/18 after deep-dive” (`main.tex:149-152`), while others say only “18/18” (`01_introduction.tex:156`, `01_introduction.tex:169-170`, `07_active_witness.tex:126`, `10_conclusion.tex:43-44`).
- “No shape retuning” is valid only at kernel-shape level. The active witness still depends on fixed decay/stimulus/design constants, which §7 acknowledges (`07_active_witness.tex:119-123`). Keep that caveat visible near every headline active claim.

**3. External Consistency / Numerics**
All requested numeric headlines match `repro/results.json`:

- `120` vertices, `720` edges, degree `12/12/12.0`: `results.json:4-9`; paper `main.tex:47-48`, `03_substrate.tex:392-409`.
- Shell sizes `{1,12,20,12,30,12,20,12,1}`: `results.json:15-25`; paper `03_substrate.tex:424-433`.
- Spectrum values/multiplicities match: `results.json:43-79`; paper `04_spectrum.tex:28-38`.
- Operator norm `2.618033988749902`, predicted `phi^2=2.618033988749895`: `results.json:81-85`; paper `04_spectrum.tex:76-78`.
- Correlations: unweighted per-vertex `0.976202`, shell `0.923208`; geometric `0.888380`; arithmetic `0.884364`: `results.json:134-146`; paper `05_agreement.tex:138-145`, `05_agreement.tex:200-202`.

Minor numeric presentation issue: spectrum table gives machine zero as `-3×10^{-15}` (`04_spectrum.tex:28`), while `results.json` grouped spectrum reports `-0.0` (`results.json:43-47`) and raw `lambda_min_L=-1.011e-15` (`results.json:81-83`). Replace with “machine zero” or the exact JSON value.

**4. Operator-Witness Scope Discipline**
No sentence directly claims `\Ph^{-2}` is derived, 600-cell uniqueness, kernel uniqueness, or a delivered ACT theorem. The main scope is disciplined.

Sentences needing tightening:
- `07_active_witness.tex:126` and `07_active_witness.tex:160`: unqualified “18/18” should become “17/18 standard; 18/18 after documented P4 `N=20` deep-dive.”
- `10_conclusion.tex:43-44`: same active-witness qualifier needed.
- `07_active_witness.tex:91-95`: add that the chess `+40.6`pp result is LOO/state-reset refinement, not the original 5-fold-CV estimator.
- `08_programme_home.tex:20-31`: remove theorem-like claims about forthcoming RH/YM artifacts or label them explicitly as non-load-bearing programme notes.

**5. Tightness**
Suggested one-line edits:

- Replace “`18/18 preregistered correspondences`” with “`17/18 under the standard validation protocol and 18/18 after the documented P4 N=20 deep-dive, with thresholds unchanged`.”
- Replace “`well above the preregistered ≥ +15pp floor`” for chess with “`+40.6pp under the disclosed LOO/state-reset refinement of the preregistered ≥+15pp substrate-lift test`.”
- Replace “`residual factor of about two remains`” with “`the basis correction accounts for part of the gap; the observed Bs→φ amplitude remains about twice the basis-corrected prediction, an open residual`.”
- In programme-home bullets, replace “`vanishing exactly on V_fix`” with “`reported in the forthcoming artifact as targeting V_fix; not used here`.”

**6. Surface Issues**
- Static cite/ref check: no missing citation keys or undefined refs found. I could not compile because the sandbox is read-only, including `/tmp`.
- Math in headings may trigger `hyperref` PDF-string warnings: `02_definition.tex:25`, `02_definition.tex:115`, `03_substrate.tex:80`, `04_spectrum.tex:65`, `04_spectrum.tex:83`, `08_programme_home.tex:12`. Use `\texorpdfstring`.
- Table `07_active_witness.tex:150` uses three `p{}` columns totaling `0.94\linewidth` plus tab padding; likely overfull. Use `@{}...@{}` or reduce widths.
- Macros `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` are used consistently.

**7. Top Three Fixes**
1. Qualify every active-witness “18/18” shorthand: `01_introduction.tex:156`, `01_introduction.tex:169-170`, `07_active_witness.tex:126`, `07_active_witness.tex:160`, `10_conclusion.tex:43-44`.
2. Add the P13 estimator/protocol qualifier wherever the chess `+40.6`pp result is inherited: especially `07_active_witness.tex:91-95`.
3. Soften or remove non-load-bearing programme claims about forthcoming RH/YM artifacts: `08_programme_home.tex:20-31`.

**8. Verdict**
Publication ready: no — must-fix list above. The core operator numerics check out, but the inherited active-witness claims need stricter qualifiers before publication.
tokens used
183,588
**1. Claim Audit**
References are repo-relative unless noted.

- “operator-norm bound `\|\Cph^{-1}\| = \Ph^{2}`” (`main.tex:51`, `02_definition.tex:72-93`, `04_spectrum.tex:65-78`): established for the connected 600-cell graph and any case with spectral bottom `0`. The paper correctly weakens this to `< \Ph^2` when `\lambda_{\min}(L_M)>0` (`02_definition.tex:86-89`).
- “continuum Green’s function `G(x)=(\Ph/2)e^{-|x|/\Ph}`” (`02_definition.tex:96-108`): correct for `-d^2/dx^2+\Ph^{-2}` on `R`. The paper does not overstate this as a continuum-limit theorem.
- “600-cell graph facts: `|V|=120`, `|E|=720`, degree 12, shells `{1,12,20,12,30,12,20,12,1}`” (`03_substrate.tex:18-37`, `03_substrate.tex:61-78`, `03_substrate.tex:80-107`): established numerically and classically cited.
- “Laplacian spectrum has nine eigenvalue classes in `Z[\Ph]`” (`04_spectrum.tex:5-14`, `04_spectrum.tex:28-38`): numerics support the values and multiplicities. The closed forms are explicitly “recognition,” not an exact derivation, which is the right scope.
- “per-vertex Pearson correlation `0.976`; shell-mean `0.923`; weighted variants `0.888`, `0.884`” (`05_agreement.tex:136-145`, `05_agreement.tex:187-204`): established by `results.json`. The paper correctly says “among the three tested variants,” not uniqueness.
- “b-anomaly five-dataset structural fit” (`06_passive_witness.tex:37-62`): table matches `../BANOMALY-001/vfd-b-anomaly/README.md:16-22`.
- “AIC tie / Gaussian alternative / Mode-B drift” (`06_passive_witness.tex:101-120`): matches README caveats at `README.md:31-33`.
- “cross-channel ratio … residual factor about two remains” (`06_passive_witness.tex:76-83`): supported by b-anomaly paper (`sections/08_discussion.tex:77-82`, `sections/10_conclusion.tex:40-41`), but not worded like the README’s “residual ~50% overshoot” (`README.md:27`). Harmonise the wording.
- “aria-chess `17/18` standard, `18/18` after `N=20` P4 deep-dive” (`main.tex:149-152`, `07_active_witness.tex:47-53`): matches aria-chess (`main.tex:81-84`, `sections/05_results.tex:92-96`). However, later shorthand “`18/18` preregistered” is too compressed (`07_active_witness.tex:126`, `07_active_witness.tex:160`, `10_conclusion.tex:43-44`).
- “chess lift `+40.6`pp” (`07_active_witness.tex:91-95`): number matches aria-chess, but the kernel summary omits that this is a disclosed LOO/state-reset refinement of a preregistered 5-fold-CV estimator (`aria-chess sections/07_cross_domain.tex:87-91`).
- “programme home: polynomial-in-`L` Lyapunov family” (`08_programme_home.tex:12-44`): safely marked programme-positioned, not classified. But the RH/YM bullets contain theorem-like detail about forthcoming artifacts (`08_programme_home.tex:20-31`) not established here; make them less specific or cite the exact source.

**2. Internal Consistency**
- Abstract/headline numbers are consistent with §5 and `results.json`: per-vertex `0.976`, weighted `0.888/0.884`, norm `2.618`, graph facts.
- Main scope discipline is strong: no derivation of `\Ph^{-2}`, no 600-cell uniqueness, no kernel uniqueness, no ACT theorem (`main.tex:65-77`, `main.tex:155-168`).
- Main inconsistency: active-witness shorthand. Some places preserve “17/18 standard, 18/18 after deep-dive” (`main.tex:149-152`), while others say only “18/18” (`01_introduction.tex:156`, `01_introduction.tex:169-170`, `07_active_witness.tex:126`, `10_conclusion.tex:43-44`).
- “No shape retuning” is valid only at kernel-shape level. The active witness still depends on fixed decay/stimulus/design constants, which §7 acknowledges (`07_active_witness.tex:119-123`). Keep that caveat visible near every headline active claim.

**3. External Consistency / Numerics**
All requested numeric headlines match `repro/results.json`:

- `120` vertices, `720` edges, degree `12/12/12.0`: `results.json:4-9`; paper `main.tex:47-48`, `03_substrate.tex:392-409`.
- Shell sizes `{1,12,20,12,30,12,20,12,1}`: `results.json:15-25`; paper `03_substrate.tex:424-433`.
- Spectrum values/multiplicities match: `results.json:43-79`; paper `04_spectrum.tex:28-38`.
- Operator norm `2.618033988749902`, predicted `phi^2=2.618033988749895`: `results.json:81-85`; paper `04_spectrum.tex:76-78`.
- Correlations: unweighted per-vertex `0.976202`, shell `0.923208`; geometric `0.888380`; arithmetic `0.884364`: `results.json:134-146`; paper `05_agreement.tex:138-145`, `05_agreement.tex:200-202`.

Minor numeric presentation issue: spectrum table gives machine zero as `-3×10^{-15}` (`04_spectrum.tex:28`), while `results.json` grouped spectrum reports `-0.0` (`results.json:43-47`) and raw `lambda_min_L=-1.011e-15` (`results.json:81-83`). Replace with “machine zero” or the exact JSON value.

**4. Operator-Witness Scope Discipline**
No sentence directly claims `\Ph^{-2}` is derived, 600-cell uniqueness, kernel uniqueness, or a delivered ACT theorem. The main scope is disciplined.

Sentences needing tightening:
- `07_active_witness.tex:126` and `07_active_witness.tex:160`: unqualified “18/18” should become “17/18 standard; 18/18 after documented P4 `N=20` deep-dive.”
- `10_conclusion.tex:43-44`: same active-witness qualifier needed.
- `07_active_witness.tex:91-95`: add that the chess `+40.6`pp result is LOO/state-reset refinement, not the original 5-fold-CV estimator.
- `08_programme_home.tex:20-31`: remove theorem-like claims about forthcoming RH/YM artifacts or label them explicitly as non-load-bearing programme notes.

**5. Tightness**
Suggested one-line edits:

- Replace “`18/18 preregistered correspondences`” with “`17/18 under the standard validation protocol and 18/18 after the documented P4 N=20 deep-dive, with thresholds unchanged`.”
- Replace “`well above the preregistered ≥ +15pp floor`” for chess with “`+40.6pp under the disclosed LOO/state-reset refinement of the preregistered ≥+15pp substrate-lift test`.”
- Replace “`residual factor of about two remains`” with “`the basis correction accounts for part of the gap; the observed Bs→φ amplitude remains about twice the basis-corrected prediction, an open residual`.”
- In programme-home bullets, replace “`vanishing exactly on V_fix`” with “`reported in the forthcoming artifact as targeting V_fix; not used here`.”

**6. Surface Issues**
- Static cite/ref check: no missing citation keys or undefined refs found. I could not compile because the sandbox is read-only, including `/tmp`.
- Math in headings may trigger `hyperref` PDF-string warnings: `02_definition.tex:25`, `02_definition.tex:115`, `03_substrate.tex:80`, `04_spectrum.tex:65`, `04_spectrum.tex:83`, `08_programme_home.tex:12`. Use `\texorpdfstring`.
- Table `07_active_witness.tex:150` uses three `p{}` columns totaling `0.94\linewidth` plus tab padding; likely overfull. Use `@{}...@{}` or reduce widths.
- Macros `\Ph`, `\Lop`, `\Cph`, `\Rsixhundred` are used consistently.

**7. Top Three Fixes**
1. Qualify every active-witness “18/18” shorthand: `01_introduction.tex:156`, `01_introduction.tex:169-170`, `07_active_witness.tex:126`, `07_active_witness.tex:160`, `10_conclusion.tex:43-44`.
2. Add the P13 estimator/protocol qualifier wherever the chess `+40.6`pp result is inherited: especially `07_active_witness.tex:91-95`.
3. Soften or remove non-load-bearing programme claims about forthcoming RH/YM artifacts: `08_programme_home.tex:20-31`.

**8. Verdict**
Publication ready: no — must-fix list above. The core operator numerics check out, but the inherited active-witness claims need stricter qualifiers before publication.
