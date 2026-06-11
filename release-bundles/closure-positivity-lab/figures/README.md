# Visual suite — the primes as the geometry's diffraction

Four instruments, one engine: the icosian object's **point-counted eigenvalues**
(geometry / Frobenius traces) reconstruct the diffraction field on the critical line.
**No zero data enters any reconstruction** — the 33 PARI-computed zeros appear only as an
external overlay to check against. Everything is cross-checked: the geometric eigenvalues
match the curve `31.1-a1/ℚ(√5)` point counts (32/32, 0 mismatches).

```bash
python3 make_all.py          # regenerates everything (numpy, matplotlib; ffmpeg optional)
```
(Needs `../out/curve_zeros.json`; `make_all.py` runs Stage B to create it if missing.)

| file | what it shows | honest status |
|------|---------------|---------------|
| `fig_diffraction.png` | each prime = one wave (freq `log N(q)`, phase from the Frobenius angle); their interference is the critical-line field, and the 33 zeros land on the fringes | exact identity (Weil explicit formula); evidence, not proof |
| `anim_diffraction.mp4` | the zeros snapping into focus as prime-"cells" switch on, 1 → 425 | same; visualises bandwidth → resolution |
| `fig_hologram.png` | 100% → 3% of the primes: every fraction reproduces **all** the zeros, blurrier | the prime↔zero Fourier duality is **holographic** (a fragment carries the whole scene at lower resolution) — true and exact |
| (tool) `lab/prime_wave.py` | `prime_to_wave(p)` — any prime's exact wave; `hologram_demo()` | reproducible |

### The tool
```bash
python3 -m lab.prime_wave wave 31     # the wave(s) of the prime ideal(s) above 31
python3 -m lab.prime_wave            # demo: first primes + the hologram fraction figure
```
Each prime's wave is fixed by the geometry with no free parameters:
`frequency = log N(q)`, and amplitude/phase from the Frobenius rotation angle
`θ_q = arccos(a_q / 2√N(q))`, where `a_q` is the point count.

### What these are / are not
- **Are:** geometry-only, zero-data-free reconstructions of the explicit formula, with the
  computed zeros landing where predicted; the hologram property is exact.
- **Are not:** a proof of RH (the explicit formula is an identity; reproducing the zeros
  is consistent-with-RH evidence). No physical/holography claim is made — "hologram" here
  is the exact information-theoretic sense (each part encodes the whole at reduced
  resolution), not AdS/CFT or any physics assertion.
