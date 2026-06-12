# closure-positivity-lab

**A degree-4 L-function made concrete from the icosian order over Q(√5):
two structurally independent algorithms agree at all 664 shared prime ideals,
its first 33 non-trivial zeros are computed, and the explicit formula —
read as one wave per prime — rebuilds the critical line so that the
independently-computed zeros fall on its interference fringes.**

> **Scope, stated up front: nothing here proves RH or any GRH.**
> RH(L) for this object is GRH for *one* cuspidal L-function, not the
> classical Riemann Hypothesis. Weil-form margins are positive on every
> finite test we ran, but the margin does not stabilize — we report that
> honestly as *not* evidence of asymptotic positivity.

## The paper

**`papers/closure-diffraction-rh.pdf`** — the principal artifact (6 pages,
two independent review passes, both GO; every headline number below was
re-run live by a reviewer and reproduced).

Checkable claims, with the artifact that certifies each:

| claim | value | artifact |
|---|---|---|
| Two independent algorithms (geometric Brandt enumeration in the icosian order vs point-counting the elliptic curve 31.1-a1/Q(√5)) agree on all cuspidal eigenvalues | **664/664 prime ideals to norm 4999, 0 mismatches** | `out/provenance_664.json` |
| The resulting degree-4 L-function (conductor 775 = disc(K)²·31) satisfies its functional equation | `lfuncheckfeq ≈ −126` (log₂), sign ε = +1 | `out/curve_zeros.json`, `out/_curve_zeros.gp` |
| Non-trivial zeros computed | **33 zeros to height 25**, first at t₁ = 3.679… | `out/curve_zeros.json` |
| Eigenvalue angles fit Sato–Tate | 2nd moment 0.2515 vs 0.25 | `figures/fig_satotate.png` |
| Prime-wave reconstruction: explicit formula rebuilds the critical line with **no zero data used**; the independently-computed zeros land on the fringes | see §3 of the paper | `figures/fig_diffraction.png`, `lab/prime_wave.py` |

**How to kill it:** every row above is recomputable. Extend the prime list past
norm 4999 and find one Brandt/point-count mismatch; or recompute the zeros in
PARI/GP and find one off the critical line within the certified height; or break
the functional-equation self-consistency. Any one falsifies the corresponding claim.

## Verify

```bash
python3 run_lab.py            # the finite positivity lab table (needs numpy)
python3 -m lab.li_certificate # Li-coefficient certificates, self-tests on zeta
gp -q out/_curve_zeros.gp     # recompute the L-function zeros (needs PARI/GP)
```

The 664/664 provenance and all headline JSON artifacts ship in `out/`.

## The prime phenomena ledger (complete: 10 rows)

A second experiment on the same instrument: nine of ten named
prime-distribution phenomena factored as *(all-finite-places closure product
— decidable, verified)* × *(a zero-distribution statement for an explicit
L-function — open)*; the tenth (Mersenne) is included precisely to mark
where the factorisation fails.
Layer-1 results are classical (Hardy–Littlewood 1923, Dirichlet 1837,
Chebotarev); this module verifies and organises, it does not discover. No
infinitude conjecture, RH, or GRH is claimed — the wall row is stated, not crossed.

```bash
python3 -m lab.prime_ledger     # 10 rows, ~11s, writes out/prime_ledger.json
```

Two papers:
- **`papers/prime-phenomena-ledger.pdf`** — "The Prime Field Through One
  Instrument": the verification ledger (what passes, at what gates).
- **`papers/how-the-primes-work.pdf`** — "Prime Patterns in Five Computed
  Pictures": the companion that explains *why* — wheels → one law → the
  prime/zero duality → Dyson's quasicrystal proposal → the open questions,
  each located in the zeros of an explicit L-function. All five figures
  computed by `figures/make_pictures.py`, none drawn.

Interactive (**`explorables/index.html`** is the guided tour):
- `explorables/residue-wheels.html` — pick ANY pattern of primes; the wheels
  predict its abundance and a live in-browser sieve to 2×10⁷ verifies it.
- `explorables/gap-slider.html` — all 105 even gaps vs the local product.
- `explorables/chebyshev-race.html` — the bias race, with Leech's 26,861.
- `explorables/crystal-diffraction.html` — Fibonacci φ-chain vs random vs the
  primes' spectrum with the zeta zeros overlaid (Dyson's question, scoped).

Results (sieve to 5×10⁷; zeros to height 2500 via `out/_zeta_zeros.gp`):

| row | phenomenon | local-law check | verdict |
|---|---|---|---|
| 1 | twin primes | 239,101 counted vs 239,107 Hardy–Littlewood (ratio 0.99997) | PASS |
| 2 | all even gaps (Polignac) | gap-6 = 2× twins (1.9950), gap-10 = 4/3 (1.3318), gap-210 = 16/5 (3.1994) — every ratio within 0.25% of its local product | PASS |
| 3 | Goldbach counts | 200 consecutive even N near 10⁶: mean deviation 0.65% from the per-N local product × HL integral (the 3∣N doubling included), max 2.2% | PASS |
| 4 | primes in APs (**theorem anchor**) | equidistribution deviation < 0.04% across mod 4/5/12; inadmissible classes exactly empty | PASS |
| 5 | Chebyshev bias | first mod-4 lead change at exactly x = 26,861 (Leech 1957); lead fraction 99.93%; mod-3 bias never reverses below 5×10⁷ | PASS |
| 6 | splitting in Q(√5) (**our base field**) | split fraction 0.49993 vs 1/2; exactly one twin pair with p ≡ 3 (mod 5) — the place-5 closure condition acting exactly | PASS |
| 7 | Sato–Tate for **our cuspidal L** (**theorem anchor**) | 663 Brandt angles (Steinberg prime dropped): moments (0.0005, 0.2515, −0.0000, 0.1265) vs ST (0, ¼, 0, ⅛), all within pre-set 3σ gates; KS 0.034 | PASS |
| 8 | prime gaps (Cramér) | mean gap = log x to 0.12%; maximal gap below 5×10⁷ is exactly 220 after 47,326,693 (the record); exponential-model tail defect reported — it is the HL correlation of rows 1–2 | PASS |
| 9 | Mersenne primes (**boundary row**) | Lucas–Lehmer recomputes all 18 known exponents ≤ 3300 exactly; every factor obeys q ≡ 1 (mod 2p), q ≡ ±1 (mod 8); LPW heuristic 20.8 ± 4.6 vs 18 — labelled beyond the instrument: no L-function handle | PASS |
| 10 | zero statistics (**the wall itself**) | 1,983 ζ-zeros to height 2500: spacing mean 1.0011; repulsion P(s<0.2) = 0.0025 vs Poisson 0.18 (70× suppression); variance and pair correlation within the documented finite-height correction scale 1/log(T/2π) ≈ 0.17 | PASS |

Rows 4, 6 and 7 are theorem-grade calibration anchors: the instrument must
reproduce proven mathematics exactly or it is broken. Row 7 doubles as an
audit of our own geometric eigenvalues — Sato–Tate is a theorem here, so a
persistent deviation would indict the Brandt data, not the conjecture.
Falsifiers per row live in `out/prime_ledger.json`.

---

## The realization underneath the provenance

**`realization/`** — the construction the 664/664 provenance certifies, as a
standalone pure-number-theory artifact: *A native icosian realization of
Hilbert modular forms over Q(√5)* (`realization/paper/`, v1.0.0-rc2). The
600-cell's unit group reproduces a **family** of cuspidal Hecke systems with
no fitted parameters: all 44 good prime ideals at level 31 (norm ≤ 200, both
Galois conjugates resolved), the 7/7 cuspidal-dimension sequence against
Dembélé's table (including the absent form at 59), a second rational
eigenform at level 41 (9/9 out-of-sample), and the genus-2 real-multiplication
form at level 61. 23 gate tests + an anti-circularity scan:
`cd realization && python3 -m pytest tests/ && python3 route_b/no_fit_guard.py`.

## The lab underneath

The wider laboratory asks a single structural question on finite objects where
both faces are decidable:

> When does a closure object's structure operator `T`, self-adjoint under its
> invariant trace form `B`, actually become **positive** under that form?

Run `python3 run_lab.py`. Representative rows (full run is 20 objects):

| object | self-adj (right form) | totally positive | B-positive | verdict |
|---|---|---|---|---|
| mult-φ | ✓ | · (conj 1−φ<0) | · | NOT_POSITIVE |
| mult-φ² , mult-(2+φ) | ✓ | ✓ | ✓ | POSITIVE |
| mult-(φ−2) , mult-√5 | ✓ | · | · | NOT_POSITIVE |
| mult-(1+√2) / mult-(3+√2) | ✓ | · / ✓ | · / ✓ | NOT_POS / POSITIVE |
| E8 / E7 / E6 / D4 / A4 / A3 / A2 Gram | ✓ | ✓ | ✓ | POSITIVE |
| Lorentzian , affine A1~ | ✓ | · | · | NOT_POSITIVE |
| **V₆₀₀ C_φ = L + φ⁻²I** , **24-cell C_φ** | ✓ | ✓ | ✓ | POSITIVE |
| mult-φ, **wrong form** (B=I) | · | — | — | **REJECTED_WRONG_FORM** |
| **icosian cuspidal L (RH)** | ✓ | ✓ (finite) | ✓ (finite) | **FINITE_POSITIVE_ASYMPTOTIC_OPEN** |

**Discriminator search:** of the structural features, **`totally_positive`
predicts `B_positive` on 18/18** of the gated, finite-decidable objects —
exactly. `form_posdef` and `real_spectrum` do not (12/18). The law holds across
two number fields (Q(√5) and Q(√2) — not golden-ratio-specific), seven
root-lattice rungs, and two closure-operator schemes:

> **Finite positivity law:** for a closure object with invariant form `B`,
> `T` is `B`-positive ⟺ `T` is **totally positive** (all conjugates/places > 0).
> The right form is the necessary precondition; total positivity is the
> sufficient ingredient.

And the gate works: the *same* operator (mult-φ) with the naive form `B=I`
instead of its invariant trace form is **rejected**, not scored — a wrong or
fitted form cannot earn a positive verdict.

### The honest caveat (read this)

In the finite case this law is, in hindsight, the spectral theorem: a
`B`-self-adjoint operator is `B`-positive iff its spectrum is positive, and its
spectrum *is* its set of conjugates/places. The finite cases are "easy"
precisely because all their places are finite and visible. The lab's value is
the organising principle and the localisation:

1. It unifies the programme's positivity statements as one — **positivity =
   total (all-places) positivity** — with self-adjointness-under-the-right-form
   as the shared precondition.
2. It pins exactly where RH(L) lives: the icosian object is self-adjoint and
   *finitely* positive (Brandt faces self-adjoint, Ramanujan). RH(L) is the
   statement that it is positive across **all** places — an infinite condition
   no finite computation closes. That row the lab leaves **OPEN**, gated
   separately. The paper's §5 frames this as an *analogy* with the classical
   signature dichotomy, not a classification — the Weil form is global, not
   per-place.

### Instruments

- `lab/li_certificate.py` — Li coefficients λ_n (`RH(L) ⟺ λ_n ≥ 0 ∀n`);
  self-tests on ζ (λ₁…λ₆ > 0 vs known Keiper–Li values). λ_n ≥ 0 over computed
  zeros is **evidence**, never proof.
- `lab/geometric_forcing.py` — the Weil form decomposed per prime, calibrated
  against the conductor-11 elliptic-curve L (explicit formula closes to
  residual < 1e-5). Established honestly: per-prime Ramanujan bounds cannot
  force positivity (else Ramanujan ⟹ RH); qualitative Sato–Tate cannot either
  (it is a theorem for non-CM Hilbert modular forms and RH(L) stays open);
  the open RH-adjacent content is the **rate** — the discrepancy curve √n·D_n
  (first datum: n=32 → D_n = 0.128, √n·D_n = 0.73; sample-dependent).
- `lab/prime_wave.py`, `lab/structure_factor.py` — the explicit-formula
  diffraction/reconstruction instruments behind the paper's figures.

### Companion note

`papers/total-positivity-closure-law.pdf` — the finite law (18/18), the
localisation, the two-level forcing mechanism, status-tagged throughout.

## Layout

```
papers/    closure-diffraction-rh (principal, reviewed) + total-positivity-closure-law
lab/       instruments: gate, registry, Li certificates, forcing, prime waves
out/       machine-readable artifacts incl. provenance_664.json, curve_zeros.json
figures/   paper figures + generators (make_all.py)
run_lab.py one command: table + gate + discriminator search
```

## Part of the VFD programme

This repo stands on its own as computational number theory; its motivation
comes from the wider closure-geometry programme at
[vibrationalfielddynamics.org](https://vibrationalfielddynamics.org/). Sibling
repos: [icosian-rh-geometric](https://github.com/vfd-org/icosian-rh-geometric)
(the Weil-positivity equivalence Q_A ≥ 0 ⟺ RH(L)),
[icosian-closure-object](https://github.com/vfd-org/icosian-closure-object)
(the theta identity L(Θ_I,s) = ζ_K(s)ζ_K(s−1)).
