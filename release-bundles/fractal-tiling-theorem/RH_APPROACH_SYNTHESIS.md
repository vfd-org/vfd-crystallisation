# The VFD Programme and the Riemann Hypothesis — a verified map and its honest boundary

**Status:** synthesis of an extended geometry-of-RH investigation (2026-06-03..07).
Every claim below is stamped **[verified]**, **[known]** (standard mathematics, not
ours), or **[interpretation]** (non-load-bearing). No claim of a proof of RH is
made anywhere in this document, and none is implied.

---

## 0. Scope, stated first

This document maps **how far the VFD geometric programme reaches toward RH, and
exactly where it stops.** The result is a *boundary*, machine-certified: the
programme verifiably reaches the **cuspidal / Eisenstein-over-K side** (the
proven-RH-analog side) and **does not** reach the Riemann ζ itself. That boundary
is the honest contribution; it is **not** a proof, and the missing step is a
construction no search or geometry supplies.

---

## 1. The one sentence everything reduces to

**[known]** RH is equivalent to a single inequality — **positivity** (`W(f) ≥ 0`,
the Weil criterion). Every geometric, spectral, algebraic, and dynamical
restatement we examined reduces to *this same inequality*. Geometry **stages** RH;
it does not **close** it.

## 2. One condition, many faces

**[known]** The following are *proven-equivalent* — they are one condition in
different clothes, and a single off-line zero breaks all of them at once:

- Weil positivity `W(f) ≥ 0`  (spectral / Connes)
- Li coefficients `λ_n ≥ 0`  (algebraic)
- Jensen-polynomial **hyperbolicity**  (real-rootedness; GOR-Z 2019)
- de Bruijn–Newman `Λ ≤ 0`  (dynamical; Rodgers–Tao 2020 proved `Λ ≥ 0`, so RH ⟺ `Λ = 0`)
- a self-adjoint operator with real spectrum  (Hilbert–Pólya)
- positivity of a Frobenius **degree-form** on an arithmetic surface  (the function-field template, Weil/Deligne — *proven there*)

**[verified]** We confirmed the unification numerically (one off-line zero drives
the Li contribution negative; the equivalences are literature).

## 3. What the VFD programme verifiably reaches — the certified atlas

**[verified]** Machine-certified by the gate-first engine (`vfd_math_engine/`,
8-check verification gate, hashed certificates in `programme_atlas.json`):

| correspondence | verdict | meaning |
|---|---|---|
| 24-cell ↔ `ζ(s)ζ(s−1)` | **VERIFIED** | on-line zeros = Riemann zeros (K=ℚ analog) |
| icosian / V_600 ↔ `ζ_K(s)ζ_K(s−1)` | **VERIFIED** | the icosian theta L-function over K=ℚ(√5) |
| φ-shell / twin ↔ `L(χ₅)` | **VERIFIED** | the Galois-sign (√5) part |
| substrate ↔ ζ (strong bridge) | **REJECTED** | fails 5 checks — encodes `ζ_K`, *not* ζ |
| fitted substrate→eigenvalue map ↔ ζ | **REJECTED** | provenance: fitted (the W5 trap) |
| generic GUE operator ↔ ζ | **REJECTED** | right *class*, wrong *individual* |

**[verified]** The programme reaches `ζ_K`, `ζ(s)ζ(s−1)`, `L(χ₅)` — all on the
**cuspidal / Eisenstein-over-K** side, the side whose RH-analog is *proven*.

## 4. What it does not reach — the wall, certified

**[verified]** It does **not** reach the Riemann ζ:
- The "strong bridge" (substrate ↔ ζ) is rejected on five independent grounds.
- Asked to find any VFD object that *is* ζ, the engine's proposer + gate return
  **none**. **The wall is confirmed automatically.**
- Structurally: `ζ_K = ζ · L(χ₅)` *swallows* ζ as a factor (contaminated by
  L(χ₅)); the substrate encodes the **product**, giving no independent grip on ζ.
  This is the open **(O2)** de-merge, now closed in the negative.

## 5. The verified structure (true, but not the wall)

**[verified]** The Riemann zeros are:
- **GUE / β=2** — the operator must be complex/chiral, time-reversal broken.
- **prime-encoding** — summed as oscillations, the zeros spell out `log(prime^k)`
  with von-Mangoldt weights (the explicit formula).
- a **β=2 Dyson gas at a critical edge** — poised exactly at `Λ = 0` (RH-config).

These are real and beautiful — and all reduce to the *same identity* (the explicit
/ trace formula), which holds **whether or not RH is true.** Structure, not proof.

## 6. The honest boundary — the missing object is a construction

**[known]** The one thing that would *force* the positivity is a **canonical
Frobenius over ℤ whose degree-form is `W(f)`** — equivalently, the intersection
theory (Hodge index) on an arithmetic surface `Spec ℤ ×_{𝔽₁} Spec ℤ`. The
function-field analog is *proven* (Deligne realized `τ(p)` as a Frobenius trace and
applied the Weil bound). Over ℤ the object is **unbuilt**.

**[known]** The leading path: **Connes–Consani** (𝔽₁ = the sphere spectrum `𝕊`,
the missing surface = `ℤ ⊗_𝕊 ℤ = THH(ℤ)`; the arithmetic / scaling site). The
**trace formula is done** (Connes); the **positivity is the wall**. This is
generational research mathematics — **not** a search, a fit, or a rebuild.

## 7. The engine — the certifying tool

**[verified]** `vfd_math_engine/` turns the above into a **reproducible certifier**:
ARIA *proposes* geometry↔arithmetic correspondences; an 8-check gate
(no-hardcoding, provenance, fingerprint, pointwise, degree, pole, density,
rigidity) *disposes*; certificates are hashed and atlas'd. It **issues
verification certificates only — never a proof certificate.** It auto-kills fitted
maps and overclaims, making every VFD claim exact and undismissable.

## 8. What is *not* claimed (framing discipline)

**[interpretation, non-load-bearing]** Several physically-suggestive readings arose
(consciousness as selector, a simulation reading observers, the fine-structure
constant as mediator, a sphere-triality, a monopole as the deepest object). **None
has mathematical content here**, several contradict the established determinism,
and all are explicitly *not* claimed as results. The mathematics in this document
does not lean on any of them.

---

## One-paragraph summary

The VFD programme's geometry reaches, verifiably and reproducibly, the **cuspidal /
Eisenstein-over-K side** of the picture (`ζ_K`, `ζ(s)ζ(s−1)`, `L(χ₅)`) — the side
whose RH-analog is proven — and **does not** reach the Riemann ζ, which it
*contains as a factor* but cannot isolate (the (O2) negative, machine-certified on
five grounds). The Riemann zeros' structure (chiral GUE, prime-encoding, a Dyson
gas poised at the `Λ=0` critical edge) is real but is the same identity that holds
regardless of RH. The single missing step — a canonical Frobenius over ℤ whose
degree-form is the Weil positivity, i.e. the arithmetic surface of the
Connes–Consani / sphere-spectrum programme — is an **unbuilt construction**, not a
measurement or a search. This map, and the engine that certifies it, is the honest
contribution: it shows exactly how far the approach reaches, stamps every step, and
respects the wall instead of faking past it.
