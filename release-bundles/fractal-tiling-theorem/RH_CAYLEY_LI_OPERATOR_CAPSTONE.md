# The Cayley–Li Operator Route to RH — Frontier Capstone

*A frozen, non-overclaiming map of the operator-route investigation.*
Companion to `paper/rh-frontier-capstone.tex` (the substrate / circle-test
capstone) and `paper/void-and-structure.tex` (the conceptual companion).

> **No proof of RH. No Hilbert–Pólya operator constructed. No role for φ.**
> Every line below is a theorem, a verified computation (with a stated gate),
> an honest negative, or an explicitly named open problem. All claims are
> reproducible from `route_b/`.

---

## 1. Abstract

Starting from the question "what operator has the Riemann zeros as its
spectrum?", this investigation tested geometric, semantic, and cavity
candidates against the real zeros (all declined), then pivoted to the
**operator's quadratic form** rather than its spectrum. That pivot reconstructed
the classical machinery: the explicit formula (heights), the functional equation
(the ½ axis), the Li/Weil criterion (positivity), and the Cayley boundary
picture (zeros on |z|=1). It then built — **stably and non-circularly** — the
arithmetic *moment side* (the completed Li coefficients from Stieltjes constants
+ the Γ factor), and isolated the single remaining step: turning the
**Li-positive sequence** into a **positive boundary kernel / Hilbert space**
(the de Branges / Connes / Weil-positivity problem). The wall is not crossed;
it is located with precision and tied to known frontier literature.

## 2. What was tested (and the discipline)

Every candidate was run against the **actual Riemann zeros** (`mpmath.zetazero`)
with controls; results were reported at their true strength, including
withholding fragile values and correcting mistaken references. The shared
discipline: mathematics stays proven-by-proof; no observer/consciousness/φ
reading is load-bearing; interpretation stays explicitly below the line.

Declined by data (controlled negatives, `route_b/`):
- `geometry_match.py` — φ-spiral, golden ratio, torus, C_φ spectrum → **no match**;
- `phase_theta_vs_zeros.py` — the ARIA semantic operator → **no match** (rank-1 at init);
- `cavity_*.py`, `three_cavity_classes.py` — real cavity → GOE; flux → GUE, but
  prime-flux = random-flux (universality washes out the primes).

The one structure the zeros keep, throughout, is **GUE** — the class is
universal/cheap; the *specific* zeros need the arithmetic.

## 3. Four classical faces of RH (all rebuilt from operators)

| face | sim | RH says |
|---|---|---|
| heights | `prime_shift_explicit_formula.py`, `rh_trace_kernel.py` | explicit formula locates γₙ |
| axis | `rh_completed_trace.py` | functional equation: ½ is the self-conjugate axis |
| positivity | `rh_positivity_detector.py` | Li/Weil: λₙ ≥ 0 ∀n |
| boundary | `rh_phi_boundary.py`, `rh_cayley_moment_operator.py` | all zeros on \|z\|=1 |

## 4. The Cayley boundary result `[verified]`

The Möbius map **z = 1 − 1/ρ** sends the critical line to the unit circle
**|z| = 1** (machine precision); the centre z=0 is the pole s=1; off-line zeros
leak radially (Re>½ inside, Re<½ outside). On-line zeros are pure boundary phase
(standing waves); off-line zeros spiral outward. The moment matrix
M_ij = m_{i−j}, m_k = Σ_ρ z_ρ^k, is **PSD on-line** with **unitary shift**, and
**loses PSD / unitarity off-line**. Doorway:

> zeros on |z|=1 ⟺ the boundary shift **U** is unitary ⟺ **H = −i log U** is self-adjoint.

(Built *from* the zeros, this is circular — a diagnostic, not a construction.)

## 5. The Stieltjes + Γ non-circular Li construction `[verified]`

`rh_arch_moment_variants.py` builds the completed Li coefficients from the
**analytic Taylor series** of log ξ(1+w):
`−log2 + log(1+w) − ((1+w)/2)logπ + logΓ((1+w)/2) + log(w·ζ(1+w))`,
with `w·ζ(1+w)` from the **Stieltjes constants** (integer-sum definition, no
zeros) and logΓ from polygamma at ½; then λ_n = n Σ C(n−1,k−1) a_k.

- λ₁–₅ verified to **~1e-8** against the literature;
- λ₁–₃₀ all ≥ 0; **exactly stable** across precision/depth (dps150/N30 vs
  dps80/N20: difference 0.0e+00);
- **fixes** the ARCH-U `mp.diff` instability (`rh_arch_u_operator.py`), which
  could only reach λ₁.

Why the archimedean term is *mandatory* (`rh_arch_u_operator.py`): the prime-only
Euler product **diverges like −log(s−1) at s=1**, exactly where the Li
coefficients live, so primes alone cannot produce them. Confirmed independently
by the completion result `rh_completed_trace.py`.

## 6. Operator doorway: U and H = −i log U

The right target is **not** "an operator whose spectrum looks like the zeros"
(universality makes that cheap and meaningless) but the **unitary boundary shift
U** whose phases are the Cayley images of the zeros — built from primes +
archimedean data, non-circularly. Then `H = −i log U` is self-adjoint iff the
shift is unitary iff the zeros lie on the boundary. This is the cleanest
statement of Hilbert–Pólya in this picture.

## 7. Why the naive Toeplitz kernels fail `[verified]`

The Li coefficients are a **positive sequence** (λₙ ≥ 0), but the naive kernels
built from them are **not** positive operators: `K_ij = λ_{|i−j|}` has min
eigenvalue −7.8; `K_ij = λ_{i+j}` has −4.2. And there is no naive probability
moment sequence (`Σ_ρ 1` diverges). **Positivity of a sequence is not positivity
of a kernel.** The naive boundary kernels are decorative.

## 8. The positive space, found — and the remaining wall

**Update (WO-RH-DEBRANGES-BRIDGE-001, Probe B — validated):** the missing
inner-product space is the **Weil test-function space.** The Weil quadratic form
`Q_ij = EF(φ_iφ_j)` on an even-Gaussian basis (built from primes + archimedean,
zeros only in the gate) is **PSD** (min eig +0.27) and matches the zero-side
Gram to **machine precision** (`Q = 2·Z`, the 2 = ±γ). Dropping the archimedean
ψ-integral breaks PSD (−3.21). So:

> Li/Weil positivity lives in the **Weil test-function space** (PSD there),
> **not** in naive boundary moments (the λ_n Toeplitz kernels were −7.8/−4.2,
> the *wrong space*); and the **archimedean term carries the positivity**
> (4th independent confirmation, after COMPTRACE / ARCH-U / ARCH-MOMENTS).

The remaining gap is now one step further in:

> **Realise this validated positive Weil form as a non-circular operator**
> (Connes-style scaling/compression, or a de Branges reproducing kernel) — and
> the open content is that the form is PSD for *all* test functions, i.e.
> global Weil positivity, i.e. RH.

This is the de Branges / Connes frontier — now standing on a *validated* positive
form rather than a failed kernel.

## 9. Connection to de Branges / Connes / Weil positivity

The wall sits exactly on known frontier territory:
- **Li / Bombieri–Lagarias / Lagarias** — the Li coefficients are the Weil
  quadratic functional evaluated on a specific family; λₙ ≥ 0 ⟺ RH.
- **Connes–Consani**, *Weil positivity and the trace formula, the archimedean
  place* — Weil positivity, the archimedean term, and Hermitian/Toeplitz
  positivity in precisely this setting (the mandatory-Γ result here is the
  numerical shadow of their archimedean term).
- **Suzuki** and the de Branges-space route — a Hilbert space derived from the
  Weil distribution, related to de Branges spaces: this *is* the "right inner
  product" the failed naive kernels were missing.

(These are cited as the established frontier the route lands on; this work
reproduces their *necessity-of-archimedean* signal numerically, it does not
extend their theorems.)

## 10. What this does **not** prove

- Not RH; not GRH; not any new theorem.
- No Hilbert–Pólya / de Branges / Connes operator is constructed.
- The Stieltjes+Γ Li construction is a faithful, stable *implementation* of
  classical mathematics (Keiper–Li/Coffey), not new mathematics.
- λₙ ≥ 0 verified only on a finite range; positivity for all n is RH.
- No role for φ anywhere (the φ-radial coordinate was a constant rescale).

## 11. Next work order — and what's now done

**Done (WO-RH-DEBRANGES-BRIDGE-001, Probe B + WO-RH-CONNES-SCALING-COMPRESSION-001,
Probe C):** the positive form is found and *realised as an operator*. Probe B:
the validated Weil form is PSD in the test-function space (archimedean carries
it). Probe C: that form is the quadratic form of an explicit **Connes scaling
operator** `D = (archimedean multiplier on the dilation generator) + pole −
Σ_n Λ(n)/√n (scaling-translations by log n)`, built non-circularly; its
compression is PSD on every cutoff, with the min eigenvalue **shrinking toward 0**
(marginal, knife-edge positivity — the signature of RH being the critical case).

**Open / next:** the genuinely hard step — **prove D ≥ 0 in the full limit**
(= Weil positivity for all test functions = RH). Numerics can't cross this (the
shrinking min eig shows the limit is delicate). Independent cross-check:
**Probe A** (de Branges reproducing kernel from a Hermite–Biehler E built from
ξ). Beyond that is the actual de Branges / Connes proof problem — untouched, and
the honest end of the operator route.

---

### One-sentence status
The operator route is mapped to its floor: the Cayley boundary picture is exact,
the Li-positive moment side is built stably and non-circularly from Stieltjes +
Γ, and the single remaining step — a positive boundary kernel / Weil–de Branges
inner product — is isolated, named, and tied to the open frontier. Nothing
overclaimed; nothing pushed.
