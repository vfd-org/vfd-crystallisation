# Experimental Design Specifications for VFD Crystallisation Signatures

## Overview

This document specifies five candidate experiment classes for testing the
crystallisation operator against competing models. Each experiment defines system
type, control variables, observables, expected signatures, and falsification criteria.

---

## Experiment Class 1 — Qubit Repeated-Preparation Statistics (EP1)

### System
Superconducting transmon qubit with tunable coupling to measurement resonator.

### State Preparation
Prepare identical superposition $|\Psi\rangle = \alpha|0\rangle + \beta|1\rangle$
with fixed $|\alpha|^2, |\beta|^2$ across $N = 10{,}000$ trials.

### Control Variables
- Qubit-resonator coupling strength (constraint parameter)
- Measurement backaction strength
- Environmental temperature
- Pulse timing and amplitude (preparation fidelity)

### Observables
- Outcome distribution $\{N_0, N_1\}$
- Outcome entropy $H$
- Repeatability score $R$
- Transition time (measurement backaction to definite outcome)

### Expected VFD Signature
- $H < H_{\mathrm{Born}}$ under strong constraint coupling
- $R > R_{\mathrm{Born}}$ (more repeatable than Born-rule prediction)
- Transition time correlates with qubit-resonator constraint geometry

### Expected Non-VFD Signature
- $H = H_{\mathrm{Born}}$ within statistical error
- $R$ consistent with binomial expectation from $|c_k|^2$
- Transition time independent of constraint geometry details

### Discrimination Threshold
- KS test p-value < 0.01 on transition-time distribution comparison
- Permutation test p-value < 0.05 on repeatability difference

### Falsification Condition
$H$ and $R$ match Born-rule predictions across all tested coupling configurations.

### Number of Repeats
$N \geq 10{,}000$ per configuration; $\geq 5$ coupling configurations.

---

## Experiment Class 2 — Mesoscopic Basin-Preference Test (EP2/EP3)

### System
Ultracold atoms in a double-well optical potential with tunable barrier height
and well asymmetry.

### State Preparation
Prepare symmetric superposition across wells: equal population amplitudes.
Introduce controlled constraint asymmetry via:
- Barrier shape modification (constraint geometry)
- NOT well-depth modification (which changes amplitudes)

### Control Variables
- Barrier height and shape (constraint geometry)
- Well depths held equal (amplitudes unchanged)
- Atom number
- Temperature

### Observables
- Basin preference index $\mathrm{BPI}_k = N_k / N$ for each well
- Deviation from 50/50 expectation under symmetric amplitudes

### Expected VFD Signature
$\mathrm{BPI}_1 \neq \mathrm{BPI}_2$ when barrier geometry is asymmetric,
even with symmetric amplitudes. Basin preference correlates with constraint
geometry.

### Expected Non-VFD Signature
$\mathrm{BPI}_1 \approx \mathrm{BPI}_2 \approx 0.5$ since amplitudes are equal
(Born rule depends only on $|c_k|^2$).

### Discrimination Threshold
Binomial test on $\mathrm{BPI}$ deviation from 0.5 with $p < 0.001$.

### Falsification Condition
No measurable basin-preference deviation across all barrier geometries when
well depths (amplitudes) are held symmetric.

### Number of Repeats
$N \geq 5{,}000$ per barrier configuration; $\geq 8$ geometries.

---

## Experiment Class 3 — Transition-Time Scaling Measurement (EP1/EP4)

### System
Cavity QED: atom coupled to optical cavity mode. Tunable atom-cavity detuning
and coupling strength.

### State Preparation
Prepare atom-cavity entangled state. Vary:
- Cavity decay rate $\kappa$ (environment coupling $\Gamma$)
- Atom-cavity coupling $g$ (constraint strength)
- Detuning $\Delta$ (constraint geometry)

### Control Variables
- $\kappa$: environment coupling
- $g$: constraint coupling
- $\Delta$: detuning / constraint mismatch
- State preparation fidelity

### Observables
- Time from preparation to definite photon-number state (transition time $\tau$)
- $\tau$ as function of $(g, \kappa, \Delta)$

### Expected VFD Curve Shape
$$\tau \sim \frac{1}{a R(g, \Delta) + b Q + c B(\Delta) + d \kappa}$$

Multi-parameter structured scaling with identifiable contributions from constraint
terms beyond simple $1/\kappa$ decoherence.

### Expected Non-VFD Curve Shape
- Decoherence: $\tau \sim 1/\kappa$ (single-parameter, environment-dominated)
- GRW: $\tau$ independent of constraint geometry
- OR: $\tau \sim \hbar / \Delta E_G$

### Discrimination Logic
Fit transition-time data to:
1. Crystallisation model: $\tau = 1/(aR + bQ + cB + d\Gamma)$
2. Decoherence model: $\tau = A/\kappa$
3. GRW model: $\tau = 1/\lambda$

Compare AIC/BIC scores.

### Falsification Condition
$\tau$ data fits single-parameter decoherence model as well or better than
multi-parameter crystallisation model (AIC selects simpler model).

### Number of Repeats
$\geq 500$ trials per parameter point; $\geq 20$ points spanning $(g, \kappa, \Delta)$ space.

---

## Experiment Class 4 — Metastable Plateau Detection (EP4)

### System
Multimode optical cavity or superconducting resonator with programmable
mode structure.

### State Preparation
Prepare multimode superposition. Monitor mode populations continuously
via homodyne or heterodyne detection.

### Control Variables
- Number of modes (basin count)
- Mode coupling structure (constraint geometry)
- Cavity decay rate
- Initial mode population distribution

### Observables
- Mode population trajectories $n_k(t)$
- Functional trajectory $F(t)$ computed from populations
- Plateau detection: regions where $|dF/dt| < \epsilon$ for duration $> \delta$
- Dwell-time statistics at plateaus

### Expected VFD Signature
- Metastable plateaus in $F(t)$ before final mode selection
- Structured dwell times correlating with mode coupling geometry
- Plateau $F$-values correspond to metastable minima in constraint landscape

### Expected Non-VFD Signature
- Decoherence: smooth monotonic decay, no plateaus
- GRW: sudden jumps, no structured intermediates

### Discrimination Logic
Count plateau events. Compare plateau frequency and dwell-time distributions
against null (no plateaus expected under decoherence/GRW).

### Falsification Condition
No metastable plateaus observed in any tested multimode configuration where
the crystallisation model predicts them.

### Number of Repeats
$\geq 1{,}000$ trajectories per mode configuration; $\geq 4$ mode configurations.

---

## Experiment Class 5 — Coupled Oscillator Analog Demonstrator (EP5)

### System
Network of 8–32 coupled classical or semi-classical oscillators with programmable
coupling matrix. Implementations: electronic oscillator arrays, coupled pendula with
feedback, photonic mesh networks.

### State Preparation
Initialise in unstable multi-mode configuration (all modes excited, incoherent phases).
Program coupling matrix to define constraint landscape with known basin structure.

### Control Variables
- Coupling matrix (defines constraint geometry and basins)
- Initial amplitude/phase distribution
- Damping rate (environment coupling analog)
- Number of oscillators

### Observables
- End-state mode occupation (which basin the network converges to)
- Convergence time $\tau$
- Trajectory similarity across repeated identical initialisations
- Plateau detection in energy/functional trajectory
- Basin preference index

### Expected VFD Signature
- End-state selection matches crystallisation-functional minimum prediction
- $\tau$ scales with residual/coherence/boundary parameters as predicted
- High trajectory reproducibility from identical initial conditions
- Metastable plateaus in multi-basin landscapes
- Basin preference correlates with constraint geometry, not just initial amplitudes

### Expected Non-VFD Curve Shape
Standard coupled-oscillator theory predicts convergence to lowest-energy normal
mode. The crystallisation model may predict different basin selection when constraint geometry conflicts
with energy ordering.

### Discrimination Logic
1. Compute predicted basin from crystallisation functional minimisation.
2. Compute predicted basin from standard energy minimisation.
3. If these differ, measure which one the physical system selects.
4. Compare transition-time scaling to crystallisation and standard models.

### Falsification Condition
System always converges to standard energy minimum with no sensitivity to
constraint geometry modifications. Trajectory similarity no better than expected
from deterministic ODE with measurement noise.

### Number of Repeats
$\geq 100$ trials per coupling configuration; $\geq 10$ coupling matrices.

### Strategic Value
This is the **nearest-term demonstrator**. It does not require quantum-regime
operation. It directly tests the mathematical machinery of the crystallisation
operator in a physical system with real constraints, basins, and convergence dynamics.

---

## Summary

| Class | Platform | Primary Signature | Difficulty | Timeline |
|-------|----------|-------------------|-----------|----------|
| 1 | Qubit statistics | Outcome entropy, repeatability | Medium | 1–2 years |
| 2 | Cold atoms, double well | Basin preference | High | 2–3 years |
| 3 | Cavity QED | Transition-time scaling | Medium-High | 1–2 years |
| 4 | Multimode cavity | Metastable plateaus | Medium | 1–2 years |
| 5 | Coupled oscillators | Full crystallisation dynamics | Low | 3–6 months |

**Recommended starting point:** Experiment Class 5 (analog demonstrator), followed
by Class 1 (qubit statistics) and Class 4 (plateau detection).
