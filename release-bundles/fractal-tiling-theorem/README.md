# The V₆₀₀ Substrate at the Riemann-Hypothesis Frontier

**A verified computation, an honest map of the wall, and a disciplined account
of what the zeros are.**

> Pre-peer-review open research. **No proof of the Riemann Hypothesis is
> claimed.** Every claim is status-tagged: `[theorem]`, `[verified]`
> (computed, with a stated correctness gate), `[evidence]`, `[conjecture]`,
> `[open]`. All computations reproduce from `route_b/` and `sims/`.

## The verified result

The **icosian ring** — the maximal order of the definite quaternion algebra
$(-1,-1/\mathbb{Q}(\sqrt5))$ whose unit group is the 600-cell — computes, by
its own intrinsic Brandt/Hecke action at level $\mathfrak{p}_{31}$ (norm 31),
the genuine cuspidal Hilbert modular newform over $\mathbb{Q}(\sqrt5)$ of that
level. Its Hecke eigenvalues **match the independently point-counted newform
exactly on all 11 prime ideals of norm ≤ 41** — including signs and
split-prime pairings, out-of-sample, with no fitting:

| N𝔮 | 4 | 5 | 9 | 11 | 19 | 29 | 41 |
|---|---|---|---|---|---|---|---|
| substrate aₚ | −3 | −2 | 2 | {−4,4} | {−4,4} | {−2,−2} | {−6,−6} |
| genuine newform | −3 | −2 | 2 | {−4,4} | {−4,4} | {−2,−2} | {−6,−6} |

By the multiplicativity tiling theorem, matching the **finite** prime data
pins the **entire** L-function. This is a non-circular substrate↔arithmetic
identification, and it is the credential the rest of the bundle rests on.

The substrate also realises the **local** critical line in full (each local
factor's zeros on Re(s)=½, via the Satake circle), and supplies real Satake
data to the genuine **Connes/Weil positivity** functional, which is positive
on every test gate-validated against the Riemann ζ zeros (0.01%).

What it does **not** do: place the **global** zeros. That is RH, and it is
open — the missing object is a self-adjoint (Hilbert–Pólya) operator on the
adelic arena, pinned here to the ℂ/unitary/β=2 class with its finite-place
part built and the single archimedean step open.

## The two papers

1. **`paper/rh-frontier-capstone.tex`** — the technical paper. The verified
   circle test, the local critical line, the multiplicativity tiling, the
   corrected scope, the quantum-chaos / division-algebra structure, and the
   precise location of the missing operator. Every claim status-tagged.

2. **`paper/void-and-structure.tex`** — the conceptual companion. What the
   Riemann zeros **are**: a generative *absence* from which the primes are
   reconstructed as harmonics (the explicit formula); timeless, observer-free,
   and formless in an exact sense; with a principled diagnosis of *why* the
   problem resists construction. It states only what is proved and marks
   explicitly where mathematics ends and interpretation begins — the
   interpretation is the reader's to make, not the text's to assert.

   *Read the capstone first: it is the verified anchor that earns the
   companion its hearing.*

## Reproduce

| Script | Produces |
|---|---|
| `sims/sim_genuine_eigenvalues.py` | the genuine norm-31 newform (Ramanujan + torsion gates) |
| `route_b/step3_4_hecke.py` | substrate Hecke eigenvalues; the circle test |
| `route_b/weil_positivity.py` | Connes/Weil functional, ζ-gated |
| `route_b/quantum_chaos_test.py` | zero spacings vs GUE |
| `route_b/deterministic_probability.py` | deterministic zeros vs a random GUE matrix |

Status-tagged supporting notes are indexed in `RH_FRONTIER.md`
(`CIRCLE_TEST.md`, `SCOPE.md`, `THE_ADJOINT.md`, `CONNES_POSITIVITY.md`,
`QUANTUM_CHAOS.md`, `DIVISION_ALGEBRA.md`, `KATZ_SARNAK.md`,
`ADELIC_SCALING.md`).

## Scope discipline

The mathematics uses only fields, lattices, quaternion orders, Hecke
operators, gamma factors, and conductors. No observer, consciousness, or
"self" enters any definition, and none is needed. Any such reading is outside
this mathematics, consistent with the programme's framing ("X exists ⟺
𝒞(X)=X").

## Licence

Paper and prose: CC BY 4.0.
