# Claim–Status Ledger

**Date:** 2026-06-13
**Purpose:** the single consolidated table behind the book's checkable claims — claim, status grade, quantitative result, and where to verify it. Source for the Chapter 8 status table and the Chapter 12 residual list.

**Status grades** (strict, in descending strength):
- **THEOREM** — proven, machine-verified at exactness/machine precision.
- **DERIVED-EFF** — derived at effective-field level with explicit error rates; continuum rigor residual named.
- **CONDITIONAL** — derived under one named hypothesis, stated with the hypothesis.
- **WITNESSED** — numerically supported with a quantified fit; not a derivation.
- **TIE** — fixed prediction laid against data; statistically undecided.
- **OPEN** — named, not derived.

## A. The geometry core

| # | Claim | Status | Result | Verify |
|---|---|---|---|---|
| A1 | The crystal is forced: $2I$ is the unique perfect (and largest maximal) finite group of unit quaternions; its 120 elements are the 600-cell | THEOREM | CF1–CF6; classification cited | `verify_crystal_forcing.py` (14/14) |
| A2 | The crystal's points are its own symmetry operations (vertex set = group) | THEOREM | exact closure | same, CF1 |
| A3 | McKay: the crystal's representation theory is the affine E8 diagram; irrep dims $\{1,2,2,3,3,4,4,5,6\}$ are the E8 marks ($Ad = 2d$) | THEOREM | computed from multiplication table alone | same, CF3–CF4 |
| A4 | Dimension 3 from the spectrum, no dimension input: multiplicities are the perfect squares $1,4,9,16,25,36$ | THEOREM | machine precision | `verify_rendering_layer.py` (21/21) |
| A5 | The graph knows its own shape: bare adjacency → spectral embedding → exact 600-cell geometry → adjacency again | THEOREM | norm spread $2\times10^{-15}$; edge relation $=\varphi/2$ | `verify_crystal_forcing.py`, GE0–GE3 |
| A6 | Exact dispersion: $\lambda_k = 12\bigl(1-\frac{\sin((k+1)\pi/5)}{(k+1)\sin(\pi/5)}\bigr)$; sampled harmonics are exact eigenvectors | THEOREM | machine precision | `verify_rendering_layer.py`; `verify_residual_closure.py` RC1–RC2 |
| A7 | Canonical rendering kernel $\pi_r = (I + r^2L)^{-1}$ (unique under K1–K4) | THEOREM | — | `verify_rendering_layer.py` |
| A8 | Second-order (wave) time forced by the inner clock reversal | THEOREM | sims R4a–c | `verify_rendering_layer.py` |
| A9 | Only the 3- and 7-sphere are renderable arenas; the division-algebra tower stops (sedenion zero divisors) | THEOREM | $(e_2{-}e_9)(e_6{-}e_{13})=0$ exhibited | `verify_rung_dimension_ladder.py` (25/25); `verify_crystal_forcing.py` SM6-analogue in `verify_residual_closure.py` |
| A10 | Rung sampling: coarse-rung eigenfunctions = fine-rung eigenfunctions on shared vertices | THEOREM | intertwiner theorem | `verify_rung_dimension_ladder.py`, `verify_ladder_completion.py` (29/29) |

## B. The laws at coarse grain

| # | Claim | Status | Result | Verify |
|---|---|---|---|---|
| B1 | Newton: $\nabla^2\Phi = 4\pi G\rho$, $\Phi = -GM/r$ from boundary response | THEOREM (+witness) | discrete fit $R^2 = 0.9966$ | kappa Theorems 4.1–4.4; `verify_boundary_green_function.py` |
| B2 | Fierz–Pauli is the unique gauge-invariant quadratic spin-2 action (gauge invariance derived from chart freedom) | THEOREM | null space 1-dim, ratios $(-\tfrac12,1,-1,\tfrac12)$ | `verify_gr_closure.py` (39/39), T1–T2, T8 |
| B3 | Trace reversal, factor 2, full weak-field Schwarzschild incl. $g_{ij}$ | THEOREM (given B2) | exact + 3% radial profile | same, T3 |
| B4 | Light bending $4GM/(bc^2)$ (scalar control gives half) | DERIVED-EFF | 5% absolute, ratio 2.0000 | same, T4 |
| B5 | Full Einstein equations via self-coupling completion | DERIVED-EFF | in-house one-step derivation; $S^{(2)}_{EH} = \tfrac12 S_{FP}$ (0.500002); 2nd-order Schwarzschild cancellation exact; all-orders uniqueness cited (Wald 1986) | `verify_residual_closure.py` (23/23), RB1–RB2 |
| B6 | Gravitational waves: 2 polarisations, speed $= c$ identically | THEOREM (given B2) | exact | `verify_gr_closure.py` T9 |
| B7 | Equivalence principle: inertial mass = gravitating mass (one field) | DERIVED-EFF | agreement $2\times10^{-4}$ on one packet | same, T12 |
| B8 | Schrödinger from the massive substrate mode (envelope reduction) | DERIVED-EFF | error $O(\epsilon^2)$, ratio 3.97 | same, T11 |
| B9 | Maxwell forced by the same uniqueness one rank down; charge conservation forced | THEOREM | null space $(1,-1,0)$ exact | same, T13 |
| B10 | Non-abelian consistency forces a Lie-algebra charge structure (su(2) passes $O(s^3)$; non-Jacobi fails at $O(s)$) | THEOREM (numeric, full uniqueness cited) | odd-part ratios 8.00 / 2.03 | `verify_crystal_forcing.py` YM1–YM2 |
| B11 | Gauge-group inventory $SU(3)\times SU(2)\times U(1)$ from the two arenas ($\mathrm{Der}(\mathbb O)=\mathfrak g_2$; clock stabiliser $=\mathfrak{su}(3)$; internal left $SU(2)$; clock $U(1)$) | THEOREM (structure only) | dims 14/8; su(3) identified | `verify_residual_closure.py` SM1–SM5 |
| B12 | Effective action of the collective metric is quadratic for any finite-moment mode statistics ($I'' = 1/\mathrm{Var}(x^2)$) | THEOREM (i.i.d. regime) | exact to $10^{-4}$ | same, RG1–RG3 |
| B13 | Continuum control: band exactness + eigenvalue rate $(3n^2{-}7)\theta^2/60$ + aliasing bound | THEOREM | explicit constants | same, RC1–RC3 |

## C. The measured numbers

| # | Claim | Status | Result | Verify / source |
|---|---|---|---|---|
| C1 | Proton radius $r_p = 4\bar\lambda_p$ | WITNESSED | 0.04% | `verify_hadron_radii.py`; proton-radius WO |
| C2 | b-anomaly: fixed-shape curve, sign-uniform across 5 datasets / 2 collaborations | TIE | 5/5 signs; statistically tied with conventional fit; documented analysis wobble | aria-closure-kernel §4 |
| C3 | Muon at cascade shell 96 = 24×4 | WITNESSED (structural claim, Paper LII) | offset $-0.0002$ shells (ppm in mass) | `cascade-masses.md` §E3 |
| C4 | Newton's constant $G = \hbar c/(m_\mu\varphi^{96})^2$ | CONDITIONAL (on C3 structural) | dev $-1.9\times10^{-4}$; look-elsewhere $p \approx 0.006$ | `verify_residual_closure.py` RGRAV1–2 |
| C5 | $\Omega_\Lambda = 0.6844$ from σ-paired complement | WITNESSED | $-0.083\%$ vs Planck | hypersphere-cosmology v1.1 (94/94) |
| C6 | $H_0 = 67.66$ | WITNESSED | $+0.45\%$ vs Planck | same |
| C7 | Z boson at shell 82 | WITNESSED (integer not derived) | offset $-0.049$ | `cascade-masses.md` §E3 |
| C8 | $\alpha^{-1} = 137 + \pi/87$ | CONDITIONAL (6-hypothesis stack) | — | alpha-chain docs |
| C9 | Muon $g{-}2$ cascade correction | CONDITIONAL | compatible either HVP scenario | paper-lii |

## D. The named open items (Chapter 12's list)

| # | Item | Status | Where recorded |
|---|---|---|---|
| D1 | (R-GH) Gromov–Hausdorff convergence of the arena geometry | OPEN (rigor-grade) | paper-xl T1–T2 |
| D2 | (R-corr) strongly-correlated substrate regime | OPEN (narrow) | residual-closure §2 |
| D3 | All-orders uniqueness of the gravity completion | CITED (Wald 1986) | residual-closure §1 |
| D4 | SM wiring: embedding/Weinberg angle, chirality, representations, couplings | OPEN | gauge-group-from-arenas §5 |
| D5 | Heavy shell integers (W/Z/H/top placements exist; integers not derived) | OPEN | cascade-masses §E3 |
| D6 | Neutrino placement | OPEN | book ch12 |
| D7 | Universal selection law | OPEN (deep) | narrative-gap-closure G9 |
| D8 | Experience / P-A | OPEN (deepest; explicitly unclaimed) | book ch12 |
| D9 | Derivation of shell 96 from the cascade (would unconditionalise C4) | OPEN | residual-closure §4 |

## E. Falsifiers on record

- Sharper b-anomaly data breaking the tie against the fixed-shape curve (C2).
- Any future derived mass meeting its measured value (no shape freedom).
- The conditional $G$ (C4): a derivation of shell 96 that then misses measured $G$ kills the anchor.
- JUNO mass ordering (window open ~2031–32) per the prospective-windows ledger.
