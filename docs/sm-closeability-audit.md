# Standard-Model Closeability Audit

**Date:** 2026-06-12
**Question answered:** of the items the papers honestly list as *not derived* — chirality, hypercharge, representations, couplings, masses, generations — which are closeable now, which are partially closeable, and which stay open with named reasons? And: can the framework's current Standard-Model content be simulated precisely?
**Deliverables of this pass:** two closures (chirality; charge quantization), one simulator (`scripts/sm_ledger.py`), this audit, Paper LVIII, and `scripts/verify_sm_structure.py` (11/11 PASS).

---

## 1. CLOSED THIS PASS (structure-grade, sim-verified)

### 1.1 Chirality — why the weak factor couples to one handedness

**The mechanism was already in the repository, unrecognised.** The arena's rotation group is $\mathrm{Spin}(4) = SU(2)_{\rm left} \times SU(2)_{\rm right}$ — and these factors are *literally* left and right quaternion multiplication. The frame split (Papers LIII/LVI, sims T14a–b) consumed the **right** factor as the scene's spatial rotations and identified the **left** factor as internal. The new observation: those two factors are exactly the two **chirality factors** of the 4D spin group. Fixing the complex structure $J = R_i$ (right multiplication by $i$), the quaternions become the 2-complex-dimensional **Weyl module**:

- every left multiplication commutes with $J$ and acts as $SU(2)$ on it — the standard $2I \hookrightarrow SU(2)$, verified for all 120 units (CH1–CH2);
- right (spatial) multiplication is $C$-linear **only** for the four units of the $i$-line — the spatial factor *cannot act* on the chiral module (CH3);
- the left action is the irreducible 2-dim rep (CH4).

**Consequence:** an internal $SU(2)$ inherited from the left factor acts on one Weyl sector only. *The weak interaction's handedness is the same fact as the frame split.* Caveats, stated: this is the Euclidean $\mathrm{Spin}(4)$ statement (the chiral split survives the standard continuation to $SL(2,\mathbb C)$, where the factors become $(\tfrac12,0)$/$(0,\tfrac12)$); and it derives why a left-factor gauge group is chiral — it does not construct the full electroweak fermion sector. **Status: CLOSED at structure grade.** (Paper LVIII §2.)

### 1.2 Electric charge — quantized in thirds, with the lepton/quark pattern

On the complexified octonions, with the **same clock unit $e_1$ and complex structure $J = L_{e_1}$** that Paper LVI used to break $G_2 \to SU(3)$: the six transverse units split into exactly three $J$-complex lines (Q0), and the three ladder operators built on them satisfy the **fermionic algebra exactly** (Q1). The number operator $N = \sum a_k^\dagger a_k$ has spectrum $\{0,1,2,3\}$ with multiplicities $\{1,3,3,1\}$ (Q2), so

$$Q = N/3 \in \{0, \tfrac13, \tfrac23, 1\},$$

— charge quantization in thirds — and the su(3) clock-stabiliser commutes with $N$, acting triplet-wise on the 3-dim charge eigenspaces and trivially on the 1-dim ones (Q3): the pattern of one neutral lepton, one charge-$\tfrac13$ colour triplet, one charge-$\tfrac23$ colour triplet, one charge-1 lepton. A genuine null (Q4): a non-$J$-compatible pairing destroys the integer spectrum. Classical precedent: Günaydin–Gürsey 1973; Furey 2016. The framework's addition is necessity at the input layer: this octonion algebra and this distinguished unit are the ones the arena theorems force. **Status: CLOSED at structure grade.** (Paper LVIII §3.)

### 1.3 Corollary: hypercharge as arithmetic

Given the derived $Q$ lattice and any doublet assignment, $Y = 2(Q - T_3)$ is fixed arithmetic. What remains genuinely open is hypercharge as an **independent gauge factor** (§3.1 below). The bookkeeping half of the hypercharge question is closed by 1.2.

## 2. SIMULATABLE NOW, WITH GRADED PRECISION (the masses question)

**Can we get all the Standard-Model masses precisely? Honest answer: no — and the framework can now say *exactly how far from yes* it is, with no fitting.** That is what `scripts/sm_ledger.py` does. Anchored only on the muon mass plus the structural shell $96 = 24\times4$ (H-shell-96), every particle's mass at its integer shell is the parameter-free number $m = m_\mu\varphi^{96-N}$:

| best today | typical | worst |
|---|---|---|
| muon exact (anchor), Z $-2.3\%$ | electron $+3.9\%$, up $+4.1\%$, tau $+6.7\%$, charm $-8.0\%$ | W $+10.8\%$, strange $+13$, Higgs $+15$, top $-17$, bottom $+19$, down/proton $+25\%$ |

The ladder (one $\varphi$ step per shell) is the framework's; the **integers** are currently read from data except the muon's; the **offsets** (up to half a shell $\approx 25\%$ in mass) are the open dynamical content — the framework's analogue of radiative corrections. The two named open derivations that would convert PLACED → DERIVED: (i) the shell-integer rule (why 96, 82, 81, …), and (ii) the offset dynamics.

**An observed offset pattern (recorded, not derived; n = 13).** Grouping the shell offsets by sector gives a clean monotone ordering of mean |offset|: leptons 0.071 (max 0.135) < electroweak bosons 0.184 < quarks 0.288 < composite (proton) 0.462. The ladder is sharpest exactly where "mass" is a clean physical observable (lepton pole masses, Z) and worst exactly where it is scheme-dependent or confinement-dressed (light quarks, proton). This is consistent with — and weak evidence for — the reading that offsets are interaction dressing on a geometric free spectrum, the framework's analogue of radiative corrections. It also yields a soft falsifiable expectation: cleanly-defined colour-singlet masses should sit nearer integer shells than scheme-dependent coloured ones. Recorded as an observation; thirteen points prove nothing. Until then, claiming "all masses from the framework" would be exactly the W5-trap our verification gate exists to kill. Neutrino masses are not even placed: **OPEN**.

## 3. STILL OPEN, WITH NAMED REASONS

1. **Independent hypercharge / Weinberg angle.** The derived $U(1)_{\rm clock}$ sits inside $SU(2)$; the SM's $U(1)_Y$ does not. The charge lattice (1.2) now constrains any future embedding, but the mixing itself — equivalently $\sin^2\theta_W$ — has no derivation; geometric candidate values are scheme-dependent and we will not numerology one.
2. **Generations = 3.** Named candidate, now on the record as a conjecture: the cascade's gravity rung is $D_4$, whose **triality** $S_3$ permutes three 8-dimensional representations (cascade-gr C1) — three copies of the same matter slot is exactly the right *shape*. Untested; no mechanism connecting triality orbits to family replication. **CONJECTURE.**
3. **Anomaly cancellation.** Arithmetic works out *if* standard assignments are adopted; not derived from the substrate.
4. **Running couplings $g_1, g_2, g_3$.** No derivation; the only contact points remain the conditional $\alpha$-chain ($137 + \pi/87$, 6-hypothesis stack) and the $C_\varphi$ response family.
5. **Shell integers + offsets** (the masses, per §2). The deepest of the SM opens; same item that would unconditionalise $G$. **First structured attack executed (WO-SHELL-OFFSET-001, `docs/shell-rule-wo.md`, 8/8 machine-checked):** the entire class "static quantum numbers + universal generation dependence" is *refuted at proof grade* (curvature obstruction: (5, 3, −2) distinct), per-type linear rules fail, cascade-residue patterns are null after look-elsewhere, simple log dressing is excluded within leptons, and a sector-limited offset-structure correlation (in-sample R² 0.86) *failed its boson out-of-sample test* and is recorded as a lead, not a law. The surviving routes: the dynamical one (blocked behind the couplings item — consistent with the integers not factoring through static quantum numbers) and the pole-mass reformulation (cheap; a falsifiable sharpening expectation is on record).
6. Unchanged from before: (R-GH), (R-corr), the universal selection law, experience.

## 4. What moved, in one line each

- Chirality: **OPEN → CLOSED (structural)** — the weak factor is chiral because it is the left factor.
- Charge quantization + multiplet pattern: **OPEN → CLOSED (structural)** — thirds from the clock unit's ladder algebra.
- Hypercharge: **OPEN → half-closed** (bookkeeping arithmetic fixed; independent gauging open).
- Masses: **OPEN → GRADED** (parameter-free simulator with explicit per-particle error; muon/Z sharp, tail at ~25%).
- Generations: **unlisted → NAMED CONJECTURE** (D₄ triality).

## 5. Verification

`scripts/verify_sm_structure.py` — 11/11 PASS (CH1–CH4, Q0–Q4). Simulator: `scripts/sm_ledger.py` (no adjustable parameters; prints its own grades). Paper form: `papers/paper-lviii/`.
