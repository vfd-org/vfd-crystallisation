# WS-C — Scattering phase and the zero-count question

On the modular line the scattering matrix is unitary, so

```
φ(½ + it) = e^{iθ(t)},     θ(t) = arg φ(½+it) = −2 arg ξ(1 + 2it).
```

Computed cumulative winding of θ(t) over t ∈ [0.5, 30] (`src/modular_scattering.py`):
the phase winds monotonically on average (0 → ~7.5 over the range), tracking the
argument of the completed zeta.

## Honest reading — what the phase does and does not encode

- **Does:** θ(t) = −2 arg ξ(1+2it) carries ζ's argument; its derivative `−φ′/φ(½+it)`
  is exactly the **continuous-spectrum density** in the Selberg trace formula for the
  modular surface (the term that distinguishes the cuspidal spectrum from the
  Eisenstein continuum). So the phase is genuine ζ spectral data on the line.
- **Does NOT:** the winding does **not** count the γₙ as a discrete spectrum. The γₙ
  are the **resonances at Re(s)=¼** (poles of φ), not points on the modular line; the
  on-line phase is a *continuous* scattering phase, not a staircase counting zeros.
  Relating the winding to N(T) requires the standard argument-principle contour around
  the resonances — i.e. it is the same statement, not an independent confirmation.

**Verdict (per WO §6 boundary):** diagnostic, not proof. The d=2 scattering channel
**contains** the correct ζ spectral data (resonances + on-line unitary phase); it does
not by itself locate the zeros. **[VERIFIED] phase = ζ-argument; [INTERPRETIVE-bounded]
phase↔count.** A separate phase-winding script/figure was not split out; the winding
is produced in `modular_scattering.py` WS-C.
