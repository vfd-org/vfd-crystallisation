# The Schläfli Decomposition of the 600-cell

**A reproducible exact-arithmetic certificate for the decomposition of
the 600-cell into five 24-cell cosets and the induced A₅ action.**

> **Status:** Reproducible mathematical note / exact computational
> certificate. Not peer-reviewed.

---

## The result in one paragraph

The 600-cell (the regular 4-polytope `{3,3,5}`, 120 vertices) is the
binary icosahedral group **2I** under quaternion multiplication. The
binary tetrahedral group **2T** sits inside 2I as the **σ-fixed**
subgroup (where σ is the Galois twist `√5 ↦ −√5`), with index 5.
The five right cosets of 2T partition V₆₀₀ into **five disjoint
24-element subsets**, each carrying the intrinsic **24-cell distance
structure** (8-regular at squared distance 1, 96 edges). Right
multiplication by 2I induces a transitive action on the five cosets;
the kernel is exactly {±1}, the image is A₅ acting on five points,
with conjugacy-class sizes matching the standard A₅ character table
(1, 15, 20, 12, 12).

All five formal claims are certified by exact ℚ(√5) / integer
arithmetic. No floating-point computation enters any certificate.

## Why this paper

This note supplies the **finite-geometric foundation** for the
companion paper [*The 24–600 Spectral
Bridge*](https://github.com/vfd-org/the-24-600-spectral-bridge). The
spectral bridge proves that the local λ=12 Laplacian eigenspaces on
each coset zero-extend exactly into the global 600-cell λ=12
eigenspace. The present note proves and certifies the coset
decomposition the spectral bridge assumes — independently and
self-contained.

## The formal claims (all certified exactly)

The proof package is a set of exact arithmetic certificates, not
floating-point evidence. Every one of the following is checked in
ℚ(√5) (for distances) or integer set-equality (for coset structure):

| Claim | Certificate |
|---|---|
| **Theorem 1** — V₆₀₀ = 2I: 120 distinct unit-norm vertices, closed under multiplication, identity + inverses present | `certify_v600_construction` — all 120² = 14 400 products + 120 inverses |
| **Theorem 2** — V₂₄ = 2T: 24 σ-fixed vertices form a subgroup of index 5 | `certify_v24_subgroup` — all 24² = 576 products + 24 inverses |
| **Theorem 3** — Schläfli decomposition: five right cosets, sizes 24, disjoint, cover V₆₀₀, C₀ = 2T | `certify_right_cosets` — exact set operations on vertex indices |
| **Theorem 4** — Each coset is a 24-cell: intra-coset shortest d² = 1, 8-regular, 96 edges, no intra-coset V₆₀₀-edge | `certify_each_coset_is_24cell` — 552 ordered pairs per coset, exact ℚ(√5) distances |
| **Theorem 5** — A₅ coset action: 60 distinct perms, kernel {±1}, image transitive + all even + class sizes (1, 15, 20, 12, 12) = A₅ | `certify_a5_coset_action` — enumerate all 120 induced permutations + explicit conjugacy-orbit classification |

No floating-point computation enters any of the certificates.

## What this does and does not claim

It claims:
- a reproducible, exact-arithmetic certificate for the
  finite-geometric decomposition above;
- the induced 2I action on the five cosets is exactly A₅, with
  kernel {±1};
- this supplies the foundation used downstream by the 24–600
  spectral bridge.

It does **not** claim to derive the Standard Model, particle masses,
cosmology, black holes, the Riemann hypothesis, or consciousness, and
it does not subsume or replace any other framework. It is a narrow,
inspectable, reproducible finite-geometry result.

## Reproduce it

Requires Python ≥ 3.8 with NumPy and SymPy (see `requirements.txt`;
developed on Python 3.8.10, NumPy 1.24.4, SymPy 1.13.3). All
certificates use exact arithmetic via `vfd_v600` (ℚ(√5)-rational
pairs) and integer set operations.

```bash
pip install -r requirements.txt          # or: pip install -e .

# Run the full protocol (~20s): builds the 600-cell from exact
# Q(sqrt 5) icosian quaternions, runs every certificate, and writes
# the frozen output artifacts to docs/outputs/.
python closure_transform_engine/examples/run_wo007_schlafli_decomposition.py

# Re-assert the certificate-level claims as a test (~45s):
pytest closure_transform_engine/tests/test_wo007_schlafli_decomposition.py
```

Expected console summary:

```text
Certificates:
  V_600 construction (Section 2):     PASS
  V_24 subgroup       (Section 3):     PASS
  Five right cosets   (Section 4):     PASS
  24-cell structure   (Section 5):     PASS
  A_5 coset action    (Section 6):     PASS

Coset sizes: [24, 24, 24, 24, 24]
A_5 conjugacy-class sizes: {'1A': 1, '2A': 15, '3A': 20, '5A': 12, '5B': 12}

Verdict:  SCHLAEFLI_DECOMPOSITION_CERTIFIED
```

The reproducibility log
(`docs/outputs/wo007_reproducibility_log.txt`) records the run UTC
timestamp, elapsed time, Python and dependency versions, platform,
**commit hash** (with a marker if the working tree was dirty), and
per-certificate pass/fail states.

## Repository layout

```
closure_transform_engine/        the computation
  decomposition.py               5 certificate routines
  examples/run_wo007_schlafli_decomposition.py   one-command runner
  tests/test_wo007_schlafli_decomposition.py     test suite (23 tests)
vfd_v600/                        vendored exact Q(sqrt 5) icosian-quaternion package
docs/
  schlafli_decomposition.{tex,pdf,md}   the technical note (canonical = .tex)
  figures/                       SVG figures (4 diagrams)
  outputs/                       frozen run artifacts
    wo007_summary.json
    wo007_cosets.json
    wo007_coset_action_table.csv
    wo007_distance_shells.csv
    wo007_reproducibility_log.txt
requirements.txt, pyproject.toml, LICENSE, CITATION.cff
```

## Companion artifact

The downstream spectral result that uses this decomposition lives at
[github.com/vfd-org/the-24-600-spectral-bridge](https://github.com/vfd-org/the-24-600-spectral-bridge):
*The 24--600 Spectral Bridge — a selective λ=12 eigenspace embedding
from five 24-cell cosets into the 600-cell.*

The two artifacts are independent and can be read in either order,
but the finite-geometric decomposition certified here is logically
prior.

## Citation

See `CITATION.cff`.

## License

MIT — see `LICENSE`.
