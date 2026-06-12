# The 26 σ-paired modes and where RH lives (map)

600-cell adjacency A_1: 9 distinct eigenvalues, 120 modes. Galois σ (√5↔−√5) splits them.
Computed by rh_residue_map.py.

## σ-fixed (rational) — 94 modes — RH-analog CLOSED
| eigenvalue | mult |
|---|---|
| 12 | 1 |
| 3 | 16 |
| 0 | 25 |
| −2 | 36 |
| −3 | 16 |
Total 1+16+25+36+16 = **94**. Eisenstein/rational layer; provably on Fix(τ) = critical line
(per-observer-zero-line, unconditional modulo Galois).

## σ-paired (φ-irrational) — 26 modes = the 26-dim block — RH-analog OPEN
| eigenvalue | a+bφ | mult | σ-conjugate |
|---|---|---|---|
| 9.708 | 6φ | 4 | ↔ 6−6φ (−3.708) |
| 6.472 | 4φ | 9 | ↔ 4−4φ (−2.472) |
| −2.472 | 4−4φ | 9 | ↔ 4φ |
| −3.708 | 6−6φ | 4 | ↔ 6φ |
Total 4+9+9+4 = **26**, in two σ-conjugate halves **13+13** ({6φ m4, 4φ m9} ↔ conjugates).
This is the non-rational, **cuspidal-candidate** block the (fitted) Hecke probes targeted.

## Where RH lives
- The 94 σ-fixed (rational) modes sit on Fix(τ): RH-analog CLOSED (proven mod Galois).
- **RH lives in the 26-dim σ-paired block** — whether the closure-flow (H_attr conjecture)
  suppresses this φ-irrational residue onto Fix(τ). For the 94: proven. For these 26: OPEN.

## Honest chain to classical RH(ζ)
- σ-fixed / Eisenstein part → `ζ_K(s)·ζ_K(s−1)` (Dedekind zeta of ℚ(√5); **verified**).
- σ-paired / 26-block part → the **cuspidal HMF over ℚ(√5)** (RH-analog OPEN; geometric
  generator = icosian Brandt = **unbuilt**).
- ℚ(√5) automorphic RH → classical RH(ζ) (further step; the root geometry).

So "RH lives in the 26" is the **RH-analog for the icosian object**; the bridge to RH(ζ)
runs through the open/unbuilt steps. A precise **localisation**, not a proof.
