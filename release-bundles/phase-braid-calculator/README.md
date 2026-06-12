# VFD Phase-Braid Calculator

**Phase-braid arithmetic and boundary-closure engine.**

A calculator that behaves like a normal calculator on the surface — ordinary
arithmetic is always correct — but lifts every integer into a richer
*phase-braid* state and lets you study whether arithmetic, Collatz dynamics,
prime structure, and finite-window self-adjointness share one computational
grammar.

> Numbers are linear bookkeeping traces of deeper phase-braid closure.
> This tool is the instrumentation to test that claim. It does **not** claim to
> prove Collatz or RH; it builds the search structure.

This is **VFD Calculator II**. Where the original VFD calculator was about
field/geometry constants, this one is about the *arithmetic substrate itself*.

## The lift

```
n  ->  VFDNumber(n) = {
  value, parity, triad_phase, residues, factors, is_prime,
  v2, v3, phi_log_phase, braid_label, closure_class
}
```

Braid legs are read off the triad phase: `0 -> A`, `1 -> B`, `2 -> C`.

## Install

```bash
pip install -e .          # exposes the `vfdcalc` command
# or run in place:
PYTHONPATH=src python3 -m vfd_phase_braid.cli inspect 27
```

Dependencies: `numpy`, `scipy` (only `self-adjoint` needs them).

## Modes

### 1. Number inspection
```bash
vfdcalc inspect 27
```
```
value:        27
parity:       odd
triad phase:  0 mod 3   (braid leg A)
factorisation:3^3
v2 (2-adic):  0
v3 (3-adic):  3
closure role: triadic expansion node
```

### 2. Lifted arithmetic
```bash
vfdcalc add 8 13
```
Reports the ordinary result *and* the braid transition `C + B -> A`, the
compression delta, and the triad-homomorphism residual (0 = the operation
respects the triad grading). Also: `subtract`, `multiply`, `divide`, `power`.

### 3. Collatz / closure
```bash
vfdcalc collatz 27 --max-steps 10000
```
Full trajectory, parity/triad sequences, the odd-to-odd compressed map
`m -> (3m+1)/2^a`, the per-step capacity `q_i = a_i·log2 − log3`, cumulative
capacity, and a closure-regime verdict.

```bash
vfdcalc capacity 27          # Q = compression − expansion verdict
```

### 4. Prime trace
```bash
vfdcalc primes --limit 10000 --modulus 6
```
Primes, gaps, triad/residue distributions, gap-phase distribution, and the
Chebyshev-style imbalance between phases 1 and 2.

### 5. Self-adjoint finite window
```bash
vfdcalc self-adjoint collatz --limit 16
```
Builds the deterministic transition matrix `T` on states `1..N` and searches
for a symmetric form `B` with `B T = Tᵀ B`, reporting the residual
`‖BT − TᵀB‖`, the signature of `B` (positive-definite / indefinite / singular),
and a verdict on whether the system admits a balanced hidden geometry. The
dense solve is `O(N⁶)`, so `N` is capped (default 48).

### Reports
```bash
vfdcalc report collatz 871 --format markdown -o report.md
vfdcalc report primes 10000 --format csv -o primes.csv
```
Any command also accepts `--json` for machine-readable output.

## Architecture

| Module                 | Responsibility |
|------------------------|----------------|
| `phase_maps.py`        | parity, residues, p-adic valuations, factorisation, primality, φ-log phase |
| `vfd_number.py`        | the `VFDNumber` lift and closure-class taxonomy |
| `lifted_arithmetic.py` | operations over `VFDNumber` with phase transitions |
| `collatz_closure.py`   | trajectory, compressed map, capacity, closure regime |
| `prime_trace.py`       | sieve, gaps, residue/phase distributions |
| `self_adjoint.py`      | finite transition matrix + `B`-form residual test |
| `boundary_capacity.py` | the `Q = compression − expansion` model |
| `report_generator.py`  | JSON / CSV / Markdown export |
| `cli.py`               | the `vfdcalc` command-line interface |

## Tests

```bash
PYTHONPATH=src python3 -m pytest tests/ -q
```

Covers number inspection (1..60 sweep + 1e9 values), lifted arithmetic
(triad-homomorphism residual = 0), Collatz closure (1..120 sweep vs reference
step counts; the 27 and 871 trajectories), prime counting (π(10000) = 1229),
and the self-adjoint sanity check.

## Roadmap

- **Phase 1 (this bundle):** Python CLI calculator + tests.
- **Phase 2:** Markdown reports and plots (trajectory, cumulative capacity,
  triad cycle, prime-gap phase, self-adjoint residual heatmap).
- **Phase 3:** Web UI.
- **Phase 4:** Connect to the existing VFD / RH / triad simulators.

## License

CC BY 4.0 — see `LICENSE`.
