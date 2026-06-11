# The Rendering Layer: Arena, Kernel, Chart, and Scene from the $V_{600}$ Substrate

**Status:** mathematical derivation, 2026-06-10. Supplies the named missing layer between the single-readout closure projection (Paper XXXIII) and the assembled realisation spine (`papers/realisation/realisation.tex`): the construction that turns a substrate state $F_t \in \mathbb R^{V_{600}}$ into a *spatial scene* — a field on a local 3-dimensional chart anchored at the observer instance. Companion to `docs/closure-cosmogenesis.md`, `docs/observer-instance-definition.md`, `docs/aria-closure-kernel.md`, and `docs/kappa-derivation-math.md`. Mathematical content; an Informal reading is a single non-load-bearing closing subsection per `feedback_mathematical_framing_discipline`.

**Sim verification:** `scripts/verify_rendering_layer.py` — **21/21 PASS** (2026-06-10). Results quoted inline.

## 1. Position

The realisation spine ends at the projection readout $\hat O \in W_\Pi$ — a scalar, vector, or matrix per projection event (Paper XXXIII; `realisation.tex` §§3–5). Every projection class outputs one observable per event. A *scene* — what an observer instance renders — is not one readout but a **field of readouts indexed over a neighbourhood of the anchor**, organised in spatial coordinates. No prior document constructs the map from $F_t$ on the 120 vertices to such a field. `realisation.tex` Remark 6.1 names the observer-local layer as open; `docs/programme-plan.md` calls the continuum limit the weakest rigorous link.

The rendering layer must supply four things:

| # | Requirement | Supplied below by |
|---|---|---|
| R1 | The **arena**: which space the scene lives in, with its dimension *derived*, not assumed | §2 (intrinsic $S^3$; spectral dimension theorem) |
| R2 | The **kernel**: the canonical map from vertex data to a smooth field (closes Open 9.2 of `closure-cosmogenesis.md`) | §3 |
| R3 | The **chart**: basepoint + axes + scene assembly at the anchor | §4 |
| R4 | The **time structure**: why the rendered dynamics is second-order (wave-type), addressing the named justification gap in (H-wave) | §5 |

§6 treats simultaneity of readouts (R5), the remaining genuinely open piece. Throughout, $V_{600}$ is the 120-vertex 600-cell graph (vertices = binary icosahedral group $2I \subset S^3 \subset \mathbb H$, degree 12, edges at inner product $\varphi/2$), $L$ its unweighted graph Laplacian, and $F_t = F_t^{\mathcal B} + F_t^\partial$ the substrate state with bulk/boundary split $20 + 100$ (`closure-cosmogenesis.md` Definition 2.1).

## 2. R1 — The arena: intrinsic $S^3$ and the spectral dimension theorem

### 2.1 Intrinsic arena

**Proposition 2.1 (Intrinsic-$S^3$).** Every object of the closure framework built on $V_{600}$ — the adjacency, shells, Laplacian $L$, pentagonal clock $T_\tau$, closure functional $F$, and every projection class — depends only on the *intrinsic* geometry of $V_{600}$ as a subset of $S^3$, never on the ambient $\mathbb R^4$.

**Proof.** All listed structures are functions of pairwise inner products $\langle v, w\rangle$ of unit quaternions (edges: $\langle v,w\rangle = \varphi/2$; shells: $|1-v|^2 = 2 - 2\langle 1, v\rangle$; clock: left multiplication, an isometry of $S^3$). For unit vectors, $\langle v, w\rangle = \cos d_{S^3}(v, w)$ where $d_{S^3}$ is geodesic distance on $S^3$. Hence all structures are functions of intrinsic geodesic distances on the 3-manifold $S^3$. The ambient radial direction enters only through the unit-norm constraint $|v| = 1$ and is never varied. $\square$

So the rendered arena is the intrinsic $S^3$ — a **3**-dimensional manifold; $\mathbb R^4$ is scaffolding. This is consistent with, and gives the substrate-level grounding for, the hypersphere-cosmology identification of the spatial universe with $S^3$. Proposition 2.1 is the soft (embedding-level) statement; the hard (substrate-only) statement is the following spectral theorem, which reads the dimension off the graph alone.

### 2.2 Spectral dimension theorem

**Theorem 2.2 (Square-multiplicity law).** The eigenspace multiplicities of the $V_{600}$ graph Laplacian $L$ are exactly the squares of the dimensions of the nine irreducible representations of $2I$:

$$\{1,\, 4,\, 9,\, 16,\, 25,\, 36\} \;\cup\; \{4,\, 9,\, 16\} \quad (\text{sum} = 91 + 29 = 120).$$

**Proof.** $V_{600}$ is the Cayley graph of the group $2I$ with connecting set $S$ = the 12 vertices at inner product $\varphi/2$ from the identity (shell 1). $S$ is a single conjugacy class of $2I$ (the order-10 elements with real part $\cos(\pi/5) = \varphi/2$) and is closed under inversion (inverse preserves real part). For a Cayley graph on a finite group $G$ whose connecting set is a union of conjugacy classes, the adjacency operator is central in the group algebra, so by the Peter–Weyl decomposition $L^2(G) = \bigoplus_\rho \rho \otimes \rho^*$ it acts as the scalar

$$a_\rho \;=\; \frac{1}{\dim \rho} \sum_{s \in S} \chi_\rho(s)$$

on the $\rho$-isotypic block of dimension $(\dim \rho)^2$ (Babai 1979; Diaconis–Shahshahani 1981). The irreps of $2I$ have dimensions $\{1, 2, 2', 3, 3', 4, 4', 5, 6\}$, giving multiplicities $\{1, 4, 4, 9, 9, 16, 16, 25, 36\}$, with $1 + 4+4 + 9+9 + 16+16 + 25 + 36 = 120$. $\square$

**Distinctness (demanded by the codex review).** The square-multiplicity *count* would still permit two irrep blocks to merge into one eigenvalue. They do not: the nine block scalars $a_\rho$ are pairwise distinct, equivalently the Laplacian has **nine distinct eigenvalues** (sim `verify_gap_strengthening.py` SR2: $\{0, 2.29, 5.53, 9, 12, 14, 14.47, 15, 15.71\}$, all simple-per-block). So each $(\dim\rho)^2$ block sits at its own eigenvalue and the multiplicity law is read off without ambiguity.

**Sim (R1a).** Observed spectrum: $\lambda = 0, 2.2918, 5.5279, 9, 12, 14, 14.4721, 15, 15.7082$ with multiplicities $1, 4, 9, 16, 25, 36, 9, 16, 4$ — all perfect squares. PASS.

**Theorem 2.3 (Harmonic identification and exact dispersion relation).** Under the McKay correspondence, the unprimed irreps $\{1, 2, 3, 4, 5, 6\}$ of $2I$ are the restrictions of the $SU(2)$ representations $V_k$, $k = 0, \ldots, 5$ (irreducible on $2I$ in this range), i.e. the $S^3$ harmonic levels $k = 0..5$ with multiplicity $(k+1)^2$. Their Laplacian eigenvalues are exactly

$$\boxed{\;\lambda_k \;=\; 12\left(1 - \frac{\sin\bigl((k+1)\pi/5\bigr)}{(k+1)\,\sin(\pi/5)}\right), \qquad k = 0, \ldots, 5.\;}$$

The primed irreps fold from higher harmonics ($V_6 = 3' \oplus 4'$, $V_7 \supset 2'$) and sit above the $k=5$ block.

**Proof.** $S$ is the conjugacy class of rotation angle $2\pi/5$ on $S^3$ (real part $\cos(\pi/5)$, so quaternion half-angle $\theta = \pi/5$). The $SU(2)$ character is $\chi_{V_k}(\theta) = \sin((k+1)\theta)/\sin\theta$. Substituting into $a_\rho$ with $|S| = 12$, $\dim V_k = k+1$:

$$a_k \;=\; \frac{12}{k+1}\cdot\frac{\sin((k+1)\pi/5)}{\sin(\pi/5)}, \qquad \lambda_k = 12 - a_k,$$

which evaluates to $\lambda_k \in \{0,\ 12 - 6\varphi,\ 12 - 4\varphi,\ 9,\ 12,\ 14\}$ for $k = 0..5$ — matching the observed spectrum to machine precision (sim R1f, PASS). The branching $V_6 = 3' \oplus 4'$, $V_7 = 6 \oplus 2'$ is the standard McKay/E$_8$ decomposition for $2I$. $\square$

**Corollary 2.4 (Spectral dimension 3).** The small-$k$ expansion of the dispersion relation is

$$\lambda_k \;=\; 2\left(\frac{\pi}{5}\right)^2 k(k+2) \;+\; O(k^4 \theta^4),$$

i.e. $L \to -2a^2\,\Delta_{S^3}$ with $a = \pi/5$ the geodesic edge length, and $k(k+2)$ is **the Laplace–Beltrami spectrum of the round $S^3$**. The factor 2 itself encodes dimension 3: for a degree-12 isotropic neighbour set on a $d$-manifold, $L \approx -(12 a^2 / 2d)\Delta$, and $12/(2 \cdot 3) = 2$. Independently, the Weyl counting fit over the harmonic blocks gives $N(\lambda) \propto \lambda^{d/2}$ with $d = 3.09$ (sim R1e, PASS), and the multiplicity law $(k+1)^2$ is specific to the round $S^3$ (an $S^2$ arena would give $2k+1$; $S^4$ would give $\tfrac{1}{6}(k+1)(k+2)(2k+3)$).

**Reading.** The dimensionality of rendered space is now **derived from the substrate spectrum alone**, three independent ways (multiplicity law, Weyl exponent, dispersion constant), with the lattice correction computable from Theorem 2.3 (3.2% at $k=1$). This discharges the "why 3 dimensions" item flagged in the gap audit: the substrate never had 4 spatial dimensions — the arena is the intrinsic $S^3$ of the icosian unit sphere, and the discrete-to-continuum dictionary is the exact dispersion relation above. Condition (C1) of `kappa-derivation-math.md` §3 is hereby upgraded from "empirical surrogate, correlation 0.9968" to a theorem at low harmonics, with $L_{V_{600}} \to -2a^2 \Delta_{S^3}$, $a = \pi/5$.

## 3. R2 — The canonical rendering kernel (closes Open 9.2)

`closure-cosmogenesis.md` Definition 6.1 left the frame-resolution map $\pi_{C_i}$ with undetermined radius $r(C_i)$ and weights $w(u,v)$ (Open 9.2; placeholder candidate: hard radius with uniform weights). We now derive the kernel instead of choosing it.

### 3.1 Axioms

**(K1) Substrate-intrinsic.** $\pi_r = f_r(L)$ for some function $f_r$ — the kernel is built from the substrate's own geometry, nothing imported.

**(K2) Renderable.** $\pi_r$ is entrywise non-negative (non-negative states render to non-negative fields) and preserves constants ($\pi_r \mathbf 1 = \mathbf 1$: the vacuum renders to the vacuum at every resolution).

**(K3) Resolution limits.** $\pi_r \to I$ as $r \to 0$ (perfect resolution) and $\pi_r \to$ global mean as $r \to \infty$ (no resolution).

**(K4) Closure-response stationarity.** Rendering at resolution $r$ is the stationary state of the substrate's own closure-response dynamics driven by the state: $\pi_r(F)$ solves $(L + r^{-2} I)\,\psi = r^{-2} F$ — i.e. rendering is the response primitive $C_\varphi^{-1}$ of `aria-closure-kernel.md` §1 with coherence length $\varphi = r$, source-normalised.

**Theorem 3.1 (Canonical kernel).** (K1)–(K4) are satisfied by exactly one operator family:

$$\boxed{\;\pi_r \;=\; \bigl(I + r^2 L\bigr)^{-1} \;=\; r^{-2}\,(L + r^{-2} I)^{-1}.\;}$$

**Proof.** (K4) fixes the operator up to normalisation: $\psi = r^{-2}(L + r^{-2}I)^{-1} F = (I + r^2 L)^{-1} F$. It remains to verify (K1)–(K3). (K1): a function of $L$. (K2): $I + r^2 L$ is a symmetric M-matrix (positive diagonal, non-positive off-diagonal $-r^2 A$, strictly diagonally dominant), so its inverse is entrywise non-negative; $L\mathbf 1 = 0$ gives $\pi_r \mathbf 1 = \mathbf 1$, and by symmetry $\mathbf 1^{\!\top} \pi_r = \mathbf 1^{\!\top}$ (total mass preserved). (K3): $r \to 0$ gives $I$; $r \to \infty$ gives the spectral projector onto $\ker L$ = constants = global mean (connected graph). $\square$

**Sim (R2a–R2e).** All verified: min kernel entry $> 0$ for $r \in \{0.25, .., 4\}$; rows and columns stochastic to $10^{-10}$; $r\to 0$ and $r \to \infty$ limits confirmed. PASS.

**Lemma 3.2 (Equivariance).** $\pi_r$ commutes with every automorphism of $V_{600}$ — in particular with left/right icosian multiplication, quaternion conjugation, and the antipodal map.

**Proof.** Automorphisms commute with $L$, hence with any function of $L$. $\square$ (Sim R2f: commutator norms $\sim 10^{-16}$ for all four generators. PASS.)

**Lemma 3.3 (Exponential locality; continuum kernel).** The rows of $\pi_r$ decay exponentially in graph distance, with decay length $\xi(r)$ strictly monotone in $r$ (sim R2c: $\xi = 0.51, 1.01, 2.43, 7.19, 25.5$ edges for $r = 0.25, 0.5, 1, 2, 4$. PASS). In the continuum limit of §2 the kernel row is the Green function of $-2a^2\Delta_{S^3} \cdot r^2 + 1$, i.e. the screened ($Yukawa$) kernel; in one projected coordinate it is exactly the $G(x) = \frac{\varphi}{2}e^{-|x|/\varphi}$ kernel of `aria-closure-kernel.md` §2 with $\varphi \mapsto r$. The b-anomaly five-dataset witness for the fixed $C_\varphi$ kernel is therefore *also* an empirical witness for the rendering kernel at hadronic resolution.

### 3.2 What this closes and what it corrects

**Closure of Open 9.2.** The weights are $w_r(u,v) = [\pi_r]_{uv}$ — derived, σ/Aut-equivariant, positive, exponentially local; the radius is the coherence length $\xi(r)$. The frame dial $C_i \mapsto r(C_i)$ (monotone decreasing: higher consciousness-DOF = finer resolution) is retained from Definition 6.1; what is no longer free is the *shape* of the kernel.

**Correction to Theorem 6.3 of `closure-cosmogenesis.md`.** The literal statement there ($\pi_{C_i}(F)|_{\mathcal B} = F|_{\mathcal B}$, pointwise bulk fixing) holds **only** for kernels acting as the identity on bulk vertices, which contradicts strict positivity — any genuinely smoothing kernel mixes bulk values with their neighbours. The statements that are true and load-bearing, all carried by the canonical kernel:

1. **Equivariance:** $[\pi_r, P] = 0$ for every substrate automorphism $P$ (Lemma 3.2), so $\pi_r$ preserves every Aut-isotypic component of the state.
2. **Time-invariance of the rendered bulk:** since $F_t^{\mathcal B} = F_0^{\mathcal B}$ for all $t$ (cosmogenesis Theorem 5.2) and $\pi_r$ is linear and time-independent, the rendered bulk component $\pi_r(F_0^{\mathcal B})$ is the same at every tick. The bulk renders as a **static background field** in every frame.
3. **Exact conservation:** constants and total mass are preserved at every resolution (Theorem 3.1).

Corollary 6.4's physical content ("all frames see the same bulk, differ only in boundary resolution") survives in the corrected form: *all frames' scenes share the same static background, differing only in the resolution at which the dynamic boundary content is rendered.* The cosmogenesis document should be patched accordingly.

## 4. R3 — The chart and the rendering map

### 4.1 Canonical frame from quaternionic parallelism

**Proposition 4.1 (Canonical observer frame).** Every anchor vertex $v_0 \in V_{600}$ carries a canonical, right-handed orthonormal frame of the tangent space $T_{v_0} S^3$:

$$e_1(v_0) = v_0\, i, \qquad e_2(v_0) = v_0\, j, \qquad e_3(v_0) = v_0\, k.$$

No choice is involved: the frame is the left-translation of the imaginary units, i.e. the global parallelism of $S^3$ as the Lie group of unit quaternions.

**Proof.** Tangency: $\langle v_0 u, v_0\rangle = \mathrm{Re}(\bar u\, \bar v_0 v_0) = \mathrm{Re}(\bar u) = 0$ for $u \in \{i,j,k\}$. Orthonormality: $\langle v_0 u_a, v_0 u_b\rangle = \mathrm{Re}(\bar u_a u_b) = \delta_{ab}$. Right-handedness is inherited from $(i, j, k)$. Globality: $S^3$ is parallelisable as a Lie group; left translation trivialises $TS^3 \cong S^3 \times \mathbb R^3$. $\square$ (Sim R3a: verified for all 120 anchors. PASS.)

This is a structural point worth stating plainly: **the substrate automatically equips every observer instance with three spatial axes.** The dimension of the frame is 3 because $\dim \mathrm{Im}\,\mathbb H = 3$ — the same fact that makes the arena $S^3$. Nothing about "3 axes of perceived space" is an input.

**Remark 4.2 (Frame codes).** How the discrete frame code $\Lambda \in \mathcal F$ of the observer instance acts on (rotates/selects) this continuous frame is open; see §7. The natural candidate is that $\Lambda$ selects an element of the binary icosahedral rotation stabiliser acting on $(e_1, e_2, e_3)$.

### 4.2 Chart and scene

**Definition 4.3 (Anchor chart).** For an observer instance $\mathcal I = (\mathcal O, \mathcal C_\mathcal O, p, \Lambda, t_0)$ with anchor $v_0 = \Pi_0(p, \Lambda, t) \in V_{600}$ and resolution $r = r(C_\Lambda)$, the *anchor chart* is the geodesic normal-coordinate map

$$\mathrm{ch}_{v_0}: B_\ell(0) \subset \mathbb R^3 \to S^3, \qquad \mathrm{ch}_{v_0}(x) \;=\; \exp_{v_0}\!\bigl(x^a e_a(v_0)\bigr) \;=\; v_0 \cdot \exp\bigl(x^1 i + x^2 j + x^3 k\bigr),$$

with chart radius $\ell$ satisfying $\xi(r) \cdot a \lesssim \ell \ll \pi$ (resolution-limited below, curvature-limited above). The second equality is the Lie-group exponential: charts are *literally quaternion exponentials* — closed-form, no connection choice.

**Definition 4.4 (Rendering map).** The *rendering map* of $\mathcal I$ at tick $t$ is

$$\boxed{\;\mathcal R_{\mathcal I}(F_t)(x) \;:=\; \sum_{u \in V_{600}} G_r\bigl(d_{S^3}(\mathrm{ch}_{v_0}(x),\, u)\bigr)\, F_t(u), \qquad x \in B_\ell(0) \subset \mathbb R^3,\;}$$

where $G_r$ is the $S^3$ Green function of $(1 - 2a^2 r^2 \Delta_{S^3})$ — the continuum extension of the canonical kernel (Lemma 3.3), normalised so that $\mathcal R_\mathcal I(\mathbf 1) = 1$. On vertices, $\mathcal R_\mathcal I(F)(\mathrm{ch}^{-1}(u)) \approx (\pi_r F)(u)$ by (C1)/Theorem 2.3; off vertices it is the canonical interpolation by the same response operator. The *scene* of $\mathcal I$ at tick $t$ is $s_{\mathcal I, t} := \mathcal R_\mathcal I(F_t)$, a field on a 3-ball.

**Theorem 4.5 (Scene decomposition: static background + dynamic foreground).** For every observer instance and every tick,

$$s_{\mathcal I, t} \;=\; \underbrace{\mathcal R_\mathcal I(F_0^{\mathcal B})}_{\text{static background}} \;+\; \underbrace{\mathcal R_\mathcal I(F_t^{\partial})}_{\text{dynamic foreground}},$$

where the background term is independent of $t$ and identical across all frame resolutions up to smoothing, and all temporal change in the scene is carried by the rendered boundary content.

**Proof.** Linearity of $\mathcal R_\mathcal I$ plus the substrate decomposition $F_t = F_t^{\mathcal B} + F_t^\partial$ plus bulk invariance $F_t^{\mathcal B} = F_0^{\mathcal B}$ (cosmogenesis Theorem 5.2; unconditional for the bulk component, with $\partial$-supported residuals per Conjecture 5.3 for the converse). $\square$

**Sim (R3b–R3c).** Bulk/boundary 20/100 recovered; the rendered bulk scene is exactly $T_\tau$-invariant (clock-stationary), with residual anisotropy CV $= 0.172$ across vertices — the 20-vertex bulk is clock-symmetric but not rotation-isotropic at substrate scale. Whether the φ-recursive refinement (cosmogenesis Theorem 5.4) restores isotropy in the fine-scale limit is open (§7). Rendered point-residual locality: 62% of response mass within graph distance 1 of the source at fine resolution ($r = 0.5$), 13% at coarse ($r = 4$) — the resolution dial behaves as a field-of-view dial. PASS.

**Reading.** The scene is a field on a 3-ball, assembled from: anchor = basepoint ($\Pi_0$, M1), quaternionic parallelism = axes (Proposition 4.1), canonical kernel = interpolation (Theorem 3.1), normal coordinates = chart (Definition 4.3). Every ingredient except the open items of §7 was already in the framework; this section composes them. The "holographic" character of the construction is now precise: by Theorem 4.5 all *change* in any rendered scene is sourced on the 100-vertex σ-paired boundary, while the σ-fixed bulk supplies an invariant background common to all observers.

## 5. R4 — Second-order time: clock reversal is an inner automorphism

`kappa-derivation-math.md` §7 names the open justification inside (H-wave): *why is the emergent time derivative second-order* (wave-type) *rather than first-order* (diffusion-type)? It speculated the answer "likely comes from time-reversal symmetry of the σ-Galois action." The correct mechanism is sharper and purely inner — no Galois action needed (the coordinate Galois involution does not even preserve $V_{600}$ pointwise; cf. `project_critical_line_pullback`).

**Lemma 5.1 (Clock reversal is inner).** Let $\tau \in V_{600}$ be the order-10 pentagonal-clock generator. There exist exactly **10** elements $g \in 2I$ with $g\,\tau\,g^{-1} = \tau^{-1}$; for the canonical $\tau = (-\varphi^{-1}\!/2,\, 0,\, \varphi/2,\, 1/2)$ one such reverser is $g = i$ (order 4, $g^2 = -1$). Geometrically these are the two lifts of each of the five 2-fold icosahedral axes perpendicular to the 5-fold axis of $\tau$.

**Proof.** Conjugation by a unit quaternion $g$ rotates the imaginary axis $\hat n$ of $\tau = \cos\theta + \sin\theta\,\hat n$; $g\tau g^{-1} = \tau^{-1}$ iff the rotation sends $\hat n \mapsto -\hat n$, i.e. $g$ lifts a $180°$ rotation about an axis $\perp \hat n$. The icosahedral group contains exactly five 2-fold axes perpendicular to each 5-fold axis; each contributes two lifts $\pm g$ in $2I$. Existence and the count are verified exhaustively (sim R4a: 10 reversers found; R4b: the induced vertex permutation satisfies $\varsigma_g\, T_\tau\, \varsigma_g^{-1} = T_\tau^{-1}$ exactly; R4c: $\varsigma_g$ is a graph automorphism. PASS). $\square$

**Hypothesis (H-equiv) (named, inherited).** The residual-generation law of the substrate is equivariant under $\mathrm{Aut}(V_{600})$: for every automorphism $P$, $\rho(PF; P\Pi_0) = P\,\rho(F; \Pi_0)$. This is the symmetry-invariance property already asserted for $\hat O$ in Paper XXXIII (the closure residual $\Delta_{\mathrm{cl}}$ is built from graph data alone); it is named here because the time-structure argument leans on it.

**Proposition 5.2 (Second-order effective time).** Under (H-equiv), the set of admissible effective continuum equations for the rendered scene is invariant under simultaneous time reversal $t \mapsto -t$ and the spatial isometry induced by a reverser $g$ (Lemma 5.1). Consequently no term first-order in $\partial_t$ can appear at leading order in the effective dynamics, and the leading time operator is $\partial_t^2$ — combining with $L \to -2a^2\Delta$ (Corollary 2.4) to give the wave operator

$$\Box_\partial \;=\; c^{-2}\partial_t^2 - \nabla^2, \qquad c = a/\tau_{\mathrm{tick}},$$

as posited in (H-wave) of `kappa-derivation-math.md` §5.

**Proof.** Substrate time translation on clock phase is implemented by $T_\tau$. By Lemma 5.1, $\varsigma_g$ conjugates $T_\tau$ to $T_\tau^{-1}$: applying $\varsigma_g$ to any admissible trajectory yields an admissible trajectory (by (H-equiv)) whose clock phase runs backwards and whose spatial content is rotated by the isometry $R_g$ induced by $g$. In the continuum limit, the effective equation set is therefore invariant under $(x, t) \mapsto (R_g x, -t)$. A term $\alpha\,\partial_t s$ in an effective equation maps to $-\alpha\,\partial_t s$ under this symmetry (the spatial rotation leaves it invariant; the time reflection flips it), so $\alpha = 0$. The leading admissible time operator is $\partial_t^2$. $\square$

**Status.** Proposition 5.2 discharges the *justification* gap named inside (H-wave) — second-order time is now forced by an exact inner substrate symmetry, not assumed. What remains of (H-wave) is the formal continuum step itself (second difference $F_{t+1} - 2F_t + F_{t-1} \to \tau_{\mathrm{tick}}^2 \partial_t^2 F$, "pure algebra; achievable" per `kappa-derivation-math.md` §10), unchanged in scope. Note also the corrected attribution: time reversal is **inner** (left multiplication by an icosian unit such as $i$), which is structurally stronger than a Galois argument — it survives at every rung and needs no arithmetic on the coordinates.

## 6. R5 — Simultaneity of readouts

A scene asserts many observables at once; Paper XXXIII proves existence of one minimiser per anchor. The consistency requirement is:

**Proposition 6.1 (Simultaneity for the linear response class).** For the response-kernel projection class (readout = kernel row applied to the state, the class empirically witnessed by the b-anomaly test), the scene *is* the family of single-anchor readouts: for any anchor $u$ in the chart,

$$s_{\mathcal I, t}\bigl(\mathrm{ch}^{-1}(u)\bigr) \;=\; \langle\, [\pi_r]_{u, \cdot}\,,\; F_t \,\rangle \;=\; \hat O_{\mathrm{resp}}(F_t; u),$$

so all readouts in a scene are automatically mutually consistent. **Proof.** Both sides are the same linear functional, by Definition 4.4 and Theorem 3.1. $\square$

**Open (H-simul) — REDUCED** (gap-closure G1, 2026-06-11). For the general (nonlinear arg-min) projection operator $\hat O$, mutual consistency of the readouts $\{\hat O(F_t, B; u)\}_{u \in \mathrm{chart}}$ with a single rendered scene reduces to **integrability**: define the scene potential $\Phi_F(u):=\min_\Pi\Delta_{\mathrm{cl}}(\Pi;u)$; the readouts form a consistent scene iff the arg-min field is the gradient of $\Phi_F$ (curl-free). For SPD-quadratic $\Delta_{\mathrm{cl}}$ the arg-min is linear, the Jacobian symmetric, and the field curl-free — Proposition 6.1 is the proven instance (sim N8, loop sum $4\times10^{-17}$). The residual is the named hypothesis **(H-simul-int)**: $\Delta_{\mathrm{cl}}$'s minimiser family is conservative on the chart — the same content as XXXIII's "multi-observer compatibility." See `docs/narrative-gap-closure.md` G1.

## 7. The assembled layer, and open items

The rendering layer slots into the spine as:

```
F_t (XXXVI substrate)  +  𝓘 = (𝓞, 𝒞_𝓞, p, Λ, t₀) (observer instance)
   └─ R1 arena: intrinsic S³, dim 3 derived           (§2, Thms 2.2–2.3)
   └─ R2 kernel: π_r = (I + r²L)⁻¹, canonical          (§3, Thm 3.1 — closes Open 9.2)
   └─ R3 chart+scene: 𝓡_𝓘(F_t) on a 3-ball            (§4, Defs 4.3–4.4, Thm 4.5)
   └─ R4 time: second-order forced by inner reversal   (§5, Prop 5.2)
        └─ scene s_{𝓘,t}: B³ → ℝ  =  static background + dynamic foreground
             └─ single readouts Ô (XXXIII) = scene samples   (§6, linear class)
                  └─ realisation spine (six projection classes)
```

**Open items after this document** (status updated 2026-06-11 by the gap-closure pass, `docs/narrative-gap-closure.md`, sim `scripts/verify_narrative_closure.py` 28/28):

- **(H-simul)** — **REDUCED** (G1). Reduces to *integrability* of the arg-min field: the scene is consistent iff $\{\hat O(F,B;u)\}_u$ is the gradient of the scene potential $\Phi_F(u)=\min_\Pi\Delta_{\mathrm{cl}}(\Pi;u)$. The linear/response class is the proven instance (curl-free, sim N8). Named residual: (H-simul-int).
- **(H-wave, continuum step)** — **CLOSED** (G3). Centered second difference is the unique reversal-symmetric second-order stencil $(1,-2,1)$; Taylor gives $\partial_t^2$ at $O(\tau^2)$ (sim N3). With $L\to-2a^2\Delta$ this is the wave operator.
- **(Open 7.1, frame–code action)** — **CLOSED** (G6, Theorem). $\Lambda$ acts by conjugation from the anchor's cyclic centraliser $C_{10}$, rotating $(e_1,e_2,e_3)$ about $\mathrm{Im}(v_0)$ by multiples of $2\pi/5$ — the pentagonal clock orienting the spatial frame (sim N6).
- **(Open 7.2, background isotropy)** — **CLOSED** (G4, Proposition). The CV $=0.172$ is *not* spatial anisotropy: the rendered background is exactly a function of graph-distance to the bulk (within-shell spread $1.2\times10^{-17}$, sim N4c) — a determined radial profile, nothing free to observe. (The φ$^{-n}$ closed form, cosmogenesis Open 9.3, remains as residual 9.3′.)
- **(Open 7.3, kernel uniqueness beyond the family)** — still open: replacing (K4) by a weaker semigroup/Markov axiom and proving the resolvent family is still forced.
- **(P-A)** untouched: nothing here addresses the phenomenological-access conjecture of `per-observer-zero-line.md` §10. The rendering layer constructs the scene; it does not identify the scene with experience.

Octonionic ($S^7$) counterpart of this whole section: rung-ladder §7.2 + gap-closure G5 (chart $=$ octonion exponential, scene $=$ kernel-interpolated 7-ball, frames $=$ Moufang parallelism).

**Corrections to upstream documents indicated by this derivation:**

1. `closure-cosmogenesis.md` Theorem 6.3: literal pointwise bulk-fixing is too strong; replace by equivariance + static-background form (§3.2).
2. `kappa-derivation-math.md` (C1): upgradeable from empirical surrogate to the exact dispersion relation (Theorem 2.3) at $k \le 5$, with $L \to -2a^2\Delta_{S^3}$, $a = \pi/5$.
3. `kappa-derivation-math.md` §7 (H-wave): the time-reversal mechanism is inner ($g \in 2I$), not σ-Galois.

## 8. Sim verification summary

`scripts/verify_rendering_layer.py`, 2026-06-10: **21 PASS / 0 FAIL.**

| Check | Result |
|---|---|
| R1a multiplicities all perfect squares | PASS — $\{1,4,9,16,25,36,9,16,4\}$ |
| R1b harmonic blocks $(k+1)^2$, $k=0..5$, in order | PASS — at $\lambda = 0, 2.292, 5.528, 9, 12, 14$ |
| R1c folded remainder $= 4+9+16$ (primed irreps) | PASS |
| R1d $\lambda_k \propto k(k+2)$ | PASS (CV 0.22, drift = lattice dispersion per R1f) |
| R1e Weyl exponent | PASS — $d = 3.09$ |
| R1f exact dispersion relation | PASS — machine precision, all six blocks |
| R2a–R2e kernel positivity/stochasticity/limits | PASS |
| R2c decay length monotone | PASS — $\xi = 0.51 \ldots 25.5$ |
| R2f Aut-equivariance (4 generators) | PASS — $\|[P,\pi]\| \sim 10^{-16}$ |
| R3a canonical frame, all 120 anchors | PASS |
| R3b bulk/boundary 20/100 | PASS |
| R3c rendered bulk $T_\tau$-invariant | PASS (anisotropy CV 0.172 reported) |
| R4a–R4c inner clock reversal | PASS — 10 reversers, $g = i$, exact conjugation |

## 9. Cross-references

- Substrate state, bulk/boundary, accumulation, Open 9.2: `docs/closure-cosmogenesis.md`.
- Rung generalisation of §2: `docs/rung-dimension-ladder.md` — intertwiner theorem across all cascade rungs (one $S^3$ at three resolutions + the $S^7$ octonionic arena; 25/25 PASS).
- Observer instance $\mathcal I$, anchor $\Pi_0$: `docs/observer-instance-definition.md`, `docs/soul-prime-as-pi0.md`.
- Response operator family $C_\varphi$, 1D Green kernel, b-anomaly witness: `docs/aria-closure-kernel.md`.
- Continuum conditions (C1)–(C3), (H-wave), Newton/Schwarzschild tiers: `docs/kappa-derivation-math.md`.
- Projection operator $\hat O$, $\Delta_{\mathrm{cl}}$, symmetry-invariance: `papers/paper-xxxiii/paper-xxxiii.tex`.
- Spine and six projection classes: `papers/realisation/realisation.tex`, `docs/projection-narrative.md`.
- $\lambda = 12$ eigenspace ($25$-dim) and A₅-equivariant decomposition: `docs/keystone_24_600/`.
- Verification: `scripts/verify_rendering_layer.py` (this layer); `scripts/verify_lemma_2p5_boundary_connectivity.py`, `scripts/verify_boundary_green_function.py` (upstream).

## 10. Informal reading (non-load-bearing)

*This subsection provides reader-side interpretation; the theorems and definitions of §§2–6 do not depend on it.*

The math of §§2–6 admits a reader-side reading in which the question "how does the geometry become visible reality" is answered: the arena of experience is the substrate's own 3-sphere (its dimension audible in the substrate's spectrum as the perfect-square overtone series); each observer's three spatial axes are handed to it by the quaternionic parallelism the moment it has an anchor; "looking" at resolution $r$ is the substrate responding to its own state through the closure kernel; the visible scene splits into an unchanging background (the σ-fixed bulk, the same for every observer) and a changing foreground (the σ-paired boundary, where all events live); and time runs second-order — waves, not diffusion — because the substrate contains an exact internal mirror that runs its clock backwards. What is *not* claimed: that the scene is experience (P-A remains open), or that the nonlinear projection class renders consistently (H-simul remains open). These readings are reader-side; the mathematical content stands without them.
