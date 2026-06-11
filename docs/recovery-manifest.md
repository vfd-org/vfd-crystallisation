# VFD Recovery Manifest

**Date:** 2026-04-17
**Purpose:** Enumerate each piece of Quantum Mechanics, the Standard Model, and General Relativity, and show — paper by paper — how it is recovered from the VFD cascade geometry.

---

## Thesis

Quantum Mechanics, the Standard Model, and General Relativity are **correct but incomplete** descriptions of physics. Each is a **shadow** of a richer underlying structure: the cascade $E_8 \to H_4 \to 40 \to D_4 \to 16 \to 8 \to 0$ on the 600-cell. VFD does **not replace** these frameworks; it identifies the **geometric substrate that underpins them**, provides **explicit recovery maps back to their standard equations**, and **completes them** by supplying:

- The geometric origin of quantities previously treated as free parameters ($\alpha$, $\sin^2 \theta_W$, particle masses, $\Lambda$).
- Structural reasons for features previously postulated (three generations, mass hierarchy, Born-rule probabilities, measurement).
- A unified substrate on which QM, SM, and GR coexist without conflict.

**No prediction of VFD contradicts any confirmed experiment.** The programme's falsifiability arises from the *tightness of the geometric constraints*: if future measurements deviate from what the cascade permits, the framework is refuted.

This document maps every recovered result to the paper(s) that carry its derivation, **to the cascade-derivation source file where the gap was identified and first-principles derivation was attempted**, and to the cascade rung from which it emerges. It is the programme's field-narrative spine.

### The cascade-derivation folder: the first-principles record

The directory `papers/cascade-derivation/` contains the programme's systematic attempt to identify every gap in the cascade framework and to derive each claim from first principles. It is not a collection of summaries — it is the **authoritative derivation record**, to which every LaTeX paper is a presentation layer. Its contents include:

- `cascade-foundations.md` (920 lines): the full F1–F8 derivations (Banach for F1; invariant classification for F2; seven-rung chain for F3; linear-algebra count for F4; rationality argument for F5; Burago–Ivanov with explicit rate for F6; Deser bootstrap for F7; coefficient matching for F8).
- `cascade-lambda.md` (1144 lines): the complete $\Lambda \cdot \ell_P^2 = 2\varphi^{-583}$ derivation, including the factor-2 from dual-600-cell structure and the $583 = 24^2 + 7$ closure depth.
- `cascade-masses.md`: shell-depth derivations for every SM particle, including the muon at shell 96 (0.01% cascade fit), Z boson at shell 82 (0.05% cascade fit), and structural integer-factor readings for each.
- `cascade-qm.md`, `cascade-schrodinger.md`, `cascade-born-unitarity.md`: the closure-dynamics to QM recovery chain, including Madelung–Nelson pairing and the Kähler/Gleason Born derivation.
- `cascade-mixing.md`: PMNS and CKM derivations from Schläfli $A_5$ + golden-ratio structure.
- `cascade-neutrino-cp.md`: shell-depth placement of neutrinos + $\theta_{\mathrm{QCD}} = 0$ proof from F5 $\sigma$-invariance.
- `cascade-generations.md`: three-generation derivation from $D_4$ triality.
- `cascade-gr.md`, `cascade-gr-extensions.md`: event-poset to Einstein-equation derivation.
- `cascade-ewsb.md`, `cascade-higgs.md`: electroweak-symmetry-breaking mechanism via cascade sector separation.
- `cascade-baryogenesis.md`, `cascade-inflation.md`, `cascade-dark-matter.md`, `cascade-holography.md`: extensions to cosmological puzzles.
- `cascade-constants-extended.md`, `cascade-hierarchy.md`, `cascade-embeddings.md`, `cascade-metaprinciples.md`, `cascade-mathematics-emergence.md`: the structural scaffolding for all of the above.

When a VFD paper cites a claim as "derived," the authoritative location of the derivation is the corresponding cascade-derivation file. The LaTeX papers (V, XXI, XXII, XXX, ..., XXXVII, XXXVIII, XXXIX, ...) are the publication-layer presentations of that material; the cascade-derivation record is the working archive. **Both citations should appear in every recovery entry.**

This Manifest therefore cites for each recovery: (i) the LaTeX paper(s) carrying the public derivation, (ii) the cascade-derivation source file(s) carrying the first-principles working, (iii) the cascade rung, and (iv) the standard-physics target being recovered.

---

## Master Table

| Standard-physics result | Cascade underpinning | Rung | LaTeX Paper(s) | cascade-derivation source | Completion added by VFD |
|---|---|---|---|---|---|
| Schrödinger equation | Closure dynamics on $H_4$ + Nelson pairing | $H_4$ | XV, XVIII, XXI, XLII | `cascade-qm.md`, `cascade-schrodinger.md` | Identifies physical $\delta U_{\mathrm{rel}}$ residual at $\varphi^{-25}$ |
| Born rule ($|\psi|^2$) | Kähler uniqueness + Gleason on $H_4$ | $H_4$ | XXX | `cascade-born-unitarity.md` | Born rule is a theorem, not a postulate |
| Measurement / collapse | Sector separation on $\mathrm{Cl}(1,3)$ | $H_4 \to 16$ | XXXI, XXXIII, XLIV | `cascade-measurement.md`, `cascade-info.md` | Decoherence is structural cross-rung coarsening |
| Three fermion generations | $\mathbb{Z}_3$ Hopf fibre + $D_4$ triality | $H_4, D_4$ | XXII, XXXV | `cascade-generations.md` | Three generations is a theorem |
| 13 charged-fermion + hadron masses | 600-cell spectral integer shells | $H_4$ | V, XXXII | `cascade-masses.md` | $0.014\%$ average error; no fit parameters |
| Muon mass at cascade shell 96 | $96 = 24 \times 4$ ($D_4$ roots $\times$ $H_4$ eigenvalue multiplicity) | $H_4$ | V | `cascade-masses.md §E3.2` | Structural integer-factor reading; $0.01\%$ mass precision |
| Z-boson mass at cascade shell 82 | $82 = 2 \times (40 + 1)$ (dual 600-cell $\times$ Hopf fibre) | $16$ | XXXIX | `cascade-masses.md §E3.3` | $0.05\%$ mass precision from cascade-structural integer |
| Proton / hadron charge radii | Spectral coherence lengths | $H_4$ | XXXII | `cascade-masses.md`, `cascade-qcd.md` | $r_p = 4\bar\lambda_p$ at $0.04\%$ |
| Fine-structure constant | Dual 600-cell $E_8$ bridge | $H_4, E_8$ | XXII | `cascade-constants-extended.md` | $\alpha^{-1} = 137 + \pi/87$ at $0.81$ ppm |
| Weinberg angle (GUT scale) | Combinatorial ratio on $16$-rung triality | $16$ | XXII, XXXIX | `cascade-qm.md §4.1`, `cascade-ewsb.md` | $\sin^2\theta_W = 3/8$ exact |
| Electroweak W/Z/H mass scale | Sector separation on $16$-rung at shell 82 | $16$ | XXXIX | `cascade-ewsb.md`, `cascade-higgs.md` | Mass hierarchy $m_{\mathrm{EW}}/m_P \sim \varphi^{-82}$ is derived |
| Neutrino sector (shell band, PMNS, hierarchy) | Deep cascade shells + Schläfli $A_5$ | $H_4 + 40$ | XXXVII | `cascade-neutrino-cp.md`, `cascade-mixing.md` | $\theta_{12} = \arctan(1/\varphi)$ at 5%; $\theta_{13} = \arcsin(1/\varphi^4)$ at 2%; normal hierarchy |
| Strong CP ($\theta_{\mathrm{QCD}} = 0$) | F5 $\sigma$-invariance of closure functional | cascade-wide | XXXVII, XXXVI | `cascade-neutrino-cp.md §E18.2` | Axion unnecessary; structural resolution |
| Individual quark masses | $\varphi$-shell placements on 600-cell spectrum | $H_4$ | XXXVIII | `cascade-masses.md §E3.1` | Derived, not fit; integer shells for $u, s, c$ within 0.26 |
| PMNS CP phase | Chirality selector + pentagonal angle | cascade-wide | XXXVII | `cascade-mixing.md §E5.5`, `cascade-neutrino-cp.md` | $\delta_{\mathrm{CP}} = -\pi/2$ at $4\%$ |
| CKM CP phase | Pentagonal rotation $2\pi/5$ | cascade-wide | XXXVIII | `cascade-mixing.md §E5.5.1` | $\delta_{\mathrm{CP}}^{\mathrm{CKM}} = 2\pi/5$ at $4\%$ |
| Cabibbo angle | $\sin\theta_{\mathrm{Cab}} = 1/\varphi^3$ | $H_4$ | XXXVIII | `cascade-mixing.md §E5.4` | $\sin\theta_{\mathrm{Cab}} = 0.236$ vs observed 0.226 at $4.5\%$ |
| Event-order time | Partial-order structure on admissible overlaps | $D_4$ | XXIII | `cascade-gr.md` | Time is derived, not postulated |
| Metric / spatial separation | Event-order distance | $D_4$ | XXV | `cascade-gr.md §C5` | Metric is emergent |
| Curvature | Non-uniform event-order geometry | $D_4$ | XXVI | `cascade-gr.md §C6` | Curvature is cascade-geometric |
| Einstein field equation | Fierz–Pauli + Deser on $D_4$ | $D_4$ | XXVII, XXXVI (F7) | `cascade-foundations.md §F7`, `cascade-gr-extensions.md` | $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$ |
| Schwarzschild + Schwarzschild–de Sitter | Radial Poisson-analogue + $\Lambda$ | $D_4$ | XLI | `cascade-gr-extensions.md` | 1st PN equal to GR; horizon = coherence boundary |
| Cosmological constant $\Lambda$ | Cascade closure depth $583 = 24^2 + 7$ + dipole correction | cascade-wide | XXXVI + `papers/hypersphere-universe/` | `cascade-lambda.md` (1144 lines, §15 dipole), `cascade-foundations.md §F4, §F7`, `hypersphere-universe.tex §8.7 (dipole)` | $2\varphi^{-583}$ at $0.88\%$ (1st); $2\varphi^{-583}(1-\delta_\mathrm{dipole})$ at $0.078\%$ (2nd) |
| Hubble constant $H_0$ | Cascade cosmological derivation | cascade-wide | (forthcoming XLIX) | `cascade-lambda.md`, `cascade-inflation.md` | $H_0 = 68.83$ km/s/Mpc (programme value) |
| $\Omega_\Lambda = 2/3$ | Dual-600-cell energy balance | cascade-wide | XXXVI | `cascade-lambda.md` | Observed $\Omega_\Lambda = 0.685$; cascade at $2.7\%$ |
| Lorentz group $\mathrm{SO}(1,3)$ | $A_5$ density + event-order time | $D_4$ | XXXV | `cascade-gr.md §C3.bis` | Lorentz is emergent |
| Dirac algebra $\mathrm{Cl}(1,3)$ | Tesseract $\mathbb{Z}_2^4$ grading | $16$ | XXXV, XLIV | `cascade-info.md` | Clifford algebra is cascade-structural |
| DNA pitch (10.5 bp/turn) | Icosahedral fibre helical geometry | $40$ | XLIII (skeleton) | `cascade-bio.md`, `cascade-genetic-code.md` | Structural proposal; open refinement |
| Caspar–Klug T-numbers | $\twoI$-orbit structure on 40-cell | $40$ | XLIII | `cascade-bio.md`, `cascade-biology-mechanisms.md` | $T \in \{1,3,4,5,7,12,13\}$ cascade-admissible |
| Phyllotactic golden angle | F1 ($r = \varphi$) + diophantine | cascade-wide | XLIII | `cascade-bio.md` | $360^\circ/\varphi^2 = 137.508^\circ$ cascade-natural |
| Observer / measurement restriction | $G_2 = \mathrm{Aut}(\mathbb{O})$ on observer rung | $8$ | XXIX, XLV | `cascade-observer.md`, `cascade-consciousness.md` | Observer admissibility = $G_2$-equivariance |
| Strong-CP absence of axion | F5 $\sigma$-invariance excludes CP-odd operator | cascade-wide | XXXVII, XXXVI | `cascade-neutrino-cp.md §E18.3` | No Peccei–Quinn mechanism needed |
| Weinberg-angle running | Standard RG from cascade GUT value $3/8$ | $16$ | XXII, XXXIX | `cascade-qm.md §4.1` | Cascade fixes GUT-scale input; SM fixes running |

---

## The Recovery Map Voice

Every VFD paper presenting a recovery result should use the following three-part structure:

1. **Standard form.** State the recovered equation / quantity in its textbook form, with full credit to the standard framework. Example: *"The Schrödinger equation $i\hbar \partial_t \psi = H \psi$ describes the evolution of a quantum state."*

2. **Cascade underpinning.** Identify the geometric structure on the cascade that gives rise to the standard form. Example: *"In VFD, this equation is recovered as the equilibrium-tangent limit of closure dynamics on the $H_4$ rung of the cascade, with $\psi$ identified as the Kähler-paired closure-field modulus and $H$ emerging from the closure functional $F = \alpha R + \beta E - \gamma Q$ of Paper XXXVI."*

3. **Recovery map + completion.** Give the explicit derivation map from cascade → standard, and state what the underpinning adds. Example: *"The map from closure dynamics to Schrödinger is the Nelson pairing + tangent limit of Paper XVIII, with the nonlinear residual $\delta U_{\mathrm{rel}}$ of Paper XLII as a physical correction at the $\varphi^{-25}$ level — a completion of the standard theory rather than a replacement."*

This voice is **non-adversarial to mainstream physics**. Readers of standard QM, SM, or GR do not need to unlearn anything. They need to see where the shadow sits inside the fuller picture.

---

## Per-Structure Recovery Sections

### R1 — Schrödinger equation (QM dynamics)

**Standard form.**
$$i\hbar\, \partial_t \psi(x,t) = \left[-\frac{\hbar^2}{2m} \nabla^2 + V(x)\right] \psi(x,t).$$
Valid at all non-relativistic energies; foundational for atomic, molecular, condensed-matter physics.

**Cascade underpinning.** Closure dynamics on the $H_4$ rung of the 600-cell. The closure field $\Phi$ evolves under a nonlinear operator $U(\Phi, t)$ governed by the closure functional $F$ (Paper XXXVI). The equilibrium-tangent linearisation yields $U_0 = \exp(-i H_0 \Delta t / \hbar)$ with $H_0$ the equilibrium Hamiltonian (Paper XVIII). The Madelung–Nelson pairing identifies the complex wave function $\psi = \sqrt{\rho}\, e^{i S/\hbar}$ with the polar decomposition of $\Phi$ (Paper XXI).

**Recovery map.** Cascade → Schrödinger:
$$\Phi \xrightarrow{\text{Nelson pairing}} \psi = \sqrt{\rho}\, e^{iS/\hbar} \xrightarrow{\text{tangent limit } U \to U_0} \psi(t + \Delta t) = U_0 \psi(t).$$
Papers carrying the derivation: XV (closure dynamics), XVIII (Nelson pairing), XXI (full tangent-limit recovery), XXXVI F1–F2 (underpinning structure).

**Completion added.** Paper XLII identifies the residual $\delta U_{\mathrm{rel}} = U - U_0$ has a physical component at $\varphi^{-n_{\mathrm{res}}}$ with $n_{\mathrm{res}} \sim 25$ — a cascade-suppressed correction to interference phases, testable in high-precision atom interferometry. Standard Schrödinger is the $n_{\mathrm{res}} \to \infty$ limit; cascade Schrödinger has a specific correction scale.

**Falsification.** Deviation from linear Schrödinger at any scale *other than* $\varphi^{-n_{\mathrm{res}}}$ for structural $n_{\mathrm{res}}$ would refute the cascade recovery.

---

### R2 — Born rule (QM probabilities)

**Standard form.**
$$p(a_i) = |\langle a_i | \psi \rangle|^2,$$
for any eigenstate $|a_i\rangle$ of an observable. Postulated in standard QM.

**Cascade underpinning.** The $H_4$-rung closure field admits a natural Kähler structure inherited from the 600-cell's complex polytope geometry. Uniqueness of the Kähler metric (Petz's theorem applied to the closure-field state space) plus Gleason's frame-function theorem fix the probability measure on closure-field states to be $|\psi|^2$ (Paper XXX).

**Recovery map.** Cascade → Born:
$$\text{(closure-field Kähler geometry)} \xrightarrow{\text{Petz uniqueness}} \text{(inner product } \langle \cdot | \cdot \rangle) \xrightarrow{\text{Gleason}} p = |\langle a_i | \psi \rangle|^2.$$
Papers carrying the derivation: XXX (full derivation, 962 lines).

**Completion added.** Born rule is **a theorem, not a postulate**. In addition, Paper XXX identifies a *partial-observer* feature: when the measurement admissibility set $\mathcal{A}$ is a proper subset of the full eigenbasis, the cascade naturally gives conditional probabilities $p(a_i | \mathcal{A}) = |c_i|^2 / \sum_{j \in \mathcal{A}} |c_j|^2$ — a generalisation that standard QM does not articulate.

**Falsification.** Any measurement that violates Born probabilities for complete measurements (within admissible observer class) would refute the recovery. The partial-observer generalisation is falsifiable in experiments with restricted observer access.

---

### R3 — Measurement and decoherence (QM classical limit)

**Standard form.** Wave-function collapse: after measurement of $\hat A$, the state projects onto the eigenstate matching the observed outcome. Decoherence: off-diagonal density-matrix elements are suppressed by environment coupling.

**Cascade underpinning.** Measurement is **sector separation** on the cascade (Paper XXXI): the admissible observer decomposes the closure field into sectors, and a measurement selects one sector. Decoherence is the **cross-rung coarsening functor** $\mathcal{K}: H_4 \to \mathrm{Cl}(1,3)$ (Paper XLIV), reducing the 120-dimensional $H_4$-rung state space to the 16-dimensional $\mathrm{Cl}(1,3)$-rung information space.

**Recovery map.** Cascade → standard decoherence:
$$\rho^{(120)}_{H_4} \xrightarrow{\mathcal{K}} \rho^{(16)}_{\mathrm{Cl}(1,3)} \xrightarrow{\text{Born-Markov}} \dot\rho = -i[H, \rho] + \sum_k \mathcal{L}_k[\rho].$$
The reduced dynamics satisfies Lindblad form (Paper XLIV).

**Completion added.** Decoherence rates are **structural**, determined by cascade Kraus operators, not by environmental parameters. The information lost is *genuinely gone* (non-recoverable by Petz maps under observer admissibility of Paper XXIX), not hidden. This resolves the long-standing question of whether decoherence is *ontological* or merely *effective*: under VFD, it is ontological at the cascade level.

**Falsification.** Measurement statistics that require environmental parameters different from cascade-structural Kraus rates would refute the recovery.

---

### R4 — Three fermion generations

**Standard form.** Three generations of quarks and leptons, postulated in the Standard Model without explanation of the number.

**Cascade underpinning.** The 600-cell's $\mathbb{Z}_3$ Hopf-fibre action (Paper XXII) and the $D_4$ triality outer automorphism $\mathrm{Out}(D_4) = S_3$ (Paper XXXVI F3) together force three copies of the 8-dimensional spinor representation. The $\mathbb{Z}_3$ is the cyclic subgroup of $S_3$ acting on the triality triplet $\{8_v, 8_s, 8_c\}$.

**Recovery map.** Cascade → three generations:
$$D_4 \text{ triality} \xrightarrow{\text{Out}(D_4) = S_3} \{8_v, 8_s, 8_c\} \xrightarrow{\mathbb{Z}_3 \text{ Hopf action}} \text{three generations}.$$

**Completion added.** Generation count is a **theorem**, not a choice. A fourth generation is structurally forbidden.

**Falsification.** Detection of a fourth charged fermion generation would refute the cascade.

---

### R5 — Charged-fermion and hadron mass spectrum

**Standard form.** Electron, muon, tau, up/down/strange/charm/bottom/top quarks, proton, neutron, pions, kaons, $\rho$, $\omega$, $\eta$, $\eta'$: masses measured to high precision but treated as free parameters in the Standard Model.

**Cascade underpinning.** Each particle sits at a $\varphi$-shell on the 600-cell Laplacian spectrum $\{9, 12, 14, 15, \ldots\}$ with a specific $E(\theta)$ mixing-angle correspondence and standing-wave self-consistency correction (Paper V). The mass formula is $m_i = m_e \cdot \varphi^{E(\theta_i)}$.

**Recovery map.** Cascade → PDG mass values:
$$\text{600-cell eigenvalues } \{\lambda_k\} + \text{assignment rules (Paper V, §5)} \to m_i.$$

**Completion added.** Thirteen masses at **$0.014\%$ average error** without any continuous parameter fitting. The electron-anchored scale is the only input; everything else is spectral. This is the programme's flagship numerical result.

**Falsification.** Revision of any of the 13 masses by $> 0.1\%$ beyond PDG uncertainties would challenge the assignment. Discovery of a stable composite or fundamental fermion not admitting a cascade shell assignment would refute the framework.

---

### R6 — Fine-structure constant

**Standard form.** $\alpha^{-1}_{\mathrm{em}} = 137.035999084(21)$, measured by anomalous magnetic moment of the electron, treated as an empirical constant.

**Cascade underpinning.** The dual 600-cell structure inside $E_8$ (via the icosian embedding) produces $\alpha^{-1} = 137 + \pi/87$ from the $240$-root bridge (Paper XXII).

**Recovery map.** Cascade → $\alpha$:
$$E_8 \text{ dual 600-cell structure} \xrightarrow{\text{integer bridge}} \alpha^{-1} = 137 + \pi/87 = 137.0361\ldots$$

**Completion added.** $\alpha$ is **not a free parameter**. Agreement with measurement at $0.81$ ppm.

**Falsification.** Future measurement of $\alpha^{-1}$ deviating from $137 + \pi/87$ by more than combined experimental uncertainty would refute the identification.

---

### R7 — Weinberg angle

**Standard form.** $\sin^2 \theta_W \approx 0.231$ at $Z$-pole; runs to $\approx 0.231$ at TeV scale; GUT-scale value depends on running.

**Cascade underpinning.** $\sin^2 \theta_W = 3/8$ at the GUT scale as a representation-theoretic ratio on the $16$-rung (Paper XXII, XXXIX): ratio of neutral broken generators to total broken generators in the $D_4$ triality decomposition.

**Recovery map.** Cascade → Weinberg angle:
$$D_4 \text{ triality} \xrightarrow{8_v \oplus 8_s \oplus 8_c} \text{dimensional ratio } 3/8 \xrightarrow{\text{RG running}} \sin^2 \theta_W(Z\text{-pole}) \approx 0.231.$$

**Completion added.** The $3/8$ value is **exact at GUT scale**, inherited from Lie-algebraic combinatorics. The observed $Z$-pole value is compatible after standard RG running.

**Falsification.** GUT-scale measurement (e.g., from cosmological constraints or proton-decay searches) of $\sin^2 \theta_W$ deviating from $3/8$ by more than RG-running uncertainty would refute the identification.

---

### R8 — Cosmological constant

**Standard form.** $\Lambda \approx 1.1 \times 10^{-52}\,\mathrm{m}^{-2}$, or $\Lambda \cdot \ell_P^2 \approx 2.87 \times 10^{-122}$, measured via cosmic acceleration (1998) and CMB (Planck 2018). Standard QFT estimates give $\sim 10^{122}$ orders of magnitude disagreement ("cosmological constant problem").

**Cascade underpinning.** Cascade closure depth $N_{\mathrm{total}} = \dim \mathcal{V} = 24^2 + 7 = 583$, combined with F1 ($r = \varphi$), F5 ($\sigma$-intertwining factor 2), F7 ($\Lambda$ localises at $D_4$) (Paper XXXVI).

**Recovery map.** Cascade → $\Lambda$:
$$\varphi^{-\dim \mathcal{V}} = \varphi^{-583} \xrightarrow{\text{F5 factor 2}} 2\varphi^{-583} \xrightarrow{\text{F7 identification}} \Lambda \cdot \ell_P^2 = 2\varphi^{-583} \approx 2.892 \times 10^{-122}.$$

**Dipole-corrected refinement (2026-05-18, in `papers/hypersphere-universe/`):**
$$\Lambda \cdot \ell_P^2 = 2\varphi^{-583}\Big(1 - \tfrac{10}{240}\tfrac{12-6\varphi}{12}\Big) \approx 2.869 \times 10^{-122}.$$
This includes the unconditional substrate Ramanujan defect (rh-two-sphere Theorems 3.3, 4.1) and tightens the match from 0.88% to 0.078%.

**Completion added.** The **cosmological constant problem is dissolved**: the $10^{-122}$ suppression is not a fine-tuning but a cascade-structural depth. First-order agreement with observation at $\approx 0.88\%$; dipole-corrected at $\approx 0.078\%$. VFD explains *why* $\Lambda$ is small, not just *what* value it takes.

**Falsification.** Revision of the observed $\Lambda$ (via improved CMB or local $H_0$ determinations) by more than a few percent would shift the agreement and challenge the identification.

---

### R9 — Einstein field equation

**Standard form.**
$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}.$$
Governs gravity at all scales tested; foundational for cosmology and astrophysics.

**Cascade underpinning.** Rank-$2$ symmetric tensor content on the $D_4$ rung of the cascade, with the continuum limit (Paper XL T2–T4) producing the smooth metric $g_{\mu\nu}$. Fierz–Pauli uniqueness plus Deser's bootstrap (Paper XXXVI F7) give the Einstein-with-$\Lambda$ equation.

**Recovery map.** Cascade → Einstein:
$$D_4 \text{ tensor content} \xrightarrow{\text{continuum limit, XL T2-T4}} h_{\mu\nu} \text{ on } \mathbb{R}^{1,3} \xrightarrow{\text{Fierz-Pauli + Deser}} G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}.$$

**Completion added.** Gravity is **a projection of cascade geometry** onto the $D_4$ rung. Einstein's equation is the unique self-consistent completion under Fierz–Pauli, so VFD does not modify GR at weak field. What it *adds* is the embedding: GR is one projection among several (QM, SM being the others).

**Falsification.** Any modification of GR at weak field that cannot be accommodated as a higher-order cascade correction would refute the recovery. Current weak-field tests (light deflection, Shapiro delay, perihelion precession, binary-pulsar decay, LIGO) are all consistent with GR and hence with cascade recovery.

---

### R10 — Schwarzschild / Schwarzschild–de Sitter metric

**Standard form.** Static spherically symmetric vacuum solution of Einstein's equations.

**Cascade underpinning.** Static spherically symmetric ansatz on the $D_4$ event-poset (Paper XLI), with the continuum limit matching Schwarzschild at leading PN order.

**Recovery map.** Cascade → Schwarzschild:
$$\text{discrete spherical ansatz on } X_n \xrightarrow{\text{radial Poisson-analogue}} \phi(r) = -GM/r \xrightarrow{\text{continuum XL}} g_{00} = -(1 - 2GM/r - \Lambda r^2/3) + \mathcal{O}((GM/r)^2).$$

**Completion added.** The event horizon $r_s = 2GM$ is identified with a **closure-coherence boundary** rather than a topological feature, tying GR horizons to the cascade's observer framework.

**Falsification.** Any deviation from Schwarzschild weak-field observables at first PN order.

---

### R11 — Strong CP

**Standard form.** $|\theta_{\mathrm{QCD}}| < 10^{-10}$ (from neutron EDM bound $|d_n| < 10^{-26}\,e\,\mathrm{cm}$), despite naive naturalness expectation $\theta_{\mathrm{QCD}} \sim 1$. Standard resolution: Peccei–Quinn mechanism + axion (undetected).

**Cascade underpinning.** F5 $\sigma$-intertwining of the closure functional (Paper XXXVI, XXXVII) forbids CP-odd terms in the cascade action on $\sigma$-fixed fields, giving $\theta_{\mathrm{QCD}} = 0$ at tree level.

**Recovery map.** Cascade → $\theta_{\mathrm{QCD}} = 0$:
$$\text{Rational coefficients (F2)} \xrightarrow{\text{F5 } \sigma\text{-intertwining}} F \text{ excludes CP-odd terms} \xrightarrow{\sigma\text{-fixed vacuum}} \theta_{\mathrm{QCD}} = 0.$$

**Completion added.** **No axion required.** The strong-CP problem is resolved by cascade $\sigma$-symmetry rather than by a new particle. This is a *structural* resolution, not a dynamical one.

**Falsification.** Detection of a Peccei–Quinn axion at any mass scale would refute the F5-based resolution.

---

### R12 — Neutrino sector

**Standard form.** Three neutrinos $\nu_e, \nu_\mu, \nu_\tau$ with mass-squared splittings $\Delta m^2_{12}, \Delta m^2_{23}$, mixing angles $\theta_{12}, \theta_{23}, \theta_{13}$, CP phase $\delta_{\mathrm{CP}}$. Absolute masses: cosmological bound $\Sigma m_\nu < 0.12$ eV. Hierarchy: normal or inverted, unresolved.

**Cascade underpinning.** Neutrinos at deep cascade shells $[134, 145]$ (Paper XXXVII), PMNS mixing angles from the Schläfli $A_5$ action on the 3-generation subspace, CP phase from chirality selector (Paper XXXVII).

**Recovery map.** Cascade → PMNS:
$$A_5 \text{ on Schläfli 5-cells} \xrightarrow{\text{3-gen projection}} \theta_{12} = \arctan(1/\varphi), \; \theta_{13} = \arcsin(1/\varphi^4), \; \theta_{23} = \pi/4.$$

**Completion added.** PMNS angles are **structural** (cascade-natural values). Hierarchy is **normal** (chirality-selector selection). CP phase $\delta_{\mathrm{CP}}^{\mathrm{PMNS}} = -\pi/2$ at $4\%$ observational agreement.

**Falsification.** Confirmed inverted hierarchy (JUNO, 2026–2027) would refute the chirality-selector selection. Deviation of $\theta_{12}$ from $\arctan(1/\varphi)$ by more than $15\%$ would challenge the PMNS identification.

---

### R13 — Proton charge radius

**Standard form.** $r_p = 0.8414(19)$ fm (CODATA 2018), a long-standing puzzle with muonic-hydrogen measurements tensioning against electronic-hydrogen values.

**Cascade underpinning.** Spectral coherence length on the 600-cell: $r_p = 4 \bar\lambda_p$, where $\bar\lambda_p$ is the cascade Compton length of the proton (Paper XXXII).

**Recovery map.** Cascade → $r_p$:
$$\text{proton shell placement} + \text{coherence operator on 600-cell} \to r_p = 4 \bar\lambda_p = 0.8414 \text{ fm at } 0.04\%.$$

**Completion added.** Proton radius is **derived**, not fit. The muonic vs electronic tension is consistent with cascade prediction at both precisions.

**Falsification.** Revision of $r_p$ beyond combined experimental uncertainty would challenge the identification.

---

## What VFD Adds Over QM + SM + GR

Reading the Recovery Manifest top to bottom: VFD is not a rival to existing physics. It is a **unifying substrate** that supplies:

1. **Geometric origins** for quantities previously treated as empirical (α, $\sin^2\theta_W$, particle masses, $\Lambda$, mixing angles).
2. **Structural theorems** for features previously postulated (three generations, Born rule, strong-CP resolution, horizon character).
3. **A common substrate** on which QM, SM, and GR are three projections rather than three independent theories (Paper XXXV).
4. **Falsifiable tightness**: with no free parameters, every measurement is a test.
5. **Zero conflict with confirmed physics**: no VFD prediction contradicts any tested standard-physics result.

Readers of standard QM/SM/GR do not unlearn anything. They see where their shadows sit within the fuller geometric picture.

---

## Reading Order for Recovery

For a reader seeking to verify that VFD recovers each piece of QM/SM/GR:

### QM recovery path
1. **XXXVI** — Cascade foundations (F1–F8); read first for structural vocabulary.
2. **XXI** — Closure dynamics to Schrödinger (R1).
3. **XXX** — Born rule from Kähler + Gleason (R2).
4. **XXXI** — Measurement as sector separation (R3a).
5. **XLIV** — Decoherence as cross-rung coarsening (R3b).
6. **XLII** — $\delta U_{\mathrm{rel}}$ physical residual (completion of R1).
7. **XXXV** — Three-projection synthesis.

### SM recovery path
1. **XXXVI** — Cascade foundations.
2. **V** — 13 masses from 600-cell spectral data (R5).
3. **XXXII** — Hadron charge radii (R12).
4. **XXII** — α and Weinberg angle (R6, R7).
5. **XXXVII** — Neutrino sector (R11).
6. **XXXVIII** — Individual quark masses (benchmark correspondence).
7. **XXXIX** — W/Z/H electroweak sector.
8. **XXXVII §4** — Strong-CP resolution (R10).

### GR recovery path
1. **XXXVI** — Cascade foundations, especially F6, F7.
2. **XXIII–XXVII** — Event poset to field equations.
3. **XL** — Continuum theorems (T1–T4).
4. **XLI** — Schwarzschild analogue (R9).
5. **XXXV** — Three-projection synthesis.
6. **XXXVI** — $\Lambda$-ansatz (R8).

### Full synthesis
- **XXXV** (three projections of $E_8$ on 600-cell).
- **XXXVI** (foundations F1–F8).
- **This Recovery Manifest** (this document).

---

## Voice / Tone Guide for Papers

Every VFD paper should:

✅ Acknowledge the standard equation / result as **correct and important**.
✅ Identify the cascade underpinning explicitly, with rung and paper citation.
✅ Give the recovery map step by step, not as assertion.
✅ State what the underpinning **adds** (the "completion" — the non-shadow content).
✅ List falsification conditions tied to cascade tightness.

❌ Never say QM / SM / GR are "wrong."
❌ Never position VFD as a replacement theory.
❌ Never claim a "new theory of everything."
❌ Never overclaim beyond what the derivation establishes.

The programme's value is **structural economy and geometric origin**, not replacement. This voice buys credibility because it is **both humble about what the standard frameworks already achieve** and **precise about what VFD adds**.

---

## Status and Forward-Looking

As of 2026-04-17 this Recovery Manifest covers thirteen recovered structures (R1–R13) with explicit paper-by-paper derivation maps. Items deferred to forthcoming papers:
- **Yukawa structure** (individual fermion-Higgs couplings) — Paper XLVII.
- **Full CKM matrix** (beyond Cabibbo) — Paper XLVIII.
- **Hubble constant tension** — Paper XLIX.
- **Inflation / horizon problem** — Paper L.
- **Dark matter** — Paper LI.

Each deferred item will, when its paper is drafted, be added to the Manifest with a recovery map of the same three-part structure.

The Manifest is the programme's field-narrative spine. Every new VFD paper should cite it in its introduction and identify its position within it.
