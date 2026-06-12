# Data access

External datasets used in the empirical notes. None are redistributed in
this repository. Each entry below lists the dataset, public source,
expected local folder path, preprocessing command, the exact scripts to
run, and the expected headline result.

## OpenNeuro EEG datasets

### `ds005620` — propofol sedation EEG (Note B, Note C)

| Field | Value |
|---|---|
| Source | https://openneuro.org/datasets/ds005620 |
| License | CC0 |
| Expected path | `external/openneuro/ds005620/` |
| Download | `datalad install https://github.com/OpenNeuroDatasets/ds005620.git` then `datalad get .` |
| Subjects | $n = 14$ |
| Preprocessing | bandpass 0.5–45 Hz, resample to 250 Hz, eyes-closed segments |
| Script | `notes/Note-B-cortical-phase-closure/repro/run_ds005620.py` |
| Expected result | 14/14 positive, $t = 7.11$, $d_z = 1.90$, $p < 2 \times 10^{-4}$ |

### `ds004541` — clinical anaesthesia EEG (Note B)

| Field | Value |
|---|---|
| Source | https://openneuro.org/datasets/ds004541 |
| Expected path | `external/openneuro/ds004541/` |
| Subjects | $n = 7$ |
| Preprocessing | as in `ds005620` |
| Script | `notes/Note-B-cortical-phase-closure/repro/run_ds004541.py` |
| Expected result | 7/7 in-sample, $t = 5.25$; LOSO $d_z = 1.16$, Jaccard $= 0.52$ |

### `ds007609` — trait anxiety resting EEG (Note D)

| Field | Value |
|---|---|
| Source | https://openneuro.org/datasets/ds007609 |
| Expected path | `external/openneuro/ds007609/` |
| Subjects | $n = 24$ (high-STAI vs low-STAI quartile contrast) |
| Phenotype file | `phenotype/stai.tsv` (STAI trait scores) |
| Preprocessing | bandpass 0.5–45 Hz, eyes-closed resting segment ≥20 s |
| Script | `notes/Note-D-trauma-cortical-closure/repro/run_ds007609.py` |
| Expected result | Cohen's $d = +0.79$, Welch $t = +1.93$, $p = 0.073$ |

### `ds004315` — mood manipulation EEG (Note D)

| Field | Value |
|---|---|
| Source | https://openneuro.org/datasets/ds004315 |
| Expected path | `external/openneuro/ds004315/` |
| Subjects | $n = 50$ (sad vs neutral arms) |
| Preprocessing | bandpass 0.5–45 Hz |
| Script | `notes/Note-D-trauma-cortical-closure/repro/run_ds004315.py` |
| Expected result | Cohen's $d = +0.70$, Welch $t = +2.47$, $p = 0.018$ (treated as CAD-v1.5 calibration addendum) |

### `ds004504` — Alzheimer's / FTD vs healthy EEG (Note C, Note D)

| Field | Value |
|---|---|
| Source | https://openneuro.org/datasets/ds004504 |
| Expected path | `external/openneuro/ds004504/` |
| Subjects | $n_{\mathrm{AD}} = 36$, $n_{\mathrm{FTD}} = 23$, $n_{\mathrm{Healthy}} = 29$ |
| Preprocessing | bandpass 0.5–45 Hz |
| Script | `notes/Note-C-closure-as-distance/repro/run_ds004504.py` |
| Expected result | AD: $d = -0.31$ (diagnostic predicted FAIL, observed FAIL); FTD: $d = +0.02$ (diagnostic predicted PASS, observed FAIL — transparent false positive) |

### `ds005520` — MOBA gaming EEG (Note E)

| Field | Value |
|---|---|
| Source | https://openneuro.org/datasets/ds005520 |
| Expected path | `external/openneuro/ds005520/` |
| Subjects | $n = 20$ (gaming vs eyes-closed rest) |
| Preprocessing | bandpass 0.5–45 Hz |
| Script | `notes/Note-E-flow-cortical-closure/repro/run_ds005520.py` |
| Expected result | $D_5 = 0.78$ FAIL (diagnostic-predicted FAIL); FlowIndex $d_z = -0.26$, n.s. (confirmed FAIL) |

### `ds004505` — table-tennis play vs baseline EEG (Note E)

| Field | Value |
|---|---|
| Source | https://openneuro.org/datasets/ds004505 |
| Expected path | `external/openneuro/ds004505/` |
| Subjects | $n = 25$ |
| Preprocessing | bandpass 0.5–45 Hz |
| Script | `notes/Note-E-flow-cortical-closure/repro/run_ds004505.py` |
| Expected result | $D_5 = 0.67$ FAIL (diagnostic-predicted FAIL); FlowIndex $d_z = +0.06$, n.s. (confirmed FAIL) |

### `ds006802` — collaborative rule-learning hyperscanning EEG (Note F)

| Field | Value |
|---|---|
| Source | https://openneuro.org/datasets/ds006802 |
| Expected path | `external/openneuro/ds006802/` |
| Subjects | 24 dyads, 128-channel BIOSEMI |
| Preprocessing | bandpass 0.5–45 Hz, late-vs-early within-pair contrast |
| Script | `notes/Note-F-hyperscanning-joint-meaning/repro/run_ds006802.py` |
| Expected result | $d_z = +0.39$, paired $t = +1.89$, $p = 0.071$, $17/24$ pairs in predicted direction (moderate-positive trend, below preregistered $d_z > 1.0$ threshold) |

### `ds007471` — musical joint-action hyperscanning EEG (Note F)

| Field | Value |
|---|---|
| Source | https://openneuro.org/datasets/ds007471 |
| Expected path | `external/openneuro/ds007471/` |
| Subjects | 13 pairs × 64-channel BrainVision, 520 trials |
| Preprocessing | bandpass 0.5–45 Hz, duet vs constant-pitch contrast with trial-condition labelling |
| Script | `notes/Note-F-hyperscanning-joint-meaning/repro/run_ds007471.py` |
| Expected result | $d_z = +0.23$ ($9/13$ pairs), $p = 0.43$, honest negative (CAD predicted FAIL a priori) |

## BETSE simulation data (Note A)

| Field | Value |
|---|---|
| Source | https://github.com/betsee/betse |
| Expected path | `external/betse/` |
| Substrate | planarian-shape geometry, $N = 5$ control + $N = 5$ each of 5 perturbations |
| Script | `notes/Note-A-bioelectric-closure/repro/run_betse_panel.py` |
| Expected result | Per-condition basin signatures: K_env $(-,-,+)$, K_mem $(+,+,+)$, na_mem_glb $(-,-,+)$, na_mem_ant $(+,+,+)$ orthogonal, cl_env null |

## ARIA-chess data (Paper III)

| Field | Value |
|---|---|
| Source | github.com/vfd-org/aria-chess |
| Expected path | `external/aria-chess/` |
| Reported metrics | 18 preregistered cortical signatures (17/18 standard, 18/18 refined); 6 v4 EEG independent tests |
| Script | Paper III §sec:aria — references the ARIA-chess kernel; reproduction is upstream-managed |
| Expected result | Reported in Paper III §sec:aria; cited as constructed witness, not proof of consciousness |

## HCP cortical data (Paper III)

| Field | Value |
|---|---|
| Source | Human Connectome Project (https://www.humanconnectome.org/) |
| Access | requires HCP data-use agreement |
| Reported metrics | ARIA participation ratio $+79.78 \sigma$; ARIA degree-std $-11.58 \sigma$ |
| Script | upstream; this repository does not contain the HCP processing pipeline |

## Reproduction workflow

```bash
# 1. Install dependencies
pip install -r repro/shared/requirements.txt
pip install mne pandas  # required for real-data EEG

# 2. Download external data (example for ds005620)
mkdir -p external/openneuro
cd external/openneuro
datalad install https://github.com/OpenNeuroDatasets/ds005620.git
cd ds005620 && datalad get .
cd ../../../

# 3. Run the relevant script
python notes/Note-B-cortical-phase-closure/repro/run_ds005620.py
```

Each script writes its results to `notes/<Note>/repro/output/` as JSON +
PNG. Expected hashes for committed results are in
`repro/shared/expected_hashes.json` where applicable.

## Data licence summary

- OpenNeuro datasets: most under CC0 1.0. Check each dataset's `dataset_description.json` for the actual licence.
- BETSE: BSD 3-Clause (upstream).
- ARIA-chess: see upstream repository.
- HCP: HCP data use agreement; not redistributed.

No external dataset is committed to this repository.
