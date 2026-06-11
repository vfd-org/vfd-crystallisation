# ARIA Closure-Response Green Kernel and the Cascade Programme

**Status (2026-04-29).** Programme-level vocabulary: response
primitive defined; externally witnessed by a structural sign-uniform
test (b-anomaly paper, §4 below) without a model-preference claim;
selection / crystallisation dynamics still open. This note is
non-load-bearing for any individual Millennium paper; it documents
the programme-wide home for the polynomial-in-$L$ Lyapunov family
that recurs across the Millennium drafts.

## 1. The closure-response operator

Let $M$ be a closure substrate (graph, simplicial complex, or
projected coordinate). Let $L_M$ be its Laplacian. Define the
**$\varphi$-regularised closure operator**
$$
C_\varphi \;=\; L_M + \varphi^{-2} I.
$$
For a non-negative localised source $f$ on $M$, the **closure
response field** is
$$
\psi \;=\; C_\varphi^{-1} f \;=\; (L_M + \varphi^{-2} I)^{-1} f.
$$
This is a Green's-function inverse. For self-adjoint non-negative
$L_M$ on $M$ (e.g. the standard graph Laplacian on a connected
finite graph, or the standard continuum Laplace operator with
free-space / decay-at-infinity boundary conditions), $C_\varphi$
is positive definite and $\varphi^{-2}$ acts as a coherence-length /
mass regularisation; for a non-negative source $f$ on such an $M$,
$\psi$ is non-oscillatory and centred on the support of $f$. In
the continuum case with smooth $f$, $\psi$ is regular away from
the singular support of $f$. (On a finite graph, "smoothness" is
not directly meaningful; the regularity statement is a discrete
exponential-decay envelope around the source, not a derivative
condition.) Substrates outside this hypothesis class (e.g.
projected coordinates with non-standard boundary conditions, or
Laplacians with negative spectrum) require their own analysis.

## 2. Continuum projection

In one projected coordinate $x$, $L_\varphi = -d^2/dx^2 + \varphi^{-2}$,
$L_\varphi G = \delta$, with closed-form Green's function
$$
G(x) \;=\; \frac{\varphi}{2}\, e^{-|x|/\varphi}.
$$
Normalised, this is the practical kernel
$\kappa(x) = e^{-|x|/\varphi}$. The decay scale is $\varphi$.

## 3. Discrete substrate: the 600-cell

The discrete VFD lift uses the 600-cell graph $V_{600}$:
- 120 vertices, 720 edges, each vertex degree 12;
- edges defined by $\langle v, w \rangle = \varphi/2$;
- 9-shell decomposition emerging intrinsically as
  $\{1, 12, 20, 12, 30, 12, 20, 12, 1\}$;
- antipodal symmetry $s(-v) = 8 - s(v)$.

The discrete response is
$\psi(v) = (L_{V_{600}} + \varphi^{-2} I)^{-1} f(v)$.

**Compression diagnostic.** The b-anomaly headline fits use the
full Green response on $V_{600}$. A spectral truncation diagnostic
(`archive/reports/wo011_spectral.csv`) reports the relative
reconstruction error stepping from $0.076$ (modes 1-8, with
$\lambda_{\max}$ reaching $5.528$ at mode 6) to $0.040$ (modes
9-14) and remaining at $0.040$ through mode 30; mode 15 marks the
entry of the truncation into the $\lambda = 9$ block, not an
additional error drop. This is a *spectral diagnostic of
compression depth*, not a rank-1 projection map; the b-anomaly
fits do not use the truncation. (The canonical full spectrum of
the $V_{600}$ Laplacian has eigenvalue $9$ with multiplicity $16$;
the multiplicity-6 figure originally reported in some prose is
not consistent with the canonical spectrum or with the b-anomaly's
own wo011 CSV and is dropped here.)

## 4. Empirical validation: shipped five-dataset b-anomaly structural test

Independent passive-regime witness for $C_\varphi$ ships in the
b-anomaly repository (`/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/`,
preprint `paper/main.pdf`, repro `repro/run_all.sh`). The witness is
a **structural** test, not a detection claim or AIC preference:

> A single fixed response kernel $\kappa(q^{2})$ — derived from the
> 600-cell $V_{600}$ graph regularised by $\varphi^{-2}$ as a
> discrete mass scale, with no shape parameters tuned to data —
> provides a consistent description of the $q^{2}$ behaviour of the
> $b\to s\mu^{+}\mu^{-}$ angular anomaly across **five public
> datasets covering two collaborations, two isospin partners, and
> three decay channels**. Only one dimensionless amplitude $A$ is
> fitted per dataset; the kernel shape itself never moves.

**Per-dataset table** (verbatim from `BANOMALY-001/vfd-b-anomaly/README.md`):

| dataset | decay | $n$ | non-linear $\Delta\mathrm{AIC}$ | best-fit $A$ | $\Delta C_{9}^{\mathrm{eff}}$ |
|---|---|---:|---:|---:|---:|
| LHCb 2015            | $B^{0}\!\to\!K^{*0}$           | 32 | $-0.24$ | $+1.24$ | $-0.96$ |
| LHCb 2021            | $B^{+}\!\to\!K^{*+}$           | 32 | $+0.17$ | $+2.06$ | $-1.59$ |
| CMS 2025 (no $P_{4}'$) | $B^{0}\!\to\!K^{*0}$           | 18 | $+0.47$ | $+1.05$ | $-0.81$ |
| LHCb 2025            | $B^{0}\!\to\!K^{*0}$           | 32 | $+1.09$ | $+1.14$ | $-0.86$ |
| LHCb 2015            | $B_{s}\!\to\!\phi$ ($S$-basis) | 24 | $-0.24$ | $+4.98$ | $-3.85$ |

**What the b-anomaly paper claims (source scope; bullets summarise from `README.md:24-28` plus paper §§6-7 detail):**

- **Universality.** Same fixed kernel for all five datasets, one
  amplitude per dataset, no shape retuning.
- **Sign uniformity.** $A>0$ in **5/5** fits;
  $\Delta C_{9}^{\mathrm{eff}}<0$ in **5/5** fits. The kernel
  reproduces the established direction of the anomaly across all
  five independent measurements.
- **Cross-channel ratio.** $B\to K^{*}$ vs $B_{s}\!\to\!\phi$
  amplitudes differ by a factor partly explained by the predicted
  Krüger–Matias $P$/$S$-basis amplification ($\sim 2.2$). The
  detailed cross-channel section reports a predicted amplitude of
  $+2.5$ vs the observed $+4.98$, leaving a factor $\sim 2$
  residual gap that the basis-amplification prediction does not
  account for.
- **Geometry-first variant test.** Of three discrete Laplacian
  variants, the unweighted choice wins on a pure-geometry criterion
  (correlation $0.997$ with the continuum kernel); the same variant
  also wins on the data $\chi^{2}$ — independent geometry and data
  criteria agree. The two-criterion agreement is criterion-independent
  but not historically blind: the b-anomaly limitations section
  (`paper/sections/09_limitations.tex`) acknowledges that the data
  was looked at first and only later verified to agree with the
  pure-geometry ranking.

**Statistical caveat (what the b-anomaly paper does NOT claim):**

- On Akaike model comparison, the kernel and a constant
  Wilson-coefficient shift ($\mathrm{FREE\_C9}$, also $k=1$) are
  statistically indistinguishable on current data: stacked
  $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$.
  Current data cannot resolve the model comparison. AIC is blind to
  the universality/shape-prediction claim itself.
- In the Mode-B stress test, a free-width Gaussian charm-loop
  proxy fits comparably in $\chi^{2}$ at the cost of one extra
  shape parameter; the kernel is *not* the unique $q^{2}$ shape
  consistent with the anomaly.
- An earlier linearised "Mode B" analysis gave a stronger
  numerical preference for the kernel
  ($\Delta\mathrm{AIC} = -1.67$ on LHCb 2025) that **did not
  survive the non-linear refit**. The $+2.77$-AIC-unit drift is the
  largest single methodological uncertainty in the project.

**Cocycle convergence (operator-level, not edge-weight-level).**
The b-anomaly geometry-first variant test compares three discrete
edge-weighting schemes on $V_{600}$ — `UNWEIGHTED`,
`PHI_GEOMETRIC` ($w_{vw} = \sqrt{\omega_+(v)\,\omega_+(w)}$ with
$\omega_+(v) = \varphi^{\kappa(v)}$), and `PHI_ARITHMETIC`
($w_{vw} = \tfrac{1}{2}[\omega_+(v) + \omega_+(w)]$) — under
both a pure-geometry criterion (correlation with the continuum
kernel) and a data criterion (LHCb 2025 $\chi^2$). The
`UNWEIGHTED` Laplacian variant wins on both criteria
(correlation $0.9968$ with the continuum kernel, data
$\chi^2 = 13.555$; b-anomaly paper §3.4 Table 1, also
`reports/wo016b_variant_geometry.md`). The φ-cocycle-weighted
variants ($\omega_+(v) = \varphi^{\kappa(v)}$) are tested and
**lose** on both criteria. So the b-anomaly result empirically
strengthens the **unweighted** $L_{V_{600}} + \varphi^{-2} I$
response operator and the 9-shell projection (which enters at the
shell-mean step, not as an edge weight); it does **not**
empirically strengthen the κ cocycle as an operative edge
weighting.

The cocycle convergence with the RH paper's pentagonal-clock
$\kappa(v) = (s(v) - 4)^2$ (`papers/millennium-rh-formal/rh-formal.tex`,
Definition `def:kappa`) is therefore **structural**: the same
shell-grade pattern $\varphi^{0,1,4,9,16}$ shows up in both the
discrete VFD lift's variant catalogue and the RH paper's cocycle.
This is a theoretical convergence on a shared algebraic shell-grade
infrastructure, not an empirical claim. ẑ **shares operator-level
infrastructure** with the b-anomaly response operator (the same
$V_{600} + \varphi^{-2} I$, the same 9-shell decomposition, the
same shell-grade pattern $\varphi^{0,1,4,9,16}$); ẑ does **not**
inherit any empirical claim about classical RH or the critical
line.

## 5. Programme home for cascade Lyapunov / projector functionals

Several cascade-internal constructions are $L$-symmetric
polynomial-in-$L$ functionals on a finite-dimensional substrate.
They are positioned as programme-proposed members of the same
family as $C_\varphi$ (the family-membership claim is not formally
canonical and is not proved in any of the cited Millennium drafts):

- **RH polynomial filter** (`rh-formal.tex`,
  `def:closure_flow`): $F_{\mathrm{filt}}(x)
  = \tfrac{1}{2}\langle x, p_{\mathrm{fix}}(L)^2 x\rangle$ with
  $\Psi_t = e^{-t\,p_{\mathrm{fix}}(L)^2}$. Programme-positioned
  as the **σ-fix-annihilator** instance of the family: a
  degree-$10$ positive functional on $\R^{120}$ vanishing exactly
  on $V_{\mathrm{fix}}$.
- **YM cascade gap operator** (`ym-mass-gap.tex`,
  Section~\ref{sec:cascade-gap}): the discrete cascade gap
  Hamiltonian is programme-positioned as a $C_\varphi$-style
  mass-regularised Laplacian on the 600-cell substrate.
- **NS regularity functional** (`ns-formal.tex`): the cascade
  hydrodynamic projector is programme-positioned in the same
  Lyapunov-of-polynomial-in-$L$ family.
- **BSD operator** (`bsd-formal.tex`): $T_E$ on the enlarged
  Hecke module is programme-positioned as a
  response-operator-family member.
- **Hodge $\sigma$-projector** (`hodge-formal.tex`): the cascade
  $\sigma$-projector is programme-positioned as a rank-1 /
  spectral-projection limit of the same family.
- **PNP cascade refinement** (`pnp-formal.tex`): the cascade
  refinement on the restricted model class is programme-positioned
  as a response-kernel projection in the bounded-resource regime.

In each case the cascade construction is positioned as a
programme-proposed family instance, selected by the structural role
it plays in the corresponding Millennium reduction. These are not
arbitrary constructions, but the family-membership claim is not
formally canonical and is not proved in any of the cited papers.

## 6. Response vs selection: the open layer

The closure response primitive now has a **shipped passive-regime
empirical landing**: the b-anomaly paper (§4 above) tests the fixed
$C_\varphi$-derived $V_{600}$ kernel without shape retuning across
five public flavour-physics datasets covering two collaborations,
two isospin partners, and three decay channels. This **does not
close the selection layer**. The active-regime companion remains
the ARIA / aria-chess selection paper: a learning-rule / Lyapunov /
coherence-descent construction for $W$-space, *not supplied* by
b-anomaly.

The closure response $\psi = C_\varphi^{-1} f$ is derived from
geometry. It is *not* a selection rule. Crystallisation
additionally requires a selection dynamic — a Lyapunov / coherence
descent rule
$$
dW/dt \;=\; -\nabla V(W)
$$
or equivalent — that selects which response is the stable
attractor.

This selection layer is **open**. The same gap appears in three
independent frames:
- **RH paper**: open $\textup{H}_{\mathrm{attr}}$ at the level of
  the original cascade closure functional (the polynomial filter
  $\Psi_t$ is only a finite-dimensional analogue, by design).
- **Adaptive Closure Transport** (`papers/adaptive-closure-transport/`):
  edge-space lift / Lyapunov mechanism for the selection programme,
  explicitly left open (lines 327--328, 377--382 of that paper).
- **ARIA framework**: crystallisation / coherence-descent rule,
  named as the next layer above response. The aria-chess paper
  (active-regime empirical companion to adaptive-closure-transport)
  is **named, not yet written**.

The convergence of the gap across these three frames is the
strongest programme-level indication that the gap is a single
mathematical problem rather than three independent ones (a
programme-level reading, not a proof of equivalence). The
passive-regime b-anomaly landing strengthens external confidence
in the *response* primitive without reducing or addressing the
selection gap.

## 7. Canonical references in this repository

- `papers/millennium-rh-formal/rh-formal.tex` — polynomial filter
  $F_{\mathrm{filt}}$ as σ-fix-annihilator family member (closing
  subsection).
- `papers/millennium-ym/ym-mass-gap.tex` — cascade gap operator as
  $C_\varphi$-style member.
- `papers/millennium-ns-formal/ns-formal.tex` — regularity
  functional as family member.
- `papers/millennium-bsd-formal/bsd-formal.tex` — $T_E$ as
  family member.
- `papers/millennium-hodge-formal/hodge-formal.tex` — σ-projector
  as rank-1 limit.
- `papers/millennium-pnp-formal/pnp-formal.tex` — cascade
  refinement as response-kernel projection.
- `papers/adaptive-closure-transport/adaptive-closure-transport.tex` —
  selection layer, open.
- `docs/convergence-with-smart.md` — programme-level architectural
  consilience between cascade and Smart frames.
- `docs/projection-narrative.md` (and related) — Layer 1 mainstream
  coherence earning Layer 2 realisation.
- `/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.pdf` —
  primary shipped passive-regime empirical witness for the fixed
  $C_\varphi$-derived $V_{600}$ kernel; five-dataset sign-uniform
  structural test (LHCb + CMS, $K^{*0}/K^{*+}/\phi$ channels) with
  honest AIC tie ($w_{\mathrm{VFD}} = 0.348$ vs
  $w_{\mathrm{FREE\_C9}} = 0.652$) and Mode-B $+2.77$ drift caveat.
- `BANOMALY-001/vfd-b-anomaly/archive/reports/wo007_eigenvalue_derivation.md` —
  Layer 1 + Layer 2 derivation (supporting).
- `BANOMALY-001/vfd-b-anomaly/archive/reports/wo008_discrete_lift.md` —
  Layer 3 numerical bridge (supporting).
- `BANOMALY-001/vfd-b-anomaly/reports/wo016b_variant_geometry.md` —
  variant-selection table; the unweighted Laplacian wins on both
  pure-geometry and data $\chi^2$ criteria.
- `BANOMALY-001/vfd-b-anomaly/reports/wo016c_nonlinear_refit.md` —
  Mode-B drift documentation; the largest single methodological
  uncertainty in the project.
