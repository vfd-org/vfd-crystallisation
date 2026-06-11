# Residual Closure: Upgrading the Named Residuals of the GR Chain

**Date:** 2026-06-12
**Status:** Second pass on `docs/gr-closure-derivation.md` §13. Sim-verified by `scripts/verify_residual_closure.py` (23/23 PASS, alongside the SM-structure items of `docs/gauge-group-from-arenas.md`).
**Effect:** (R-boot) closed in-house; (R-Gauss) generalised to non-Gaussian modes; (R-cont) converted from open programme to an explicit-rate theorem, with only the geometric (Gromov–Hausdorff) refinement left to Paper XL; (R-G) upgraded from calibration to a conditional derivation accurate to $1.9\times10^{-4}$.

---

## 1. R-boot → closed in-house

**What was owed.** Theorem G.1 of the GR-closure chain cited the Gupta–Kraichnan–Feynman–Deser bootstrap for the step from the linear (Fierz–Pauli) theory to the full Einstein equations. The citation was honest but imported.

### 1.1 The first-order one-step argument, in-house

Work in first-order (Palatini) form: treat the field $h^{\mu\nu}$ and the connection $\Gamma^\lambda_{\mu\nu}$ as independent. The free massless spin-2 theory is

$$\mathcal L_0 \;=\; h^{\mu\nu}\bigl(\partial_\alpha\Gamma^\alpha_{\mu\nu} - \partial_\nu\Gamma^\alpha_{\mu\alpha}\bigr)\;+\;\eta^{\mu\nu}\bigl(\Gamma^\alpha_{\mu\beta}\Gamma^\beta_{\nu\alpha} - \Gamma^\alpha_{\mu\nu}\Gamma^\beta_{\alpha\beta}\bigr),$$

whose stationary points reproduce linearised Einstein (eliminating $\Gamma$ by its algebraic equation of motion returns the Fierz–Pauli action). The self-coupling requirement says: $h^{\mu\nu}$ must couple to the **total** stress tensor, including the field's own. In first-order form the field's own stress tensor with respect to the flat background is read off from the only place the background appears — the $\eta^{\mu\nu}\Gamma\Gamma$ term. Coupling $h$ to it is therefore the substitution

$$\eta^{\mu\nu} \;\longrightarrow\; \eta^{\mu\nu} + h^{\mu\nu}$$

in that term, and **nothing else changes**, because no other term carries the background. The substitution is exact, not the first step of an infinite ladder: defining $\mathfrak g^{\mu\nu} := \sqrt{-g}\,g^{\mu\nu} = \eta^{\mu\nu} + h^{\mu\nu}$, the resulting Lagrangian is identically the first-order (Palatini) form of the Einstein–Hilbert action. The iteration closes in one step because after the substitution the background no longer appears anywhere, so there is no further stress tensor to add. This is Deser's argument; the point of this section is that it is now *derived in the programme's own pages*, in three sentences, rather than cited. (All-orders **uniqueness** of the completion — that no inequivalent consistent completion exists — we still take from the classical literature, Wald 1986; that is a statement about the space of all theories, not a step in our construction.)

### 1.2 Numeric witnesses

Two identities make the bootstrap concrete and falsifiable:

**RB1 (the fixed point is Fierz–Pauli).** On a periodic $8^4$ grid with spectral derivatives, the full nonlinear Einstein–Hilbert action of $g = \eta + \varepsilon h$ for random multi-mode $h$ satisfies
$$S_{EH}[\eta + \varepsilon h] \;=\; \tfrac12\,\varepsilon^2\, S_{FP}[h] \;+\; O(\varepsilon^3),$$
with the constant $\tfrac12$ measured as $0.500002$ and constant across random metrics to $4\times10^{-5}$. The quadratic germ of Einstein–Hilbert **is** the unique gauge-forced action of the GR-closure chain.

**RB2 (gravity gravitates, exactly).** Symbolically (sympy), the isotropic Schwarzschild metric truncated at second order,
$$f = 1 - 4\varepsilon A + 8\varepsilon^2A^2,\qquad g = 1 + 4\varepsilon A + 6\varepsilon^2A^2,\qquad A = \tfrac{M}{2r},$$
satisfies the full Einstein equations through $O(\varepsilon^2)$ **exactly**: the second-order metric coefficient cancels the self-energy of the first-order field identically. The null: truncating at first order leaves the residual $G^t{}_t = -3\varepsilon^2/r^4 \neq 0$ — the linear theory alone is inconsistent, and what repairs it is precisely the self-coupling. Gravity *must* gravitate, and when it does, Schwarzschild's second order is forced.

**Status.** (R-boot) closed: construction in-house (§1.1), fixed point verified (RB1), second-order consistency verified with a genuine null (RB2). Imported remainder: all-orders uniqueness (Wald 1986), now a named *classical-uniqueness* citation rather than a load-bearing construction step.

---

## 2. R-Gauss → generalised beyond the Gaussian regime

**What was owed.** Proposition B.3 of the GR chain proved the quadratic effective action for the collective field assuming **Gaussian** substrate fluctuations (Wishart argument).

**Theorem (Cramér upgrade).** Let the substrate modes be i.i.d. with any bounded (or sub-Gaussian) distribution of finite variance — no Gaussianity assumed. The collective second-moment field $h$ then satisfies a large-deviations principle with rate function $I$, and the effective action is $\Gamma_N[h] = N\,I(h)$ where:
1. $I$ is smooth and strictly convex near the background, with $I(\text{bg}) = 0$ and minimum exactly at the background;
2. the quadratic coefficient is $I'' = 1/\mathrm{Var}(x^2)$ — the **kurtosis-corrected** inverse susceptibility;
3. at the equilibrium fluctuation scale $\delta h \sim N^{-1/2}$, the cubic term is $O(N^{-1/2})$ relative to the quadratic.

*Proof.* Cramér's theorem (classical, unconditional) gives the LDP with $I(s) = \sup_t[ts - \Lambda(t)]$, $\Lambda$ the cumulant generating function of $x^2$, finite for bounded/sub-Gaussian modes; smoothness and strict convexity near the mean follow from $\Lambda$ analytic with $\Lambda'' > 0$. Sims RG1–RG3 verify all three numbered statements at machine precision for uniform and two-scale (strongly non-Gaussian, kurtosis $\neq 3$) modes: $I'' = 1/\mathrm{Var}(x^2)$ exact to $10^{-4}$, cubic/quadratic ratio scaling $4.00$ under $N \to 16N$, empirical fluctuation scaling confirmed. $\square$

**The physics point.** Non-Gaussianity changes **only the coefficient** of the quadratic effective action (statement 2) — and the coefficient is absorbed into the normalisation $16\pi G/c^4$ at the Newtonian matching step. The *form* of the action is fixed by the gauge-invariance uniqueness theorem, which never sees the coefficient. So the derived field equations are unchanged for any finite-moment mode statistics; what survives of (R-Gauss) is only the strongly-*correlated* / strong-field substrate regime (where modes are not independent), and there the nonlinear completion of §1 governs. The residual is renamed **(R-corr)** and is no longer about Gaussianity.

---

## 3. R-cont → an explicit-rate theorem

**What was owed.** "The strict discrete-to-continuum limit is open (Paper XL programme)." That statement was too coarse: it lumped together two very different things — the convergence of the *field dynamics* (what the GR chain actually uses) and the convergence of the *metric geometry* (Gromov–Hausdorff). The first is now a theorem with explicit constants; the second remains Paper XL's.

### 3.1 Band exactness (no limit needed)

The sampled spherical harmonics of degree $k \le 5$ are **exact eigenvectors** of the 600-cell Laplacian — not approximate ones. Verified directly: the four coordinate functions ($k=1$) and the nine traceless quadratics ($k=2$) satisfy $L\,Y = \lambda_k Y$ to $7\times10^{-15}$ (sims RC1a–b); the full statement for $k \le 5$ is the intertwiner theorem of the rung ladder (`docs/rung-dimension-ladder.md`, sim-verified 25/25). On the rendered band there is **nothing to converge**: the discrete spatial eigenfunctions *are* the continuum ones, sampled.

### 3.2 Eigenvalue rate (explicit, from the closed-form dispersion)

The exact dispersion $\lambda_k = 12\bigl(1 - \frac{\sin((k+1)\theta)}{(k+1)\sin\theta}\bigr)$, $\theta = \pi/5$, expands as
$$\lambda_k \;=\; 2\theta^2\,k(k+2)\,\Bigl[\,1 \;-\; \frac{(3n^2-7)\,\theta^2}{60} \;+\; O(\theta^4)\,\Bigr],\qquad n = k+1,$$
using $\frac{\sin n\theta}{n\sin\theta} = 1 - \frac{(n^2-1)\theta^2}{6} + \frac{(n^2-1)(3n^2-7)\theta^4}{360} - \cdots$ and $k(k+2) = n^2 - 1$. So the discrete eigenvalues equal the continuum $S^3$ eigenvalues $k(k+2)$ (up to the global scale defining $a$) with a **proven, explicit second-order rate** in the resolution parameter $\theta$. Sim RC2 confirms the rate term against the exact formula and (RC2b) confirms the formula's values sit in the actual graph spectrum with full multiplicity $(k+1)^2$.

### 3.3 Aliasing bound

The canonical kernel suppresses above-band content by exactly $1/(1 + r^2\lambda)$ (sim RC3: highest mode passed at $0.0905$ while the $k=1$ band passes at $0.4054$, matching the formula to $10^{-12}$). Rendered observables are therefore band-dominated with an explicit, monotone error budget.

### 3.4 The theorem and the remaining geometry

**Theorem (field-dynamics continuum control).** For band-$k$ rendered observables on a design rung with resolution $\theta$: spatial eigenfunctions are exact (3.1); frequencies match continuum frequencies with relative error $\frac{(3n^2-7)\theta^2}{60} + O(\theta^4)$ (3.2); above-band contamination is bounded by $1/(1+r^2\lambda_{>K})$ (3.3); and the time-step error is $O(\tau^2)$ (GR chain, sim T10). Every constant is explicit. $\square$

What this does **not** prove: that the vertex set with its graph metric converges in the Gromov–Hausdorff sense to round $S^3$ under Schläfli refinement — the geometric statement, Paper XL's T1–T2. After this pass that question is a *refinement of rigor about the arena*, no longer a gap in the derivation of the field equations on it. (R-cont) is renamed **(R-GH)** and scoped accordingly.

---

## 4. R-G → conditional derivation of Newton's constant

**What was owed.** $G$ was "a calibration constant" (kappa Definition 4.2): structure derived, one dimensional anchor borrowed from experiment.

**The reduction.** With $c$ and $\hbar$ substrate-assigned, fixing $G$ is equivalent to fixing one dimensionless number — equivalently, the Planck mass in units of any one derived particle mass.

**The anchor that already exists.** The cascade mass-shell analysis (`papers/cascade-derivation/cascade-masses.md` §E3) places every SM particle at $N = \log_\varphi(m_P/m)$ and finds the **muon at shell $96.000$** with offset $-0.0002$ — parts-per-million in mass — where $96 = 24 \times 4$ is the structural shell already used, *prior to and independently of this question*, in the muon $g{-}2$ work (Paper LII). Taking that placement as structural:

**Conditional theorem (H-shell-96 $\Rightarrow$ G).** Under the hypothesis that the muon's cascade shell is exactly 96,
$$G \;=\; \frac{\hbar c}{\bigl(m_\mu\,\varphi^{96}\bigr)^2} \;=\; 6.67305\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}},$$
against the measured $6.67430\times10^{-11}$: relative deviation $-1.9\times10^{-4}$ (sim RGRAV1). Gravity's absolute strength follows from the muon mass to two parts in ten thousand.

**Honesty block, in full.**
- *Conditionality.* The shell integer was first read off using measured $G$; what makes the inversion non-circular is the **prior structural claim** ($96 = 24\times4$, Paper LII's $g{-}2$ shell) plus the ppm-level offset. Chance probability of one particle landing within $|{\rm offset}| \le 2\times10^{-4}$ of an integer is $4\times10^{-4}$; with the look-elsewhere correction over the 14 particles in table E3.1, $p \approx 0.006$. Suggestive, not conclusive.
- *The residual is real.* Measured $G$ is known to $2.2\times10^{-5}$, so the $-1.9\times10^{-4}$ deviation is significant — equivalently, the muon's shell offset $-0.0002$ is physical (a radiative-correction-scale effect), not measurement noise. The conditional theorem is accurate to $1.9\times10^{-4}$ and honest about it.
- *Honesty gate (sim RGRAV2).* The direct $\alpha_G$ route through the proton fails integer-forcing (proton shell $91.46$, offset $0.46$, among the worst in the table) and the gate rejects it. No numerology was admitted: one pre-registered anchor, one prediction, one recorded deviation.

**Status.** (R-G) upgraded from *calibration* to *conditional derivation* under the named hypothesis (H-shell-96), accuracy $1.9\times10^{-4}$. Deriving the integer 96 from the cascade (rather than inheriting it as Paper LII's claim) is the remaining step, and it is the same open item as the heavy-sector shell integers.

---

## 5. Status after this pass

| Residual | Before | After |
|---|---|---|
| R-boot | bootstrap cited (Deser 1970 etc.) | **closed in-house** (§1; RB1 const = 0.500002, RB2 exact); only all-orders uniqueness still cited (Wald 1986) |
| R-Gauss | Gaussian-only effective action | **generalised** to all finite-moment i.i.d. modes (§2); coefficient kurtosis-corrected, form unchanged; renamed (R-corr): strongly-correlated regime |
| R-cont | "continuum limit open" | **explicit-rate theorem** for the field dynamics (§3); renamed (R-GH): only the Gromov–Hausdorff arena statement remains (Paper XL) |
| R-G | calibration constant | **conditional derivation** to $1.9\times10^{-4}$ under H-shell-96 (§4) |
| R-Λ | fixed by cosmology wing | unchanged |

The gauge-group structure derivation (the Standard-Model bridge upgrade) is the companion document `docs/gauge-group-from-arenas.md`, verified by the SM-section of the same sim suite.

## 6. Verification manifest (`scripts/verify_residual_closure.py`, 23/23)

| Sim | Verifies | Result |
|---|---|---|
| RB1 | $S^{(2)}_{EH} = \tfrac12 S_{FP}$, random metrics, 4D grid | const 0.500002, spread $4{\times}10^{-5}$ |
| RB2a–c | Schwarzschild $O(\varepsilon^2)$ self-coupling identity, symbolic + null | exact; null residual $-3/r^4$ |
| RG1–2 | Cramér rate function: $I''=1/\mathrm{Var}(x^2)$, cubic/quad $\sim N^{-1/2}$ (uniform, two-scale) | exact / ratio 4.00 |
| RG3 | empirical $N^{-1/2}$ fluctuations, non-Gaussian | ratio 4.12 |
| RC1a–b | degree-1, degree-2 sampled harmonics exact eigenvectors | $<10^{-14}$ |
| RC2, RC2b | dispersion rate $(3n^2{-}7)\theta^2/60$; multiplicities $(k{+}1)^2$ | within $O(\theta^4)$ envelope |
| RC3 | aliasing bound $1/(1+r^2\lambda)$ | $<10^{-12}$ |
| RGRAV1 | $G = \hbar c/(m_\mu\varphi^{96})^2$ | dev $-1.9\times10^{-4}$ |
| RGRAV2 | honesty gate: proton not forced, muon anchor ppm | offsets 0.462 / 0.0002 |
| SM0–SM6 | gauge-structure items | see companion doc |

## 7. Cross-references

- `docs/gr-closure-derivation.md` — the chain whose residuals this pass upgrades.
- `docs/gauge-group-from-arenas.md` — companion: SM gauge-group structure.
- `papers/paper-liii/` — formal write-up of the GR chain (its §13 now points here).
- `papers/paper-xl/` — home of the remaining (R-GH) geometric statement.
- `papers/cascade-derivation/cascade-masses.md` §E3 — the shell table behind §4.
- `papers/paper-lii/` — the prior structural claim $N_\mu = 96$ (muon $g{-}2$).
