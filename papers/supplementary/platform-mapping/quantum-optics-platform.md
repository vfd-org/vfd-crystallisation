# Platform Mapping Sheet: Quantum Optics / Cavity QED System (EP4)

## Platform Overview

The quantum optics platform uses electromagnetic field modes confined in optical or microwave cavities to test crystallisation in systems where mode selection, coherence dynamics, and attractor formation are directly observable. Implementations include Fabry-Perot optical cavities coupled to atoms (cavity QED), superconducting microwave resonators coupled to transmon qubits (circuit QED), multimode optical cavities, and photonic mesh networks.

The key strength of this platform is continuous, real-time monitoring of mode populations and coherence via homodyne or heterodyne detection. This provides direct access to the full crystallisation trajectory $F(t)$, not just the endpoints. The system naturally supports multiple competing modes (attractors), tuneable dissipation, and controllable reservoir coupling, making it the primary platform for testing metastable plateau structure (SGT-5) and path reproducibility (SGT-6).

This platform targets SGT-3 (transition-time scaling), SGT-5 (metastable plateaus), and SGT-6 (path reproducibility). It is a medium-to-high difficulty platform with an estimated timeline of 1--2 years.

---

## State Representation

### Single-mode cavity field

The cavity field state is described by the density operator in the Fock basis:

$$\rho = \sum_{n,m} \rho_{nm} |n\rangle\langle m|$$

where $|n\rangle$ is the $n$-photon Fock state. For coherent or thermal states, the $P$-function or Wigner function provides a phase-space representation:

$$W(\alpha) = \frac{2}{\pi} \mathrm{Tr}\left[\rho\, D^\dagger(\alpha)\, (-1)^{a^\dagger a}\, D(\alpha)\right]$$

### Multimode system

For $M$ cavity modes, the state lives in the tensor product of mode Hilbert spaces:

$$\rho \in \mathcal{H}_1 \otimes \mathcal{H}_2 \otimes \cdots \otimes \mathcal{H}_M$$

The accessible observables are mode occupation numbers $\langle a_k^\dagger a_k \rangle$, inter-mode correlations $\langle a_j^\dagger a_k \rangle$, and the full quadrature record from homodyne detection.

### Atom-cavity system (Jaynes-Cummings)

For a single atom coupled to a single cavity mode:

$$H = \omega_c\, a^\dagger a + \frac{\omega_a}{2}\sigma_z + g(a^\dagger \sigma_- + a\, \sigma_+)$$

The combined state is $\rho \in \mathcal{H}_{\mathrm{atom}} \otimes \mathcal{H}_{\mathrm{cavity}}$. The crystallisation operator acts on the full joint density matrix.

---

## Control Variables

| Variable | Physical Realisation | Role in VFD Framework |
|----------|---------------------|----------------------|
| Cavity loss rate $\kappa$ | Mirror transmissivity, absorption, scattering | Controls dissipation; maps directly to $\Gamma$ |
| Drive strength $\varepsilon$ | Injected laser/microwave power | Pumps the system; controls competition between driving and dissipation |
| Atom-cavity coupling $g$ | Atomic dipole matrix element, mode volume, atom position | Constraint coupling strength; determines basin structure in dressed-state picture |
| Detuning $\Delta = \omega_a - \omega_c$ | Frequency difference between atom and cavity | Constraint geometry parameter; shifts relative basin positions |
| Mode coupling | Inter-mode scattering, nonlinear crystal, beam splitter | Couples different cavity modes; creates multi-basin landscape |
| Reservoir temperature $\bar{n}_{\mathrm{th}}$ | Cryogenic temperature (microwave), thermal photon background (optical) | Thermal noise source; contributes to $\lambda$ |
| Number of modes $M$ | Cavity geometry, free spectral range selection | Sets dimensionality of the crystallisation landscape |
| Atom number $N_{\mathrm{atom}}$ | Atom loading rate, MOT density | Collective coupling enhancement: $g_{\mathrm{eff}} = g\sqrt{N}$; scales constraint strength |

---

## Observables

| Observable | Symbol | How Measured | VFD Relevance |
|-----------|--------|-------------|---------------|
| Mode selection | Which mode(s) reach steady-state occupation | Heterodyne detection; spectral analysis of output field | SGT-4: does mode selection track constraint geometry or energy ordering? |
| Coherence envelope | $|\langle a_j^\dagger a_k \rangle(t)|$ | Two-mode heterodyne; cross-correlation of output fields | Tracks inter-mode coherence during crystallisation; distinguishes crystallisation dynamics from standard decay |
| Attractor repeatability | Fraction of trials converging to same end-state | Repeated preparation and steady-state measurement | SGT-6: path reproducibility; determinism indicator |
| Photon number trajectory | $\langle n_k(t) \rangle$ for each mode | Time-resolved photon counting or homodyne quadrature record | Full crystallisation trajectory; plateau detection |
| Functional trajectory | $F(t)$ computed from mode data | Post-processing of $\{n_k(t), \langle a_j^\dagger a_k\rangle(t)\}$ | Direct test of monotonic descent (Theorem 3); plateau detection (SGT-5) |
| Transition time | $\tau$ from preparation to steady state | Time to reach $|dF/dt| < \epsilon$ threshold | SGT-3: scaling with $(g, \kappa, \Delta)$ |
| Wigner function negativity | $W_{\min} < 0$ | Quantum state tomography via displaced photon counting | Quantum non-classicality witness; is consistent with operation in quantum regime |

---

## Parameter Mapping

### Primary crystallisation functional

$$F[\rho] = \alpha\, R_c[\rho] + \beta\, E[\rho] - \gamma\, Q[\rho]$$

| Canonical Parameter | Symbol | Quantum Optics Realisation | How to Tune |
|--------------------|--------|---------------------------|-------------|
| Closure weight | $\alpha$ | Weight of constraint mismatch between the current multi-mode state and the nearest constraint-compatible (single-mode or dressed-state) configuration | Determined by cavity geometry and atom-cavity coupling topology; changes with mode structure |
| Energy weight | $\beta$ | Energetic cost of photon occupation: $\beta E \sim \beta \sum_k \omega_k \langle n_k \rangle$ | Set by cavity frequencies $\omega_k$ and drive-cavity detuning |
| Coherence weight | $\gamma$ | Reward for inter-mode or atom-field phase alignment; related to the cavity superradiant order parameter | Larger in strong-coupling regime ($g > \kappa$); reduced by decoherence |
| Noise strength | $\lambda$ | Thermal photon number $\bar{n}_{\mathrm{th}}$, vacuum fluctuations, technical laser noise | Controlled by temperature (microwave: dilution fridge; optical: room-temperature $\bar{n} \approx 0$), laser linewidth |
| Constraint sensitivity | $\eta$ | $\eta = \partial(\text{mode selection})/\partial \Delta$ at fixed drive power | Measured by sweeping atom-cavity detuning and tracking which mode dominates |
| Environment coupling | $\Gamma$ | Total field decay rate: $\Gamma = \kappa + \kappa_{\mathrm{abs}} + \gamma_{\mathrm{atom}}$ combining mirror loss, absorption, and atomic spontaneous emission | $\kappa$ tuned by mirror reflectivity or coupler design; $\gamma_{\mathrm{atom}}$ by atomic species and cavity geometry |
| Closure residual | $R_c$ | Mismatch between current mode-occupation pattern and the predicted crystallised state | Computed from measured $\{n_k\}$ and inter-mode coherences; $R_c \to 0$ at steady state if crystallisation is complete |
| Boundary coupling | $\kappa_B$ | Coupling between the cavity modes and the external electromagnetic environment through the mirrors | Directly proportional to mirror transmissivity $T$; tuned by mirror coating or coupling port design |
| Coherence coupling | $\kappa_Q$ | Rate at which inter-mode coherence recirculates within the cavity and feeds back into mode dynamics; related to cavity round-trip time and nonlinear coupling | $\kappa_Q \propto g^2/\Delta$ in dispersive regime; $\kappa_Q \propto g$ on resonance |

---

## Expected Usable Regimes

| Regime | Condition | Signature Accessibility |
|--------|-----------|------------------------|
| Strong coupling | $g > \kappa, \gamma_{\mathrm{atom}}$ | Dressed states form distinct basins; richest crystallisation dynamics; mode selection is non-trivial |
| Multimode strong coupling | Multiple modes with $g_k > \kappa$ | Multiple competing attractors; metastable plateaus expected; highest-information regime |
| Dispersive regime | $\Delta \gg g$ | Atom-cavity interaction modifies mode frequencies without exchanging excitations; perturbative constraint coupling |
| Bad-cavity limit | $\kappa \gg g$ | Environment dominates; crystallisation model predictions reduce to standard cavity decay; serves as null-control regime |
| Driven-dissipative steady state | Continuous drive balanced by cavity loss | Tests whether steady-state mode selection depends on constraint geometry beyond Hamiltonian parameters |
| Ultrastrong coupling | $g / \omega_c > 0.1$ | Non-perturbative regime; constraint landscape fundamentally restructured; novel crystallisation model predictions possible |

**Primary target regime:** Strong coupling ($g/\kappa \geq 2$), multimode ($M \geq 3$), low thermal noise ($\bar{n}_{\mathrm{th}} < 0.1$).

---

## Dominant Confounders

| Confounder | Effect | Mitigation |
|-----------|--------|------------|
| Spontaneous emission into non-cavity modes | Atom decays outside the cavity mode, introducing uncontrolled decoherence | Use high-cooperativity cavities ($C = g^2/\kappa\gamma \gg 1$); select atoms with narrow linewidths |
| Technical laser noise | Amplitude and phase noise on the drive field broadens mode dynamics | Use ultra-stable laser references; characterise noise spectrum; filter above crystallisation bandwidth |
| Mode competition from standard nonlinear dynamics | Classical mode competition in driven-dissipative systems mimics crystallisation mode selection | Carefully distinguish: standard theory predicts mode selection based on gain/loss balance; the crystallisation model predicts additional constraint-geometry dependence. Standard predictions should be established first. |
| Atom number fluctuations | Shot-to-shot variation in atom-cavity coupling | Post-select on measured atom number; use single-atom techniques where possible |
| Thermal photon background | Adds incoherent occupation to modes | Operate at optical frequencies (negligible $\bar{n}_{\mathrm{th}}$) or at millikelvin temperatures (microwave) |
| Detector inefficiency and dark counts | Distorts measured mode trajectories | Characterise detector response; apply quantum efficiency corrections; use superconducting detectors |
| Cavity birefringence and mode splitting | Unintended lifting of mode degeneracies | Characterise cavity mode spectrum precisely; include measured splittings in both crystallisation and standard models |

Distinguishing these effects is essential before attributing behaviour to the crystallisation model.

---

## Calibration Path

### Step 1: Cavity characterisation
- Measure cavity linewidths $\kappa_k$ for all relevant modes via ringdown or transmission spectroscopy.
- Map the mode spectrum: frequencies $\omega_k$, free spectral range, transverse mode splittings.
- Characterise input/output coupling efficiencies.

### Step 2: Atom-cavity coupling calibration
- Measure vacuum Rabi splitting to extract $g$.
- Verify strong-coupling condition: $g > \kappa, \gamma$.
- Characterise coupling as a function of atom position (if applicable).

### Step 3: Standard driven-dissipative baseline
- Drive the cavity and measure steady-state mode occupation without atom coupling.
- Verify agreement with standard input-output theory.
- This provides the null baseline for mode selection in the absence of constraint coupling.

### Step 4: Single-mode transition-time measurement
- Prepare atom-cavity system in superposition of dressed states.
- Measure the time from preparation to definite photon-number state.
- Sweep $(g, \kappa, \Delta)$ systematically:
  - $g$ sweep: vary atom position or atom number.
  - $\kappa$ sweep: use variable output coupler or different cavity.
  - $\Delta$ sweep: tune atom or cavity frequency.
- Fit $\tau(g, \kappa, \Delta)$ to crystallisation model: $\tau = 1/(a R_c + b Q + c \kappa_B + d \Gamma)$.
- Fit to decoherence model: $\tau = A/\kappa$.
- Compare via AIC/BIC across $\geq 20$ parameter points, $\geq 500$ trials each.

### Step 5: Multimode plateau detection
- Prepare multimode superposition (excite $M \geq 3$ modes simultaneously).
- Record mode-population trajectories $\{n_k(t)\}$ for $\geq 1000$ trials.
- Compute $F(t)$ from measured data.
- Search for metastable plateaus: regions where $|dF/dt| < \epsilon$ for duration $> \delta$.
- Characterise dwell-time statistics at each plateau.
- Compare to standard prediction (smooth monotonic decay to lowest-loss mode).

### Step 6: Mode-selection sensitivity to constraint geometry
- Vary mode coupling structure (detuning, nonlinear interaction, beam splitter ratio) while holding drive and loss parameters fixed.
- Track which mode the system selects as steady state.
- Standard prediction: mode selection depends on gain/loss balance.
- Crystallisation model prediction: mode selection also depends on constraint geometry (coupling topology, residual structure).
- Compute constraint sensitivity $\eta = \partial(\text{selected mode})/\partial(\text{constraint parameter})$.

### Step 7: Attractor repeatability measurement
- Prepare identical initial states across $\geq 200$ trials per configuration.
- Measure end-state and full trajectory for each trial.
- Compute reproducibility: fraction converging to same mode, trajectory distance $D_{\mathrm{traj}}$.
- Compare to expected stochastic spread from quantum noise.

### Step 8: Wigner function verification
- At key time points during the crystallisation trajectory, perform quantum state tomography.
- Verify non-classical features (negativity, squeezing) at intermediate times.
- Confirm that the system operates in the quantum regime, not merely as a classical oscillator.

---

## Practical Considerations

- **Circuit QED (nearest-term quantum optics implementation):** Superconducting microwave cavities coupled to transmon qubits. Strong coupling is routinely achieved ($g/\kappa > 10$). Multimode cavities with $M = 3$--$10$ modes are accessible. Dilution refrigerator temperatures ($\sim 20$ mK) ensure $\bar{n}_{\mathrm{th}} < 0.01$. Repetition rates of $\sim 10$ kHz allow rapid data collection.

- **Optical cavity QED:** Fabry-Perot cavities with single atoms. Higher frequencies mean zero thermal background. Strong coupling is more difficult but achieved in several labs. Single-atom loading introduces shot-to-shot variation.

- **Photonic mesh networks:** Programmable integrated photonic circuits. Provide tuneable multimode coupling matrices. Operate at room temperature. May serve as a bridge to the analog oscillator platform (EP5).

- **Data rates:** Homodyne detection produces continuous quadrature records at $\sim 100$ MHz bandwidth. A single trajectory of 1 microsecond duration generates $\sim 100$ data points. For 1000 trajectories across 20 parameter points, total data volume is modest ($\sim 1$ GB).

- **Real-time $F(t)$ computation:** The crystallisation functional can be computed in real time from the homodyne record if the parameter mapping is calibrated in advance. This enables adaptive experiments: terminate early if the system clearly enters a known regime.

- **Standard mode competition as a confounder:** This is the most important confounder for this platform. Driven-dissipative multimode systems exhibit rich mode-competition dynamics even without the crystallisation model. The experimental design must carefully distinguish crystallisation-specific predictions (constraint-geometry dependence of mode selection, metastable plateaus with specific dwell-time statistics) from standard nonlinear-optics mode competition. The calibration path (Steps 3 and 6) addresses this directly.

- **Connection to predictions:** This platform tests PRED-002 (transition-time scaling), PRED-004 (metastable plateaus), PRED-005 (path reproducibility), PRED-006 (constraint-geometry sensitivity), and PRED-009 (multi-basin landscape structure).
