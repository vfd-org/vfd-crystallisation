# WS-B/C — The modular scattering function and where the zeros live

**Object.** The constant term of the SL(2,ℤ) Eisenstein series `E(z,s) = y^s + φ(s)y^{1−s}`:

```
φ(s) = ξ(2s − 1) / ξ(2s),     ξ(s) = π^{−s/2} Γ(s/2) ζ(s).
```

ζ is *manifestly inside* the scattering coefficient of the d=2 arithmetic surface.

## Verified scattering identities (`src/modular_scattering.py`)

- **Sample values:** φ(0.7) = −2.291, φ(1.3) = +4.026, φ(0.6+3i) = 0.810 − 0.585i.
- **Scattering / unitarity off-line:** `φ(s)φ(1−s) = 1` to **1e-32**.
- **Unitary on the modular line:** `|φ(½+it)| = 1` exactly for every t tested
  (t = 1, 5, 10, 14.13, 21.02, 30). The scattering matrix is unitary on Re(s)=½.
- **Pole at s=1:** φ(0.97) = −31, φ(0.99) = −95, φ(0.999) = −954 → the residue/pole
  giving the constant eigenfunction.

## The decisive fact — the Riemann zeros are the scattering RESONANCES

Poles of φ = zeros of ξ(2s) = {2s = ρ} = **s = ρ/2**. Under RH (ρ = ½+iγ) the
resonance sits at **s = ¼ + iγ/2**. Test of `|φ|` there:

| γ | \|φ(¼+iγ/2)\| | \|φ(.30+iγ/2)\| | \|φ(¼+i(γ/2+1))\| |
|---|---|---|---|
| 14.134 | 7.26×10⁶ | 9.21 | 1.17 |
| 21.022 | 2.96×10⁶ | 9.49 | 1.30 |
| 25.011 | 2.58×10⁶ | 9.59 | 1.23 |
| 30.425 | 9.06×10⁶ | 10.0 | 2.62 |

`|φ|` **spikes by ~10⁶** exactly at `s = ¼ + iγₙ/2` and collapses to O(1) between
zeros → **the Riemann zeros are the modular surface's scattering resonances.**

## Honest scope

- The resonances sit at **Re(s) = ¼**, *not* on the modular critical line Re(s)=½, and
  they are **not** the Laplace (Maass cusp-form) eigenvalues (those are a different
  set, first ≈ ¼+9.53²). The zeros enter as **scattering poles**, not as the discrete
  spectrum.
- **RH ⟺ all these resonances sit exactly on Re(s)=¼ ⟺ ρ on Re=½.** This *relocates*
  RH into the modular scattering channel; it does not prove it. **[VERIFIED] presence;
  [OPEN] location.**
