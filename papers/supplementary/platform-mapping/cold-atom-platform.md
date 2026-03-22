# Platform Mapping Sheet: Cold Atom / Optical Lattice System (EP3)

## Platform Overview

The cold atom platform uses ultracold atoms confined in programmable optical potentials -- double wells, multi-well lattices, and engineered potential landscapes -- to test crystallisation in systems with rich basin structure. Unlike the qubit (two basins) or interferometer (two paths), optical lattice systems provide access to multi-level occupation, tuneable inter-particle interactions, and programmable constraint geometries with many competing attractors.

The central experimental idea is to prepare atoms in a symmetric or controlled superposition across multiple wells, then engineer the constraint geometry (barrier shape, lattice topology, interaction strength) independently of the well-depth amplitudes. The crystallisation model predicts that the final basin occupation depends on constraint geometry, not solely on $|c_k|^2$. Standard quantum mechanics predicts that only amplitudes matter for measurement outcomes.

This platform targets SGT-2 (constraint-geometry dependence), SGT-4 (basin preference), and SGT-5 (metastable plateaus). It is a high-difficulty platform with an estimated timeline of 2--3 years.

---

## State Representation

### Single particle in multi-well potential

For $n$ wells, the state is an $n$-level system:

$$\rho = \sum_{j,k} \rho_{jk} |j\rangle\langle k|$$

where $|j\rangle$ denotes localisation in well $j$. Diagonal elements $\rho_{jj}$ give well-occupation probabilities; off-diagonal elements $\rho_{jk}$ encode inter-well coherence.

### Many-body lattice system

For $N$ atoms in $M$ sites, the state lives in the Fock space:

$$|\Psi\rangle = \sum_{\{n_j\}} c_{\{n_j\}} |n_1, n_2, \ldots, n_M\rangle$$

The density matrix $\rho$ acts on the full $N$-particle Hilbert space. Experimentally, the accessible observables are site-occupation numbers $\langle n_j \rangle$ and their correlations.

### Bose-Hubbard regime

When the system is well-described by the Bose-Hubbard model:

$$H = -J \sum_{\langle j,k \rangle} a_j^\dagger a_k + \frac{U}{2} \sum_j n_j(n_j - 1) + \sum_j \epsilon_j n_j$$

the tunnelling $J$, interaction $U$, and site energies $\epsilon_j$ parameterise the constraint landscape. The crystallisation operator acts on the evolving density matrix within this landscape.

---

## Control Variables

| Variable | Physical Realisation | Role in VFD Framework |
|----------|---------------------|----------------------|
| Lattice depth $V_0$ | Laser intensity of standing wave | Controls tunnelling $J \propto e^{-\sqrt{V_0}}$; sets basin barrier heights |
| Interaction strength $U$ | Feshbach resonance (magnetic field), atom density | Inter-particle constraint coupling; modifies basin geometry via mean-field shifts |
| Site energy perturbation $\delta\epsilon_j$ | Local AC Stark shift, magnetic gradient | Controlled constraint asymmetry; tilts the landscape without changing coherent amplitudes |
| Barrier shape | Holographic beam shaping, multi-frequency lattice | Modifies constraint geometry (barrier curvature, tunnelling paths) independently of well depths |
| Bath coupling $\Gamma_{\mathrm{bath}}$ | Spontaneous emission rate, background gas collision rate, deliberate photon scattering | Controls environment coupling $\Gamma$; tuned by laser detuning and vacuum quality |
| Atom number $N$ | Loading protocol, evaporative cooling endpoint | Scales many-body effects; more atoms increase interaction-driven constraint complexity |
| Temperature $T$ | Evaporative cooling depth | Sets thermal noise floor; controls $\lambda$ |
| Lattice geometry | 1D, 2D, 3D; triangular, square, honeycomb | Defines constraint topology and coordination number |

---

## Observables

| Observable | Symbol | How Measured | VFD Relevance |
|-----------|--------|-------------|---------------|
| Site occupation / dwell time | $\langle n_j \rangle$, $\tau_{\mathrm{dwell}}$ | Fluorescence imaging, quantum gas microscope, band mapping | Basin preference and dwell-time statistics |
| Pattern selection | Which spatial pattern (Mott insulator, superfluid, density wave) emerges | Time-of-flight imaging, in-situ density measurement | SGT-4: does the selected pattern track constraint geometry or amplitudes? |
| Basin preference index | $\mathrm{BPI}_k = N_k / N_{\mathrm{trials}}$ | Repeated preparation and measurement of final state | Direct test of PRED-003 |
| Path geometry | Trajectory of occupation numbers $\{n_j(t)\}$ during relaxation | Time-resolved in-situ imaging with quantum gas microscope | SGT-6: path reproducibility |
| Coherence envelope | $|\rho_{jk}(t)|$ for adjacent sites | Interference after lattice release; noise correlations | Tracks crystallisation progress; distinguishes coherent convergence from decoherence |
| Entropy | $S = -\mathrm{Tr}(\rho \ln \rho)$ (or approximation via fluctuations) | Fluctuation thermometry, equation-of-state measurements | Global state-resolution indicator |
| Metastable plateau | Dwell time in intermediate configuration before final pattern | Time-resolved density measurement | SGT-5: structured intermediates |

---

## Parameter Mapping

### Primary crystallisation functional

$$F[\rho] = \alpha\, R_c[\rho] + \beta\, E[\rho] - \gamma\, Q[\rho]$$

| Canonical Parameter | Symbol | Cold Atom Realisation | How to Tune |
|--------------------|--------|----------------------|-------------|
| Closure weight | $\alpha$ | Weight of constraint mismatch: how strongly the lattice geometry and interaction constraints drive the system toward a specific configuration | Set by lattice topology and dimensionality; not directly tunable but changes discretely with lattice type |
| Energy weight | $\beta$ | Energetic cost from kinetic energy, interaction energy, and site-energy terms in the Bose-Hubbard Hamiltonian | Tuned via $J$ (lattice depth), $U$ (Feshbach field), and $\epsilon_j$ (local potentials) |
| Coherence weight | $\gamma$ | Reward for maintaining inter-site phase coherence; related to superfluid order parameter | Larger in shallow lattices (large $J/U$) where superfluid coherence is energetically favoured |
| Noise strength | $\lambda$ | Thermal fluctuations, quantum projection noise, technical noise (laser intensity, pointing) | Controlled by temperature $T$, atom number $N$ (projection noise $\sim 1/\sqrt{N}$), laser stability |
| Constraint sensitivity | $\eta$ | $\eta = \partial (\mathrm{BPI}) / \partial (\text{barrier shape})$ at fixed well depths | Measured by sweeping barrier curvature or lattice topology while holding $\epsilon_j$ fixed |
| Environment coupling | $\Gamma$ | Spontaneous emission rate $\Gamma_{\mathrm{sp}}$ plus background gas collision rate plus any deliberate decoherence channel | $\Gamma_{\mathrm{sp}} = (\Omega^2 / 4\Delta_L^2) \gamma_{\mathrm{nat}}$ where $\Delta_L$ is lattice detuning; tuned by laser intensity and detuning |
| Closure residual | $R_c$ | Mismatch between current occupation pattern and nearest constraint-compatible configuration (Mott state, density wave, etc.) | Computed from measured $\{n_j\}$ compared to predicted ground-state pattern; $R_c \to 0$ at crystallisation |
| Boundary coupling | $\kappa_B$ | Coupling at the lattice edge: harmonic confinement gradient, lattice termination effects, contact with thermal reservoir at boundary | Tuned by harmonic trap frequency; edge sites can be individually addressed |
| Coherence coupling | $\kappa_Q$ | Rate at which inter-site coherence feeds back into the occupation dynamics; related to tunnelling rate $J$ and superfluid stiffness | $\kappa_Q \propto J$; tuned by lattice depth |

---

## Expected Usable Regimes

| Regime | Condition | Signature Accessibility |
|--------|-----------|------------------------|
| Superfluid regime | $J/U \gg 1$ | High inter-site coherence; $\gamma$ dominates; crystallisation competes with delocalisation; tests coherence coupling $\kappa_Q$ |
| Mott insulator regime | $J/U \ll 1$ | Strong constraint-driven localisation; $\alpha$ dominates; basin structure is pronounced; best for BPI measurements |
| SF-MI crossover | $J/U \sim 1$ | Richest crystallisation dynamics; multiple competing configurations; metastable plateaus expected |
| Tilted lattice | $\delta\epsilon \neq 0$, well depths equal | Direct test of constraint-geometry sensitivity: $\eta \neq 0$ under the crystallisation model, $\eta = 0$ under Born rule if amplitudes are symmetric |
| Frustrated lattice (triangular) | Geometric frustration in constraint satisfaction | The crystallisation model predicts specific pattern selection from frustrated landscape; standard theory predicts degenerate manifold |
| Low temperature, low noise | $k_B T \ll J, U$; $\lambda \ll J$ | Cleanest regime for crystallisation signatures; thermal noise does not mask deterministic selection |

**Primary target regime:** SF-MI crossover ($J/U \in [0.5, 2]$), low temperature ($k_B T < 0.1 J$), with controlled barrier-shape asymmetry.

---

## Dominant Confounders

| Confounder | Effect | Mitigation |
|-----------|--------|------------|
| Harmonic trap inhomogeneity | Creates position-dependent $\epsilon_j$ mimicking constraint asymmetry | Use box traps (flat-bottom potentials); characterise and subtract trap curvature |
| Heating during hold time | Atom loss and energy increase during lattice hold | Minimise hold times; characterise heating rate; restrict analysis to low-loss windows |
| Finite imaging resolution | Cannot resolve single-site occupation in dense lattices | Use quantum gas microscope with single-site resolution; restrict to low-density regimes |
| Interaction-driven redistribution | $U$-driven dynamics alter occupation independently of crystallisation | Map the standard Bose-Hubbard phase diagram first; test crystallisation model predictions only in regimes where standard theory makes definite and different predictions |
| Atom number fluctuations | Shot-to-shot $N$ variation broadens occupation statistics | Post-select on measured total atom number; require $\delta N / N < 1\%$ |
| Three-body loss | Density-dependent atom loss at high occupation | Operate at low filling ($\bar{n} \leq 2$); monitor loss rates |
| Adiabaticity failure | Non-adiabatic lattice ramps excite higher bands | Calibrate ramp rates against band-excitation thresholds; verify adiabaticity via band-mapping |

---

## Calibration Path

### Step 1: Lattice characterisation
- Calibrate lattice depth $V_0$ via parametric heating resonance or Kapitza-Dirac diffraction.
- Measure tunnelling rate $J$ from expansion dynamics.
- Characterise trap frequencies and harmonic confinement.
- Map site energies $\epsilon_j$ via spectroscopic or in-situ density measurements.

### Step 2: Interaction calibration
- Measure $U$ via clock-shift spectroscopy or interaction-energy measurements in deep lattice.
- Characterise Feshbach resonance if used to tune $U$.
- Map the $J/U$ ratio across the accessible lattice-depth range.

### Step 3: Standard phase diagram baseline
- Map the SF-MI phase diagram by sweeping $V_0$ and measuring coherence (time-of-flight) and number fluctuations.
- Verify agreement with standard Bose-Hubbard predictions.
- This is the null baseline: any crystallisation signature must appear as a deviation from this well-understood physics.

### Step 4: Symmetric-amplitude, asymmetric-constraint preparation
- Prepare atoms in a double-well or multi-well potential with equal well depths ($\epsilon_j = \epsilon$ for all $j$).
- Modify barrier shape (height, width, curvature) while keeping well depths symmetric.
- Measure BPI across $\geq 8$ barrier configurations, $\geq 5000$ trials each.
- Born-rule null: BPI = $1/n$ for $n$ wells with equal amplitudes.
- Crystallisation model prediction: BPI deviates from $1/n$, correlating with barrier geometry.

### Step 5: Dwell-time and plateau measurement
- Prepare atoms in excited or unstable configuration (e.g., population-inverted double well).
- Monitor occupation dynamics $\{n_j(t)\}$ with time-resolved imaging.
- Search for metastable plateaus: regions where $|d\langle n_j\rangle/dt| < \epsilon$ for duration $> \delta$.
- Measure dwell-time statistics and compare to crystallisation model predictions.

### Step 6: Constraint-sensitivity extraction
- Sweep barrier shape parameter $s$ (e.g., barrier curvature) at fixed well depths.
- Compute $\eta = \partial(\mathrm{BPI})/\partial s$.
- Standard prediction: $\eta = 0$ (BPI depends only on amplitudes).
- Crystallisation model prediction: $\eta \neq 0$ with specific functional form.

### Step 7: Environment coupling sweep
- Deliberately increase decoherence by reducing lattice laser detuning (more spontaneous emission) or introducing controlled photon scattering.
- Map BPI and dwell-time statistics as functions of $\Gamma$.
- Identify the $\Gamma$ threshold above which crystallisation signatures are washed out.

### Step 8: Path reproducibility
- For identical preparations, track full occupation trajectories $\{n_j(t)\}$ across $\geq 100$ trials.
- Compute trajectory distance $D_{\mathrm{traj}} = \sum_j \int |n_j^{(a)}(t) - n_j^{(b)}(t)| dt$.
- Compare to expected stochastic spread from quantum projection noise.

---

## Practical Considerations

- **Experimental complexity:** This is the most demanding platform in terms of setup and calibration. A quantum gas microscope with single-site resolution, programmable potentials, and time-resolved imaging is the gold-standard instrument. Several groups worldwide operate such systems (Harvard, MPQ Munich, Princeton, etc.).

- **Sample sizes:** BPI measurements require $\geq 5000$ experimental cycles per barrier configuration, with each cycle taking 10--60 seconds (BEC production, lattice loading, hold, imaging). A single configuration therefore requires 14--84 hours. A full sweep of 8 configurations needs 5--28 days of continuous operation.

- **Key advantage:** The multi-well system provides the richest basin structure of any quantum platform. It can support many competing attractors, frustrated geometries, and non-trivial constraint topologies that are inaccessible to two-level systems.

- **Key disadvantage:** The long cycle time limits statistics. Unlike the qubit platform (MHz repetition) or the analog oscillator (continuous operation), cold atom experiments accumulate data slowly. This is the primary bottleneck.

- **Discriminating crystallisation model from standard many-body physics:** The critical test is whether occupation statistics depend on barrier geometry at fixed well depths. Standard Bose-Hubbard theory predicts that the ground state depends on $J$, $U$, and $\epsilon_j$; barrier shape only enters through $J$ (the tunnelling rate). The crystallisation model predicts that the full barrier shape -- not just the tunnelling amplitude it generates -- influences the crystallisation outcome. Testing this requires independently varying barrier shape while controlling $J$ (e.g., by compensating with lattice depth).

- **Connection to predictions:** This platform primarily tests PRED-003 (basin preference under asymmetric constraints), PRED-004 (metastable plateaus), PRED-005 (path reproducibility), and PRED-006 (constraint-geometry sensitivity).

- **Staging strategy:** Begin with a simple double-well configuration (2 basins) to establish the BPI measurement protocol, then extend to multi-well and lattice configurations for richer basin structure. Frustrated geometries (triangular lattice) represent the highest-impact but also highest-risk experiments.
