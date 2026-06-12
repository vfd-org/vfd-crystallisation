"""closure_transform_engine: foundation paper artifact for the Schläfli
decomposition of the 600-cell.

This package wraps a single reproducible finite-geometric result around
the vendored ``vfd_v600`` icosian/quaternion package: the 600-cell vertex
set 2I decomposes as the disjoint union of five right cosets of the
binary tetrahedral subgroup 2T, each carrying the intrinsic 24-cell
distance structure, with the induced action of 2I on the five cosets
descending through {±1} to a transitive A_5.

The result is narrow by design and self-contained. It does not depend on
any physics interpretation; it is a finite-group / finite-geometry fact
about the 600-cell.

See ``docs/schlafli_decomposition.{tex,pdf,md}`` for the technical note
and ``closure_transform_engine.decomposition`` for the computational
certificates.
"""

from .decomposition import (
    DecompositionResult,
    right_cosets,
    distance_shells_v600,
    certify_v600_construction,
    certify_v24_subgroup,
    certify_right_cosets,
    certify_each_coset_is_24cell,
    certify_a5_coset_action,
    run_decomposition,
)

__all__ = [
    "DecompositionResult",
    "right_cosets",
    "distance_shells_v600",
    "certify_v600_construction",
    "certify_v24_subgroup",
    "certify_right_cosets",
    "certify_each_coset_is_24cell",
    "certify_a5_coset_action",
    "run_decomposition",
]
