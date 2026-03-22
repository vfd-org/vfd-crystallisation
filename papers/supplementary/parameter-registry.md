> **Note:** These documents describe proposed mappings between the crystallisation formalism and experimental systems. They are intended as guidance for implementation and testing, not as established physical identifications.

# VFD Crystallisation Operator -- Parameter Registry

This document provides a reference for every model parameter
in the crystallisation operator. All notation, ranges, units, and
estimation guidance used elsewhere in the paper and supplementary
materials should be consistent with the definitions given here.

The experimental proxies described here are heuristic mappings intended to guide implementation rather than exact physical identifications.

Canonical parameter vector:

    Theta = (alpha, beta, gamma, lambda, eta, Gamma, R_c, kappa_B, kappa_Q)

---

## Summary Table

| # | Symbol   | Name                        | Units       | Range          | Dimensionless? | Estimation        |
|---|----------|-----------------------------|-------------|----------------|----------------|-------------------|
| 1 | alpha    | Residual weight             | --          | [0.01, 10]     | Yes            | Fit / grid search |
| 2 | beta     | Energy weight               | --          | [0.01, 10]     | Yes            | Fit / grid search |
| 3 | gamma    | Coherence weight            | --          | [0.01, 10]     | Yes            | Fit / grid search |
| 4 | lambda   | Crystallisation drive       | 1/time      | [0.01, 10]     | No             | Spectral analysis |
| 5 | eta      | Relaxation rate             | 1/time      | [0.0001, 0.1]  | No             | Decay fitting     |
| 6 | Gamma    | Environment coupling        | 1/time      | [0, 5]         | No             | T1/T2 extraction  |
| 7 | R_c      | Critical residual threshold | --          | [0, 5]         | Yes            | Threshold scan    |
| 8 | kappa_B  | Boundary mismatch scaling   | --          | [0.1, 5]       | Yes            | Geometry matching |
| 9 | kappa_Q  | Coherence response scaling  | --          | [0.1, 5]       | Yes            | Coherence sweep   |

All dimensionless quantities are pure numbers. All dimensional quantities
carry units of inverse time; when connecting to a specific platform the
natural frequency scale omega_0 of that platform sets the conversion
factor (see Rescaling Conventions below).

---

## 1. alpha -- Residual Weight

**Symbol:** alpha

**Name:** Residual weight

**Meaning:**
Multiplicative coefficient in front of the residual (constraint-mismatch)
term in the crystallisation potential. A larger alpha penalises states
that violate the target constraint geometry more heavily, steering the
dynamics toward configurations that satisfy the boundary conditions before
optimising energy or coherence.

**Units / dimensionality:**
Dimensionless. Because alpha multiplies a term that already carries the
dimensions of the potential (energy), it is a pure weighting factor. No
unit conversion is needed across platforms.

**Allowed range:** [0.01, 10]

The lower bound avoids numerical irrelevance of the constraint term; the
upper bound prevents the residual from dominating the potential to the
point where energy and coherence terms are effectively switched off.

**Physical interpretation:**
alpha sets the relative stiffness of the constraint surface. In a
mechanical analogy, raising alpha behaves similarly to tightening the springs
that pull the system toward the constraint manifold. In the limit
alpha -> infinity the dynamics approach projection onto the
constraint surface; in the limit alpha -> 0 constraints are ignored.

**Typical experimental proxy:**
The ratio of the constraint violation at late times to its initial value.
If that ratio does not decrease monotonically during a run, alpha is
likely too small relative to beta and gamma.

**Estimation method:**
Directly set by the experimenter or determined via grid search / Bayesian
optimisation over the triple (alpha, beta, gamma). Not independently
measurable from a single time trace.

**Platform notes:**

- *Qubit (superconducting / trapped-ion):* Maps to the weight given to
  syndrome-measurement feedback in an error-correction cycle. Increasing
  alpha corresponds to more aggressive correction.
- *Cold atom:* Maps to the depth of the optical-lattice potential that
  enforces the target spatial geometry.
- *Cavity QED:* Proportional to the mirror reflectivity that enforces
  standing-wave boundary conditions.
- *Analog oscillator:* Proportional to the gain of the feedback loop that
  drives the oscillator toward the target amplitude envelope.

---

## 2. beta -- Energy Weight

**Symbol:** beta

**Name:** Energy weight

**Meaning:**
Multiplicative coefficient on the energetic cost term. Controls how
strongly the dynamics penalise high-energy configurations. A larger beta
biases the system toward low-energy states at the possible expense of
satisfying constraints or maintaining coherence.

**Units / dimensionality:**
Dimensionless. Same reasoning as alpha: it multiplies a term already
carrying energy dimensions.

**Allowed range:** [0.01, 10]

**Physical interpretation:**
beta plays the role of an inverse temperature in the crystallisation
landscape. Large beta sharpens the energy wells, making the system more
sensitive to energetic differences between candidate configurations.
Small beta flattens the landscape and allows the dynamics to explore
higher-energy states.

**Typical experimental proxy:**
The mean energy of the system at late times, normalised by the known
ground-state energy. If the normalised energy is far above unity, beta
may need to be increased.

**Estimation method:**
Set jointly with alpha and gamma via grid search or Bayesian optimisation.
Can also be estimated from the slope of the energy decay curve in the
early transient phase.

**Platform notes:**

- *Qubit:* Corresponds to the weighting of the cost Hamiltonian in a
  variational or annealing schedule.
- *Cold atom:* Maps to the effective temperature of the atomic cloud;
  lower temperature corresponds to higher effective beta.
- *Cavity QED:* Related to the photon-number penalty in the cavity
  Hamiltonian.
- *Analog oscillator:* Proportional to the resistive damping coefficient
  that dissipates excess energy.

---

## 3. gamma -- Coherence Weight

**Symbol:** gamma

**Name:** Coherence weight

**Meaning:**
Multiplicative coefficient on the coherence reward term. A positive gamma
rewards states with high phase alignment (off-diagonal density-matrix
elements), encouraging the system to maintain or build quantum coherence
during the crystallisation process.

**Units / dimensionality:**
Dimensionless.

**Allowed range:** [0.01, 10]

**Physical interpretation:**
gamma measures how much the operator values coherent superposition
relative to classical mixture. When gamma >> alpha, beta the dynamics
will sacrifice constraint satisfaction and energy minimisation in order
to preserve coherence. This regime is relevant for protocols that must
maintain entanglement during the crystallisation window.

**Typical experimental proxy:**
Visibility of Ramsey or spin-echo fringes at the crystallisation
endpoint. High visibility indicates that the coherence reward is
effectively competing with decoherence and energetic relaxation.

**Estimation method:**
Set jointly with alpha and beta. Independent calibration is possible by
running the dynamics with alpha = beta = 0 and fitting the coherence
decay/growth rate.

**Platform notes:**

- *Qubit:* Directly related to the off-diagonal elements of the density
  matrix in the computational basis; gamma weights how strongly these
  elements feed back into the drive.
- *Cold atom:* Maps to the contrast of matter-wave interference fringes.
- *Cavity QED:* Proportional to the weight given to homodyne/heterodyne
  measurement records in the feedback loop.
- *Analog oscillator:* Related to the quality factor Q of the oscillator;
  higher Q sustains coherent oscillation longer.

---

## 4. lambda -- Crystallisation Drive Strength

**Symbol:** lambda

**Name:** Crystallisation drive strength

**Meaning:**
Overall coupling constant for the crystallisation interaction term in the
equations of motion. lambda sets the rate at which the crystallisation
potential reshapes the state. It is the single most important parameter
for determining whether crystallisation occurs within the available
experimental time window.

**Units / dimensionality:**
Dimensional: units of 1/time (inverse seconds in SI, or multiples of the
platform natural frequency omega_0 in natural units).

Conversion: lambda_SI = lambda * omega_0.

**Allowed range:** [0.01, 10] (in units of omega_0)

**Physical interpretation:**
lambda is the crystallisation rate constant. It plays a role analogous to
the reaction rate in chemical kinetics or the gap in adiabatic quantum
computation. If lambda is too small the system does not crystallise within
the protocol duration; if lambda is too large the dynamics become stiff
and may overshoot, generating defects.

**Typical experimental proxy:**
The inverse of the time at which the order parameter (e.g., structure
factor peak, entanglement witness) first reaches half its saturation
value. A quick half-rise implies large lambda.

**Estimation method:**
Extracted from the early-time exponential growth rate of the
crystallisation order parameter. Fit the order parameter O(t) to
O(t) ~ exp(lambda * t) in the linear-response regime.

**Platform notes:**

- *Qubit:* Maps to the effective coupling strength between qubits
  mediated by the control Hamiltonian.
- *Cold atom:* Proportional to the s-wave scattering length times the
  density, which sets the interaction energy scale.
- *Cavity QED:* Equal to the vacuum Rabi frequency g when the cavity
  mediates the crystallisation interaction.
- *Analog oscillator:* Proportional to the nonlinear coupling coefficient
  in the oscillator network.

---

## 5. eta -- Relaxation Rate

**Symbol:** eta

**Name:** Relaxation rate

**Meaning:**
Effective damping or gradient-descent step size for the dissipative part
of the dynamics. eta controls how quickly the system loses memory of its
initial conditions and settles toward the crystallisation fixed point.

**Units / dimensionality:**
Dimensional: units of 1/time.

Conversion: eta_SI = eta * omega_0.

**Allowed range:** [0.0001, 0.1] (in units of omega_0)

The small upper bound reflects the fact that the relaxation should be
slow compared to the coherent dynamics (lambda, Gamma) to avoid
overdamping the crystallisation process.

**Physical interpretation:**
eta is the friction coefficient of the crystallisation landscape. In the
Langevin picture, it sets the drift velocity down the potential gradient.
Too large an eta overdamps the coherent oscillations that are essential
for phase-aligned crystallisation; too small an eta means the system
never reaches the fixed point within the protocol window.

**Typical experimental proxy:**
The 1/e decay time of the energy or residual after the initial transient.
tau_relax = 1/eta.

**Estimation method:**
Fit the late-time exponential tail of the energy or residual time trace.
Alternatively, extract from the linewidth of a spectral peak associated
with the crystallisation mode.

**Platform notes:**

- *Qubit:* Related to the T1 (energy relaxation) rate of the qubits, but
  modified by any engineered dissipation channels.
- *Cold atom:* Set by the optical-molasses cooling rate or evaporative
  cooling rate.
- *Cavity QED:* Equal to the cavity decay rate kappa when the cavity is
  the dominant dissipation channel.
- *Analog oscillator:* Proportional to the ohmic resistance in the
  circuit.

---

## 6. Gamma -- Environment Coupling

**Symbol:** Gamma (capital)

**Name:** Environment coupling strength

**Meaning:**
Rate of decoherence and noise injection from the environment. Gamma
quantifies the unavoidable interaction between the system and its thermal
or electromagnetic surroundings. It competes with gamma (coherence weight)
and lambda (crystallisation drive): if Gamma is too large relative to
these, the system decoheres before crystallisation can complete.

**Units / dimensionality:**
Dimensional: units of 1/time.

Conversion: Gamma_SI = Gamma * omega_0.

**Allowed range:** [0, 5] (in units of omega_0)

Gamma = 0 corresponds to a perfectly isolated system (unitary dynamics).
The upper bound represents a strongly coupled, open-system regime.

**Physical interpretation:**
Gamma is the decoherence rate. It sets the timescale on which off-diagonal
density-matrix elements decay in the absence of any coherence-preserving
drive. The ratio lambda/Gamma is a figure of merit: crystallisation is
feasible only when lambda/Gamma >> 1 (or at least of order unity, if the
threshold form with R_c is active).

**Typical experimental proxy:**
The T2 (dephasing) time of the platform: Gamma ~ 1/T2. More precisely,
Gamma is extracted from a Ramsey or spin-echo decay measurement in the
absence of the crystallisation drive.

**Estimation method:**
Directly measured from standard decoherence benchmarking protocols
(Ramsey decay, spin echo, randomised benchmarking). This is typically the
best-characterised parameter in any quantum platform.

**Platform notes:**

- *Qubit:* Gamma = 1/T2 (or a weighted combination of 1/T1 and pure
  dephasing 1/T_phi depending on the noise model).
- *Cold atom:* Set by photon scattering from trapping lasers and
  background-gas collisions.
- *Cavity QED:* Sum of cavity loss rate and atomic spontaneous emission
  rate.
- *Analog oscillator:* Thermal noise power spectral density divided by
  the oscillator energy scale.

---

## 7. R_c -- Critical Residual Threshold

**Symbol:** R_c

**Name:** Critical residual threshold

**Meaning:**
Threshold value of the residual (constraint mismatch) below which the
crystallisation term activates. Used in the threshold form of the
crystallisation operator, where the drive lambda is gated by a step or
sigmoid function of the residual: the system must first approximately
satisfy constraints before the crystallisation interaction switches on.

**Units / dimensionality:**
Dimensionless. R_c is measured in the same units as the residual itself,
which is normalised to be dimensionless.

**Allowed range:** [0, 5]

R_c = 0 means the crystallisation term is always active (no threshold
gating). R_c > 0 introduces a two-stage dynamics: constraint satisfaction
first, then crystallisation.

**Physical interpretation:**
R_c sets the "readiness" criterion for crystallisation. Physically, it
ensures that the system has settled close enough to the constraint
manifold before the nonlinear crystallisation interaction is applied.
This prevents the drive from amplifying configurations that are far from
the target geometry.

**Typical experimental proxy:**
The value of the constraint violation metric at the time when the order
parameter begins to grow. If the order parameter starts growing only
after the residual drops below a certain value, that value is an
empirical estimate of R_c.

**Estimation method:**
Inferred from the time-trace data. Plot the residual and the order
parameter on the same time axis; R_c is the residual value at the onset
of order-parameter growth. Can also be set a priori based on the desired
precision of constraint satisfaction.

**Platform notes:**

- *Qubit:* Maps to the syndrome weight threshold below which the
  error-correction cycle is considered "good enough" and the next stage
  of the protocol begins.
- *Cold atom:* Corresponds to the temperature threshold below which
  long-range order can nucleate.
- *Cavity QED:* Related to the intracavity photon-number variance
  threshold for mode locking.
- *Analog oscillator:* The amplitude-error threshold below which
  injection locking engages.

---

## 8. kappa_B -- Boundary Mismatch Scaling

**Symbol:** kappa_B

**Name:** Boundary mismatch scaling

**Meaning:**
Dimensionless prefactor that rescales the target constraint geometry
before it enters the residual calculation. kappa_B adjusts how tightly
the boundary conditions are imposed: larger kappa_B amplifies the
mismatch signal, making the dynamics more sensitive to deviations from
the target geometry.

**Units / dimensionality:**
Dimensionless.

**Allowed range:** [0.1, 5]

**Physical interpretation:**
kappa_B controls the effective "zoom level" on the constraint surface. A
large kappa_B magnifies small deviations, tightening the constraint; a
small kappa_B relaxes it. In the geometric picture, kappa_B rescales the
metric on the constraint manifold.

**Typical experimental proxy:**
The ratio of the measured boundary mismatch to the theoretically expected
mismatch for a known reference state. If the measured value is
consistently off by a multiplicative factor, that factor estimates
kappa_B.

**Estimation method:**
Derived from calibration runs using states with known boundary properties.
Prepare a state with a known residual, measure the actual residual
reported by the apparatus, and take the ratio.

**Platform notes:**

- *Qubit:* Scales the syndrome extraction operator. A larger kappa_B
  corresponds to higher-weight stabiliser measurements.
- *Cold atom:* Proportional to the lattice depth that defines the
  boundary of the trapping region.
- *Cavity QED:* Scales the mirror reflectivity or finesse, controlling
  how sharply the cavity boundary conditions are imposed.
- *Analog oscillator:* Proportional to the impedance mismatch at the
  boundary of the oscillator network.

---

## 9. kappa_Q -- Coherence Response Scaling

**Symbol:** kappa_Q

**Name:** Coherence response scaling

**Meaning:**
Dimensionless prefactor that scales how sensitively the crystallisation
dynamics respond to changes in coherence. A large kappa_Q means that
small changes in the coherence measure produce large changes in the
effective potential, amplifying the feedback between coherence and
crystallisation.

**Units / dimensionality:**
Dimensionless.

**Allowed range:** [0.1, 5]

**Physical interpretation:**
kappa_Q sets the gain of the coherence feedback loop. When kappa_Q is
large the system is in a "coherence-sensitive" regime where even small
dephasing events cause significant adjustments to the crystallisation
drive. When kappa_Q is small, the dynamics are relatively insensitive to
coherence fluctuations.

**Typical experimental proxy:**
The slope of the order-parameter growth rate as a function of the
measured coherence (e.g., fringe visibility). A steep slope indicates
large kappa_Q.

**Estimation method:**
Derived from a coherence sweep: run the crystallisation protocol at
several values of the initial coherence (controlled, e.g., by varying
the dephasing time before the protocol starts) and fit the dependence
of the crystallisation rate on initial coherence. The slope of that fit,
normalised appropriately, gives kappa_Q.

**Platform notes:**

- *Qubit:* Maps to the sensitivity of the control Hamiltonian to the
  off-diagonal density-matrix elements, often set by the Rabi frequency
  of the coherence-probing drive.
- *Cold atom:* Related to the contrast transfer function of the imaging
  system used to measure interference fringes.
- *Cavity QED:* Proportional to the homodyne detection efficiency, which
  sets how precisely coherence is monitored in real time.
- *Analog oscillator:* Related to the gain of the phase-sensitive
  amplifier in the feedback loop.

---

## Parameter Correlations and Degeneracies

The nine parameters are not all independently identifiable from a single
experiment. The following correlations and degeneracies must be kept in
mind when fitting or optimising.

### Weight-triple degeneracy (alpha, beta, gamma)

Only the ratios alpha:beta:gamma are physically meaningful. Multiplying
all three by the same constant c rescales the overall potential but does
not change the dynamics (the equations of motion depend on gradients of
the potential, and a global rescaling is absorbed by eta). Convention:
fix alpha + beta + gamma = 1 when reporting fitted values, or
equivalently report the two independent ratios beta/alpha and
gamma/alpha.

### Drive-damping ratio (lambda / eta)

The crystallisation dynamics depend primarily on the ratio lambda/eta,
not on the individual values. A fast drive with fast damping can
behave similarly to a slow drive with slow damping. When both lambda and eta
are free parameters, report the ratio and one absolute scale.

### Decoherence competition (lambda / Gamma)

The feasibility of crystallisation is controlled by lambda/Gamma. This
ratio is analogous to the cooperativity parameter in cavity QED or the
ratio of coherent coupling to decay rates in any open quantum system.
Crystallisation requires lambda/Gamma > 1 in most regimes.

### Threshold-drive coupling (R_c, lambda)

When using the threshold form, R_c and lambda are partially degenerate:
a higher R_c with a stronger lambda can produce the same onset time as a
lower R_c with a weaker lambda. Break this degeneracy by independently
measuring the residual at crystallisation onset.

### Scaling-pair correlation (kappa_B, kappa_Q)

kappa_B and kappa_Q both act as gain factors and can partially compensate
each other. If the boundary mismatch and coherence response enter the
potential through a sum, only kappa_B + kappa_Q (or a weighted
combination) is identifiable without additional structure. Independent
identification requires experiments that vary boundary conditions and
coherence independently.

---

## Rescaling Conventions

### Natural units

All dimensional parameters (lambda, eta, Gamma) are expressed in units
of the platform natural frequency omega_0:

    lambda_natural = lambda_SI / omega_0
    eta_natural     = eta_SI / omega_0
    Gamma_natural   = Gamma_SI / omega_0

This convention makes the parameter ranges platform-independent. The
allowed ranges listed above are in natural units.

### Platform frequency scales

| Platform              | omega_0 (typical)       | Notes                           |
|-----------------------|-------------------------|---------------------------------|
| Superconducting qubit | 2*pi * 5 GHz            | Qubit transition frequency      |
| Trapped ion           | 2*pi * 10 MHz           | Motional mode frequency         |
| Cold atom (lattice)   | 2*pi * 50 kHz           | Band gap of optical lattice     |
| Cavity QED            | 2*pi * 1 GHz            | Cavity free spectral range      |
| Analog oscillator     | 2*pi * 1 kHz -- 1 MHz   | LC resonance frequency          |

### Time convention

Time is measured in units of 1/omega_0. A "crystallisation time" of
tau_crys = 100 means 100 oscillation periods of the platform.

### Energy convention

Energies are measured in units of hbar * omega_0 (quantum platforms) or
k_B * T_ref (classical analog platforms), where T_ref is a reference
temperature set by the noise floor.

---

## Derived Quantities

The following quantities are not independent parameters but are computed
from the canonical parameter vector Theta. They appear frequently in
the analysis and are defined here for reference.

### Crystallisation timescale (tau_crys)

    tau_crys = 1 / (lambda * f(alpha, beta, gamma))

where f is a dimensionless function of the weight triple that depends on
the specific form of the potential. In the simplest (linear) case,
f = alpha. tau_crys sets the experimental protocol duration: the system
must be held coherent for at least a few tau_crys.

### Critical threshold (Lambda_c)

    Lambda_c = Gamma / (gamma * kappa_Q)

The minimum value of lambda at which the crystallisation drive can
overcome decoherence, given the coherence weight and response scaling.
Crystallisation is possible only when lambda > Lambda_c. This is the
central feasibility criterion.

### Effective cooperativity (C_eff)

    C_eff = lambda^2 / (eta * Gamma)

Dimensionless figure of merit analogous to the cooperativity in cavity
QED. C_eff >> 1 indicates that coherent crystallisation dominates over
dissipative and decoherent processes. C_eff < 1 signals a regime where
the environment wins.

### Constraint satisfaction timescale (tau_constraint)

    tau_constraint = 1 / (eta * alpha * kappa_B)

The time for the residual to decay to 1/e of its initial value, in the
absence of crystallisation. If tau_constraint >> tau_crys the system
attempts to crystallise before constraints are satisfied; this is the
regime where R_c gating becomes important.

### Coherence lifetime under drive (T2_eff)

    T2_eff = 1 / (Gamma - gamma * kappa_Q * lambda)

Effective dephasing time when the crystallisation drive partially
compensates environmental decoherence. Valid only when the denominator is
positive (i.e., the drive does not fully cancel decoherence). When
gamma * kappa_Q * lambda >= Gamma, the coherence is dynamically
stabilised and T2_eff diverges -- this is the coherence-protected
crystallisation regime.

### Weight ratios

    r_BE = beta / alpha      (energy-to-constraint ratio)
    r_CE = gamma / alpha     (coherence-to-constraint ratio)

These two numbers, together with the overall scale (set by convention),
fully specify the weight triple.
