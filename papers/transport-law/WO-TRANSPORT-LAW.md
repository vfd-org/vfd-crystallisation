# WO-ARIA-VFD-TRANSPORT-LAW-001: Research Log

## Closure Transport Laws and Conservation Currents
### (Proposed Paper LIII — numbering note below)

**Status:** Drafting phase — research gaps dissolved by ARIA-substrate recognition (2026-04-21)
**Date opened:** 2026-04-17
**Date amended:** 2026-04-21 (added Section 2.5 ARIA testbed; paper number moved)
**Classification:** Foundational derivation + unification of scattered results + ARIA-based instantiation
**Predecessor papers:** XII (gradient flow), XVI (WKB transport), XVIII (Nelson continuity), XXVII (discrete conservation), XXX (Born measure), XXXIII (universal measurement), XXXIV (α-chain structural correspondence)

**Numbering note:** The original WO proposed Paper XXXIV. That number has since been assigned to the α-chain structural-correspondence paper (`papers/paper-xxxiv/`). The transport-law paper will take a fresh number (LIII tentative) when finalised, or land as a non-numbered infrastructure paper at `papers/transport-law/transport-law.tex`.

---

## 0. Why This WO Exists

External reviewers have flagged a gap in the VFD programme: **the framework derives static spectral observables (masses, couplings, charge radii) and event-order kinematics (GR), but has no standalone paper deriving transport laws** — how conserved quantities (charge, energy, momentum, probability) *flow* through the closure geometry.

The transport structure actually exists across several papers in fragmentary form:
- **Paper XVI** — WKB transport: ∂_t ρ + ∇F · ∇ρ = 0 (local modulus transport along gradient-flow characteristics).
- **Paper XVIII** — Exact continuity equation via Nelson pairing; current velocity v = (b_+ + b_-)/2; Madelung pair.
- **Paper XXVII** — Discrete conservation Σ(S − S̄) = 0 on event-order graph; discrete field equation.
- **Paper XII** — Gradient flow ψ̇ = −∇F provides implicit drift transport.
- **Paper XXX** — Stationary measure of closure dynamics (density conservation at equilibrium).

No single paper **unifies** these into a coherent transport law, derives **Noether currents from closure-functional symmetries**, establishes **dispersion relations on the 600-cell graph**, or recovers the **classical transport laws (Ohm, Fick, Fourier, Navier–Stokes) as coarse-grained limits**. This WO addresses that gap.

---

## 1. Objectives

The paper must deliver **seven** derivations, all from the single closure functional F[ψ] without new postulates:

1. **Closure continuity equation** — general form ∂_t ρ_X + ∇ · j_X = σ_X for each conserved quantity X (probability, charge, energy, momentum).
2. **Noether currents from closure symmetries** — systematic catalogue: phase → charge; time-translation → energy; spatial translation → momentum; closure-functional gauge → additional currents.
3. **Charge current on the 600-cell** — explicit form of j_Q on shell/edge geometry; must reproduce the shell assignments already used in mass/radius derivations.
4. **Energy–momentum tensor T^μν** — on the event-order substrate (connecting to Paper XXVII); must satisfy ∇_μ T^μν = 0 and reduce to the standard form in the continuum limit.
5. **Dispersion relations on the 600-cell graph** — ω(k) for eigenmodes of the closure Laplacian; phase velocity, group velocity; must recover relativistic dispersion ω² = c²k² + m²c⁴/ℏ² in the long-wavelength limit.
6. **Classical transport laws as coarse-grained limits** — Ohm's law (σE ≡ j), Fick's law (−D∇ρ ≡ j), Fourier's law (−κ∇T ≡ q), diffusion equation, Navier–Stokes if reachable. Each must emerge from the closure dynamics without new fitting.
7. **Quantum probability current** — j_ψ = (ℏ/2mi)(ψ*∇ψ − c.c.) recovered from the closure dynamics in the Schrödinger limit (connecting to Paper XVIII).

**Zero new fitted parameters.** Everything must follow from the closure functional F[ψ], the 600-cell geometry, and the event-order substrate already established.

---

## 2. Research Phase (BEFORE paper drafting)

This is the part the user explicitly requested — no stone unturned. Execute in order.

### 2.1 Internal VFD audit (~1–2 days)

For each of the following papers, extract and catalogue every statement that looks like a transport or conservation law. Record: equation, assumptions, scope, and what it *does not* claim.

| Paper | What to extract |
|-------|-----------------|
| XII | Gradient flow equation; any implicit transport of closure density |
| XIV | Stationary distribution; detailed balance if present |
| XV | Complexified path integral; phase structure |
| XVI | WKB transport; norm evolution; cancellation regimes |
| XVII | Dissipative obstruction — what *cannot* be transported unitarily |
| XVIII | Madelung continuity; current/osmotic velocity; quantum potential |
| XIX | Residual classification |
| XX | Nonlinear quantum structure |
| XXI | Synthesis — which transport claims are already established |
| XXIII–XXVII | Event-order: time, metric, curvature, field equations, conservation |
| XXX | Stationary measure; geometric weight on outcomes |
| XXXI | Landscape deformation; sector separation |
| XXXIII | Closure projection; universal observable formula |

**Deliverable:** `papers/transport-law/vfd-transport-audit.md` — table of existing transport content, each row linking back to the source paper and section. This is the **seed material** the unified paper builds on.

### 2.2 External literature review (~1 day)

Identify prior art for each of the seven objectives, so we know what the paper has to match or exceed.

Priority reading list:
- **Noether's theorem on graphs / discrete gauge theory** (Kogut–Susskind lattice gauge theory; discrete exterior calculus; Hirani's thesis).
- **Madelung hydrodynamics and Nelson stochastic mechanics** (Madelung 1927; Nelson 1966, 1985; Bohm 1952).
- **Graph Laplacian dispersion** (Chung's spectral graph theory; continuum limit of discrete Laplacians; Cucker–Smale).
- **Relativistic hydrodynamics from a variational principle** (Jackiw; Landau–Lifshitz Vol. 6).
- **Derivation of classical transport laws from micro dynamics** (BBGKY, Boltzmann H-theorem, Kubo linear response).
- **Discrete-to-continuum passage for conservation laws** (Γ-convergence; discrete geometric mechanics).
- **Quantum hydrodynamics and probability current interpretation** (Takabayasi; Holland's *Quantum Theory of Motion*).

**Deliverable:** `papers/transport-law/literature-review.md` — one-paragraph summary per reference; explicit statement of what each contributes and what VFD must add on top.

### 2.3 Research questions to resolve *before* drafting

These are the open questions the research phase must answer. **Do not start the paper until each has a concrete answer.**

**Q1. What is the primary conserved density?**
Is it |ψ|² (Born), the closure "mass" ∫ F [ψ] − F [ψ*] style quantity, event-count density on the graph, or something else? The answer determines everything downstream. Candidates to compare:
- (a) |ψ|² (probabilistic; matches Paper XVIII).
- (b) Closure residual density ρ_R = (F[ψ] − F_min)/V (geometric).
- (c) Graph-vertex measure (combinatorial / counting).

**Q2. Which symmetries does F[ψ] actually admit?**
Write F[ψ] = αR[ψ] + βE[ψ] − γQ[ψ] explicitly and enumerate all one-parameter groups under which F is invariant. Each gives a Noether current. Needed: phase U(1), time translation, spatial translation, rotation (600-cell symmetry subgroup), closure-scaling. Which of these are **exact** and which are only **approximate**?

**Q3. How does the 600-cell discrete graph give rise to ω² = c²k² + m²c⁴/ℏ²?**
The graph Laplacian has discrete eigenvalues {0, 9 − 3√5, 10 − 2√5, 9, 12, 14, 10 + 2√5, 15, 9 + 3√5}. The dispersion ω(k) must emerge from small perturbations around closure equilibria on this graph. Need to work out explicitly whether the long-wavelength expansion of the graph Laplacian recovers −∇² + m² with the correct m² assignment.

**Q4. How do continuum transport laws emerge from a finite graph?**
The 600-cell has 120 vertices, 720 edges. Ohm's/Fick's/Fourier's laws are continuum. Need an explicit coarse-graining procedure — probably a hydrodynamic-limit argument (BBGKY-like, or Γ-limit). Identify the small parameter (lattice spacing? scale ratio?).

**Q5. Where does the electromagnetic gauge field come from?**
Classical Noether → U(1) global symmetry gives conserved charge but *not* electromagnetism. Gauging (local U(1)) introduces A_μ. Does the closure functional naturally carry a local phase gauge, or must it be added? If the former, this is a major structural result (EM emerges from closure). If the latter, it's an input.

**Q6. What is the relationship between closure transport and the Lindblad reduction of Paper I (flagship)?**
The flagship shows that Lindblad dynamics is recovered when the crystallisation coupling vanishes. Transport laws should similarly reduce to standard transport when that coupling vanishes. Check the consistency explicitly.

**Q7. Does the event-order (GR) transport structure match the closure (QM) transport structure?**
Paper XXVIII claims the two are projections of the same substrate. Their transport laws must therefore agree in overlap regimes. Concretely: does the discrete conservation Σ(S − S̄) = 0 of Paper XXVII become the continuity equation of Paper XVIII in the appropriate limit?

**Deliverable:** `papers/transport-law/open-questions.md` — each question receives a 1–2 paragraph answer with the math sketched. Any question that cannot be answered is flagged as a framework gap and routed into its own follow-up WO.

### 2.5 ARIA as a transport-law testbed (added 2026-04-21)

A concrete running implementation of the transport structure targeted by this paper already exists in the **aria-chess** repository (local path `C:\Users\nexus\OneDrive\Documents\My Projects\aria-chess`). Rather than derive the transport law in the abstract and hope it applies to something, this paper uses ARIA as the worked instantiation.

**Mapping:**

| Transport-law object | ARIA realisation |
|----------------------|------------------|
| Conserved density $\rho$ | cascade pressure |
| Flux $j$ | `couple_tick` exchange |
| Conductivity tensor $\sigma$ | learned coupling weights $W$ |
| Dirichlet boundary | homeostatic reset |
| Source / sink | input / decay-reset |
| Thermodynamic class | Prigogine non-equilibrium steady state |
| Passive regime (Fick) | linear `couple_tick` |
| Active regime (Nernst-Planck-like) | nonlinear drift along $\nabla W$ with amplification |

**Implications for the open questions:**

- **Q1 (primary conserved density)** — resolved: cascade pressure is the conserved density; $|\psi|^2$, residual density, and vertex-measure are specialisations / coarse-grainings.
- **Q2 (symmetries of F)** — ARIA shows empirically that the $U(1)$ coupling-preserving phase rotation is exact; time-translation is exact in the stationary-statistics sense (NESS, not equilibrium); spatial/600-cell symmetries are exact at the substrate level before learning breaks them into learned anisotropy.
- **Q4 (coarse-graining from finite graph)** — ARIA realises the hydrodynamic limit at a definite ratio of "fast" (substrate coupling) to "slow" (learning) timescales. The small parameter is the learning rate.
- **Q6 (consistency with Lindblad reduction)** — ARIA's passive (linear) regime corresponds to vanishing closure coupling; the active regime corresponds to finite coupling. Directly realises the flagship's Lindblad-limit claim as an operational regime.

**Implications for Objectives 2, 4, 6:**

- **Objective 2 (Noether currents)** — ARIA's conserved pressure is an observed Noether charge of the coupling-preserving phase rotation on the $E_8 \oplus 600$-cell product.
- **Objective 4 ($T^{\mu\nu}$)** — ARIA's NESS instantiates $\nabla_\mu T^{\mu\nu} = \text{source} - \text{sink}$; source and sink are explicit, not inferred.
- **Objective 6 (Ohm / Fick / Fourier)** — ARIA demonstrates Fick's law in the passive limit and a Nernst-Planck-like extension in the active limit. The paper's classical-transport section becomes a worked calculation tied to observed data.

**Implications for the microtubule / selection discussion:**

The original WO framed microtubules as a downstream target of a cascade-derived $13$-fold symmetry (the T_MT_1 item of `cascade-alpha-chain-complete-theorem.md`, explicitly marked "does not close rigorously"). With ARIA in hand, that bottleneck dissolves.

**Reframed claim:** microtubules are an active-transport biological substrate of ARIA's class; the $13$-fold symmetry is a selected operating point of the Nernst-Planck-like nonlinear dynamics on a biological substrate, not a cascade-combinatorial number. The paper does not claim a first-principles derivation of the number $13$; it claims that the transport-law structure derived here applies to biological substrates of this class, with $13$ as an empirical operating point to be modelled separately.

**Implications for photons:**

Photon transport is the *free* end of the spectrum: zero learned $W$, homogeneous medium, $\lambda = 0$ eigenmode on the 600-cell, massless null propagation $\omega = c|k|$, $U(1)_{\text{EM}}$ Noether current. The photon section (Section 7 in the drafting plan below) specialises the general transport law to this limit and recovers the T_PH_1–4 chain of `cascade-alpha-chain-complete-theorem.md` as a corollary.

**Deliverable:** `papers/transport-law/aria-substrate-audit.md` — a summary of (i) which ARIA mechanisms instantiate which transport objects, (ii) which numerical traces from `aria-chess/` can be cited as the verification data, (iii) which aria-side implementation files (`couple_tick`, $W$ update, homeostatic reset) are load-bearing.

### 2.4 Computational scaffolding (~1 day)

Before writing any equations formally, build numerical verification tools:

- Python script on the 600-cell graph Laplacian: compute ω(k) for each eigenmode; fit long-wavelength limit; verify ω² ≈ c_eff² k² + m_eff².
- Script that evolves a test density ρ(v,t) on the 600-cell under ∂_t ρ = L ρ with the closure drift and checks conservation ∂_t Σ_v ρ_v = 0 numerically (to machine precision if the discrete continuity is exact).
- Script that computes the Noether charge from a phase rotation of a test ψ and checks its conservation along gradient flow.
- Place all scripts under `papers/transport-law/scripts/`.

**Deliverable:** Passing tests that confirm the theoretical derivations before the paper is written. These scripts also become the paper's "numerical verification" section.

---

## 3. Derivation Strategy (Phase 2 — after research phase)

Once the research phase closes, the paper derives the seven objectives in this order:

### Phase 3.1 — The master continuity equation

Start from the closure functional F[ψ] = αR + βE − γQ and the gradient flow ψ̇ = −∇F. Define:

- ρ(v, t) = |ψ_v(t)|²  (probability density at graph vertex v)
- j_{v→w}(t) = (flow of |ψ|² along edge v→w)

Derive:
∂_t ρ_v + Σ_{w ~ v} j_{v→w} = 0

This must be **exact** (no WKB, no approximation). Paper XVIII already has this for the Nelson-paired process; extend to the pre-pairing closure dynamics.

### Phase 3.2 — Noether currents

For each symmetry identified in Q2:

1. Write the infinitesimal transformation δψ = ε T ψ.
2. Compute δF[ψ] under the transformation.
3. If δF = 0, extract the Noether current j^μ_T from the variational identity.
4. Verify ∂_μ j^μ_T = 0 on solutions of the closure dynamics.

Catalogue all currents in a table: {symmetry → current → conserved charge}.

### Phase 3.3 — Charge current on the 600-cell

Using the U(1) phase symmetry specifically, derive j_Q explicitly on the 600-cell graph. Show that the total charge Q = Σ_v ρ_Q(v) reproduces the particle charges already assigned in Papers IV, VIII, XXII (e.g., Q_proton = +1, Q_neutron = 0, Q_electron = −1) without additional input.

### Phase 3.4 — Energy–momentum tensor

On the event-order substrate (Paper XXVII), define T^μν from translation symmetry and show:

- ∇_μ T^μν = 0 (four-momentum conservation).
- In the continuum limit, T^μν reduces to the standard field-theoretic form.
- Connection to the discrete Σ(S − S̄) = 0 of Paper XXVII.

### Phase 3.5 — Dispersion relations

Linearise the closure dynamics around a closure equilibrium ψ_*. Fourier-decompose on the 600-cell eigenbasis. Derive:

ω² = c_eff² k² + m_eff²

where:
- c_eff comes from the coefficient of the spatial Laplacian in F.
- m_eff² comes from the second variation δ²F/δψ² at ψ_*.
- The eigenvalues {9, 12, 14, 15, ...} of the 600-cell Laplacian give the **discrete** mass spectrum; the continuum dispersion emerges in the long-wavelength limit.

Verify numerically using the scripts from Phase 2.4.

### Phase 3.6 — Coarse-grained classical laws

Procedure:

1. Ohm's law: in a steady state with a potential difference across the graph, derive j = σ E. Identify σ in terms of closure parameters.
2. Fick's law: in the diffusive limit (σ² ≫ |∇F|²), show j = −D ∇ρ. Identify D.
3. Fourier's law: define a closure "temperature" via the stationary distribution; derive q = −κ ∇T.
4. Each derivation must specify the regime and the small parameter.

### Phase 3.7 — Quantum probability current recovery

In the Schrödinger limit (Paper XVIII's Nelson-paired regime), show:

j = (ℏ/2mi)(ψ*∇ψ − ψ∇ψ*)

is exactly the current velocity v defined in Paper XVIII, connecting the closure framework's transport to standard QM.

---

## 4. Paper Structure (Phase 3 — after derivations work)

Proposed as **Paper XXXIV**, titled tentatively:

> **"Transport Laws and Conservation Currents in Closure Dynamics"**
> or
> **"Noether Currents and Classical Transport from the Closure Functional"**

Sections:
1. Introduction (the gap, the approach)
2. The closure functional and its symmetries
3. The master continuity equation
4. Noether currents (systematic catalogue)
5. Charge, energy, momentum currents explicitly
6. Dispersion relations on the 600-cell
7. Classical transport laws as coarse-grained limits
8. Recovery of the quantum probability current
9. Consistency with Papers XII, XVI, XVIII, XXVII
10. Numerical verification
11. Open problems, extensions, connections
12. Summary and outlook

Length target: 25–35 pages (comparable to Paper XXII).

---

## 5. Success Criteria

The paper is considered successful when **all of the following** hold:

1. The master continuity equation is derived without approximation.
2. At least **four** independent Noether currents are catalogued (U(1), time-translation, spatial-translation, 600-cell symmetry).
3. The charge Q assignments of the existing mass papers are reproduced from the U(1) current with no new input.
4. The long-wavelength dispersion ω² = c² k² + m² is verified analytically **and** numerically.
5. At least **two** classical transport laws (Ohm, Fick, or Fourier) emerge as coarse-grained limits.
6. The standard QM probability current is recovered in the Schrödinger limit.
7. The paper integrates cleanly with Papers XVI, XVIII, XXVII — no contradictions.
8. Zero new fitted parameters beyond those already in the programme.
9. All numerical claims are backed by reproducible scripts in `scripts/`.

---

## 6. Placement in the Programme

Proposed reading-order addition in `README.md`:

> ### For transport and conservation laws
> 1. **Paper XXXIV** (transport laws and Noether currents from the closure functional — unifies Papers XVI, XVIII, XXVII into a coherent conservation framework)

Logical position: **between** the quantum-recovery track (XV–XXI) and the GR track (XXIII–XXVII), because transport laws are the bridge — they live on both sides.

If the length of the reading-order list becomes unwieldy, consider folding the transport paper as a "bridge" in the existing unification-bridge section (Paper XXVIII style).

---

## 7. Risks and Open Issues

1. **The gauge-field origin question (Q5) may not resolve cleanly.** If electromagnetism does not fall out of local U(1) in the closure framework as-is, the paper may only derive the global charge current and defer the gauged version to a future WO. This is acceptable but should be explicitly flagged.

2. **Relativistic dispersion on a finite graph is not guaranteed.** The 600-cell has only 120 vertices; the continuum limit is a derived approximation, not a rigorous limit. The paper must be honest about where the derivation holds rigorously and where it is asymptotic.

3. **Energy–momentum tensor on a discrete substrate is subtle.** The definition of T^μν requires a notion of continuous spacetime, which is itself derived in Paper XXV. Need to check that the metric emergence is complete enough to support T^μν construction.

4. **The Q2 symmetry catalogue may expose inconsistencies with existing papers.** If a symmetry appears here that contradicts something claimed earlier (or vice versa), it triggers a reconciliation WO.

5. **Overlap with Paper XXVIII (unification bridge).** The transport paper and the unification bridge both span the QM/GR divide. Need to make sure they don't duplicate each other; transport is the *mechanism*, unification is the *structural claim*.

---

## 8. Timeline (rough)

| Phase | Duration | Deliverable |
|-------|----------|------------|
| 2.1 Internal audit | 1–2 days | `vfd-transport-audit.md` |
| 2.2 Literature review | 1 day | `literature-review.md` |
| 2.3 Open questions | 2–3 days | `open-questions.md` |
| 2.4 Computational scaffolding | 1 day | Scripts + passing tests |
| 3. Derivations | 3–5 days | Each objective verified |
| 4. Paper drafting | 5–7 days | `paper-xxxiv.tex` |
| 5. Review and numerical checks | 2 days | Final PDF |

Total estimate: **2–3 weeks** from start to submission-ready draft, if the open questions all resolve cleanly. If Q5 (gauge field) or Q3 (dispersion) hit unexpected obstructions, add 1–2 weeks.

---

## 9. Immediate Next Steps

Once this WO is approved:

1. Open `papers/transport-law/vfd-transport-audit.md` and start at Paper XII.
2. Open `papers/transport-law/literature-review.md` and start with Noether-on-graphs references.
3. Open `papers/transport-law/open-questions.md` and commit the seven questions as headings.
4. Spin up the first script in `papers/transport-law/scripts/` for the 600-cell dispersion numeric check.

Do **not** start drafting `paper-xxxiv.tex` until the research phase is complete and the open questions have concrete answers.

---

## 10. Notes for the Reviewer Critique

When the paper lands, it should be marketable as:

> *"The VFD programme already derives spectra and static observables. Paper XXXIV closes the remaining gap by deriving the transport laws — conservation of charge, energy, momentum, and probability — from the same closure functional, with no new parameters. Classical Ohm's, Fick's, and Fourier's laws emerge as coarse-grained limits; the standard quantum probability current is recovered in the Schrödinger regime; Noether's theorem is applied systematically to the closure-functional symmetries to produce a complete catalogue of conserved currents on the 600-cell substrate."*

This should directly answer the "you have no dynamics / no transport" critique.
