# WO-RH-ARCH-U-001 — Prime-Built Archimedean Boundary Operator (report)

**Status:** run; honest partial result. **Sim:** `route_b/rh_arch_u_operator.py`.
**No proof of RH; no Hilbert–Pólya operator constructed; φ not required.**

## 1. Summary
Attempted the first *non-circular* path toward the Cayley boundary shift `U`:
build the completed Li/boundary-moment data from **primes + archimedean Γ**
(no zeros), check positive boundary structure, validate against zeros only at
the end. The outcome is the WO's own predicted "most likely" one: the
construction **sharpens the wall, it does not cross it.**

## 2. Anti-circularity statement
No zero heights, Cayley phases, `z_ρ`, zero-derived Li coefficients, or zero
tables entered the construction path. The only place real zeros appear is the
explicit off-boundary diagnostic (synthetic) and the validation note. **One
honest caveat:** any *tractable* "completed" value uses ζ's analytic
continuation (`mpmath`), which is *more* than pure prime-side terms — flagged,
not hidden.

## 3. Recap (Cayley boundary, WO-RH-CAYLEY-OPERATOR-001)
`z = 1 − 1/ρ` sends the critical line to `|z|=1`; on-line zeros → PSD Toeplitz
moment matrix + unitary shift; off-line → negative eigenvalue + non-unitary
shift. Doorway: zeros on `|z|=1` ⟺ `U` unitary ⟺ `H = −i log U` self-adjoint.
Building the moments *from the zeros* is circular; this WO sought the prime
side.

## 4. Why the archimedean Γ completion is mandatory — confirmed cleanly
The completed boundary moments are the **Keiper–Li / Bombieri–Lagarias**
coefficients `λ_n`, which live at **s = 1**. The prime-only Euler product
`Σ_p −log(1−p^{−s})` **diverges like `−log(s−1)`** as `s→1` — exactly the point
where `λ_n` is defined. Therefore **primes alone cannot produce the boundary
moments; the archimedean continuation/Γ-factor is *structurally* mandatory**,
not merely helpful. This is "Advance 4", confirmed non-circularly, and it
agrees with WO-RH-COMPTRACE-001.

## 5–7. What was achieved / controls
- **`λ_1` reproduced** from `ξ = π^{−s/2}Γ(s/2)ζ(s)·s(s−1)/2` to `9×10⁻⁹`
  (method correct at n=1).
- **prime-only control fails structurally** (Euler product diverges at s=1).
- **off-boundary diagnostic** reproduces leakage: `Σ(log|z|)²` is 0 on the
  boundary and grows with the off-line offset δ (matches CAYLEY-001).

## 8–9. Shift / validation
Not reached: no stable completed moment sequence to high n ⇒ no candidate `U`
to test for unitarity, and hence no spectral-phase validation against the
known Cayley zero phases.

## 10. Off-boundary leakage
Confirmed (above): the diagnostics detect radial leakage as designed.

## 11. Interpretation
The arithmetic boundary-moment data is, by construction, the Li-coefficient
sequence; it is positive (for the true ζ) and its positivity *is* RH. The WO
confirms the **necessity** of the archimedean term and the **circularity
barrier** of any zero-fed construction, but produces no operator.

## 12. Failure modes (honest)
1. **Numerical:** `mp.diff` on `log ξ` is unstable for `n≥2` (differentiation
   through the ζ-pole region) — fragile values **not reported**.
2. **Structural / circularity:** a tractable "completed" `λ_n` uses ζ's
   continuation; a genuinely pure prime+Γ build is the Bombieri–Lagarias /
   Stieltjes-constant research task, not a quick sim.
3. **Truncation:** at fixed prime cutoff the Euler-product partial sum plateaus
   rather than visibly diverging; the divergence is in the *true* `−log(s−1)`.

## 13. Next work order
**WO-RH-ARCH-MOMENT-VARIANTS-002** — pin the *canonical* explicit-formula →
boundary-moment map using the Stieltjes constants `γ_k` (computable
independently, non-circularly via `mp.stieltjes`), giving a *stable* prime+Γ
`λ_n` to high n. Only with that in hand is a candidate `U` and its
unitarity/validation meaningful. A φ role remains unsupported and parked.

## Net
The WO did its job: it **localised the operator wall with new precision** —
primes diverge at the Keiper–Li point, so the archimedean completion is
mandatory; a non-circular high-n moment construction is the exact open task —
without overclaiming. No proof, no operator, no φ. Honest partial result.
