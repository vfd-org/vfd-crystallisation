# Technical core — the witness operator on the scale axis

*Draft of §§(2)–(4) of the bridge paper. Classical inputs (Weil explicit formula, Tate's
local theory, the Weil positivity criterion) are cited, not reproven; the new content is
(i) the realisation of the witness as one operator `A` on the scale axis, and (ii) the
identification of its prime-side coefficients with the **geometric** icosian Brandt
eigenvalues. Rigor caveats are stated inline.*

---

## 0. Conventions

Let `π` be the self-dual cuspidal automorphic representation attached to the icosian
Brandt module at level `𝔭₃₁` over `K = ℚ(√5)`, with `L`-function (analytic normalisation)

```
L(s, π) = Σ_n λ_π(n) n^{-s} = Π_𝔮 Π_{i} (1 − α_{𝔮,i} N𝔮^{-s})^{-1},
```

completed `Λ(s,π) = N^{s/2} L_∞(s,π) L(s,π)` with `Λ(s,π) = ε Λ(1−s,π)`, conductor
`N = 775`, and archimedean factor `L_∞(s,π) = Π_j Γ_ℝ(s + μ_j)`, `Γ_ℝ(s)=π^{-s/2}Γ(s/2)`.
Write the log-derivative coefficients

```
−(L'/L)(s,π) = Σ_n Λ_π(n) n^{-s},   Λ_π(N𝔮^k) = ( Σ_i α_{𝔮,i}^k ) · log N𝔮.
```

The first one, `a_𝔮 := λ_π(𝔮) = Σ_i α_{𝔮,i}`, **is the geometric Brandt/Hecke eigenvalue**
read off the 600-cell (the `witness-from-triad` result). Ramanujan for `π` (holomorphic
Hilbert-modular via Jacquet–Langlands, then Deligne-type bounds) gives `|a_𝔮| ≤ 2` per
place, hence `|Λ_π(N𝔮^k)| ≤ d·log N𝔮` with `d = deg`. **This bound is what makes every
sum below converge on Schwartz data** — it is the discharged version of the old "tail
bound" worry.

**Scale axis.** Coordinate `t ∈ ℝ`, multiplicative variable `x = e^t ∈ ℝ₊*`. Test
functions `h ∈ C_c^∞(ℝ)`. Transform and inverse

```
ĥ(r) = ∫_ℝ h(t) e^{i r t} dt,     h(t) = (1/2π) ∫_ℝ ĥ(r) e^{-i r t} dr.
```

A nontrivial zero `ρ = ½ + iγ` of `L` sits at the spectral point `γ ∈ ℂ`; RH(L) is the
statement that every `γ` is **real**.

**Two structures the cylinder gives for free.**
- **Translation** `(τ_a h)(t) = h(t − a)`: a prime of norm `N𝔮` will act by `τ_{log N𝔮}`.
- **Involution** `h^*(t) = \overline{h(−t)}`: the reciprocal mirror `t ↦ −t`. Under the
  transform this is `s ↦ 1 − s` — **the functional equation is the mirror symmetry of the
  scale axis.**

---

## (2) The archimedean operator `A∞` from the scale-axis boundary (Tate at ∞)

**Claim.** The archimedean term of the explicit formula is a Fourier multiplier on the
scale axis whose symbol is the log-derivative of the gamma factor, and it arises as the
`t → ±∞` boundary data of the scale axis via Tate's local zeta integral.

*Tate's local integral.* At the archimedean place, for a Schwartz `f_∞` on `K_∞`,

```
Z_∞(s, f_∞) = ∫_{K_∞^×} f_∞(x) |x|^s d^×x  =  L_∞(s, π) · (entire factor),
```

and the convergence/continuation of `Z_∞` is governed entirely by the behaviour of the
integrand as `|x| → 0` and `|x| → ∞` — i.e. as `t → −∞` and `t → +∞` on the scale axis.
The local functional equation `Z_∞(s, f_∞) = γ_∞(s) Z_∞(1−s, \hat f_∞)` is exactly the
mirror `t ↦ −t`. So **`L_∞` is the boundary invariant of the scale axis**, not an external
import.

*The operator.* Define the **archimedean symbol**

```
ω_∞(r) := log N + ½[ (L_∞'/L_∞)(½ + i r, π) + (L_∞'/L_∞)(½ − i r, π) ]
        = log N + Σ_j Re ψ_ℝ( ½ + μ_j + i r ),   ψ_ℝ = (Γ_ℝ'/Γ_ℝ),
```

and let `A∞` be the self-adjoint Fourier multiplier with symbol `ω_∞`:

```
A∞ := F^{-1} ∘ (multiply by ω_∞) ∘ F      (so  ⟨h, A∞ h⟩ = (1/2π)∫ ω_∞(r) |ĥ(r)|² dr ).
```

`ω_∞(r) ≥ 0` for large `|r|` (digamma grows like `log|r|`); `A∞` is the **boundary/capacity
term `H`** of the closure picture. *Status: this is Tate (1950) + standard digamma; the
only new thing is reading it as the scale-axis boundary operator.*

---

## (3) Assembling the witness operator `A`

Define the **prime operator** as the geometric weighted sum of symmetric scale-shifts:

```
A_P := Σ_𝔮 Σ_{k≥1}  ( Λ_π(N𝔮^k) / N𝔮^{k/2} ) · ½( τ_{k log N𝔮} + τ_{−k log N𝔮} ).
```

The `k = 1` coefficient is `a_𝔮 · log N𝔮 / N𝔮^{1/2}` — **the geometric Brandt eigenvalue,
times the analytic weight, attached to a translation of the scale axis by `log N𝔮`.** This
is the precise sense in which "the geometry supplies the coefficients and the scale axis
carries them."

*Convergence.* For `h ∈ C_c^∞`, `⟨h, τ_a h⟩ = (h ⋆ h^*)(a)` is Schwartz in `a`; with
`|Λ_π(N𝔮^k)| ≤ d \log N𝔮` (Ramanujan, §0) and `N𝔮^{-k/2}` decay, the double sum converges
absolutely. `A_P` is self-adjoint and bounded on the `C_c^∞` domain. *This is the step the
earlier memo flagged as "the one real analysis risk"; Ramanujan discharges it.*

**The witness operator.**

```
┌─────────────────────────────────────────────┐
│   A  :=  A∞  −  A_P                          │
│       =  (archimedean boundary)  −  (geometric prime shifts)   │
└─────────────────────────────────────────────┘
```

`A` is self-adjoint on the `C_c^∞(ℝ)` domain. It is the closure-picture `Q = H − R` made
into an operator: `H = A∞` (boundary capacity), `R = A_P` (arithmetic residue).

---

## (4) The identification lemma and the equivalence

**Lemma (identification).** For every `h ∈ C_c^∞(ℝ)`,

```
⟨ h, A h ⟩  =  Σ_ρ |ĥ(γ_ρ)|² ,
```

the sum over the nontrivial zeros `ρ = ½ + iγ_ρ` of `L(s,π)`.

*Proof.* Apply the Weil explicit formula (Iwaniec–Kowalski, Thm 5.12) to the even,
positive-type test function `g = h ⋆ h^*`, for which `ĝ(r) = |ĥ(r)|²`:

```
Σ_ρ |ĥ(γ_ρ)|² = (1/2π)∫ ω_∞(r) |ĥ(r)|² dr
              − Σ_𝔮 Σ_k (Λ_π(N𝔮^k)/N𝔮^{k/2}) (h⋆h^*)(k log N𝔮).
```

The first term is `⟨h, A∞ h⟩` by definition of `A∞`. For the second, `(h⋆h^*)(a) =
⟨h, τ_a h⟩`, so the prime sum is `⟨h, A_P h⟩`. Hence `Σ_ρ |ĥ(γ_ρ)|² = ⟨h, (A∞ − A_P) h⟩ =
⟨h, A h⟩`. The rearrangement is justified by the §0 convergence bound. ∎

**Theorem (VFD-native equivalent).**

```
A ≥ 0   on the C_c^∞ domain   ⟺   RH for L(s,π)
                              ( i.e. every zero γ_ρ ∈ ℝ ).
```

*Proof.* (⇐) If RH(L) holds, each `γ_ρ ∈ ℝ`, so `|ĥ(γ_ρ)|² ≥ 0` and the Lemma gives
`⟨h,Ah⟩ ≥ 0`. (⇒) If some `γ_{ρ₀} ∉ ℝ`, the functional equation pairs it with a reflected
zero, and the classical Weil argument (choose `h` with `ĥ` an approximate identity peaked
at `γ_{ρ₀}` along the analytic continuation) makes `⟨h,Ah⟩ < 0`. Both directions are the
Weil criterion; the content here is that the criterion is the **positivity of the single
operator `A`** above. ∎

**Reading.** `A ≥ 0` is the closure law `Q[Φ] ≥ 0` of the VFD object, now a precise operator
statement, and the theorem is the VFD-native *equivalent* of RH(L): **one self-adjoint
operator on the scale axis, with archimedean boundary part `A∞` (Tate) and arithmetic part
`A_P` built from the geometric icosian eigenvalues, is positive if and only if the
Riemann-type Hypothesis holds for this `L`.**

---

## What is proved here, and what is not

- **Proved (this core):** the equivalence `A ≥ 0 ⟺ RH(L)`, with `A` constructed
  geometry-first — boundary from the scale axis, coefficients from the 600-cell.
- **Not proved (the wall):** that `A ≥ 0` actually *holds*. That is RH(L) itself
  (= GRH for this cuspidal `L`), and it is **not** addressed.
- **Scope:** `L(s,π)` is the icosian **cuspidal** `L` (so RH(L) here is GRH for one
  `L`-function), **not** classical `ζ`. Classical `ζ` is the Eisenstein face, which is not
  positivity-valid for this operator; it stays open.
- **Novelty, honestly:** the construction is an *assembly* of classical pieces (explicit
  formula + Tate + Weil criterion); the genuinely new content is the **explicit scale-axis
  operator with geometric Brandt coefficients** and the resulting clean operator-positivity
  equivalent. It is a new, concretely realised member of the Weil/Li/Hilbert–Pólya family —
  not a new hard theorem, and not a step toward crossing the wall.
```
