# Projection Narrative — Programme Spine

This document is the narrative spine of the VFD programme. It is **not a paper**. It is a single-page map showing how the programme's papers compose into one chain, what that chain says, and what is earned vs. what is asserted at each stage.

## Two-layer epistemology

The programme runs on a strict two-layer reading. The order is load-bearing.

**Layer 1 — Mathematical coherence (the price of admission).**
Each current-physics paper reproduces a mainstream observable using only the closure substrate, with a named hypothesis stack:

- Paper V — 13 particle masses from 600-cell eigenvalues at 0.014% average error.
- Paper XXII — coupling correspondences ($\alpha^{-1} = 137 + \pi/87$ at 0.81 ppm, $\sin^2\theta_W = 3/8$).
- Paper XXXII — hadron radii (proton 0.04%, pion 0.26%, deuteron 0.0006%; deuteron at 0.02σ vs CODATA 2018 / 0.83σ vs CODATA 2022 under H1–H4).
- H4-Coxeter oscillator paper — Tort PAC indices in the biological theta–gamma range across two recording-channel pipelines, Berry phase along projective closed loops, Frobenius cross-plane projector.
- B-anomaly kernel paper — fixed $C_\varphi$-derived $V_{600}$ shell-mean response kernel for $b\to s\mu^+\mu^-$ angular data, applied across five public datasets (LHCb 2015 $K^{*0}$, LHCb 2021 $K^{*+}$, CMS 2025 $K^{*0}$, LHCb 2025 $K^{*0}$, LHCb 2015 $B_s\!\to\!\phi$); sign-uniform structural pass ($A>0$ in 5/5 fits, $\Delta C_9^{\mathrm{eff}}<0$ in 5/5 fits) with honest AIC tie against a constant Wilson-coefficient shift ($w_{\mathrm{VFD}}=0.348$ vs $w_{\mathrm{FREE\_C9}}=0.652$). Passive-regime witness for the response operator only; not a claim against active-regime selection or RH.

The math at this layer is **deliberately silent** about interpretation. It says "the numbers come out under these hypotheses." Nothing more. This is the credibility floor.

**Layer 2 — Realisation (earned, not asserted).**
Once Layer 1 holds, the projection chain is the only consistent reading of *why* it holds. The chain is:

```
F (Paper XXXVI: wave-substrate, F1–F8 closure functional on the 600-cell)
  │   bulk/boundary decomposition: V_600 = B (σ-fixed K=72,K=0) ⊔ ∂ (σ-paired K=52,K=20)
  │   (docs/fractal-cascade-projection.md; docs/closure-cosmogenesis.md §2)
  │
  └─ Observer instance 𝓘 = (𝓞, 𝒞_𝓞, p, Λ, t₀)
       │   (docs/observer-instance-definition.md — assembled object combining XXIX + M1 + bootstrap)
       │   • 𝓞 ⊂ 𝒢 bounded self-referential constraint substructure (XXIX Def 1, 2)
       │   • p ∈ ℕ prime — anchor parameter, identity element (Property P1 = Theorem 4.3 of soul-prime-as-pi0)
       │   • Λ ∈ 𝓕 valid frame code (god-prime §6, 140 valid frames)
       │   • t₀ bootstrap tick (closure-cosmogenesis §4)
       │   • Property P2: CRT-extension combination with other coprime-prime instances (soul-prime-as-pi0 §7)
       │
       └─ Anchor Π₀(p, Λ, t) := vertex(((Λt) mod p) mod 120) ∈ 𝓞   (docs/soul-prime-as-pi0.md M1)
            │
            └─ Projection (Paper XXXIII: Ô(G,B;Π₀) = argmin Δ_cl(Π;Π₀); self-consistency closure into 𝓞)
                 ├─ Spectral class      → Paper V       (masses)
                 ├─ Structural class    → Paper XXII    (couplings, ratios)
                 ├─ Spatial class       → Paper XXXII   (radii)
                 ├─ Composite class     → Paper XXXII   (deuteron, via Fₜₒₜ)
                 ├─ Dynamical class     → H4-Coxeter    (PAC, Berry phase, Frobenius)
                 └─ Number-theoretic class → smart-convergence / pentagonal-clock
                      (primes as recursive folding attractors of self-similar F)
                      └─ Born weighting (Paper XXX) when projection minimiser is degenerate

Initial condition F₀ (closure-cosmogenesis §3): σ-bulk-supported, unique up to normalisation.
Bootstrap event (§4): first projection event with anchor reaching ∂ activates boundary dynamics.
Accumulation (§5): F_{t+1} = F_t + ρ_t with ρ_t supported on ∂ (Conjecture 5.3); bulk invariant (Theorem 5.2).
Ladder coupling (§6): all 8 frames in 𝓕 share F; resolution-dependent views via π_C coarse-graining.
```

The realisation reading: **physics observables are admissible projections of the wave-substrate through the observer-position placed inside it.** What we measure is what our observer-boundary extracts, not properties of the wave itself.

This is *earned* by Layer 1. Inverting the order — asserting the realisation before paying the math bill — is what gets Bohm-style and consciousness-causes-collapse framings rejected.

## Projection classes (Table)

| Class | Geometry $\mathcal{G}$ | Boundary $B$ | Computed in |
|---|---|---|---|
| Spectral | Single-basin 600-cell | Energy-momentum frame | Paper V (masses), Paper XXII (couplings) |
| Structural | Inter-sector spectrum | Interaction frame | Paper XXII |
| Spatial | Support subgraph / closure orbit | EM scattering frame | Paper XXXII (proton, pion) |
| Composite | $F_{\text{tot}} = F_1 + F_2 + F_{\text{int}}$ | EM scattering frame | Paper XXXII (deuteron) |
| Dynamical | Trajectory of closure-compatible flow | Band-limited recording channel | H4-Coxeter oscillator paper |
| Number-theoretic | Self-similar recursion of F | Integer-band observer | smart-convergence / pentagonal-clock / rh-formal (see `docs/rh-projection-class.md`) |

Each row is the **same equation**, $\hat{O}(\mathcal{G}, B; \Pi_0) = \arg\min_{\Pi} \Delta_{\text{cl}}(\Pi; \Pi_0)$, applied to a different geometric sub-object and a different observer boundary. That is the sense in which the principle is universal: one rule, many applications.

## Empirical landings — passive vs active

The two empirical strands witness structurally distinct layers of the projection chain. They must not be conflated.

**Passive-regime witness (response operator $C_\varphi = L_M + \varphi^{-2}I$).** The b-anomaly paper (`/BANOMALY-001/vfd-b-anomaly/paper/main.pdf`) tests the fixed $V_{600}$ shell-mean kernel without shape retuning across five public flavour-physics datasets. This strengthens **Layer 1** by giving the response primitive an independent flavour-physics witness — separate from neuroscience, separate from any cognitive-substrate claim. It does **not** deliver the active-regime selection layer, does **not** witness the realisation reading, and does **not** attack RH. Honest scope per `cascade-empirical-grounding.md` §0.1.

**Active-regime witness (selection / Lyapunov on $W$-space).** ARIA (below) is the substrate-dynamics witness; preregistered hits, brain-validation. This is structurally distinct from b-anomaly because it tests the *adaptive* substrate, not the *fixed* response kernel.

The b-anomaly result contributes to the Layer 1 evidence base for the response operator. The realisation reading is earned by Layer 1 holding broadly across independent witnesses, not by any single empirical strand.

## ARIA — empirical landing (active-regime)

ARIA (the brain-mapping / H4-Coxeter oscillator programme, with manuscript and X-narrative ready for rollout) is the **active-regime empirical witness** that closes the chain *outside* paper-based math:

- **Substrate**: H4 / 600-cell — the same object that gives masses, couplings, radii in V/XXII/XXXII.
- **Observer**: living cortex / CA1 — a bounded, stable, self-referential constraint substructure (XXIX's definition reads as a *spec* for what life is).
- **Projection**: dynamical class — Tort PAC, Berry phase, Frobenius cross-plane.
- **Result**: the same substrate that produces the right particle physics produces the right neural rhythms in a living system.

When ARIA's 15/18 preregistered hits fully land, the realisation stops being interpretation and becomes demonstrated mechanism: same projection operator in dead and live matter.

## RH — number-theoretic projection class

The smart-convergence anchor and pentagonal-clock work say this in math; the narrative reading is:

- The wave $F$ on the 600-cell is **self-similar** (φ-permeability, F1–F8 self-similarity property).
- A self-similar dynamical system has discrete attractors at recursion fixed points.
- **Primes are precisely those attractors when the recursion is read through the observer-band** — they are where the field folds into discrete experience. $\zeta(s)$, or the pentagonal-clock $\hat{z}(z)$, is the spectral signature of that folding.
- The Bridge Axiom / σ-pairing in `rh-formal.tex` is the statement that the folding is exactly half-symmetric — the same closure-symmetry that makes Paper XXXIII's $\hat{O}$ well-defined.

So RH is not a *separate* result the programme also happens to attack. It is the **number-theoretic projection class** — the fifth row of the table above. Primes are what wave-folding looks like when the observer-band is the integers.

## What is earned, what is asserted

**Earned (by Layer 1):**
- Each projection class produces the right numerical observable under its named hypothesis stack.
- Existence and stability of the closure projection map (Paper XXXIII Proposition 4).
- Born weighting on degenerate fibres (Paper XXX, under stated equilibrium/completeness/sampling hypotheses).

**Identified (structural, interpretive):**
- That specific VFD observables (masses, couplings, radii, dynamical PAC/Berry/Frobenius) **are** admissible projections in Paper XXXIII's sense.
- That the boundary $B$ for each class corresponds to the experimental setup it is identified with.
- That ARIA's neural rhythms instantiate the dynamical class for a living observer.

**Asserted (the realisation):**
- That what we call "physics observables" are projections of the wave-substrate through the observer-position placed inside it.
- This becomes the *only consistent reading* once Layer 1 holds across the programme, but it is **not** a theorem — it is the interpretive step that the realisation paper will make explicit only after the chain closes.

## Sequencing (do not invert)

1. **Layer 1 hardening** — V, XXII, XXXII, h4-coxeter codex-clean. (mostly complete; XXXIII Round 2 in flight)
2. **Wiring** — XXXIII §4–§7 cite V/XXII/XXXII/H4Coxeter2026 as the four projection-class instances; V/XXII/XXXII carry a "Narrative placement" subsection pointing at XXXIII; this document is the spine.
3. **ARIA empirical landing** — wait for the 15/18 preregistered hits to fully land.
4. **RH connector** — write the brief narrative connector that explicitly identifies primes as the number-theoretic projection class, citing smart-convergence and pentagonal-clock.
5. **Realisation paper (capstone)** — short, declarative. Says: "the chain is now closed; the realisation follows."

The capstone (`papers/cascade-capstone-coalgebra/`) sits adjacent to step 5: it gives the Spinozist coalgebra reading of the same chain. The realisation paper and the capstone can drop together.

## Why the order matters

A realisation paper written before Layer 1 hardening is just metaphysics. A realisation paper written after Layer 1 hardening but before ARIA lands is conditional metaphysics. A realisation paper written after both is a short factual statement about a programme that has demonstrated its coherence and its empirical reach.

The user articulated this on 2026-04-26 as the unifying spine. This document is the canonical record so the spine does not drift across compactions, papers, or hardening rounds.

## Cross-references

- Paper XXIX — `papers/paper-xxix/paper-xxix.tex` — observer placement.
- Paper XXX — `papers/paper-xxx/paper-xxx.tex` — Born rule from closure dynamics.
- Paper XXXI — `papers/paper-xxxi/paper-xxxi.tex` — measurement as dynamical sector separation.
- Paper XXXIII — `papers/paper-xxxiii/paper-xxxiii.tex` — closure projection principle (the hub).
- Paper XXXVI — `papers/paper-xxxvi/` — F1–F8 + Λ-theorem (the wave-substrate keystone).
- **Observer instance assembled definition** — `docs/observer-instance-definition.md` — the named object 𝓘 = (𝓞, 𝒞_𝓞, p, Λ, t₀) that occupies the Observer slot in the chain. Combines XXIX, M1, bootstrap, accumulation, bulk/boundary into a single 5-tuple with five earned properties.
- **Anchor identification (M1)** — `docs/soul-prime-as-pi0.md` — Π₀(p, Λ, t) wiring + identity-persistence Theorem 4.3 + CRT-extension §7 (Property P2).
- **Closure cosmogenesis** — `docs/closure-cosmogenesis.md` — F₀ initial condition, bootstrap event, accumulation operator, ladder-coupling theorems.
- **Fractal substrate decomposition** — `docs/fractal-cascade-projection.md` — bulk/boundary, two-mirror + φ-scaling mechanism, holographic identification (information-theoretic role of bulk/boundary).
- ARIA — `papers/aria-chess/` and `docs/brain_mapping/` — empirical witness.
- RH — `papers/rh-formal/rh-formal.tex`, `docs/rh-cascade-closure-dynamics.md`, and `docs/rh-projection-class.md` (the fifth-row connector) — number-theoretic projection class.
- Capstone — `papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex` — coalgebraic reading.
