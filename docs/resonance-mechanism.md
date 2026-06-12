# How the Crystal Resonates: the Mass-as-Closure-Frequency Mechanism

**Date:** 2026-06-12
**Purpose:** the mechanism answer to "what drives the crystal's resonances to produce the particles and their weights, and how do atoms follow?" — with each link graded derived / open. Companion to `docs/shell-rule-wo.md` (which constrains the open link) and `scripts/sm_ledger.py`.

---

## 1. The chain, link by link

**Link 1 — The crystal's resonant spectrum at one scale: DERIVED, exact.**
The 600-cell's vibration spectrum is closed-form and machine-verified:
$$\lambda_k = 12\Bigl(1 - \frac{\sin((k{+}1)\pi/5)}{(k{+}1)\sin(\pi/5)}\Bigr), \qquad k = 0..5,$$
with multiplicities $(k+1)^2$ — the harmonics of a 3-sphere, at machine precision (Paper LV; `verify_rendering_layer.py`). This is *how the crystal rings at a fixed grain*. These spatial harmonics give fields their **shapes** (and read off the dimension of space); they are not yet particle masses.

**Link 2 — Mass = closure frequency: DERIVED as the identification, exact as kinematics.**
A particle is a localized mode that *closes on itself* — a standing wave of the substrate. Its rest frequency $\omega_0$ **is** its mass ($m = \hbar\omega_0/c^2$), and this is not an analogy in the framework: the massive end of the response family $C_\varphi = L + \varphi^{-2}I$ gives modes obeying $(\Box - \mu^2)F = 0$ with $\mu = \varphi^{-1}$ — the rest frequency is set by the **coherence length at which the mode closes**. The same identification was verified dynamically: the envelope of such a mode obeys the Schrödinger equation with exactly that mass, and its inertia equals its gravitating energy on one simulated wavepacket (Paper LIII, items T11–T12).

**Link 3 — Why the ladder is golden: DERIVED from the refinement tower.**
The substrate is $\varphi$-self-similar: the refinement tower rescales the geometry by one factor of $\varphi$ per level (the cosmogenesis multi-shell refinement; the rung ladder). A mode that closes at depth $N$ of the tower therefore closes at coherence length $\propto \varphi^{N}$ and rest frequency
$$m(N) \;=\; m_P\,\varphi^{-N}.$$
One golden step per level — this is *why* the mass ladder is geometric in $\varphi$, and it is the part of the "weights" question that is already derived. The muon sits on it at parts-per-million; the Z at 2.3%.

**Link 4 — Which depths host which particles: OPEN, and now precisely fenced.**
This is the shell-integer rule — the analogue of "which orbits close" in the old quantum theory. What WO-SHELL-OFFSET-001 established about this link:
- it is **not** a function of the static quantum numbers (charge, colour, chirality, generation) — refuted at proof grade (the curvature obstruction);
- it is **not** any of eight natural geometric/prime sieves (all null after correction; the sieve *class* remains live, with the GL3 target: a derived level set hitting all nine shells at density ≤ 1/3);
- it behaves exactly like an **interacting** closure condition: the standing-wave selection depends on the mode's self-interaction, which is the coupling sector. Dependency order: **couplings → closure selection → shell integers → offsets → precise masses.**
So "what drives the resonance selection" has a definite answer-shape: the closure condition of the interacting flow on the tower — a computation the programme can specify but cannot yet run, because the couplings are not derived. Not primes; dynamics.

**Link 5 — From particles to atoms: DERIVED CHAIN (standard physics on derived equations).**
Once a mode has a mass, a charge, and obeys the Schrödinger equation, *everything atomic follows by ordinary quantum mechanics* — and every ingredient of that sentence is now in the derived layer: Schrödinger (Paper LIII, envelope reduction), Maxwell/Coulomb (Paper LIII, uniqueness scan), the charge lattice in thirds (Paper LVIII), chirality (Paper LVIII), and gravity for the large-scale binding (Papers LIII/LVII). Hydrogen's spectrum, the Bohr radius, chemistry's shell structure — none of these needs a new framework derivation; they are theorems of the already-derived equations given the mass and coupling inputs. The ledger (`sm_ledger.py`, atoms section) prints the standard chain: $E_n = -\tfrac{\alpha^2 m_e c^2}{2n^2}$ with the framework's conditional $\alpha$ and placed $m_e$.

## 2. The honest summary sentence

The crystal's resonance *mechanism* is derived end-to-end — exact spectrum at fixed grain, mass = closure frequency, golden ladder from the refinement tower, and standard atomic physics downstream — with exactly **one** link open in the middle: the interacting closure-selection condition that picks the integer depths (and dresses them). That link is fenced on three sides: not static quantum numbers (proof), not the tested sieves (nulls with a quantitative door), and blocked behind the coupling sector (the genuine frontier).

## 3. What would close Link 4

1. **Derive the couplings** (the named open), then compute the self-interaction correction to the closure condition — the framework's Lamb-shift analogue — and the selected depths fall out as the spectroscopy of the interacting flow.
2. **Or** derive a new intermediate-geometry level set (finer Schläfli strata; new resonance levels from the pentagonal-clock instrument) blind to the shell table and score it once against GL3 (all nine shells, density ≤ 1/3).
3. **First, cheaply:** reformulate the shell table against pole/physical masses only — the scheme-dependence gradient (leptons 0.071 < EW 0.184 < quarks 0.288 < composite 0.462) predicts the reformulated table sharpens. Falsifiable; on record.

## 4. Cross-references

Paper LV (spectrum), LIII §11 (mass identification, T11–T12), LVII §4 (the conditional Planck anchor), LVIII (charges/chirality), `docs/shell-rule-wo.md` (the fence around Link 4), `scripts/sm_ledger.py` (the graded outputs).
