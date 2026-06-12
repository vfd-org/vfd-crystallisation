# Where ℍ becomes ℂ: the class transition traced (Tier-1, done)
### 2026-05-30 · `route_b/jacquet_langlands_trace.py`

The question: where does the substrate's **quaternionic** (ℍ, β=4, GSE,
degenerate) arithmetic become the **complex/unitary** (ℂ, β=2, GUE) object
whose high zeros are GUE? Answer, now traced and verified: **at
complexification** — and every step is checked.

## The chain (steps 1–2 verified here, 3–4 earlier in the bundle)

```
ℍ  (β=4, GSE — the quaternionic substrate, icosian ring)
  │  STEP 1–2: COMPLEXIFY.  ℍ⊗ℂ = M₂(ℂ);  units → SU(2)        ← the class flip
  ▼
SU(2) / GL₂  (β=2, UNITARY — the ℂ structure)
  │  STEP 3: Jacquet–Langlands (B^× ↔ GL₂), Hecke eigenvalues a_𝔮 preserved
  ▼
GL₂ Hilbert cusp form π,  L(π,s)  (degree 4)
  │  STEP 4: Rudnick–Sarnak universality
  ▼
high zeros of L(π,s)  ~  GUE  (β=2, ℂ)
```

## Verifications
- **Step 1 — ℍ⊗ℂ ≅ M₂(ℂ):** the splitting 1↦I, i↦[[i,0],[0,−i]], j↦[[0,1],[−1,0]],
  k=ij is an algebra isomorphism (i²=j²=k²=−1, ij=k, ji=−k ✓), and the
  quaternion **reduced norm becomes the matrix determinant**:
  `max|nrd(q) − det ρ(q)| = 2e-16` over all 120 units. **Verified.**
  (Local face: the splitting B⊗F₃₁≅M₂(F₃₁) used in `step2_eichler.py` is
  exactly this, mod the prime.)
- **Step 2 — units → SU(2):** the 120 icosian units map to SU(2)
  (`‖ρρ* − I‖ = 2.5e-17`, `|det − 1| = 2e-16`). So **2I ⊂ SU(2)**: the
  quaternionic units sit inside the **unitary** group. The Satake angles
  θ_𝔮 (a_𝔮 = 2√N𝔮·cos θ_𝔮) are SU(2) conjugacy angles — **Sato–Tate is the
  SU(2) measure.** **Verified.**
- **Step 3 — Jacquet–Langlands:** B^× ↔ GL₂, a_𝔮 preserved. **= the circle
  test** (substrate a_𝔮 = genuine newform a_𝔮, 11 primes). Already verified.
- **Step 4 — GUE high zeros:** Rudnick–Sarnak universality. **= the
  quantum-chaos test** (level repulsion, ⟨r⟩≈0.62). Already verified.

## The result
**The ℍ→ℂ class flip happens at complexification** — ℍ⊗ℂ = M₂(ℂ), units →
SU(2) — which is precisely the algebraic content of Jacquet–Langlands
(B and GL₂ are *inner forms*: both become M₂(ℂ) over ℂ). The β=4 (GSE,
degenerate) substrate becomes β=2 (GUE, unitary) **when the quaternions are
complexified into the unitary group**, *not* anywhere in the polytope
geometry. GUE-ness then follows from L-function universality.

## Why this matters for the missing operator
This pins the **home of the missing operator**: it must live on the
**GL₂ / SU(2) (complexified, β=2, unitary) side** — the complexified image —
not on the quaternionic geometric side. Building symmetric ℍ-geometry stays
at β=4; the generator is on the β=2 complexified image. So the search is
**not** "more icosian geometry"; it is "the self-adjoint scaling operator on
the unitary (GL₂/adelic) side," consistent with `THE_ADJOINT.md` and
`SCALE_AND_SYMMETRY.md`.

## Honest status
Steps 1–2 are exact algebra (verified to machine precision); steps 3–4 are
theorems (JL; Rudnick–Sarnak) we confirmed numerically on the substrate's
own data. This **traces** the transition completely and locates the
operator's home — it does **not** construct the operator (Tier-3, open).
