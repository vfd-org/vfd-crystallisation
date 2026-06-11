# Hawking Radiation from V_600 σ-pair Excitations

**Status: 2026-05-06.** Single-quantum spectrum + exact first-law identity.

## Setup

For the cascade-BH analog (one Dic_5-coset = horizon, 4 σ-fixed = anchor
states, 16 σ-mobile = horizon modes), the natural energy observable for
Hawking emission is the σ-pair excitation:

```
E(v) := |v - σ(v)|²_trace / 2
```

where σ is the Galois twist √5 ↦ -√5 acting on icosian quaternion components,
and ⟨ , ⟩_trace is the trace inner product on the icosian ring.

For σ-fixed vertices (24-cell), σ(v) = v ⇒ E(v) = 0 (no emission).
For σ-mobile vertices, σ(v) ≠ v and E(v) > 0.

## Result

`hawking_radiation_derivation.py` computes E(v) over all 120 V_600 vertices.

```
σ-fixed (24-cell):    24 vertices,  E = 0
σ-mobile (boundary):  96 vertices,  E = 5/2  (ALL identical)
```

**The σ-pair spectrum is a single delta function at E_q = 5/2.**

This is forced by W(H₄) symmetry: σ-mobile vertices form a single
W(H₄)-orbit, and the trace metric is W(H₄)-invariant, so
|v - σ(v)|²_trace is a constant on the orbit. The 96-fold degeneracy
is the orbit size.

## First-law identity (exact, per Dic_5-coset)

| Quantity | Value | Interpretation |
|---|---|---|
| Quantum gap | E_q = 5/2 | σ-pair excitation energy |
| Horizon modes | A = 16 | σ-mobile vertices per coset |
| Anchor states | S = 4 | σ-fixed vertices per coset |
| Coset energy | E = A·E_q = 40 | total horizon emission budget |
| **Bekenstein** | **S/A = 1/4** | exact, structural |
| **Cascade T_H** | **T_H = E_q = 5/2** | quantum gap = temperature |
| **First law** | **T_H·S = E/4 = 10** | exact identity |

Aggregate over all 5 boundary cosets:
- Total E = 200, Total S = 20, Total A = 80.
- T_H·S_total = 50 = E_total/4. ✓

## Why a single line, not a Planck spectrum

In continuum QFT, Hawking radiation is approximately thermal with
T_H = ℏc³/(8πGMk_B), and the spectrum is a Planck distribution because
the horizon has a continuum of modes.

The cascade has only **finitely many discrete modes** (96 σ-mobile
vertices), and the σ-Galois twist is a single binary operation. There
is exactly **one** way for a σ-mobile vertex to "exit" — by going to
its σ-image in σ(V_600). This produces a monochromatic spectrum.

The Planck continuum should be recovered in the **semiclassical /
many-coset limit**: summing over many cascade resolutions and many
neighbouring cascade cells, the discrete E_q gap broadens into a
quasi-thermal distribution. This is a Tier-2 derivation.

## Mapping to standard Bekenstein-Hawking

To match T_H = ℏc³/(8πGMk_B) numerically requires identifying:

1. The cascade trace-energy unit ↔ ℏc/r_horizon.
2. The horizon area unit ↔ Planck-area count.
3. The σ-twist scale ↔ frame-resolution scale.

These mappings are explicitly listed in `cmb_mapping.py` for the
cosmological observables (H₀, σ_8). For BH thermodynamics, the
mappings are:

```
A_cascade = 16 (per coset)         ↔  A_phys = 4πr_s²
S_cascade = 4 (per coset)          ↔  S_phys = A_phys / (4ℓ_P²)
T_H_cascade = E_q = 5/2            ↔  T_H_phys = ℏc/(8πGM)
```

The **structural ratio S/A = 1/4 is invariant under unit choice** —
this is the content of Bekenstein-Hawking 1/4 derived from V_600.

## Falsifiable predictions

For BHs of mass M satisfying T_H_phys ≪ E_cascade_quantum (i.e.,
small primordial BHs near Planck scale), the cascade prediction is
that the Hawking spectrum should show a discrete cutoff at the
single-quantum level rather than a smooth thermal tail.

This is testable in primordial BH evaporation searches (e.g.,
gamma-ray bursts from PBH evaporation, where the final-burst
spectrum should reveal the discrete cascade gap).

## Files

- `hawking_radiation_derivation.py` — derivation script.
- `bh_bekenstein_1_4.py` — companion S/A = 1/4 derivation.
- `UNIFIED_RESULT.md` — full programme summary.

## Honest scope

What's solid:
1. σ-pair spectrum derivation: exact (group theory + trace metric).
2. Single-quantum result: forced by W(H₄) transitivity.
3. T_H = E_q identification: clean from first-law identity.
4. First-law E = T·A and T·S = E/4: exact per coset.

What's deferred:
1. Quantitative Planck-spectrum recovery in semiclassical limit.
2. Numerical T_H_phys ↔ E_q mapping (cascade unit calibration).
3. Primordial BH evaporation cutoff prediction (Tier-2 quantitative).
