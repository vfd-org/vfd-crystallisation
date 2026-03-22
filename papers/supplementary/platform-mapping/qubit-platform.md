# Platform Mapping Sheet: Qubit System (EP1)

## Platform Overview

The qubit platform uses a two-level quantum system -- typically a superconducting transmon, trapped ion, or photon polarisation degree of freedom -- as the simplest non-trivial testbed for crystallisation signatures. A qubit prepared in superposition and subjected to measurement-backaction or controlled decoherence provides direct access to outcome statistics, coherence decay dynamics, and transition-time structure. The 2x2 density matrix makes the full state experimentally reconstructable, and the low Hilbert-space dimension keeps the crystallisation functional landscape analytically tractable.

This platform targets SGT-1 (outcome selection entropy), SGT-3 (transition-time scaling), and SGT-6 (path reproducibility). It is a medium-difficulty platform with an estimated timeline of 1--2 years for conclusive data.

---

## State Representation

The system state is a 2x2 density matrix:

$$\rho = \begin{pmatrix} \rho_{00} & \rho_{01} \\ \rho_{10} & \rho_{11} \end{pmatrix}$$

where $\rho_{00} + \rho_{11} = 1$, $\rho_{01} = \rho_{10}^*$, and $|\rho_{01}|^2 \leq \rho_{00}\rho_{11}$.

In the Bloch representation: $\rho = \frac{1}{2}(I + \vec{r} \cdot \vec{\sigma})$ with Bloch vector $\vec{r} = (r_x, r_y, r_z)$, $|\vec{r}| \leq 1$.

The crystallisation functional acts on $\rho(t)$ as the system evolves from a prepared superposition toward a definite outcome state.

---

## Control Variables

| Variable | Physical Realisation | Role in VFD Framework |
|----------|---------------------|----------------------|
| Drive amplitude $\Omega$ | Microwave/RF pulse power | Sets initial superposition; controls preparation fidelity |
| Detuning $\Delta$ | Frequency offset between drive and qubit | Shifts constraint landscape; modifies residual geometry |
| Environment coupling $g_{\mathrm{env}}$ | Qubit-resonator coupling, bath temperature | Controls dissipation rate; maps to $\Gamma$ |
| Measurement basis | Rotation before projective readout | Probes different slices of the crystallisation landscape |
| Coupling strength $g$ | Qubit-resonator or qubit-qubit coupling | Constraint coupling; modifies basin structure |
| Pulse timing $\Delta t$ | Gate duration, delay between preparation and readout | Controls evolution time on the crystallisation flow |

---

## Observables

| Observable | Symbol | How Measured | VFD Relevance |
|-----------|--------|-------------|---------------|
| State probabilities | $p_0, p_1$ | Repeated projective measurement | Outcome distribution; entropy calculation |
| Outcome entropy | $H = -\sum_i p_i \ln p_i$ | Computed from statistics over $N \geq 10^4$ trials | SGT-1: structured selection vs Born-rule baseline |
| Coherence decay | $|\rho_{01}(t)|$ | Ramsey interferometry; state tomography | Tracks off-diagonal evolution toward crystallisation |
| Purity | $\mathrm{Tr}(\rho^2)$ | Full state tomography | Distinguishes coherent crystallisation from decoherence |
| Transition time | $\tau$ | Time from preparation to definite outcome (purity threshold) | SGT-3: multi-parameter scaling test |
| Repeatability score | $R = N_{\max}/N$ | Fraction of trials yielding most-common outcome | SGT-1: determinism indicator |
| Bloch trajectory | $\vec{r}(t)$ | Time-resolved tomography | SGT-6: path reproducibility |

---

## Parameter Mapping

### Primary crystallisation functional

$$F[\rho] = \alpha\, R_c[\rho] + \beta\, E[\rho] - \gamma\, Q[\rho]$$

| Canonical Parameter | Symbol | Qubit Realisation | How to Tune |
|--------------------|--------|-------------------|-------------|
| Closure weight | $\alpha$ | Relative importance of constraint mismatch in the qubit-resonator system | Fixed by system Hamiltonian; varies with coupling topology |
| Energy weight | $\beta$ | Relative cost of the qubit excited-state population | Set by qubit frequency and temperature; $\beta \sim \hbar\omega_q / k_B T$ |
| Coherence weight | $\gamma$ | Reward for phase alignment between $|0\rangle$ and $|1\rangle$ components | Tuned via drive coherence and measurement backaction strength |
| Noise strength | $\lambda$ | Amplitude of stochastic perturbations (flux noise, charge noise, photon shot noise) | Controlled by shielding, filtering, temperature; deliberately injected via noise generators |
| Constraint sensitivity | $\eta$ | Rate of change of outcome statistics with constraint perturbation: $\eta = \partial O / \partial C$ | Measured by sweeping detuning $\Delta$ or coupling $g$ and tracking outcome shifts |
| Environment coupling | $\Gamma$ | Total decoherence rate combining $T_1$ and $T_2$ processes: $\Gamma = 1/T_1 + 1/T_2$ | Tuned by qubit-bath coupling, resonator $Q$-factor, temperature |
| Closure residual | $R_c$ | $R_c = \|G[\rho] - K\|^2$ where $G[\rho]$ encodes the constraint structure of the qubit-measurement system and $K$ is the closure target | Computed from state tomography; depends on measurement Hamiltonian |
| Boundary coupling | $\kappa_B$ | Coupling between the qubit and its measurement/readout boundary: dispersive shift, Purcell rate | Tuned by resonator geometry and qubit-resonator detuning |
| Coherence coupling | $\kappa_Q$ | Rate at which phase information feeds back into the crystallisation flow; related to measurement-induced dephasing rate | Controlled by measurement power and readout protocol (weak vs strong measurement) |

### Extracting $\Gamma$ from $T_1$ and $T_2$

The environment coupling decomposes as:

$$\Gamma = \Gamma_1 + \Gamma_\phi = \frac{1}{T_1} + \frac{1}{T_\phi}$$

where $T_\phi$ is the pure dephasing time: $1/T_2 = 1/(2T_1) + 1/T_\phi$.

Standard $T_1$ (energy relaxation) and $T_2$ (Ramsey/echo) measurements directly yield $\Gamma$. The crystallisation model prediction is that the dynamics produce structure in the transition-time data beyond what $\Gamma$ alone accounts for.

---

## Expected Usable Regimes

| Regime | Condition | Signature Accessibility |
|--------|-----------|------------------------|
| Strong constraint, low noise | $g \gg \Gamma$, $\lambda \ll g$ | Best regime for detecting crystallisation: crystallisation dynamics dominate over decoherence; $\tau$ scaling should show multi-parameter structure |
| Moderate constraint, moderate noise | $g \sim \Gamma$ | Crossover regime; crystallisation and decoherence predictions begin to overlap; useful for mapping the noise threshold (PRED-008) |
| Weak constraint, high noise | $g \ll \Gamma$ or $\lambda \gg g$ | The crystallisation model predicts indistinguishability from standard decoherence; serves as null-control regime |
| Near-resonance | $\Delta \approx 0$ | Maximises constraint coupling; strongest crystallisation signal expected |
| Large detuning | $\Delta \gg g$ | Weakens constraint; should approach standard dynamics |

**Primary target regime:** $g/\Gamma \geq 5$, $\lambda/g \leq 0.1$, $\Delta/g \leq 1$.

---

## Dominant Confounders

| Confounder | Effect | Mitigation |
|-----------|--------|------------|
| State preparation infidelity | Variation in initial $\rho$ mimics stochastic outcome selection | Benchmark preparation fidelity via process tomography; require $F_{\mathrm{prep}} > 0.999$ |
| Readout error | Misassignment of $|0\rangle$/$|1\rangle$ inflates apparent entropy | Calibrate readout with known states; apply confusion-matrix correction |
| Residual thermal population | $n_{\mathrm{th}} > 0$ shifts outcome probabilities | Operate at $T \ll \hbar\omega_q/k_B$; verify with Rabi population measurement |
| $1/f$ flux noise | Time-varying detuning broadens transition-time distribution | Characterise noise spectrum; restrict analysis to noise-stationary windows |
| Purcell decay | Measurement-induced relaxation mimics crystallisation timescale | Measure Purcell rate independently; subtract from $\tau$ data |
| Drift and slow parameter variation | Systematic shifts over long data runs | Interleave calibration sequences; randomise measurement order |

---

## Calibration Path

### Step 1: Baseline characterisation
- Measure $T_1$, $T_2$, $T_\phi$ using standard relaxation and Ramsey protocols.
- Extract $\Gamma = 1/T_1 + 1/T_\phi$.
- Characterise readout fidelity and apply confusion-matrix correction.

### Step 2: Preparation fidelity
- Prepare target superposition $|\Psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$.
- Verify via state tomography that $F_{\mathrm{prep}} > 0.999$.
- Record any systematic preparation bias.

### Step 3: Born-rule null baseline
- Collect $N \geq 10^4$ outcome measurements at fixed preparation.
- Compute $H_{\mathrm{obs}}$ and $R_{\mathrm{obs}}$.
- Verify agreement with $H_{\mathrm{Born}}$ within statistical uncertainty.
- This indicates the null hypothesis against which crystallisation-model deviations are tested.

### Step 4: Constraint sweep
- Vary coupling strength $g$ across $\geq 5$ values spanning $g/\Gamma \in [0.1, 50]$.
- At each $g$, collect $N \geq 10^4$ trials.
- Record $H(g)$, $R(g)$, $\tau(g)$.

### Step 5: Detuning sweep
- Vary $\Delta$ across $\geq 5$ values at fixed $g$.
- Record $H(\Delta)$, $\tau(\Delta)$.
- Test for constraint-geometry sensitivity: $\eta = \partial H / \partial \Delta$.

### Step 6: Noise injection sweep
- Inject controlled noise at amplitude $\lambda$ via an external noise source.
- Sweep $\lambda$ from sub-threshold to above threshold.
- Map the deterministic-to-stochastic crossover (PRED-008).

### Step 7: Transition-time extraction
- Use time-resolved measurement (weak continuous monitoring or repeated projective snapshots) to extract $\tau$ for each trial.
- Fit $\tau$ data to crystallisation model: $\tau = 1/(a R_c + b Q + c \kappa_B + d \Gamma)$.
- Fit to decoherence model: $\tau = A/\Gamma$.
- Compare via AIC/BIC.

### Step 8: Path reproducibility
- Perform time-resolved Bloch-vector tracking for $\geq 100$ identically prepared trials.
- Compute trajectory distance $D_{\mathrm{traj}} = \int \|\vec{r}_i(t) - \vec{r}_j(t)\| dt$.
- Compare to stochastic baseline.

---

## Practical Considerations

- **Sample size requirements:** Minimum $10^4$ trials per configuration point to resolve $H$ deviations at the 1% level. For transition-time analysis, $\geq 500$ time-resolved trajectories per point.

- **Run time:** At typical repetition rates of 10--100 kHz for superconducting qubits, $10^4$ trials take 0.1--1 second per configuration. A full sweep of 25 configuration points requires approximately 30 minutes to 5 hours including calibration overhead.

- **Platform candidates:** IBM/Google superconducting processors (publicly accessible but limited control), dedicated cryogenic qubit setups (full control), trapped-ion systems (slower repetition but longer coherence).

- **Data management:** Each trial produces a binary outcome plus optional time-resolved trajectory. Storage requirements are modest: approximately 1 GB for $10^6$ trials with trajectory data.

- **Blinding protocol:** To avoid confirmation bias, analysis should be performed blind to the crystallisation/null model labels until statistical tests are complete. Pre-register the analysis pipeline and discrimination thresholds.

- **Known limitations:** The 2-level system provides limited basin structure (only two basins). Multi-qubit extensions or qutrit systems could enrich the landscape but increase experimental complexity.

- **Connection to predictions:** This platform directly tests PRED-001 (outcome entropy), PRED-002 (transition-time scaling), PRED-005 (path reproducibility), and PRED-008 (noise threshold crossover).
