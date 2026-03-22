# Platform Mapping Sheet: Interferometry System (EP2)

## Platform Overview

The interferometry platform uses path-superposition states -- a quantum particle or massive object traversing two or more spatially separated paths simultaneously -- to probe crystallisation in the regime where spatial coherence is progressively lost. Implementations include Mach-Zehnder interferometers with single photons or neutrons, matter-wave interferometers with molecules or nanoparticles, and mesoscopic mechanical resonators in superposition of displacement states.

The key advantage of this platform is direct access to fringe visibility as a continuous, high-resolution observable. Standard decoherence predicts smooth exponential fringe decay governed by environment-induced dephasing. The crystallisation model predicts that fringe-loss dynamics carry additional structure: constraint-geometry dependence, non-exponential envelopes, and bias signatures tied to path asymmetry in the constraint manifold rather than in the Hilbert-space amplitudes.

This platform targets SGT-2 (constraint-geometry dependence), SGT-3 (transition-time scaling), and SGT-5 (metastable pre-crystallisation regime). It is a medium-to-high difficulty platform with an estimated timeline of 1--2 years for photonic implementations, 2--3 years for matter-wave and mesoscopic systems.

---

## State Representation

The path-superposition density matrix in a two-path interferometer is:

$$\rho = \begin{pmatrix} |a|^2 & a b^* e^{i\phi} \\ a^* b\, e^{-i\phi} & |b|^2 \end{pmatrix}$$

where $|a|^2 + |b|^2 = 1$ are the path amplitudes and $\phi$ is the relative phase between paths.

For multi-path interferometers (diffraction gratings, multi-slit), the state generalises to an $n \times n$ density matrix:

$$\rho_{jk} = c_j c_k^* e^{i\phi_{jk}}$$

Fringe visibility is directly related to the off-diagonal magnitude:

$$\mathcal{V} = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}} = 2|a||b| \cdot |\rho_{01}| / (|a|^2 |b|^2)^{1/2}$$

For balanced paths ($|a| = |b|$): $\mathcal{V} = 2|\rho_{01}|$.

The crystallisation operator acts on $\rho(t)$ as the system evolves from coherent superposition toward a path-resolved (crystallised) state.

---

## Control Variables

| Variable | Physical Realisation | Role in VFD Framework |
|----------|---------------------|----------------------|
| Path imbalance $\delta L$ | Optical path length difference; arm asymmetry | Modifies constraint geometry without changing amplitudes; probes $\eta$ |
| Environmental noise $\sigma_{\mathrm{env}}$ | Vibration, thermal radiation, gas scattering | Controls decoherence rate; maps to $\Gamma$ and $\lambda$ |
| Controlled phase shift $\phi_{\mathrm{ext}}$ | Piezo-driven mirror, electrostatic phase plate | Scans the interference pattern; accesses different points on the constraint landscape |
| Which-way coupling $g_{\mathrm{ww}}$ | Detector at one path; entangling interaction with marker particle | Introduces measurement backaction; maps to $\kappa_B$ |
| Beam splitter ratio | Reflectivity/transmissivity of splitter | Controls path amplitudes $|a|^2, |b|^2$; separable from constraint geometry |
| Particle mass $m$ | Choice of photon, neutron, atom, molecule, nanoparticle | Scales decoherence and Penrose-OR threshold; crystallisation-model discriminant vs M5 |
| Propagation distance $L$ | Interferometer arm length | Sets evolution time on the crystallisation flow |

---

## Observables

| Observable | Symbol | How Measured | VFD Relevance |
|-----------|--------|-------------|---------------|
| Fringe visibility | $\mathcal{V}$ | Intensity modulation depth at output | Primary coherence measure; tracks crystallisation progress |
| Fringe-loss time | $\tau_{\mathcal{V}}$ | Time (or equivalent path length) for $\mathcal{V}$ to drop below threshold | SGT-3: scaling with constraint and environment parameters |
| Visibility envelope shape | $\mathcal{V}(t)$ | Time-resolved visibility measurement | The crystallisation model predicts the possibility of non-exponential structure; decoherence predicts exponential |
| Output bias | $B = (N_1 - N_2)/(N_1 + N_2)$ | Asymmetry of detection counts at the two output ports | SGT-4: basin preference under constraint asymmetry |
| Entropy of output distribution | $H$ | Shannon entropy of port-count statistics | SGT-1: structured selection signature |
| Which-way information | $\mathcal{D}$ (distinguishability) | Correlation with marker particle state | Complementarity relation: $\mathcal{V}^2 + \mathcal{D}^2 \leq 1$; the crystallisation model may modify the boundary |
| Recurrence structure | Plateau count in $\mathcal{V}(t)$ | Time-resolved visibility tracking | SGT-5: metastable plateaus during fringe loss |

---

## Parameter Mapping

### Primary crystallisation functional

$$F[\rho] = \alpha\, R_c[\rho] + \beta\, E[\rho] - \gamma\, Q[\rho]$$

| Canonical Parameter | Symbol | Interferometric Realisation | How to Tune |
|--------------------|--------|----------------------------|-------------|
| Closure weight | $\alpha$ | Determines how strongly constraint mismatch between the two paths drives crystallisation | Set by interferometer geometry and coupling to environment; not independently tunable but varies with $\delta L$ and $g_{\mathrm{ww}}$ |
| Energy weight | $\beta$ | Energetic cost of maintaining path superposition; related to particle kinetic energy and potential difference between arms | Tuned by particle velocity, gravitational potential difference, or electrostatic bias between paths |
| Coherence weight | $\gamma$ | Reward for maintaining phase coherence between paths; related to fringe contrast utility | Set by the interferometric measurement configuration; stronger when detection is phase-sensitive |
| Noise strength | $\lambda$ | Amplitude of stochastic perturbations: vibration, thermal photon scattering, residual gas collisions | Controlled by vacuum level, vibration isolation, temperature; deliberately injected via shaker or noise source |
| Constraint sensitivity | $\eta$ | $\eta = \partial \mathcal{V} / \partial (\delta L)$ at fixed amplitudes: rate of visibility change with path asymmetry | Measured by sweeping $\delta L$ while holding beam splitter ratio fixed; nonzero $\eta$ beyond standard prediction is a crystallisation signature |
| Environment coupling | $\Gamma$ | Total decoherence rate from all environmental channels: thermal radiation, gas scattering, vibration-induced dephasing | $\Gamma = 1/\tau_{\mathrm{dec}}$ where $\tau_{\mathrm{dec}}$ is the standard decoherence time; tuned by vacuum, temperature, isolation |
| Closure residual | $R_c$ | Mismatch between the current path-superposition state and the nearest constraint-compatible (crystallised) state | Computed from tomographic reconstruction; $R_c \to 0$ as $\mathcal{V} \to 0$ or $\mathcal{V} \to 1$ (pure states); maximal at intermediate coherence with asymmetric constraints |
| Boundary coupling | $\kappa_B$ | Coupling between the interferometric paths and external degrees of freedom that carry which-way information | Tuned by which-way detector coupling $g_{\mathrm{ww}}$; marker particle entanglement strength |
| Coherence coupling | $\kappa_Q$ | Rate at which phase information recirculates within the interferometer and feeds back into the crystallisation flow | Related to cavity finesse (if paths are recycled), or to feedback loops in adaptive interferometry |

---

## Expected Usable Regimes

| Regime | Condition | Signature Accessibility |
|--------|-----------|------------------------|
| High visibility, low noise | $\mathcal{V} > 0.95$, $\lambda \ll \Gamma$ | Baseline regime; indicates standard fringe behaviour |
| Intermediate visibility, constraint asymmetry | $\mathcal{V} \in [0.3, 0.8]$, $\delta L \neq 0$ | Primary crystallisation test zone: fringe-loss dynamics should show constraint-dependent structure |
| Mesoscopic mass regime | $m > 10^4$ amu | Discriminates crystallisation model from Penrose OR: the crystallisation model predicts constraint-geometry dependence, OR predicts mass-only dependence |
| Strong which-way coupling | $g_{\mathrm{ww}} \sim 1$ (full which-way) | Boundary coupling saturated; crystallisation should be fast; tests $\kappa_B$ dependence |
| Controlled decoherence sweep | Sweep $\Gamma$ from $\Gamma \ll 1/\tau_{\mathrm{flight}}$ to $\Gamma \gg 1/\tau_{\mathrm{flight}}$ | Maps the full crossover; identifies where the crystallisation model deviates from standard decoherence |

**Primary target regime:** Intermediate visibility with non-trivial path asymmetry: $\mathcal{V} \in [0.3, 0.8]$, $\delta L / L \in [0.01, 0.1]$, $\Gamma \cdot \tau_{\mathrm{flight}} \in [0.1, 10]$.

---

## Dominant Confounders

| Confounder | Effect | Mitigation |
|-----------|--------|------------|
| Vibration-induced phase noise | Washes out fringes; mimics decoherence | Active vibration isolation; common-mode rejection; short integration times |
| Beam misalignment | Reduces visibility via geometric mismatch, not decoherence | Automated alignment feedback; spatial mode filtering |
| Detector dark counts and efficiency asymmetry | Introduces artificial bias $B \neq 0$ | Calibrate detectors independently; swap detectors between ports |
| Thermal decoherence (for massive particles) | Path separation creates thermal-radiation which-way information | Operate in cryogenic environment; choose internal-state-insensitive species |
| Gravitational sag | Mass-dependent path deviation; conflates crystallisation-model and OR signatures | Horizontal interferometer geometry; control for gravitational effects |
| Classical wave effects | Classical interference patterns in multi-photon regime | Use heralded single-particle sources; verify antibunching |
| Slow drift in path length | Systematic phase drift mimics structured fringe-loss dynamics | Active stabilisation; interleave reference measurements |

---

## Calibration Path

### Step 1: Interferometer characterisation
- Maximise fringe visibility with balanced beam splitter and aligned paths.
- Measure $\mathcal{V}_{\max}$ and compare to theoretical limit.
- Characterise all visibility-reducing instrumental effects: misalignment, mode mismatch, detector asymmetry.

### Step 2: Decoherence baseline
- Measure $\mathcal{V}(t)$ or $\mathcal{V}(\Gamma)$ under controlled environmental conditions.
- Fit to standard decoherence model: $\mathcal{V}(t) = \mathcal{V}_0 \exp(-\Gamma t)$.
- Extract $\Gamma$ and verify consistency with known environmental coupling.
- This indicates the null-hypothesis envelope.

### Step 3: Path-asymmetry sweep (constraint geometry)
- Introduce controlled path imbalance $\delta L$ without changing beam splitter ratio.
- Measure $\mathcal{V}(\delta L)$ at fixed $\Gamma$.
- Standard prediction: $\mathcal{V}$ depends only on temporal/spatial coherence length, not on $\delta L$ per se (for $\delta L$ within coherence length).
- Crystallisation model prediction: $\mathcal{V}$ dynamics (not just final value) depend on constraint geometry encoded by $\delta L$.
- Compute $\eta = \partial \mathcal{V}_{\mathrm{dynamics}} / \partial (\delta L)$.

### Step 4: Which-way coupling sweep
- Gradually increase $g_{\mathrm{ww}}$ from 0 to maximal which-way information.
- Track $\mathcal{V}(g_{\mathrm{ww}})$ and $\tau_{\mathcal{V}}(g_{\mathrm{ww}})$.
- Compare fringe-loss time scaling to crystallisation model: $\tau \sim 1/(a R_c + b Q + c \kappa_B + d \Gamma)$.
- Compare to standard complementarity: $\mathcal{V}^2 + \mathcal{D}^2 \leq 1$.

### Step 5: Bias measurement
- Under path-asymmetric constraints ($\delta L \neq 0$) with balanced amplitudes ($|a| = |b|$), measure output port statistics.
- Compute bias $B = (N_1 - N_2)/(N_1 + N_2)$.
- Born-rule null: $B = 0$ for balanced amplitudes regardless of path asymmetry.
- Crystallisation model prediction: $B \neq 0$ when constraint geometry is asymmetric.
- Binomial test on $B$ with $p < 0.001$ threshold.

### Step 6: Visibility envelope analysis
- Acquire high-time-resolution $\mathcal{V}(t)$ traces for $\geq 1000$ interferometer traversals.
- Test for non-exponential structure: plateaus, inflection points, multi-timescale behaviour.
- Fit to crystallisation model with metastable intermediate and to standard single-exponential.
- Compare via AIC/BIC.

### Step 7: Mass scaling (if available)
- Repeat Steps 2--6 for particles of different mass.
- Map $\tau_{\mathcal{V}}(m)$ and compare to Penrose-OR prediction ($\tau \sim \hbar / \Delta E_G \propto 1/m$) vs crystallisation model prediction (depends on constraint geometry, not mass alone).

---

## Practical Considerations

- **Photonic implementation (nearest-term):** Single-photon Mach-Zehnder with fibre or free-space paths. High repetition rate (MHz), excellent stability, but limited mass regime. Best for testing constraint-geometry signatures at low mass.

- **Neutron interferometry:** Perfect-crystal interferometers provide exceptional path stability. Moderate mass ($m \approx 1$ amu). Well-established technique with decades of precision data. Constraint geometry can be modified by inserting phase objects in one arm.

- **Molecular/nanoparticle interferometry:** Talbot-Lau or OTIMA interferometers with large molecules ($10^3$--$10^5$ amu). Accesses mesoscopic regime where Penrose-OR and crystallisation model predictions diverge. Technically demanding but several groups worldwide have demonstrated the capability.

- **Sample sizes:** Fringe visibility measurements require $\geq 10^3$ detected particles per phase point, with $\geq 20$ phase points per fringe. For bias measurements, $\geq 10^5$ total detections to resolve $B$ at the 0.1% level.

- **Systematic error budget:** Dominant contributions from vibration ($\sim 10^{-3}$ rad rms phase), detector asymmetry ($\sim 0.1\%$ efficiency difference), and alignment drift ($\sim 10^{-4}$ rad/hour). All must be characterised and subtracted before interpreting residuals as crystallisation signatures.

- **Blinding:** Phase-scan data should be analysed with constraint-configuration labels hidden. Pre-register the fitting procedure and model-comparison criteria.

- **Connection to predictions:** This platform tests PRED-002 (transition-time scaling via $\tau_{\mathcal{V}}$), PRED-003 (basin preference via bias $B$), PRED-004 (metastable plateaus in visibility envelope), and PRED-006 (constraint-geometry sensitivity via $\eta$).
