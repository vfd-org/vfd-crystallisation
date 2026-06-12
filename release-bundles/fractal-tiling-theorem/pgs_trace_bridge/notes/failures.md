# Failures / self-fooling guards triggered — WO-VFD-PGS-TRACE-BRIDGE-001

- **σ-probe vacuity (caught):** `R(σ)=|Φ(σ)−Φ(1−σ)|=0` at σ=1/2 for all weights. Had we
  reported "minimum at σ=1/2" as a PASS, it would have been a false positive — random
  weights pass identically. Demonstrated with the `random` null.
- **Self-adjointness vacuity (caught):** symmetric tridiagonal ⇒ real eigenvalues for any
  diagonal. The `random` diagonal passes with the same sym-error (0) and real spectrum.
- **Chamber-symmetry near-null:** real vs gap-local-shuffle differ by only 0.046
  (local autocorrelation), not a structural symmetry.
- **No critical-line signal:** nothing in E/H produced a σ=1/2 feature absent from the
  random / log / Λ comparators.
