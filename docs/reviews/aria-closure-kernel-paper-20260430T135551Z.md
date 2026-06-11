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
session id: 019ddead-1b4d-7840-8e1a-70ab0aac7aff
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

Source documents the kernel paper draws from:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/aria-closure-kernel.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md

This paper is an OPERATOR WITNESS, not a derivation. Hard discipline:
- never claim phi^-2 is derived (it is a design-level shift)
- never claim 600-cell uniqueness
- never claim the operator IS the unique kernel on either empirical landing
- never claim a Lyapunov / 2I-equivariance / selection theorem is delivered
- never inherit b-anomaly claims beyond what b-anomaly itself claims (AIC tie + Mode-B drift caveats inherited verbatim)
- never inherit aria-chess claims beyond substrate-witness scope
- per-vertex correlation is 0.976 unweighted, 0.888 phi-geom, 0.884 phi-arith
- shell-mean correlation is 0.923 unweighted (the per-vertex test is the headline)
- operator-norm ||C_phi^-1|| = phi^2 ~ 2.618 (computed) matches closed-form
- Laplacian spectrum: {0, 12-6phi, 12-4phi, 9, 12, 14, 4phi+8, 15, 6phi+6} with multiplicities {1,4,9,16,25,36,9,16,4}, sum 120

Read the file in full, then produce a structured review with the following sections:

1. **Claim audit**  Cite file:line for every issue.
2. **Internal consistency**
3. **External consistency / numerics**
4. **Operator-witness scope discipline**
5. **Tightness**
6. **Surface issues**
7. **Top three fixes**
8. **Verdict** -- exactly 'Publication ready: yes' or 'Publication ready: no -- must-fix list above'.

Be direct. Over-claiming is worse than under-claiming. Don't pad.
warning: Codex could not find bubblewrap on PATH. Install bubblewrap with your OS package manager. See the sandbox prerequisites: https://developers.openai.com/codex/concepts/sandboxing#prerequisites. Codex will use the vendored bubblewrap in the meantime.
codex
I’ll do this as a referee pass against the TeX, scripts, results, and cited source documents. I’m going to read the paper and the supporting artifacts first, then I’ll cross-check the numeric and scope claims before giving the structured verdict.
exec
/bin/bash -lc "wc -l papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex papers/aria-closure-kernel/paper/references.bib papers/aria-closure-kernel/repro/verify_kernel.py papers/aria-closure-kernel/repro/results.json docs/aria-closure-kernel.md /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/BANOMALY-001/vfd-b-anomaly/README.md papers/aria-chess-paper/paper/main.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"derive|derived|unique|uniqueness|Lyapunov|equivariance|selection theorem|phi\\"'^-2|600-cell|600 cell|AIC|Mode-B|Mode B|0'"\\.976|0\\.888|0\\.884|0\\.923|2\\.618|12-6|12-4|per-vertex|shell-mean|correlation|witness|operator\" papers/aria-closure-kernel/paper papers/aria-closure-kernel/repro docs/aria-closure-kernel.md /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/BANOMALY-001/vfd-b-anomaly/README.md papers/aria-chess-paper/paper/main.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 249ms:
papers/aria-chess-paper/paper/main.tex:19:\title{A geometry-fixed substrate witness for cortical signatures:\\
papers/aria-chess-paper/paper/main.tex:21:       signatures from the 600-cell under H$_4$ Coxeter symmetry}
papers/aria-chess-paper/paper/main.tex:39:Once the 600-cell substrate is chosen, its graph structure is fixed:
papers/aria-chess-paper/paper/main.tex:43:and through the response-operator stability shift $\Ph^{-2}$. The
papers/aria-chess-paper/paper/main.tex:52:literature-derived thresholds on a single deterministic substrate
papers/aria-chess-paper/paper/main.tex:62:This paper presents an empirical \emph{substrate witness}: it shows
papers/aria-chess-paper/paper/main.tex:66:selection theorem, nor a uniqueness claim for the 600-cell among regular
papers/aria-chess-paper/paper/main.tex:70:sits as the $L_M$ instance; the selection of the 600-cell as the active
papers/aria-chess-paper/paper/main.tex:74:We test whether a geometry-fixed substrate — the 600-cell regular
papers/aria-chess-paper/paper/main.tex:77:operator — is consistent with cortical signatures across five
papers/aria-chess-paper/paper/main.tex:112:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/main.tex:155:We do not claim the 600-cell is the unique substrate consistent with
papers/aria-chess-paper/paper/main.tex:157:have been ruled out. We do not derive the $\Ph^{-2}$ floor from
papers/aria-chess-paper/paper/main.tex:193:al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
docs/aria-closure-kernel.md:4:primitive defined; externally witnessed by a structural sign-uniform
docs/aria-closure-kernel.md:8:the programme-wide home for the polynomial-in-$L$ Lyapunov family
docs/aria-closure-kernel.md:11:## 1. The closure-response operator
docs/aria-closure-kernel.md:15:**$\varphi$-regularised closure operator**
docs/aria-closure-kernel.md:26:finite graph, or the standard continuum Laplace operator with
docs/aria-closure-kernel.md:49:## 3. Discrete substrate: the 600-cell
docs/aria-closure-kernel.md:51:The discrete VFD lift uses the 600-cell graph $V_{600}$:
docs/aria-closure-kernel.md:78:Independent passive-regime witness for $C_\varphi$ ships in the
docs/aria-closure-kernel.md:80:preprint `paper/main.pdf`, repro `repro/run_all.sh`). The witness is
docs/aria-closure-kernel.md:81:a **structural** test, not a detection claim or AIC preference:
docs/aria-closure-kernel.md:83:> A single fixed response kernel $\kappa(q^{2})$ — derived from the
docs/aria-closure-kernel.md:84:> 600-cell $V_{600}$ graph regularised by $\varphi^{-2}$ as a
docs/aria-closure-kernel.md:94:| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
docs/aria-closure-kernel.md:119:  (correlation $0.997$ with the continuum kernel); the same variant
docs/aria-closure-kernel.md:133:  Current data cannot resolve the model comparison. AIC is blind to
docs/aria-closure-kernel.md:135:- In the Mode-B stress test, a free-width Gaussian charm-loop
docs/aria-closure-kernel.md:137:  shape parameter; the kernel is *not* the unique $q^{2}$ shape
docs/aria-closure-kernel.md:139:- An earlier linearised "Mode B" analysis gave a stronger
docs/aria-closure-kernel.md:141:  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that **did not
docs/aria-closure-kernel.md:142:  survive the non-linear refit**. The $+2.77$-AIC-unit drift is the
docs/aria-closure-kernel.md:145:**Cocycle convergence (operator-level, not edge-weight-level).**
docs/aria-closure-kernel.md:151:both a pure-geometry criterion (correlation with the continuum
docs/aria-closure-kernel.md:154:(correlation $0.9968$ with the continuum kernel, data
docs/aria-closure-kernel.md:160:response operator and the 9-shell projection (which enters at the
docs/aria-closure-kernel.md:161:shell-mean step, not as an edge weight); it does **not**
docs/aria-closure-kernel.md:171:infrastructure, not an empirical claim. ẑ **shares operator-level
docs/aria-closure-kernel.md:172:infrastructure** with the b-anomaly response operator (the same
docs/aria-closure-kernel.md:178:## 5. Programme home for cascade Lyapunov / projector functionals
docs/aria-closure-kernel.md:193:- **YM cascade gap operator** (`ym-mass-gap.tex`,
docs/aria-closure-kernel.md:196:  mass-regularised Laplacian on the 600-cell substrate.
docs/aria-closure-kernel.md:199:  Lyapunov-of-polynomial-in-$L$ family.
docs/aria-closure-kernel.md:200:- **BSD operator** (`bsd-formal.tex`): $T_E$ on the enlarged
docs/aria-closure-kernel.md:202:  response-operator-family member.
docs/aria-closure-kernel.md:220:$C_\varphi$-derived $V_{600}$ kernel without shape retuning across
docs/aria-closure-kernel.md:224:the ARIA / aria-chess selection paper: a learning-rule / Lyapunov /
docs/aria-closure-kernel.md:228:The closure response $\psi = C_\varphi^{-1} f$ is derived from
docs/aria-closure-kernel.md:230:additionally requires a selection dynamic — a Lyapunov / coherence
docs/aria-closure-kernel.md:244:  edge-space lift / Lyapunov mechanism for the selection programme,
docs/aria-closure-kernel.md:264:- `papers/millennium-ym/ym-mass-gap.tex` — cascade gap operator as
docs/aria-closure-kernel.md:281:  primary shipped passive-regime empirical witness for the fixed
docs/aria-closure-kernel.md:282:  $C_\varphi$-derived $V_{600}$ kernel; five-dataset sign-uniform
docs/aria-closure-kernel.md:284:  honest AIC tie ($w_{\mathrm{VFD}} = 0.348$ vs
docs/aria-closure-kernel.md:285:  $w_{\mathrm{FREE\_C9}} = 0.652$) and Mode-B $+2.77$ drift caveat.
docs/aria-closure-kernel.md:294:  Mode-B drift documentation; the largest single methodological
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:3:**A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit.**
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:14:A single fixed response kernel $\kappa(q^{2})$ — derived from the 600-cell $V_{600}$ graph regularised by the golden ratio $\varphi^{-2}$ as a discrete mass scale, **with no shape parameters tuned to data** — provides a consistent description of the $q^{2}$ behaviour of the $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets covering two collaborations, two isospin partners, and three decay channels. Predictions are evaluated with `flavio.np_prediction` (non-linear in $\Delta C_{9}$). Only **one dimensionless amplitude $A$** is fitted per dataset; the kernel shape itself never moves.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:16:| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:28:- **Geometry-first variant test.** Of three discrete Laplacian variants, the unweighted choice wins on a *pure-geometry* criterion (correlation $0.997$ with the continuum kernel) decided **independently of the LHCb data**. The same variant later wins on the data $\chi^{2}$ — independent geometry and data criteria agree.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:31:- On Akaike model comparison, the kernel and a constant Wilson-coefficient shift $\mathrm{FREE\_C9}$ (also $k=1$) are statistically indistinguishable on current data: stacked Akaike weight $w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$. AIC compares per-parameter goodness-of-fit and is blind to the universality/shape-prediction claim itself.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:32:- A free-width Gaussian charm-loop proxy fits comparably in $\chi^{2}$ at the cost of one extra shape parameter; the kernel is not the unique $q^{2}$ shape consistent with the anomaly.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:33:- An earlier linearised analysis (the project's "Mode B") gave a stronger numerical preference for the kernel ($\Delta\mathrm{AIC}=-1.67$ on LHCb 2025) that **did not survive the non-linear refit**. The $+2.77$-AIC-unit drift is the largest single methodological uncertainty in the project. See §2 and §4 of [the paper](paper/main.pdf) and [`reports/wo016c_nonlinear_refit.md`](reports/wo016c_nonlinear_refit.md). Linearised numbers are retained in the paper as a methodology diagnostic.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:35:The structural test the project was designed to run — *can a fixed geometry-derived shape describe the anomaly across multiple independent datasets without retuning?* — is satisfied. Whether the kernel is statistically *preferred* over a constant shift is a question current data cannot resolve and will require future $b\to s\ell\ell$ measurements.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:44:| **F1** Geometry-derived kernel $\kappa(q^{2})$ on the LHCb $q^{2}$ window. Solid blue: discrete $V_{600}$ shell-mean (Layer 3, used in fits). Dashed grey: continuum $e^{-|x|/\varphi}$ (Layer 1). Red points: LHCb 2025 bin centres. | **F2** Per-bin pulls on the LHCb 2025 four-observable joint fit under the non-linear FREE\_C9 ($\Delta C_{9}=-1.00$) and VFD ($A=+1.14$) fits. |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:74:│   ├── wo009_full_lift.py         # 600-cell V_600 graph and discrete Green's response
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:88:│   ├── wo009_full_lift.{json,csv,md}  # 600-cell graph spectral data
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:175:| 2 | Datasets, SM backend (non-linear flavio + linearised Mode B), reproducibility ledger |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:178:| 5 | Stress tests on LHCb 2025 under Mode B (bin bootstrap, region splits, alternative Wilson-coefficient models, charm-loop Gaussian, BSZ form-factor MC) |
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:185:The paper went through three rounds of internal hostile review. The major finding from Round 2 was that the linearised fit's $\Delta\mathrm{AIC}=-1.67$ on LHCb 2025 flipped to $+1.09$ under a non-linear refit; the paper was rewritten around that negative finding and accepted as preprint-ready in Round 3.
/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md:207:  title        = {A geometry-derived response kernel for the $B \to K^{*}\mu^{+}\mu^{-}$ angular anomaly: sign-uniform cross-dataset and cross-channel fit},
papers/aria-closure-kernel/repro/README.md:17:1. **600-cell vertex set** — 8 axis + 16 half-integer + 96 φ-mixed
papers/aria-closure-kernel/repro/README.md:26:   {0, 12-6φ, 12-4φ, 9, 12, 14, 4φ+8, 15, 6φ+6} with multiplicities
papers/aria-closure-kernel/repro/README.md:29:5. **Operator-norm bound** — ‖C_φ⁻¹‖ = 2.618034 = φ², matching the
papers/aria-closure-kernel/repro/README.md:32:6. **Discrete ↔ continuum agreement** — per-vertex Pearson
papers/aria-closure-kernel/repro/README.md:33:   correlation between ψ = C_φ⁻¹ e_pole and the continuum kernel
papers/aria-closure-kernel/repro/README.md:35:   - **0.976** (unweighted Laplacian — wins)
papers/aria-closure-kernel/repro/README.md:36:   - 0.888 (φ-geometric weights)
papers/aria-closure-kernel/repro/README.md:37:   - 0.884 (φ-arithmetic weights)
papers/aria-closure-kernel/repro/verify_kernel.py:7:C_phi = L + phi^-2 I, runs the discrete <-> continuum agreement
papers/aria-closure-kernel/repro/verify_kernel.py:8:test as a per-vertex Pearson correlation between psi(v) and
papers/aria-closure-kernel/repro/verify_kernel.py:10:(plus a shell-mean cross-check), tests the unweighted vs
papers/aria-closure-kernel/repro/verify_kernel.py:12:correlation criterion, sweeps the per-vertex correlation across
papers/aria-closure-kernel/repro/verify_kernel.py:16:All constants (phi, the 600-cell vertex generators, the short-edge
papers/aria-closure-kernel/repro/verify_kernel.py:46:# 1. 600-cell vertex construction (120 vertices on S^3)
papers/aria-closure-kernel/repro/verify_kernel.py:63:    Canonical 600-cell vertex set: 8 + 16 + 96 = 120 unit vectors on S^3.
papers/aria-closure-kernel/repro/verify_kernel.py:107:    criterion on the unit 3-sphere). For the 600-cell this gives a
papers/aria-closure-kernel/repro/verify_kernel.py:147:# 4. Closure operator and discrete Green's function
papers/aria-closure-kernel/repro/verify_kernel.py:151:    """C_phi = L + phi^-2 I."""
papers/aria-closure-kernel/repro/verify_kernel.py:170:    Group vertices by their inner product with V[pole_idx]. The 600-cell's
papers/aria-closure-kernel/repro/verify_kernel.py:208:    shell radius, and the Pearson correlation between them.
papers/aria-closure-kernel/repro/verify_kernel.py:232:    # Pearson correlation of (discrete shell mean) with (continuum prediction)
papers/aria-closure-kernel/repro/verify_kernel.py:243:        "pearson_correlation": corr,
papers/aria-closure-kernel/repro/verify_kernel.py:283:def variant_correlation(V, A, source_idx, variant):
papers/aria-closure-kernel/repro/verify_kernel.py:297:    # Per-vertex correlation (excluding the source itself, which is degenerate)
papers/aria-closure-kernel/repro/verify_kernel.py:304:        "shell_mean_correlation": test["pearson_correlation"],
papers/aria-closure-kernel/repro/verify_kernel.py:305:        "per_vertex_correlation": per_vertex_corr,
papers/aria-closure-kernel/repro/verify_kernel.py:317:    short-edge adjacency matrix. Connectedness is reported, not derived from
papers/aria-closure-kernel/repro/verify_kernel.py:329:    Per-vertex correlation between psi = C_phi^-1 e_v and the continuum kernel
papers/aria-closure-kernel/repro/verify_kernel.py:331:    predicts the correlation is invariant under choice of source vertex; this
papers/aria-closure-kernel/repro/verify_kernel.py:345:        "min_correlation": float(corrs.min()),
papers/aria-closure-kernel/repro/verify_kernel.py:346:        "mean_correlation": float(corrs.mean()),
papers/aria-closure-kernel/repro/verify_kernel.py:347:        "max_correlation": float(corrs.max()),
papers/aria-closure-kernel/repro/verify_kernel.py:352:def operator_norm_check(L, w):
papers/aria-closure-kernel/repro/verify_kernel.py:354:    lam_min_C = lam_min_L + INV_PHI2  # phi^-2
papers/aria-closure-kernel/repro/verify_kernel.py:359:        "operator_norm_C_phi_inv": op_norm,
papers/aria-closure-kernel/repro/verify_kernel.py:381:    op_norm = operator_norm_check(L, w)
papers/aria-closure-kernel/repro/verify_kernel.py:396:        out = variant_correlation(V, A, pole_idx, variant)
papers/aria-closure-kernel/repro/verify_kernel.py:398:            "shell_mean_correlation": out["shell_mean_correlation"],
papers/aria-closure-kernel/repro/verify_kernel.py:399:            "per_vertex_correlation": out["per_vertex_correlation"],
papers/aria-closure-kernel/repro/verify_kernel.py:424:        "operator_norm": op_norm,
papers/aria-closure-kernel/repro/verify_kernel.py:426:        "variant_correlation": variants,
papers/aria-closure-kernel/repro/verify_kernel.py:449:    print(f"||C_phi^-1||  = {op_norm['operator_norm_C_phi_inv']:.6f}")
papers/aria-closure-kernel/repro/verify_kernel.py:452:    print("Discrete <-> continuum agreement (Pearson correlation):")
papers/aria-closure-kernel/repro/verify_kernel.py:453:    print(f"  variant         | shell-mean  | per-vertex")
papers/aria-closure-kernel/repro/verify_kernel.py:455:        sm = variants[v]["shell_mean_correlation"]
papers/aria-closure-kernel/repro/verify_kernel.py:456:        pv = variants[v]["per_vertex_correlation"]
papers/aria-closure-kernel/repro/verify_kernel.py:460:    print(f"  per-vertex correlation min  = {multi_source['min_correlation']:.6f}")
papers/aria-closure-kernel/repro/verify_kernel.py:461:    print(f"  per-vertex correlation mean = {multi_source['mean_correlation']:.6f}")
papers/aria-closure-kernel/repro/verify_kernel.py:462:    print(f"  per-vertex correlation max  = {multi_source['max_correlation']:.6f}")
papers/aria-closure-kernel/paper/main.tex:19:\title{The closure-response operator
papers/aria-closure-kernel/paper/main.tex:21:       a geometry-fixed kernel on the 600-cell with two\\
papers/aria-closure-kernel/paper/main.tex:22:       independent empirical witnesses}
papers/aria-closure-kernel/paper/main.tex:44:the 600-cell instance $\Rsixhundred$ as the discrete substrate
papers/aria-closure-kernel/paper/main.tex:45:shared by the two empirical witnesses (the choice of this polytope
papers/aria-closure-kernel/paper/main.tex:51:operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ from the smallest
papers/aria-closure-kernel/paper/main.tex:53:agreement at per-vertex Pearson correlation $0.976$ between the
papers/aria-closure-kernel/paper/main.tex:61:active-regime substrate witness against eighteen preregistered
papers/aria-closure-kernel/paper/main.tex:66:This paper presents an empirical \emph{operator witness}: a
papers/aria-closure-kernel/paper/main.tex:67:geometry-fixed response operator with operator shape held fixed
papers/aria-closure-kernel/paper/main.tex:73:$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
papers/aria-closure-kernel/paper/main.tex:75:selection theorem on the companion adaptive-closure-transport
papers/aria-closure-kernel/paper/main.tex:78:empirical landing (the b-anomaly AIC comparison and the aria-chess
papers/aria-closure-kernel/paper/main.tex:79:substrate-witness scope are documented in their own preprints and
papers/aria-closure-kernel/paper/main.tex:85:$\Ph = (1+\sqrt 5)/2$, give the 600-cell graph $\Rsixhundred$ as
papers/aria-closure-kernel/paper/main.tex:86:the discrete instance shared by two empirical witnesses, and
papers/aria-closure-kernel/paper/main.tex:87:document its appearance as the same fixed operator (no shape
papers/aria-closure-kernel/paper/main.tex:92:preregistered substrate witness against substrate/neuroscience
papers/aria-closure-kernel/paper/main.tex:100:values, operator-norm identity $\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$
papers/aria-closure-kernel/paper/main.tex:103:agreement at per-vertex Pearson correlation $0.976$ for the
papers/aria-closure-kernel/paper/main.tex:105:tested ($0.888$ geometric, $0.884$ arithmetic). Within the three
papers/aria-closure-kernel/paper/main.tex:117:$\Ph^{-2} \approx 0.382$, operator norm
papers/aria-closure-kernel/paper/main.tex:118:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
papers/aria-closure-kernel/paper/main.tex:122:\noindent\emph{(ii) The 600-cell instance.}
papers/aria-closure-kernel/paper/main.tex:131:Per-vertex Pearson correlation between the discrete response
papers/aria-closure-kernel/paper/main.tex:134:vertex's chord distance: $0.976$ (unweighted Laplacian), $0.888$
papers/aria-closure-kernel/paper/main.tex:135:($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
papers/aria-closure-kernel/paper/main.tex:137:correlation is invariant under choice of source up to numerical
papers/aria-closure-kernel/paper/main.tex:140:\noindent\emph{(iv) Two independent empirical witnesses.}
papers/aria-closure-kernel/paper/main.tex:160:We do not derive the $\Ph^{-2}$ floor; it is a design-level
papers/aria-closure-kernel/paper/main.tex:162:not claim $\Rsixhundred$ is the unique substrate consistent with
papers/aria-closure-kernel/paper/main.tex:163:either empirical landing. We do not claim the operator is the
papers/aria-closure-kernel/paper/main.tex:164:unique kernel shape consistent with the b-anomaly data
papers/aria-closure-kernel/paper/main.tex:165:(b-anomaly's free-width Gaussian alternative and Mode-B refit
papers/aria-closure-kernel/paper/main.tex:167:aria-chess substrate witness establishes a selection theorem on
papers/aria-closure-kernel/paper/main.tex:169:this paper is: \emph{one geometry-fixed operator on one fixed
papers/aria-closure-kernel/paper/main.tex:181:\input{sections/06_passive_witness.tex}
papers/aria-closure-kernel/paper/main.tex:182:\input{sections/07_active_witness.tex}
papers/aria-closure-kernel/paper/main.tex:190:short-edge graph build, Laplacian spectrum, operator-norm bound,
papers/aria-closure-kernel/paper/main.tex:191:discrete-to-continuum correlation across three Laplacian variants)
papers/aria-closure-kernel/paper/main.tex:196:The two empirical witness preprints
papers/aria-closure-kernel/paper/README.md:3:The closure-response operator $C_\varphi = L + \varphi^{-2} I$ on the
papers/aria-closure-kernel/paper/README.md:4:600-cell graph $V_{600}$, threading two independent empirical witnesses
papers/aria-closure-kernel/paper/README.md:5:(b-anomaly + aria-chess) on the same fixed operator with no shape
papers/aria-closure-kernel/paper/README.md:18:Laplacian spectrum, operator-norm bound, discrete-to-continuum Pearson
papers/aria-closure-kernel/paper/README.md:19:correlations across three Laplacian variants) are reproduced from
papers/aria-closure-kernel/paper/README.md:38:sections/05_agreement.tex             discrete↔continuum correlation test
papers/aria-closure-kernel/paper/README.md:39:sections/06_passive_witness.tex       b-anomaly five-dataset structural fit
papers/aria-closure-kernel/paper/README.md:40:sections/07_active_witness.tex        aria-chess 18/18 + 6/6 EEG
papers/aria-closure-kernel/paper/README.md:41:sections/08_programme_home.tex        polynomial-in-L Lyapunov family + open selection layer
papers/aria-closure-kernel/paper/README.md:43:sections/10_conclusion.tex            operator-witness verdict
papers/aria-closure-kernel/paper/README.md:48:This is an **operator witness**, not:
papers/aria-closure-kernel/paper/README.md:50:- a uniqueness claim for the 600-cell among regular 4-polytopes,
papers/aria-closure-kernel/paper/README.md:51:- a selection theorem on the ACT 4-tuple,
papers/aria-closure-kernel/paper/README.md:52:- a kernel-uniqueness claim on either empirical landing
papers/aria-closure-kernel/paper/README.md:53:  (b-anomaly Mode-B and AIC-tie caveats inherited verbatim;
papers/aria-closure-kernel/paper/README.md:54:  aria-chess substrate-witness scope inherited verbatim).
papers/aria-closure-kernel/paper/README.md:63:  witness against eighteen preregistered cortical correspondences.
papers/aria-closure-kernel/paper/references.bib:18:% Companion VFD preprints (the two empirical witnesses + selection-layer paper).
papers/aria-closure-kernel/paper/references.bib:22:  title  = {A geometry-derived response kernel for the $B \to K^*\mu^+\mu^-$
papers/aria-closure-kernel/paper/references.bib:30:  title  = {A geometry-fixed substrate witness for cortical signatures:
papers/aria-closure-kernel/paper/references.bib:32:            signatures from the 600-cell under H$_4$ Coxeter symmetry},
papers/aria-closure-kernel/repro/results.json:81:  "operator_norm": {
papers/aria-closure-kernel/repro/results.json:84:    "operator_norm_C_phi_inv": 2.618033988749902,
papers/aria-closure-kernel/repro/results.json:85:    "predicted_phi_squared": 2.618033988749895
papers/aria-closure-kernel/repro/results.json:132:    "pearson_correlation": 0.9232082699765517
papers/aria-closure-kernel/repro/results.json:134:  "variant_correlation": {
papers/aria-closure-kernel/repro/results.json:136:      "shell_mean_correlation": 0.9232082699765517,
papers/aria-closure-kernel/repro/results.json:137:      "per_vertex_correlation": 0.9762022978516623
papers/aria-closure-kernel/repro/results.json:140:      "shell_mean_correlation": 0.879553132802029,
papers/aria-closure-kernel/repro/results.json:141:      "per_vertex_correlation": 0.8883800503732451
papers/aria-closure-kernel/repro/results.json:144:      "shell_mean_correlation": 0.8784315463215415,
papers/aria-closure-kernel/repro/results.json:145:      "per_vertex_correlation": 0.8843640031310793
papers/aria-closure-kernel/repro/results.json:150:    "min_correlation": 0.9762022978516617,
papers/aria-closure-kernel/repro/results.json:151:    "mean_correlation": 0.9762022978516628,
papers/aria-closure-kernel/repro/results.json:152:    "max_correlation": 0.9762022978516637,
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:2:\section{Active-regime witness: aria-chess}\label{sec:active_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:7:summarise here only what the operator-witness narrative requires
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:8:and inherit the preprint's substrate-witness scope verbatim.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:35:witness.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:64:against literature-derived thresholds:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:118:\subsection{Reading at the operator level}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:121:witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:125:operator, aria-chess inherits its own dynamical and stimulus
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:138:The aria-chess preprint stays inside substrate-witness scope: it
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:140:claim 600-cell uniqueness among regular 4-polytopes, and does not
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:141:deliver a selection theorem on the ACT 4-tuple. We inherit the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:142:scope verbatim. What we add at the operator level is the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:147:layer above $\Cph$ are distinct above-operator constructions; the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:148:operator below them is the same).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:150:\subsection{Two-witness structure}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:157:\label{tab:two_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:171:Caveat             & AIC tie; free-width Gaussian alt.\ & single-seed EEG; no polytope ablation \\
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:176:The two witnesses share, by design, exactly the geometry-fixed
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:177:operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:179:threshold, dataset, or methodological choice above the operator
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:185:the empirical layer above the shared operator.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:7:localised source has high per-vertex Pearson correlation in radial
papers/aria-closure-kernel/paper/sections/05_agreement.tex:10:the source. Pearson correlation is a shape similarity statistic, not
papers/aria-closure-kernel/paper/sections/05_agreement.tex:30:The agreement criterion is the Pearson correlation between
papers/aria-closure-kernel/paper/sections/05_agreement.tex:38:\texttt{repro/verify\_kernel.py:variant\_correlation} returns:
papers/aria-closure-kernel/paper/sections/05_agreement.tex:40:\item \textbf{Multiplicity-weighted per-vertex Pearson correlation
papers/aria-closure-kernel/paper/sections/05_agreement.tex:41:  over shell-constant responses}: $\rho = 0.976$. (See
papers/aria-closure-kernel/paper/sections/05_agreement.tex:43:  to machine precision under H$_3$-fixed source, so the per-vertex
papers/aria-closure-kernel/paper/sections/05_agreement.tex:45:  correlation rather than $119$ independent radial samples.)
papers/aria-closure-kernel/paper/sections/05_agreement.tex:46:\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
papers/aria-closure-kernel/paper/sections/05_agreement.tex:48:  correlating the $9$-point shell-mean trajectory with the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:51:The two correlations measure the same shell-radius fact at
papers/aria-closure-kernel/paper/sections/05_agreement.tex:60:  on the shell-mean side and contributes a single
papers/aria-closure-kernel/paper/sections/05_agreement.tex:63:On the unweighted 600-cell graph with an H$_3$-fixed source,
papers/aria-closure-kernel/paper/sections/05_agreement.tex:67:source convention, not in noise content: the per-vertex test
papers/aria-closure-kernel/paper/sections/05_agreement.tex:70:and excludes the source vertex, while the shell-mean test gives
papers/aria-closure-kernel/paper/sections/05_agreement.tex:72:per-vertex test is the headline agreement criterion in this paper.
papers/aria-closure-kernel/paper/sections/05_agreement.tex:95:\caption{Per-vertex and shell-mean Pearson correlations between the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:99:Computed by \texttt{repro/verify\_kernel.py:variant\_correlation}.}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:100:\label{tab:variant_correlation}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:103:Variant            & Per-vertex correlation & Shell-mean correlation \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:105:\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:106:$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:107:$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:114:($+0.088$ per-vertex over the next variant, $+0.044$ shell-mean).
papers/aria-closure-kernel/paper/sections/05_agreement.tex:118:on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:120:correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
papers/aria-closure-kernel/paper/sections/05_agreement.tex:122:this is a uniqueness or blind-selection result; we report it as a
papers/aria-closure-kernel/paper/sections/05_agreement.tex:131:response of a fixed-shift Green operator on a fixed graph
papers/aria-closure-kernel/paper/sections/05_agreement.tex:132:correlates per-vertex in radial shape, at Pearson $0.976$, with
papers/aria-closure-kernel/paper/sections/05_agreement.tex:134:$\Ph$. This is a non-trivial Pearson correlation between
papers/aria-closure-kernel/paper/sections/05_agreement.tex:142:\paragraph{Does not establish.} Operator uniqueness on either
papers/aria-closure-kernel/paper/sections/05_agreement.tex:148:$\Rsixhundred$ is the unique discrete substrate with this
papers/aria-closure-kernel/paper/sections/05_agreement.tex:150:graphs would need to be tested on the same correlation criterion
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:6:and identifies what the operator does not deliver. The framing
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:12:\subsection{Programme home: polynomial-in-$L$ Lyapunov family}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:28:\item \textbf{YM cascade gap operator} (forthcoming YM artifact in
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:41:theorem is used here. Each named operator is in a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:59:  time? (Crystallisation / Lyapunov descent dynamics on a
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:72:  4-tuple $(M, L_M, W, R_{\mathrm{hom}})$ proposes a Lyapunov
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:74:  $2I$-equivariance, and a full reduced-flow convergence theorem
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:77:  the substrate-witness scope explicitly does \emph{not} deliver
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:78:  a selection theorem; ACT is positioned as the future
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:79:  selection-theorem witness.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:85:gives no proof of equivalence. The two empirical witnesses landed
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:92:\paragraph{Closes (at the operator-witness level).}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:94:\item The operator $\Cph$ is well-defined and positive definite
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:95:  on any $(M, L_M)$ satisfying (H1)--(H3); the operator-norm
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:102:\item The 600-cell instance $\Rsixhundred$ has the construction
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:106:\item Discrete-to-continuum agreement at per-vertex Pearson
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:107:  correlation $0.976$ on the unweighted variant, with the unweighted
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:112:  qualitatively distinct regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:113:  \S\ref{sec:active_witness}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:119:  as a design-level shift; not derived from a closure functional
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:121:\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:125:\item \emph{Kernel-uniqueness on either empirical landing.} The
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:127:  one extra shape parameter) and the AIC tie
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:130:\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:131:  decomposition under $2I$-equivariance, full reduced-flow
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:136:  positioning of cascade Lyapunov functionals as members of the
papers/aria-closure-kernel/paper/sections/02_definition.tex:2:\section{The closure-response operator}\label{sec:definition}
papers/aria-closure-kernel/paper/sections/02_definition.tex:11:continuum operator $-\Delta$ with chosen boundary conditions).
papers/aria-closure-kernel/paper/sections/02_definition.tex:15:The \emph{closure-response operator} is
papers/aria-closure-kernel/paper/sections/02_definition.tex:45:  for the operator-norm identity in
papers/aria-closure-kernel/paper/sections/02_definition.tex:53:  undirected graph (the 600-cell case, $\lambda_{\min}(L_M) = 0$);
papers/aria-closure-kernel/paper/sections/02_definition.tex:63:is unbounded, or operators with negative spectrum — require their
papers/aria-closure-kernel/paper/sections/02_definition.tex:80:The operator norm of $\Cph^{-1}$ is the reciprocal of the smallest
papers/aria-closure-kernel/paper/sections/02_definition.tex:90:\|\Cph^{-1}\| \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/02_definition.tex:101:2.618034$ on $\Rsixhundred$ (\texttt{repro/verify\_kernel.py},
papers/aria-closure-kernel/paper/sections/02_definition.tex:130:\item both the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ and
papers/aria-closure-kernel/paper/sections/02_definition.tex:133:  dimensional parameter throughout the operator;
papers/aria-closure-kernel/paper/sections/02_definition.tex:137:We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
papers/aria-closure-kernel/paper/sections/09_limitations.tex:14:\textbf{Single substrate (the 600-cell).} We have not tested
papers/aria-closure-kernel/paper/sections/09_limitations.tex:16:Coxeter graphs would give comparable per-vertex correlations on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:18:fits on either empirical landing. The 600-cell choice is post-hoc
papers/aria-closure-kernel/paper/sections/09_limitations.tex:22:\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
papers/aria-closure-kernel/paper/sections/09_limitations.tex:23:empirical landings of \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/09_limitations.tex:24:\S\ref{sec:active_witness}. \emph{Strengthening build:}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:26:$120$-cell, with the same per-vertex correlation criterion
papers/aria-closure-kernel/paper/sections/09_limitations.tex:34:comparable per-vertex correlation, or whether the empirical
papers/aria-closure-kernel/paper/sections/09_limitations.tex:39:continuum correlation; report sensitivity envelope.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:43:\textbf{The 600-cell choice is post-hoc justified by empirical
papers/aria-closure-kernel/paper/sections/09_limitations.tex:50:\emph{Evidence:} two independent empirical witnesses on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:59:\emph{criterion-independent} (geometry-only correlation here is a
papers/aria-closure-kernel/paper/sections/09_limitations.tex:66:\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
papers/aria-closure-kernel/paper/sections/09_limitations.tex:68:strictly positive definite; it is not derived from a closure
papers/aria-closure-kernel/paper/sections/09_limitations.tex:71:same operator with the same shift serves as the basis for two
papers/aria-closure-kernel/paper/sections/09_limitations.tex:72:independent empirical witnesses across qualitatively distinct
papers/aria-closure-kernel/paper/sections/09_limitations.tex:73:regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:74:\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
papers/aria-closure-kernel/paper/sections/09_limitations.tex:77:uniqueness is not assumed and is itself an open problem.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:82:causal.} The per-vertex correlation $0.976$ between $\psi$ on
papers/aria-closure-kernel/paper/sections/09_limitations.tex:86:objects, not a derivation that the discrete operator equals the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:89:precision in the operator-norm bound and at $\rho = 0.976$ in the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:90:per-vertex correlation. \emph{Strengthening build:} a formal
papers/aria-closure-kernel/paper/sections/09_limitations.tex:98:\emph{unique} natural ranking. Edge-weighted variants outside the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:108:under an AIC tie with $\mathrm{FREE\_C9}$ on current data; the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:109:aria-chess result is a substrate witness (no claim that the
papers/aria-closure-kernel/paper/sections/09_limitations.tex:113:verbatim. \emph{Disclosure:} \S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:114:\S\ref{sec:active_witness}. \emph{Evidence:} the witnesses pass
papers/aria-closure-kernel/paper/sections/09_limitations.tex:115:their own preregistered or literature-derived thresholds.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:117:(LHCb Run~3, Belle~II) for the passive-regime witness;
papers/aria-closure-kernel/paper/sections/09_limitations.tex:119:(Schaefer, Glasser) for the active-regime witness; both already
papers/aria-closure-kernel/paper/sections/09_limitations.tex:122:\textbf{Discrete-to-continuum correlation reported on a single pole,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:123:verified across all $|V|$.} The headline per-vertex correlation
papers/aria-closure-kernel/paper/sections/09_limitations.tex:124:$0.976$ is reported with the canonical pole ($+x_{0}$ axis) as
papers/aria-closure-kernel/paper/sections/09_limitations.tex:125:source. H$_4$ transitivity predicts the correlation is invariant
papers/aria-closure-kernel/paper/sections/09_limitations.tex:128:per-vertex correlation $0.976202$ to within $\sim 10^{-15}$
papers/aria-closure-kernel/paper/sections/09_limitations.tex:131:representative, not a sample, of the operator's behaviour under
papers/aria-closure-kernel/paper/sections/09_limitations.tex:138:(Lyapunov $V(W)$, edge-space decomposition under $2I$-equivariance,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:141:delivered here. The two empirical witnesses strengthen confidence
papers/aria-closure-kernel/paper/sections/09_limitations.tex:146:coalgebra paper, and the Millennium drafts share operator-level
papers/aria-closure-kernel/paper/sections/09_limitations.tex:152:\item Lyapunov function $V(W)$ on the reduced flow — open build
papers/aria-closure-kernel/paper/sections/09_limitations.tex:154:\item $2I$-equivariance audit of the closure operator family —
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:170:The result is an \emph{operator witness}: a geometry-fixed response
papers/aria-closure-kernel/paper/sections/09_limitations.tex:171:operator on a fixed graph, with no shape parameters tuned to any
papers/aria-closure-kernel/paper/sections/09_limitations.tex:173:qualitatively distinct regimes. We do not claim the operator is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:174:the unique kernel for either landing. We do not claim selection is
papers/aria-closure-kernel/paper/sections/09_limitations.tex:175:delivered. We do not claim 600-cell uniqueness. The strengthening
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:5:The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:6:600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:10:smallest eigenvalue $\Ph^{-2}$ and operator-norm identity
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:11:$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$ (general substrates with
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:14:The 600-cell instance has $|V|=120$, $|E|=720$, uniform degree
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:19:the continuum kernel $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:20:chord distances (non-source vertices) is Pearson $\rho = 0.976$ on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:22:variants tested ($0.888$ geometric, $0.884$ arithmetic). All numbers are reproduced from canonical
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:39:  recurrent self-model layer above the same operator (one
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:50:By design, the two witnesses share exactly the geometry-fixed
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:51:operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:52:$\Ph^{-2}$. Above that operator level, they share no fitted
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:56:independence at the empirical layer above the shared operator,
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:57:not statistical independence of the operator itself.
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:59:\textbf{Operator-witness scope.} This is an operator witness, not
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:60:a derivation of physics on either landing. We do not derive the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:62:claim 600-cell uniqueness; alternative regular 4-polytopes are an
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:63:explicit ablation build. We do not claim kernel uniqueness on
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:65:alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:67:aria-chess substrate-witness scope is inherited verbatim. We do
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:68:not deliver a selection theorem on the ACT
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:70:open builds (Lyapunov $V(W)$, edge-space decomposition under
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:71:$2I$-equivariance, full reduced-flow convergence) remain open and
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:84:The empirical material gathered here is the operator witness; the
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:85:broader programme to convert the witness into a selection-theorem-
papers/aria-closure-kernel/paper/sections/01_introduction.tex:5:A response operator on a fixed graph, with no shape parameters
papers/aria-closure-kernel/paper/sections/01_introduction.tex:14:preprint that names the operator, gives its construction in full,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:19:The operator is
papers/aria-closure-kernel/paper/sections/01_introduction.tex:29:operator-norm bound is
papers/aria-closure-kernel/paper/sections/01_introduction.tex:31:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:37:The discrete substrate used by the two empirical witnesses is
papers/aria-closure-kernel/paper/sections/01_introduction.tex:38:the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:56:We claim a single \emph{operator witness}: that one geometry-fixed
papers/aria-closure-kernel/paper/sections/01_introduction.tex:57:operator, on one fixed graph, with no shape-parameter retuning
papers/aria-closure-kernel/paper/sections/01_introduction.tex:67:  operator. The Laplacian spectrum, the operator-norm bound, and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:73:  response $\psi = \Cph^{-1} f$ correlates per-vertex with the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:75:  $\rho = 0.976$ on the unweighted graph Laplacian. This is
papers/aria-closure-kernel/paper/sections/01_introduction.tex:82:  $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
papers/aria-closure-kernel/paper/sections/01_introduction.tex:83:  correlation: $0.888$ and $0.884$ respectively. Within the three
papers/aria-closure-kernel/paper/sections/01_introduction.tex:88:  (\S\ref{sec:passive_witness}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:89:\item \textbf{Two independent empirical landings, same operator.}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:108:  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
papers/aria-closure-kernel/paper/sections/01_introduction.tex:111:\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
papers/aria-closure-kernel/paper/sections/01_introduction.tex:114:  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
papers/aria-closure-kernel/paper/sections/01_introduction.tex:117:\item \emph{Not a kernel-uniqueness claim on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:121:  parameter; the b-anomaly AIC comparison against
papers/aria-closure-kernel/paper/sections/01_introduction.tex:126:\item \emph{Not a selection theorem on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:130:  fills the response slot. Selection — Lyapunov $V(W)$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:131:  reduced flow, edge-space decomposition under $2I$-equivariance,
papers/aria-closure-kernel/paper/sections/01_introduction.tex:137:  do not relitigate them here; their substrate-witness scope
papers/aria-closure-kernel/paper/sections/01_introduction.tex:143:To keep this paper inside the operator-witness scope, we use the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:156:operator-norm bound, the per-vertex correlation $0.976$) licenses
papers/aria-closure-kernel/paper/sections/01_introduction.tex:158:fixed operator (sign uniformity in $5/5$ b-anomaly datasets, the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:162:`derives the kernel', `proves uniqueness', or `establishes
papers/aria-closure-kernel/paper/sections/01_introduction.tex:169:\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:170:600-cell graph, with computed spectrum, operator-norm bound, and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:171:discrete-to-continuum correlation; the same fixed operator appearing
papers/aria-closure-kernel/paper/sections/01_introduction.tex:178:\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
papers/aria-closure-kernel/paper/sections/01_introduction.tex:179:$\Rsixhundred$; uniqueness of the kernel shape on either empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:180:landing; a selection theorem on the ACT 4-tuple; that either
papers/aria-closure-kernel/paper/sections/01_introduction.tex:182:or consciousness) by the operator alone.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:188:\S\ref{sec:definition} gives the operator definition, the positivity
papers/aria-closure-kernel/paper/sections/01_introduction.tex:189:properties of $\Cph$, the operator-norm bound, and the continuum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:195:across three Laplacian variants. \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:196:\S\ref{sec:active_witness} thread the two independent empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:197:witnesses (b-anomaly and aria-chess) at the operator level.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:199:for the polynomial-in-$L$ Lyapunov family that recurs across the
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:72:and the operator-norm bound is
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:74:\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618034.
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:76:\texttt{repro/verify\_kernel.py:operator\_norm\_check} reports
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:77:$\|\Cph^{-1}\| = 2.618034$ (numerical) vs $\Ph^{2} = 2.618034$
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:99:a load-bearing fact for any operator-witness claim made here. We
papers/aria-closure-kernel/paper/sections/03_substrate.tex:2:\section{The 600-cell substrate}\label{sec:substrate}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:6:witnesses: $M = \Rsixhundred$, the 600-cell regular 4-polytope
papers/aria-closure-kernel/paper/sections/03_substrate.tex:58:nearest-neighbour adjacency on the canonical 600-cell embedding
papers/aria-closure-kernel/paper/sections/03_substrate.tex:73:  classical 600-cell connectivity result is well known
papers/aria-closure-kernel/paper/sections/03_substrate.tex:106:The antipode $-v_{0}$ is the unique shell-$8$ vertex.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:129:  (\S\ref{ssec:opnorm}); the operator-norm bound
papers/aria-closure-kernel/paper/sections/03_substrate.tex:133:  4-polytopes / Coxeter substrates. The 600-cell choice is
papers/aria-closure-kernel/paper/sections/03_substrate.tex:135:  (\S\ref{sec:passive_witness}, \S\ref{sec:active_witness}). A
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:2:\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:7:summarise here only what the operator-witness narrative requires
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:27:operator, not a derivation of $\Ph^{-2}$), and $A$ is a single
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:52:Dataset & Decay & $n$ & $\Delta\mathrm{AIC}_{\mathrm{NL}}$ &
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:92:  criterion (correlation $0.997$ with the continuum kernel under
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:95:  paper's per-vertex test, whose unweighted score is $0.976$;
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:99:  fixed operator.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:108:\item \textbf{AIC tie on current data.} On Akaike model comparison,
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:109:  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:111:  indistinguishable: stacked AIC weights
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:113:  Current data cannot resolve the model comparison. AIC is blind
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:119:  is not the unique $q^{2}$ shape consistent with the anomaly.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:120:\item \textbf{Mode-B drift (linearised-to-non-linear refit).} An
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:121:  earlier analysis the b-anomaly project labels Mode-B
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:123:  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:124:  the subsequent non-linear refit; the $+2.77$-AIC-unit drift
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:125:  between Mode-B (linearised) and the non-linear refit is the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:139:\subsection{Reading at the operator level}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:142:witness for $\Cph$ on $\Rsixhundred$: a single linear response
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:149:side (the AIC tie, the free-width Gaussian alternative, and the
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:150:Mode-B linearised-to-non-linear refit drift prevent that). It
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:151:does support, at the operator-witness level, the inherited reading
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:155:second landing is in \S\ref{sec:active_witness}.

 succeeded in 272ms:
   204 papers/aria-closure-kernel/paper/main.tex
   201 papers/aria-closure-kernel/paper/sections/01_introduction.tex
   145 papers/aria-closure-kernel/paper/sections/02_definition.tex
   138 papers/aria-closure-kernel/paper/sections/03_substrate.tex
   100 papers/aria-closure-kernel/paper/sections/04_spectrum.tex
   152 papers/aria-closure-kernel/paper/sections/05_agreement.tex
   155 papers/aria-closure-kernel/paper/sections/06_passive_witness.tex
   185 papers/aria-closure-kernel/paper/sections/07_active_witness.tex
   139 papers/aria-closure-kernel/paper/sections/08_programme_home.tex
   176 papers/aria-closure-kernel/paper/sections/09_limitations.tex
    87 papers/aria-closure-kernel/paper/sections/10_conclusion.tex
    68 papers/aria-closure-kernel/paper/references.bib
   469 papers/aria-closure-kernel/repro/verify_kernel.py
   154 papers/aria-closure-kernel/repro/results.json
   295 docs/aria-closure-kernel.md
   227 /mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/README.md
   212 papers/aria-chess-paper/paper/main.tex
  3107 total

codex
The first scan shows the manuscript is trying to police the right boundaries. I’m now reading the line-numbered text and the numerical artifacts directly, because several possible issues depend on exact wording rather than just keyword hits.
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/main.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/01_introduction.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/02_definition.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/03_substrate.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 174ms:
     1	% =====================================================================
     2	\section{The 600-cell substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section gives the discrete instance used by the two empirical
     6	witnesses: $M = \Rsixhundred$, the 600-cell regular 4-polytope
     7	under H$_4$ Coxeter symmetry, with the standard short-edge graph
     8	Laplacian. The choice of this polytope is post-hoc motivated by
     9	the empirical landings (\S\ref{sec:limitations}); the
    10	construction itself is a classical Coxeter-group result we cite,
    11	not prove, here~\citep{CoxeterRegularPolytopes}. All facts in
    12	this section are reproduced numerically by
    13	\texttt{repro/verify\_kernel.py} from the canonical generators
    14	alone.
    15	
    16	\subsection{Vertex set}\label{ssec:vertices}
    17	
    18	$\Rsixhundred$ has $|V|=120$ unit vectors on the unit $3$-sphere
    19	$S^{3} \subset \mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,
    20	Weisstein600Cell}. With $\Ph = (1+\sqrt 5)/2$ the canonical vertex
    21	list partitions into three standard coordinate families:
    22	\begin{itemize}\itemsep=2pt
    23	\item \textbf{Axis family} ($8$ vertices): all permutations of
    24	  $(\pm 1, 0, 0, 0)$;
    25	\item \textbf{Half-integer family} ($16$ vertices): all sign
    26	  combinations of $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    27	\item \textbf{$\Ph$-mixed family} ($96$ vertices): all even
    28	  permutations of $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$ (with the
    29	  $\Ph^{2} = \Ph + 1$ identity, equivalently
    30	  $(\pm \Ph, \pm 1, \pm \Ph^{-1}, 0)/2$).
    31	\end{itemize}
    32	The total is $8 + 16 + 96 = 120$ unit vectors. These are coordinate
    33	families, not H$_4$ orbits: H$_4$ acts transitively on the full
    34	$120$-vertex set, so the three families lie in a single H$_4$
    35	orbit. Reproduced by \texttt{repro/verify\_kernel.py:build\_v600};
    36	the numerical check $\max_{v} |\,\|v\| - 1\,| < 10^{-10}$ confirms
    37	all vertices on $S^{3}$.
    38	
    39	The H$_4$ Coxeter group (order $14400$) acts transitively on the
    40	$120$ vertices. Every vertex therefore has \emph{identical} local
    41	structure under $H_{4}$; in particular, every vertex has the same
    42	degree in the short-edge graph defined below.
    43	
    44	\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
    45	
    46	For two unit vectors $v, w \in \Rsixhundred$ on $S^{3}$, the
    47	Euclidean chord distance is
    48	\[
    49	\|v - w\| \;=\; \sqrt{2 - 2\,\langle v, w\rangle}.
    50	\]
    51	The \emph{short-edge graph} $G_{V_{600}}=(V,E)$ connects two vertices
    52	if their inner product equals the canonical short-edge value
    53	\begin{equation}\label{eq:short_edge}
    54	\langle v, w\rangle \;=\; \Ph/2 \;\approx\; 0.809,
    55	\end{equation}
    56	equivalently chord distance
    57	$\|v-w\|=\sqrt{2-\Ph} = 1/\Ph \approx 0.618$. This is the
    58	nearest-neighbour adjacency on the canonical 600-cell embedding
    59	into $S^{3}$~\citep{CoxeterRegularPolytopes}.
    60	
    61	\paragraph{Graph facts (forced by the construction).}
    62	The graph $G_{V_{600}}$ has:
    63	\begin{itemize}\itemsep=2pt
    64	\item $|V|=120$ vertices,
    65	\item $|E|=720$ edges,
    66	\item every vertex has degree exactly $12$ (H$_4$ transitivity on
    67	  the vertex set forces \emph{uniformity} of the local structure;
    68	  the short-edge nearest-neighbour construction gives the
    69	  numerical degree $12$, verified by
    70	  \texttt{repro/verify\_kernel.py}),
    71	\item the graph is connected (verified numerically by counting
    72	  connected components of the short-edge adjacency matrix; the
    73	  classical 600-cell connectivity result is well known
    74	  in~\citep{CoxeterRegularPolytopes}).
    75	\end{itemize}
    76	All four facts are reproduced numerically:
    77	\texttt{repro/verify\_kernel.py} reports $|V|=120$, $|E|=720$,
    78	degree-min/max $=12/12$ (uniform), and one connected component.
    79	
    80	\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
    81	
    82	Choose any vertex $v_{0}$ as the pole; the H$_3$ subgroup of H$_4$
    83	fixing $v_{0}$ partitions the remaining $119$ vertices into shells
    84	of constant inner product with $v_{0}$. The nine canonical inner
    85	products are
    86	\begin{equation}\label{eq:shell_inner}
    87	\langle v, v_{0}\rangle
    88	\;\in\;
    89	\bigl\{1,\, \Ph/2,\, 1/2,\, 1/(2\Ph),\, 0,\,
    90	       -1/(2\Ph),\, -1/2,\, -\Ph/2,\, -1\bigr\},
    91	\end{equation}
    92	indexing shells $s = 0, 1, \ldots, 8$ from the pole to the
    93	antipode. The shell-size sequence is
    94	\begin{equation}\label{eq:shell_sizes}
    95	(|S_{0}|, |S_{1}|, \ldots, |S_{8}|)
    96	\;=\;
    97	(1,\ 12,\ 20,\ 12,\ 30,\ 12,\ 20,\ 12,\ 1).
    98	\end{equation}
    99	The middle shell $S_{4}$ has $30$ equatorial vertices forming the
   100	icosidodecahedral ring. The total is
   101	$1+12+20+12+30+12+20+12+1 = 120$, matching $|V|$. Reproduced
   102	verbatim by \texttt{repro/verify\_kernel.py:shell\_indices}.
   103	
   104	\paragraph{Antipodal symmetry.} The map $v \mapsto -v$ takes the
   105	shell-$s$ vertices to the shell-$(8-s)$ vertices: $s(-v) = 8 - s(v)$.
   106	The antipode $-v_{0}$ is the unique shell-$8$ vertex.
   107	
   108	\subsection{Inner-product check}\label{ssec:inner_product_check}
   109	
   110	The canonical short-edge criterion (Eq.~\eqref{eq:short_edge}) and
   111	the canonical shell inner products (Eq.~\eqref{eq:shell_inner})
   112	are jointly consistent: a vertex in shell $s_{1}$ is connected to a
   113	vertex in shell $s_{2}$ if and only if their pairwise inner product
   114	is $\Ph/2$, which restricts the admissible $(s_{1}, s_{2})$
   115	adjacency types to those compatible with the H$_3$ orbit structure.
   116	The numerically constructed graph respects this: every edge has
   117	inner product exactly $\Ph/2$ within machine precision (tolerance
   118	$10^{-10}$ in \texttt{repro/verify\_kernel.py:build\_short\_edge\_graph}).
   119	
   120	\subsection{What the substrate fixes, and what it does not}
   121	
   122	\begin{itemize}\itemsep=2pt
   123	\item \textbf{Fixed by the construction once $\Rsixhundred$ is
   124	  chosen}: $|V|=120$, uniform degree $12$, $9$-shell partition
   125	  $\{1,12,20,12,30,12,20,12,1\}$, antipodal symmetry, and the
   126	  Laplacian spectrum (\S\ref{sec:spectrum}).
   127	\item \textbf{Fixed by the design-level $\Ph^{-2}$ shift}:
   128	  $\Cph$ is positive definite with smallest eigenvalue $\Ph^{-2}$
   129	  (\S\ref{ssec:opnorm}); the operator-norm bound
   130	  $\|\Cph^{-1}\| = \Ph^{2}$.
   131	\item \textbf{Not fixed by this paper}: the choice of
   132	  $\Rsixhundred$ over the $24$-cell, $120$-cell, or other regular
   133	  4-polytopes / Coxeter substrates. The 600-cell choice is
   134	  post-hoc motivated by the empirical landings
   135	  (\S\ref{sec:passive_witness}, \S\ref{sec:active_witness}). A
   136	  formal substrate ablation is an
   137	  open build (\S\ref{sec:limitations}).
   138	\end{itemize}

 succeeded in 198ms:
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
    62	substrate/neuroscience correspondences plus six drug/sleep EEG
    63	signatures~\citep{SmartAriaChess2026}.
    64	
    65	\noindent\emph{Scope.}
    66	This paper presents an empirical \emph{operator witness}: a
    67	geometry-fixed response operator with operator shape held fixed
    68	across two disjoint-domain empirical landings (flavour physics
    69	and cortical neuroscience) with no kernel-shape retuning between
    70	regimes; the substrate $\Rsixhundred$ is post-hoc disclosed as
    71	the choice motivated by these landings, not selected by an
    72	independent criterion. It is \emph{not} a derivation of the
    73	$\Ph^{-2}$ shift from first principles, \emph{not} a uniqueness
    74	claim for $\Rsixhundred$ among regular 4-polytopes, \emph{not} a
    75	selection theorem on the companion adaptive-closure-transport
    76	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
    77	a model-preference claim against alternative kernels on either
    78	empirical landing (the b-anomaly AIC comparison and the aria-chess
    79	substrate-witness scope are documented in their own preprints and
    80	inherited verbatim here).
    81	
    82	\begin{abstract}
    83	We define a closure-response primitive $\Cph = L_M + \Ph^{-2} I$ on
    84	a closure substrate $M$ with corresponding Laplacian $L_M$ and
    85	$\Ph = (1+\sqrt 5)/2$, give the 600-cell graph $\Rsixhundred$ as
    86	the discrete instance shared by two empirical witnesses, and
    87	document its appearance as the same fixed operator (no shape
    88	retuning) in two independent empirical
    89	works: (i)~a five-dataset structural fit of the
    90	$b\to s\mu^{+}\mu^{-}$ angular anomaly with sign-uniform amplitude
    91	direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
    92	preregistered substrate witness against substrate/neuroscience
    93	signatures plus six drug/sleep EEG
    94	signatures~\citep{SmartAriaChess2026}. We
    95	include the numerical reproduction script
    96	(\texttt{repro/verify\_kernel.py}) that constructs $\Rsixhundred$
    97	from canonical generators, verifies the graph facts
    98	($|V|=120$, $|E|=720$, uniform degree~$12$, $9$-shell decomposition,
    99	Laplacian spectrum numerically matching closed-form $\mathbb{Z}[\Ph]$
   100	values, operator-norm identity $\|\Cph^{-1}\|=\Ph^{2}\approx 2.618$
   101	on the connected finite graph $\Rsixhundred$ where
   102	$\lambda_{\min}(L_M)=0$), and tests the discrete-to-continuum
   103	agreement at per-vertex Pearson correlation $0.976$ for the
   104	unweighted variant, above the two $\Ph$-cocycle weighted variants
   105	tested ($0.888$ geometric, $0.884$ arithmetic). Within the three
   106	tested variants the unweighted Laplacian ranks highest on the
   107	geometry-only criterion, reproducing the qualitative ranking
   108	established separately by b-anomaly's data $\chi^{2}$ comparison
   109	(the b-anomaly preprint flags that its data was looked at first
   110	and the geometry ranking verified afterward; the agreement is
   111	criterion-independent but historically non-blind, a caveat we
   112	inherit verbatim).
   113	
   114	\noindent\emph{(i) Operator definition and properties.}
   115	$\Cph = L_M + \Ph^{-2} I$ is positive definite for self-adjoint
   116	non-negative $L_M$ on a connected finite graph; smallest eigenvalue
   117	$\Ph^{-2} \approx 0.382$, operator norm
   118	$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$. The continuum projection
   119	in one coordinate $x$ is the closed-form Green's function
   120	$G(x) = (\Ph/2)\, e^{-|x|/\Ph}$, with decay scale $\Ph$.
   121	
   122	\noindent\emph{(ii) The 600-cell instance.}
   123	$\Rsixhundred$ has $120$ canonical unit vectors on $S^{3}$
   124	generated by three orbits ($8$~axis, $16$~half-integer,
   125	$96$~$\Ph$-mixed). H$_4$ transitivity forces uniform degree~$12$
   126	on the short-edge graph; the Laplacian has nine eigenvalue classes
   127	in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$ (Table
   128	\ref{tab:spectrum}, \S\ref{sec:substrate}).
   129	
   130	\noindent\emph{(iii) Discrete-to-continuum agreement.}
   131	Per-vertex Pearson correlation between the discrete response
   132	$\psi = \Cph^{-1} f$ for a localised source and the continuum
   133	prediction $G(\|v - v_{\mathrm{src}}\|)$ at each non-source
   134	vertex's chord distance: $0.976$ (unweighted Laplacian), $0.888$
   135	($\Ph$-geometric weights), $0.884$ ($\Ph$-arithmetic weights).
   136	Same source vertex, same fixed shift, no parameter fitting; the
   137	correlation is invariant under choice of source up to numerical
   138	precision (multi-source sweep, \S\ref{sec:limitations}).
   139	
   140	\noindent\emph{(iv) Two independent empirical witnesses.}
   141	(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
   142	$\Cph$ on the same $\Rsixhundred$ provides a sign-uniform
   143	$\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
   144	$b\to s\mu^{+}\mu^{-}$ angular anomaly across five public datasets
   145	(LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015 $B_s\to\phi$),
   146	with one fitted dimensionless amplitude per dataset and the kernel
   147	shape held fixed. (b)~Active regime,
   148	aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
   149	$\Rsixhundred$, augmented by a recurrent self-model layer with one
   150	condition-dependent self-injection coupling
   151	$\eta\in\{0,0.05,0.20\}$ and one substrate-pinned nonlinearity
   152	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
   153	degree, passes $17/18$ preregistered correspondences (frozen
   154	2026-04-18) at standard methodology and $18/18$ after a documented
   155	$N\!=\!20$ deep-dive on the residual high-variance
   156	$C\!\times\!P$ interaction (P4), plus $6/6$ literature-thresholded
   157	drug/sleep EEG signatures on a single deterministic seed.
   158	
   159	\noindent\emph{What we do not claim.}
   160	We do not derive the $\Ph^{-2}$ floor; it is a design-level
   161	stability clamp making $\Cph$ strictly positive definite. We do
   162	not claim $\Rsixhundred$ is the unique substrate consistent with
   163	either empirical landing. We do not claim the operator is the
   164	unique kernel shape consistent with the b-anomaly data
   165	(b-anomaly's free-width Gaussian alternative and Mode-B refit
   166	drift caveats are inherited verbatim) nor that the
   167	aria-chess substrate witness establishes a selection theorem on
   168	the adaptive-closure-transport 4-tuple. The structural scope of
   169	this paper is: \emph{one geometry-fixed operator on one fixed
   170	graph appears as the shared response primitive underneath two independent
   171	empirical works in two distinct regimes, with no shape retuning
   172	between them}.
   173	\end{abstract}
   174	
   175	% =====================================================================
   176	\input{sections/01_introduction.tex}
   177	\input{sections/02_definition.tex}
   178	\input{sections/03_substrate.tex}
   179	\input{sections/04_spectrum.tex}
   180	\input{sections/05_agreement.tex}
   181	\input{sections/06_passive_witness.tex}
   182	\input{sections/07_active_witness.tex}
   183	\input{sections/08_programme_home.tex}
   184	\input{sections/09_limitations.tex}
   185	\input{sections/10_conclusion.tex}
   186	% =====================================================================
   187	
   188	\section*{Reproducibility}
   189	The complete numerical verification (vertex construction,
   190	short-edge graph build, Laplacian spectrum, operator-norm bound,
   191	discrete-to-continuum correlation across three Laplacian variants)
   192	is reproducible from \texttt{repro/verify\_kernel.py} in this
   193	paper's bundle. No randomness, no fitted parameters: all numbers
   194	in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
   195	\S\ref{sec:agreement} are deterministic outputs of the script.
   196	The two empirical witness preprints
   197	(b-anomaly~\citep{SmartBAnomaly2026},
   198	aria-chess~\citep{SmartAriaChess2026}) carry their own
   199	reproducibility artifacts; this paper does not duplicate them.
   200	
   201	\bibliographystyle{plainnat}
   202	\bibliography{references}
   203	
   204	\end{document}

 succeeded in 188ms:
     1	% =====================================================================
     2	\section{Introduction}\label{sec:intro}
     3	% =====================================================================
     4	
     5	A response operator on a fixed graph, with no shape parameters
     6	tuned to any dataset, that simultaneously gives (i) a structural
     7	fit consistent with the $q^{2}$ shape of the
     8	$b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
     9	flavour-physics datasets in their passive linear-response regime,
    10	and (ii) eighteen preregistered substrate/neuroscience
    11	correspondences plus six drug/sleep EEG signatures in the active
    12	dynamical regime of a
    13	recurrent self-model layer above the same graph, deserves a separate
    14	preprint that names the operator, gives its construction in full,
    15	and threads the relationship between the two empirical landings
    16	without inheriting either's load-bearing claims. That is what this
    17	paper does.
    18	
    19	The operator is
    20	\begin{equation}\label{eq:cphi_intro}
    21	\Cph \;=\; L_M + \Ph^{-2} I,
    22	\qquad \Ph \;=\; (1+\sqrt 5)/2,
    23	\end{equation}
    24	where $M$ is a closure substrate (graph, simplicial complex, or
    25	projected coordinate) and $L_M$ is its Laplacian. The shift
    26	$\Ph^{-2} \approx 0.382$ regularises the inverse: for self-adjoint
    27	non-negative $L_M$ on a connected finite graph, $\Cph$ is strictly
    28	positive definite, the smallest eigenvalue is $\Ph^{-2}$, and the
    29	operator-norm bound is
    30	\begin{equation}\label{eq:opnorm_intro}
    31	\|\Cph^{-1}\| \;=\; 1/\Ph^{-2} \;=\; \Ph^{2} \;\approx\; 2.618.
    32	\end{equation}
    33	The continuum projection in one coordinate $x$ has a closed-form
    34	Green's function $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ with decay scale
    35	$\Ph$ (\S\ref{sec:definition}).
    36	
    37	The discrete substrate used by the two empirical witnesses is
    38	the 600-cell graph $\Rsixhundred$: $120$ unit vectors on $S^{3}$,
    39	generated by three standard coordinate families ($8$ axis vertices,
    40	$16$ half-integer vertices, $96$ $\Ph$-mixed vertices), connected by
    41	short edges $\langle v, w\rangle = \Ph/2$. The choice of this
    42	polytope is post-hoc motivated by the empirical landings
    43	(\S\ref{sec:limitations}); the construction itself is theorem-level
    44	rigorous. The graph has $|E|=720$ edges, uniform degree by H$_4$
    45	transitivity (with the value $12$ from the short-edge
    46	construction), a $9$-shell H$_3$ partition
    47	$\{1,12,20,12,30,12,20,12,1\}$, and antipodal symmetry
    48	$s(-v) = 8 - s(v)$. The Laplacian spectrum has nine eigenvalue
    49	classes in $\mathbb{Z}[\Ph]$ with multiplicities summing to $120$.
    50	All of these facts are reproduced numerically by
    51	\texttt{repro/verify\_kernel.py} from the canonical generators
    52	alone — no external data input.
    53	
    54	\subsection*{What this paper claims}
    55	
    56	We claim a single \emph{operator witness}: that one geometry-fixed
    57	operator, on one fixed graph, with no shape-parameter retuning
    58	between regimes, appears as the shared response primitive
    59	underneath two
    60	empirical works covering qualitatively distinct physical settings.
    61	
    62	\begin{enumerate}\itemsep=2pt
    63	\item \textbf{Operator definition is fixed by the construction.}
    64	  Once $\Rsixhundred$ is selected and the stability shift
    65	  $\Ph^{-2}$ is chosen, $\Cph$ is fully determined. No shape
    66	  parameter, no fitted threshold, no learned weight enters the
    67	  operator. The Laplacian spectrum, the operator-norm bound, and
    68	  the discrete-to-continuum agreement are computed (not fitted)
    69	  from the construction and reproduced in
    70	  \texttt{repro/verify\_kernel.py}.
    71	\item \textbf{Discrete-to-continuum agreement is empirical, not
    72	  postulated.} For a localised source at any vertex, the discrete
    73	  response $\psi = \Cph^{-1} f$ correlates per-vertex with the
    74	  continuum prediction $G(\|v - v_{\mathrm{src}}\|)$ at Pearson
    75	  $\rho = 0.976$ on the unweighted graph Laplacian. This is
    76	  numerical agreement between two independently-defined objects (a
    77	  120-dimensional discrete inverse and a continuum exponential
    78	  kernel), not a definitional identity.
    79	\item \textbf{Variant comparison among the three tested variants.}
    80	  Two $\Ph$-cocycle weighted Laplacian variants ($\Ph$-geometric,
    81	  $\Ph$-arithmetic edge weights via shell-grade exponents
    82	  $\omega_{+}(v) = \Ph^{\kappa(v)}$) score lower per-vertex
    83	  correlation: $0.888$ and $0.884$ respectively. Within the three
    84	  tested variants, the unweighted Laplacian ranks highest on the
    85	  geometry-only criterion. This reproduces,
    86	  on a different test, the qualitative ranking established
    87	  independently by the b-anomaly paper's data-$\chi^{2}$ comparison
    88	  (\S\ref{sec:passive_witness}).
    89	\item \textbf{Two independent empirical landings, same operator.}
    90	  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
    91	  same fixed $\Cph$ on the same $\Rsixhundred$ to describe the
    92	  $q^{2}$ shape of the $b\to s\mu^{+}\mu^{-}$ anomaly across five
    93	  public datasets, with one fitted dimensionless amplitude per
    94	  dataset and the kernel held fixed; sign uniformity holds in
    95	  $5/5$ datasets ($A>0$, $\Delta C_{9}^{\mathrm{eff}} < 0$).
    96	  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
    97	  same fixed $\Cph$ on the same $\Rsixhundred$, augmented by a
    98	  recurrent self-model layer above the substrate, to pass eighteen
    99	  preregistered substrate/neuroscience correspondences (frozen
   100	  2026-04-18) plus six drug/sleep EEG signatures.
   101	\end{enumerate}
   102	
   103	\subsection*{What this paper does \emph{not} claim}
   104	
   105	\begin{itemize}\itemsep=2pt
   106	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shift
   107	  $\Ph^{-2}$ is a design-level stability clamp that bounds
   108	  $\|\Cph^{-1}\|$ at $\Ph^{2}$. It is not derived from a closure
   109	  functional or a symmetry argument; we report its role as a
   110	  regularisation-of-mass scale.
   111	\item \emph{Not a uniqueness claim for $\Rsixhundred$.} Other
   112	  regular 4-polytopes (the $24$-cell, the $120$-cell), other
   113	  highly symmetric graphs, and continuum substrates are all
   114	  candidate $M$ for $\Cph = L_M + \Ph^{-2} I$. The 600-cell choice
   115	  is post-hoc motivated by the empirical landings; a formal
   116	  ablation against alternative substrates is an open build.
   117	\item \emph{Not a kernel-uniqueness claim on either empirical
   118	  landing.} The b-anomaly's free-width Gaussian alternative shows
   119	  that a free-width Gaussian charm-loop proxy fits the same five
   120	  datasets comparably in $\chi^{2}$ at the cost of one extra shape
   121	  parameter; the b-anomaly AIC comparison against
   122	  $\mathrm{FREE\_C9}$ (a constant Wilson-coefficient shift) is a
   123	  statistical tie on current data
   124	  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$).
   125	  Both caveats are inherited verbatim from the b-anomaly preprint.
   126	\item \emph{Not a selection theorem on the
   127	  ACT 4-tuple.} The companion adaptive-closure-transport
   128	  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
   129	  selection layer $(M, L_M, W, R_{\mathrm{hom}})$ in which $\Cph$
   130	  fills the response slot. Selection — Lyapunov $V(W)$ on the
   131	  reduced flow, edge-space decomposition under $2I$-equivariance,
   132	  full reduced-flow convergence — is left open in that paper and
   133	  is not delivered here.
   134	\item \emph{Not a circuit-level model on the active-regime side.}
   135	  The aria-chess preprint operates at the architectural-algorithmic
   136	  level above $\Cph$. We import its empirical results verbatim and
   137	  do not relitigate them here; their substrate-witness scope
   138	  applies.
   139	\end{itemize}
   140	
   141	\subsection*{Mapping from numerics to admissible claims}
   142	
   143	To keep this paper inside the operator-witness scope, we use the
   144	same claim-boundary discipline as the aria-chess
   145	preprint~\citep{SmartAriaChess2026}: numerical results
   146	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   147	$\mathcal C_{\mathrm{admissible}}$ by the rule
   148	\[
   149	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow
   150	        \mathcal C_{\mathrm{admissible}},
   151	\qquad
   152	\mathcal C_{\mathrm{admissible}}
   153	   \;=\;\{\text{`computed', `consistent with', `direction confirmed'}\}.
   154	\]
   155	A numerically computed quantity (the Laplacian spectrum, the
   156	operator-norm bound, the per-vertex correlation $0.976$) licenses
   157	a `computed'-type claim. Downstream empirical agreement using the
   158	fixed operator (sign uniformity in $5/5$ b-anomaly datasets, the
   159	aria-chess $17/18$ standard plus $18/18$ after the documented
   160	$N\!=\!20$ P4 deep-dive) licenses a `consistent
   161	with'-type claim. We never write
   162	`derives the kernel', `proves uniqueness', or `establishes
   163	selection'.
   164	
   165	\medskip
   166	\begin{center}
   167	\fbox{\parbox{0.92\linewidth}{\small
   168	\textbf{What is claimed / what is not.}\par
   169	\emph{Claimed:} a geometry-fixed response operator $\Cph$ on the
   170	600-cell graph, with computed spectrum, operator-norm bound, and
   171	discrete-to-continuum correlation; the same fixed operator appearing
   172	in two independent empirical works (b-anomaly five-dataset
   173	structural fit; aria-chess $17/18$ preregistered correspondences
   174	under the standard validation protocol and $18/18$ after the
   175	documented P4 $N\!=\!20$ deep-dive (thresholds unchanged), plus
   176	$6/6$ literature-thresholded companion EEG signatures) without
   177	shape-parameter retuning between regimes.\par
   178	\emph{Not claimed:} derivation of $\Ph^{-2}$; uniqueness of
   179	$\Rsixhundred$; uniqueness of the kernel shape on either empirical
   180	landing; a selection theorem on the ACT 4-tuple; that either
   181	empirical landing settles the underlying physics (flavour anomaly
   182	or consciousness) by the operator alone.
   183	}}
   184	\end{center}
   185	
   186	\subsection*{Layout}
   187	
   188	\S\ref{sec:definition} gives the operator definition, the positivity
   189	properties of $\Cph$, the operator-norm bound, and the continuum
   190	projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
   191	canonical generators, gives the graph facts, and the $9$-shell
   192	decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
   193	in $\mathbb{Z}[\Ph]$ with multiplicities, computed numerically.
   194	\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
   195	across three Laplacian variants. \S\ref{sec:passive_witness} and
   196	\S\ref{sec:active_witness} thread the two independent empirical
   197	witnesses (b-anomaly and aria-chess) at the operator level.
   198	\S\ref{sec:programme_home} positions $\Cph$ as the programme home
   199	for the polynomial-in-$L$ Lyapunov family that recurs across the
   200	Millennium drafts. \S\ref{sec:limitations} enumerates limitations
   201	in a five-move guard matrix. \S\ref{sec:conclusion} concludes.

 succeeded in 183ms:
     1	% =====================================================================
     2	\section{The closure-response operator}\label{sec:definition}
     3	% =====================================================================
     4	
     5	\subsection{Definition}
     6	
     7	Let $M$ be a closure substrate: a connected finite undirected graph
     8	$M=(V,E)$, a finite simplicial complex with chosen Laplacian, or a
     9	projected continuum coordinate. Let $L_M$ be the corresponding
    10	Laplacian (graph Laplacian $L = D - A$, simplicial Laplacian, or
    11	continuum operator $-\Delta$ with chosen boundary conditions).
    12	Let $\Ph = (1+\sqrt 5)/2$ be the golden ratio, with $\Ph^{-1} = \Ph - 1$
    13	and $\Ph^{-2} = 2 - \Ph \approx 0.381966$.
    14	
    15	The \emph{closure-response operator} is
    16	\begin{equation}\label{eq:cphi}
    17	\Cph \;=\; L_M + \Ph^{-2} I.
    18	\end{equation}
    19	For a non-negative localised source $f$ on $M$, the
    20	\emph{closure response field} is
    21	\begin{equation}\label{eq:psi}
    22	\psi \;=\; \Cph^{-1} f \;=\; (L_M + \Ph^{-2} I)^{-1} f.
    23	\end{equation}
    24	
    25	\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}
    26	
    27	The properties developed in \S\ref{ssec:positivity}--\S\ref{ssec:opnorm}
    28	require:
    29	
    30	\begin{itemize}\itemsep=2pt
    31	\item \textbf{(H1) Self-adjointness.} $L_M$ is self-adjoint on the
    32	  $L^{2}$ inner product on $M$ (with counting measure on a finite
    33	  graph, with Lebesgue measure with appropriate boundary conditions
    34	  in the continuum case).
    35	\item \textbf{(H2) Non-negativity.} $L_M \geq 0$ as a
    36	  quadratic form: $\langle f, L_M f\rangle \geq 0$ for all $f$.
    37	\item \textbf{(H3) Known spectral bottom.} On a finite graph, $M$
    38	  is connected (so the kernel of $L_M$ is exactly the constant
    39	  vector and $\lambda_{\min}(L_M) = 0$). In the continuum case,
    40	  the spectral bottom $\inf \sigma(L_M)$ is explicitly known on
    41	  the chosen domain (it equals $0$ for the full line; equals the
    42	  first Dirichlet eigenvalue $> 0$ on a bounded Dirichlet
    43	  interval). The full-line case has $\inf \sigma(L_M) = 0$ as
    44	  spectral bottom but not as an eigenvalue, which is sufficient
    45	  for the operator-norm identity in
    46	  \S\ref{ssec:opnorm}; H3 does not require a finite-dimensional
    47	  zero eigenspace.
    48	\end{itemize}
    49	
    50	Three concrete settings illustrate the hypothesis class:
    51	\begin{itemize}\itemsep=2pt
    52	\item the standard combinatorial Laplacian on a connected finite
    53	  undirected graph (the 600-cell case, $\lambda_{\min}(L_M) = 0$);
    54	\item the continuum $L = -d^{2}/dx^{2}$ on the full line with
    55	  decay-at-infinity (spectral bottom $\inf \sigma(L_M) = 0$,
    56	  not attained as an eigenvalue; used for the closed-form Green's
    57	  function in \S\ref{ssec:continuum});
    58	\item the continuum $L = -d^{2}/dx^{2}$ on a bounded interval
    59	  with Dirichlet boundary conditions ($\lambda_{\min}(L_M) > 0$).
    60	\end{itemize}
    61	Substrates outside this class — projected coordinates with
    62	non-standard boundaries, weighted Laplacians whose weight function
    63	is unbounded, or operators with negative spectrum — require their
    64	own analysis, which we do not give here.
    65	
    66	\subsection{Positive definiteness}\label{ssec:positivity}
    67	
    68	Under (H1)--(H3) on a finite connected graph, $L_M$ has a smallest
    69	eigenvalue $\lambda_{\min}(L_M) = 0$ with one-dimensional
    70	eigenspace (the constant vector). For $\Cph = L_M + \Ph^{-2} I$,
    71	\[
    72	\lambda_{\min}(\Cph) \;=\; \lambda_{\min}(L_M) + \Ph^{-2}
    73	                    \;=\; \Ph^{-2} \;>\; 0,
    74	\]
    75	so $\Cph$ is strictly positive definite and $\Cph^{-1}$ is
    76	well-defined and bounded.
    77	
    78	\subsection{Operator-norm bound}\label{ssec:opnorm}
    79	
    80	The operator norm of $\Cph^{-1}$ is the reciprocal of the smallest
    81	eigenvalue of $\Cph$:
    82	\begin{equation}\label{eq:opnorm}
    83	\|\Cph^{-1}\| \;=\; 1/\lambda_{\min}(\Cph)
    84	              \;=\; 1/(\lambda_{\min}(L_M) + \Ph^{-2}).
    85	\end{equation}
    86	On any substrate where $\lambda_{\min}(L_M) = 0$ (e.g.\ the
    87	connected finite graph $\Rsixhundred$, or the full-line continuum
    88	case used in \S\ref{ssec:continuum}), this reduces to the identity
    89	\begin{equation}\label{eq:opnorm_zero_mode}
    90	\|\Cph^{-1}\| \;=\; \Ph^{2} \;\approx\; 2.618034.
    91	\end{equation}
    92	On substrates where $\lambda_{\min}(L_M) > 0$ (e.g.\ Dirichlet
    93	intervals), Eq.~\eqref{eq:opnorm} gives the strict inequality
    94	$\|\Cph^{-1}\| < \Ph^{2}$. The response-amplification ceiling is,
    95	in either case, $\|\psi\|_{2} \leq \|\Cph^{-1}\|\, \|f\|_{2}$. On
    96	substrates with $\lambda_{\min}(L_M) > 0$ a finite ceiling is
    97	already guaranteed by the Dirichlet structure alone; on substrates
    98	with $\lambda_{\min}(L_M) = 0$ (the cases of interest here) the
    99	shift $\Ph^{-2}$ is what guarantees a finite ceiling and pins it
   100	at $\Ph^{2}$. Numerically reproduced as $\|\Cph^{-1}\| =
   101	2.618034$ on $\Rsixhundred$ (\texttt{repro/verify\_kernel.py},
   102	\S\ref{ssec:opnorm_check}); this matches the closed-form $\Ph^{2}$
   103	to machine precision.
   104	
   105	\subsection{Continuum projection}\label{ssec:continuum}
   106	
   107	In one projected coordinate $x \in \mathbb{R}$ with
   108	$L_{\Ph} = -d^{2}/dx^{2} + \Ph^{-2}$, the Green's function
   109	$G(x)$ satisfies $L_{\Ph} G = \delta_{0}$ and is the closed-form
   110	exponential
   111	\begin{equation}\label{eq:green_continuum}
   112	G(x) \;=\; \frac{\Ph}{2}\, e^{-|x|/\Ph}.
   113	\end{equation}
   114	The decay scale is $\Ph$ — the same constant that appears in the
   115	shift, by construction. Normalised, the kernel is
   116	$\kappa(x) = e^{-|x|/\Ph}$ with unit value at the source.
   117	
   118	This continuum Green's function is the comparison object for the
   119	discrete-to-continuum agreement test (\S\ref{sec:agreement}):
   120	the discrete response $\psi(v) = \Cph^{-1} f(v)$ at a vertex $v$ at
   121	chord distance $\|v - v_{\mathrm{src}}\|$ from a localised source
   122	is compared to $G(\|v - v_{\mathrm{src}}\|)$.
   123	
   124	\subsection{Disclosure: $\Ph^{-2}$ is a design-level shift}
   125	
   126	The shift $\Ph^{-2}$ is chosen so that:
   127	\begin{enumerate}\itemsep=2pt
   128	\item $\Cph$ is strictly positive definite (the smallest eigenvalue
   129	  is exactly $\Ph^{-2}$);
   130	\item both the operator-norm bound $\|\Cph^{-1}\| = \Ph^{2}$ and
   131	  the continuum decay scale $\Ph$ (Eq.~\eqref{eq:green_continuum})
   132	  are fixed by the single design choice $\Ph^{-2}$, giving a single
   133	  dimensional parameter throughout the operator;
   134	\item the continuum projection (Eq.~\eqref{eq:green_continuum})
   135	  has decay scale $\Ph$, not a free length parameter.
   136	\end{enumerate}
   137	We do \emph{not} derive $\Ph^{-2}$ from a closure functional or
   138	symmetry argument. It is a design-level choice motivated by
   139	(1)--(3); we report this explicitly and treat formal derivation as
   140	an open build (\S\ref{sec:limitations}). The companion
   141	adaptive-closure-transport
   142	preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
   143	selection-layer dynamics over $W$-space that would, if delivered,
   144	constrain the shift further; that derivation is not delivered
   145	there or here.

exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/04_spectrum.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/05_agreement.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/06_passive_witness.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/07_active_witness.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 251ms:
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
    28	$0$            & machine zero ($\sim 10^{-15}$)         & $1$ \\
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

 succeeded in 238ms:
     1	% =====================================================================
     2	\section{Discrete-to-continuum agreement}\label{sec:agreement}
     3	% =====================================================================
     4	
     5	This is the central geometric diagnostic of the paper: the
     6	discrete response $\psi = \Cph^{-1} f$ on $\Rsixhundred$ for a
     7	localised source has high per-vertex Pearson correlation in radial
     8	shape with the continuum kernel
     9	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the vertex's chord distance from
    10	the source. Pearson correlation is a shape similarity statistic, not
    11	an equality claim. We give the test, the numerical result, and a variant
    12	comparison in which the unweighted Laplacian ranks highest among
    13	the three tested variants (unweighted, $\Ph$-geometric weighted,
    14	$\Ph$-arithmetic weighted).
    15	
    16	\subsection{The test}\label{ssec:test}
    17	
    18	Pick a pole vertex $v_{0}$ (we use the canonical $+x_{0}$ axis
    19	vertex). Set $f = e_{v_{0}}$ (the unit vector at $v_{0}$, all
    20	other entries zero). Compute
    21	\[
    22	\psi \;=\; \Cph^{-1} f \;=\; (\Lop + \Ph^{-2} I)^{-1} e_{v_{0}}
    23	\]
    24	by direct linear solve (no eigenmode truncation). For each vertex
    25	$v \in V$, compute the Euclidean chord distance
    26	$x(v) = \|v - v_{0}\|$ and the continuum prediction
    27	\[
    28	G(x(v)) \;=\; (\Ph/2)\,\exp(-\,x(v)/\Ph).
    29	\]
    30	The agreement criterion is the Pearson correlation between
    31	$\psi(v)$ and $G(x(v))$ across $v \in V \setminus \{v_{0}\}$ (the
    32	source itself is excluded, since the discrete response there is
    33	trivially the diagonal of $\Cph^{-1}$ and the chord distance is
    34	zero, both degenerate for the comparison).
    35	
    36	\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
    37	
    38	\texttt{repro/verify\_kernel.py:variant\_correlation} returns:
    39	\begin{itemize}\itemsep=2pt
    40	\item \textbf{Multiplicity-weighted per-vertex Pearson correlation
    41	  over shell-constant responses}: $\rho = 0.976$. (See
    42	  \S\ref{ssec:result_unweighted} below: $\psi$ is shell-constant
    43	  to machine precision under H$_3$-fixed source, so the per-vertex
    44	  test is mathematically a multiplicity-weighted shell-radius
    45	  correlation rather than $119$ independent radial samples.)
    46	\item \textbf{Shell-mean Pearson correlation}: $\rho = 0.923$
    47	  (averaging $\psi(v)$ over each H$_3$ shell first, then
    48	  correlating the $9$-point shell-mean trajectory with the
    49	  continuum prediction at the shell mean radius).
    50	\end{itemize}
    51	The two correlations measure the same shell-radius fact at
    52	different weightings and with different source-vertex conventions:
    53	\begin{itemize}\itemsep=2pt
    54	\item Per-vertex test: $|V|-1 = 119$ data points (every
    55	  non-source vertex), source $v_{0}$ \emph{excluded} (the discrete
    56	  response there is the diagonal of $\Cph^{-1}$ and the chord
    57	  distance is $0$, both degenerate for the comparison).
    58	\item Shell-mean test: $9$ data points (one per H$_3$ shell);
    59	  shell $0$ contains only the source vertex, so it is included
    60	  on the shell-mean side and contributes a single
    61	  ($\psi(v_{0}), G(0)$) point.
    62	\end{itemize}
    63	On the unweighted 600-cell graph with an H$_3$-fixed source,
    64	$\psi$ is shell-constant up to numerical precision — the
    65	within-shell standard deviations are at machine precision
    66	($\sim 10^{-16}$). The two tests therefore differ in weighting and
    67	source convention, not in noise content: the per-vertex test
    68	weights each shell by its multiplicity
    69	($\{12, 20, 12, 30, 12, 20, 12, 1\}$ for the non-source shells)
    70	and excludes the source vertex, while the shell-mean test gives
    71	equal weight to every shell and includes the source. The
    72	per-vertex test is the headline agreement criterion in this paper.
    73	
    74	\subsection{Variant comparison}\label{ssec:variant_comparison}
    75	
    76	Two $\Ph$-cocycle weighted Laplacian variants are tested as
    77	controls:
    78	
    79	\begin{itemize}\itemsep=2pt
    80	\item \textbf{$\Ph$-geometric weights}: edge weight
    81	  $w_{vw} = \sqrt{\omega_{+}(v)\,\omega_{+}(w)}$ with vertex weight
    82	  $\omega_{+}(v) = \Ph^{\kappa(v)}$, where $\kappa(v) \in \{0,\ldots,8\}$
    83	  is the shell index of $v$.
    84	\item \textbf{$\Ph$-arithmetic weights}: edge weight
    85	  $w_{vw} = \tfrac12[\omega_{+}(v) + \omega_{+}(w)]$ with the same
    86	  $\omega_{+}$.
    87	\end{itemize}
    88	The weighted Laplacian is then
    89	$L_{w} = D_{w} - A_{w}$ where $A_{w}$ is the weighted adjacency.
    90	We re-run the discrete-to-continuum test on each variant.
    91	
    92	\begin{table}[ht]
    93	\centering
    94	\small
    95	\caption{Per-vertex and shell-mean Pearson correlations between the
    96	discrete response $\psi = (L_{w} + \Ph^{-2} I)^{-1} e_{v_{0}}$
    97	and the continuum prediction $G(\|v - v_{0}\|)$ for three
    98	Laplacian variants ($L_{w}$ unweighted or $\Ph$-cocycle weighted).
    99	Computed by \texttt{repro/verify\_kernel.py:variant\_correlation}.}
   100	\label{tab:variant_correlation}
   101	\begin{tabular}{l c c}
   102	\toprule
   103	Variant            & Per-vertex correlation & Shell-mean correlation \\
   104	\midrule
   105	\textbf{Unweighted}     & $\mathbf{0.976}$ & $\mathbf{0.923}$ \\
   106	$\Ph$-geometric weighted    & $0.888$  & $0.880$ \\
   107	$\Ph$-arithmetic weighted   & $0.884$  & $0.878$ \\
   108	\bottomrule
   109	\end{tabular}
   110	\end{table}
   111	
   112	\textbf{Reading.} Among the three tested variants, the unweighted
   113	Laplacian ranks highest on both reported criteria
   114	($+0.088$ per-vertex over the next variant, $+0.044$ shell-mean).
   115	This reproduces, on a different test, the qualitative ranking the
   116	b-anomaly paper~\citep{SmartBAnomaly2026} established
   117	independently against its data-$\chi^{2}$ criterion
   118	on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
   119	b-anomaly numbers). Two independent criteria — geometry-only
   120	correlation here, and angular-anomaly $\chi^{2}$ in b-anomaly —
   121	agree on which of the three tested variants ranks highest. We do not claim
   122	this is a uniqueness or blind-selection result; we report it as a
   123	two-criterion agreement on the highest-ranked tested variant (the
   124	b-anomaly paper's own caveat that the data was looked at first
   125	and the geometry criterion verified afterward is inherited
   126	verbatim).
   127	
   128	\subsection{What the agreement does and does not establish}
   129	
   130	\paragraph{Does establish.} A geometric agreement: the discrete
   131	response of a fixed-shift Green operator on a fixed graph
   132	correlates per-vertex in radial shape, at Pearson $0.976$, with
   133	the closed-form continuum exponential at the same length scale
   134	$\Ph$. This is a non-trivial Pearson correlation between
   135	separately evaluated discrete and continuum Green responses
   136	sharing the same design-level scale $\Ph^{-2}$: (i) the discrete
   137	inverse of a $120\times 120$ Laplacian-plus-shift matrix; and
   138	(ii) a one-dimensional continuum exponential. The $\Ph$-mediated
   139	agreement is an empirical fact about the chosen substrate and
   140	shift, computed (not fitted) by the verification script.
   141	
   142	\paragraph{Does not establish.} Operator uniqueness on either
   143	empirical landing — the b-anomaly paper documents a free-width
   144	Gaussian alternative that fits comparably in $\chi^{2}$ at the
   145	cost of one extra shape parameter, and the aria-chess preprint
   146	does not run a substrate ablation; both caveats are inherited
   147	verbatim. The agreement also does not establish that
   148	$\Rsixhundred$ is the unique discrete substrate with this
   149	property; the $24$-cell, $120$-cell, and other H$_n$ Coxeter
   150	graphs would need to be tested on the same correlation criterion
   151	to make any comparative claim, and a formal substrate ablation is
   152	an open build (\S\ref{sec:limitations}).

 succeeded in 270ms:
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
    64	\subsection{What the structural fit reports}
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
    76	\item \textbf{Cross-channel ratio.} The b-anomaly README reports
    77	  the basis amplification (the predicted Krüger--Matias $P$-basis
    78	  vs $S$-basis factor $\sim 2.2$~\citep{KrugerMatias2005}) as
    79	  partly explanatory for the $B\to K^{*}$ vs $B_{s}\!\to\!\phi$
    80	  amplitude gap. Working through the explicit arithmetic with
    81	  $B\to K^{*}$ best-fit $A_{P} \approx 1.14$: the basis-corrected
    82	  prediction for $B_{s}\!\to\!\phi$ is
    83	  $A_{P} \cdot 2.2 \approx 2.5$; the observed $B_{s}\!\to\!\phi$
    84	  amplitude is $A \approx 4.98$, leaving an unresolved amplitude
    85	  excess of about a factor two above the basis-corrected
    86	  prediction. The b-anomaly preprint reports this residual as an
    87	  open item, not a discharge.
    88	\item \textbf{Geometry-first variant test.} Of three discrete
    89	  Laplacian variants on $\Rsixhundred$ (unweighted,
    90	  $\Ph$-geometric weighted, $\Ph$-arithmetic weighted), the
    91	  unweighted choice ranks highest on both a pure-geometry
    92	  criterion (correlation $0.997$ with the continuum kernel under
    93	  the b-anomaly preprint's $q^{2}$/shell-projection geometry
    94	  metric, §3.4 of~\citep{SmartBAnomaly2026} — \emph{not} this
    95	  paper's per-vertex test, whose unweighted score is $0.976$;
    96	  the two metrics differ in what is correlated) and the LHCb~2025
    97	  data $\chi^{2}$ ($\chi^{2}=13.555$). The two criteria agree on
    98	  the variant ranking — a two-criterion agreement on the same
    99	  fixed operator.
   100	\end{itemize}
   101	
   102	\subsection{What the structural fit does \emph{not} establish}
   103	
   104	The b-anomaly preprint is explicit about the following caveats,
   105	which we inherit verbatim:
   106	
   107	\begin{itemize}\itemsep=2pt
   108	\item \textbf{AIC tie on current data.} On Akaike model comparison,
   109	  $\Cph$-derived $\kappa_{V_{600}}$ and a constant Wilson-coefficient
   110	  shift ($\mathrm{FREE\_C9}$, also $k=1$) are statistically
   111	  indistinguishable: stacked AIC weights
   112	  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
   113	  Current data cannot resolve the model comparison. AIC is blind
   114	  to the universality / shape-prediction claim itself, but it is
   115	  decisive about whether the shape is forced by data: it is not.
   116	\item \textbf{Free-width Gaussian alternative.} A free-width
   117	  Gaussian charm-loop proxy fits the same five datasets comparably
   118	  in $\chi^{2}$ at the cost of one extra shape parameter; $\Cph$
   119	  is not the unique $q^{2}$ shape consistent with the anomaly.
   120	\item \textbf{Mode-B drift (linearised-to-non-linear refit).} An
   121	  earlier analysis the b-anomaly project labels Mode-B
   122	  (linearised) gave a stronger preference
   123	  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that did not survive
   124	  the subsequent non-linear refit; the $+2.77$-AIC-unit drift
   125	  between Mode-B (linearised) and the non-linear refit is the
   126	  largest single methodological uncertainty in the b-anomaly
   127	  project.
   128	\item \textbf{Look-elsewhere on the variant test.} The b-anomaly
   129	  preprint's limitations section~\citep{SmartBAnomaly2026}
   130	  acknowledges that the LHCb~2025 data was looked at first, and
   131	  only later was the agreement of the data-$\chi^{2}$ ranking with
   132	  the pure-geometry ranking verified. (The b-anomaly README
   133	  emphasises that the geometry-only criterion is independent of
   134	  the LHCb data; the historical non-blindness is in the project's
   135	  ordering, not in the criterion.) The two-criterion agreement is
   136	  criterion-independent but not historically blind.
   137	\end{itemize}
   138	
   139	\subsection{Reading at the operator level}
   140	
   141	The b-anomaly result is the \emph{passive-regime} empirical
   142	witness for $\Cph$ on $\Rsixhundred$: a single linear response
   143	$\psi = \Cph^{-1} f$, projected to the $q^{2}$ axis through a
   144	fixed discrete-to-momentum projection, gives a sign-uniform
   145	structural fit consistent with the $b\to s\mu^{+}\mu^{-}$ angular
   146	anomaly across five independent measurements without shape
   147	retuning. This does
   148	not establish the kernel as theorem-grade physics on the flavour
   149	side (the AIC tie, the free-width Gaussian alternative, and the
   150	Mode-B linearised-to-non-linear refit drift prevent that). It
   151	does support, at the operator-witness level, the inherited reading
   152	that the same fixed $\Cph$ on the same fixed $\Rsixhundred$ is
   153	consistent with one of two independent empirical landings without
   154	parameter retuning. The
   155	second landing is in \S\ref{sec:active_witness}.

 succeeded in 272ms:
     1	% =====================================================================
     2	\section{Active-regime witness: aria-chess}\label{sec:active_witness}
     3	% =====================================================================
     4	
     5	This section threads the second independent empirical landing of
     6	$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
     7	summarise here only what the operator-witness narrative requires
     8	and inherit the preprint's substrate-witness scope verbatim.
     9	
    10	\subsection{What aria-chess tests}\label{ssec:aria_setup}
    11	
    12	The aria-chess preprint adds a recurrent self-model layer above
    13	the same $\Cph$ on the same $\Rsixhundred$. The architecture
    14	introduces:
    15	\begin{itemize}\itemsep=2pt
    16	\item One \emph{condition-dependent} self-injection coupling
    17	  $\eta \in \{0, 0.05, 0.20\}$ (PROPOFOL, SLEEP\_N3,
    18	  WAKE/RECOVERY) that controls the strength of the recurrent
    19	  feedback;
    20	\item One \emph{substrate-pinned} nonlinearity
    21	  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
    22	  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
    23	  $k=12$ is not a free hyperparameter; it is the substrate's
    24	  average degree.
    25	\item Condition-specific \emph{biologically-motivated} stimulus
    26	  models (slow oscillation + spindles + K-complexes for SLEEP\_N3,
    27	  AR(1) noise + tonic shell + attention episodes for WAKE,
    28	  low-amplitude tonic noise for PROPOFOL). These are
    29	  biologically-motivated design choices, not measurement-fits to
    30	  subject-level EEG data.
    31	\end{itemize}
    32	The kernel parameter $\Ph^{-2}$ is \emph{not retuned} between
    33	b-anomaly and aria-chess; the same fixed shift used in the
    34	flavour-physics structural fit is used in the cortical substrate
    35	witness.
    36	
    37	\subsection{Eighteen preregistered correspondences}
    38	
    39	Eighteen quantitative predictions (P1--P18) were locked on
    40	2026-04-18 in the aria-chess preprint's
    41	\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any
    42	validation run. Each prediction has a specific numerical claim, a
    43	falsifiable threshold, and a named validation script. The
    44	preregistered tally as reported in~\citep{SmartAriaChess2026}:
    45	
    46	\begin{itemize}\itemsep=2pt
    47	\item $17/18$ at standard validation methodology ($5$-seed
    48	  cascade block plus state-reset protocol);
    49	\item $18/18$ after a documented $N\!=\!20$ deep-dive on the
    50	  residual high-variance interaction $C\!\times\!P$ (P4: bootstrap
    51	  point estimate $+0.190$, $95\%$ CI $[+0.143, +0.239]$,
    52	  $0/2000$ resamples at-or-below zero, reported as $0.0000$).
    53	\item No preregistered threshold has been modified.
    54	\end{itemize}
    55	The aria-chess preprint reports this as methodology refinement
    56	(documented seed-count increase on a high-per-seed-variance
    57	interaction term), \emph{not} as a threshold change. We inherit the
    58	reading verbatim.
    59	
    60	\subsection{Six drug/sleep EEG signatures}
    61	
    62	On a single deterministic substrate trajectory at seed~$42$, the
    63	aria-chess preprint reports six biological signatures testing
    64	against literature-derived thresholds:
    65	
    66	\begin{itemize}\itemsep=2pt
    67	\item \textbf{Wake cortical-avalanche $\alpha$}: $\alpha = 2.252$,
    68	  $95\%$ CI $[1.82, 2.86]$, $R^{2}=0.956$ — the WAKE confidence
    69	  interval overlaps both the Sleep-EDFx EEG CI $[2.50, 2.53]$
    70	  ($n=30$ subjects) and aria-chess's prior cascade pipeline CI
    71	  $[2.73, 3.25]$ pairwise (the Sleep-EDFx and prior-pipeline
    72	  intervals do not overlap each other; the WAKE interval is the
    73	  pairwise common ground).
    74	\item \textbf{NREM-N3 phenomenal-intensity variance ratio}:
    75	  $0.463\!\times$ wake (predicted $\sim 0.365$, threshold $<0.70$).
    76	\item \textbf{Propofol modality-switching ratio}: $1.83\!\times$
    77	  wake (threshold $\in [1.5, 5.0]$, empirical reference
    78	  $2.96\!\times$ from OpenNeuro \texttt{ds005620}).
    79	\item \textbf{Propofol continuity drop}: $+0.066$
    80	  (threshold $> 0.020$).
    81	\item \textbf{Propofol $\Phi$ collapse}: $0.33\!\times$ wake (IIT
    82	  direction confirmed; $\Phi$-proxy not full IIT).
    83	\item \textbf{Recovery deterministic identity to wake}: under the
    84	  WAKE stimulus protocol, the RECOVERY trajectory is bit-identical
    85	  to the WAKE trajectory.
    86	\end{itemize}
    87	
    88	\subsection{Cross-domain selectivity}
    89	
    90	\begin{itemize}\itemsep=2pt
    91	\item \textbf{Chess pattern recognition (P9--P13)}: $32$ chess
    92	  positions across $4$ categories on $8$-D V2 features; under the
    93	  disclosed leave-one-out / state-reset refinement of the
    94	  preregistered $\geq +15$pp substrate-lift test (the original
    95	  prereg used $5$-fold cross-validation; the LOO/state-reset
    96	  protocol is documented in the aria-chess
    97	  preprint~\citep{SmartAriaChess2026}), substrate routing lifts
    98	  classification at canonical depth $n=25$ ticks from raw
    99	  $53.1\%$ to substrate-routed $93.8\%$ ($+40.6$pp), above the
   100	  preregistered $\geq +15$pp floor.
   101	\item \textbf{Conversation pattern recognition (P14--P16)}:
   102	  $64$ utterances, $8$ categories; raw classification $87.5\%$,
   103	  substrate-routed lift $-4.4$pp (within the preregistered
   104	  neutrality band $|\cdot| < 10$pp). The substrate is selectively
   105	  amplifying in tasks where raw features are ambiguous and
   106	  approximately neutral when raw features are already
   107	  discriminative.
   108	\item \textbf{HCP brain functional connectivity (P17--P18)}:
   109	  full-cohort descriptive statistics on $n=1003$ subjects show
   110	  ARIA's $H_4$-transitive structure at $-11.58\sigma$ on degree
   111	  homogeneity, $+79.78\sigma$ on raw participation ratio (with
   112	  node-count caveat: ARIA $|V|=120$ vs HCP ICA-50 $|V|=50$), and
   113	  $+6.80\sigma$ on clustering coefficient. ARIA's degree std is
   114	  $0$ by H$_4$ transitivity (a theorem), $11.58$ standard
   115	  deviations below the HCP biological cohort.
   116	\end{itemize}
   117	
   118	\subsection{Reading at the operator level}
   119	
   120	The aria-chess result is the \emph{active-regime} empirical
   121	witness for $\Cph$ on $\Rsixhundred$. The recurrent self-model
   122	layer above $\Cph$ uses one condition-dependent coupling and one
   123	substrate-pinned nonlinearity at the graph's average degree
   124	$k=12$; no other \emph{kernel-shape} parameter enters. Above the
   125	operator, aria-chess inherits its own dynamical and stimulus
   126	constants (e.g.\ a fixed dynamical decay, fixed cascade gains,
   127	condition-specific biologically-motivated stimulus models); these
   128	are documented in the aria-chess preprint and are not retuned in
   129	this paper. The kernel shift $\Ph^{-2}$ is not retuned between
   130	b-anomaly and aria-chess. Under those design choices, the same
   131	fixed $\Cph$ on the same $\Rsixhundred$ is consistent with the
   132	aria-chess active-regime tally (frozen 2026-04-18): $17/18$
   133	preregistered cortical correspondences under the standard
   134	validation protocol, $18/18$ after the documented $N\!=\!20$ P4
   135	deep-dive (thresholds unchanged), plus six literature-thresholded
   136	EEG drug/sleep signatures.
   137	
   138	The aria-chess preprint stays inside substrate-witness scope: it
   139	does not claim the substrate \emph{is} consciousness, does not
   140	claim 600-cell uniqueness among regular 4-polytopes, and does not
   141	deliver a selection theorem on the ACT 4-tuple. We inherit the
   142	scope verbatim. What we add at the operator level is the
   143	observation that the same fixed $\Cph$ — under no shape-parameter
   144	retuning between regimes — is the shared response primitive
   145	underneath both empirical landings (the b-anomaly $q^{2}$
   146	projection above $\Cph$ and the aria-chess recurrent self-model
   147	layer above $\Cph$ are distinct above-operator constructions; the
   148	operator below them is the same).
   149	
   150	\subsection{Two-witness structure}
   151	
   152	\begin{table}[ht]
   153	\centering
   154	\small
   155	\caption{Two independent empirical landings of $\Cph$ on
   156	$\Rsixhundred$, with no shape retuning between regimes.}
   157	\label{tab:two_witness}
   158	\begin{tabular}{p{0.22\linewidth} p{0.36\linewidth} p{0.36\linewidth}}
   159	\toprule
   160	& Passive regime & Active regime \\
   161	\midrule
   162	Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
   163	Domain             & flavour physics                    & cortical neuroscience \\
   164	Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) & prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
   165	Operator           & same fixed $\Cph$                  & same fixed $\Cph$ \\
   166	Substrate          & same $\Rsixhundred$                & same $\Rsixhundred$ \\
   167	Shift $\Ph^{-2}$   & not retuned                        & not retuned \\
   168	Headline           & $5/5$ sign uniformity              & $17/18$ standard, $18/18$ after P4 deep-dive; $6/6$ EEG \\
   169	Kernel-shape free params & 0                            & 0 \\
   170	Other free params  & 1 amplitude $A$ per dataset        & 1 coupling $\eta$ per condition; v4 stimulus protocols \\
   171	Caveat             & AIC tie; free-width Gaussian alt.\ & single-seed EEG; no polytope ablation \\
   172	\bottomrule
   173	\end{tabular}
   174	\end{table}
   175	
   176	The two witnesses share, by design, exactly the geometry-fixed
   177	operator: the same $\Cph$, the same substrate $\Rsixhundred$, and
   178	the same shift $\Ph^{-2}$. They share no fitted parameter,
   179	threshold, dataset, or methodological choice above the operator
   180	level. The b-anomaly amplitude $A$ is fitted to flavour-physics
   181	$q^{2}$ shape, dataset by dataset; the aria-chess coupling $\eta$
   182	is fixed by experimental condition (PROPOFOL/SLEEP/WAKE), not by
   183	neural data; the v4 stimulus protocols are biologically motivated,
   184	not subject-fit. Independence in this paper is independence at
   185	the empirical layer above the shared operator.

exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/08_programme_home.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/09_limitations.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/sections/10_conclusion.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/paper/references.bib' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 222ms:
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
    21	  this programme). A cascade closure functional of the schematic
    22	  form $F_{\mathrm{filt}}(x) = \tfrac12 \langle x,
    23	  p_{\mathrm{fix}}(L)^{2} x\rangle$ for some polynomial
    24	  $p_{\mathrm{fix}}$ targeting $V_{\mathrm{fix}}$; the explicit
    25	  form, properties, and any classification claim are reported in
    26	  the forthcoming artifact, not here. This is a non-load-bearing
    27	  programme note.
    28	\item \textbf{YM cascade gap operator} (forthcoming YM artifact in
    29	  this programme). A $\Cph$-style mass-regularised Laplacian on
    30	  $\Rsixhundred$ is the schematic role; the explicit construction
    31	  and properties are reported in the forthcoming artifact, not
    32	  here. This is a non-load-bearing programme note.
    33	\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
    34	  The homeostatic regulariser
    35	  $R_{\mathrm{hom}}$ in the 4-tuple $(M, L_M, W, R_{\mathrm{hom}})$,
    36	  programme-positioned as a member of the same polynomial-in-$L$
    37	  family.
    38	\end{itemize}
    39	
    40	These are schematic programme placements; no family-classification
    41	theorem is used here. Each named operator is in a
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
    86	in this paper provide external consistency checks on the
    87	\emph{response} primitive without reducing or addressing the
    88	selection gap.
    89	
    90	\subsection{What this paper closes vs leaves open}
    91	
    92	\paragraph{Closes (at the operator-witness level).}
    93	\begin{itemize}\itemsep=2pt
    94	\item The operator $\Cph$ is well-defined and positive definite
    95	  on any $(M, L_M)$ satisfying (H1)--(H3); the operator-norm
    96	  identity $\|\Cph^{-1}\| = \Ph^{2}$ holds whenever
    97	  $\lambda_{\min}(L_M) = 0$ (e.g.\ on a connected finite graph
    98	  with the standard combinatorial Laplacian). On substrates where
    99	  $\lambda_{\min}(L_M) > 0$ (e.g.\ Dirichlet-boundary continuum
   100	  cases) the bound $\|\Cph^{-1}\| \leq \Ph^{2}$ holds and is
   101	  generally strict (\S\ref{sec:definition}).
   102	\item The 600-cell instance $\Rsixhundred$ has the construction
   103	  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
   104	  Table~\ref{tab:spectrum}, both reproduced numerically
   105	  (\texttt{repro/verify\_kernel.py}).
   106	\item Discrete-to-continuum agreement at per-vertex Pearson
   107	  correlation $0.976$ on the unweighted variant, with the unweighted
   108	  variant winning the geometry-only criterion against two
   109	  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
   110	\item Same fixed $\Cph$ on same fixed $\Rsixhundred$ appears as
   111	  the shared response primitive underneath two independent empirical works in
   112	  qualitatively distinct regimes (\S\ref{sec:passive_witness},
   113	  \S\ref{sec:active_witness}).
   114	\end{itemize}
   115	
   116	\paragraph{Leaves open.}
   117	\begin{itemize}\itemsep=2pt
   118	\item \emph{First-principles derivation of $\Ph^{-2}$.} Reported
   119	  as a design-level shift; not derived from a closure functional
   120	  or symmetry argument.
   121	\item \emph{Substrate-uniqueness ablation.} The 600-cell choice is
   122	  post-hoc motivated by the empirical landings; alternative regular
   123	  4-polytopes are an explicit ablation build, not a discharged
   124	  comparison.
   125	\item \emph{Kernel-uniqueness on either empirical landing.} The
   126	  b-anomaly free-width Gaussian alternative (fits comparably with
   127	  one extra shape parameter) and the AIC tie
   128	  ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$) are
   129	  inherited verbatim from~\citep{SmartBAnomaly2026}.
   130	\item \emph{Selection theorem on ACT.} Lyapunov $V(W)$, edge-space
   131	  decomposition under $2I$-equivariance, full reduced-flow
   132	  convergence — all explicitly not delivered
   133	  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
   134	  here.
   135	\item \emph{Family-membership theorem.} The programme-home
   136	  positioning of cascade Lyapunov functionals as members of the
   137	  same polynomial-in-$L$ family is reported as
   138	  \emph{programme-positioned}, not formally classified.
   139	\end{itemize}

 succeeded in 202ms:
     1	% =====================================================================
     2	\section{Conclusion}\label{sec:conclusion}
     3	% =====================================================================
     4	
     5	The closure-response operator $\Cph = L_M + \Ph^{-2} I$ on the
     6	600-cell graph $\Rsixhundred$, with $\Ph = (1+\sqrt 5)/2$, is a
     7	geometry-fixed response primitive: positive definite under
     8	(H1)--(H3) on the substrate $(M, L_M)$, and on the connected
     9	finite graph $\Rsixhundred$ where $\lambda_{\min}(L_M) = 0$ it has
    10	smallest eigenvalue $\Ph^{-2}$ and operator-norm identity
    11	$\|\Cph^{-1}\| = \Ph^{2} \approx 2.618$ (general substrates with
    12	$\lambda_{\min}(L_M) > 0$ give the strict inequality
    13	$\|\Cph^{-1}\| < \Ph^{2}$).
    14	The 600-cell instance has $|V|=120$, $|E|=720$, uniform degree
    15	$12$, $9$-shell partition $\{1,12,20,12,30,12,20,12,1\}$, and a
    16	Laplacian spectrum that numerically resolves to the closed-form
    17	$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
    18	discrete-to-continuum agreement between $\psi = \Cph^{-1} f$ and
    19	the continuum kernel $G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at per-vertex
    20	chord distances (non-source vertices) is Pearson $\rho = 0.976$ on
    21	the unweighted Laplacian, above the two $\Ph$-cocycle weighted
    22	variants tested ($0.888$ geometric, $0.884$ arithmetic). All numbers are reproduced from canonical
    23	generators by \texttt{repro/verify\_kernel.py}; no parameter is
    24	fitted.
    25	
    26	\textbf{Two independent empirical landings.} The same fixed
    27	$\Cph$ on the same fixed $\Rsixhundred$, with no shape-parameter
    28	retuning between regimes, appears as the shared response
    29	primitive underneath:
    30	\begin{enumerate}\itemsep=2pt
    31	\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
    32	  fitted dimensionless amplitude $A$ per dataset (kernel shape
    33	  held fixed) gives a sign-uniform
    34	  $\Delta C_{9}^{\mathrm{eff}} < 0$ description of the
    35	  $b\to s\mu^{+}\mu^{-}$ angular anomaly across five public
    36	  datasets (LHCb 2015, LHCb 2021, CMS 2025, LHCb 2025, LHCb 2015
    37	  $B_s\to\phi$).
    38	\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
    39	  recurrent self-model layer above the same operator (one
    40	  condition-dependent self-injection coupling
    41	  $\eta\in\{0,0.05,0.20\}$, one substrate-pinned nonlinearity
    42	  $\mathrm{bounded\_topk}(\cdot, k=12)$ at the graph's average
    43	  degree) is consistent with the aria-chess active-regime tally
    44	  (frozen 2026-04-18): $17/18$ preregistered
    45	  substrate/neuroscience correspondences under the standard
    46	  validation protocol, $18/18$ after the documented $N\!=\!20$
    47	  P4 deep-dive (thresholds unchanged), plus six
    48	  literature-thresholded drug/sleep EEG signatures.
    49	\end{enumerate}
    50	By design, the two witnesses share exactly the geometry-fixed
    51	operator: the same $\Cph$, substrate $\Rsixhundred$, and shift
    52	$\Ph^{-2}$. Above that operator level, they share no fitted
    53	parameter, threshold, or dataset, and the empirical claims are
    54	tested on disjoint physical domains (flavour physics vs cortical
    55	neuroscience). Independence here is
    56	independence at the empirical layer above the shared operator,
    57	not statistical independence of the operator itself.
    58	
    59	\textbf{Operator-witness scope.} This is an operator witness, not
    60	a derivation of physics on either landing. We do not derive the
    61	$\Ph^{-2}$ shift; it is a design-level stability clamp. We do not
    62	claim 600-cell uniqueness; alternative regular 4-polytopes are an
    63	explicit ablation build. We do not claim kernel uniqueness on
    64	either empirical landing; the b-anomaly's free-width Gaussian
    65	alternative and AIC tie ($w_{\mathrm{VFD}}=0.348$ vs
    66	$w_{\mathrm{FREE\_C9}}=0.652$) are inherited verbatim, and the
    67	aria-chess substrate-witness scope is inherited verbatim. We do
    68	not deliver a selection theorem on the ACT
    69	4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
    70	open builds (Lyapunov $V(W)$, edge-space decomposition under
    71	$2I$-equivariance, full reduced-flow convergence) remain open and
    72	are not delivered here.
    73	
    74	\textbf{Programme position.} \S\ref{sec:programme_home} positions
    75	$\Cph$ within a broader programme-level family of
    76	polynomial-in-$L$ functionals (with the schematic family members
    77	named there as non-load-bearing future-programme context, not
    78	established here). Family-membership is
    79	\emph{programme-positioned}, not formally classified. The two
    80	empirical landings provide external consistency checks on the
    81	\emph{response} primitive without reducing or addressing the
    82	selection gap.
    83	
    84	The empirical material gathered here is the operator witness; the
    85	broader programme to convert the witness into a selection-theorem-
    86	grade claim is sketched in the companion preprints and remains
    87	the natural next step.

 succeeded in 212ms:
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
    14	\textbf{Single substrate (the 600-cell).} We have not tested
    15	whether $\Cph$ on the $24$-cell, the $120$-cell, or other H$_n$
    16	Coxeter graphs would give comparable per-vertex correlations on
    17	the discrete-to-continuum agreement test, or comparable structural
    18	fits on either empirical landing. The 600-cell choice is post-hoc
    19	motivated by the empirical landings, not from an a-priori
    20	derivation. \emph{Disclosure:} \S\ref{sec:intro},
    21	\S\ref{sec:substrate}, \S\ref{sec:programme_home}.
    22	\emph{Evidence:} per-vertex correlation $0.976$ on $\Rsixhundred$;
    23	empirical landings of \S\ref{sec:passive_witness} and
    24	\S\ref{sec:active_witness}. \emph{Strengthening build:}
    25	\texttt{repro/verify\_kernel.py} extension to the $24$-cell and
    26	$120$-cell, with the same per-vertex correlation criterion
    27	applied; verbatim re-run of the b-anomaly fit on alternative
    28	substrates from~\citep{SmartBAnomaly2026}; the aria-chess
    29	preprint's regime section already lists alternative-polytope
    30	ablation as an open build.
    31	
    32	\textbf{Single shift ($\Ph^{-2}$).} We have not tested whether
    33	nearby shifts ($\Ph^{-2} \pm \epsilon$ for small $\epsilon$) give
    34	comparable per-vertex correlation, or whether the empirical
    35	landings tolerate a shift sweep. The shift is held fixed across
    36	both regimes; perturbation analysis is an open build.
    37	\emph{Strengthening build:} sweep $\Ph^{-2} \cdot (1 \pm \delta)$
    38	for $\delta \in \{0.01, 0.05, 0.10, 0.25\}$ on the discrete-to-
    39	continuum correlation; report sensitivity envelope.
    40	
    41	\subsection{Post-hoc}\label{ssec:posthoc}
    42	
    43	\textbf{The 600-cell choice is post-hoc justified by empirical
    44	observables.} While the construction of $\Rsixhundred$ is
    45	theorem-level rigorous (H$_4$ Coxeter group theory), the choice
    46	of \emph{this} polytope as the discrete substrate instance is
    47	motivated by the empirical landings observed, not by an a-priori
    48	geometric or algebraic argument selecting it over the $24$-cell
    49	or $120$-cell. \emph{Disclosure:} \S\ref{sec:intro}.
    50	\emph{Evidence:} two independent empirical witnesses on
    51	$\Rsixhundred$. \emph{Strengthening build:} formal substrate
    52	ablation (above).
    53	
    54	\textbf{The geometry-first variant agreement is not historically
    55	blind on b-anomaly.} Per the b-anomaly preprint's limitations
    56	section, the LHCb 2025 data was inspected first and the
    57	pure-geometry ranking was verified afterward to agree with the
    58	data-$\chi^{2}$ ranking. The two-criterion agreement is
    59	\emph{criterion-independent} (geometry-only correlation here is a
    60	different test from b-anomaly's data $\chi^{2}$) but not
    61	historically pre-registered. \emph{Disclosure:} we inherit the
    62	caveat verbatim. \emph{Strengthening build:} a future blind variant
    63	test would freeze the variant choice before observing the data
    64	$\chi^{2}$.
    65	
    66	\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
    67	$\Ph^{-2} \approx 0.382$ is a stability clamp making $\Cph$
    68	strictly positive definite; it is not derived from a closure
    69	functional or symmetry argument. \emph{Disclosure:}
    70	\S\ref{ssec:opnorm}, \S\ref{sec:definition}. \emph{Evidence:} the
    71	same operator with the same shift serves as the basis for two
    72	independent empirical witnesses across qualitatively distinct
    73	regimes (\S\ref{sec:passive_witness},
    74	\S\ref{sec:active_witness}). \emph{Strengthening build:} derive
    75	or justify a distinguished shift under a named criterion (e.g.\
    76	minimum-amplitude amplification on a specified function class);
    77	uniqueness is not assumed and is itself an open problem.
    78	
    79	\subsection{Interpretation}\label{ssec:interpretation}
    80	
    81	\textbf{The discrete-to-continuum agreement is descriptive, not
    82	causal.} The per-vertex correlation $0.976$ between $\psi$ on
    83	$\Rsixhundred$ and the continuum kernel
    84	$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ at the same chord radii is a
    85	\emph{computed agreement} between two independently-defined
    86	objects, not a derivation that the discrete operator equals the
    87	continuum kernel. \emph{Disclosure:} \S\ref{sec:agreement} marks
    88	this explicitly. \emph{Evidence:} the agreement is at machine
    89	precision in the operator-norm bound and at $\rho = 0.976$ in the
    90	per-vertex correlation. \emph{Strengthening build:} a formal
    91	discrete-continuum convergence proof under a specified large-graph
    92	limit; a continuum limit theorem on H$_n$ Coxeter substrates as
    93	$n \to \infty$.
    94	
    95	\textbf{Variant ranking is criterion-dependent.} The unweighted
    96	variant wins on both the geometry-only criterion of this paper
    97	and b-anomaly's data $\chi^{2}$, but neither criterion is the
    98	\emph{unique} natural ranking. Edge-weighted variants outside the
    99	$\Ph$-cocycle family ($\sqrt{\deg}$-weighted, normalised
   100	Laplacian) are not tested here. \emph{Strengthening build:}
   101	extend \texttt{repro/verify\_kernel.py} to a wider variant
   102	catalogue.
   103	
   104	\subsection{Test/claim}\label{ssec:testclaim}
   105	
   106	\textbf{Two independent empirical landings, not formal physics.}
   107	The b-anomaly result is a structural fit (kernel shape held fixed)
   108	under an AIC tie with $\mathrm{FREE\_C9}$ on current data; the
   109	aria-chess result is a substrate witness (no claim that the
   110	substrate \emph{is} consciousness). Neither lands a theorem-grade
   111	physics claim on its own domain; both are appropriately
   112	hedged in their own preprints, and we inherit those hedges
   113	verbatim. \emph{Disclosure:} \S\ref{sec:passive_witness},
   114	\S\ref{sec:active_witness}. \emph{Evidence:} the witnesses pass
   115	their own preregistered or literature-derived thresholds.
   116	\emph{Strengthening build:} more flavour-physics datasets
   117	(LHCb Run~3, Belle~II) for the passive-regime witness;
   118	cross-cohort EEG (TUH, NHM) and cross-parcellation HCP
   119	(Schaefer, Glasser) for the active-regime witness; both already
   120	listed in the respective preprints.
   121	
   122	\textbf{Discrete-to-continuum correlation reported on a single pole,
   123	verified across all $|V|$.} The headline per-vertex correlation
   124	$0.976$ is reported with the canonical pole ($+x_{0}$ axis) as
   125	source. H$_4$ transitivity predicts the correlation is invariant
   126	under choice of source vertex. \texttt{repro/verify\_kernel.py}
   127	sweeps over all $120$ vertices: every source returns the same
   128	per-vertex correlation $0.976202$ to within $\sim 10^{-15}$
   129	(\texttt{multi\_source\_sweep.max\_minus\_min} in
   130	\texttt{results.json}). The single-pole headline is therefore a
   131	representative, not a sample, of the operator's behaviour under
   132	H$_4$ transitivity.
   133	
   134	\subsection{State-drift / out-of-scope}\label{ssec:scope}
   135	
   136	\textbf{Selection layer not delivered.} As enumerated in
   137	\S\ref{sec:programme_home}, the selection-layer constructions
   138	(Lyapunov $V(W)$, edge-space decomposition under $2I$-equivariance,
   139	full reduced-flow convergence) are open in the companion ACT
   140	preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
   141	delivered here. The two empirical witnesses strengthen confidence
   142	in the response primitive without addressing the selection gap.
   143	
   144	\textbf{No deuteron / hadron / RH / capstone material is loaded
   145	into this paper.} The cascade-derivation programme, the capstone
   146	coalgebra paper, and the Millennium drafts share operator-level
   147	infrastructure with this paper but are not load-bearing here.
   148	Deliberately out of scope.
   149	
   150	\textbf{Out-of-scope items NOT delivered (correctly).}
   151	\begin{itemize}\itemsep=2pt
   152	\item Lyapunov function $V(W)$ on the reduced flow — open build
   153	  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
   154	\item $2I$-equivariance audit of the closure operator family —
   155	  open build of ACT.
   156	\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   157	  Hodge edge Laplacian — open build of ACT.
   158	\item Selection theorem identifying $\Rsixhundred$ over alternative
   159	  regular 4-polytopes — see \S\ref{ssec:regime}.
   160	\item Formal discrete-to-continuum convergence theorem under a
   161	  specified large-graph limit — see \S\ref{ssec:interpretation}.
   162	\item First-principles derivation of the $\Ph^{-2}$ shift — see
   163	  \S\ref{ssec:posthoc}.
   164	\item Family-membership classification theorem for the
   165	  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
   166	\end{itemize}
   167	
   168	\subsection{The honest verdict}
   169	
   170	The result is an \emph{operator witness}: a geometry-fixed response
   171	operator on a fixed graph, with no shape parameters tuned to any
   172	dataset, is consistent with two independent empirical landings in
   173	qualitatively distinct regimes. We do not claim the operator is
   174	the unique kernel for either landing. We do not claim selection is
   175	delivered. We do not claim 600-cell uniqueness. The strengthening
   176	builds for stronger claims are listed above and remain open.

 succeeded in 289ms:
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

codex
The manuscript’s own numerical statements mostly line up internally so far, but I’ve found places where the presentation strength may exceed the evidence source. I’m cross-checking the script/results and the two source documents now, especially the inherited b-anomaly and aria-chess claims.
exec
/bin/bash -lc 'nl -ba papers/aria-closure-kernel/repro/results.json' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba papers/aria-closure-kernel/repro/verify_kernel.py | sed -n '1,240p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba papers/aria-closure-kernel/repro/verify_kernel.py | sed -n '241,520p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba docs/aria-closure-kernel.md' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 348ms:
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

 succeeded in 376ms:
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

 succeeded in 404ms:
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

 succeeded in 377ms:
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

exec
/bin/bash -lc "nl -ba /mnt/c/Users/nexus/OneDrive/Documents/My\\ Projects/BANOMALY-001/vfd-b-anomaly/README.md" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'nl -ba papers/aria-chess-paper/paper/main.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"17/18|18/18|P4|N=20|N\\"'!='"\\"'!20|six|6/6|EEG|bounded_topk|eta|condition|HCP|Sleep-EDFx|wake|alpha|Propofol|Recovery|substrate witness|selection theorem|unique|phi|600-cell|preregistered|2026-04-18" papers/aria-chess-paper -g '"'*.tex' -g '*.md'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "input|include|bibliography" papers/aria-chess-paper/paper/main.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 215ms:
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

 succeeded in 226ms:
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

 succeeded in 220ms:
171:\input{sections/01_introduction.tex}
172:\input{sections/02_method.tex}
173:\input{sections/03_substrate.tex}
174:\input{sections/04_consciousness_chain.tex}
175:\input{sections/05_results.tex}
176:\input{sections/06_stress_tests.tex}
177:\input{sections/07_cross_domain.tex}
178:\input{sections/08_discussion.tex}
179:\input{sections/09_limitations.tex}
180:\input{sections/10_conclusion.tex}
202:from the project repository~\citep{ariaChessRepo} via the included
209:\bibliographystyle{plainnat}
210:\bibliography{references}

 succeeded in 290ms:
papers/aria-chess-paper/README.md:23:    ├── PAPER_PREDICTIONS.md                    Preregistration frozen 2026-04-18 (P1–P18)
papers/aria-chess-paper/README.md:26:    ├── VALIDATION_RESULTS_2026-04-29.md        18/18 tally with thresholds
papers/aria-chess-paper/README.md:27:    ├── CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md    Six EEG signatures, per-condition
papers/aria-chess-paper/README.md:28:    ├── P4_SYNERGY_FINDING.md                   N=20 C×P deep-dive
papers/aria-chess-paper/README.md:29:    ├── CROSS_DOMAIN_RESULTS.md                 Chess / conversation / HCP
papers/aria-chess-paper/README.md:37:results, and protocol detail. These are the artifacts a reviewer needs to verify
papers/aria-chess-paper/README.md:43:  `run_preregistered_validation.py`, `run_chess_robustness.py`,
papers/aria-chess-paper/README.md:89:  `run_preregistered_validation.py` and the HCP analysis pipeline) or change
papers/aria-chess-paper/README.md:95:This is a **substrate witness**, not a selection theorem. The paper does not
papers/aria-chess-paper/README.md:98:- 600-cell uniqueness among regular 4-polytopes;
papers/aria-chess-paper/README.md:100:- the ACT 4-tuple bridge delivers a selection theorem here.
papers/aria-chess-paper/README.md:102:The 18/18 preregistered tally is reported as methodology refinement (no
papers/aria-chess-paper/paper/README.md:3:A geometry-fixed substrate witness for cortical signatures: eighteen
papers/aria-chess-paper/paper/README.md:4:preregistered correspondences and six drug/sleep EEG signatures from
papers/aria-chess-paper/paper/README.md:5:the 600-cell regular 4-polytope under H₄ Coxeter symmetry.
papers/aria-chess-paper/paper/README.md:41:# six drug/sleep signatures (~30 s)
papers/aria-chess-paper/paper/README.md:44:# C×P synergy N=20 deep-dive (~28 min)
papers/aria-chess-paper/paper/README.md:47:# eighteen preregistered correspondences (~18 min)
papers/aria-chess-paper/paper/README.md:48:python3 run_preregistered_validation.py
papers/aria-chess-paper/paper/README.md:56:per-condition means in §5.1 to 4 decimal places.
papers/aria-chess-paper/paper/README.md:63:- `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` (six signatures)
papers/aria-chess-paper/paper/README.md:64:- `docs/brain_mapping/P4_SYNERGY_FINDING.md` (N=20 deep-dive)
papers/aria-chess-paper/paper/README.md:65:- `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md` (chess / conversation / HCP)
papers/aria-chess-paper/paper/README.md:66:- `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` (18/18 tally)
papers/aria-chess-paper/paper/README.md:67:- `docs/brain_mapping/PAPER_PREDICTIONS.md` (preregistered 2026-04-18)
papers/aria-chess-paper/paper/README.md:72:This is a **substrate witness**: a geometry-fixed substrate is
papers/aria-chess-paper/paper/README.md:73:consistent with eighteen preregistered neuroscience correspondences
papers/aria-chess-paper/paper/README.md:74:and six drug/sleep EEG signatures, with no fitted shape parameters
papers/aria-chess-paper/paper/README.md:76:not a selection theorem on the companion adaptive-closure-transport
papers/aria-chess-paper/paper/README.md:77:4-tuple, and not a uniqueness claim for the 600-cell among regular
papers/aria-chess-paper/paper/main.tex:7:\usepackage{graphicx}
papers/aria-chess-paper/paper/main.tex:12:\graphicspath{{figures/}}
papers/aria-chess-paper/paper/main.tex:14:\newcommand{\Ph}{\varphi}
papers/aria-chess-paper/paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
papers/aria-chess-paper/paper/main.tex:19:\title{A geometry-fixed substrate witness for cortical signatures:\\
papers/aria-chess-paper/paper/main.tex:20:       eighteen preregistered correspondences and six drug/sleep EEG\\
papers/aria-chess-paper/paper/main.tex:21:       signatures from the 600-cell under H$_4$ Coxeter symmetry}
papers/aria-chess-paper/paper/main.tex:39:Once the 600-cell substrate is chosen, its graph structure is fixed:
papers/aria-chess-paper/paper/main.tex:49:quantitative correspondences with neuroscience data — preregistered
papers/aria-chess-paper/paper/main.tex:50:on 2026-04-18 before any validation run — plus six drug/sleep EEG
papers/aria-chess-paper/paper/main.tex:56:at the graph's average degree and one condition-dependent self-injection
papers/aria-chess-paper/paper/main.tex:57:coupling $\eta\!\in\!\{0, 0.05, 0.20\}$; condition-specific stimulus
papers/aria-chess-paper/paper/main.tex:62:This paper presents an empirical \emph{substrate witness}: it shows
papers/aria-chess-paper/paper/main.tex:64:neural dataset, is consistent with eighteen preregistered correspondences
papers/aria-chess-paper/paper/main.tex:65:and six EEG signatures. It is not a derivation of consciousness, nor a
papers/aria-chess-paper/paper/main.tex:66:selection theorem, nor a uniqueness claim for the 600-cell among regular
papers/aria-chess-paper/paper/main.tex:70:sits as the $L_M$ instance; the selection of the 600-cell as the active
papers/aria-chess-paper/paper/main.tex:74:We test whether a geometry-fixed substrate — the 600-cell regular
papers/aria-chess-paper/paper/main.tex:75:4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
papers/aria-chess-paper/paper/main.tex:79:preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
papers/aria-chess-paper/paper/main.tex:81:preregistered tally is $17/18$ at standard validation methodology
papers/aria-chess-paper/paper/main.tex:82:($5$-seed cascade block plus state-reset protocol), and $18/18$ after
papers/aria-chess-paper/paper/main.tex:84:interaction (P4); no preregistered threshold has been modified. We
papers/aria-chess-paper/paper/main.tex:85:additionally report six drug/sleep EEG signatures tested on a recurrent
papers/aria-chess-paper/paper/main.tex:87:trajectory at seed~$42$. The six signatures are not part of the
papers/aria-chess-paper/paper/main.tex:89:from the published literature (Sleep-EDFx CI for the wake $\alpha$,
papers/aria-chess-paper/paper/main.tex:93:obtained under condition-specific v4 stimulus models redesigned to
papers/aria-chess-paper/paper/main.tex:97:Wake cascade-event power-law exponent $\alpha = 2.252$,
papers/aria-chess-paper/paper/main.tex:99:This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
papers/aria-chess-paper/paper/main.tex:100:subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
papers/aria-chess-paper/paper/main.tex:101:pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
papers/aria-chess-paper/paper/main.tex:105:NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
papers/aria-chess-paper/paper/main.tex:107:ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
papers/aria-chess-paper/paper/main.tex:110:integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
papers/aria-chess-paper/paper/main.tex:111:direction confirmed); recovery deterministically identical to wake.
papers/aria-chess-paper/paper/main.tex:112:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/main.tex:118:ablation model, and the original preregistered C$\times$P synergy
papers/aria-chess-paper/paper/main.tex:125:estimate at $N\!=\!3$. In this cascade matrix, P4 required $N\!=\!20$;
papers/aria-chess-paper/paper/main.tex:135:preregistered estimator P13 was $5$-fold CV with threshold
papers/aria-chess-paper/paper/main.tex:142:discriminative. On HCP brain functional connectivity
papers/aria-chess-paper/paper/main.tex:143:(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
papers/aria-chess-paper/paper/main.tex:146:$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
papers/aria-chess-paper/paper/main.tex:149:$|V|\!=\!120$ vs HCP ICA-50 $|V|\!=\!50$; the $\sigma$ value reflects
papers/aria-chess-paper/paper/main.tex:151:clustering coefficient (implicit HCP across-subject sd $\approx 0.035$
papers/aria-chess-paper/paper/main.tex:155:We do not claim the 600-cell is the unique substrate consistent with
papers/aria-chess-paper/paper/main.tex:161:the per-condition signatures are an explicit strengthening build.
papers/aria-chess-paper/paper/main.tex:164:is consistent with eighteen preregistered neuroscience
papers/aria-chess-paper/paper/main.tex:165:correspondences and six drug/sleep EEG signatures, with all gaps in
papers/aria-chess-paper/paper/main.tex:167:without modifying any preregistered threshold.}
papers/aria-chess-paper/paper/main.tex:184:We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
papers/aria-chess-paper/paper/main.tex:187:the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
papers/aria-chess-paper/paper/main.tex:188:HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
papers/aria-chess-paper/paper/main.tex:193:al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
papers/aria-chess-paper/paper/main.tex:199:The complete pipeline (substrate construction, six-signature
papers/aria-chess-paper/paper/main.tex:201:preregistered validation, figure regeneration, this paper) is reproducible
papers/aria-chess-paper/paper/main.tex:206:$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
papers/aria-chess-paper/paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:6:gives the six drug/sleep EEG signatures on the recurrent layer
papers/aria-chess-paper/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:9:gives the three-way $\alpha$ overlap. We lift the result map
papers/aria-chess-paper/paper/sections/05_results.tex:10:$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
papers/aria-chess-paper/paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:18:\textbf{Setup.} Four conditions $\times$ $800$ ticks at seed $42$,
papers/aria-chess-paper/paper/sections/05_results.tex:20:(\S\ref{sec:chain}). Per-condition trajectory observables are
papers/aria-chess-paper/paper/sections/05_results.tex:21:$(n_{\mathrm{evt}}, \alpha, \mathrm{CI}_{95}, R^{2}, I_{\mathrm{var}},
papers/aria-chess-paper/paper/sections/05_results.tex:27:\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
papers/aria-chess-paper/paper/sections/05_results.tex:29:\label{tab:per_condition}
papers/aria-chess-paper/paper/sections/05_results.tex:32:condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
papers/aria-chess-paper/paper/sections/05_results.tex:46:\label{tab:six_signatures}
papers/aria-chess-paper/paper/sections/05_results.tex:52:   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
papers/aria-chess-paper/paper/sections/05_results.tex:54:2 & Propofol switching ratio &
papers/aria-chess-paper/paper/sections/05_results.tex:57:3 & Propofol continuity drop &
papers/aria-chess-paper/paper/sections/05_results.tex:58:   EEG microstate~\citep{Brodbeck2012Microstates} &
papers/aria-chess-paper/paper/sections/05_results.tex:60:4 & Propofol $\Phi$ collapse (IIT) &
papers/aria-chess-paper/paper/sections/05_results.tex:63:5 & Recovery reversibility &
papers/aria-chess-paper/paper/sections/05_results.tex:65:   identical to wake & $0$ diff & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:66:6 & Wake cortical-avalanche $\alpha$ &
papers/aria-chess-paper/paper/sections/05_results.tex:67:   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
papers/aria-chess-paper/paper/sections/05_results.tex:68:   $\alpha\!\in\![1.5, 3.5]$, $R^{2}\!>\!0.85$ &
papers/aria-chess-paper/paper/sections/05_results.tex:75:All six signatures pass against their literature-derived thresholds
papers/aria-chess-paper/paper/sections/05_results.tex:76:on the same deterministic substrate trajectory. The six signatures
papers/aria-chess-paper/paper/sections/05_results.tex:77:are not part of the dated 2026-04-18 P1--P18 preregistration; their
papers/aria-chess-paper/paper/sections/05_results.tex:78:thresholds are drawn from the literature (Sleep-EDFx CI for
papers/aria-chess-paper/paper/sections/05_results.tex:79:wake $\alpha$, OpenNeuro \texttt{ds005620} point-estimate window for
papers/aria-chess-paper/paper/sections/05_results.tex:83:biologically-motivated condition-specific stimulus models
papers/aria-chess-paper/paper/sections/05_results.tex:90:\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
papers/aria-chess-paper/paper/sections/05_results.tex:92:\textbf{Tally.} $17/18$ at standard validation
papers/aria-chess-paper/paper/sections/05_results.tex:93:(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
papers/aria-chess-paper/paper/sections/05_results.tex:94:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
papers/aria-chess-paper/paper/sections/05_results.tex:95:on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
papers/aria-chess-paper/paper/sections/05_results.tex:96:$32000$--$32019$). \emph{No preregistered threshold has been modified.}
papers/aria-chess-paper/paper/sections/05_results.tex:101:\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
papers/aria-chess-paper/paper/sections/05_results.tex:107:P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:110:\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
papers/aria-chess-paper/paper/sections/05_results.tex:113:P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:125:P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:130:\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
papers/aria-chess-paper/paper/sections/05_results.tex:134:\S\ref{sec:cross_domain} for the depth sweep and protocol detail.
papers/aria-chess-paper/paper/sections/05_results.tex:143:\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
papers/aria-chess-paper/paper/sections/05_results.tex:147:\item P13 (chess substrate lift): the 2026-04-18 preregistration
papers/aria-chess-paper/paper/sections/05_results.tex:156:  the preregistered test}, not as preregistration revision.
papers/aria-chess-paper/paper/sections/05_results.tex:159:\textbf{Headline verdict.} Eighteen preregistered correspondences
papers/aria-chess-paper/paper/sections/05_results.tex:160:all pass at preregistered thresholds, with two interaction tests
papers/aria-chess-paper/paper/sections/05_results.tex:166:\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:168:The substrate's wake cascade-$\alpha$ confidence interval overlaps
papers/aria-chess-paper/paper/sections/05_results.tex:174:\caption{Three-way $\alpha$ overlap on the wake cascade-event power
papers/aria-chess-paper/paper/sections/05_results.tex:176:\label{tab:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:179:Source & $\alpha$ & 95\% CI & $n$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:182:Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
papers/aria-chess-paper/paper/sections/05_results.tex:190:real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
papers/aria-chess-paper/paper/sections/05_results.tex:193:$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
papers/aria-chess-paper/paper/sections/05_results.tex:194:intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
papers/aria-chess-paper/paper/sections/05_results.tex:203:stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
papers/aria-chess-paper/paper/sections/10_conclusion.tex:5:The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
papers/aria-chess-paper/paper/sections/10_conclusion.tex:9:preregistered neuroscience correspondences plus six companion
papers/aria-chess-paper/paper/sections/10_conclusion.tex:10:drug/sleep EEG signatures of conscious vs unconscious states. Once
papers/aria-chess-paper/paper/sections/10_conclusion.tex:14:fixed; only one condition-dependent self-injection coupling
papers/aria-chess-paper/paper/sections/10_conclusion.tex:15:$\eta\in\{0, 0.05, 0.20\}$ and one substrate-pinned nonlinearity
papers/aria-chess-paper/paper/sections/10_conclusion.tex:20:\textbf{Headline tally.} On a single deterministic trajectory, six
papers/aria-chess-paper/paper/sections/10_conclusion.tex:21:drug/sleep EEG signatures pass against their literature-derived
papers/aria-chess-paper/paper/sections/10_conclusion.tex:22:thresholds (Sleep-EDFx CI, OpenNeuro \texttt{ds005620}, Brodbeck 2012,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:24:$0.463\!\times$ wake; propofol modality-switching $1.83\!\times$ wake;
papers/aria-chess-paper/paper/sections/10_conclusion.tex:26:$\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/10_conclusion.tex:27:recovery deterministically identical to wake under the WAKE stimulus
papers/aria-chess-paper/paper/sections/10_conclusion.tex:28:protocol; wake cortical-avalanche power law $\alpha\!=\!2.252$,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:29:$95\%$ CI $[1.82, 2.86]$, $R^{2}\!=\!0.956$. The wake $95\%$ CI
papers/aria-chess-paper/paper/sections/10_conclusion.tex:30:overlaps the real Sleep-EDFx EEG
papers/aria-chess-paper/paper/sections/10_conclusion.tex:31:$95\%$ CI ($n\!=\!30$ subjects, $\alpha\!=\!2.51$,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:35:\textbf{Eighteen preregistered correspondences.} All eighteen pass at
papers/aria-chess-paper/paper/sections/10_conclusion.tex:36:preregistered thresholds, with two interaction tests requiring
papers/aria-chess-paper/paper/sections/10_conclusion.tex:40:preregistered threshold has been modified. The original 2026-04-20
papers/aria-chess-paper/paper/sections/10_conclusion.tex:42:failure; the closure of the three gaps (P3, P4, P13) is documented
papers/aria-chess-paper/paper/sections/10_conclusion.tex:63:$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
papers/aria-chess-paper/paper/sections/10_conclusion.tex:69:on the full-cohort descriptive HCP $n\!=\!1003$ statistics
papers/aria-chess-paper/paper/sections/10_conclusion.tex:70:(preregistered test on the $n\!=\!100$ subset), ARIA's H$_4$-transitive
papers/aria-chess-paper/paper/sections/10_conclusion.tex:75:\textbf{Substrate-witness scope.} This is a substrate witness, not a
papers/aria-chess-paper/paper/sections/10_conclusion.tex:76:derivation of consciousness, not a selection theorem on the
papers/aria-chess-paper/paper/sections/10_conclusion.tex:79:uniqueness claim for the 600-cell among regular 4-polytopes. The
papers/aria-chess-paper/paper/sections/10_conclusion.tex:83:HCP replication, a Lyapunov function on the reduced flow,
papers/aria-chess-paper/paper/sections/10_conclusion.tex:88:tested against this many preregistered cortical correspondences from
papers/aria-chess-paper/paper/sections/10_conclusion.tex:91:gathered here is the substrate witness; the broader programme to
papers/aria-chess-paper/paper/sections/02_method.tex:13:\textbf{Frozen 2026-04-18.} Eighteen quantitative predictions
papers/aria-chess-paper/paper/sections/02_method.tex:14:(P1--P18) were locked on 2026-04-18 in
papers/aria-chess-paper/paper/sections/02_method.tex:21:predictions and rung observables — were preregistered on 2026-04-24
papers/aria-chess-paper/paper/sections/02_method.tex:24:not include those batteries in the headline 18/18 tally.} They are
papers/aria-chess-paper/paper/sections/02_method.tex:27:\textbf{Six EEG signatures (set B).} The drug/sleep signatures on the
papers/aria-chess-paper/paper/sections/02_method.tex:28:recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six companion
papers/aria-chess-paper/paper/sections/02_method.tex:31:propofol $\Phi$ collapse, recovery reversibility, wake
papers/aria-chess-paper/paper/sections/02_method.tex:32:cascade-$\alpha$). They are not part of the P1--P18 preregistration;
papers/aria-chess-paper/paper/sections/02_method.tex:37:2026-04-20 validation reported failures (P3, P4, P13), the documented
papers/aria-chess-paper/paper/sections/02_method.tex:41:(P4, C$\times$P), and
papers/aria-chess-paper/paper/sections/02_method.tex:44:preregistered threshold.
papers/aria-chess-paper/paper/sections/02_method.tex:61:P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:64:\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:65:P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:66:P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:67:P7 ($W{\to}N3$ var) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.70$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:68:P8 ($W{\to}N3$ switch) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.50$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:72:P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:78:P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
papers/aria-chess-paper/paper/sections/02_method.tex:87:\textbf{Sleep-EDFx (PhysioNet).} Public polysomnography
papers/aria-chess-paper/paper/sections/02_method.tex:89:the cortical-avalanche $\alpha$ baseline; $n=24$ subjects used for
papers/aria-chess-paper/paper/sections/02_method.tex:90:the wake$\to$N3 variance and switching ratios. Cortical-avalanche
papers/aria-chess-paper/paper/sections/02_method.tex:94:\textbf{OpenNeuro \texttt{ds005620}.} Propofol-induced loss of
papers/aria-chess-paper/paper/sections/02_method.tex:95:consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
papers/aria-chess-paper/paper/sections/02_method.tex:98:($2.96\!\times$ wake) in Sig~2.
papers/aria-chess-paper/paper/sections/02_method.tex:101:EEG~\citep{OpenNeuroDS004902},
papers/aria-chess-paper/paper/sections/02_method.tex:105:\textbf{Zenodo \texttt{3992359}.} DMT EEG public
papers/aria-chess-paper/paper/sections/02_method.tex:109:\textbf{HCP S1200.} Human Connectome Project
papers/aria-chess-paper/paper/sections/02_method.tex:110:S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
papers/aria-chess-paper/paper/sections/02_method.tex:111:matrix. The preregistered test (P18) was on $n=100$ subjects for
papers/aria-chess-paper/paper/sections/02_method.tex:115:preregistered test.
papers/aria-chess-paper/paper/sections/02_method.tex:118:signature (Sig~3) follows the EEG microstate methodology lineage of
papers/aria-chess-paper/paper/sections/02_method.tex:119:Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
papers/aria-chess-paper/paper/sections/02_method.tex:128:\textbf{Cascade-$\alpha$ fitting.} Power-law $\alpha$ is fit by
papers/aria-chess-paper/paper/sections/02_method.tex:138:\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
papers/aria-chess-paper/paper/sections/02_method.tex:140:preregistered cascade-$\alpha$ tests, 2000 resamples for the
papers/aria-chess-paper/paper/sections/02_method.tex:142:preregistered; 42 for the deep-dive.
papers/aria-chess-paper/paper/sections/02_method.tex:146:$0/2000$ were below the preregistered floor $+0.10$; we report these
papers/aria-chess-paper/paper/sections/02_method.tex:151:ablation conditions $\{----, -C--, --P-, -CP-\}$, the interaction is
papers/aria-chess-paper/paper/sections/02_method.tex:154:\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
papers/aria-chess-paper/paper/sections/02_method.tex:155:        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
papers/aria-chess-paper/paper/sections/02_method.tex:158:\textbf{$\sigma$-distance against external nulls.} For the HCP
papers/aria-chess-paper/paper/sections/02_method.tex:160:$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
papers/aria-chess-paper/paper/sections/02_method.tex:175:preregistered floor). The reset protocol is documented in
papers/aria-chess-paper/paper/sections/02_method.tex:190:\item Eighteen preregistered:
papers/aria-chess-paper/paper/sections/02_method.tex:191:  \texttt{python3 run\_preregistered\_validation.py}
papers/aria-chess-paper/paper/sections/02_method.tex:198:recurrent layer should reproduce per-condition means in this paper to
papers/aria-chess-paper/TASK-aria-paper-completion.md:4:**Bar:** Hostile-review-ready, no overclaim. Strong, confident paper backed by lots of empirical evidence. Per `feedback_credibility_bar.md`: "complete + undismissable" not "honest + conditional."
papers/aria-chess-paper/TASK-aria-paper-completion.md:14:- `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` — 6/6 v4 signature table, full per-signature documentation
papers/aria-chess-paper/TASK-aria-paper-completion.md:15:- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — N=20 deep-dive narrative + per-seed values + bootstrap
papers/aria-chess-paper/TASK-aria-paper-completion.md:16:- `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md` — chess + conversation + HCP results
papers/aria-chess-paper/TASK-aria-paper-completion.md:17:- `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` — 18/18 prereg tally with thresholds
papers/aria-chess-paper/TASK-aria-paper-completion.md:26:| 6/6 v4 EEG signature table | 4 conditions × 6 signatures all pass | `demo_drug_sleep_v4.py` | ~30s |
papers/aria-chess-paper/TASK-aria-paper-completion.md:27:| P4 C×P synergy (N=20) | +0.190 [+0.143, +0.239]; P(≤0)=0.0000 | `demo_p4_cxp_deep_dive.py` | ~28 min |
papers/aria-chess-paper/TASK-aria-paper-completion.md:28:| 18/18 preregistered tally | All P1-P18 pass | `run_preregistered_validation.py` | ~18 min |
papers/aria-chess-paper/TASK-aria-paper-completion.md:29:| HCP categorical separation | Degree-std 11.58σ, PR 79.78σ (n=1003) | Cascade pipeline | (deterministic) |
papers/aria-chess-paper/TASK-aria-paper-completion.md:30:| Sleep-EDFx spindle α | 2.513 (real) ∈ ARIA CI | Sleep-EDFx public data + `run_baseline_for_eeg.py` | (cached) |
papers/aria-chess-paper/TASK-aria-paper-completion.md:31:| Cascade-α three-way overlap | WAKE [1.82,2.86] ∩ EEG [2.50,2.86] ∩ ARIA prior [2.73,3.25] | Combined | (cached) |
papers/aria-chess-paper/TASK-aria-paper-completion.md:33:**Validation persistence:** `~/.aria/preregistered_validation/results_1777466957.json` (Apr 29 13:49) is the 18/18 record.
papers/aria-chess-paper/TASK-aria-paper-completion.md:47:- A deterministic geometric substrate (600-cell under H₄ symmetry) reproduces 18 preregistered neuroscience predictions across multiple paradigms with NO fitted shape parameters.
papers/aria-chess-paper/TASK-aria-paper-completion.md:48:- The claim is **not** that the substrate explains consciousness or that it's the unique solution.
papers/aria-chess-paper/TASK-aria-paper-completion.md:74:    │   ├── 03_substrate.tex          # the 600-cell + cascade decomposition + Green response
papers/aria-chess-paper/TASK-aria-paper-completion.md:76:    │   ├── 05_results.tex            # 6/6 v4 + 18/18 + cascade-α match
papers/aria-chess-paper/TASK-aria-paper-completion.md:77:    │   ├── 06_stress_tests.tex       # P4 N=20 + bootstrap + ablation matrix
papers/aria-chess-paper/TASK-aria-paper-completion.md:78:    │   ├── 07_cross_domain.tex       # chess + conversation + HCP
papers/aria-chess-paper/TASK-aria-paper-completion.md:91:- The geometry: H₄ Coxeter / 600-cell — biological motivation (icosahedral hippocampus, theta-gamma 11:1 ratio, etc.) but NOT a-priori derivation.
papers/aria-chess-paper/TASK-aria-paper-completion.md:93:- Programme position: passive-regime witness for $C_\varphi$ in b-anomaly is the companion (one substrate, two empirical layers).
papers/aria-chess-paper/TASK-aria-paper-completion.md:96:- Datasets: Sleep-EDFx (n=30/24), OpenNeuro ds005620 propofol (n=20), Zenodo ds003992359 DMT (n=29), ds004902 SD (n=35), HCP-YA S1200 (n=1003) — all public, cite DOIs.
papers/aria-chess-paper/TASK-aria-paper-completion.md:97:- Substrate construction summary (full derivation in §3): 600-cell, H₄ acting transitively, 9 H₃-shells, 12-degree.
papers/aria-chess-paper/TASK-aria-paper-completion.md:101:- Preregistration protocol (frozen 2026-04-18 / 2026-04-24, what was peeked / what was not — be honest about ordering).
papers/aria-chess-paper/TASK-aria-paper-completion.md:106:- 600-cell vertex set V_600, 720 edges, 12-regular, 9 H₃-shells {1,12,20,12,30,12,20,12,1}.
papers/aria-chess-paper/TASK-aria-paper-completion.md:109:- Green response operator $C_\varphi = L + \varphi^{-2} I$, programme-level definition (NOT load-bearing for the empirical claims; cite docs/aria-closure-kernel.md).
papers/aria-chess-paper/TASK-aria-paper-completion.md:122:**§5.1 Six v4 EEG signatures across 4 brain states**
papers/aria-chess-paper/TASK-aria-paper-completion.md:124:Verbatim from MANUSCRIPT_V2 lines 661-677. Per-condition table:
papers/aria-chess-paper/TASK-aria-paper-completion.md:134:**§5.2 18/18 preregistered validation tally**
papers/aria-chess-paper/TASK-aria-paper-completion.md:140:WAKE α [1.82, 2.86] ∩ real EEG α [2.50, 2.86] (Sleep-EDFx n=30) ∩ ARIA prior α [2.73, 3.25].
papers/aria-chess-paper/TASK-aria-paper-completion.md:144:**§6.1 P4 C×P deep-dive (the headline stress test)**
papers/aria-chess-paper/TASK-aria-paper-completion.md:150:**§6.2 16-condition 2⁴ ablation matrix**
papers/aria-chess-paper/TASK-aria-paper-completion.md:156:Conditions A/B/C/D (no homeostasis / periodic only / wake-decay only / dual). Both required.
papers/aria-chess-paper/TASK-aria-paper-completion.md:162:**§7.3 HCP categorical separation** — n=1003, degree-std 11.58σ, PR 79.78σ.
papers/aria-chess-paper/TASK-aria-paper-completion.md:166:**§8.1 What's new** — substrate witness, no fitted parameters, 18/18 prereg, 4-state cross-paradigm.
papers/aria-chess-paper/TASK-aria-paper-completion.md:169:**§8.4 Substrate as null reference** — HCP separation reading.
papers/aria-chess-paper/TASK-aria-paper-completion.md:178:**Move 2 (post-hoc structure verification):** P4 retest at N=20 was data-second (we saw N=3 fail first). Acknowledge ordering.
papers/aria-chess-paper/TASK-aria-paper-completion.md:180:**Move 3 (interpretation alternatives):** Three readings — (a) substrate is real-physics, (b) H₄ is structurally right, (c) data is rank-1 in any group-theoretic substrate. Adopt (c) as conservative.
papers/aria-chess-paper/TASK-aria-paper-completion.md:187:- 8.1 Substrate-level (600-cell only tested; no comparison to 24-cell, 120-cell)
papers/aria-chess-paper/TASK-aria-paper-completion.md:190:- 8.4 Preregistered validation (single seed range for N=20 P4; freeze date 2026-04-18 vs 2026-04-24 ambiguity)
papers/aria-chess-paper/TASK-aria-paper-completion.md:191:- 8.5 Theoretical (post-hoc 600-cell choice; cascade decomposition non-unique; φ⁻² floor design-level not derived)
papers/aria-chess-paper/TASK-aria-paper-completion.md:205:**AC1.** Every numerical claim is verbatim from the deterministic scripts. The 18/18 table, the 6/6 signature table, the P4 N=20 result, the HCP separation — exact numbers reproducible from `demo_drug_sleep_v4.py`, `demo_p4_cxp_deep_dive.py`, `run_preregistered_validation.py`.
papers/aria-chess-paper/TASK-aria-paper-completion.md:212:- DO NOT claim the substrate is the unique solution.
papers/aria-chess-paper/TASK-aria-paper-completion.md:214:**AC3.** The five b-anomaly honest-scope moves have explicit equivalents in §9 (regime, post-hoc, interpretation, test/claim, state-drift).
papers/aria-chess-paper/TASK-aria-paper-completion.md:224:**AC8.** Preregistration date ambiguity (2026-04-18 frozen predictions vs 2026-04-24 frozen H4-fingerprint) is explicitly clarified.
papers/aria-chess-paper/TASK-aria-paper-completion.md:254:**SECTION C.** Citation requirements: which papers need bibtex entries (b-anomaly, ACT, foundation papers, EEG literature). Cite with file paths.
papers/aria-chess-paper/TASK-aria-paper-completion.md:260:- post-hoc N=20 P4 retest
papers/aria-chess-paper/TASK-aria-paper-completion.md:261:- 600-cell as post-hoc choice
papers/aria-chess-paper/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-chess-paper/paper/sections/09_limitations.tex:14:\textbf{Single substrate (the 600-cell).} We have not tested whether
papers/aria-chess-paper/paper/sections/09_limitations.tex:16:comparable correspondences. The 600-cell was chosen because its
papers/aria-chess-paper/paper/sections/09_limitations.tex:19:\emph{Disclosure:} substrate-witness scope, no uniqueness claim
papers/aria-chess-paper/paper/sections/09_limitations.tex:21:on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
papers/aria-chess-paper/paper/sections/09_limitations.tex:22:$\{24\text{-cell}, 120\text{-cell}\}$ on the same six-signature
papers/aria-chess-paper/paper/sections/09_limitations.tex:23:battery and the eighteen preregistered tests, with thresholds
papers/aria-chess-paper/paper/sections/09_limitations.tex:27:six-signature results in~\S\ref{ssec:six_signatures} are reported on
papers/aria-chess-paper/paper/sections/09_limitations.tex:32:in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
papers/aria-chess-paper/paper/sections/09_limitations.tex:33:\emph{Evidence:} bootstrap CI on the wake 58 events, plus three-way
papers/aria-chess-paper/paper/sections/09_limitations.tex:34:overlap with two independent reference $\alpha$ ranges.
papers/aria-chess-paper/paper/sections/09_limitations.tex:47:to subject-level measurements, but they are condition-specific
papers/aria-chess-paper/paper/sections/09_limitations.tex:58:\textbf{The 600-cell choice is post-hoc justified by empirical
papers/aria-chess-paper/paper/sections/09_limitations.tex:59:observables.} While the construction of $\Rsixhundred$ is theorem-
papers/aria-chess-paper/paper/sections/09_limitations.tex:63:\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
papers/aria-chess-paper/paper/sections/09_limitations.tex:64:derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
papers/aria-chess-paper/paper/sections/09_limitations.tex:65:preregistered correspondences plus six signatures; the H$_4$
papers/aria-chess-paper/paper/sections/09_limitations.tex:76:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
papers/aria-chess-paper/paper/sections/09_limitations.tex:83:strictly positive definite (\S\ref{ssec:cphi}); it is not derived
papers/aria-chess-paper/paper/sections/09_limitations.tex:85:\S\ref{ssec:cphi} marks this as a design-level choice; the companion
papers/aria-chess-paper/paper/sections/09_limitations.tex:90:derive the $\Ph^{-2}$ shift as the unique stability clamp under a
papers/aria-chess-paper/paper/sections/09_limitations.tex:93:\subsection{Interpretation}\label{ssec:interpretation}
papers/aria-chess-paper/paper/sections/09_limitations.tex:95:\textbf{The recurrent layer is a method, not a metaphysics claim.}
papers/aria-chess-paper/paper/sections/09_limitations.tex:97:we claim quantitative consistency with six published biological
papers/aria-chess-paper/paper/sections/09_limitations.tex:99:\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
papers/aria-chess-paper/paper/sections/09_limitations.tex:100:\emph{Evidence:} six signatures vs published thresholds.
papers/aria-chess-paper/paper/sections/09_limitations.tex:107:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
papers/aria-chess-paper/paper/sections/09_limitations.tex:109:\texttt{phi\_iit\_full} implementation following Balduzzi--Tononi
papers/aria-chess-paper/paper/sections/09_limitations.tex:112:\textbf{HCP $\sigma$-distances are descriptive, not normative.} We
papers/aria-chess-paper/paper/sections/09_limitations.tex:121:\textbf{Two preregistered interaction tests required higher $N$
papers/aria-chess-paper/paper/sections/09_limitations.tex:122:than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
papers/aria-chess-paper/paper/sections/09_limitations.tex:134:threshold modification.} The reversals (P3, P4, P13) are documented
papers/aria-chess-paper/paper/sections/09_limitations.tex:141:builds for P3/P4/P13 above; no further claim is needed.
papers/aria-chess-paper/paper/sections/09_limitations.tex:153:\textbf{Single condition-dependent parameter $\eta$ is not derived
papers/aria-chess-paper/paper/sections/09_limitations.tex:154:as a learned variable.} $\eta\in\{0, 0.05, 0.20\}$ across PROPOFOL,
papers/aria-chess-paper/paper/sections/09_limitations.tex:155:SLEEP\_N3, and WAKE/RECOVERY is a condition-dependent constant in
papers/aria-chess-paper/paper/sections/09_limitations.tex:157:extension where $\eta$ adapts on an error norm is an open build.
papers/aria-chess-paper/paper/sections/09_limitations.tex:172:\item Selection theorem for $\Rsixhundred$ over alternative regular
papers/aria-chess-paper/paper/sections/09_limitations.tex:174:\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
papers/aria-chess-paper/paper/sections/09_limitations.tex:175:  of the six signatures.
papers/aria-chess-paper/paper/sections/09_limitations.tex:176:\item Cross-parcellation replication of the HCP $\sigma$-distances
papers/aria-chess-paper/paper/sections/09_limitations.tex:179:\item Verification of P10 (chess null mapping) at the preregistered
papers/aria-chess-paper/paper/sections/09_limitations.tex:187:The result is a substrate witness: a geometry-fixed substrate, with
papers/aria-chess-paper/paper/sections/09_limitations.tex:189:eighteen preregistered correspondences and six companion drug/sleep
papers/aria-chess-paper/paper/sections/09_limitations.tex:190:EEG signatures, with all original gaps closed by methodology
papers/aria-chess-paper/paper/sections/09_limitations.tex:191:refinement and without modifying any preregistered threshold. We do
papers/aria-chess-paper/paper/sections/09_limitations.tex:193:selection theorem on the ACT bridge. We do not claim uniqueness for
papers/aria-chess-paper/paper/sections/09_limitations.tex:194:$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
papers/aria-chess-paper/paper/sections/01_introduction.tex:12:has yielded the kind of preregistered multi-domain quantitative
papers/aria-chess-paper/paper/sections/01_introduction.tex:13:benchmark on real EEG data tested here. The structure-driven
papers/aria-chess-paper/paper/sections/01_introduction.tex:22:600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
papers/aria-chess-paper/paper/sections/01_introduction.tex:26:candidate substrate for consciousness-linked signatures. We construct $\Rsixhundred$, fix its response
papers/aria-chess-paper/paper/sections/01_introduction.tex:28:single condition-dependent self-injection coupling $\eta$ and a
papers/aria-chess-paper/paper/sections/01_introduction.tex:30:against eighteen preregistered correspondences plus six companion
papers/aria-chess-paper/paper/sections/01_introduction.tex:31:drug/sleep EEG signatures.
papers/aria-chess-paper/paper/sections/01_introduction.tex:35:We claim a single \emph{substrate witness}: that a geometry-fixed
papers/aria-chess-paper/paper/sections/01_introduction.tex:37:consistent with eighteen preregistered correspondences (frozen
papers/aria-chess-paper/paper/sections/01_introduction.tex:38:2026-04-18) and six companion drug/sleep EEG signatures of
papers/aria-chess-paper/paper/sections/01_introduction.tex:42:\item \textbf{Substrate is fixed once chosen.} Once $\Rsixhundred$
papers/aria-chess-paper/paper/sections/01_introduction.tex:44:  $3$-sphere) is forced by the canonical 600-cell construction; H$_4$
papers/aria-chess-paper/paper/sections/01_introduction.tex:54:  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
papers/aria-chess-paper/paper/sections/01_introduction.tex:55:  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
papers/aria-chess-paper/paper/sections/01_introduction.tex:60:  collapse to $0.463\!\times$ wake; propofol modality-switching
papers/aria-chess-paper/paper/sections/01_introduction.tex:61:  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
papers/aria-chess-paper/paper/sections/01_introduction.tex:62:  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
papers/aria-chess-paper/paper/sections/01_introduction.tex:63:  recovery deterministically identical to wake; wake cascade-$\alpha$
papers/aria-chess-paper/paper/sections/01_introduction.tex:65:\item \textbf{Eighteen preregistered correspondences pass.}
papers/aria-chess-paper/paper/sections/01_introduction.tex:66:  $17/18$ at standard methodology; $18/18$ after a documented
papers/aria-chess-paper/paper/sections/01_introduction.tex:68:  test; \emph{no preregistered threshold has been modified}.
papers/aria-chess-paper/paper/sections/01_introduction.tex:72:  conversation $-4.4$pp lift, within preregistered neutrality bounds)
papers/aria-chess-paper/paper/sections/01_introduction.tex:74:  cortical functional connectivity (HCP full-cohort descriptive
papers/aria-chess-paper/paper/sections/01_introduction.tex:83:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
papers/aria-chess-paper/paper/sections/01_introduction.tex:84:  the unique substrate consistent with these signatures. Other regular
papers/aria-chess-paper/paper/sections/01_introduction.tex:86:  build, not a discharged comparison. The 600-cell choice is post-hoc
papers/aria-chess-paper/paper/sections/01_introduction.tex:89:\item \emph{Not a derivation of consciousness.} The substrate witness
papers/aria-chess-paper/paper/sections/01_introduction.tex:93:\item \emph{Not a selection theorem.} The companion adaptive-closure-
papers/aria-chess-paper/paper/sections/01_introduction.tex:96:  this substrate fills the $L_M$ slot. The selection of the 600-cell
papers/aria-chess-paper/paper/sections/01_introduction.tex:105:  that some such mechanisms appear in the substrate's preregistered
papers/aria-chess-paper/paper/sections/01_introduction.tex:128:A result that lands inside its preregistered threshold licenses a
papers/aria-chess-paper/paper/sections/01_introduction.tex:129:`consistent with' claim. A result that exceeds the preregistered
papers/aria-chess-paper/paper/sections/01_introduction.tex:133:(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
papers/aria-chess-paper/paper/sections/01_introduction.tex:142:\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
papers/aria-chess-paper/paper/sections/01_introduction.tex:143:signatures, on a geometry-fixed substrate with one condition-dependent
papers/aria-chess-paper/paper/sections/01_introduction.tex:144:parameter $\eta$ and one graph-pinned nonlinearity, against published
papers/aria-chess-paper/paper/sections/01_introduction.tex:146:\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
papers/aria-chess-paper/paper/sections/01_introduction.tex:147:selection theorem on the 4-tuple bridge; circuit-level mechanistic
papers/aria-chess-paper/paper/sections/01_introduction.tex:149:that cortex \emph{is} the 600-cell.
papers/aria-chess-paper/paper/sections/01_introduction.tex:157:constructs $\Rsixhundred$ and the response operator $\Cph$, with the
papers/aria-chess-paper/paper/sections/01_introduction.tex:161:\S\ref{sec:results} reports the empirical tables: six drug/sleep
papers/aria-chess-paper/paper/sections/01_introduction.tex:162:signatures, eighteen preregistered correspondences, three-way
papers/aria-chess-paper/paper/sections/01_introduction.tex:163:$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
papers/aria-chess-paper/paper/sections/01_introduction.tex:166:selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
papers/aria-chess-paper/paper/sections/01_introduction.tex:167:discusses the substrate witness and proposes a non-load-bearing
papers/aria-chess-paper/paper/sections/01_introduction.tex:168:ACT bridge (without claiming a selection theorem).
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:6:cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:10:graph-pinned nonlinearity, one condition-dependent self-injection
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:11:coupling $\eta$, and four trajectory observables. No shape parameter
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:14:This section is method, not metaphysics. We do not claim the
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:24:f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:30:with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:31:condition-dependent architectural parameter. $f_{\mathrm{self}}$ maps
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:35:across all conditions.
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:39:\item $\eta = 0.20$ for WAKE and RECOVERY (active recurrent self-loop);
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:40:\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:41:\item $\eta = 0.00$ for PROPOFOL (broken recurrence; residual cortex
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:52:gives smooth dynamics with cascade $\alpha\approx 1.09$ — no
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:53:avalanches. Adding bounded-top-$K$ at $k=12$ drives $\alpha$ into the
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:58:geometry, not by neural data. Smaller $k$ (e.g.\ $k=6$) gives $\alpha$
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:59:at the band edge with poorer fit; larger $k$ ($24, 48$) gives $\alpha$
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:67:\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:82:\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:90:of effect on the propofol-vs-wake state contrast; it is not a
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:124:Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:127:\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:131:that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:142:$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:155:condition-specific design choices iterated to close v3 stimulus-model
papers/aria-chess-paper/paper/sections/04_consciousness_chain.tex:164:ablation grid is the basis for the preregistered tests P1--P5 and
papers/aria-chess-paper/brain_mapping_refs/PREREG_RUNG_OBSERVABLES.md:5:(P-A, G6.4, QMS-2 L40-YES), that's the *predicted* outcome if EEG reads
papers/aria-chess-paper/brain_mapping_refs/PREREG_RUNG_OBSERVABLES.md:7:tests which rung cortical EEG/ECoG actually reads at.
papers/aria-chess-paper/brain_mapping_refs/PREREG_RUNG_OBSERVABLES.md:48:2. **ds004902 scalp EEG** — 61 channels, n=20; cross-modality check.
papers/aria-chess-paper/brain_mapping_refs/PREREG_RUNG_OBSERVABLES.md:49:3. **Sleep-EDFx** — 2 channels, insufficient for PCA; excluded.
papers/aria-chess-paper/brain_mapping_refs/PREREG_RUNG_OBSERVABLES.md:59:  Sleep-EDFx Nyquist but ds004902 at 500 Hz can see low-γ)
papers/aria-chess-paper/brain_mapping_refs/PREREG_RUNG_OBSERVABLES.md:76:**FROZEN 2026-04-24, preregistered before any analysis.**
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:1:# Cross-Domain Validation: Chess, Conversation, and HCP Connectivity
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:6:> **Headline.** The 600-cell substrate functions as a **selective
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:13:> transitivity); HCP n=1003 degree std = 3.28 ± 0.28; ARIA is
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:27:1. **Chess pattern recognition** (P9–P13 in the preregistered set):
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:38:   **selective** amplifier (not an unconditional one).
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:40:3. **HCP brain connectivity** (P17–P18): compare ARIA's vertex-graph
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:47:preregistered tests on chess + conversation pass at fresh seeds; both
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:48:HCP tests pass deterministically (P17 from theorem; P18 from data).
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:78:Critical detail: between successive depth measurements, the substrate
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:95:**Interpretation:** Substrate-routed classification at 5-fold CV is
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:115:**Interpretation:** This is the most architecturally informative cross-
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:117:substrate retains 65.4% classification power — well above the 25%
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:142:**Interpretation:** With shuffled labels, classification drops to chance
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:151:**Method:** Run the substrate at six different `n_ticks` values
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:167:**Interpretation:** The substrate has a clear optimal depth around
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:192:**Interpretation:** The substrate amplifies the chess-position
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:195:the substrate's 600-cell graph. This is **+40.6pp of geometric
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:203:diagnostic details.
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:214:preregistered floor. The 65.4% null mapping shows two-thirds of the
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:240:**Interpretation:** Conversation features are already strongly
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:258:**Interpretation:** This is the **selective amplifier signature**.
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:262:preregistered window, and the negative sign suggests minor noise
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:279:**Interpretation:** Conversation null mapping (70.6%) is slightly
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:301:substrate routing at 83.1% (lift −4.4pp) is within preregistered
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:307:## 4. HCP brain connectivity (P17–P18)
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:311:**Reference cohort:** Human Connectome Project (HCP), n=1003 subjects.
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:312:For preregistered tests, n=100 subjects (computational tractability)
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:320:**ARIA reference:** 600-cell H₄ graph. By H₄ transitivity, every
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:330:**Interpretation:** This is a theorem, not a measurement. The H₄
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:331:Coxeter group acts transitively on the 600-cell vertices; every
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:336:### 4.3 P18 — HCP degree std (hub-spoke structure)
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:338:**Threshold:** HCP ICA-50 degree std > 2.0.
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:342:**Interpretation:** Real cortical functional connectivity has
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:347:**ARIA is at −11.58σ** below the HCP cohort mean on this metric:
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:348:ARIA's degree std is 0; HCP n=1003 mean is 3.28 ± 0.28; the gap is
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:349:(0 − 3.28) / 0.28 = −11.7σ. **Zero of 1003 HCP subjects** have
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:354:Three metrics computed across the full HCP cohort, with ARIA's value
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:358:Metric                 ARIA     HCP n=1003 mean   σ from HCP
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:365:**Interpretation:**
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:369:  hub-concentrated). ARIA at 68.54 vs HCP at 19.72 — ARIA is
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:373:  ARIA at 0.455 vs HCP at 0.220 — ARIA has more local clustering
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:379:The HCP comparison places ARIA as a **principled maximum-symmetry
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:383:quantitatively measurable as the σ-distance between ARIA and HCP on
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:394:induced noise envelope — the gap between ARIA and HCP is robust to
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:416:### 4.7 HCP summary
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:418:ARIA's degree std = 0 (theorem); HCP n=1003 degree std = 3.28 ± 0.28,
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:440:is correctly null (lift −4.4pp, well within preregistered neutrality
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:442:unconditional booster. On HCP brain functional connectivity (n=1003,
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:445:participation ratio ARIA at 68.54 is +79.78σ above HCP (19.72 ± 0.61),
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:446:and on clustering coefficient ARIA at 0.455 is +6.80σ above HCP (0.220).
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:493:python3 run_preregistered_validation.py
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:502:- HCP n=100 ICA-50: deterministic from group average
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:507:- `run_hcp_registration.py` for HCP
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:509:JSON outputs land in `~/.aria/preregistered_validation/results_*.json`.
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:527:3. **HCP comparison uses one parcellation (ICA-50).** Different
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:551:- `run_preregistered_validation.py` — full P1–P18 harness
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:555:- `run_hcp_registration.py` — HCP track
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:565:- `docs/brain_mapping/PAPER_PREDICTIONS.md` — frozen 2026-04-18
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:567:  preregistered tally
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:568:- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — synergy deep-dive
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:569:- `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` — six
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:570:  EEG drug/sleep signatures (recurrent self-model layer above
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:582:- `project_hcp_maxsymmetry_null.md` — HCP comparison detail
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:583:- `project_preregistered_validation_17_of_18.md` — re-run summary
papers/aria-chess-paper/brain_mapping_refs/CROSS_DOMAIN_RESULTS.md:584:- `project_p4_cxp_underpowered_not_wrong.md` — N=20 deep-dive
papers/aria-chess-paper/brain_mapping_refs/NON_EQUILIBRIUM_FINDING.md:116:cortex operates as a dissipative structure requiring metabolic input.
papers/aria-chess-paper/brain_mapping_refs/NON_EQUILIBRIUM_FINDING.md:132:during wake. Our reset operation is a direct computational analogue.
papers/aria-chess-paper/brain_mapping_refs/NON_EQUILIBRIUM_FINDING.md:146:- **W** (wake): canonical ~2.5 (our existing n=30 finding)
papers/aria-chess-paper/brain_mapping_refs/NON_EQUILIBRIUM_FINDING.md:151:- **REM**: another active regime, α likely closer to canonical wake
papers/aria-chess-paper/brain_mapping_refs/NON_EQUILIBRIUM_FINDING.md:159:have — Sleep-EDFx 30-subject PSGs with hypnogram stage labels.
papers/aria-chess-paper/brain_mapping_refs/NON_EQUILIBRIUM_FINDING.md:169:biological EEG signatures across multiple paradigms."
papers/aria-chess-paper/brain_mapping_refs/NON_EQUILIBRIUM_FINDING.md:179:computationally explicit. The signatures we match (SOC α, HCP
papers/aria-chess-paper/brain_mapping_refs/NON_EQUILIBRIUM_FINDING.md:202:2. ⏳ Map to sleep data: compute per-stage avalanche α on Sleep-EDFx
papers/aria-chess-paper/brain_mapping_refs/NON_EQUILIBRIUM_FINDING.md:206:5. ⏳ Re-run preregistered validation with proper reset — convert
papers/aria-chess-paper/brain_mapping_refs/NON_EQUILIBRIUM_FINDING.md:208:6. 📋 Future: sleep deprivation data (OpenNeuro ds*), HCP-Lifespan
papers/aria-chess-paper/brain_mapping_refs/NON_EQUILIBRIUM_FINDING.md:247:  confounds (metabolism, neuromodulation, local dynamics).
papers/aria-chess-paper/paper/sections/03_substrate.tex:2:\section{The 600-cell response substrate}\label{sec:substrate}
papers/aria-chess-paper/paper/sections/03_substrate.tex:7:computed Laplacian spectrum. \S\ref{ssec:cphi} gives the response
papers/aria-chess-paper/paper/sections/03_substrate.tex:16:The 600-cell $\Rsixhundred$ has $120$ vertices in
papers/aria-chess-paper/paper/sections/03_substrate.tex:38:sizes. The 600-cell construction itself is
papers/aria-chess-paper/paper/sections/03_substrate.tex:75:for the Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism
papers/aria-chess-paper/paper/sections/03_substrate.tex:84:\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
papers/aria-chess-paper/paper/sections/03_substrate.tex:88:\begin{equation}\label{eq:cphi}
papers/aria-chess-paper/paper/sections/03_substrate.tex:117:enters. The condition-dependent self-injection coupling
papers/aria-chess-paper/paper/sections/03_substrate.tex:118:$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
papers/aria-chess-paper/paper/sections/03_substrate.tex:119:varies between conditions in~\S\ref{sec:chain}; it is reported
papers/aria-chess-paper/paper/sections/03_substrate.tex:120:explicitly per condition.
papers/aria-chess-paper/paper/sections/03_substrate.tex:155:cascade is a decomposition of operators on $\Rsixhundred$, and the
papers/aria-chess-paper/paper/sections/03_substrate.tex:156:choice of $\Rsixhundred$ as the active substrate is post-hoc justified
papers/aria-chess-paper/paper/sections/03_substrate.tex:162:\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
papers/aria-chess-paper/paper/sections/03_substrate.tex:168:\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:8:\S\ref{ssec:hcp} gives the HCP brain-graph H$_4$-transitive null.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:11:or, in the HCP case,
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:12:$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}})/\sigma_{\mathrm{HCP}}$.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:29:\textbf{Critical methodological detail.} Between successive depth
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:58:\caption{Chess preregistered tests (with reset, $n=25$ canonical
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:74:$^{\dagger}$ The 2026-04-18 preregistration combined the null-mapping
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:77:and P16 (conversation null); both pass. The 2026-04-18 preregistration
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:80:(\texttt{run\_preregistered\_validation.py}; the $\geq 50\%$ threshold
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:84:range. Verification at the preregistered $20$-perm setting is an open
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:87:$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:97:This is a $+40.6$pp lift on the LOO refinement; on the preregistered
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:107:substrate retains $65.4\%$ classification accuracy under random
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:115:unique; it is a description of the observed accuracy stack.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:126:\caption{Conversation preregistered tests.}
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:141:lift is $-4.4$pp, well within the preregistered neutrality band
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:146:selective-amplifier behaviour preregistered in 2026-04-18: in these
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:154:\subsection{HCP brain-graph H$_4$-transitive null
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:157:\textbf{Setup.} Reference cohort: Human Connectome Project (HCP)
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:158:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:171:\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:176:Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:178:Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:186:\noindent$^{\flat}$ The HCP across-subject standard deviation for the
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:190:the reported gap and $\sigma$, the implicit HCP sd is
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:197:\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:199:  HCP subjects have degree std below $2.0$.
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:202:\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:214:$120$ nodes; the HCP ICA-50 connectivity matrix has $50$ nodes. The
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:219:($\mathrm{ARIA}=68.54$ on a 120-node graph; $\mathrm{HCP}=19.72$ on a
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:220:50-node graph) and the $\sigma$-distance against the HCP
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:224:$\mathrm{PR}/|V|$ gives $\mathrm{ARIA}=0.571$ vs $\mathrm{HCP}=0.394$,
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:226:because the HCP subject distribution and the across-subject
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:265:($12$--$18$pp) is the domain-specific contribution. On HCP,
papers/aria-chess-paper/paper/sections/07_cross_domain.tex:271:\emph{selectively} amplifying (not unconditionally), and it is an
papers/aria-chess-paper/paper/sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
papers/aria-chess-paper/paper/sections/08_discussion.tex:15:Three things are claimed novel as a substrate witness:
papers/aria-chess-paper/paper/sections/08_discussion.tex:18:  real-cortex EEG signatures without fitted shape parameters on neural
papers/aria-chess-paper/paper/sections/08_discussion.tex:19:  data.} Once the 600-cell is chosen as the substrate, its graph
papers/aria-chess-paper/paper/sections/08_discussion.tex:23:  shape parameter is tuned to neural data); cascade-$\alpha$ matches
papers/aria-chess-paper/paper/sections/08_discussion.tex:24:  Sleep-EDFx within preregistered tolerance with pairwise CI overlap
papers/aria-chess-paper/paper/sections/08_discussion.tex:25:  on three reference ranges; six drug/sleep signatures pass at
papers/aria-chess-paper/paper/sections/08_discussion.tex:28:  against this many preregistered cortical correspondences from a
papers/aria-chess-paper/paper/sections/08_discussion.tex:39:\item \textbf{The 18/18 preregistered correspondences with no
papers/aria-chess-paper/paper/sections/08_discussion.tex:40:  threshold modification.} Every prediction in the preregistered set
papers/aria-chess-paper/paper/sections/08_discussion.tex:41:  passes at the preregistered thresholds. The two interaction tests
papers/aria-chess-paper/paper/sections/08_discussion.tex:42:  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
papers/aria-chess-paper/paper/sections/08_discussion.tex:52:wake). The $\Phi$ proxy (\S\ref{sec:chain}) is designed to be small
papers/aria-chess-paper/paper/sections/08_discussion.tex:57:on the propofol--wake state contrast. This is a consistency-of-direction
papers/aria-chess-paper/paper/sections/08_discussion.tex:71:The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
papers/aria-chess-paper/paper/sections/08_discussion.tex:74:Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
papers/aria-chess-paper/paper/sections/08_discussion.tex:80:circuits implement context rotation or partial emission. The 600-cell
papers/aria-chess-paper/paper/sections/08_discussion.tex:96:(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
papers/aria-chess-paper/paper/sections/08_discussion.tex:101:witness claims (six signatures, $18/18$, chess $+40.6$pp,
papers/aria-chess-paper/paper/sections/08_discussion.tex:102:HCP $\sigma$-distances) do not require any of the ACT theorems.
papers/aria-chess-paper/paper/sections/08_discussion.tex:119:\emph{substrate witness} for the family that ACT names; ACT is not the
papers/aria-chess-paper/paper/sections/08_discussion.tex:142:\emph{a hypothesis the substrate witness raises}, not as a proof.
papers/aria-chess-paper/paper/sections/08_discussion.tex:143:The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
papers/aria-chess-paper/paper/sections/08_discussion.tex:153:  matrix specifically, P4 ($C\!\times\!P$) required $N\!=\!20$ for
papers/aria-chess-paper/paper/sections/08_discussion.tex:154:  reliable detection at the preregistered threshold. The general
papers/aria-chess-paper/paper/sections/08_discussion.tex:171:The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
papers/aria-chess-paper/paper/sections/08_discussion.tex:188:\subsection{Open questions raised by the substrate witness}
papers/aria-chess-paper/paper/sections/08_discussion.tex:191:\item Do the six drug/sleep signatures replicate across $10$--$20$
papers/aria-chess-paper/paper/sections/08_discussion.tex:203:\item Does the Sleep-EDFx three-way CI overlap survive on a different
papers/aria-chess-paper/paper/sections/08_discussion.tex:204:  EEG cohort (TUH, NHM)?
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:7:preregistered prediction was P4: $C\times P$ interaction
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:8:$\Delta_{CP} \geq +0.10$ on cascade-$\alpha$. The 2026-04-20
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:11:was walked back. Closing this gap without modifying the preregistered
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:20:For the four ablation conditions $\{----, -C--, --P-, -CP-\}$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:25:\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:26:        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:29:four conditions.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:58:\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:60:\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:67:\textbf{Per-condition means at \texorpdfstring{$N\!=\!20$}{N=20}.}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:72:\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:76:condition & mean $\alpha$ & std & sem \\
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:86:\textbf{Main effects at \texorpdfstring{$N\!=\!20$}{N=20}.}
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:87:$C$ main effect $= +0.456$ (turning $C$ off raises $\alpha$);
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:88:$P$ main effect $= -0.218$ (turning $P$ off lowers $\alpha$).
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:101:\item $0/2000$ bootstrap resamples were below the preregistered
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:112:\textbf{The 95\% CI is entirely above the preregistered $+0.10$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:115:were below the preregistered $+0.10$ floor, reported as $0.0000$.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:117:\textbf{Architectural reading (substrate witness).} $C$ creates churn
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:144:\item It does not establish that the substrate is uniquely selected by
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:146:\item It does not establish an $\eta$-trajectory derivation; $\eta$
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:147:  is treated as a condition-dependent constant in this paper.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:150:test of one preregistered interaction prediction, on a fresh-seed
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:159:P4 ($C\times P$) required $N\!=\!20$ fresh seeds for reliable detection
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:160:at the preregistered threshold; P3 ($D\times C$) closed at $N\!=\!5$.
papers/aria-chess-paper/paper/sections/06_stress_tests.tex:161:The original 3-seed preregistered validation gave estimates consistent
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:4:It records the most recent run of the preregistered validation harness
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:5:plus the N=20 deep-dive on the residual P4 prediction.*
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:8:> 18 / 18 with N=20 deep-dive on the residual P4.** Original 15/18
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:12:> condition, (b) `homeostatic_reset(level=1.0)` wired in between depth
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:13:> measurements for chess LOO, and (c) N=20 fresh-seed replication of
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:15:> set is fully validated against preregistered thresholds.
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:23:Eighteen quantitative predictions were frozen on **2026-04-18** in
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:27:`run_preregistered_validation.py` — git-tracked, deterministic given
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:39:- All EEG/sleep deterministic re-runs passed (P6, P7, P8).
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:45:  - **P4** (C×P synergy): observed +0.044 at N=3, below +0.10 floor.
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:50:- "P3, P4 walked back to 'preliminary, requires larger N'."
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:59:1. **Cascade block N bumped 3 → 5** for P2, P3, P4, P5 conditions
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:60:   in `run_preregistered_validation.py`. The original 3 seeds was
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:61:   the source of high-variance failure on P3 and P4.
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:69:3. **N=20 deep-dive** on the residual P4 (`demo_p4_cxp_deep_dive.py`):
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:72:   `P4_SYNERGY_FINDING.md` for the standalone report.
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:80:| ID | Claim | Threshold | 2026-04-20 (3-seed) | **2026-04-29 (5-seed + reset + N=20 P4)** | Verdict |
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:85:| P4 | C×P synergy | ≥ +0.10 | +0.044 ❌ | **+0.190 at N=20, CI [+0.143, +0.239]** | ✅ at N=20 |
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:87:| P6 | Real EEG α | ∈ [2.0, 3.0] | 2.513 ✅ | **2.513** | ✅ |
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:99:| P18 | HCP ICA-50 degree std | > 2.0 | 3.388 ✅ | **3.388** | ✅ |
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:125:cascade-α" is **supported** by the N=5 re-run within the preregistered
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:130:### 3.2 P4 — C×P synergy
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:133:`P4_SYNERGY_FINDING.md` for the full story.
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:142:**N=20 fresh-seed deep-dive (`demo_p4_cxp_deep_dive.py`, seeds 32000–32019):**
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:151:The 95% CI is **entirely above the preregistered +0.10 threshold**.
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:155:(per-seed std = 0.089 at N=20).
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:161:`P4_SYNERGY_FINDING.md` for the mechanistic interpretation.
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:186:original LOO test ran six consecutive depth measurements (n=5, 15, 25,
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:216:### 4.2 Real EEG and sleep-stage signatures (P6, P7, P8)
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:218:These are deterministic re-runs against fixed Sleep-EDFx datasets:
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:219:- **P6**: Real EEG spindle α = 2.513 (n=30 subjects). Inside [2.0, 3.0].
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:252:### 4.5 HCP brain-graph comparison (P17, P18)
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:255:- **P18**: HCP ICA-50 degree std = 3.388 (n=100 subjects, density-
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:262:## 5. The 18/18 verdict
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:264:**Standard validation tally:** 17/18 (the residual P4 fails at N=5).
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:265:**Including the N=20 deep-dive:** 18/18 (P4 passes decisively at N=20).
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:267:The empirical tally is **18/18 at adequate replication**. Two of the
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:269:improvements (5-seed cascade block + reset protocol). The third (P4)
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:275:All eighteen preregistered predictions are **supported by the data
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:276:within preregistered thresholds**, with the methodological caveat
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:277:that two interaction tests (P3, P4) require N ≥ 5 and N ≥ 20
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:286:> *"All eighteen preregistered predictions pass at empirical thresholds.
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:288:> homeostatic reset between LOO depth measurements) give 17/18; the
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:289:> residual prediction (P4 — C×P synergy) requires higher-N replication
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:290:> (we used N=20 fresh seeds) due to the high per-seed variance of
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:291:> interaction-term estimates. With adequate N, P4 passes decisively
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:293:> ~90% above the preregistered floor, indicating C and P are strongly
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:310:within the preregistered |·| < 0.20 band, confirmed at N=5.
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:313:### 6.2 Original walk-back on P4 (C×P synergy)
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:318:**Now reads:** C×P synergy is +0.190 [+0.143, +0.239] at N=20, ~90%
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:319:above preregistered. C and P are strongly coupled cascade-state
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:328:**Partially retained.** The state-dependence observation is a real
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:338:The original validation methodology — 18 preregistered predictions
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:343:reset. The fact that this gave 18/18 (with N=20 P4) where the
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:364:# Standard validation (17/18, ~18 min)
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:366:python3 run_preregistered_validation.py
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:368:# P4 N=20 deep-dive (~28 min)
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:372:JSON results are saved to `~/.aria/preregistered_validation/results_*.json`.
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:378:per-condition means in this document to 4 decimal places.
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:384:- `docs/brain_mapping/PAPER_PREDICTIONS.md` — frozen 2026-04-18
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:387:- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — standalone N=20 report
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:389:- `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` — six
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:390:  drug/sleep EEG signatures (independent of preregistered set, on
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:396:- `run_preregistered_validation.py` — validation harness
papers/aria-chess-paper/brain_mapping_refs/VALIDATION_RESULTS_2026-04-29.md:397:- `demo_p4_cxp_deep_dive.py` — N=20 deep-dive script
papers/aria-chess-paper/brain_mapping_refs/PREREG_H4_FINGERPRINT.md:11:and requires a new preregistered document.
papers/aria-chess-paper/brain_mapping_refs/PREREG_H4_FINGERPRINT.md:37:**Current status: existing n=30 Sleep-EDFx gives 2.51, so default prior
papers/aria-chess-paper/brain_mapping_refs/PREREG_H4_FINGERPRINT.md:53:- **Rereferencing:** common average (scalp EEG) or bipolar (ECoG) where
papers/aria-chess-paper/brain_mapping_refs/PREREG_H4_FINGERPRINT.md:110:1. Sleep-EDFx wake (n ≥ 30)
papers/aria-chess-paper/brain_mapping_refs/PREREG_H4_FINGERPRINT.md:119:- `~/.aria/datasets/physionet_sleep_edfx/` — wake stage W only
papers/aria-chess-paper/brain_mapping_refs/PREREG_H4_FINGERPRINT.md:133:Staged after H1. Preregistration of H4 details deferred to a later
papers/aria-chess-paper/brain_mapping_refs/PREREG_H4_FINGERPRINT.md:150:- Primary dataset: ds003708 ECoG (76 channels) for pilot; HCP MEG for
papers/aria-chess-paper/brain_mapping_refs/PREREG_H4_FINGERPRINT.md:171:Targets: h = 12 and h = 120, both preregistered.
papers/aria-chess-paper/brain_mapping_refs/PREREG_H4_FINGERPRINT.md:194:- Section 4: interpretation under full H₄ framework.
papers/aria-chess-paper/brain_mapping_refs/PREREG_H4_FINGERPRINT.md:195:- Section 5: rescues considered and rejected / accepted (preregistered).
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:3:*Standalone publishable finding from N=20 seed deep-dive on the residual P4
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:4:preregistered prediction. Compiled 2026-04-29.*
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:11:> preregistered prediction of ≥+0.10. The original 3-seed preregistered
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:20:## 1. Background: what was preregistered, what failed at N=3
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:24:ARIA's substrate is the 600-cell regular 4-polytope (120 vertices,
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:48:### 1.2 The preregistered predictions for D/C/P/E mechanisms
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:50:Predictions frozen 2026-04-18 in `docs/brain_mapping/PAPER_PREDICTIONS.md`:
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:57:| **P4** | **C×P synergy ≥ +0.10** | ≥ +0.10 |
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:60:**P4 was the genuine architectural prediction:** because C creates variety
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:63:contribution to cascade-α. The preregistered floor was +0.10 — stating
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:68:Original validation (2026-04-20, 3 seeds per condition):
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:87:This was below the +0.10 threshold, so P4 was reported as a **fail**
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:94:N=20 deep-dive presented below shows this was wrong.**
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:98:## 2. The N=20 deep-dive (2026-04-29)
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:102:We ran the same 4-condition ablation (baseline, -C--, --P-, -CP-) at:
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:125:### 2.2 Per-condition means at N=20
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:143:### 2.3 Main-effect estimates at N=20
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:171:**The 95% CI is entirely above the preregistered +0.10 threshold.**
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:177:For each seed (paired across the four conditions), we can compute that
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:191:per-seed std at N=20 (0.089) is just under half the per-seed std at
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:193:N=20 reveals a clean, narrow positive distribution.
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:220:   30040–30054 across the four conditions; the deep-dive used 31000–31009
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:227:landed on outliers; the N=20 sample (32000–32019) had std 0.089. **The
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:228:correct interpretation is that the original test was Type II underpowered
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:233:| Effect | N=3 / N=5 estimate | N=20 estimate | Shift |
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:245:## 4. Mechanistic interpretation
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:281:the N=20 deep-dive — is that these are mostly orthogonal. Losing one
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:284:The N=20 result reverses this. **Strong inter-mechanism coupling is the
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:300:### 5.1 The corrected paper claim on P4
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:304:> *"P4 (C×P synergy ≥+0.10) failed at +0.04 in 3-seed validation. We
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:308:**New framing (2026-04-29, with N=20 result):**
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:310:> *"P4 (C×P synergy ≥+0.10) was preregistered with a +0.10 floor.
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:313:> interaction term. Replication at N=20 fresh seeds (32000–32019)
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:334:### 5.3 The 18/18 verdict
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:336:P4 was the residual gap in the 17/18 validation re-run from earlier in
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:337:this session. With the N=20 deep-dive, the synergy is decisively above
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:338:the preregistered floor. **Effectively, all eighteen preregistered
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:364:**Output:** Per-condition seed-by-seed alphas, main-effect estimates,
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:368:**Verification:** seeds 32000–32019 should give the per-condition means
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:377:1. **One seed range tested at N=20.** A second N=20 run at a different
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:383:   well-powered N=20 estimate.
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:395:   (with one large positive outlier and two negatives) while N=20 has a
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:404:The C×P interaction in ARIA's cascade ablation matrix was preregistered
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:420:from the preregistered prediction set, taking the empirical tally from
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:421:17/18 to 18/18.
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:427:- `demo_p4_cxp_deep_dive.py` — N=20 script (this work)
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:430:- `run_preregistered_validation.py` — original cascade-block test
papers/aria-chess-paper/brain_mapping_refs/P4_SYNERGY_FINDING.md:431:- `docs/brain_mapping/PAPER_PREDICTIONS.md` — frozen 2026-04-18
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:3:**Frozen: 2026-04-18** — predictions below were locked before running
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:5:`CASCADE_FINDINGS.md` (pairwise ablations, multi-subject EEG,
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:6:conversation + chess closed-loop, HCP registration).
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:41:- **Run**: Fresh seeds, 4 conditions, compute interaction term.
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:43:### P4. C×P synergy is positive and substantial
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:48:- **Run**: Fresh seeds, 4 conditions.
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:55:- **Run**: Fresh seeds, conditions ---- vs ---E.
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:59:## Predictions 6-8: EEG spindle & state analysis
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:61:### P6. Real EEG spindle α is in the SOC range
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:62:- **Claim**: On the existing 30 Sleep-EDFx subjects, pooled spindle α
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:67:- **Run**: `bootstrap_alpha_ci` with fresh seed on already-computed
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:148:## Predictions 17-18: HCP structural registration
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:157:### P18. HCP ICA-50 has non-trivial degree std
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:159:  same), group-averaged HCP graph has **degree std > 2.0** at
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:164:- **Run**: Deterministic recompute (HCP data is fixed).
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:168:## Meta-claims (reported but not tested)
papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md:192:We do not expect 18/18 — some are noisy empirical tests and statistical
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:1:# Consciousness Chain v4 — Six EEG Signatures Reproduced
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:3:*Validation of ARIA's consciousness chain against six pre-registered drug/sleep
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:4:EEG signatures. All six pass with biologically realistic stimulus models on a
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:6:that already matched real EEG cascade-α inside 95% CI).*
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:15:recurrence on the 600-cell with bounded-top-K thresholding) plus
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:16:`phi_iit_trajectory` (cross-irrep auto-correlation transport) — reproduces
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:17:**six distinct quantitative drug/sleep signatures** observed in real EEG and
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:20:The six signatures span four conditions (WAKE, SLEEP_N3, PROPOFOL, RECOVERY)
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:22:single self-coupling parameter η changing across conditions. Each signature
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:23:has a published reference and a falsifiable threshold; all six pass.
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:26:stimulus-model artefacts in `demo_wake_alpha_diagnosis.py`) to 6/6 by
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:32:| 1 | Sleep variance ratio | NREM-N3 EEG (Lee 2017, Jobst 2017) | ratio ≈ 0.365 | 0.463 | ✓ within 30% |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:33:| 2 | Propofol switching ↑ | OpenNeuro ds005620 (n=8, 2.96×) | ratio in [1.5, 5.0] | 1.83× | ✓ |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:34:| 3 | Propofol continuity ↓ | EEG microstate (Brodbeck 2012) | drop > 0.020 | +0.066 | ✓ |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:35:| 4 | Propofol Φ collapse | IIT prediction (Tononi 2008) | ratio < 0.5 | 0.33× | ✓ |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:36:| 5 | Recovery reversibility | clinical anaesthesia | identical to wake | 0 diff | ✓ |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:37:| 6 | Cortical avalanche α | Sleep-EDFx n=30 (α=2.51 [2.50, 2.53]) | α ∈ [1.5, 3.5], R² > 0.85 | 2.252 [1.82, 2.86] R²=0.956 | ✓ |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:40:**ARIA WAKE α CI [1.82, 2.86] overlaps real Sleep-EDFx EEG CI [2.50, 2.86]
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:58:ψ_thresh =  bounded_topk(ψ, k=12)             # critical nonlinearity
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:63:**The bounded_topk(k=12) thresholding is the load-bearing nonlinearity.**
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:65:α ≈ 1.09 (no avalanches). Adding bounded_topk(k=12) drives α to 3.20 with
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:69:η is the only condition-dependent architectural parameter:
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:74:### 2. phi_iit_trajectory — principled IIT integration
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:87:information. This is a port of the published `integrated_information_phi_irrep`
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:119:def wake_source(t, rng):
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:195:All four conditions run for 800 ticks at seed = 42, k_threshold = 12.
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:207:**Prediction:** N3 sleep collapses cortical state-variance to ≈ 36.5% of wake.
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:208:Source: prior real Sleep-EDFx W→N3 analysis (n=24, ratio = 0.365), confirmed
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:220:### Signature 2 — Propofol regime-switching ↑
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:222:**Prediction:** Propofol increases the rate of phenomenological-state
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:223:transitions ~3× over wake. Source: OpenNeuro ds005620 (n=8 propofol EEG,
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:235:### Signature 3 — Propofol continuity ↓
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:237:**Prediction:** Propofol disrupts stream continuity (binding + valence +
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:249:### Signature 4 — Propofol Φ collapse (IIT)
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:251:**Prediction:** Propofol collapses integrated information Φ to <50% of wake.
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:264:### Signature 5 — Recovery reversibility
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:266:**Prediction:** Removing propofol restores the wake state exactly. Source:
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:280:cortical avalanche literature; ARIA prior cascade pipeline; Sleep-EDFx
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:281:EEG spindle α.
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:286:- Real Sleep-EDFx EEG CI [2.50, 2.86] (n=30 subjects, prior preregistration)
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:290:R² = 0.956 is the cleanest single-condition power-law fit observed in the
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:291:project, beating both v3 PROPOFOL (R²=0.93) and the n=30 EEG fit (R²~0.85).
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:293:**Mechanism:** The bounded_topk(k=12) thresholding is the critical
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:306:`demo_wake_alpha_diagnosis.py` tested four hypotheses against the v3 result:
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:316:inside real EEG CI with R²=0.94 — the substrate produces clean cortical
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:329:- **v4.final**: AR(1) β=0.90 + tonic shell + episodes 20-50 amp 0.8 anchored to shell + within-shell rotation → 6/6
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:332:component matches a feature of real wake cortical input.
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:345:- k_threshold: 12 (cortical band; bounded_topk nonlinearity)
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:346:- Run length: 800 ticks per condition
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:357:- The deterministic 600-cell substrate with bounded_topk thresholding
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:358:  reproduces six independent quantitative signatures of conscious vs
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:359:  unconscious states observed in real EEG.
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:362:- All six signatures pass under preregistered thresholds.
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:373:  preregistered validation methodology).
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:376:  "exact match" — only "within preregistered tolerance."
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:378:  three-way overlap with both real EEG and ARIA prior pipeline.
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:386:| `demo_drug_sleep_v4.py` | The 6/6 demo script — single deterministic run |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:387:| `demo_wake_alpha_diagnosis.py` | The diagnostic that proved v3 partials were stim artefacts |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:389:| `kernel/self_model_stream.py` | SelfModelLoop with bounded_topk(k=12) |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:390:| `kernel/consciousness_binding.py` | phi_iit_trajectory + bind_phenomenal_field |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:392:| `kernel/lyapunov_selector.py` | bounded_topk thresholding |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:393:| `docs/brain_mapping/CASCADE_VALIDATION_REPORT.md` | Companion report (cascade pipeline n=30 EEG) |
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:399:- `project_consciousness_chain_v4_six_of_six.md` — this work
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:401:- `project_wake_alpha_diagnosed.md` — diagnostic isolating stim-model cause
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:406:  (n=30 Sleep-EDFx, α=2.51 [2.50, 2.53])
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:412:ARIA's consciousness chain — a Green-response substrate on a 600-cell
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:414:self-loop — reproduces six independent drug/sleep EEG signatures. Each
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:416:power law in the wake-state band (passes with α = 2.252, 95% CI [1.82, 2.86]
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:417:overlapping the real Sleep-EDFx CI [2.50, 2.86]), NREM-N3 variance collapse to
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:418:~37% of wake (passes at 0.46), propofol regime-switching elevation (passes at
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:420:in the IIT direction (passes at 0.33× wake), and recovery reversibility (passes
papers/aria-chess-paper/brain_mapping_refs/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:423:episodes for wake; slow waves plus spindle bursts plus K-complexes for N3 —

exec
/bin/bash -lc "nl -ba papers/aria-chess-paper/paper/sections/05_results.tex | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba papers/aria-chess-paper/paper/sections/10_conclusion.tex | sed -n '1,130p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba papers/aria-chess-paper/paper/sections/09_limitations.tex | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "nl -ba papers/aria-chess-paper/README.md | sed -n '1,130p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 220ms:
     1	# aria-chess paper bundle
     2	
     3	Maintenance copy of the aria-chess substrate-witness paper for publishing. The
     4	upstream development repo is `aria-chess` (the GitHub repo cited in the paper's
     5	`@misc{ariaChessRepo}` bibtex entry); this bundle is the publication-ready
     6	artifact, kept here so the paper and its supporting evidence can be edited and
     7	released from this repo.
     8	
     9	## Layout
    10	
    11	```
    12	papers/aria-chess-paper/
    13	├── README.md                          (this file)
    14	├── TASK-aria-paper-completion.md      (work order; see also docs/codex-derive/)
    15	├── paper/
    16	│   ├── main.tex                       LaTeX source (212 lines)
    17	│   ├── main.pdf                       Built PDF (247 KB)
    18	│   ├── references.bib                 Bibliography (180 lines)
    19	│   ├── README.md                      Paper-specific build/repro notes
    20	│   ├── sections/01..10_*.tex          Ten section files (~1900 lines total)
    21	│   └── figures/                       (empty placeholder)
    22	└── brain_mapping_refs/
    23	    ├── PAPER_PREDICTIONS.md                    Preregistration frozen 2026-04-18 (P1–P18)
    24	    ├── PREREG_H4_FINGERPRINT.md                Later prereg battery (2026-04-24)
    25	    ├── PREREG_RUNG_OBSERVABLES.md              Later prereg battery (2026-04-24)
    26	    ├── VALIDATION_RESULTS_2026-04-29.md        18/18 tally with thresholds
    27	    ├── CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md    Six EEG signatures, per-condition
    28	    ├── P4_SYNERGY_FINDING.md                   N=20 C×P deep-dive
    29	    ├── CROSS_DOMAIN_RESULTS.md                 Chess / conversation / HCP
    30	    └── NON_EQUILIBRIUM_FINDING.md              State-reset protocol
    31	```
    32	
    33	## What's here
    34	
    35	The publication-ready paper plus the eight supporting `brain_mapping/*.md`
    36	documents the paper text references for preregistration provenance, validation
    37	results, and protocol detail. These are the artifacts a reviewer needs to verify
    38	the paper's claims at the documentation level.
    39	
    40	## What's intentionally not here
    41	
    42	- **Validation scripts** (`demo_drug_sleep_v4.py`, `demo_p4_cxp_deep_dive.py`,
    43	  `run_preregistered_validation.py`, `run_chess_robustness.py`,
    44	  `reproduce_paper_claims.sh`) — these live in the upstream `aria-chess` repo
    45	  cited via `@misc{ariaChessRepo}` in `paper/references.bib`. The paper §2
    46	  provenance ledger names them so a reviewer can locate them; the bundle isn't
    47	  meant to be a self-contained execution environment.
    48	- **Kernel modules** (`kernel/vfd_closure_kernel.py`, `kernel/sigma_orbit_basis.py`,
    49	  `kernel/dimensional_monitor.py`, `kernel/cascade_descent.py`,
    50	  `kernel/lyapunov_selector.py`, `kernel/self_model_stream.py`,
    51	  `kernel/consciousness_binding.py`, `kernel/consciousness_tensor.py`) — same
    52	  reasoning; ~5,000 lines of repository infrastructure, cited by file:line in
    53	  the paper, but not part of the publication artifact itself.
    54	- **`paper/results.json`, `paper/paper_summary.md`** (in upstream `aria-chess/paper/`) —
    55	  these belong to a *different* paper draft titled "The H₄ Oscillator Law"
    56	  and are not associated with this substrate-witness manuscript. Deliberately
    57	  excluded.
    58	- **`docs/brain_mapping/MANUSCRIPT_V2.md`** — earlier 1253-line draft form of the
    59	  same paper. The `.tex` paper is the canonical publication form; including
    60	  the older draft alongside would create reader confusion about which document
    61	  is canonical.
    62	
    63	## Building the paper
    64	
    65	```bash
    66	cd paper/
    67	tectonic main.tex
    68	# or pdflatex main / bibtex main / pdflatex main / pdflatex main
    69	```
    70	
    71	The build is self-contained — no external file references needed for compilation.
    72	The references in the paper text to `docs/brain_mapping/*.md` are documentary
    73	mentions (the reviewer can find them in `brain_mapping_refs/` here, or in the
    74	upstream `aria-chess` repo).
    75	
    76	## Codex hostile-review trail
    77	
    78	The paper went through 8 codex review rounds before reaching `Publication ready: yes`:
    79	
    80	- Reviews: `docs/reviews/aria-chess-paper-2026043​0T*.md` (eight passes, in this repo)
    81	- Round 7 (b) substantive verdict: *"No over-claim, scope-drift, or numerical inconsistency found."*
    82	- Round 8 (c) verdict: **`Publication ready: yes`** — last cosmetic line-wrap fixed.
    83	
    84	## Known paper-text issues (worth fixing before journal submission)
    85	
    86	- §2 Provenance ledger cites two scripts that **don't exist in upstream**:
    87	  `run_conversation_robustness.py` and `run_hcp_validation.py`. Either create
    88	  thin wrappers in upstream (preferred — the underlying logic exists in
    89	  `run_preregistered_validation.py` and the HCP analysis pipeline) or change
    90	  the paper text to point to the existing combined script. Not blocking for
    91	  preprint; would surface under journal review.
    92	
    93	## Scope discipline (locked)
    94	
    95	This is a **substrate witness**, not a selection theorem. The paper does not
    96	claim:
    97	- the substrate IS consciousness;
    98	- 600-cell uniqueness among regular 4-polytopes;
    99	- a Lyapunov function on the reduced flow has been delivered;
   100	- the ACT 4-tuple bridge delivers a selection theorem here.
   101	
   102	The 18/18 preregistered tally is reported as methodology refinement (no
   103	threshold modified). See `paper/sections/01_introduction.tex` claim-boundary box
   104	and `paper/sections/09_limitations.tex` five-move guard matrix.

 succeeded in 250ms:
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
    45	\caption{Six drug/sleep signatures with literature references.}
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

 succeeded in 239ms:
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

 succeeded in 231ms:
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

exec
/bin/bash -lc "rg -n \"citep\\{(["'^}]*)'"\\}\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc "rg -n \"label\\{|ref\\{\" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "overlap|three-way|pairwise|Sleep-EDFx|prior cascade|P3|P13|standard validation|methodology refinement|state-reset" papers/aria-closure-kernel/paper/main.tex papers/aria-closure-kernel/paper/sections/07_active_witness.tex papers/aria-chess-paper/paper/main.tex papers/aria-chess-paper/paper/sections/05_results.tex papers/aria-chess-paper/paper/sections/09_limitations.tex' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
exec
/bin/bash -lc 'rg -n "round_spectrum|laplacian_spectrum_grouped|eigenvalue|spectrum =" papers/aria-closure-kernel/repro/verify_kernel.py papers/aria-closure-kernel/repro/results.json' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 332ms:
papers/aria-closure-kernel/paper/sections/09_limitations.tex:7:template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
papers/aria-closure-kernel/paper/sections/09_limitations.tex:28:substrates from~\citep{SmartBAnomaly2026}; the aria-chess
papers/aria-closure-kernel/paper/sections/09_limitations.tex:140:preprint~\citep{SmartAdaptiveClosureTransport2026} and are not
papers/aria-closure-kernel/paper/sections/09_limitations.tex:153:  of the ACT companion paper~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartBAnomaly2026}; we
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:40:(verbatim from~\citep{SmartBAnomaly2026}, also at
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:47:from~\citep{SmartBAnomaly2026}; one fitted amplitude $A$ per
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:74:  anomaly~\citep{LHCbAngular2020} across all five independent
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:78:  vs $S$-basis factor $\sim 2.2$~\citep{KrugerMatias2005}) as
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:94:  metric, §3.4 of~\citep{SmartBAnomaly2026} — \emph{not} this
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:129:  preprint's limitations section~\citep{SmartBAnomaly2026}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:6:$\Cph$. The full preprint is~\citep{SmartAriaChess2026}; we
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:44:preregistered tally as reported in~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:97:  preprint~\citep{SmartAriaChess2026}), substrate routing lifts
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:162:Preprint           & b-anomaly~\citep{SmartBAnomaly2026} & aria-chess~\citep{SmartAriaChess2026} \\
papers/aria-closure-kernel/paper/sections/05_agreement.tex:116:b-anomaly paper~\citep{SmartBAnomaly2026} established
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:31:\item \textbf{Passive regime}~\citep{SmartBAnomaly2026}: a single
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:38:\item \textbf{Active regime}~\citep{SmartAriaChess2026}: a
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:69:4-tuple~\citep{SmartAdaptiveClosureTransport2026}; that paper's
papers/aria-closure-kernel/paper/sections/02_definition.tex:142:preprint~\citep{SmartAdaptiveClosureTransport2026} formulates the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:33:\item \textbf{ACT regulariser}~\citep{SmartAdaptiveClosureTransport2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:71:  Transport}~\citep{SmartAdaptiveClosureTransport2026}: the
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:76:\item \textbf{Aria-chess companion}~\citep{SmartAriaChess2026}:
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:129:  inherited verbatim from~\citep{SmartBAnomaly2026}.
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:133:  in~\citep{SmartAdaptiveClosureTransport2026} and not delivered
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:92:layer~\citep{SmartAriaChess2026} realises this block decomposition
papers/aria-closure-kernel/paper/sections/03_substrate.tex:11:not prove, here~\citep{CoxeterRegularPolytopes}. All facts in
papers/aria-closure-kernel/paper/sections/03_substrate.tex:59:into $S^{3}$~\citep{CoxeterRegularPolytopes}.
papers/aria-closure-kernel/paper/sections/03_substrate.tex:74:  in~\citep{CoxeterRegularPolytopes}).
papers/aria-closure-kernel/paper/main.tex:60:public flavour-physics datasets~\citep{SmartBAnomaly2026}, and an
papers/aria-closure-kernel/paper/main.tex:63:signatures~\citep{SmartAriaChess2026}.
papers/aria-closure-kernel/paper/main.tex:76:4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and \emph{not}
papers/aria-closure-kernel/paper/main.tex:91:direction~\citep{SmartBAnomaly2026}; (ii)~an eighteen-prediction
papers/aria-closure-kernel/paper/main.tex:94:signatures~\citep{SmartAriaChess2026}. We
papers/aria-closure-kernel/paper/main.tex:141:(a)~Passive regime, b-anomaly~\citep{SmartBAnomaly2026}: same
papers/aria-closure-kernel/paper/main.tex:148:aria-chess~\citep{SmartAriaChess2026}: same $\Cph$ on the same
papers/aria-closure-kernel/paper/main.tex:197:(b-anomaly~\citep{SmartBAnomaly2026},
papers/aria-closure-kernel/paper/main.tex:198:aria-chess~\citep{SmartAriaChess2026}) carry their own
papers/aria-closure-kernel/paper/sections/01_introduction.tex:90:  (a)~The b-anomaly preprint~\citep{SmartBAnomaly2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:96:  (b)~The aria-chess preprint~\citep{SmartAriaChess2026} uses the
papers/aria-closure-kernel/paper/sections/01_introduction.tex:128:  preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
papers/aria-closure-kernel/paper/sections/01_introduction.tex:145:preprint~\citep{SmartAriaChess2026}: numerical results

 succeeded in 321ms:
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:2:\section{Conclusion}\label{sec:conclusion}
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:17:$\mathbb{Z}[\Ph]$ values listed in Table~\ref{tab:spectrum}. The
papers/aria-closure-kernel/paper/sections/10_conclusion.tex:74:\textbf{Programme position.} \S\ref{sec:programme_home} positions
papers/aria-closure-kernel/paper/sections/05_agreement.tex:2:\section{Discrete-to-continuum agreement}\label{sec:agreement}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:16:\subsection{The test}\label{ssec:test}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:36:\subsection{Result on the unweighted Laplacian}\label{ssec:result_unweighted}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:42:  \S\ref{ssec:result_unweighted} below: $\psi$ is shell-constant
papers/aria-closure-kernel/paper/sections/05_agreement.tex:74:\subsection{Variant comparison}\label{ssec:variant_comparison}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:100:\label{tab:variant_correlation}
papers/aria-closure-kernel/paper/sections/05_agreement.tex:118:on the LHCb 2025 dataset (see \S\ref{sec:passive_witness} for the
papers/aria-closure-kernel/paper/sections/05_agreement.tex:152:an open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:2:\section{The Laplacian spectrum}\label{sec:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:8:Table~\ref{tab:spectrum} to machine precision; multiplicities sum
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:23:\label{tab:spectrum}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:65:\subsection{Operator-norm bound on $\Cph$}\label{ssec:opnorm_check}
papers/aria-closure-kernel/paper/sections/04_spectrum.tex:84:\label{ssec:irrep}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:2:\section{Programme home and the open selection layer}\label{sec:programme_home}
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:101:  generally strict (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:103:  described (\S\ref{sec:substrate}) and the Laplacian spectrum of
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:104:  Table~\ref{tab:spectrum}, both reproduced numerically
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:109:  $\Ph$-cocycle weighted controls (\S\ref{sec:agreement}).
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:112:  qualitatively distinct regimes (\S\ref{sec:passive_witness},
papers/aria-closure-kernel/paper/sections/08_programme_home.tex:113:  \S\ref{sec:active_witness}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:2:\section{The 600-cell substrate}\label{sec:substrate}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:9:the empirical landings (\S\ref{sec:limitations}); the
papers/aria-closure-kernel/paper/sections/03_substrate.tex:16:\subsection{Vertex set}\label{ssec:vertices}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:44:\subsection{Short-edge nearest-neighbour graph}\label{ssec:graph}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:53:\begin{equation}\label{eq:short_edge}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:80:\subsection{$9$-shell H$_3$ partition}\label{ssec:shells}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:86:\begin{equation}\label{eq:shell_inner}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:94:\begin{equation}\label{eq:shell_sizes}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:108:\subsection{Inner-product check}\label{ssec:inner_product_check}
papers/aria-closure-kernel/paper/sections/03_substrate.tex:110:The canonical short-edge criterion (Eq.~\eqref{eq:short_edge}) and
papers/aria-closure-kernel/paper/sections/03_substrate.tex:111:the canonical shell inner products (Eq.~\eqref{eq:shell_inner})
papers/aria-closure-kernel/paper/sections/03_substrate.tex:126:  Laplacian spectrum (\S\ref{sec:spectrum}).
papers/aria-closure-kernel/paper/sections/03_substrate.tex:129:  (\S\ref{ssec:opnorm}); the operator-norm bound
papers/aria-closure-kernel/paper/sections/03_substrate.tex:135:  (\S\ref{sec:passive_witness}, \S\ref{sec:active_witness}). A
papers/aria-closure-kernel/paper/sections/03_substrate.tex:137:  open build (\S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:2:\section{Passive-regime witness: b-anomaly}\label{sec:passive_witness}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:10:\subsection{What b-anomaly tests}\label{ssec:banomaly_setup}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:18:\begin{equation}\label{eq:banomaly_kernel}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:29:sign in Eq.~\eqref{eq:banomaly_kernel} reflects the b-anomaly
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:49:\label{tab:banomaly}
papers/aria-closure-kernel/paper/sections/06_passive_witness.tex:155:second landing is in \S\ref{sec:active_witness}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:2:\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:12:\subsection{Regime}\label{ssec:regime}
papers/aria-closure-kernel/paper/sections/09_limitations.tex:20:derivation. \emph{Disclosure:} \S\ref{sec:intro},
papers/aria-closure-kernel/paper/sections/09_limitations.tex:21:\S\ref{sec:substrate}, \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:23:empirical landings of \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/09_limitations.tex:24:\S\ref{sec:active_witness}. \emph{Strengthening build:}
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
papers/aria-closure-kernel/paper/sections/09_limitations.tex:159:  regular 4-polytopes — see \S\ref{ssec:regime}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:161:  specified large-graph limit — see \S\ref{ssec:interpretation}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:163:  \S\ref{ssec:posthoc}.
papers/aria-closure-kernel/paper/sections/09_limitations.tex:165:  polynomial-in-$L$ Lyapunov family — see \S\ref{sec:programme_home}.
papers/aria-closure-kernel/paper/sections/01_introduction.tex:2:\section{Introduction}\label{sec:intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:20:\begin{equation}\label{eq:cphi_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:30:\begin{equation}\label{eq:opnorm_intro}
papers/aria-closure-kernel/paper/sections/01_introduction.tex:35:$\Ph$ (\S\ref{sec:definition}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:43:(\S\ref{sec:limitations}); the construction itself is theorem-level
papers/aria-closure-kernel/paper/sections/01_introduction.tex:88:  (\S\ref{sec:passive_witness}).
papers/aria-closure-kernel/paper/sections/01_introduction.tex:188:\S\ref{sec:definition} gives the operator definition, the positivity
papers/aria-closure-kernel/paper/sections/01_introduction.tex:190:projection. \S\ref{sec:substrate} constructs $\Rsixhundred$ from
papers/aria-closure-kernel/paper/sections/01_introduction.tex:192:decomposition. \S\ref{sec:spectrum} reports the Laplacian spectrum
papers/aria-closure-kernel/paper/sections/01_introduction.tex:194:\S\ref{sec:agreement} runs the discrete-to-continuum agreement test
papers/aria-closure-kernel/paper/sections/01_introduction.tex:195:across three Laplacian variants. \S\ref{sec:passive_witness} and
papers/aria-closure-kernel/paper/sections/01_introduction.tex:196:\S\ref{sec:active_witness} thread the two independent empirical
papers/aria-closure-kernel/paper/sections/01_introduction.tex:198:\S\ref{sec:programme_home} positions $\Cph$ as the programme home
papers/aria-closure-kernel/paper/sections/01_introduction.tex:200:Millennium drafts. \S\ref{sec:limitations} enumerates limitations
papers/aria-closure-kernel/paper/sections/01_introduction.tex:201:in a five-move guard matrix. \S\ref{sec:conclusion} concludes.
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:2:\section{Active-regime witness: aria-chess}\label{sec:active_witness}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:10:\subsection{What aria-chess tests}\label{ssec:aria_setup}
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:22:  degree (\S\ref{ssec:graph}: degree $12$ uniform). The choice
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:157:\label{tab:two_witness}
papers/aria-closure-kernel/paper/sections/02_definition.tex:2:\section{The closure-response operator}\label{sec:definition}
papers/aria-closure-kernel/paper/sections/02_definition.tex:16:\begin{equation}\label{eq:cphi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:21:\begin{equation}\label{eq:psi}
papers/aria-closure-kernel/paper/sections/02_definition.tex:25:\subsection{Hypotheses on $(M, L_M)$}\label{ssec:hypotheses}
papers/aria-closure-kernel/paper/sections/02_definition.tex:27:The properties developed in \S\ref{ssec:positivity}--\S\ref{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:46:  \S\ref{ssec:opnorm}; H3 does not require a finite-dimensional
papers/aria-closure-kernel/paper/sections/02_definition.tex:57:  function in \S\ref{ssec:continuum});
papers/aria-closure-kernel/paper/sections/02_definition.tex:66:\subsection{Positive definiteness}\label{ssec:positivity}
papers/aria-closure-kernel/paper/sections/02_definition.tex:78:\subsection{Operator-norm bound}\label{ssec:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:82:\begin{equation}\label{eq:opnorm}
papers/aria-closure-kernel/paper/sections/02_definition.tex:88:case used in \S\ref{ssec:continuum}), this reduces to the identity
papers/aria-closure-kernel/paper/sections/02_definition.tex:89:\begin{equation}\label{eq:opnorm_zero_mode}
papers/aria-closure-kernel/paper/sections/02_definition.tex:93:intervals), Eq.~\eqref{eq:opnorm} gives the strict inequality
papers/aria-closure-kernel/paper/sections/02_definition.tex:102:\S\ref{ssec:opnorm_check}); this matches the closed-form $\Ph^{2}$
papers/aria-closure-kernel/paper/sections/02_definition.tex:105:\subsection{Continuum projection}\label{ssec:continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:111:\begin{equation}\label{eq:green_continuum}
papers/aria-closure-kernel/paper/sections/02_definition.tex:119:discrete-to-continuum agreement test (\S\ref{sec:agreement}):
papers/aria-closure-kernel/paper/sections/02_definition.tex:131:  the continuum decay scale $\Ph$ (Eq.~\eqref{eq:green_continuum})
papers/aria-closure-kernel/paper/sections/02_definition.tex:134:\item the continuum projection (Eq.~\eqref{eq:green_continuum})
papers/aria-closure-kernel/paper/sections/02_definition.tex:140:an open build (\S\ref{sec:limitations}). The companion
papers/aria-closure-kernel/paper/main.tex:46:is post-hoc motivated by those landings, \S\ref{sec:limitations};
papers/aria-closure-kernel/paper/main.tex:55:$G(x) = (\Ph/2)\,e^{-|x|/\Ph}$ (\S\ref{sec:agreement};
papers/aria-closure-kernel/paper/main.tex:128:\ref{tab:spectrum}, \S\ref{sec:substrate}).
papers/aria-closure-kernel/paper/main.tex:138:precision (multi-source sweep, \S\ref{sec:limitations}).
papers/aria-closure-kernel/paper/main.tex:194:in \S\ref{sec:substrate}, \S\ref{sec:spectrum}, and
papers/aria-closure-kernel/paper/main.tex:195:\S\ref{sec:agreement} are deterministic outputs of the script.

 succeeded in 381ms:
papers/aria-closure-kernel/repro/results.json:43:  "laplacian_spectrum_grouped": [
papers/aria-closure-kernel/repro/results.json:45:      "eigenvalue": -0.0,
papers/aria-closure-kernel/repro/results.json:49:      "eigenvalue": 2.291796067500629,
papers/aria-closure-kernel/repro/results.json:53:      "eigenvalue": 5.527864045000407,
papers/aria-closure-kernel/repro/results.json:57:      "eigenvalue": 8.999999999999993,
papers/aria-closure-kernel/repro/results.json:61:      "eigenvalue": 11.999999999999984,
papers/aria-closure-kernel/repro/results.json:65:      "eigenvalue": 13.999999999999977,
papers/aria-closure-kernel/repro/results.json:69:      "eigenvalue": 14.472135954999567,
papers/aria-closure-kernel/repro/results.json:73:      "eigenvalue": 14.999999999999988,
papers/aria-closure-kernel/repro/results.json:77:      "eigenvalue": 15.708203932499362,
papers/aria-closure-kernel/repro/verify_kernel.py:122:    """L = D - A; return sorted eigenvalues + eigenvectors."""
papers/aria-closure-kernel/repro/verify_kernel.py:129:def round_spectrum(w, decimals=6):
papers/aria-closure-kernel/repro/verify_kernel.py:130:    """Group eigenvalues into multiplicity classes (within numerical tol)."""
papers/aria-closure-kernel/repro/verify_kernel.py:378:    spectrum = round_spectrum(w, decimals=4)
papers/aria-closure-kernel/repro/verify_kernel.py:421:        "laplacian_spectrum_grouped": [
papers/aria-closure-kernel/repro/verify_kernel.py:422:            {"eigenvalue": ev, "multiplicity": m} for ev, m in spectrum
papers/aria-closure-kernel/repro/verify_kernel.py:445:    print("Laplacian spectrum (eigenvalue, multiplicity):")

 succeeded in 400ms:
papers/aria-chess-paper/paper/main.tex:81:preregistered tally is $17/18$ at standard validation methodology
papers/aria-chess-paper/paper/main.tex:82:($5$-seed cascade block plus state-reset protocol), and $18/18$ after
papers/aria-chess-paper/paper/main.tex:89:from the published literature (Sleep-EDFx CI for the wake $\alpha$,
papers/aria-chess-paper/paper/main.tex:99:This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
papers/aria-chess-paper/paper/main.tex:100:subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
papers/aria-chess-paper/paper/main.tex:101:pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
papers/aria-chess-paper/paper/main.tex:102:overlap.
papers/aria-chess-paper/paper/main.tex:135:preregistered estimator P13 was $5$-fold CV with threshold
papers/aria-chess-paper/paper/main.tex:166:the original preregistration closed by methodology refinement and
papers/aria-chess-paper/paper/main.tex:184:We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
papers/aria-chess-paper/paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:9:gives the three-way $\alpha$ overlap. We lift the result map
papers/aria-chess-paper/paper/sections/05_results.tex:52:   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
papers/aria-chess-paper/paper/sections/05_results.tex:67:   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
papers/aria-chess-paper/paper/sections/05_results.tex:78:thresholds are drawn from the literature (Sleep-EDFx CI for
papers/aria-chess-paper/paper/sections/05_results.tex:92:\textbf{Tally.} $17/18$ at standard validation
papers/aria-chess-paper/paper/sections/05_results.tex:94:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
papers/aria-chess-paper/paper/sections/05_results.tex:109:P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:120:\textbf{P13}$^{\ddagger}$ & Chess substrate lift (with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
papers/aria-chess-paper/paper/sections/05_results.tex:130:\noindent$^{\ddagger}$ P13 was preregistered with the substrate-lift
papers/aria-chess-paper/paper/sections/05_results.tex:137:methodology refinement (no threshold change).}
papers/aria-chess-paper/paper/sections/05_results.tex:139:\item P3 (D$\times$C interaction independence) was outside the band
papers/aria-chess-paper/paper/sections/05_results.tex:147:\item P13 (chess substrate lift): the 2026-04-18 preregistration
papers/aria-chess-paper/paper/sections/05_results.tex:163:requiring the documented state-reset protocol. The original $15/18$
papers/aria-chess-paper/paper/sections/05_results.tex:166:\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:168:The substrate's wake cascade-$\alpha$ confidence interval overlaps
papers/aria-chess-paper/paper/sections/05_results.tex:174:\caption{Three-way $\alpha$ overlap on the wake cascade-event power
papers/aria-chess-paper/paper/sections/05_results.tex:176:\label{tab:alpha_overlap}
papers/aria-chess-paper/paper/sections/05_results.tex:182:Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
papers/aria-chess-paper/paper/sections/05_results.tex:183:ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
papers/aria-chess-paper/paper/sections/05_results.tex:190:real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
papers/aria-chess-paper/paper/sections/05_results.tex:193:$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
papers/aria-chess-paper/paper/sections/05_results.tex:194:intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
papers/aria-chess-paper/paper/sections/05_results.tex:205:any specific subject (\S\ref{sec:chain}). Three-way overlap on the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:47:\item $17/18$ at standard validation methodology ($5$-seed
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:48:  cascade block plus state-reset protocol);
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:55:The aria-chess preprint reports this as methodology refinement
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:69:  interval overlaps both the Sleep-EDFx EEG CI $[2.50, 2.53]$
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:70:  ($n=30$ subjects) and aria-chess's prior cascade pipeline CI
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:71:  $[2.73, 3.25]$ pairwise (the Sleep-EDFx and prior-pipeline
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:72:  intervals do not overlap each other; the WAKE interval is the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:73:  pairwise common ground).
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:91:\item \textbf{Chess pattern recognition (P9--P13)}: $32$ chess
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:93:  disclosed leave-one-out / state-reset refinement of the
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:95:  prereg used $5$-fold cross-validation; the LOO/state-reset
papers/aria-closure-kernel/paper/sections/07_active_witness.tex:164:Datasets           & 5 public ($n_{\mathrm{tot}}=138$ bins) & prereg + EEG (HCP $n=1003$, Sleep-EDFx $n=30$, etc.) \\
papers/aria-chess-paper/paper/sections/09_limitations.tex:33:\emph{Evidence:} bootstrap CI on the wake 58 events, plus three-way
papers/aria-chess-paper/paper/sections/09_limitations.tex:34:overlap with two independent reference $\alpha$ ranges.
papers/aria-chess-paper/paper/sections/09_limitations.tex:122:than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
papers/aria-chess-paper/paper/sections/09_limitations.tex:134:threshold modification.} The reversals (P3, P4, P13) are documented
papers/aria-chess-paper/paper/sections/09_limitations.tex:137:the original failure values, the methodology refinement, and the
papers/aria-chess-paper/paper/sections/09_limitations.tex:141:builds for P3/P4/P13 above; no further claim is needed.

codex
**Claim Audit**

No direct hard-forbidden overclaim found: the paper does not claim `\varphi^{-2}` is derived, does not claim 600-cell uniqueness, does not claim kernel uniqueness, and does not deliver Lyapunov / `2I` / selection theorems.

Issues:

1. Active-witness tally under-discloses inherited methodology refinements. `main.tex:153-157` and `sections/07_active_witness.tex:46-57` frame the move from `17/18` to `18/18` mainly as the P4 `N=20` deep-dive. The companion also says P3 required `N=5` and P13 required LOO/state-reset refinement: `aria-chess-paper/paper/sections/05_results.tex:136-157`, `aria-chess-paper/paper/sections/09_limitations.tex:121-141`. Add this caveat wherever the headline tally appears.

2. The `0.976` per-vertex correlation is numerically correct but too easy to read as 119 independent radial samples in the abstract/headline: `main.tex:52-55`, `sections/01_introduction.tex:71-78`. Section 5 correctly discloses that it is shell-constant and multiplicity-weighted: `sections/05_agreement.tex:40-45`, `54-72`. Propagate “multiplicity-weighted shell-constant per-vertex correlation” into the first occurrence.

3. Reproducibility bundle mismatch: the paper says all section 3-5 numbers are deterministic script outputs, `main.tex:188-195`, but the current script rounds grouped spectrum eigenvalues before writing, `verify_kernel.py:129-143`, `378`, `421-423`, while `results.json` stores full-precision grouped eigenvalues, `results.json:43-79`. Either regenerate `results.json` with the current script or change the script to preserve full precision.

4. Programme-home material drifts beyond the operator-witness claim. `sections/04_spectrum.tex:58-63` and `sections/08_programme_home.tex:14-44`, `63-88` introduce forthcoming RH/YM/programme-family claims. They are marked non-load-bearing, but a referee will still treat them as claims needing support. Move to an appendix or remove.

**Internal Consistency**

The core operator numerics are internally consistent: spectrum, multiplicities, norm, and correlations match the stated values. The main internal weakness is presentation hierarchy: the rigorous operator-witness material is clean, while the active-witness and programme-position sections carry extra narrative load.

**External Consistency / Numerics**

`results.json` supports the required values: `|V|=120`, `|E|=720`, degree `12`, spectrum multiplicities summing to `120`, `||C_\varphi^{-1}||=2.6180339887`, per-vertex correlations `0.976/0.888/0.884`, and shell-mean unweighted `0.923`.

The b-anomaly inheritance is disciplined: AIC tie, Gaussian alternative, and Mode-B drift caveats are present with the right numbers. The aria-chess inheritance is mostly disciplined, but the P3/P13 methodology refinements need to be carried into the kernel paper’s headline tally. I did not rerun the script because this sandbox is read-only and the script writes `results.json`.

**Operator-Witness Scope Discipline**

Good overall. The paper repeatedly says this is an operator witness, not a derivation, uniqueness result, or selection theorem. The remaining scope risk is not a forbidden claim, but clutter: future programme notes make the manuscript look broader than the evidence it actually audits.

**Tightness**

Cut or appendicize the RH/YM/programme-home discussion. Keep the paper centered on: definition, 600-cell instance, spectrum/norm, discrete-continuum correlation, and carefully bounded inherited witnesses. Also reduce repeated abstracts-within-the-paper; the caveats are good, but repetition makes the argument look defensive.

**Surface Issues**

Define `2I` on first use. Fix the self-reference “See \S\ref{ssec:result_unweighted} below” inside the same subsection, `sections/05_agreement.tex:40-43`. Add stable URLs/commit identifiers for unpublished companion preprints in `references.bib:20-44`. Wrap the long conclusion line at `sections/10_conclusion.tex:22`.

**Top Three Fixes**

1. Add the full aria-chess methodology-refinement caveat: P3 `N=5`, P4 `N=20`, P13 LOO/state-reset, no threshold changes.
2. Sync `verify_kernel.py` and `results.json`, then state exactly which artifact is canonical.
3. Remove or appendix the programme/forthcoming-material claims and sharpen the first `0.976` description.

**Verdict**

Publication ready: no -- must-fix list above
tokens used
129,900
**Claim Audit**

No direct hard-forbidden overclaim found: the paper does not claim `\varphi^{-2}` is derived, does not claim 600-cell uniqueness, does not claim kernel uniqueness, and does not deliver Lyapunov / `2I` / selection theorems.

Issues:

1. Active-witness tally under-discloses inherited methodology refinements. `main.tex:153-157` and `sections/07_active_witness.tex:46-57` frame the move from `17/18` to `18/18` mainly as the P4 `N=20` deep-dive. The companion also says P3 required `N=5` and P13 required LOO/state-reset refinement: `aria-chess-paper/paper/sections/05_results.tex:136-157`, `aria-chess-paper/paper/sections/09_limitations.tex:121-141`. Add this caveat wherever the headline tally appears.

2. The `0.976` per-vertex correlation is numerically correct but too easy to read as 119 independent radial samples in the abstract/headline: `main.tex:52-55`, `sections/01_introduction.tex:71-78`. Section 5 correctly discloses that it is shell-constant and multiplicity-weighted: `sections/05_agreement.tex:40-45`, `54-72`. Propagate “multiplicity-weighted shell-constant per-vertex correlation” into the first occurrence.

3. Reproducibility bundle mismatch: the paper says all section 3-5 numbers are deterministic script outputs, `main.tex:188-195`, but the current script rounds grouped spectrum eigenvalues before writing, `verify_kernel.py:129-143`, `378`, `421-423`, while `results.json` stores full-precision grouped eigenvalues, `results.json:43-79`. Either regenerate `results.json` with the current script or change the script to preserve full precision.

4. Programme-home material drifts beyond the operator-witness claim. `sections/04_spectrum.tex:58-63` and `sections/08_programme_home.tex:14-44`, `63-88` introduce forthcoming RH/YM/programme-family claims. They are marked non-load-bearing, but a referee will still treat them as claims needing support. Move to an appendix or remove.

**Internal Consistency**

The core operator numerics are internally consistent: spectrum, multiplicities, norm, and correlations match the stated values. The main internal weakness is presentation hierarchy: the rigorous operator-witness material is clean, while the active-witness and programme-position sections carry extra narrative load.

**External Consistency / Numerics**

`results.json` supports the required values: `|V|=120`, `|E|=720`, degree `12`, spectrum multiplicities summing to `120`, `||C_\varphi^{-1}||=2.6180339887`, per-vertex correlations `0.976/0.888/0.884`, and shell-mean unweighted `0.923`.

The b-anomaly inheritance is disciplined: AIC tie, Gaussian alternative, and Mode-B drift caveats are present with the right numbers. The aria-chess inheritance is mostly disciplined, but the P3/P13 methodology refinements need to be carried into the kernel paper’s headline tally. I did not rerun the script because this sandbox is read-only and the script writes `results.json`.

**Operator-Witness Scope Discipline**

Good overall. The paper repeatedly says this is an operator witness, not a derivation, uniqueness result, or selection theorem. The remaining scope risk is not a forbidden claim, but clutter: future programme notes make the manuscript look broader than the evidence it actually audits.

**Tightness**

Cut or appendicize the RH/YM/programme-home discussion. Keep the paper centered on: definition, 600-cell instance, spectrum/norm, discrete-continuum correlation, and carefully bounded inherited witnesses. Also reduce repeated abstracts-within-the-paper; the caveats are good, but repetition makes the argument look defensive.

**Surface Issues**

Define `2I` on first use. Fix the self-reference “See \S\ref{ssec:result_unweighted} below” inside the same subsection, `sections/05_agreement.tex:40-43`. Add stable URLs/commit identifiers for unpublished companion preprints in `references.bib:20-44`. Wrap the long conclusion line at `sections/10_conclusion.tex:22`.

**Top Three Fixes**

1. Add the full aria-chess methodology-refinement caveat: P3 `N=5`, P4 `N=20`, P13 LOO/state-reset, no threshold changes.
2. Sync `verify_kernel.py` and `results.json`, then state exactly which artifact is canonical.
3. Remove or appendix the programme/forthcoming-material claims and sharpen the first `0.976` description.

**Verdict**

Publication ready: no -- must-fix list above
