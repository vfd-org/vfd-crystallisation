# Derivation of the Schwarzschild Compactness Parameter $\kappa$ from VFD Substrate

**Status:** Working math derivation, started 2026-05-11. **Updated 2026-06-10:** (C1) upgraded to a theorem at low harmonics and the (H-wave) second-order-time justification discharged, both via `docs/rendering-layer.md`. Goal: derive
$$\kappa(r) \;=\; \frac{2GM}{rc^2}$$
from the existing VFD closure substrate, rather than postulate it. Tier 1 (Newtonian limit) is targeted as a theorem; Tier 2–4 (metric promotion, emergent constants) are named as conditional hypotheses with explicit content. No paper draft yet; this is the math-first scratchpad.

This document depends on `docs/closure-cosmogenesis.md` (substrate state, bulk/boundary, accumulation) and `docs/aria-closure-kernel.md` ($C_\varphi$ operator family, Green function). It does not depend on any paper draft.

## 0. Position

Two facts force the structure of the derivation.

**Fact A** (`aria-closure-kernel.md` §1–2). The closure-response operator family is
$$C_\varphi \;:=\; L_M + \varphi^{-2} I,$$
and its 3D continuum Green function is
$$G_{C_\varphi}(\vec r) \;=\; \frac{e^{-r/\varphi}}{4\pi r}.$$
For finite $\varphi$ this is **Yukawa** — exponentially screened at scale $\varphi$, not $1/r$. The b-anomaly empirical witness sits at this finite-$\varphi$ regime (φ is the hadronic-scale coherence length).

**Fact B** (`closure-cosmogenesis.md` Theorem 5.2). The σ-fixed bulk is invariant under accumulation: $F_t^{\mathcal B} = F_0^{\mathcal B}$ for all $t$. All dynamical content lives on the σ-paired boundary $\partial$ (Conjecture 5.3).

These two facts together force a clean structural reading: $C_\varphi$ is a **one-parameter family** of response operators, with $\varphi^{-1}$ playing the role of a coherence mass. Different values of $\varphi^{-1}$ correspond to different physical regimes:

- **Finite $\varphi$** (hadronic scale): Yukawa response, e.g. b-anomaly.
- **$\varphi \to \infty$** (massless limit): pure Laplacian response, $1/r$ Green function. This is the regime where **Newtonian gravity must live**, if gravity is a substrate-response phenomenon at all.

The derivation below works in the $\varphi \to \infty$ limit on the σ-paired boundary, in the long-wavelength continuum approximation $a \ll r \ll R$ where $a$ is substrate spacing and $R$ is the global $S^3$ radius.

## 1. Substrate axioms (recap)

Adopting `closure-cosmogenesis.md` Definitions 2.1–2.2 and Theorem 5.2:

**(S1)** The substrate is $V_{600}$, the 120-vertex 600-cell graph embedded in $S^3 \subset \mathbb H \cong \mathbb R^4$ via the icosian ring. Each vertex has degree 12; edge inner product $\langle v, w\rangle = \varphi/2$ for adjacent $v, w$.

**(S2)** $V_{600} = \mathcal B \sqcup \partial$ with $|\mathcal B| = 20$ (σ-fixed bulk, K-classes $\{0, 72\}$) and $|\partial| = 100$ (σ-paired boundary, K-classes $\{20, 52\}$).

**(S3)** The substrate state is $F_t \in \mathcal S = \mathbb R^{V_{600}}$. Initial state $F_0 = (1/\sqrt 2)(\chi_{K=72} + \chi_{K=0})$ is σ-bulk-supported.

**(S4)** Dynamics: $F_{t+1} = F_t + \rho_t$ where $\rho_t$ is the projection-event residual. Theorem 5.2: $F_t^{\mathcal B} = F_0^{\mathcal B}$ for all $t$. Conjecture 5.3: $\rho_t^{\mathcal B} = 0$.

**(S5)** Substrate ticks index a discrete time variable $t \in \mathbb Z_{\geq 0}$. The physical duration of one tick is denoted $\tau$ (undetermined at this stage; introduced as a substrate constant).

## 2. The response operator family on the boundary

**Definition 2.1 (Boundary subgraph).** Let $\mathcal G_\partial$ be the induced subgraph of $V_{600}$ on the 100 σ-paired vertices. Its graph Laplacian is $L_\partial$ (unweighted, per the `aria-closure-kernel.md` §4 variant-selection result).

**Definition 2.2 (Boundary response operator family).** For $\varphi \in (0, \infty]$, the boundary response operator is
$$C^\partial_\varphi \;:=\; L_\partial + \varphi^{-2} I_\partial$$
acting on $F \in \mathbb R^{\partial}$. For $\varphi = \infty$, this is $C^\partial_\infty = L_\partial$ (massless).

**Definition 2.3 (Boundary response field).** For a localised source $\rho \in \mathbb R^{\partial}$, the response field is
$$\Phi_\varphi \;:=\; (C^\partial_\varphi)^{-1} \rho.$$
On the boundary subgraph, this is well-defined iff $L_\partial$ is connected (so that $L_\partial$ has zero kernel mod constants); for $\varphi < \infty$, $C^\partial_\varphi$ is strictly positive and $\Phi_\varphi$ is unique. For $\varphi = \infty$, $\Phi_\infty$ is defined up to a global additive constant (gauge choice: $\Phi_\infty \to 0$ at $\partial$-infinity in the continuum limit).

**Lemma 2.5 ($\mathcal G_\partial$-connectivity and regularity).** The induced subgraph $\mathcal G_\partial$ on the 100 σ-paired vertices of $V_{600}$ is:
1. **10-regular**: every $\partial$-vertex has exactly 10 σ-paired neighbors (and exactly 2 bulk neighbors).
2. **Connected**: the Laplacian $L_\partial$ has a single zero eigenvalue with algebraic connectivity $\lambda_2(L_\partial) = 1.7715$ and largest eigenvalue $\lambda_{\max}(L_\partial) = 13.3216$.
3. **500 edges**, with the edge-decomposition of $V_{600}$ being $|E(\mathcal B)| + |E(\mathcal B, \partial)| + |E(\partial)| = 20 + 200 + 500 = 720$.

**Proof (computational).** Verified by `scripts/verify_lemma_2p5_boundary_connectivity.py`, which builds $V_{600}$ from quaternionic icosian coordinates, identifies the pentagonal-clock orbits under left-multiplication by an order-10 quaternion $\tau \in V_{600}$, computes the cycle K-values $K(C) = \sum_{v\in C}(s(v)-4)^2$, recovers the predicted K-multiset $\{0:1, 20:5, 52:5, 72:1\}$, extracts the σ-paired boundary (cycles with $K \in \{20, 52\}$), and diagonalises $L_\partial$. The 10-regularity is read off the row-sums of the induced adjacency; connectivity from the single zero Laplacian eigenvalue, confirmed by BFS reaching all 100 vertices. $\square$

**Corollary 2.6 (Bulk substructure).** As a by-product, the σ-fixed bulk subgraph $\mathcal G_\mathcal B$ has 20 vertices, 20 edges, and uniform degree 2 — it decomposes as **two disjoint 10-cycles** (the K=0 and K=72 pentagonal-clock orbits). This is consistent with closure-cosmogenesis Definition 2.1 and with Theorem 5.2's bulk-invariance: the bulk dynamics is trivial in the sense that it has no inter-cycle coupling.

## 3. Long-wavelength continuum limit

**Setup.** $V_{600}$ vertices sit on $S^3$ with unit (icosian) radius. As a graph approximating $S^3$, the graph Laplacian $L_{V_{600}}$ satisfies a Hoffman–Davidson-style spectral approximation to the Laplace–Beltrami operator $-\Delta_{S^3}$ at low spectral modes. (`aria-closure-kernel.md` §4 reports correlation $0.9968$ between the discrete kernel and the 3D continuum kernel; this is the empirical content of the approximation.)

**(C1) Continuum approximation.** At length scales $\ell$ satisfying $a \ll \ell \ll R$ (where $a$ is substrate edge length and $R$ is $S^3$ radius), the discrete operator $L_\partial$ acts on slowly varying functions as
$$L_\partial F \;\approx\; -a^2 \nabla^2 F$$
in any local Euclidean chart. (Standard graph-to-manifold Laplacian limit; correlation 0.9968 is the empirical surrogate.)

**(C1) upgrade (2026-06-10).** For the full $V_{600}$ Laplacian this is now a theorem at low harmonics, not an empirical surrogate: the spectrum obeys the exact dispersion relation
$$\lambda_k \;=\; 12\left(1 - \frac{\sin((k+1)\pi/5)}{(k+1)\sin(\pi/5)}\right), \qquad k = 0, \ldots, 5,$$
on the $S^3$ harmonic blocks of multiplicity $(k+1)^2$ (Cayley-graph character formula on the 12-element conjugacy class), with small-$k$ limit $L_{V_{600}} \to -2a^2\,\Delta_{S^3}$ at geodesic edge length $a = \pi/5$, and Weyl exponent $d = 3.09$. See `docs/rendering-layer.md` Theorems 2.2–2.3 and Corollary 2.4; sim `scripts/verify_rendering_layer.py` (R1a–R1f, machine-precision match). The boundary-subgraph version ($L_\partial$, used below) retains the empirical-surrogate status.

**(C2) Local flat-space approximation.** At a scale $\ell \ll R$, $S^3$ is locally Euclidean: in normal coordinates centered at any point, $g_{ij} = \delta_{ij} + O(\ell^2/R^2)$, and $\Delta_{S^3} \to \Delta_{\mathbb R^3}$ as $\ell/R \to 0$. So the boundary response equation in the local continuum is
$$-a^2 \nabla^2 \Phi_\infty(\vec r) \;=\; \rho(\vec r), \qquad a \ll r \ll R. \tag{3.1}$$

**(C3) Substrate length scale.** Adopt $a = \varphi/2$ (the icosian edge inner product, taken as the substrate length). Then (3.1) becomes
$$-\frac{\varphi^2}{4} \nabla^2 \Phi_\infty(\vec r) \;=\; \rho(\vec r). \tag{3.2}$$

## 4. Newton's $1/r$ law from substrate

**Theorem 4.1 (Boundary $1/r$ response).** In the continuum approximation (C1)–(C3), the boundary response field $\Phi_\infty$ due to a point σ-paired source of total charge $Q$ at the origin satisfies
$$\Phi_\infty(r) \;=\; -\frac{Q}{\pi \varphi^2 r}, \qquad a \ll r \ll R.$$

**Proof.** Equation (3.2) with $\rho(\vec r) = Q \, \delta^3(\vec r)$ has Green's-function solution: from the identity $\nabla^2(-1/(4\pi r)) = \delta^3(\vec r)$, the solution of $-(\varphi^2/4)\nabla^2 \Phi_\infty = Q\delta^3$ is
$$\Phi_\infty(\vec r) \;=\; -\frac{4 Q}{\varphi^2} \cdot \frac{1}{4\pi r} \;=\; -\frac{Q}{\pi\varphi^2 r}.$$
For positive σ-paired charge $Q$, the response field is negative (attractive potential well at the source). Existence and uniqueness modulo additive constants follow from Lemma 2.5 (connectivity of $\mathcal G_\partial$): in the discrete substrate the inverse $(C^\partial_\infty)^{-1}$ on the orthogonal complement of constants is well-defined. $\square$

**Definition 4.2 (Gravitational mass).** The gravitational mass $M$ associated with a localised σ-paired source of total charge $Q$ is defined by
$$\boxed{\;\; M \;:=\; \frac{Q}{\pi \varphi^2 G} \;\;} \tag{4.1}$$
where $G$ is the conversion factor between σ-paired substrate charge and physical mass. Equivalently:
$$Q \;=\; \pi G \varphi^2 M. \tag{4.2}$$

**Theorem 4.3 (Newton's gravitational potential from substrate).** Under Definition 4.2 and the continuum approximation, the boundary response field of a point mass $M$ is
$$\Phi_\infty(r) \;=\; -\frac{GM}{r}, \qquad a \ll r \ll R.$$

**Proof.** Substituting (4.2) into Theorem 4.1:
$$\Phi_\infty(r) \;=\; -\frac{\pi G \varphi^2 M}{\pi \varphi^2 r} \;=\; -\frac{GM}{r}. \quad\square$$

**Theorem 4.4 (Newtonian acceleration).** The substrate gravitational acceleration is
$$\vec g \;:=\; -\nabla \Phi_\infty \;=\; -\frac{GM}{r^2} \hat r,$$
matching Newton's law of gravity.

**Status.** Theorems 4.1, 4.3, 4.4 hold under (S1)–(S5), (C1)–(C3), Lemma 2.5 (now proven), and Definition 4.2. The content of Definition 4.2 is identification — it defines $G$ as the substrate-physical mass-unit conversion factor. The σ-paired charge $Q$ is intrinsic to the substrate; the mass-side coefficient $G$ is a calibration constant of the substrate-to-physical-mass identification.

### 4.5 Discrete empirical witness

The continuum-limit argument in §3 is empirically witnessed at the discrete substrate level by `scripts/verify_boundary_green_function.py`, which computes the Moore–Penrose pseudo-inverse $L_\partial^{+}$ on $\mathcal G_\partial$, picks a source vertex $v_0$, and reports the mean response $\psi(v) = (L_\partial^{+} \delta_{v_0})$ binned by graph distance $d(v_0, v)$:

| $d$ | count | mean $\psi$ |
|----:|------:|------------:|
| 0 | 1 | $+0.1231$ |
| 1 | 10 | $+0.0241$ |
| 2 | 24 | $+0.0039$ |
| 3 | 34 | $-0.0048$ |
| 4 | 24 | $-0.0091$ |
| 5 | 7 | $-0.0113$ |

A least-squares fit $\psi(d) \approx A/d + B$ for $d = 1, \ldots, 5$ gives $A = 0.0443$, $B = -0.0196$, $R^2 = 0.9966$. The $B$ constant is the unavoidable Moore–Penrose orthogonality offset to the zero-mode kernel. The fit is consistent with the continuum $1/r$ law of Theorem 4.1, with the caveat that on $|\partial| = 100$ vertices the graph diameter is only $5$ and the $1/d$ form is not sharply distinguished from $1/\sqrt d$ (which fits R² = 0.9970). A multi-shell substrate refinement (Theorem 5.4 of `closure-cosmogenesis.md`) would give more distance shells and sharpen this discrimination; that is not done here.

### 4.6 Mode-separation clarification (replaces earlier conjecture)

A natural question is whether gravity and the b-anomaly Yukawa response live in distinct $W(H_4)$-irreducible subspaces of $\mathbb R^\partial$. The empirical eigenvalue multiplicities of $L_\partial$ are
$$\{0:1,\ 1.77:4,\ 3.53:4,\ 5.39:4,\ 7.00:8,\ 8.00:1,\ 8.77:4,\ 9.14:4,\ 10.00:16,\ 11.14:4,\ 11.76:4,\ 12.00:26,\ 12.47:4,\ 12.72:4,\ 13.00:8,\ 13.32:4\}$$
— clean $W(H_4)$-irrep structure on the 100-dimensional function space on $\partial$.

But the correct statement is **regime separation, not irrep separation**: the same response operator family $C_\varphi = L_\partial + \varphi^{-2} I$ produces different physics in different regimes of the family parameter $\varphi^{-1}$.

- **IR / massless regime** ($\varphi^{-1} \to 0$): Green function $G(r) \sim 1/r$, dominated by **low-eigenvalue modes** of $L_\partial$ (which approximate low spherical harmonics on $S^3$). This is the Newton regime.
- **UV / massive regime** ($\varphi^{-1}$ = hadronic scale): Green function $G(r) \sim e^{-r/\varphi}/r$ (Yukawa), exponentially screened at scale $\varphi$. All eigenmodes of $L_\partial$ contribute with $\varphi^{-1}$ playing the role of a regulator. This is the b-anomaly regime.

So gravity and the b-anomaly are **two ends of a one-parameter family of response operators on the same boundary space**, not two disjoint sub-irreps. The empirical content of `aria-closure-kernel.md` §4 (b-anomaly five-dataset sign-uniform test) places the hadronic regime at a specific finite $\varphi$ that fits flavour-physics data; gravity sits at $\varphi^{-1} = 0$ on the same family. The Tier 1 derivation above sits cleanly at $\varphi^{-1} = 0$.

## 5. The factor 2: required structure for Schwarzschild

To reach $\kappa(r) = 2GM/(rc^2)$, we need to promote the scalar $\Phi_\infty$ to the time-time component of a metric perturbation:
$$g_{00} \;=\; -(1 + 2\Phi_\infty/c^2) \;=\; -\left(1 - \frac{2GM}{rc^2}\right) \;=\; -(1 - \kappa). \tag{5.1}$$

The factor 2 in (5.1) is not a free coefficient. In linearized GR it comes from the trace-reversed stress-energy coupling:
$$\Box \bar h_{\mu\nu} \;=\; -\frac{16\pi G}{c^4} T_{\mu\nu}, \qquad \bar h_{\mu\nu} := h_{\mu\nu} - \tfrac{1}{2} \eta_{\mu\nu} h. \tag{5.2}$$

For a static dust source ($T_{00} = \rho c^2$, others zero), (5.2) gives $\bar h_{00} = -4GM/(rc^2)$ via the wave-equation Green function. Converting back from trace-reversed via $h_{\mu\nu} = \bar h_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu} \bar h$ produces $h_{00} = -2\Phi_\infty/c^2$, giving (5.1).

Four named hypotheses constitute the substrate-side requirements:

**(H-wave) Emergent wave operator.** Adopting the substrate tick duration $\tau$ from (S5), define
$$c \;:=\; \frac{a}{\tau} \;=\; \frac{\varphi}{2\tau} \tag{5.3}$$
as the substrate propagation speed. The boundary response operator extends to a wave operator
$$\Box_\partial \;:=\; c^{-2}\partial_t^2 - L_\partial / a^2 \to c^{-2}\partial_t^2 - \nabla^2$$
in the continuum, so that finite-tick boundary dynamics produces a relativistic wave equation in the long-wavelength limit. The static $\nabla^2$ used in §3–§4 is the $\partial_t \to 0$ reduction of $\Box_\partial$.

**(H-tensor) Rank-2 metric perturbation from icosian quaternions.** The icosian ring $\mathbb H_I$ provides $V_{600} \subset S^3 \subset \mathbb H \cong \mathbb R^4$. A 4-vector field $A^\mu : V_{600} \to \mathbb R^4$ is the natural substrate analog of a Lorentz 4-vector. A symmetric rank-2 perturbation
$$h_{\mu\nu}(\vec r, t) \;:=\; \text{Sym}_2[A_\mu(\vec r, t) \otimes A_\nu(\vec r, t)]$$
or analogous bilinear construction lifts the scalar $\Phi_\infty$ to a tensor object. Specific construction TBD; the substrate datum is icosian-quaternionic.

**(H-stress) Stress-energy from σ-paired residual structure.** The σ-paired residual $\rho_t$ admits a 4-tensor refinement: the "stress" components $T^{ij}$ measure σ-paired residual flux across boundary cycles, while the "energy" component $T^{00}$ measures local σ-paired residual density. Construction TBD; the substrate datum is the K-class structure $\{20, 52\}$ on σ-paired cycles and the cocycle $\kappa(v) = (s(v) - 4)^2$.

**(H-trace) Trace-reversed coupling.** The substrate dynamics of $h_{\mu\nu}$ couples to $T_{\mu\nu}$ in trace-reversed form
$$\Box_\partial \bar h_{\mu\nu} \;=\; -\frac{16\pi G}{c^4} T_{\mu\nu}, \qquad \bar h_{\mu\nu} = h_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu} h. \tag{5.4}$$
The factor 16π and the trace-reversal need to fall out of the substrate construction, not be input by hand.

### 5.5 Explicit form of the (H-tensor) coupling

The metric perturbation built from the scalar $\Phi_\infty$ and the substrate tick direction $u^\mu = (1, 0, 0, 0)$ is
$$\boxed{\;\; h_{\mu\nu}(\vec r) \;=\; -\frac{2\Phi_\infty(\vec r)}{c^2}\,\bigl(\eta_{\mu\nu} + 2 u_\mu u_\nu\bigr) \;\;} \tag{5.5}$$
where $\eta = \mathrm{diag}(-1, +1, +1, +1)$ and $u_\mu = (-1, 0, 0, 0)$ so $u_\mu u_\nu = \mathrm{diag}(1, 0, 0, 0)$.

**Component check.** $\eta_{\mu\nu} + 2 u_\mu u_\nu = \mathrm{diag}(-1+2, +1, +1, +1) = \mathrm{diag}(1, 1, 1, 1) = \delta_{\mu\nu}$. So (5.5) reduces in this gauge to
$$h_{\mu\nu}(\vec r) \;=\; -\frac{2\Phi_\infty(\vec r)}{c^2}\,\delta_{\mu\nu}, \qquad h_{00} = h_{ii} = -\frac{2\Phi_\infty}{c^2}, \quad h_{0i} = 0.$$

This is the standard weak-field isotropic-gauge metric perturbation for static dust. The factor 2 and the $(\eta + 2 u u)$ tensor structure together encode the trace-reversed coupling: they are the substrate-side content of (H-stress) ∧ (H-trace) combined.

**Status of (5.5).** Postulated as (H-tensor). What the substrate has to supply for (5.5) to be derived rather than postulated:
- **Substrate 4-vector $u$.** The tick direction. $u^\mu = (1, 0, 0, 0)$ in the substrate's natural frame is a definition once tick-time is identified as $x^0$.
- **The factor 2 and the $(\eta + 2 u u)$ structure.** This is the form of the matter coupling, which in standard GR comes from the Einstein–Hilbert action plus a minimally coupled dust Lagrangian. From the substrate side, it should fall out of a Lorentz-covariant substrate action with σ-paired residual as the source. This is the residual content of (H-action) below.

## 6. Conditional Schwarzschild theorem

**Theorem 6.1 (Conditional Schwarzschild compactness).** Under (S1)–(S5), (C1)–(C3), Open Lemma 2.5, Definition 4.2, and the four hypotheses (H-wave), (H-tensor), (H-stress), (H-trace), the boundary metric perturbation due to a point mass $M$ in the regime $a \ll r \ll R$ satisfies
$$g_{00}(r) \;=\; -(1 - \kappa(r)), \qquad \kappa(r) \;=\; \frac{2GM}{rc^2}.$$

**Proof sketch.** Work in signature $(-, +, +, +)$, with the wave operator $\Box = \eta^{\mu\nu}\partial_\mu \partial_\nu = -c^{-2}\partial_t^2 + \nabla^2$ from (H-wave). By (H-stress), a point mass $M$ at rest at the origin sources stress-energy
$$T_{00}(\vec r) = M c^2 \delta^3(\vec r), \qquad T_{ij} = 0,$$
with trace $T = \eta^{\mu\nu}T_{\mu\nu} = -T_{00} = -Mc^2 \delta^3(\vec r)$.

By (H-trace), the static reduction of (5.4) is
$$\nabla^2 \bar h_{\mu\nu}(\vec r) \;=\; -\frac{16\pi G}{c^4} T_{\mu\nu}(\vec r).$$
Using $\nabla^2 (1/(4\pi r)) = -\delta^3$, the Green's-function solution for the only non-zero source component is
$$\bar h_{00}(r) \;=\; \frac{4 G M}{c^2 r},$$
with $\bar h_{ij} = 0$. The trace is $\bar h = \eta^{\mu\nu}\bar h_{\mu\nu} = -\bar h_{00}$. Converting back from trace-reversed:
$$h_{\mu\nu} \;=\; \bar h_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu}\bar h,$$
which on the 00-component gives
$$h_{00} \;=\; \bar h_{00} - \tfrac{1}{2}(-1)(-\bar h_{00}) \;=\; \bar h_{00} - \tfrac{1}{2}\bar h_{00} \;=\; \tfrac{1}{2}\bar h_{00} \;=\; \frac{2GM}{c^2 r}.$$
Therefore
$$g_{00}(r) \;=\; \eta_{00} + h_{00}(r) \;=\; -1 + \frac{2GM}{c^2 r} \;=\; -\left(1 - \frac{2GM}{rc^2}\right) \;=\; -(1 - \kappa(r)),$$
which matches the weak-field expansion $g_{00} = -(1 + 2\Phi_\infty/c^2)$ via $\Phi_\infty = -GM/r$ from Theorem 4.3. $\square$

**Status.** Theorem 6.1 is **conditional** on the four hypotheses (H-wave), (H-tensor), (H-stress), (H-trace), and on Open Lemma 2.5. The Newtonian limit (Theorems 4.1–4.4) is closed up to Open Lemma 2.5 and Definition 4.2.

## 6.5 Substrate scalar action (H-action, scalar part)

For the scalar field $\Phi_\infty$ on the substrate, a natural Lorentz-covariant action is
$$S_\Phi \;=\; \int d^4x \,\left[\, -\frac{1}{8\pi G}\, \eta^{\mu\nu}\partial_\mu \Phi_\infty \,\partial_\nu \Phi_\infty \;+\; \Phi_\infty\, \rho_m\,\right] \tag{6.5}$$
where $\rho_m$ is the physical mass density. Stationary point under variation of $\Phi_\infty$:
$$\frac{1}{4\pi G}\, \eta^{\mu\nu}\partial_\mu \partial_\nu \Phi_\infty \;=\; \rho_m,$$
which in the static case reduces to the Poisson equation
$$\nabla^2 \Phi_\infty \;=\; 4\pi G \rho_m \tag{6.6}$$
— Newton's gravitational field equation. For a point source $\rho_m = M\delta^3(\vec r)$, (6.6) gives $\Phi_\infty = -GM/r$, matching Theorem 4.3.

**Substrate origin of (6.5).** In substrate units, the action discretises to
$$S_\Phi^{\text{lat}} \;=\; \tau\, a^3 \sum_t \sum_{v \in \partial} \left[\, -\frac{1}{8\pi G_{\text{sub}}}\,\left(\frac{F_{t+1}(v) - F_t(v)}{\tau}\right)^2 \cdot a^2 \;+\; \frac{1}{a^4}\, F_t(v)\,\langle L_\partial F_t, F_t\rangle_{v} \;+\; F_t(v)\, \rho_m(v)\,\right]$$
(schematic; exact coefficients require careful unit tracking). The key point: each substrate ingredient — tick $\tau$, lattice $a$, $L_\partial$, σ-paired residual — has a natural slot in the action. The Lorentz-covariant form (6.5) emerges in the continuum limit $\tau, a \to 0$ with $c = a/\tau$ fixed. **What is NOT supplied by the substrate yet: the absolute normalization $G$ as a substrate constant.** Per Definition 4.2, $G$ is a calibration factor; once a substrate-derived reference mass (e.g., proton mass from `paper-xxxii`) is in hand, $G$ is determined.

This gives Newton + the scalar field equation **from a substrate action**, modulo the Lorentz-covariance assumption (which itself rests on H-wave).

## 6.6 Tensor lift: from $\Phi_\infty$ to $h_{\mu\nu}$

The scalar action (6.5) does not by itself give $h_{\mu\nu}$. The lift to the metric perturbation requires either (a) postulating (5.5) as the matter-coupling ansatz, or (b) constructing a Fierz–Pauli-style tensor action whose linearised stationary point gives both the scalar Poisson equation and the trace-reversed coupling.

**Option (a) — postulate ansatz.** (5.5) supplies $h_{\mu\nu} = -2\Phi_\infty/c^2 \cdot \delta_{\mu\nu}$, then $g_{00} = -(1 - \kappa)$ with $\kappa = 2GM/(rc^2)$ by direct substitution. The "factor 2" lives in the ansatz; the substrate supplies $\Phi_\infty$ and $c$.

**Option (b) — derive Fierz–Pauli on substrate.** The natural substrate-tensor candidate uses the icosian quaternion structure $V_{600} \subset \mathbb H \cong \mathbb R^4$: a 4-vector field $A^\mu(\vec r, t)$ on the substrate, with rank-2 perturbation built bilinearly,
$$h_{\mu\nu} \;\sim\; \alpha\, A_\mu A_\nu \;+\; \beta\, \eta_{\mu\nu} A^\rho A_\rho,$$
or its gauge-fixed analog. A Fierz–Pauli substrate action
$$S_h \;=\; \int d^4x \,\left[\, -\frac{c^4}{32\pi G} \bigl(\partial_\rho h_{\mu\nu} \partial^\rho h^{\mu\nu} - 2 \partial_\mu h^{\mu\nu} \partial^\rho h_{\rho\nu} + \cdots\bigr) \;+\; h_{\mu\nu} T^{\mu\nu}\,\right]$$
would, on stationary point with dust source $T_{\mu\nu} = \rho_m c^2 u_\mu u_\nu$, give the linearised Einstein equation $\Box \bar h_{\mu\nu} = -(16\pi G/c^4) T_{\mu\nu}$ — exactly (5.4) — and hence (5.5) in the static dust regime.

The substrate derivation of $S_h$ is **the central open piece**. Plausible substrate datum for $A^\mu$: the icosian gradient $A^\mu := \partial^\mu F$ of the closure functional $F$ (which is quaternion-valued on $V_{600}$). The substrate kinetic term then arises from the icosian inner product $\langle A^\mu A_\mu\rangle$ evaluated on the V_600 → $S^3$ continuum limit. The factor $1/32\pi G$ is the substrate-physical normalization (same calibration as for the scalar).

**Open Conjecture 6.6.1 (icosian Fierz–Pauli action).** The icosian-gradient bilinear $h_{\mu\nu} = \mathrm{Sym}_2(\partial_\mu F \otimes \partial_\nu F)/c^4$ on $V_{600}$ admits a continuum-limit Fierz–Pauli action whose stationary equations in the static dust regime reproduce (5.4), and hence (via §6 proof) the conditional Schwarzschild theorem becomes unconditional (modulo calibration $G$).

## 6.7 Attempt at Conjecture 6.6.1: substrate Fierz–Pauli action

> **UPDATE (2026-06-11): the chain is closed — by reidentification, not by this construction.** `docs/gr-closure-derivation.md` shows the bilinear (6.7.1) is the canonical Noether **stress tensor** of the substrate field (the source, properly quadratic in matter — discharging (H-stress)), not the metric; $h_{\mu\nu}$ is instead the coarse **collective** deformation field, whose effective action is quadratic by the large-$N$/Wishart argument (dissolving Obstacle 1) and is forced to be Fierz–Pauli by chart-freedom gauge invariance + uniqueness (so trace reversal and the 16π coupling are theorems, closing Obstacle 3 and (H-trace); Obstacle 2's Nordström fallback is retired, the full $g_{ij}$ and light-bending factor 2 now derived). The Deser bootstrap then gives the full Einstein equations. Sim: `scripts/verify_gr_closure.py`, 39/39 PASS. The analysis below is retained as the honest record of why the *direct* construction could not work.

This section attempts the construction. Three substantive obstacles are identified; the construction is not closed in this session.

### 6.7.1 Setup

Take the substrate state to be a quaternion-valued field
$$F: V_{600} \times \mathbb Z \;\to\; \mathbb H \;\cong\; \mathbb R^4, \qquad F(v, t) \in \mathbb H,$$
extending the scalar-state space $\mathcal S = \mathbb R^{V_{600}}$ of closure-cosmogenesis to a 4-component field. Each component lives in $\mathbb R^{V_{600}}$.

(Justification for the quaternionic lift: each $V_{600}$ vertex sits in $\mathbb H \cong \mathbb R^4$ via the icosian embedding, so $\mathbb H$ is the natural target. The scalar substrate state is the real part of an $\mathbb H$-valued state.)

Define discrete derivatives:
- **Time:** $(\partial_0 F)(v, t) := (F(v, t+1) - F(v, t))/\tau \,\in\, \mathbb H.$
- **Space:** Let $\{w_1, \ldots, w_{12}\}$ be the 12 neighbors of $v$ in $V_{600}$. Each tangent vector $\hat e_i := (w_i - v) / a$ lies in $T_v S^3 \subset \mathbb H$ (3D tangent space). Define
$$(\partial_a F)(v, t) := \frac{1}{a}\sum_{i=1}^{12} \langle\hat e_i, \hat \epsilon_a\rangle\, (F(w_i, t) - F(v, t)) \;\in\; \mathbb H, \qquad a = 1, 2, 3,$$
where $\{\hat \epsilon_1, \hat \epsilon_2, \hat \epsilon_3\}$ is an orthonormal frame on $T_v S^3$. (The choice of frame is non-canonical at each vertex; gauge-invariance of the eventual action under local frame rotation has to be checked.)

So at each $(v, t)$, we have a 4-vector of quaternions $\partial_\mu F = (\partial_0 F, \partial_1 F, \partial_2 F, \partial_3 F) \in \mathbb H^4$.

### 6.7.2 Bilinear tensor field

Define
$$h_{\mu\nu}(v, t) \;:=\; \mathrm{Re}\bigl[(\partial_\mu F(v, t))^* \cdot (\partial_\nu F(v, t))\bigr] \;\in\; \mathbb R, \tag{6.7.1}$$
where $q^*$ is quaternion conjugation and $\cdot$ is quaternion multiplication. Real-part of a quaternion product is the standard inner product $\langle q_1, q_2\rangle = \mathrm{Re}(q_1^* q_2)$. So
$$h_{\mu\nu}(v, t) \;=\; \langle \partial_\mu F, \partial_\nu F\rangle_v$$
is automatically a **symmetric** rank-2 tensor on each $(v, t)$. It has 10 independent components (4×4 symmetric).

### 6.7.3 Substrate action attempt

The natural quadratic substrate action for $F$ is
$$S_F \;=\; \tau\, a^3 \sum_t \sum_v \left[\, -\frac{1}{2} \alpha \,\langle\partial_\mu F, \partial^\mu F\rangle \;+\; \langle F, J\rangle\,\right] \tag{6.7.2}$$
where $\alpha$ is a normalization constant, indices contracted with $\eta^{\mu\nu}$ (the substrate-Lorentz metric), and $J$ is a quaternion-valued source. The continuum limit is
$$S_F \;\to\; \int d^4x \,\left[\, -\frac{\alpha}{2} \,\partial_\mu F \cdot \partial^\mu F \;+\; F \cdot J\,\right],$$
giving EOM $\alpha \,\Box F = -J$, the **massless quaternionic scalar wave equation**.

This is a vector-field theory for the 4-component $F$, **not** a tensor field theory for $h_{\mu\nu}$. The action (6.7.2) is quadratic in $F$, which means it is **quartic in $h_{\mu\nu}$** (since $h \sim (\partial F)^2$). It is therefore **not** a quadratic Fierz–Pauli action for $h_{\mu\nu}$.

### 6.7.4 Obstacle 1: scalar/vector vs. tensor

The construction (6.7.1) reduces tensor dynamics to scalar/vector dynamics. The "metric perturbation" $h_{\mu\nu}$ emerges as an observable bilinear in $F$, not as a fundamental field. The substrate equations of motion at the level of $F$ are not Einstein's equations for $h_{\mu\nu}$.

**Possible resolution.** Promote $h_{\mu\nu}$ itself to a fundamental substrate field (a 4×4 symmetric matrix at each $(v, t)$), with its own Fierz–Pauli action:
$$S_h^{\text{FP}} \;=\; \tau\, a^3 \sum_t \sum_v \,\frac{c^4}{32\pi G}\left[\, -\partial_\rho h_{\mu\nu} \partial^\rho h^{\mu\nu} + 2 \partial_\mu h^{\mu\nu} \partial^\rho h_{\rho\nu} - 2\partial_\mu h^{\mu\nu} \partial_\nu h + \partial_\mu h \partial^\mu h\,\right] + h_{\mu\nu} T^{\mu\nu}.$$
But this just postulates Fierz–Pauli at the substrate level; the icosian-structure derivation is lost. **Open: which substrate origin of $h_{\mu\nu}$ avoids this circularity.**

### 6.7.5 Obstacle 2: Nordström-style scalar gravity as fallback

For the **target $\kappa$ at leading order in weak field**, the substrate scalar action (6.5) plus the (H-tensor) ansatz (5.5) is sufficient. The factor 2 in $h_{00} = -2\Phi_\infty/c^2$ is then a postulated coupling, not a derived one. This reduces the open content of Schwarzschild $\kappa$ derivation to **one** named ansatz, not three:

> **Reformulated (H-tensor) (concise).** The substrate metric perturbation built from the scalar Φ is $h_{\mu\nu} = -2\Phi/c^2 \cdot \delta_{\mu\nu}$ in the rest frame of static dust. The factor 2 is the trace-reversed-coupling content.

This is a Nordström-style scalar-gravity ansatz. It reproduces Schwarzschild $\kappa$ at leading order but fails at $O(\kappa^2)$ (where $g_{rr}^{Schw} = 1/(1-\kappa) \neq 1 - \kappa = g_{rr}^{Nordström}$). For the target "derive $\kappa$" (the dimensionless compactness parameter, defined from $g_{00}$), this scalar Nordström substrate is sufficient.

### 6.7.6 Obstacle 3: tensor lift requires nonlinear matter coupling

A full Fierz–Pauli (= linearised Einstein) substrate would give all of weak-field Schwarzschild, not just $\kappa$ in $g_{00}$. For that, the substrate matter coupling has to dynamically generate the trace-reversed source structure $T_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu} T$. This is the central piece that the icosian-bilinear construction (6.7.1) does **not** automatically supply.

**Avenue for future work.** The 24-600 spectral bridge result (`docs/keystone_24_600/`) provides an A₅-equivariant decomposition $E_{600}(12) = 5 \cdot Y_5$ of the 25-dim λ=12 eigenspace. The 10-dim subspace $E_{\text{lifted}} \cong 2 \cdot Y_5$ has the **same dimension as a 4×4 symmetric tensor** (10 components). The dimensional match is suggestive but the SO(4)-vs-A₅ structural match is not established. Whether $h_{\mu\nu}$ naturally lives in $E_{\text{lifted}}$ as an A₅-equivariant sub-bundle is open.

### 6.7.7 Status of Conjecture 6.6.1

Not closed. Partial progress:
- ✓ Quaternionic field $F: V_{600} \times \mathbb Z \to \mathbb H$ defined.
- ✓ Discrete tangent-space derivatives $\partial_\mu F$ defined.
- ✓ Symmetric bilinear $h_{\mu\nu} = \langle \partial_\mu F, \partial_\nu F\rangle$ at every $(v, t)$.
- ✗ Substrate action quadratic in $h_{\mu\nu}$ (Fierz–Pauli) **not derived** from action quadratic in $F$. The natural $F$-action is vector-field theory, not tensor.
- ✗ Trace-reversed matter coupling $T_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu} T$ not derived from σ-paired residual.

**Net effect on the κ derivation.** Theorem 6.1 remains conditional on (H-tensor) and (H-stress)/(H-trace). For the **leading-order κ in $g_{00}$**, the Nordström-style scalar substrate (§6.7.5) is sufficient and reduces the open content to one ansatz. For full linearised GR, Conjecture 6.6.1 is still open.

## 7. Where the conditionals come from in the substrate

This section indicates the substrate machinery that should discharge each of (H-wave) through (H-trace). Each is a separate piece of work; nothing here is claimed proven.

**(H-wave).** Substrate dynamics is discrete-tick accumulation $F_{t+1} = F_t + \rho_t$. Promoting to continuous time gives $\partial_t F = (1/\tau) \rho$ in the long-tick limit. The substrate "wave operator" should arise as a second-order time derivative of the accumulation dynamics; one candidate is the second difference $F_{t+1} - 2F_t + F_{t-1}$ which gives $\tau^2 \partial_t^2 F$ in the continuum. Combined with $L_\partial / a^2 \to -\nabla^2$ from §3, this gives a relativistic wave operator with speed $c = a/\tau$. **Update (2026-06-10): the substrate justification for second-order time is now supplied.** Clock reversal is an *inner* automorphism: exactly ten elements $g \in 2I$ satisfy $g\tau g^{-1} = \tau^{-1}$ (e.g. $g = i$, order 4), so the induced vertex permutation conjugates the pentagonal clock $T_\tau$ to $T_\tau^{-1}$ exactly; under XXXIII's symmetry-equivariance of the residual law this forbids first-order $\partial_t$ terms in the effective continuum dynamics (`docs/rendering-layer.md` Lemma 5.1 + Proposition 5.2, sim-verified R4a–R4c). The earlier speculation that the mechanism is "time-reversal symmetry of σ-Galois action on F" is withdrawn — coordinate Galois does not preserve $V_{600}$ pointwise; the inner reversal does the work. What remains of (H-wave) is the formal second-difference continuum step only.

**(H-tensor).** The icosian ring $\mathbb H_I \cong \mathbb Z[\varphi]^4 \subset \mathbb H$ gives a natural $\mathbb R^4$ structure on substrate-valued fields. A 4-vector field on $V_{600}$ is a map $A : V_{600} \to \mathbb H$. The natural rank-2 tensor on $\mathbb H \otimes \mathbb H$ is the bilinear $A_\mu \otimes A_\nu$ symmetrised; this lifts a scalar field $\Phi$ to a tensor. Specific construction requires identifying which substrate object plays the role of $A$ — candidate: the gradient of the closure functional itself, $A_\mu = \partial_\mu F$ in the continuum.

**(H-stress).** σ-paired residuals $\rho_t$ have K-class structure $\{20, 52\}$. The two K-classes correspond to two distinct cycle types on the boundary. A natural decomposition of $\rho_t$ into "energy" (scalar K-class-symmetric part) and "stress" (anti-symmetric or rank-2 part) follows from the cycle structure. Identification of $T^{00}$ with the σ-symmetric K-class density and $T^{ij}$ with the K-anti-symmetric flux is plausible but not proven.

**(H-trace).** The factor 16π in (5.4) and the trace-reversal are geometric consequences of the GR action being the Einstein–Hilbert form $S = (c^4 / 16\pi G) \int R \sqrt{-g} \, d^4 x$. From the substrate side, an action principle would have to emerge. Candidate: minimisation of total closure residual $\Delta_{\mathrm{cl}}$ across the substrate, plus a kinetic term from accumulation dynamics. The 16π coefficient should then follow from the geometric normalisation of $L_\partial$ on $V_{600}$.

## 8. Emergent constants $G$, $c$, $\hbar$ (interpretive)

Standard physics has three independent fundamental constants $G, c, \hbar$. The VFD substrate has one length scale $\varphi$ (icosian) and one time scale $\tau$ (tick duration). Two substrate constants cannot generate three independent physical constants, so one of $G, c, \hbar$ is a calibration choice rather than a substrate prediction.

Natural assignments:
- $c = \varphi/(2\tau)$ from (5.3) — fixed by substrate.
- $\hbar$ — from the tick action quantum: $\hbar = (\text{closure-residual quantum}) \cdot \tau$ (TBD).
- $G$ — from Definition 4.2: $M = Q / (\pi G \varphi^2)$. $G$ is the substrate-to-physical-mass conversion factor; given a physical reference mass (e.g., proton mass derived elsewhere in programme, see `project_paper_xxxii.md`), $G$ is determined.

Under this assignment, the dimensionless Schwarzschild compactness is
$$\kappa(r) \;=\; \frac{2GM}{rc^2} \;=\; \frac{2 Q}{\pi \varphi^2 c^2 r} \;=\; \frac{8 Q \tau^2}{\pi \varphi^4 r}$$
purely in substrate units. So $\kappa$ has a substrate-intrinsic form once $\tau$ and $\varphi$ are fixed.

## 9. Status summary

> **UPDATE (2026-06-11).** The conditional/conjectural entries below are superseded by `docs/gr-closure-derivation.md`: (H-wave) fully discharged; (H-stress) closed (Theorem A.1: canonical Noether tensor); (H-trace) closed (theorem of the unique Fierz–Pauli action); (H-tensor) reduced to the collective-field construction with (5.5) now derived; Conjecture 6.6.1 superseded by uniqueness; Theorem 6.1 **unconditional** modulo Definition 4.2 and the rigor-grade residuals (R-cont, R-Gauss); full Einstein equations derived modulo the classical bootstrap. Verified 39/39 by `scripts/verify_gr_closure.py`. The pre-closure status below is retained as the historical record.

**Theorems (closed):**
- Lemma 2.5: $\mathcal G_\partial$-connectivity, 10-regularity, $\lambda_2 = 1.7715$. Verified by `scripts/verify_lemma_2p5_boundary_connectivity.py`.
- Corollary 2.6: bulk substructure (two disjoint 10-cycles).
- Theorem 4.1: Boundary $1/r$ response from substrate.
- Theorem 4.3: Newton's gravitational potential $\Phi(r) = -GM/r$.
- Theorem 4.4: Newtonian acceleration $\vec g = -GM/r^2 \hat r$.

**Conditional theorem:**
- Theorem 6.1: Schwarzschild compactness $\kappa(r) = 2GM/(rc^2)$. **Two-tier status:**
  - **Leading-order $\kappa$ in $g_{00}$.** Conditional on the reformulated (H-tensor) of §6.7.5 (Nordström-style scalar coupling $h_{\mu\nu} = -2\Phi/c^2 \delta_{\mu\nu}$) and Definition 4.2. **One ansatz away from closed.**
  - **Full linearised Schwarzschild (also $g_{rr}$ at $O(\kappa)$).** Conditional on Conjecture 6.6.1 (substrate Fierz–Pauli action). **Three obstacles open** (§6.7.4–6.7.6).

**Substrate scalar action (closed):**
- Equation (6.5): $S_\Phi = \int [-(8πG)^{-1}(\partial\Phi)^2 + \Phi\rho_m]$. Stationary point reproduces Newton's field equation. Scalar (H-action) discharged.

**Conjecture 6.6.1 attempt (§6.7): partial progress with three named obstacles.**
- ✓ Quaternionic substrate field $F: V_{600} \times \mathbb Z \to \mathbb H$.
- ✓ Bilinear $h_{\mu\nu} = \langle\partial_\mu F, \partial_\nu F\rangle$ symmetric rank-2 at each $(v, t)$.
- ✗ $S$ quadratic in $h$ (Fierz–Pauli) not derived from $S$ quadratic in $F$ (Obstacle 1).
- ✗ Trace-reversed source structure not derived (Obstacle 3).
- ↔ Nordström scalar fallback (Obstacle 2) suffices for κ-leading.

**Named open hypotheses (reduced set):**
- **(H-tensor) reformulated (concise).** Nordström-style scalar-gravity coupling $h_{\mu\nu} = -2\Phi/c^2 \cdot \delta_{\mu\nu}$. Needed for κ-leading.
- **Conjecture 6.6.1.** Substrate Fierz–Pauli action from icosian gradient bilinear. Needed for full linearised Schwarzschild.
- **(H-wave).** Justification half **discharged** (2026-06-10): second-order time forced by the inner clock reversal $g\tau g^{-1} = \tau^{-1}$, $g \in 2I$ (`docs/rendering-layer.md` Prop 5.2). Remaining: the formal second-difference continuum step $F_{t+1} - 2F_t + F_{t-1} \to \tau^2 \partial_t^2 F$. Pure algebra; achievable.

**Definition (calibration, not theorem):**
- Definition 4.2. $G = Q/(\pi \varphi^2 M)$ defines the substrate-physical mass conversion. $G$ is a calibration constant.

## 10. Next steps

In order of dependency:

**Closed in this session (2026-05-11):**

1. ~~Verify Open Lemma 2.5 computationally.~~ **Done.** `scripts/verify_lemma_2p5_boundary_connectivity.py` reports PASS: $\mathcal G_\partial$ is 10-regular on 100 vertices, connected, $\lambda_2 = 1.7715$.

2. ~~Compute the discrete Green function on $V_{600}$.~~ **Done.** `scripts/verify_boundary_green_function.py` reports $\psi(d) \approx 0.0443/d - 0.0196$, R² = 0.9966 across $d = 1..5$. Empirical witness for Theorem 4.1 confirmed; 1/d vs 1/√d distinction limited by small diameter (5).

3. **Substrate scalar action (6.5)** drafted; Newton's field equation falls out of stationary point. (H-action, scalar part) addressed.

**Conjecture 6.6.1 attempted (§6.7), partial progress:**

3. **Quaternionic field construction** $F: V_{600} \times \mathbb Z \to \mathbb H$ with discrete derivatives $\partial_\mu F$ on tangent spaces $T_v S^3$; symmetric bilinear $h_{\mu\nu} = \langle\partial_\mu F, \partial_\nu F\rangle$ well-defined at each $(v, t)$. **Done.**

4. **Obstacle 1**: substrate action quadratic in $F$ gives vector-field (massless quaternionic scalar) dynamics, not tensor (Fierz–Pauli) dynamics — $h$ is quartic in $F$. **Open.**

5. **Obstacle 3**: trace-reversed source coupling $T_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu} T$ not derived from σ-paired residual structure. **Open.**

6. **Nordström fallback (§6.7.5)**: For leading-order κ in $g_{00}$, scalar substrate (§6.5) plus the simplified Nordström-style coupling $h_{\mu\nu} = -2\Phi/c^2 \cdot \delta_{\mu\nu}$ suffices. This reduces the open content from 4 hypotheses to 1 ansatz.

**Remaining to close Theorem 6.1 unconditionally:**

7. **Formalise (H-wave)**: second-difference substrate dynamics. Pure algebra; achievable. (Justification half closed 2026-06-10 via `docs/rendering-layer.md` Prop 5.2; only the continuum step remains.)

8. **Discharge Conjecture 6.6.1** for full linearised Schwarzschild: requires either (a) a substrate origin of $h_{\mu\nu}$ as a fundamental field (avoiding the $F$-bilinear circularity of §6.7.4), or (b) derivation of trace-reversed coupling from σ-paired K-class structure.

9. **Substrate calibration of $G$**: identify σ-paired-charge to physical-mass conversion using a substrate-derived reference mass (e.g., proton mass from `paper-xxxii`). Calibration, not derivation.

**Current closed state**: Tier 1 (Newton) **theorem**. Tier 2 leading-order κ in $g_{00}$ **one ansatz away** (the Nordström-style $h \sim -2\Phi/c^2 \delta$). Tier 2 full Schwarzschild **two obstacles away** (Conjecture 6.6.1).

## 11. Cross-references

- `docs/gr-closure-derivation.md` — **closure of this document's open items** (2026-06-11): stress-tensor reidentification, collective field, FP uniqueness, bootstrap to full Einstein equations; sim `scripts/verify_gr_closure.py` 39/39.
- `docs/closure-cosmogenesis.md` — substrate state, bulk/boundary, accumulation (Theorem 5.2).
- `docs/rendering-layer.md` — spectral-dimension theorem + exact dispersion (upgrades C1), canonical kernel, inner clock reversal (discharges H-wave justification), chart/scene construction.
- `docs/aria-closure-kernel.md` — $C_\varphi$ operator family, Yukawa Green function.
- `docs/observer-instance-definition.md` — observer slot $\mathcal I$; relevant for §7's $A_\mu$ candidate.
- `docs/fractal-cascade-projection.md` — K-class structure $\{0, 20, 52, 72\}$; relevant for (H-stress).
- `docs/rh-cascade-closure-dynamics.md` — pentagonal-clock cocycle $\kappa(v) = (s(v)-4)^2$; relevant for (H-stress).
- `papers/paper-xxiv/paper-xxiv.tex` — observer-frame kinematics; relevant for time-dilation interpretation of $g_{00}$.
- `project_paper_xxxii.md` (memory) — proton mass from substrate; relevant for §8's $G$ calibration.
