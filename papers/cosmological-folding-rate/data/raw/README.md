# Public H(z) compilations

This module **does not** ship real H(z) values, to avoid any risk of
mis-transcription. To run on real data:

1. Download a published compilation, e.g.:
   - Moresco et al. cosmic-chronometer compilations (2012, 2016, 2022)
   - Public BAO line-of-sight H(z) tables (BOSS / eBOSS / DESI DR1)
2. Convert to a CSV with the canonical header
   `z,H,sigma_H,source` and place it in `data/processed/`.
3. Run the pipeline pointed at the new file:
   ```
   PYTHONPATH=. python3 notebooks/06_real_data_run.py data/processed/<your_file>.csv
   ```

Always cite the source compilation in your write-up. Cosmic chronometer
covariance matrices, where available, should be added as an extension
(the current pipeline assumes diagonal σ_H errors).
