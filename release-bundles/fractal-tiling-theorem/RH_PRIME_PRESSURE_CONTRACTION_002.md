# WO-RH-PRIME-PRESSURE-CONTRACTION-002 — Analytic Contraction Bound (report)

**Status:** run; **obstruction-report outcome — the contraction is sharp but
RH-equivalent; one route reveals the crux.** Sim:
`route_b/rh_prime_pressure_contraction.py`. **No proof of RH; no proof of
‖K‖≤1; no φ; no zeros in construction; no God Prime claimed.**

## 1. Summary
This was the first *proof-oriented* attack on the sharpest formulation reached:
**RH ⟺ ‖K‖ ≤ 1**, `K = H^{−½} R H^{−½}`, `H = A + P` (archimedean + pole
capacity, PSD), `R` = prime-pressure. The decisive fact framing the whole WO:

> `D = H^{½}(I − K)H^{½}`, so **‖K‖ ≤ 1 ⟺ D ≥ 0 ⟺ Weil positivity ⟺ RH** — at
> *every* cutoff. The contraction is **logically equivalent to RH**, not weaker.

So no analytic route can give a free proof; each must be either **too weak** or
**RH-equivalent**. Six routes (Schur / bandwise / multiplier / factorisation /
form-limit / variational) were tested. The honest result: **all blocked**, but
the **multiplier route (C) localises the crux** — `R`'s Mellin symbol is
essentially `−ζ′/ζ(½+iξ)`, whose **poles are the zeros**, so no smooth capacity
multiplier can dominate it pointwise. That is the cleanest statement of *why*
the contraction is exactly as hard as RH.

## 2. Anti-circularity
`A`, `P`, `R`, `K` built from primes + von Mangoldt + archimedean digamma + pole
only. The symbol `r(ξ) = Σ Λ(n)n^{−½}cos(ξ log n)` is a prime sum. Known zero
heights appear **only** as evaluation points in the §6 diagnostic table to show
`r` peaks there — never in any operator construction. No RH/Weil/Li assumed.

## 3. Exact operator forms (Phase 1)
On the Gaussian test-function basis (centres `c_k = 14+4k`, k=0..11; width
`S=3`), in the `r`-variable (`s = ½+ir`) Weil/Connes representation:

- **Archimedean** `A_ij = (1/2π) ∫ ĝ_ij(r) · Re ψ(¼+ir/2) dr`, multiplier
  `M(r) = Re ψ(¼+ir/2)` (**sign-indefinite**: negative at low r).
- **Pole** `P_ij = 2 ĝ_ij(i/2) − g_ij(0) log π` (the `s=1` pole + `log π`).
- **Prime** `R_ij = 2 Σ_{n≥2} Λ(n) n^{−½} g_ij(log n)` — von Mangoldt-weighted
  scaling translations by `log n`.
- **Capacity** `H = A + P` (**PSD**, min eig +0.076 — pole lifts arch positive,
  THRESHOLD-001). **Defect** `D = H − R` (Weil form, PSD, min eig +0.00004).
- All symmetric; `K = H^{−½} R H^{−½}` symmetric ⇒ `‖K‖ = μ_max(K)`.
- Confirmed here: **μ_max(K) = 0.99979** (reproduces THRESHOLD-001).

## 4. Why ‖K‖≤1 IS RH (the wall, stated cleanly)
`⟨f, Df⟩ = Σ_ρ |ĝ(γ_ρ)|²` (explicit formula, sum over zeros). `D ≥ 0` for all
admissible `f` ⟺ every `γ_ρ` is real ⟺ RH (Weil). Since `D = H^{½}(I−K)H^{½}`
with `H ≻ 0`, this is identical to `‖K‖ ≤ 1`. **There is no sub-lemma weaker
than RH here** — only a cleaner shape for it.

## 5. Kernel / symbol form (Phase 2)
In Mellin/Fourier (log-scale) coordinates the scaling-translations `T_{log n}`
diagonalise to phases `n^{−iξ}`, so `R` has the formal **symbol**
`r(ξ) = Σ_{n≥2} Λ(n) n^{−½−iξ} = −ζ′/ζ(½+iξ)` (real part `Σ Λ(n)n^{−½}cos(ξ log n)`).
**Key structural fact:** `−ζ′/ζ` has **simple poles at every zero** `½+iγ`. So
`R` is **not** a bounded multiplier — its symbol is singular exactly at the
zeros. `H`'s multiplier `h(ξ) = Re ψ(¼+iξ/2)` is smooth (`~ ½log ξ`). This makes
`K` a sandwiched singular object, not a clean pseudo-differential operator.

## 6. Route verdicts (Phases 3–4, diagnostics)

**Route A — Schur / weighted row-sum bound.** `‖K‖ ≤ max_i Σ_j |K_ij| w_j/w_i`:

| weight w | Schur const | verdict |
|---|---|---|
| `w = 1` | **1.408** | > 1 — too loose |
| `w = diag(H)` | **1.560** | > 1 — too loose |
| `w = √capacity` | **1.477** | > 1 — too loose |

Schur over-counts the sign-varying off-diagonal of `K`; it cannot capture the
razor-thin `μ_max = 0.9998` margin. **Blocked (too weak).**

**Route C — Mellin multiplier comparison.** Need `|r(ξ)| ≤ h(ξ)`:

| ξ | `|r(ξ)|` | `h(ξ)` | `|r|≤h`? | |
|---|---|---|---|---|
| 10.00 | 2.87 | 1.61 | **no** | between zeros |
| **14.13** | **5.42** | 1.96 | **no** | **at γ₁ — r spikes, h smooth** |
| **21.02** | **6.19** | 2.35 | **no** | **at γ₂** |
| **25.01** | **5.01** | 2.53 | **no** | **at γ₃** |
| 17.00 | 0.47 | 2.14 | yes | far from any zero |

`r(ξ)` peaks **above** `h(ξ)` precisely at the zeros (where the true symbol
`−ζ′/ζ` has poles). **No pointwise multiplier bound exists.** Blocked — but this
**localises the crux**: the prime-pressure symbol is singular exactly at the
objects RH constrains. The contraction is a *form-level / integrated* statement
that these poles do not push the form past capacity — which is RH itself.

**Route D — Factorisation `I − K = B*B`.** `I−K ≽ 0` ⇒ a square root exists, but
only the **trivial** basis-dependent `(I−K)^{½}`. The *structured* `B` would be
the de Branges/Connes reproducing-kernel object — shown **missing** for the naive
`E` in SPACE-002 (kernel not PSD, −7e-3 persists at dps 200). **Blocked.**

**Route E — Form-limit / monotone convergence.** Would conclude `‖K‖≤1` from
`K_N ≤ I` + strong convergence. But the premise `μ_max(K_N) ≤ 1` is itself the
Weil criterion restricted to N test functions — i.e. **RH-restricted, not an
unconditional input**. `μ_max(K_N) > 1 ⟺` an off-line zero detectable in range.
**Circular** (assumes finite RH).

**Route F — Variational / extremal.** `sup_f ⟨f,Rf⟩/⟨f,Hf⟩ = μ_max(K)`. The
threshold equation `Rf = Hf` characterises the near-null modes (NULLMODE-FACTOR:
stable, low-edge, archimedean-carried, spread). `μ > 1 ⟺` off-line zero (Weil).
**The extremal problem IS RH** — no simplification.

## 7. Controls
The symbol-peaks-at-zeros effect is a **prime-structure** signature: shuffling
`Λ(n)` destroys the `−ζ′/ζ` pole structure (the peaks at γ vanish), and
removing the pole drops `H` below PSD (THRESHOLD-001 / NULLMODE-FACTOR). The
α-sweep gives `α_c = 0.9999` (real Γ exactly critical). None of these change the
verdict; they confirm the structure is prime-and-archimedean-carried, not
artefact.

## 8. Best theorem candidate & the exact remaining lemma
> **Multiplier-crux lemma.** For all admissible `f`,
> `Σ_n Λ(n)n^{−½}⟨f, T_{log n} f⟩ ≤ ⟨f, (A+P) f⟩` — equivalently, the
> prime symbol `−ζ′/ζ(½+iξ)` is dominated *in the form sense* by the pole-lifted
> archimedean capacity, **across its poles at the zeros**.

This is the sharpest, cleanest target the route produces — a single named
operator-norm inequality with the real Γ coefficient exactly critical. **But it
is RH** (the form-sense domination across the symbol's poles is precisely the
positivity of `Σ_ρ|ĝ(γ_ρ)|²`).

## 9. Verdict / what this does and does NOT establish
- **Does:** documents the exact operator forms; states the contraction
  equivalence cleanly; tests six routes analytically + numerically; shows Schur
  is too loose; shows the multiplier route fails **and why** (symbol `= −ζ′/ζ`,
  poles at zeros); shows D/E/F reduce to RH; confirms `H` PSD needs the pole and
  `α_c ≈ 1`.
- **Does NOT:** prove RH; prove `‖K‖ ≤ 1`; claim finite `μ_max<1` proves the
  infinite contraction; claim any inequality unconditional that secretly uses
  RH-strength input; identify a God Prime.
- **Net:** the contraction reformulation is **sharper and cleaner** than raw
  Weil positivity (one named norm inequality, real Γ critical), but it is
  **logically equivalent to RH at every cutoff** — there is *no* weaker
  sub-lemma in this route. The single most illuminating finding is the crux:
  **`K`'s difficulty is that the prime-pressure symbol `−ζ′/ζ` is singular
  exactly at the zeros.**

## 10. Recommendation for next proof step
The honest reading: this route has reached its floor. Per the WO's own decision
tree this is the **WO-RH-CONTRACTION-OBSTRUCTION-REPORT-003** outcome (all
routes RH-equivalent or too weak), with the bonus that **Route C is the right
place to keep looking** if anyone continues — but it requires controlling
`−ζ′/ζ` around its poles, which is RH. The constructive next step is therefore
**not** another route but **WO-RH-OPERATOR-ROUTE-PUBLISH-001**: freeze the
operator route (Cayley → Stieltjes/Γ Li → Weil Probe B → Connes Probe C →
de Branges → near-null → contraction → this obstruction) as the bundle's honest
RH-frontier statement.
