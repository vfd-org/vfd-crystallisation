# Public post draft

We isolated one concrete result from the broader VFD closure-geometry
programme.

The 600-cell has a five-coset decomposition where each coset carries
a d=1 graph isomorphic to the 24-cell. The λ=12 eigenspace of each
local 24-cell Laplacian lifts exactly into the λ=12 eigenspace of the
full 600-cell.

Not approximately:

    ‖L₆₀₀ v − 12 v‖ ≈ 6.2 × 10⁻¹⁵.

Negative controls at λ = 0, 4, 8, 10 all fail (residuals 13, 9, 5, 3).
The lift is selective for λ = 12.

The full λ=12 sector decomposes under A₅ as

    E_lifted   ≅ 2·Y₅
    E_residual ≅ 3·Y₅
    E₆₀₀(12)   ≅ 5·Y₅,

where Y₅ is the 5-dimensional A₅ irrep.

This is not a physics claim. It is a reproducible geometry result —
a selective local/global spectral bridge between the 24-cell and
600-cell.

Reproduce with:

    python closure_transform_engine/examples/run_wo008_keystone.py
