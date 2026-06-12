# Vibrational Field Dynamics — the geometry-to-physics programme

*A map, not a manifesto. This page exists so that no single repository is read as an
orphan: each one is a chapter, and this is the table of contents. Every rung below carries
an explicit status stamp — **VERIFIED** (proved / computed in that repo), **OPEN** (named,
not done), or **INTERPRETATION** (a picture that motivates, proves nothing). Read the stamp
before the story.*

---

## The one idea that runs through all of it

There is a single family of geometric objects — the **icosian ring on the 600-cell**, its
parent **E₈ / H₄** symmetry, a **golden-ratio (σ) pairing**, and a **closure operator** —
and the same structure keeps reappearing as the organizing language in very different
places: in pure number theory, and (separately) in physical modelling.

**What is claimed:** the recurrence itself — the *same* geometry shows up in *different*
domains, and each appearance is its own self-contained result.

**What is NOT claimed:** that one domain *implies* another. The number-theory work does not
prove the physics, the physics does not prove the number theory, and — stated plainly —
**no cosmological model here explains, implies, or is implied by the Riemann zeta
function.** The domains share a vocabulary, not a proof. (This firewall is deliberate and
load-bearing; it is what keeps each piece honest.)

So this is a programme held together by a *shared geometric language*, not by a chain of
cross-domain theorems. That is a more modest claim than "it all connects" — and a far more
defensible one.

---

## The arc: geometry → physics

### 0. The picture (why a point, a circle, and infinity are one object)
**Status: INTERPRETATION.**
One compactified scale–phase object — a cylinder whose two ends are the point and infinity
and whose middle is the unit circle — with a positivity/closure law. It is the intuition
that aims the whole programme. It proves nothing; it says where to look.
→ companions in **icosian-closure-object** (`from-a-point-to-a-universe`, `vfd-rh-reformulation`).

### 1. The object and its exact arithmetic
**Status: VERIFIED identity / OPEN positivity.**
A purely geometric object — the maximal icosian order on the 600-cell over ℚ(√5) — has an
*exact* arithmetic shadow: `L(Θ,s) = ζ_K(s)·ζ_K(s−1)`. The Riemann ζ sits inside as one
factor of four, but the object provably does **not** isolate ζ. Its cuspidal face supplies,
parameter-free, the prime side of a Weil positivity witness; the single open step is GRH
for one cuspidal L-function — **not** classical RH. No proof of RH is claimed.
→ **icosian-triad-v600** (the exact identity, v1.1.0) and
  **icosian-closure-object** (the boundary + witness, v0.1.0-review).

### 2. The closure operator and the cascade
**Status: mixed — VERIFIED structure / OPEN selection.**
The same geometry carries a **closure operator** (a golden-ratio-weighted Laplacian-type
map) and a σ-pairing that splits its spectrum. This is the structural spine that the
number-theoretic and physical pieces both sit on. Parts are computed and verified; the
"why this structure and not another" selection question is open.
→ **the-24-600-spectral-bridge** (the closure-projection channel, Schläfli decomposition,
  spectral bridge) and **existence-life-closure-programme** (existence-as-closure framing).
  *(The detailed cascade-refinement papers are internal / not yet public.)*

### 3. The E₈ / H₄ geometry
**Status: VERIFIED — but known mathematics, exactly reproduced (not new).**
The 600-cell's symmetry sits inside E₈ via the H₄ folding; the exact 240-root E₈ and the
H₄→E₈ trace-form are recovered exactly. This is classical (Wilson / Moody–Patera) — we
verify and use it, we do not claim to have discovered it. It is the bridge that lets the
same object speak both the arithmetic and the physical dialects.
→ material in **the-24-600-spectral-bridge**; pure-geometry engine is internal.

### 4. A cosmological model on the same geometry
**Status: VERIFIED-within-its-own-model / SEPARATE domain.**
A cosmological model in which the *same* σ-pairing geometry appears as a dipole structure;
within that model the fitted parameters land close to Planck values. This is a **physical
model and application** — it stands or falls on its own cosmological merits, and it is
**firewalled from the number theory**: it is the same geometry used again, not a bridge to
ζ or to RH.
→ **hypersphere-cosmology** (v1.1.0).

---

## What connects, and what does not

| Connects (real) | Does NOT connect (firewalled) |
|---|---|
| The same geometric objects (icosian / E₈ / H₄, σ-pairing, closure operator) recur across domains | One domain proving another |
| A shared *vocabulary* and a shared *picture* | The universe "encoding the primes" |
| Each rung is individually verified or honestly marked open | Cosmology implying / implied by the Riemann Hypothesis |

The honest thesis in one line:

> **One geometric language; several independent results; no cross-domain proof claimed.**

---

## Where to start

- **Want the mathematics?** Start at rung 1 — `icosian-closure-object`, and read its
  `CLAIMS.md` first.
- **Want the physics application?** Go straight to rung 4 — `hypersphere-cosmology`.
- **Want the vision?** Read the rung-0 companions, knowing they are the picture, not a proof.

## The repositories

| repo | rung | status |
|---|---|---|
| [icosian-closure-object](https://github.com/vfd-org/icosian-closure-object) | 1 | review draft; verified identity + located wall |
| [icosian-triad-v600](https://github.com/vfd-org/icosian-triad-v600) | 1 | v1.1.0; exact identity C₂=1 |
| [the-24-600-spectral-bridge](https://github.com/vfd-org/the-24-600-spectral-bridge) | 2–3 | published; spectral / closure-projection channel |
| [existence-life-closure-programme](https://github.com/vfd-org/existence-life-closure-programme) | 2 | published; existence-as-closure |
| [hypersphere-cosmology](https://github.com/vfd-org/hypersphere-cosmology) | 4 | v1.1.0; cosmological model |

*Licences vary per repo (typically Apache-2.0 for code, CC BY 4.0 / NC for prose). "Commons
of knowledge. Stewardship of power."*
