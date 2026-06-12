# The Cuspidal–Eisenstein Bridge Conjecture (O2), stated falsifiably

**Status:** TESTED 2026-06-06 — **REFUTED (negative), as predicted.** See §7.

**Status (original):** OPEN conjecture, drafted 2026-06-06. Honest prior: **expected to be FALSE.**
A clean refutation is the intended deliverable — it closes (O2) in the negative and
costs no credibility. This document states the conjecture precisely, gives a
falsifiable out-of-sample test, and builds in safeguards against the hardcoding
that was caught in prior substrate→Hecke attempts.

---

## 0. Why this is the only live target

This session established, by construction:
- Every *geometric restatement* of RH reaches the same positivity wall (the
  prime↔zero loop is self-referential; restating it cannot close it).
- The VFD closure selector is a **finite self-adjoint** operator. It failed four
  structural tests against ζ's selector (discrete vs continuous spectrum; no pole
  vs pole at s=1; no Euler product vs Euler product; rigid spacing vs GUE). So as
  a finite object it **cannot** be ζ's selector.
- The verified icosian result is `L(Θ_𝓘, s) = ζ_K(s)·ζ_K(s−1)` over `K = ℚ(√5)`
  — the **cuspidal/Hilbert side**, NOT the Riemann ζ.

So the one precise, falsifiable question left is: **does the closure selector reach
the *Riemann* ζ (the Eisenstein/ℚ side), or only the ℚ(√5) cuspidal side it is
already known to reach?**

---

## 1. Objects (all defined before any zeros are looked at)

- `K = ℚ(√5)`, `φ = (1+√5)/2`, ring of integers `ℤ[φ]`.
- `𝓘` = icosian ring; `V_600` = the 120 unit icosians = vertices of the 600-cell.
- `C_φ = L_M + φ^{−2} I` = the closure (Green) kernel on `V_600`
  (`L_M` = the V_600 graph Laplacian/adjacency; see `aria-closure-kernel`).
- `Θ_𝓘(τ)` = the icosian theta series; `L(Θ_𝓘,s) = ζ_K(s)·ζ_K(s−1)` (verified).
- `ζ(s)` = Riemann zeta, nontrivial zeros `{γ_n}` (ordinates).
- `ζ_K(s)` = Dedekind zeta of `K`, with its own zeros `{β_m}`.

**Established (the cuspidal anchor):** the selector's arithmetic data encodes `ζ_K`,
not `ζ`. This is the proven side and the control.

---

## 2. The conjecture

> **(O2-Bridge).** There exists an explicit, parameter-free map
> `Φ : spec(C_φ-derived data) ⟶ ℝ`, defined without reference to the Riemann
> zeros, whose image reproduces the ordinates `{γ_n}` of the **Riemann** ζ zeros
> (the Eisenstein/ℚ component), not merely the `ζ_K` zeros `{β_m}` over `ℚ(√5)`.

Two graded forms:
- **C-strong:** `Φ(data)` matches `γ_1, γ_2, …` pointwise (out-of-sample) to
  tolerance.
- **C-weak:** `Φ(data)` reproduces the *statistics* of `{γ_n}` (GUE spacing,
  Riemann density `~ (T/2π)log(T/2π)`) distinguishably from the `ζ_K` statistics.

---

## 3. The falsifiable test (protocol)

1. **Freeze `Φ` first.** Write `Φ` down completely — every constant traced to
   `φ`, `V_600`, or `C_φ` — *before* loading any Riemann zero. Commit it (hash it).
2. **Compute the prediction** `S = Φ(C_φ data)`. No Riemann zeros are inputs.
3. **Out-of-sample comparison.** Split: if `Φ` uses any primes/data up to `X`,
   test its output against Riemann zeros/data strictly **beyond** `X`
   (mirror the 13/13 out-of-sample discipline of the icosian work).
4. **Three discriminating metrics** (each separates ζ from ζ_K):
   - **Pointwise:** `|S_k − γ_k|` for the first `k` — PASS if small without fitting.
   - **Pole:** does `S` carry a pole at `s=1` (Riemann) — finite operators do not.
   - **Spacing fingerprint:** fraction of normalized gaps `< 0.3` — Riemann ≈ 0
     (GUE repulsion); a rigid/finite spectrum ≈ 0.4+. Must match Riemann, not ζ_K.

**PASS** = predicts the Riemann zeros out-of-sample, parameter-free, with the
Riemann pole + GUE fingerprint. **FAIL** = predicts the `ζ_K` zeros, or nothing,
or only after fitting.

---

## 4. No-hardcoding safeguards (mandatory)

The prior attempts failed here; these are non-negotiable:
- **No zeros as inputs.** `Φ` may not contain `{γ_n}` in any form (the `diag` /
  `hecke_lift` trap). If removing the zeros from `Φ` collapses the result, it was
  hardcoded.
- **Provenance audit.** Every constant in `Φ` traced to geometry, not fit by
  least-squares to the zeros (cf. the W5 provenance audit that caught the fitted map).
- **Pre-registration.** `Φ` and the tolerance are fixed before the out-of-sample
  data is seen.
- **Control run.** `Φ` *must* still reproduce the `ζ_K` zeros (the known cuspidal
  anchor). If it can't even hit the proven side, the construction is broken.

---

## 5. Expected outcome and what each means

- **FAIL (expected):** `Φ` reproduces `ζ_K` (ℚ(√5)) but not Riemann ζ, or needs
  fitting. ⟹ the selector reaches only the cuspidal side; **(O2) closed negative.**
  This is a real, honest, publishable result — it sharpens the de-merge into a
  theorem-shaped statement: *finite geometric closure data encodes `ζ_K`, not `ζ`.*
- **PASS (unlikely, extraordinary):** parameter-free out-of-sample match to Riemann
  zeros with pole + GUE. ⟹ a genuine bridge; would require independent replication
  before any claim. Treat with maximum skepticism; assume hardcoding until proven.

---

## 6. Credibility bar

State it as a conjecture **and its likely refutation**, never as a discovery.
The deliverable is the *test and its honest outcome*. Frame: "We test whether the
closure selector reaches Riemann ζ; it does not, and here is the structural reason"
— that is undismissable. "We bridged geometry to RH" — fails at the abstract.

---

---

## 7. RESULT (run 2026-06-06, `run_bridge_test.py`)

`Φ` constructed from the verified `L(Θ_𝓘,s)=ζ_K(s)ζ_K(s−1)` plus the Dedekind
factorization `ζ_K(s)=ζ(s)·L(s,χ_5)` (χ_5 = real character mod 5). **No Riemann
zeros inserted** — they enter only as the ζ-factor of ζ_K.

- **Control — PASS:** Φ reproduces the ζ_K zeros (proven cuspidal anchor).
- **Metric 1 (pointwise) — FAIL:** prediction `6.65, 9.83, 11.96, 14.13, …` vs
  Riemann `14.13, 21.02, 25.01, …`. The L(χ_5) zeros are interleaved; Φ outputs
  `ζ ∪ L(χ_5)`, not ζ alone.
- **Metric 2 (pole) — hollow pass:** ζ_K has the s=1 pole, but it merely *contains*
  ζ's; no independent control.
- **Metric 3 (spacing) — FAIL (decisive):** fraction of normalized gaps < 0.3 is
  **0.000** for pure Riemann (GUE repulsion) vs **0.085** for Φ=ζ_K (two GUE
  spectra superposed → repulsion washed out). Φ's output is provably not pure-Riemann.

**Verdict: (O2) closed NEGATIVE.** The VFD selector encodes `ζ_K`, which contains
the Riemann ζ only as a *factor*, contaminated by L(χ_5). It gives **no independent
grip** on the Riemann zeros — not pointwise, not statistically. The positivity wall
(RH) is untouched: RH for ζ_K already *contains* RH for ζ.

This is the theorem-shaped negative the conjecture was designed to extract:
*finite VFD closure data encodes ζ_K = ζ·L(χ_5), which swallows ζ rather than
isolating it; the cuspidal→Eisenstein bridge does not exist in the strong sense.*
Honest, run, not asserted.

## 8. REFINEMENT — the 24-cell isolates ζ (POSITIVE, but capped)

Diagnosis (`twin_mirror.py`): there are **two mirror systems** and they differ —
H4/kaleidoscope reflections preserve V_600 (120/120); the **Galois mirror
√5→−√5** fixes the 24-cell (24, no √5) and sends the φ-shell to the **96-vertex
twin** (the source of the L(χ_5) contamination). Their *agreement locus* is the
**24-cell**.

Test (`test_24cell_isolates_zeta.py`): the 24-cell is the **K=ℚ** analog of the
icosian K=ℚ(√5) construction → L-function `ζ(s)·ζ(s−1)` (no √5 ⟹ no L(χ_5)).
Since `ζ(s−1)` zeros sit at Re=3/2 (off the line), the **critical-line content is
pure Riemann**. Spacing fingerprint (gaps<0.3): 24-cell = **0.000** (= pure
Riemann) vs 600-cell ζ_K = **0.089** (contaminated). **The 24-cell isolates ζ.**

Complete (O2) map: **ζ ← 24-cell** (ℚ, Galois-trivial) · **L(χ_5) ← 96-twin**
(φ-shell, Galois-sign) · **ζ_K ← 600-cell** (product).

**Caps (mandatory, so this is not over-read):**
- (a) Does **not** touch RH — isolating ζ ≠ proving its zeros on the line; the
  ζ(s)-factor positivity is the same wall.
- (b) Partly **tautological** — the rational sub-polytope carries the rational ζ.
- (c) ζ on the 24-cell is an **Eisenstein** L-function (analytic continuation),
  NOT a finite operator's eigenvalues; so finite self-adjointness (free positivity)
  does not transfer.

**Net (O2):** strong bridge — NEGATIVE; refined 24-cell localization —
POSITIVE-but-capped. The geometric-localization program is complete; the RH
positivity wall is intact.

---

*This is a map and a falsifiable probe, not a proof and not a claim of one. The
positivity wall (RH itself) is untouched by this document; (O2) is a separate,
testable question about which L-function the VFD selector encodes — now answered
in the negative.*
