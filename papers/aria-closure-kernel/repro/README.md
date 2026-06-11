# aria-closure-kernel — repro

Numerical verification of every empirical claim in §3, §4, §5 of the paper.

## Run

```bash
python3 verify_kernel.py
```

Requires Python 3.8+, numpy, scipy. Wallclock ~1 second on a laptop.
No external data, no fitted parameters, no random seed (the
eigendecomposition is deterministic).

## What it computes

1. **600-cell vertex set** — 8 axis + 16 half-integer + 96 φ-mixed
   = 120 unit vectors on S³, all radii within 1e-10 of unit.

2. **Short-edge nearest-neighbour graph** — adjacency where
   ⟨v, w⟩ = φ/2; 720 edges, uniform degree 12.

3. **9-shell H₃ partition** — sizes {1, 12, 20, 12, 30, 12, 20, 12, 1}.

4. **Laplacian spectrum** — nine eigenvalue classes in ℤ[φ]:
   {0, 12-6φ, 12-4φ, 9, 12, 14, 4φ+8, 15, 6φ+6} with multiplicities
   {1, 4, 9, 16, 25, 36, 9, 16, 4} summing to 120.

5. **Operator-norm bound** — ‖C_φ⁻¹‖ = 2.618034 = φ², matching the
   closed-form prediction from §2 of the paper.

6. **Discrete ↔ continuum agreement** — per-vertex Pearson
   correlation between ψ = C_φ⁻¹ e_pole and the continuum kernel
   G(x) = (φ/2) e^(-x/φ) at chord distances:
   - **0.976** (unweighted Laplacian — wins)
   - 0.888 (φ-geometric weights)
   - 0.884 (φ-arithmetic weights)

   Same source vertex, same fixed shift, no parameter fitting.

## Output

Writes `results.json` with all the headline numbers in machine-readable
form. The .tex paper lifts these values verbatim.

## Determinism

The script uses no `numpy.random` calls; the linear algebra path
(`numpy.linalg.eigh`, `numpy.linalg.solve`) is deterministic at
machine precision. Reruns reproduce all reported numbers to at
least 6 decimal places.
