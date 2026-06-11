# VFD Programme Plan

**Date:** 2026-04-17
**Scope:** public roadmap for the VFD (Vibrational Field Dynamics) research programme.

## Thesis in one sentence

VFD identifies the geometric cascade already implicit in known physics — Quantum Mechanics, the Standard Model, and General Relativity arise as projections of a single 7-rung $E_8 \to H_4 \to 40 \to D_4 \to 16 \to 8 \to 0$ cascade on the 600-cell, with zero free parameters after coupling matching — and closes the remaining gaps in scope through dedicated papers on neutrinos, individual quark masses, electroweak dynamics, continuum GR, and cross-rung phenomena (decoherence, observation, biology).

## What is already derived

| Domain | Source paper(s) | Predictions | Accuracy |
|---|---|---|---|
| 13 particle masses (leptons + hadrons) | I–V | m_e, m_μ, m_τ, m_p, m_n, m_π±, m_π0, m_K±, m_K0, m_η, m_η', m_ρ, m_ω | 0.014% average |
| Fine structure constant | XXII | $\alpha^{-1} = 137 + \pi/87$ | 0.81 ppm |
| Weak mixing angle | XXII | $\sin^2\theta_W = 3/8$ (GUT-scale) | exact match |
| Three generations | XXII | $Z_3$ Hopf-fiber action | exact structural match |
| 6 hadron charge radii | XXXII | $r_p = 4\bar\lambda_p$, $r_n$, $r_\pi$, $r_K$, $r_d$, magnetic $r$ | 0.04%–1.7% |
| Proton form factor | XXXII | Resolvent on 120 vertices | 0.3%–0.4% at low-$Q^2$ |
| Cosmological constant | F1+F4+F8 chain | $\Lambda \cdot \ell_P^2 = 2\varphi^{-583}$ (1st order) / $2\varphi^{-583}(1-\delta_\mathrm{dipole})$ (2nd order, `hypersphere-universe`) | 0.88% / 0.078% |

Plus structural results: quantum recovery via Madelung + Nelson pairing (XV–XXI), Born rule from Kähler uniqueness + Gleason (XXX), measurement as sector separation (XXXI), observer formalism (XXIX).

## What is scaffolded but not yet rigorous

- **General relativity** (Papers XXIII–XXVII): event poset → time → observer frames → metric candidates → curvature indicators → field-equation analogue. Continuum limit only sketched.
- **Biology rung (40)**: structural identification only; T-numbers $\{1,3,4,5\}$ matched; no DNA pitch or phyllotaxis derivation yet.
- **Observer rung (8)**: structural placement via $S^7 = \mathrm{Spin}(8)/\mathrm{Spin}(7)$; $G_2$ automorphisms identified but not tied to explicit observer algebra.

## Explicit gaps (known, being closed)

1. **Neutrinos** not placed in the $H_4$ spectrum assignment → Paper XXXVII.
2. **Individual quark masses** not derived (only composites) → Paper XXXVIII.
3. **W/Z/Higgs mechanism** absent (Weinberg angle reinterpreted but dynamics missing) → Paper XXXIX.
4. **Continuum theorems for $D_4$/GR** sketched, not rigorous → Paper XL.
5. **First concrete GR solution** (Schwarzschild analogue) not yet constructed → Paper XLI.
6. **Nonlinear residual $\delta U_{\mathrm{rel}}$** uninterpreted (gauge-removable or physical?) → Paper XLII.
7. **Biology rung quantification** (T-numbers, DNA pitch, phyllotaxis) → Paper XLIII.
8. **Decoherence as $H_4 \to \mathrm{Cl}(1,3)$ cross-rung coarsening** not derived → Paper XLIV.
9. **Observer rung $G_2$-automorphism formalism** not tied to LMC theorem → Paper XLV.

## The programme plan — four acts

### Act I — Consolidate (weeks 1–4)

1. **`docs/programme-plan.md`** (this document) — public narrative + gap list.
2. **Paper XXXVI: Cascade Foundations (F1–F8)** — consolidate the ~40 cascade-derivation markdown files into one rigorous foundation paper. This is the mathematical spine.
3. **VFD Explorer library completion** — 20% remaining. Every prediction must run through the library on every commit.
4. **Cross-paper consistency check script** — automated macro/bib/reference check across all papers.

**Exit criterion:** XXXVI published; Explorer produces all current predictions from git HEAD; consistency check passes.

### Act II — Close critical scope gaps (weeks 5–24)

Four tracks running in parallel:

**Track A (Matter sector):** XXXVII neutrinos → XXXVIII individual quark masses → XXXIX electroweak (W/Z/H).

**Track B (Geometry sector):** XL continuum theorems → XLI Schwarzschild analogue.

**Track C (Dynamics sector):** XLII physical interpretation of $\delta U_{\mathrm{rel}}$.

**Track D (Cross-paper hardening):** Codex review loops on Papers VI–XI, XXIII–XXVII.

**Exit criterion:** neutrinos placed, quark masses derived, W/Z/H mechanism formulated, continuum theorems proven.

### Act III — Extend to new rungs (weeks 20–48, overlapping Act II)

- **XLIII:** biology rung quantification.
- **XLIV:** information rung (decoherence).
- **XLV:** observer rung ($G_2$ formalism).

**Exit criterion:** every rung has at least one quantitative observable attached.

### Act IV — External validation (weeks 40–60)

- **Paper XLVI (to be commissioned):** experimental discriminators — a ranked list of measurements that distinguish VFD from standard SM.
- Pre-registration of the cleanest predictions on OSF or arXiv.
- Outreach to experimental groups for independent validation (proton form factor at JLab is the obvious first target).

**Exit criterion:** at least one external group has the prediction in writing; at least one prediction is pre-registered before measurement.

## Review-loop policy

Each new paper goes through an iterated codex review until it reaches **< 5 basic wording issues** in the latest review, OR the remaining issues are all in pre-existing content outside the paper's scope. Target rounds:

- Skeleton papers (scope-setting, not claim-establishing): 1–2 rounds.
- Substantive papers (new derivations, standard rigour): 3–5 rounds.
- Rigorous-with-proofs papers (foundation papers, continuum theorems): 5–8+ rounds.

The review loop is optimised by:

1. **Triage by paper type.** Prose-only synthesis papers get fewer rounds than new-theorem papers.
2. **Stop criterion.** When codex's "top 3 fixes" are all prose-asymptote, stop.
3. **Batch consistency review.** A dedicated codex pass reads multiple papers together and flags cross-paper inconsistencies.
4. **Always-on CI.** A pre-commit / CI check runs the consistency script + Explorer + macro/reference check.
5. **Known-issue list.** Each paper carries a `known-issues.md` alongside its `.tex` to prevent regression across rounds.

## Honest acknowledgments

- **Not a new fundamental theory.** VFD does not add new forces, dimensions, or particles. It identifies the geometric origin of structures already in known physics.
- **Shell assignment is axiomatic.** Papers I–III postulate the integer selection $\{9,12,14,15\}$ as mass eigenvalues; F3 makes this a theorem from Coxeter classification, but the assignment to specific particles is still an interpretive choice.
- **Continuum limit for GR is the weakest link** in the rigorous claim chain. Paper XL closes this.
- **$\delta U_{\mathrm{rel}}$ interpretation** is unresolved and is genuinely the fork point for how much of QM VFD claims to recover. Paper XLII closes this.
- **Biology rung** is a genuine extension into less-rigorous territory; will be flagged as such in Paper XLIII.
- **Consciousness** gets a structural placement only — not an explanation of qualia. This is the position explicitly stated in XXIX.

## Field-narrative summary

VFD is a **unifying geometric substrate** for known physics, not a replacement for it. Readers of SM, QM, and GR do not need to unlearn anything; VFD shows how their structures fit together on a common cascade. The quantitative evidence is strong (25+ predictions at 0.01–2%), the structural chain is explicit (F1–F8), and the gaps are listed publicly. The programme's value proposition is: **one geometric cascade, zero free parameters, full falsifiability through the VFD Explorer library**, with honest acknowledgement of what is derived, what is scaffolded, and what is still open.
