# Cosmological Folding Rate — Real-Data Run

Dataset: `data/processed/cc_moresco_bc03.csv`  (n=15)

## Fits

| model | params | χ² | χ²_red | AIC | BIC | ΔAIC | ΔBIC |
|---|---:|---:|---:|---:|---:|---:|---:|
| LCDM | 2 | 6.11 | 0.470 | 10.11 | 11.53 | +0.00 | +0.00 |
| VFD-A | 4 | 6.02 | 0.547 | 14.02 | 16.85 | +3.91 | +5.32 |
| VFD-B | 5 | 5.35 | 0.535 | 15.35 | 18.89 | +5.24 | +7.36 |

## Bootstrap (500 resamples)

| model | param | p16 | p50 | p84 |
|---|---|---:|---:|---:|
| VFD-A | A | -0.0822 | 0.0100 | 0.0382 |
| VFD-A | theta | 0.0000 | 0.0000 | 1.4372 |
| VFD-B | A | -0.5000 | -0.5000 | -0.5000 |
| VFD-B | z0 | -0.0123 | 0.0439 | 0.5000 |
| VFD-B | sigma | 0.1500 | 0.1500 | 0.1500 |

## Verdict

**NOT SUPPORTED**

## Notes

- ΛCDM is the baseline; ΔAIC/ΔBIC are computed against it.
- BIC penalty per parameter ≈ ln(N), heavier than AIC's 2.
- VFD-B amplitude has a partial degeneracy with H0 when σ ≳ ln(φ).
- A φ-supported claim requires ΔBIC < -10 *and* bootstrap A interval excluding zero.
