# WS-D — The Mayer transfer operator (native, validated, reaches the wall)

The one genuinely new, non-redundant object from the lossless-folding plan: the
**Mayer transfer operator**, the modular surface realized through *its own
symbolic dynamics* — continued fractions / the Gauss map, which are native to
SL(2,ℤ).

## The object
```
(L_s f)(x) = Σ_{n≥1} (n+x)^{-2s} f(1/(n+x)),    x ∈ [0,1].
```
**Mayer's theorem (1991):** the Selberg zeta of PSL(2,ℤ)\H² is the Fredholm
determinant
```
Z_Selberg(s) = det(1 − L_s) · det(1 + L_s).
```

## Built and VALIDATED (`src/transfer_operator_mayer.py`)
- **GKW anchor:** at s=1 the eigenvalues are |λ₁| = **0.99964** (must be 1) and
  |λ₂| = **0.30352** vs the Gauss–Kuzmin–Wirsing constant **0.303663**. The
  operator is correct. **[VERIFIED]**
- **Pressure λ_max(s):** 2.106 (s=¾) → **1.000 (s=1)** → 0.599 → 0.396 → 0.199.
  The leading eigenvalue crosses 1 exactly at s=1.
- **Fredholm determinant:** det(1−L_s) → 0 at **s=1** (the trivial Selberg zero,
  where λ_max = 1). **[VERIFIED]**

## What it is — and why it still hits the wall
- This is the **most native** realization in the whole plan: SL(2,ℤ)'s *own*
  continued-fraction dynamics produce the Selberg zeta directly. Real and beautiful.
- **Riemann ζ genuinely enters:** for the cusped modular surface, the scattering
  φ(s) = ξ(2s−1)/ξ(2s) appears in the Selberg-zeta structure, so the transfer
  operator does touch ζ — it's not disconnected.
- **BUT** "the zeros of det(1−L_s) lie on the critical line" is *again* an RH-type
  statement, and the **positivity** (the operator's spectral positivity / those
  zeros being on the line) is the **same unproven wall**. The operator gives a
  native, computable *realization* of the ζ-data — **not a proof.**

## Verdict
> The Mayer transfer operator is the genuine, validated, native object the plan
> pointed at (continued fractions → Selberg zeta, GKW constant recovered). It
> realizes the modular surface through its own dynamics and even touches ζ — but
> it reaches the **identical positivity wall**. This is exactly the governing
> objection confirmed once more: a **lossless native encoding preserves the
> positivity question and cannot prove it.** Honest exploration, not progress
> past the wall. **[VERIFIED build; OPEN positivity = RH, for everyone.]**
