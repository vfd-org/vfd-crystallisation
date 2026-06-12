# route_c / arithmetic_horizon

New route opened after the route_b operator path reached its honest floor
(`RH ⟺ ‖K‖ ≤ 1`, blocked because the prime symbol `−ζ′/ζ` is singular at the
zeros). It asks whether the **maximal-pressure (μ≈1) modes** of the normalised
prime-pressure operator `K = H^{−½}RH^{−½}` define a **stable, prime-specific
"arithmetic horizon" pressure envelope** `Π(log n)` — a candidate new invariant /
"God-Prime envelope."

**Outcome (WO-RH-ARITHMETIC-HORIZON-INVARIANT-001): NOT supported.** The envelope
is generic (a smoothed-PNT `1/√n` surrogate reproduces it at +0.96 overlap and
overshoots the contraction, `μ=1.26>1`), partly a basis artefact (shape drifts
with test-function width), and trivial (the first 3–4 primes, participation
2.68). The prime-specific content of the horizon law is the **cancellation /
explicit-formula fluctuation** that pulls `μ` from 1.26 to 0.9998 — i.e. RH
itself — not a separable envelope. No God Prime. No new invariant.

- `rh_arithmetic_horizon_invariant.py` — the sim (horizon mode + envelope + basis
  test + N-scaling + controls + α_c).
- `RH_ARITHMETIC_HORIZON_INVARIANT_001.md` — full report.
- `results/rh_arithmetic_horizon_invariant_001/` — JSON output.

**Follow-on (WO-RH-BLACK-HOLE-PRIME-FUNNEL-001): black-hole funnel is a
VISUALISATION, not new math.** Plotting primes as compressed infall (depth=log n,
r=1/log n, θ=ξ log n) and studying `ΔR = R_smooth − R_prime`: (1) the radius is
**cosmetic** (bijection; the ξ-spectrum is byte-identical for every radial map);
(2) `ΔR` is two smooth branches (prime / composite), no grooves; (3) the only
prime-specific signal is the ξ-coherence resonating ~10× at every zero (smooth
flat) — which **is** the known explicit formula `−ζ′/ζ` (poles at γ), a
*validation* fact, not new construction. No new invariant, no arithmetic Planck
cell. Plots kept as intuition-only in `funnel_gallery/`.

- `rh_black_hole_prime_funnel.py` — the sim (ΔR + ξ-coherence + compression test +
  controls + validation overlay + plots).
- `RH_BLACK_HOLE_PRIME_FUNNEL_001.md` — full report.
- `funnel_gallery/` — `funnel_3d.png`, `xi_coherence.png`, `cancellation_unwrapped.png` (intuition only).
- `results/rh_black_hole_prime_funnel_001/` — JSON output.

**Anti-circularity:** primes + archimedean + pole only; zeros only as a final
validation overlay. **No proof of RH; no φ; no God Prime.** LOCAL, not pushed.
