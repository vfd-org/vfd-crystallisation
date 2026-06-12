# WO-RH-UNIVERSAL-BOUNDARY-SCATTERING-001 — Universal Boundary-Scattering Law (report)

**Status:** run; **shared architecture is REAL but KNOWN (trace-formula /
Lax–Phillips scattering), and transfers NO proof.** Strongest of the three
route_c probes — genuinely structural, not visual — but still the same wall.
Modules: `boundary_scattering_system.py`, `arithmetic_response.py`,
`toy_horizon_scattering.py`, `compare_scattering_laws.py`; plot in `plots/`.
**No proof of RH; no φ; no God Prime; zeros/QNMs only validate.**

## 1. Summary
Tested whether arithmetic RH and black-hole horizon ringdown share a *formal*
boundary-scattering law: impulses → determinant → log-derivative response →
resonance poles → stability/contraction. The answer is **yes, genuinely** — and
that "yes" is the known **trace-formula / scattering-determinant** architecture
(Selberg–Weil; Lax–Phillips/Faddeev–Pavlov realise the ζ-zeros as scattering
resonances). Concretely shared (not visual):
- **Γ-function determinant** — completed ξ has `π^{−s/2}Γ(s/2)`; the Pöschl–Teller
  toy determinant is a Γ-ratio `1/[Γ(½+iν−iw)Γ(½−iν−iw)]`.
- **digamma boundary response** — both log-derivative responses are *ψ-valued*
  (Γ-determinant ⟹ ψ-response); the arithmetic archimedean term is the same
  `½ψ(¼+iξ/2)` that is the route_b capacity multiplier.
- **log-derivative response with poles at the resonances** (zeros / QNMs).
- **resonances on line(s)** — ζ-zeros on the critical line; PT QNMs
  `ω_n = α(±ν − i(n+½))` on two vertical lines in the lower half-plane.
- **stability = self-adjointness/contraction**; **archimedean Γ = greybody factor**.

**But it yields no new mathematics and no provability transfer.** The toy's
stability is *provable precisely because the potential is real* (self-adjoint ⟹
damped QNMs); the arithmetic instance of the identical statement is "the prime
scattering system is self-adjoint" = **Hilbert–Pólya = RH**. The architecture
**relocates** RH into scattering language; it does not weaken it. The "universal
contraction law" is the route_b `‖K‖≤1` in a new dress.

## 2. Why this route after funnel/envelope failure
HORIZON-INVARIANT-001 (no stable envelope) and BLACK-HOLE-FUNNEL-001 (radius
cosmetic) showed the prime-specific content is the oscillatory *response*, not a
shape. This WO correctly targeted the **response/scattering** structure — the
right object — and found the shared architecture is real, just already known.

## 3. Anti-circularity
Arithmetic response `−ζ′/ζ(½+iξ)` and archimedean `½ψ(¼+iξ/2)` built from ζ/Γ;
toy determinant/response from the PT potential parameters `(V0,α)` only. **No zero
heights or QNM poles used in construction.** ζ-zeros (mpmath) and the QNM ladder
appear only in §6[3] as *validation* of the already-defined responses' poles.

## 4. Abstract `BoundaryScatteringSystem`
7-tuple `(impulse_source, capacity_term, determinant, response=d log det,
resonances, stability_form, failure_mode)` + `provable` flag. Instantiated for
both systems (`boundary_scattering_system.py`).

## 5–6. The two instances and what is shared

| component | arithmetic ζ | toy horizon (Pöschl–Teller) |
|---|---|---|
| impulses | primes `Λ(n)` (closed orbits) | trapped modes of `V0 sech²(αx)` |
| capacity / boundary | archimedean `π^{−s/2}Γ(s/2)` + pole | greybody `|T|²` (Γ-ratio) |
| determinant | `ξ(s)` | `Δ(ω)=1/[Γ(½+iν−iw)Γ(½−iν−iw)]` |
| response (`d log det`) | `−ζ′/ζ(½+iξ)` | `(i/α)[ψ(½+iν−iw)+ψ(½−iν−iw)]` |
| boundary response | `½ψ(¼+iξ/2)` (digamma) | ψ-sum (digamma) |
| resonances | zeros ρ (on the line ⟺ RH) | QNMs `α(±ν−i(n+½))`, all `Im<0` |
| stability | Weil pos. / `‖K‖≤1` | no growing mode / contractive S |
| **provable?** | **OPEN (= Hilbert–Pólya = RH)** | **YES (V real ⟹ self-adjoint)** |

**[2] digamma — structural, not a numeric coincidence.** Both responses are
ψ-valued because both determinants are Γ-objects. They are **not** the same
function of the scan variable: arithmetic `Re ½ψ(¼+iξ/2)` runs 0.46→1.01→1.35
(ξ=5,15,30); the toy response on the real axis is a different (here near-constant)
value. The shared content is the **functional class (Γ→ψ)**, not a fitted match.

**[3] poles at resonances (validation).** `−ζ′/ζ(½+iξ)` **diverges at every
zero** (numerically >10⁶ on-grid vs baseline ≈0.5 between zeros — a pole). The
PT response has poles exactly at the QNMs `α(±ν−i(n+½))`; for `V0=4,α=1` these are
`(±1.94, −0.5), (±1.94, −1.5), …`, **all `Im<0`** (damped/stable).

**[4] stability = self-adjointness — the crux.** PT QNMs lie in the lower
half-plane **provably**, because `H=−d²/dx²+V` with `V` real is self-adjoint
(real spectrum ⟹ resonances damped). The arithmetic instance of the *same*
statement — zeros on the line ⟺ the prime scattering system is self-adjoint /
`‖K‖≤1` — is **Hilbert–Pólya = RH, open**. *(Honest caveat: my one-line
"gain/non-self-adjoint" perturbation of the toy stayed damped (`−1.97−0.12i`), so
it did **not** itself demonstrate a crossing; the failure-mode claim rests on the
standard theorem that non-self-adjoint `V` can push resonances to `Im>0`, not on
that number.)*

**[5] smooth vs structured.** Arithmetic: smoothed-PNT overshoots capacity
(`μ=1.26>1`, HORIZON-INVARIANT-001); structured primes restore `‖K‖≤1`. Toy:
removing the barrier (`V0→0`, `ν` imaginary) kills the real resonance ladder; the
structured barrier creates the damped QNMs. The failure modes **align
qualitatively** (structure is what creates a stable resonance spectrum), but this
is an analogy, not a theorem-level identity.

## 7. What is genuinely shared vs only analogy
- **Genuinely shared (formal):** Γ-determinant; ψ-valued log-derivative response;
  poles-at-resonances; resonances-on-lines; stability = self-adjointness /
  contraction; **archimedean Γ ≅ greybody factor**. This is the recognised
  trace-formula / Lax–Phillips scattering correspondence.
- **Only analogy:** the smooth-overshoot ↔ no-barrier alignment (qualitative);
  any "we live in a black hole" reading (rejected); funnel geometry (rejected,
  prior WO).

## 8. Universal-law candidate — verdict
> *Stability of a boundary-scattering system ⟺ the normalised response operator is
> contractive (`‖C^{−½} I C^{−½}‖ ≤ 1`), with resonances confined to the allowed
> boundary domain.*

This schema is **viable and shared** — but it is **the known scattering/trace
framework**, and its arithmetic instance is **exactly** `‖K‖≤1` = RH. So:
**promising-but-known; not new math; no provability transfer.**

## 9. The crux (why no breakthrough)
The toy is solvable because **self-adjointness is given** (real potential). The
entire difficulty of RH is that the arithmetic system's self-adjointness is
**not** given — that *is* Hilbert–Pólya. A correspondence that maps RH onto "prove
the arithmetic scattering operator is self-adjoint" returns RH to its oldest open
form. Illuminating; not a new lever.

## 10. What this does and does NOT claim
- **Does NOT:** prove RH; claim black holes prove RH; claim ζ-zeros are physical
  QNMs; claim a *new* invariant; claim a numeric digamma match (it's structural);
  claim the gain-control demonstrated instability (it did not).
- **Does:** establish a genuine, concrete shared formal architecture (Γ-determinant,
  ψ-response, poles-at-resonances, stability=self-adjointness, Γ=greybody);
  identify it as the known trace-formula/Lax–Phillips framework; and show the
  arithmetic instance is exactly the route_b/Hilbert–Pólya wall — no proof transfers.

## 11. Obstructions
- The shared law's arithmetic instance = RH (`‖K‖≤1`); no sub-RH sublemma.
- Self-adjointness is *assumed* in the toy, *open* in arithmetic — the whole gap.
- digamma sharing is structural (Γ→ψ), not a fitted identity.

## 12. Recommended next WO
This is closest to the WO's **WO-RH-ARCHIMEDEAN-GREYBODY-002** thread — the one
concrete, defensible shared object is **Γ/pole completion as an arithmetic greybody
factor** (`½ψ(¼+iξ/2)` = boundary response in both). But that correspondence is
*known* (the archimedean local factor is the scattering datum at the infinite
place), so it would document, not break, the wall. The constructive next step
remains **WO-RH-OPERATOR-ROUTE-PUBLISH-001**: freeze route_b + the three route_c
negatives (envelope / funnel / scattering) as the bundle's honest RH-frontier —
*the prime-specific content is the explicit-formula scattering response; its
stability is `‖K‖≤1` = self-adjointness = RH, and no envelope, geometry, or
horizon correspondence separates it from RH.*
