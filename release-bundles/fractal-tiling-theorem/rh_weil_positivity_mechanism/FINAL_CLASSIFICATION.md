# Final classification

```
GRADE 2 — CANDIDATE BRIDGE OBJECT (canonical H−R capacity decomposition),
          REDUCES TO WEIL POSITIVITY.
rh_claim: NO_RH_PROOF_CLAIMED
```

## Answer to the WO's boxed question

> Can VFD geometry expose a non-circular positivity mechanism behind Weil
> positivity?

**It exposes the *structure* of the mechanism, not a new mechanism.** Concretely,
the Weil functional factors canonically as

```
Q_Weil = H − R,   H = archimedean capacity (POSITIVE kernel),   R = prime load (INDEFINITE),
```

so positivity is "capacity dominates load", and RH `⇔` `H ⪰ R ∀h`. The
positivity lives in the archimedean completion; the prime side alone is never
positive. This is a faithful, non-circular, completion-aware account — but it is
the classical Weil structure, and proving the universal dominance is RH.

## Which WO success was achieved

- **Success A (honest negative):** no *new* positivity mechanism — VFD closure
  language is a re-description of Weil positivity. ✓
- **Success B (diagnostic factorisation):** `Q=|Ah|²` exists on PSD bases, with
  **off-line teeth** (PSD lost iff a zero leaves the line) — a genuine RH-sensitive
  finite diagnostic. ✓
- **Success C (candidate bridge object):** the canonical `H−R` decomposition with
  positive archimedean kernel is non-circular, completion-aware, explicit-formula-
  linked, positive on tested spaces. ✓ → **Grade 2**.
- **Success D (proof-equivalent reduction):** the whole thing reduces to Weil
  positivity. ✓ (classical, not VFD-novel — hence Grade 2, not Grade 3.)

Not achieved: Success E (proof). No universal positivity.

## Theorem-target scorecard

| target | status |
|---|---|
| T1 `Q=|Ah|²` | realised zero-side with teeth; constructive prime-side `A` open |
| T2 `Q=H−R`, `H⪰R` | `H` positive & `R` indefinite verified; universal `H⪰R` = RH |
| T3 positive kernel `K` | `K` = Weil kernel; `K⪰0` = RH; not new |
| T4 self-adjoint `K` | finite self-adjoint `K` built; canonical zero-spectrum operator open |

## Validation tests

| test | result |
|---|---|
| 1 RH-circularity | PASS (no zeros in any construction) |
| 2 completion | PASS (archimedean kept; prime-only fails) |
| 3 universal quantifier | tracked; only finite/tested positivity (diagnostic) |
| 4 norm-square | PASS finite, with teeth; universal = RH |
| 5 kernel positivity | `K_arch` PSD, `K_prime` indefinite; total at edge |
| 6 boundary-capacity | explanatory (localises positivity in archimedean block) |
| 7 existing-math reduction | reduces to Weil positivity (stated) |

## One-line standing

The Weil wall is now **anatomised** — positivity localised in the archimedean
capacity, threatened by the indefinite prime load, with a teeth-bearing
norm-square diagnostic — but it is not crossed: universal `H ⪰ R` is RH, and the
canonical zero-spectrum operator remains the open archimedean–adelic
Hilbert–Pólya object.
