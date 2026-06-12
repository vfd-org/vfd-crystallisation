# Deliverable D — norm-square factorisation report

Source: `norm_square_factorisation_search.py`,
`results/phase_4_factorisation_kernel/norm_square.json`.

## Theorem Target 1: `Q_Weil[h] = |A h|²`

On a finite basis the Weil Gram `Q` is real symmetric. If `Q ⪰ 0`, Cholesky gives
`Q = AᵀA`, hence `Q[c] = |Ac|²` — the **factorisation exists on that subspace**.

### D1 — cutoff growth (formula side, no zeros)

| basis size | min eigenvalue | PSD | Cholesky `A` exists |
|---|---|---|---|
| 3 | 0.159 | yes | yes |
| 5 | 0.159 | yes | yes |
| 7 | 0.159 | yes | yes |

The factorisation is stable across basis size for this (well-separated) family.

### D2 — the teeth (zero side; the decisive RH-sensitivity)

Build the Weil Gram on a **rich** basis (12 functions, heights 10–45) so the
on-line Gram sits at the PSD edge, then move the first 4 zero-quadruples off the
critical line by `δ`:

| δ (off-line displacement) | min eigenvalue | PSD / `|Ah|²` possible |
|---|---|---|
| 0.0 (on line) | −5e-16 ≈ 0 | **yes** (marginal — the critical edge) |
| 0.1 | −0.0042 | **no** |
| 0.2 | −0.0169 | **no** |
| 0.3 | −0.0386 | **no** |
| 0.4 | −0.0698 | **no** |

So:

```
Q_Weil = |A h|²   ⇔   Gram PSD   ⇔   zeros on Re(s)=1/2   ⇔   RH.
```

The on-line case is **marginally** PSD (the factorisation is *just* possible — the
zeros sit exactly where positivity is tight), and any off-line zero destroys it.

## Structural or artefactual?

**Structural, and RH-equivalent — but zero-side.** The factor `A` here is built
from the zeros (`A_{ρ,a} = ĝ_a(ρ)`). It is not artefactual (it tracks the line
sharply, with teeth), but it is **not constructive**: deriving the *same* `A`
from the prime + archimedean side **without** the zeros is exactly the open
Hilbert–Pólya/Weil problem. We can exhibit `|Ah|²` where RH already lives; we
cannot manufacture `A` from arithmetic alone.

## Verdict

Theorem Target 1 is realised as a faithful, non-circular **diagnostic** of RH
(Test 4 passes at finite level, with teeth), but the universal/constructive
factorisation is not available — it is RH.
