# Einstein's Equations from the Substrate: Closing the GR Chain

**Date:** 2026-06-11
**Status:** Derivation complete at effective-field-theory level; sim-verified by `scripts/verify_gr_closure.py`. Named residuals listed in §13.
**Supersedes:** the open status of Conjecture 6.6.1 and Obstacles 1–3 in `docs/kappa-derivation-math.md` §6.6–6.7; discharges (H-stress), (H-trace), and the remaining algebra of (H-wave); reduces (H-tensor) to the collective-field construction of §4.

---

## 1. Purpose and result

`docs/kappa-derivation-math.md` left the GR chain in the following state: Newton derived (Theorems 4.1–4.4), the conditional Schwarzschild Theorem 6.1 resting on four hypotheses (H-wave, H-tensor, H-stress, H-trace), and the Fierz–Pauli Conjecture 6.6.1 blocked by three named obstacles, the load-bearing one (Obstacle 1) being:

> the substrate action is quadratic in $F$, hence quartic in $h_{\mu\nu} \sim (\partial F)^2$, so it is not a quadratic Fierz–Pauli action for $h$.

This document closes the chain. The key move is a **reidentification**: the symmetric bilinear $\langle \partial_\mu F, \partial_\nu F\rangle$ of §6.7.2 is not the metric perturbation. It is (up to its trace part) the canonical **stress-energy tensor** of the substrate field — the *source* of gravity, not gravity itself. Once the bilinear is put on the correct side of the field equation, "quadratic in $F$ = quadratic in the source" is exactly what a matter sector should be, and Obstacle 1 dissolves: it was a category error, not a wall.

The metric perturbation $h_{\mu\nu}$ is then identified as the **collective (coarse-grained) deformation field** of the rendered scene, and its dynamics is not constructed but **forced**, by a uniqueness theorem: given the three substrate-derived inputs

1. a symmetric rank-2 collective field (§4),
2. second-order time / the substrate wave operator (`docs/rendering-layer.md` Prop 5.2),
3. invariance under chart redescription (§5),

the unique quadratic action is Fierz–Pauli, the trace-reversed coupling and the factor 2 follow as theorems (§7), the source is forced to be the conserved stress tensor (§6), and the unique consistent nonlinear completion is Einstein's equations with a cosmological constant as the single allowed constant (§8, riding the classical Gupta–Kraichnan–Feynman–Deser bootstrap). Every finite-dimensional step is verified numerically in `scripts/verify_gr_closure.py`.

**Result.** Modulo the named residuals of §13 (continuum-limit rigor, Gaussian-regime restriction, the classical bootstrap citations, and the calibration constant $G$ of Definition 4.2), the substrate implies the full Einstein field equations
$$G_{\mu\nu} + \Lambda g_{\mu\nu} \;=\; \frac{8\pi G}{c^4}\, T_{\mu\nu},$$
with $\Lambda$ not fixed by this chain but fixed independently by the programme's cosmology wing (`hypersphere-cosmology` v1.1: $\Omega_\Lambda$ within 0.083% of Planck).

---

## 2. Inputs (all previously derived)

- **(I1) Substrate wave dynamics.** Second-order time is forced by the inner clock reversal $g\tau g^{-1} = \tau^{-1}$, $g \in 2I$ (`rendering-layer.md` Lemma 5.1 + Prop 5.2, sims R4a–R4c). Spatial operator $L_\partial/a^2 \to -\nabla^2$ (kappa §3, C1 upgraded by the exact dispersion relation of rendering-layer R1f). Together: $\Box = c^{-2}\partial_t^2 - \nabla^2$ with $c = a/\tau$. The one remaining formality of (H-wave) — the second-difference continuum step — is closed in §9.1 below (Taylor algebra + sim T10).
- **(I2) Arena and chart.** Rendered arena is intrinsic $S^3$, dimension 3 derived from the spectrum; canonical kernel $\pi_r = (I + r^2L)^{-1}$; anchor chart $\mathrm{ch}_{v_0}$ via quaternion exponential with frame $\{v_0 i, v_0 j, v_0 k\}$ (`rendering-layer.md` R1–R3). The chart is explicitly **non-canonical**: it is observer bookkeeping, not substrate structure.
- **(I3) Newton.** $\nabla^2\Phi_\infty = 4\pi G\rho_m$, $\Phi_\infty = -GM/r$ (kappa Theorems 4.1–4.4, witnessed by `verify_boundary_green_function.py`).
- **(I4) Quaternionic substrate field.** $F : V_{600}\times\mathbb Z \to \mathbb H$ with discrete tangent-frame derivatives $\partial_\mu F$ (kappa §6.7.1), action $S_F = \int[-\tfrac{\alpha}{2}\langle\partial_\mu F, \partial^\mu F\rangle + \langle F, J\rangle]$, EOM $\Box F = -J/\alpha$ (kappa 6.7.2–6.7.3).
- **(I5) Response-operator family.** $C_\varphi = L_\partial + \varphi^{-2}I$: the $\varphi^{-1}\to 0$ end is the Newton regime, finite $\varphi^{-1}$ the massive/Yukawa regime (kappa §4.6). Used in §11 for the QM bridge.

---

## 3. Step A — Reidentification: the bilinear is the stress tensor

**Theorem A.1 (canonical stress tensor; discharges (H-stress)).** For the substrate field $F$ with action (I4), the canonical Noether current of spacetime-translation invariance is
$$\Theta_{\mu\nu} \;:=\; \alpha\left[\langle\partial_\mu F, \partial_\nu F\rangle \;-\; \tfrac{1}{2}\,\eta_{\mu\nu}\,\langle\partial_\rho F, \partial^\rho F\rangle\right],$$
which is (i) symmetric, (ii) conserved on shell, $\partial^\mu\Theta_{\mu\nu} = \alpha\,\langle\Box F, \partial_\nu F\rangle = 0$ when $\Box F = 0$, and (iii) has non-negative energy density $\Theta_{00} = \tfrac{\alpha}{2}(\langle\partial_0F,\partial_0F\rangle + \langle\partial_iF,\partial_iF\rangle) \ge 0$.

*Proof.* Standard: $\partial^\mu\Theta_{\mu\nu} = \alpha[\langle\Box F,\partial_\nu F\rangle + \langle\partial_\mu F,\partial^\mu\partial_\nu F\rangle - \langle\partial_\rho F, \partial_\nu\partial^\rho F\rangle] = \alpha\langle\Box F, \partial_\nu F\rangle$. Symmetry is manifest; positivity of $\Theta_{00}$ is a sum of squares. $\square$

On the **discrete substrate** the time-component statements are exact, not approximate. For the leapfrog substrate dynamics $F_{t+1} = 2F_t - F_{t-1} - \varepsilon^2 LF_t$ (the discrete form of (I1)):

**Lemma A.2 (exact discrete conservation).** (a) The discrete energy $E_{t+1/2} = \tfrac{1}{2}\|({F_{t+1}-F_t})/{\tau}\|^2 + \tfrac{c^2}{2a^2}\langle F_t, LF_{t+1}\rangle$ is conserved tick-by-tick exactly. (b) In the semi-discrete dynamics $\ddot F = -(c^2/a^2)LF$, the local energy $e_v = \tfrac{1}{2}\dot F_v^2 + \tfrac{c^2}{4a^2}\sum_{w\sim v}(F_v - F_w)^2$ and edge flux $J_{vw} = \tfrac{c^2}{2a^2}(F_v - F_w)(\dot F_v + \dot F_w)$ satisfy the **exact** continuity equation $\dot e_v + \sum_{w\sim v} J_{vw} = 0$ at every vertex. (Sims T5, T6.)

**Lemma A.3 (dust limit).** For a slowly modulated carrier mode (envelope scale $\gg$ carrier scale), $\Theta_{00} \to \rho c^2$ and $|\Theta_{ij}|/\Theta_{00} = O(\epsilon^2)$ where $\epsilon$ is the envelope/carrier scale ratio — i.e. matter wavepackets source gravity as static dust at leading order, exactly the source used in kappa Theorem 6.1. (Sim T7.)

**Consequence for Obstacle 1.** The diagnosis "action quadratic in $F$ is quartic in $h$" assumed $h \sim \langle\partial F, \partial F\rangle$. With the bilinear correctly identified as $\Theta_{\mu\nu}$, "quadratic in $F$" means "quadratic in matter" — the matter coupling $h_{\mu\nu}\Theta^{\mu\nu}$ is *supposed* to be quadratic in $F$. Obstacle 1 is dissolved, not solved: there was nothing to solve. The remaining question — where does $h$ itself live? — is §4.

---

## 4. Step B — The collective metric field

**Definition B.1 (rendered deformation field).** Let $\delta F$ denote the substrate fluctuation about the homogeneous closure background, and let $\pi_r$ be the canonical kernel (I2). The **rendered deformation field** at chart point $x$ is the coarse-grained, background-subtracted second moment
$$h_{\mu\nu}(x) \;\propto\; \pi_r\!\left[\,\langle\partial_\mu \delta F\, \partial_\nu \delta F\rangle\,\right](x) \;-\; (\text{homogeneous background value}),$$
a symmetric rank-2 field on the chart, with 10 components.

This is a **collective field**: a constrained statistic of many substrate modes per kernel cell, not a pointwise function of $F$. Two facts give it independent dynamics:

**Proposition B.2 (tensoriality).** Under the substrate symmetry $2I\times 2I$ acting by left/right icosian multiplication, the frame components $h_{ab}$ transform as a rank-2 tensor: left multiplication acts trivially on the right-quaternionic frame ($g(v\,i) = (gv)\,i$), and right multiplication by $g^{-1}$ rotates the frame by the adjoint $SO(3)$ action $i \mapsto g\,i\,g^{-1}$, so $h \mapsto R_g^{\!\top} h\, R_g$ with $R_g = \mathrm{Ad}(g)$. (Sim T14, on the actual 600-cell.)

**Proposition B.3 (quadratic effective action; dissolves the dynamical half of Obstacle 1).** Let $h$ be the sample second moment of $N$ independent substrate modes per kernel cell in the Gaussian (linear-response) regime. The effective action (constrained free energy) is
$$\Gamma[h] \;=\; \tfrac{N}{4}\,\mathrm{tr}\!\left[(\Sigma_0^{-1}\delta h)^2\right] \;+\; O\!\left(N\,\delta h^3\right),$$
and since equilibrium fluctuations scale as $\delta h \sim N^{-1/2}$, the cubic term is $O(N^{-1/2})$ **relative to** the quadratic one. In the coarse limit $N \to \infty$ the effective action of the collective field is exactly quadratic.

*Proof sketch.* For Gaussian modes the sample covariance is Wishart-distributed; $\log P(h)$ is $N$ times an analytic function of $h$ with a nondegenerate quadratic minimum at $\Sigma_0$; expand. (Sim T15 verifies the quadratic dominance and the $N$-scaling numerically on Wishart samples.) $\square$

This is the standard emergent-field mechanism (it is how phonons acquire a quadratic action from an anharmonic microscopic crystal). The microscopic action's order in $F$ is irrelevant to the order of the **effective** action in the collective field. What Proposition B.3 does *not* fix is which quadratic action — that is §5–§6, and it is forced.

**Status of (H-tensor).** Reduced from "ansatz (5.5)" to Definition B.1 + Propositions B.2–B.3: the substrate supplies a symmetric rank-2 collective field with a quadratic effective action. The specific coefficient pattern is *not* assumed; it is derived next.

---

## 5. Step C — Gauge invariance from chart freedom

**Proposition C.1 (chart redescription acts as linearised diffeomorphism).** The anchor chart $\mathrm{ch}_{v_0}$ of (I2) is observer bookkeeping: no substrate quantity depends on it. An infinitesimal redescription $x \mapsto x + \xi(x)$ of the chart changes the components of the rendered metric $g = \eta + h$ by the Lie derivative, i.e. at linear order
$$h_{\mu\nu} \;\longmapsto\; h_{\mu\nu} + \partial_\mu \xi_\nu + \partial_\nu \xi_\mu + O(\xi\,\partial h,\ \xi^2).$$
Since the substrate physics is chart-independent, the effective action $\Gamma[h]$ must be invariant under this shift. (Sim T8 verifies the transformation law numerically by re-charting a rendered metric.)

Two honesty notes. (i) The substrate does have a preferred *frame* (the tick direction $u^\mu$): a frame is a state of motion, not a chart, and does not reduce the redescription freedom — the same situation as cosmology, where the CMB frame coexists with full diffeomorphism invariance. (ii) The discrete lattice has no continuous diffeomorphisms; the statement lives at the level of the **rendered** (kernel-smoothed) fields, where the chart is literally an arbitrary choice in `rendering-layer.md` Definition 4.3. This is where the frame non-canonicity flagged in kappa §6.7.1 ("gauge-invariance of the eventual action under local frame rotation has to be checked") gets its answer: the non-canonicity *is* the gauge freedom.

---

## 6. Step D — Uniqueness: Fierz–Pauli is forced

**Theorem D.1 (uniqueness of the quadratic action).** The most general local, Lorentz-invariant action for a symmetric rank-2 field $h_{\mu\nu}$ with at most two derivatives is, modulo total derivatives, a 6-parameter family
$$S[h] = \!\int\! d^4x\,\Big[a_1\,\partial_\rho h_{\mu\nu}\partial^\rho h^{\mu\nu} + a_2\,\partial_\mu h^{\mu\nu}\partial^\rho h_{\rho\nu} + a_3\,\partial_\mu h^{\mu\nu}\partial_\nu h + a_4\,\partial_\mu h\,\partial^\mu h + b_1\, h_{\mu\nu}h^{\mu\nu} + b_2\, h^2\Big].$$
Invariance under $h_{\mu\nu} \to h_{\mu\nu} + \partial_\mu\xi_\nu + \partial_\nu\xi_\mu$ for all $\xi$ forces $b_1 = b_2 = 0$ and
$$(a_1, a_2, a_3, a_4) \;\propto\; \left(-\tfrac{1}{2},\ 1,\ -1,\ \tfrac{1}{2}\right),$$
i.e. the solution space is exactly one-dimensional and is the **Fierz–Pauli action**. The graviton is massless (the $b$'s die) and carries exactly **2** physical polarisations ($10 - 4$ gauge $- 4$ constraints).

*Proof.* Finite linear algebra in momentum space: write the action as a quadratic form $Q(h,h;k)$, impose $Q(h, \delta_\xi h; k) = 0$ for all $h, \xi, k$, and compute the null space of the resulting linear system on $(a_1,\dots,b_2)$. This is done **numerically with random sampling and SVD** in sims T1 (null space is 1-dimensional with the stated ratios, mass terms killed) and T2 (kernel of the FP operator at null momentum is 6-dimensional, containing the 4-dimensional gauge orbit, leaving 2 physical polarisations). The result is the classical Fierz–Pauli uniqueness theorem (Fierz–Pauli 1939); the sim re-derives it from scratch so the chain nowhere assumes it. $\square$

**Corollary D.2.** The variation of the Fierz–Pauli action is the linearised Einstein tensor: $\delta S_{FP}/\delta h^{\mu\nu} \propto G^{\mathrm{lin}}_{\mu\nu}[h]$. (Sim T3a checks the proportionality identity numerically for random fields and momenta.)

So the substrate does not have to *construct* Fierz–Pauli (the failed programme of kappa §6.7.3); it has to supply the **premises** — rank-2 collective field (§4), two-derivative quadratic effective action (§4), gauge invariance (§5) — and uniqueness does the rest. The dynamics of $h$ is the only one it could have been.

---

## 7. Step E/F — Source coupling, trace reversal, and the factor 2 as theorems

**Proposition E.1 (conservation is forced; coupling is consistent).** Adding the matter coupling $S_{\rm int} = \lambda\int h_{\mu\nu}\,\Theta^{\mu\nu}$, gauge invariance of the total action requires $\int \xi_\nu\,\partial_\mu\Theta^{\mu\nu} = 0$ for all $\xi$, i.e. **the source must be a conserved symmetric tensor** — which $\Theta_{\mu\nu}$ is, by Theorem A.1. Conversely, the only Lorentz-covariant conserved symmetric rank-2 current of the substrate matter sector is $\Theta_{\mu\nu}$ up to improvement terms, so the coupling is unique up to normalisation.

**Proposition E.2 (universality = equivalence principle).** All foreground matter is σ-paired substrate modes of the one field $F$, rendered through the same chart and the same kernel (I2, I4). There is therefore one coupling constant $\lambda$ for everything — no per-species gravitational charge exists in the substrate, because there is only one substrate. Inertial and gravitational mass agree quantitatively in sim T12 (§11).

**Theorem F.1 (trace-reversed field equation; discharges (H-trace) and Obstacle 3).** The stationary point of $S_{FP} + S_{\rm int}$ in harmonic (de Donder) gauge is
$$\Box\,\bar h_{\mu\nu} \;=\; -\frac{16\pi G}{c^4}\,\Theta_{\mu\nu}, \qquad \bar h_{\mu\nu} = h_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu}h,$$
with the normalisation $16\pi G/c^4$ **fixed by matching the Newtonian limit** already derived (I3): the static solution must reproduce $h_{00} = -2\Phi_\infty/c^2$ with $\nabla^2\Phi_\infty = 4\pi G\rho_m$. The trace reversal is generated by the variation of the Fierz–Pauli kinetic term (Corollary D.2) — it is kinematics of the unique action, not a property of the matter coupling. Equation (5.4) of `kappa-derivation-math.md` is hereby **derived**; the factor 2 of (5.1), and the full isotropic form (5.5)
$$h_{\mu\nu} = -\frac{2\Phi_\infty}{c^2}\,\delta_{\mu\nu}$$
follow by the Green-function computation already written out in kappa §6 — now unconditional. (Sim T3 solves the field equation on a 3-D grid with a dust blob and confirms $h_{00} = h_{11} = h_{22} = h_{33} = 2GM/(rc^2)$, $h_{0i} = 0$, against the analytic profile.)

**Corollary F.2 (Theorem 6.1 upgraded).** The Schwarzschild compactness $\kappa(r) = 2GM/(rc^2)$ holds with no remaining hypotheses beyond Definition 4.2 ($G$ calibration) and the §13 residuals — including the **spatial** components $g_{ij}$ at $O(\kappa)$, which the Nordström fallback of kappa §6.7.5 could not deliver.

**Corollary F.3 (light bending, the discriminator).** Null rays in the derived weak-field metric deflect by $\alpha = 4GM/(bc^2)$ — twice the Newtonian-corpuscle value, the classic 1919 test — *because* $h_{ij} \neq 0$. A scalar-gravity substrate ($h_{00}$ only) gives half; a conformally-coupled scalar gives zero. (Sim T4 integrates rays through the *numerically solved* metric of T3 and recovers $4GM/(bc^2)$, and through the scalar-only metric and recovers half.)

---

## 8. Step G — Nonlinear completion: Einstein's equations

**Theorem G.1 (conditional on classical bootstrap).** A massless spin-2 field with gauge-invariant quadratic action, coupled universally to the total stress-energy — *including its own* — has a unique consistent nonlinear completion: the Einstein–Hilbert action, hence the full field equations
$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu},$$
with $\Lambda$ the single undetermined constant of the completion. This is the Gupta–Kraichnan–Feynman–Deser bootstrap (Gupta 1954; Kraichnan 1955; Feynman 1962/1995 lectures; **Deser 1970**, which closes the iteration in one step in first-order form; uniqueness per Wald 1986; see also Boulware–Deser 1975). The substrate's role is to supply the premises, all derived above: massless spin-2 (§4–§6), universal coupling to conserved $T_{\mu\nu}$ (§7, Prop E.2), and the self-coupling requirement (gravitational energy is energy: $\Theta_{00} \geq 0$ applies to the $h$-sector's own collective energy on the same footing, by Prop E.2's one-substrate argument).

**Remark G.2 (the cosmological constant).** The bootstrap *permits* $\Lambda$ and cannot fix it — and the substrate programme fixes it elsewhere: the closure-budget/σ-paired complement determination in `hypersphere-cosmology` v1.1 reproduces $\Omega_\Lambda = 0.6844$ (−0.083% vs Planck). The one constant the gravity chain leaves free is exactly the one the cosmology chain determines. The two chains are independent, which makes the agreement a consilience check rather than a fit.

**Remark G.3 (relation to the D₄/cascade route).** `papers/cascade-derivation/cascade-gr.md` phases C2–C7 pursue the same target by continuum limit of the 24-cell rung. The bootstrap route closes the field-equation question first; the cascade route remains valuable as the *geometric* (rather than effective-field-theoretic) derivation and as the rigorous home for the continuum-limit residual (R-cont) of §13. The two are complementary, not competing.

---

## 9. Consequences and checks

### 9.1 (H-wave), final formality
$\frac{F_{t+1} - 2F_t + F_{t-1}}{\tau^2} = \partial_t^2 F + \frac{\tau^2}{12}\partial_t^4 F + O(\tau^4)$ by Taylor expansion; combined with $L/a^2 \to -\nabla^2$ this gives $\Box$ with $c = a/\tau$. The leapfrog substrate dynamics reproduces each 600-cell eigenmode's continuum frequency with $O(\tau^2)$ convergence (sim T10). **(H-wave) is now fully discharged.**

### 9.2 Gravitational waves
In TT gauge the derived field equation gives $\Box h_{\mu\nu}^{TT} = 0$: two polarisations (Theorem D.1), dispersion $\omega = c|k|$ exactly (sim T9), and — because gravity and matter ride the *same* substrate wave operator (I1) — the GW speed equals the matter-wave/light speed identically, consistent with GW170817's $|c_{GW}/c - 1| < 10^{-15}$ as a structural fact rather than a coincidence.

### 9.3 Time dilation
$g_{00} = -(1 - 2GM/(rc^2))$ is Corollary F.2; the rate of the inner clock (the pentagonal tick) at depth $\Phi$ scales as $\sqrt{-g_{00}}$, recovering gravitational time dilation with the time direction = the real-quaternion clock axis, as in `narrative-gap-closure.md` G8.

### 9.4 Geodesic motion
$\partial_\mu T^{\mu\nu} = 0$ in the curved background implies wavepacket worldlines are geodesics of $g = \eta + h$ at leading order (the standard conservation→geodesic argument; eikonal version checked implicitly by T4's null rays, which follow the metric, not the potential).

---

## 10. What this closes in earlier documents

| Item | Old status | New status |
|---|---|---|
| (H-wave) | justification closed, algebra step open | **closed** (§9.1, T10) |
| (H-tensor) | ansatz (5.5) postulated | **reduced to Def. B.1 + forced dynamics**; (5.5) now derived (Thm F.1) |
| (H-stress) | construction TBD | **closed** (Thm A.1: canonical Noether tensor; T5–T7) |
| (H-trace) | factor 16π & trace reversal by hand | **closed** (Thm F.1: theorem of the unique action) |
| Obstacle 1 (quartic-in-h) | load-bearing, unsolved | **dissolved** (§3: bilinear = source; §4: effective action quadratic) |
| Obstacle 2 (Nordström fallback) | fallback for $g_{00}$ only | **retired** (full $h_{ij}$ derived; light bending ×2, T4) |
| Obstacle 3 (trace-reversed source) | open | **closed** (trace reversal lives in the kinetic term, §7) |
| Conjecture 6.6.1 | open | **superseded**: FP obtained by uniqueness, not by icosian bilinear construction |
| Theorem 6.1 (Schwarzschild κ) | conditional on 4 hypotheses | **unconditional** modulo Def. 4.2 + §13 residuals (Cor. F.2) |
| Full Einstein equations | not derived | **derived** modulo classical bootstrap + §13 residuals (Thm G.1) |

---

## 11. The QM bridge: one field, two faces

The same substrate field $F$ that sources gravity *is* the quantum sector at the fine rung. The bridge is the massive end of the response family (I5):

**Proposition Q.1 (envelope → Schrödinger).** A substrate mode at the massive end of $C_\varphi$ obeys the Klein–Gordon-type equation $\partial_t^2 F = c^2(\nabla^2 - \mu^2)F$ with $\mu = \varphi^{-1}$. Writing $F = \mathrm{Re}[\psi\, e^{-i\omega_0 t}\,\hat q]$ with rest carrier $\omega_0 = c\mu$ and slowly varying envelope $\psi$, the wave equation reduces to
$$i\,\partial_t \psi \;=\; -\frac{c^2}{2\omega_0}\,\nabla^2\psi \;+\; O(\epsilon^2), \qquad \epsilon = \frac{c\,k_{\rm env}}{\omega_0},$$
i.e. the free Schrödinger equation with mass $m = \hbar\omega_0/c^2$. (Sim T11: lattice Klein–Gordon vs Schrödinger envelope, error $O(\epsilon^2)$ verified by halving $\epsilon$.) This complements Paper XVIII's Nelson-pairing route (which handles the interacting/equilibrium structure); the envelope route is the direct free-sector reduction.

**Theorem Q.2 (equivalence principle, quantitative).** For the same wavepacket: (i) the inertial mass read off its Schrödinger dispersion (spreading rate) is $m = \hbar\omega_0/c^2$; (ii) the gravitating mass read off its stress tensor is $Mc^2 = \int \Theta_{00} = \hbar\omega_0 \times (\text{quanta})$. They agree identically because both are moments of the *same* field — there are not two masses to differ. (Sim T12 measures both on one simulated packet and confirms agreement to $O(\epsilon^2)$.)

**Rung sampling.** The QM↔GR resolution bridge is the already-proven sampling theorem (coarse-rung eigenfunctions = fine-rung eigenfunctions sampled on shared vertices; 24-cell ⊂ 600-cell, `cascade-gr.md` C1, `the-24-600-spectral-bridge`): quantum mechanics and gravity are the same substrate read at two grains, and §8 plus Paper XVIII are the two grains' effective laws.

---

## 12. The Standard-Model bridge: same mechanism, one rank down — and the honest open list

**Proposition S.1 (Maxwell forced).** Run the §6 uniqueness scan for a rank-1 collective field $A_\mu$ with the chart-phase redundancy $A_\mu \to A_\mu + \partial_\mu\chi$: the general 3-parameter quadratic action $a_1\partial_\mu A_\nu\partial^\mu A^\nu + a_2(\partial_\mu A^\mu)^2 + b\,A_\mu A^\mu$ collapses to the 1-dimensional null space $(a_1, a_2, b) \propto (1, -1, 0)$ — the Maxwell action $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$ — with 2 photon polarisations and conserved charge forced exactly as in Prop E.1. (Sims T13a–c.)

So the *form* of both long-range force laws — Maxwell and Einstein — is forced by one theorem applied at rank 1 and rank 2, with the substrate supplying the field content and the redundancies. What the substrate has **not yet** supplied for the Standard Model, stated plainly:

- the non-abelian gauge **group content** (why $SU(3)\times SU(2)\times U(1)$) — open; the natural candidate direction is the icosian/quaternionic automorphism structure, not yet derived;
- the **heavy sector** (W/Z/Higgs masses, heavy quarks) and neutrino placement — open, as the book's Chapter 12 already records;
- what exists today as contact points: the mass-ladder placements of the light sector, the b-anomaly response-family shape (kappa §4.6 — the same $C_\varphi$ family whose two ends are Newton and Yukawa), and the conditional α-chain.

This section is the honest boundary of the bridge: form forced, content partially open.

---

## 13. Named residuals (what "closed" does and does not mean)

1. **(R-cont) Continuum-limit rigor.** The chain operates at effective-field-theory level: discrete substrate → rendered smooth fields via the kernel, with the exact dispersion relation and $O(\tau^2)$/$O(a^2)$ convergence checks as witnesses. A fully rigorous discrete→continuum theorem (Gromov–Hausdorff style) is the cascade-gr C2 programme. Open, and now the *only* mathematically deep gap in the gravity chain.
2. **(R-Gauss) Gaussian regime.** Proposition B.3 proves quadratic dominance of $\Gamma[h]$ for Gaussian substrate fluctuations. Strong-field/strongly-coupled substrate regimes are not covered (physically: the deep-nonlinear regime near horizons is taken over by the bootstrap's nonlinear completion, but the substrate-side statement is Gaussian).
3. **(R-boot) Classical citations.** Theorem G.1 cites the bootstrap (Deser 1970 etc.) rather than re-deriving it; the cited results are mainstream and unconditional, but they are imported, not substrate-internal.
4. **(R-G) Calibration.** $G$ remains the substrate↔physical mass conversion of Definition 4.2 (calibration, not derivation), as before.
5. **(R-Λ)** $\Lambda$ is not fixed by this chain; it is fixed by the cosmology wing (Remark G.2).

None of these is of the "missing mechanism" kind that Obstacles 1–3 were; they are rigor-grade and calibration-grade residuals, plus two classical imports.

---

## 14. Simulation manifest (`scripts/verify_gr_closure.py`)

| Sim | Verifies | Section |
|---|---|---|
| T1 | FP uniqueness: 6-param scan → 1-dim null space, ratios $(-\tfrac12,1,-1,\tfrac12)$, masses killed | D.1 |
| T2 | Polarisation count: $\dim\ker K(k_{\rm null}) = 6 \supset$ 4-dim gauge orbit ⇒ 2 physical | D.1 |
| T3a | $\delta S_{FP}/\delta h$ = linearised Einstein tensor (random-input identity) | D.2 |
| T3 | Grid solve, dust blob: $h_{00}=h_{ii}=2GM/rc^2$, $h_{0i}=0$ (factor 2 + isotropy) | F.1 |
| T4 | Ray tracing: deflection $4GM/(bc^2)$; scalar-only control gives half | F.3 |
| T5 | Exact tick-energy conservation of leapfrog substrate dynamics on the 600-cell | A.2a |
| T6 | Exact local continuity $\dot e_v + \sum J_{vw} = 0$ on the 600-cell graph | A.2b |
| T7 | $\Theta_{\mu\nu}$: symmetry, on-shell conservation $O(dx^2)$, dust limit, $\Theta_{00}\ge0$ | A.1, A.3 |
| T8 | Chart redescription shifts $h$ by $\partial_\mu\xi_\nu + \partial_\nu\xi_\mu$ (numeric re-charting) | C.1 |
| T9 | TT waves: $K(k)h_{TT} = 0$ iff $\omega = c|k|$ | 9.2 |
| T10 | Second-difference → $\partial_t^2$ at $O(\tau^2)$; leapfrog eigenmode frequency convergence | 9.1 |
| T11 | Klein–Gordon envelope → Schrödinger, error $O(\epsilon^2)$ | Q.1 |
| T12 | Inertial mass (spreading) = gravitating mass ($\int\Theta_{00}$) on one packet | Q.2 |
| T13 | Maxwell uniqueness, photon 2 polarisations, charge conservation forced | S.1 |
| T14 | Substrate rank-2 equivariance of coarse bilinear under $2I\times 2I$ (on $V_{600}$) | B.2 |
| T15 | Wishart effective action: quadratic dominance, cubic/quadratic $\sim N^{-1/2}$ | B.3 |

## 15. Cross-references

- `docs/kappa-derivation-math.md` — Newton tier, conditional Schwarzschild, the obstacles closed here.
- `docs/rendering-layer.md` — arena, kernel, chart, inner clock reversal (inputs I1, I2).
- `docs/narrative-gap-closure.md` — G8 (now closable: the 1+3 split feeds Thm F.1's rest-frame structure).
- `papers/cascade-derivation/cascade-gr.md` — D₄ geometric route; home of residual (R-cont).
- `papers/paper-xviii/` — Nelson pairing (interacting QM face); complements Prop Q.1.
- `papers/paper-xxiv/` — event-order kinematics (simultaneity/time-dilation precursors).
- `hypersphere-cosmology` v1.1 — independent determination of Λ (Remark G.2).
