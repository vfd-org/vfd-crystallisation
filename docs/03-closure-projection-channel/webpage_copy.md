# Web page copy — From Schläfli Decomposition to Spectral Bridge

## Hero

**From Schläfli Decomposition to Spectral Bridge**

*A first explicit local-to-global closure-projection channel in V₆₀₀ —
synthesised from two reproducible exact-arithmetic notes.*

## The two artifacts

**Paper 1 (foundation).** The Schläfli decomposition of the
600-cell. V₆₀₀ ≅ 2I splits into five right cosets of the binary
tetrahedral group 2T, each carrying intrinsic 24-cell structure;
the induced coset action descends to A₅ = 2I/{±1}. Certified
exactly over ℚ(√5).

**Paper 2 (the spectral consequence).** The 24–600 Spectral
Bridge. The local λ=12 eigenspaces of those five 24-cell sectors
zero-extend exactly into the global λ=12 eigenspace of the
600-cell Laplacian. Certified exactly over ℚ. Selective: no other
local Laplacian eigenvalue admits a non-trivial lift.

## Why the synthesis matters

The two papers, read together, exhibit a pattern: a *local*
shell structure inside the 600-cell does not merely sit inside
the global geometry — at one specific spectral value (λ=12), it
couples *exactly* to a global invariant sector. We call this a
**closure-projection channel** — interpretive language for the
local-to-global compatibility relation that the two exact results
together exhibit.

The synthesis introduces no new theorem and no physics claim. It
is a reader's map between the two artifacts and a precise
statement of what the pattern is.

## What is and is not established

**Established (by the two cited artifacts):**

- V₆₀₀ decomposes into five 24-cell cosets.
- The coset action descends to A₅.
- The local and global Laplacians live on *different* distance
  shells; intra-coset 24-cell edges and 600-cell edges share no
  vertex pairs.
- At λ=12, the local eigenspaces zero-extend *exactly* into the
  global eigenspace.
- The lifted subspace is A₅-stable: 2·Y₅ inside 5·Y₅.

**Not established (here or in the prior artifacts):**

- No derivation of particle masses, the Standard Model, or any
  physical observable.
- No claim that λ=12 is physically realised.
- No claim that all closure projection is explained by this
  example.

## Reproduce

```bash
git clone https://github.com/vfd-org/the-24-600-spectral-bridge
cd the-24-600-spectral-bridge
pip install -r requirements.txt
python closure_transform_engine/examples/run_wo007_schlafli_decomposition.py
python closure_transform_engine/examples/run_wo008_keystone.py
pytest closure_transform_engine/tests/
```

All certificates use exact rational arithmetic; floating-point
diagonalisation is included only as an independent cross-check.

## What this synthesis sets up

The next paper in the programme will attempt to formalise the
*closure-projection channel* concept into a general selection
principle: *given a local sector, a local operator, a global
operator, and a projection/lift map, when does a local eigenspace
contribute to a global invariant sector?* This synthesis note
identifies the λ=12 lift in the 24–600 case as one positive
instance and one negative-control template (at every other local
eigenvalue) for that general question — but does not attempt the
formalisation here.
