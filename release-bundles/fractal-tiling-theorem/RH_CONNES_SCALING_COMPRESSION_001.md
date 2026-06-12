# WO-RH-CONNES-SCALING-COMPRESSION-001 — Probe C (report)

**Status:** run; **succeeded.** Sim: `route_b/rh_connes_scaling_compression.py`.
**No proof of RH; no φ; the operator's *global* positivity is RH.**

## 1. Summary
The validated Weil positive form (Probe B) is realised as the quadratic form of
an explicit **Connes-style scaling operator** on `L²(ℝ₊*, d*x)`, built
**non-circularly** from primes + archimedean data (no zeros). Its compression to
finite cutoffs is **PSD** and the archimedean term carries that positivity; this
identifies the *operator-theoretic mechanism* that produces the positive space.
The min eigenvalue **shrinks toward 0** as the cutoff grows — marginal, knife-edge
positivity, consistent with RH being the critical case.

## 2. The operator
```
D = M_arch  +  pole  −  Σ_n Λ(n)/√n · (T_{log n} + T_{−log n})
```
- `T_a` = the **scaling action** (translation by a = log n in the log-coordinate
  on ℝ₊*) — so the prime side is literally a sum of scaling translations;
- `M_arch` = multiplication by `Re ψ(¼ + ir/2) − log π` in the dilation
  (Mellin/Fourier) spectral variable r — a **function of the self-adjoint
  dilation generator** (the archimedean place);
- `pole` = the s=1 term.
`⟨φ_i, D φ_j⟩` = the Weil form `Q_ij` of Probe B. **No zeros enter D.**

## 3. Results
- **Validation:** D-form vs 2×zero-Gram, relerr **0.0016** (tail of 400 zeros).
- **Compression sweep** (min eigenvalue vs cutoff N):

| cutoff N | complete D | no archimedean |
|---|---|---|
| 2 | +0.5106 (PSD) | −3.39 (not PSD) |
| 3 | +0.0916 (PSD) | −4.05 |
| 4 | +0.0131 (PSD) | −4.30 |
| 5 | +0.0020 (PSD) | −4.60 |
| 6 | +0.0007 (PSD) | −4.69 |

- complete D **PSD at every cutoff**; archimedean term **carries** the positivity
  (dropping it → indefinite at every cutoff);
- min eig **decreasing toward 0** → **marginal / near-critical** positivity.

## 4. Interpretation
The operator-theoretic *mechanism* is identified: **prime side = scaling action;
archimedean side = a function of the dilation generator; their difference is the
positive defect D** — exactly Connes' object, built here non-circularly and shown
to carry the validated Weil positivity. (WO success criteria 1–5 at the
form/compression level.)

## 5. The marginal-positivity nuance (honest)
The shrinking min eigenvalue (0.51 → 0.0007) says the positive form sits **at the
edge** of PSD, not robustly inside it. This is the numerical signature of the
**knife-edge**: RH is precisely the statement that this near-critical positivity
**holds in the limit / for all test functions**. The finite cutoffs are PSD
*because* the actual zeros are on the line; the limit being PSD is RH.

## 6. What this does NOT prove
- Not RH. Finite-cutoff PSD **reflects** zeros-on-line; **D ≥ 0 in the full
  compression limit = Weil positivity = RH** (open). The shrinking min eig shows
  the limit is delicate, not safely bounded away from 0.
- Classical content (Connes/Weil), realised and validated numerically; not new
  mathematics; no operator *proven* positive in the limit.

## 7. Net / next
The operator route now has its mechanism: **a non-circular Connes scaling
operator D whose quadratic form is the validated positive Weil form, PSD on every
finite cutoff (marginally), with the archimedean term as the carrier.** The
single remaining, genuinely open step is **prove D ≥ 0 in the limit** (= RH).
Independent cross-check available: **Probe A** (de Branges reproducing kernel from
a Hermite–Biehler E built from ξ) — a second realisation of the same positive
form. Beyond that lies the actual de Branges/Connes proof problem, untouched.
