# Platform Mapping Sheet: Analog Coupled Oscillator System (EP5)

## Platform Overview

This is the fastest demonstrator platform in the crystallisation experimental programme. No quantum regime is required. No cryogenics, no vacuum system, no single-photon detectors. A network of 8--32 coupled classical oscillators with a programmable coupling matrix can be built and producing data within weeks, not years. The crystallisation operator's mathematical machinery -- closure functional minimisation, basin selection, metastable plateaus, path reproducibility, transition-time scaling -- can all be tested directly in a fully classical system where the dynamics are fast, repeatable, and continuously observable.

The analog oscillator platform does not test whether crystallisation occurs in quantum systems. It tests whether the mathematical framework of the crystallisation operator correctly predicts the dynamics of constrained multi-attractor systems. If the crystallisation functional $F = \alpha R + \beta E - \gamma Q$ captures the attractor structure, basin selection, and convergence dynamics of a physical coupled-oscillator network, then the mathematical framework gains credibility before it is applied to quantum-regime experiments where confounders are far more severe.

Estimated timeline to first results: 3--6 months. This is the recommended starting point for the entire experimental programme.

Implementations: electronic oscillator arrays (LC circuits, op-amp oscillators, FPGA-emulated oscillators), coupled pendula with electromagnetic feedback, acoustic resonator networks, or photonic mesh lattices.

---

## State Representation

The system state is a vector of oscillator amplitudes and phases:

$$\vec{x}(t) = \{A_1(t), \phi_1(t), A_2(t), \phi_2(t), \ldots, A_N(t), \phi_N(t)\}$$

where $A_k$ is the amplitude and $\phi_k$ is the phase of the $k$-th oscillator.

In complex notation: $z_k(t) = A_k(t) e^{i\phi_k(t)}$, and the state vector is $\vec{z}(t) \in \mathbb{C}^N$.

The density-matrix analogue is the covariance matrix:

$$\Sigma_{jk}(t) = \langle z_j(t) z_k^*(t) \rangle$$

Diagonal elements give mode energies $|z_k|^2$; off-diagonal elements give inter-oscillator coherence. The crystallisation functional acts on $\vec{z}(t)$ or equivalently on $\Sigma(t)$.

The normal-mode decomposition provides the spectral representation:

$$\vec{z}(t) = \sum_\mu c_\mu(t) \vec{v}_\mu$$

where $\vec{v}_\mu$ are the eigenvectors of the coupling matrix. Mode amplitudes $c_\mu(t)$ evolve under the combined effects of coupling, damping, and driving -- this is the direct analog of spectral reweighting in the crystallisation operator.

---

## Control Variables

| Variable | Physical Realisation | Role in VFD Framework |
|----------|---------------------|----------------------|
| Coupling matrix $\mathbf{K}$ | Resistive/capacitive coupling between electronic oscillators; spring constants between pendula; programmed weights in FPGA | Defines the constraint landscape: basin structure, number of attractors, basin boundaries |
| Damping rates $\gamma_k$ | Series/parallel resistance; mechanical friction; programmed dissipation | Environment coupling $\Gamma$; controls dissipation timescale |
| Forcing function $f_k(t)$ | External drive voltage/current; mechanical excitation; programmed input | Controls initial energy injection and sustained driving; can probe driven-dissipative steady states |
| Boundary perturbation $\delta K_{jk}$ | Small changes to selected coupling elements | Constraint-geometry perturbation; tests $\eta$ (constraint sensitivity) without changing oscillator frequencies |
| Oscillator frequencies $\omega_k$ | Component values (LC); pendulum length; programmed frequency | Sets the energy landscape; analogous to site energies |
| Network topology | Which oscillators are coupled; ring, chain, all-to-all, random graph | Constraint topology; determines coordination number and frustration |
| Noise injection $\sigma_{\mathrm{noise}}$ | Noise voltage source in series with each oscillator; thermal noise at controlled temperature | Maps to $\lambda$; allows sweeping the deterministic-to-stochastic crossover |
| Initial conditions $\vec{z}(0)$ | Programmed initial voltages/currents; mechanical displacement | Sets the starting point on the crystallisation landscape |

---

## Observables

| Observable | Symbol | How Measured | VFD Relevance |
|-----------|--------|-------------|---------------|
| Phase locking | $\Delta\phi_{jk} = \phi_j - \phi_k$ at steady state | Phase comparator; cross-correlation of oscillator signals | Coherence metric $Q$; phase alignment indicates crystallisation |
| Attractor entry time | $\tau$ | Time from release to phase-locked or steady-amplitude state | SGT-3: transition-time scaling with constraint parameters |
| Mode dominance | Which normal mode $\mu$ carries most energy at steady state | Spectral analysis of oscillator signals; projection onto normal-mode basis | SGT-4: basin preference; does mode selection track $F$-landscape or energy alone? |
| Metastable ordering | Intermediate configurations visited before final convergence | Time-resolved amplitude and phase recording | SGT-5: plateau detection; dwell-time statistics |
| Energy trajectory | $E(t) = \sum_k |z_k(t)|^2$ | Sum of squared amplitudes from voltage/displacement measurements | Monitors descent toward attractor; tests Theorem 3 (monotonic descent) |
| Functional trajectory | $F(t) = \alpha R_c(t) + \beta E(t) - \gamma Q(t)$ | Computed in real time from measured amplitudes and phases | Direct test of crystallisation dynamics; most informative observable |
| Basin preference index | $\mathrm{BPI}_\mu = N_\mu / N_{\mathrm{trials}}$ | Fraction of trials ending in each normal-mode attractor | Tests whether basin selection depends on $\mathbf{K}$ geometry beyond energy ordering |
| Trajectory distance | $D_{\mathrm{traj}} = \int \|\vec{z}^{(a)}(t) - \vec{z}^{(b)}(t)\| dt$ | Computed from time-series data across repeated identical initialisations | SGT-6: path reproducibility |

---

## Parameter Mapping

### Primary crystallisation functional

$$F[\vec{z}] = \alpha\, R_c[\vec{z}] + \beta\, E[\vec{z}] - \gamma\, Q[\vec{z}]$$

| Canonical Parameter | Symbol | Oscillator Realisation | How to Tune |
|--------------------|--------|----------------------|-------------|
| Closure weight | $\alpha$ | Weight of constraint mismatch: deviation of the current oscillator configuration from the nearest coupling-compatible normal mode | Determined by the coupling matrix $\mathbf{K}$; varies with network topology and coupling strengths |
| Energy weight | $\beta$ | Total oscillator energy: $E = \sum_k |z_k|^2$ (sum of squared amplitudes) | Set by oscillator frequencies $\omega_k$ and damping rates $\gamma_k$; energy scale is controlled by drive amplitude |
| Coherence weight | $\gamma$ | Global phase coherence: $Q = \frac{1}{N^2} \sum_{j,k} \cos(\phi_j - \phi_k)$ | Tuned by coupling strength: stronger coupling rewards phase alignment more strongly |
| Noise strength | $\lambda$ | RMS amplitude of injected noise voltage/force | Directly controlled by noise generator amplitude; can be swept from zero to above the deterministic-selection threshold |
| Constraint sensitivity | $\eta$ | $\eta = \partial(\mathrm{BPI})/\partial(\delta K_{jk})$: rate of change of basin preference with coupling perturbation | Measured by sweeping individual coupling elements while holding oscillator frequencies fixed |
| Environment coupling | $\Gamma$ | Average damping rate: $\Gamma = \frac{1}{N}\sum_k \gamma_k$ | Tuned by resistance values (electronic), friction (mechanical), or programmed damping |
| Closure residual | $R_c$ | $R_c = \|\vec{z} - P_\mu \vec{z}\|^2$ where $P_\mu$ projects onto the nearest normal mode; measures how far the current state is from any pure-mode attractor | Computed from measured amplitudes and phases; decreases as the system approaches a normal-mode fixed point |
| Boundary coupling | $\kappa_B$ | Coupling between the oscillator network and its termination: edge effects, coupling to external load, measurement backaction | Tuned by termination impedance, measurement probe coupling, or deliberate boundary drive |
| Coherence coupling | $\kappa_Q$ | Rate at which phase information propagates through the network; related to the spectral gap of the coupling matrix | $\kappa_Q \sim \lambda_2(\mathbf{K})$ (algebraic connectivity / Fiedler value); tuned by overall coupling strength |

---

## Expected Usable Regimes

| Regime | Condition | Signature Accessibility |
|--------|-----------|------------------------|
| Low noise, strong coupling | $\lambda \ll \min(\gamma_k)$, $\|K_{jk}\| \gg \gamma_k$ | **Optimal regime.** Crystallisation dynamics dominate; deterministic basin selection; high path reproducibility; clear plateaus |
| Multi-basin landscape | Coupling matrix with $\geq 3$ distinct normal-mode attractors at comparable energies | Richest dynamics; mode competition; metastable intermediates; best for testing full crystallisation functional |
| Frustrated coupling | Non-trivially frustrated topology (triangular, random graph with competing interactions) | Constraint satisfaction is non-trivial; the crystallisation model predicts specific resolution; standard energy minimisation may be ambiguous |
| Driven-dissipative steady state | Continuous forcing balanced by damping | Tests whether steady-state mode selection depends on coupling geometry beyond gain/loss balance |
| Near-degenerate modes | Two or more normal modes with $|\omega_\mu - \omega_\nu| \ll \gamma$ | Maximises competition between attractors; most sensitive to constraint-geometry effects |
| High noise | $\lambda \gg \min(\gamma_k)$ | Stochastic regime; crystallisation model predictions reduce to noise-dominated dynamics; null-control regime |

**Primary target regime:** Low noise, multi-basin landscape with $N = 8$--$16$ oscillators, $\geq 3$ competing attractors, coupling strengths $\|K_{jk}\| / \gamma_k \geq 10$.

---

## Dominant Confounders

| Confounder | Effect | Mitigation |
|-----------|--------|------------|
| Component tolerance | Variation in oscillator frequencies and coupling values from nominal | Measure all component values; calibrate the actual coupling matrix before comparison to theory |
| Nonlinearity | Real oscillators are nonlinear at large amplitudes; introduces harmonic generation and amplitude-dependent frequency shifts | Operate in the linear regime (small amplitudes); characterise nonlinearity threshold; include leading nonlinear corrections in the model |
| Parasitic coupling | Unintended electromagnetic coupling between non-adjacent oscillators | Shield oscillator circuits; measure the full coupling matrix including parasitics; use FPGA implementation for precise coupling control |
| Thermal drift | Component values drift with temperature; changes the coupling matrix over long runs | Temperature-stabilise the experiment; interleave calibration measurements; use FPGA (digital coupling is temperature-independent) |
| Measurement backaction | Voltage probes load the oscillator circuits | Use high-impedance probes ($Z_{\mathrm{probe}} \gg Z_{\mathrm{osc}}$); characterise loading effect; include in model |
| Initial-condition sensitivity | Chaotic dynamics in some coupling topologies | Characterise Lyapunov exponents; restrict to non-chaotic parameter regimes; verify reproducibility before testing crystallisation model predictions |
| Standard coupled-oscillator theory matching crystallisation model | If crystallisation model predictions are identical to standard normal-mode theory, the test is uninformative | Design coupling matrices where crystallisation and standard theory make different predictions (constraint geometry vs energy ordering); this is the critical experimental design requirement |

---

## Calibration Path

### Step 1: Network construction and characterisation
- Build or programme the oscillator network with target coupling matrix $\mathbf{K}$.
- Measure all oscillator frequencies $\omega_k$ (free-running, uncoupled).
- Measure the full coupling matrix including any parasitic coupling.
- Record damping rates $\gamma_k$ for each oscillator.
- Verify the normal-mode structure: eigenvalues and eigenvectors of $\mathbf{K}$.

### Step 2: Standard dynamics baseline
- Release the system from a known initial condition.
- Record $\vec{z}(t)$ for all oscillators at high time resolution.
- Verify that the dynamics match the standard coupled-oscillator ODE: $\dot{z}_k = i\omega_k z_k - \gamma_k z_k + i \sum_j K_{jk} z_j$.
- This indicates the null model: any crystallisation signature must appear as a deviation from standard coupled-oscillator theory.

### Step 3: Multi-basin landscape design
- Choose a coupling matrix $\mathbf{K}$ such that:
  - There exist $\geq 3$ normal modes at comparable energies.
  - The crystallisation functional $F$ predicts a different basin preference than standard energy minimisation.
  - Specifically: construct $\mathbf{K}$ where the lowest-energy normal mode is NOT the mode with the lowest closure residual $R_c$.
- This is the critical design step. If crystallisation and standard theory make the same prediction for all coupling matrices, the test is uninformative.

### Step 4: Basin preference measurement
- Release from $\geq 100$ identical initial conditions per coupling matrix.
- Record which normal-mode attractor the system converges to.
- Compute $\mathrm{BPI}_\mu$ for each mode.
- Standard prediction: system converges to lowest-energy (least-damped) mode.
- Crystallisation model prediction: system converges to the mode minimising $F = \alpha R_c + \beta E - \gamma Q$.
- If these differ, measure which prediction matches the data.

### Step 5: Transition-time scaling
- Sweep coupling strength ($\|K_{jk}\|$), damping ($\gamma_k$), and initial energy ($\|\vec{z}(0)\|$).
- Measure $\tau$ (time to reach attractor) for each configuration.
- Fit $\tau$ data to crystallisation model: $\tau = 1/(a R_c + b Q + c \kappa_B + d \Gamma)$.
- Fit to standard model: $\tau = A/\gamma_{\mathrm{eff}}$ (damping-dominated).
- Compare via AIC/BIC across $\geq 20$ parameter points.

### Step 6: Metastable plateau detection
- In multi-basin landscapes, record $F(t)$ trajectories at high time resolution.
- Search for plateau events: $|dF/dt| < \epsilon$ for duration $> \delta$.
- Measure dwell-time statistics at each plateau.
- Standard prediction: monotonic exponential decay toward lowest-loss mode.
- Crystallisation model prediction: structured plateaus at metastable $F$-values corresponding to saddle points or local minima.

### Step 7: Constraint-geometry perturbation
- Starting from the baseline coupling matrix, perturb individual coupling elements $\delta K_{jk}$ while keeping oscillator frequencies fixed.
- Measure $\Delta(\mathrm{BPI})$ as a function of $\delta K_{jk}$.
- Compute $\eta = \partial(\mathrm{BPI})/\partial(\delta K_{jk})$.
- Standard prediction: BPI changes only insofar as the normal-mode structure changes (which it does, but in a specific and calculable way).
- Crystallisation model prediction: BPI shows additional sensitivity to constraint geometry beyond what normal-mode theory predicts.
- This is the most demanding discrimination: it requires comparing measured $\eta$ to both crystallisation and standard predictions with sufficient precision to distinguish them.

### Step 8: Noise threshold sweep
- Inject noise at amplitude $\lambda$ and sweep from sub-threshold to above threshold.
- Measure the crossover from deterministic basin selection (same attractor every trial) to stochastic selection (random attractor from trial to trial).
- Characterise the crossover shape: sharp threshold vs gradual transition.
- The crystallisation model predicts a structured crossover at a critical noise level (PRED-008).

### Step 9: Path reproducibility
- For identical initial conditions and zero (or minimal) noise, run $\geq 100$ trials.
- Compute trajectory distance $D_{\mathrm{traj}}$ between all pairs.
- Standard prediction for a deterministic ODE: $D_{\mathrm{traj}} \approx 0$ up to measurement noise.
- Crystallisation model prediction: also $D_{\mathrm{traj}} \approx 0$ -- but the value of this measurement is as a baseline for comparison with quantum platforms where crystallisation and standard models diverge on path reproducibility.

---

## Practical Considerations

- **Recommended starting experiment.** It requires no quantum-regime operation, no cryogenics, no vacuum, no single-photon detection. An electronic oscillator array can be built on a breadboard or PCB in days. An FPGA implementation can be programmed in weeks. First data can be collected within a month of starting.

- **Implementation options ranked by speed:**
  1. **FPGA-emulated oscillators** (fastest: days to first data). Programme the coupled-oscillator ODE on an FPGA; coupling matrix is software-defined; no component tolerance issues; perfect repeatability; arbitrary network size and topology. Drawback: simulating physics with a computer raises the question of whether you are testing the math or the physics. This approach tests the mathematical implementation rather than the underlying physical hypothesis.
  2. **Electronic oscillator array** (fast: weeks). LC circuits or op-amp relaxation oscillators coupled by resistors/capacitors. Real physics, real noise, real component variation. $N = 8$--$32$ oscillators on a single PCB. Measurement via oscilloscope or data acquisition card.
  3. **Coupled pendula** (moderate: months). Mechanical oscillators with electromagnetic coupling and feedback. Visually compelling. Slower dynamics (Hz vs kHz for electronics). Good for demonstrations, less practical for high-statistics measurements.

- **Cost estimate:** Electronic oscillator array: under $500 in components plus standard lab equipment (oscilloscope, function generator, DAQ). FPGA: $200--$2000 for development board. Coupled pendula: $1000--$5000 depending on precision.

- **Data collection rate:** Electronic oscillators at kHz frequencies produce attractor convergence in milliseconds. At $\geq 1000$ trials per second (with automated initial-condition reset), $10^5$ trials per coupling matrix can be collected in under 2 minutes. A full sweep of 10 coupling matrices with calibration takes approximately 1 hour. This is orders of magnitude faster than any quantum platform.

- **Critical design requirement:** The coupling matrix must be designed so that crystallisation and standard theory make distinct predictions. If the crystallisation functional minimum always coincides with the standard energy minimum, the experiment cannot discriminate. Section "Step 3" of the calibration path addresses this directly. Candidate coupling matrices should be pre-screened via numerical simulation of both models.

- **What this platform does NOT test:** It does not test quantum-specific crystallisation model predictions (non-classical state resolution, Born-rule deviation, wavefunction crystallisation). It tests the mathematical framework: whether $F = \alpha R + \beta E - \gamma Q$ correctly predicts attractor dynamics in a physical multi-basin system. This is a necessary but not sufficient validation.

- **Scaling path:** Start with $N = 8$ oscillators (manageable, analytically tractable). Scale to $N = 16$, then $N = 32$. At each scale, verify that crystallisation model predictions scale correctly. The FPGA implementation scales trivially; the electronic implementation scales linearly in hardware complexity.

- **Connection to predictions:** This platform directly tests PRED-009 (multi-basin landscape structure) and PRED-010 (analog validation). It also provides quantitative calibration of the crystallisation functional parameters ($\alpha, \beta, \gamma$) that can then be carried forward to quantum platforms.

- **Strategic value:** If the analog oscillator platform shows that the crystallisation functional accurately predicts attractor dynamics in a classical multi-basin system, this provides a test of the mathematical framework. If it fails -- if standard coupled-oscillator theory fully accounts for all observed dynamics with no additional explanatory value from the crystallisation functional -- then the applicability of the framework would need to be reassessed, and the more expensive quantum experiments should be reconsidered.
