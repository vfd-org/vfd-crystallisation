# Reproduce locally

All that follows requires only Python 3.8 +.

## Install

```bash
git clone https://github.com/VFD-org/vfd-crystalisation-paper.git
cd vfd-crystalisation-paper
pip install -e .
```

## Run

```bash
vfd verify
```

Expected output (abbreviated):

```
VFD verification · 11 predictions
[PASS] proton_charge_radius           0.0399% ( 0.84σ)  tol 0.1%
[PASS] neutron_charge_radius_squared  1.3107% ( 0.69σ)  tol 5.0%
[PASS] pion_charge_radius             0.2587% ( 0.43σ)  tol 5.0%
[PASS] kaon_charge_radius             1.6793% ( 0.30σ)  tol 5.0%
[PASS] deuteron_charge_radius         0.1050% ( 3.02σ)  tol 1.0%
[PASS] alpha_inverse                  0.0001% tol 0.001%
...
Result: 11 / 11 pass, 0 fail
```

## Inspect a single prediction

```bash
vfd predict proton_charge_radius
```

## Regenerate the credibility report

```bash
vfd report -o docs/report.md
```

## Run the test suite

```bash
pip install -e .[dev]
pytest tests/vfd_core -q
```

## Build this site locally

```bash
pip install -e .[web]
vfd report -o docs/report.md
mkdocs serve
```

Then open `http://127.0.0.1:8000`.

## Modify a primitive and see the DAG react

Want to see the consistency check in action? Edit
`src/vfd_core/shells/assignment.py` — change the proton's shell
assignment from `(2, 3, 4)` to `(2, 3, 5)` — and rerun `vfd verify`.
You'll see the proton radius, the deuteron radius, and any other
predictions that depend on the proton's shell invariants move with
it. That is the DAG exposed as the framework's immune system.
