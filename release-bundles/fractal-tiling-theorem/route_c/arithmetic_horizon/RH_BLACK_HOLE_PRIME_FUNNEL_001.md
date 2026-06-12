# WO-RH-BLACK-HOLE-PRIME-FUNNEL-001 — Compressed Prime Funnel (report)

**Status:** run; **black-hole funnel is a VISUALISATION, not new mathematics —
no new invariant.** One real (but *known*) prime-specific signal, demonstrated
honestly. Sim: `route_c/arithmetic_horizon/rh_black_hole_prime_funnel.py`;
plots in `funnel_gallery/`. **No proof of RH; no φ; no God Prime; zeros used
only as a final validation overlay.**

## 1. Summary
Tested whether plotting prime pressure as **compressed black-hole infall** (depth
`= log n`, compressed radius `r = 1/log n`, phase `θ = ξ log n`) and studying the
**cancellation field `ΔR = R_smooth − R_prime`** reveals stable, prime-specific
"horizon geometry." It does not. Three findings:
1. **The compression is cosmetic.** `r(n)` is a bijective re-coordinate; it does
   **not** enter the spectral transform `Σ_n w(n)e^{iξ log n}` — the ξ-spectrum is
   *byte-identical* for `r=1/log(n+e)`, `n^{−0.25}`, `1/(1+log n)`. The funnel is
   a picture, not a mechanism.
2. **`ΔR` has no grooves.** It is two **smooth branches** — `(1−log p)/√p < 0` on
   primes, `+1/√n` on composites — whose only "structure" is the prime/composite
   split (i.e. the primes themselves). Not low-prime-dominated, but not a rich
   geometric object either.
3. **The one real signal is the known explicit formula.** The real von Mangoldt
   ξ-coherence resonates **~10× at every zero**; smoothed-PNT is **flat**. But this
   is exactly `Σ Λ(n)n^{−½−iξ} = −ζ′/ζ(½+iξ)` (poles at γ) — the CONTRACTION-002
   symbol — and it *reads out* the known γ, so it is **validation, not new
   construction or new geometry.**

**No new invariant. The black-hole picture stays interpretive.**

## 2. Why route_c continued here
HORIZON-INVARIANT-001 showed the pressure *envelope* is generic (smoothed-PNT
reproduces it, overshooting `μ=1.26>1`), and the prime-specific content is the
**cancellation** `ΔR`. This WO asked whether `ΔR` has its own stable compressed
geometry. Answer: no — `ΔR`'s only content is the explicit-formula resonance,
which lives in the 1-D ξ-spectrum, not in any funnel coordinate.

## 3. Anti-circularity
`R_prime`, `R_smooth`, `ΔR`, the ξ-scan, and all geometry built from primes +
prime powers + smooth density only. **No zero heights, no Cayley phases, no
fitting to zeros, no RH/Weil/Li assumed.** Known γ_n appear **only** in §6[B]/[D]
as a *post-hoc read-out* of the resonance enhancement — never in construction,
and the funnel/spectrum are computed blind to them.

## 4. Coordinates & fields (definitions)
Depth `x = log n`; compressed radius `r ∈ {1/log(n+e), n^{−β}, 1/(1+log n)}`;
phase `θ_ξ(n) = ξ log n mod 2π`; embedding `(r cosθ, r sinθ, −x)` (large n fall
deep). Weights `w_prime = Λ(n)/√n`, `w_smooth = 1/√n` (avg von Mangoldt = 1 on
every integer), `ΔR = w_smooth − w_prime`. Coherence `C_w(ξ) = Σ_n w(n)cos(ξ log n)`.

## 5. Black-hole / horizon analogy — *interpretation only*
"Large primes fall deeper and project onto a smaller boundary radius; smooth
density over-collapses; prime fluctuations regularise the horizon." Evocative,
but §6[C] shows the radius carries **zero** mathematical content, so the analogy
is a *visual coordinate model*, not structure. Recorded as interpretation only.

## 6. Results

**[A] `ΔR` structure.** On primes `ΔR=(1−log p)/√p` (n=2:+0.217, 3:−0.057,
5:−0.273, 7:−0.358 …); on composites `ΔR=+1/√n`. Absolute cancellation mass is
**not** low-prime-dominated (only 0.2% below n=11, 8% below n=1000 — spread over
the composite bulk `~2√N`), but `ΔR` is **two smooth monotone branches**, no
ridges/grooves. The only "structure" is prime-vs-composite.

**[B] ξ-coherence (ξ∈[10,50], smooth-tapered, above the bulk).** Enhancement =
`max|C|` within ±0.5 of γ, over median|C|:

| field | enhancement at the 9 known γ | reading |
|---|---|---|
| **real prime** | **10.3×** (uniform 9.9–10.8×) | resonates at *every* zero |
| smoothed-PNT | **1.6×** (0/9 above 3×) | **flat — no zero resonance** |
| shuffled-Λ | 4.6× over a huge noise floor (median 5.8 vs prime 0.81) | incoherent |
| real @ 200 random ξ | 4.2× | at-γ is 2.5× a typical ξ |

> **Honest caveat (a corrected false start):** the *raw, hard-cutoff* sum is
> swamped by a low-ξ **bulk** where real and smooth coincide; a naive global
> peak-finder returns that bulk (ξ≈0.5–0.9), **not** the zeros, and there the
> controls look identical. The genuine prime-specific resonance only appears
> **above the bulk (ξ≥10) with a smooth taper**, as tabulated. This was caught
> and fixed before reporting.

**[C] Compression is cosmetic.** ξ-spectrum hash identical (`4a2bfbe4`) for all
three radial maps — `r(n)` does not enter `Σ w(n)e^{iξ log n}`. **The funnel adds
no mathematics.**

**[D] Validation overlay (zeros only here).** Real-prime coherence resonates
(>3×) at **9/9** known γ; smoothed-PNT at **0/9**. This is the **known explicit
formula** (`−ζ′/ζ` poles at γ), demonstrated honestly above the bulk — *not* a new
construction (it reads out γ) and *not* carried by the funnel radius.

**[E] No arithmetic "Planck cell."** `log n ↔ ξ` is a Fourier pair, so
`Δ(log n)·Δξ ≳ 2π` is the **generic** time-frequency bound, present for any
sequence (smooth or random). No prime-specific minimal cell.

## 7. Controls
- **smoothed-PNT** (fair): reproduces the bulk, **flat at the zeros** → the
  resonance is prime-specific, the bulk is generic.
- **shuffled-Λ** (log-support-preserving): high incoherent noise floor, no clean
  γ-structure → coherence destroyed.
- **random ξ**: at-γ enhancement 2.5× a typical ξ → the γ-alignment is real
  (modulo accidental proximity of a few random ξ to zeros).

## 8. Compressed vs ordinary geometry
Identical information (§6[C]). The compressed view makes large-n infall *visually*
compact but cannot reveal structure absent from the ξ-spectrum. **No structure is
gained by compression.**

## 9. Interpretation / verdict
The black-hole/holographic funnel is a **productive picture** (the plots are nice
intuition for "primes as compressed infall, smooth density over-collapsing"), but
it is **not new mathematics**: the radius is cosmetic, `ΔR` is two smooth branches,
and the only prime-specific content is the **already-known explicit-formula
resonance** (`−ζ′/ζ` poles at the zeros = the CONTRACTION-002 symbol). This is the
*same* wall reached three times now (operator route, horizon-invariant, here):
**the prime-specific object is the explicit-formula fluctuation = RH itself, not a
separable geometry or envelope.**

## 10. What this does and does NOT claim
- **Does NOT:** prove RH; find a new invariant; find a God Prime / arithmetic
  Planck cell; claim the black-hole geometry is mathematically load-bearing; claim
  the radius matters; claim zero-tuning was avoided if γ were used (they were used
  only to *read out* the resonance, never to build).
- **Does:** show the funnel radius is cosmetic; show `ΔR` is two smooth branches;
  honestly demonstrate the real-prime ξ-resonance (10.3× at γ vs 1.6× smooth) and
  identify it as the known `−ζ′/ζ` explicit formula; show no arithmetic Planck cell
  beyond generic Fourier uncertainty; and flag/fix a low-ξ-bulk false start.

## 11. Obstructions
- Radius is a bijection → no geometric degree of freedom.
- `ΔR` has no grooves (two smooth branches).
- The prime signal is the explicit formula (validation, not construction).
- Naive coherence is bulk-dominated; the real signal needs bulk removal + taper.

## 12. Recommended next WO
This is the WO's **WO-RH-HORIZON-GEOMETRY-OBSTRUCTION-001** outcome (compressed
funnel geometry yields no new invariant), with the plots retained as
**WO-RH-HORIZON-VISUAL-GALLERY-001**-style *intuition-only* material (`funnel_gallery/`).
The constructive next step remains **WO-RH-OPERATOR-ROUTE-PUBLISH-001**: freeze
route_b + route_c (both negatives) as the bundle's honest RH-frontier statement —
*the prime-specific content of the horizon law is the explicit-formula fluctuation
(RH), and neither a stable envelope nor a compressed geometry separates it out.*
