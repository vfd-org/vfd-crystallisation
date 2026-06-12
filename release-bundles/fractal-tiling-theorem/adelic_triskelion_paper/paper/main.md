# The Adelic Triskelion: A Tested Normal Form for the Completed-Zeta Architecture and its Capacity-Positivity Frontier

*Technical note / research-programme consolidation. **This work does not prove the
Riemann Hypothesis.** It identifies and tests a normal form for the completed-zeta
architecture and isolates the remaining RH-equivalent positivity theorem.*

---

## 1. Introduction

A recurring lesson of this programme is **negative and disciplinary**: the Riemann
Hypothesis (RH) is not reachable from a raw prime-gap observable, a naive symmetry
residual, a finite polytope ("simplex") geometry, or a directed-flow intuition. Each was
built, tested against null models, and retired (§3).

The decisive structure is the **completed-zeta object**: finite arithmetic + archimedean
completion + scale involution. We package this as a three-arm *normal form*, the **Adelic
Triskelion**, verify that all three arms are necessary, construct its centre, and reduce
the positivity question to a single operator-norm condition. We then show — honestly —
that the remaining step is an infinite-dimensional theorem equivalent to RH.

Final position:
> **The Adelic Triskelion is the object. Its centre is constructed. The wall is the
> infinite-limit positivity theorem `‖K‖ ≤ 1`, which is RH-equivalent.**

## 2. Background: the completed-zeta architecture (classical)

All of §2 is classical (Riemann 1859; Tate's thesis).

**2.1 Euler product (finite/p-adic places).** `ζ(s)=∏_p (1−p^{−s})^{−1}`, `Re(s)>1`.

**2.2 Archimedean completion (real place).**
`∫₀^∞ e^{−πx²} x^{s−1} dx = ½ π^{−s/2}Γ(s/2)` (substitute `u=πx²`). The Mellin transform
of the Gaussian heat kernel *is* the archimedean local factor.

**2.3 Theta self-duality (scale action).** `θ(t)=Σ_{n∈ℤ} e^{−πn²t}` satisfies the Jacobi
identity `θ(t)=t^{−1/2}θ(1/t)` (Poisson summation). This is the source of the functional
equation.

**2.4 Completed zeta.** `Ξ(s)=π^{−s/2}Γ(s/2)ζ(s)`; `ξ(s)=½s(s−1)Ξ(s)`; functional
equation `ξ(s)=ξ(1−s)`.

> **Crucial caveat (stated up front):** the functional equation gives *symmetry about
> Re(s)=1/2*, not RH. RH is the *positivity/self-adjointness* statement that the zeros lie
> *on* that axis. Symmetry ≠ positivity.

## 3. Failed / retired routes (the discipline)

**3.1 Prime-gap / divisor excess.** `E(n)=(τ(n)/2−1)log n` (0 on primes, >0 on composite
interiors). Real local diagnostic, but the chamber/σ tests were **tautological**: a
symmetric tridiagonal has real eigenvalues for *any* diagonal, and the σ-residual vanishes
at 1/2 for *every* weight (incl. random). It does not beat null models. **Retired as a
direct RH bridge; kept as a divisor-pressure diagnostic.**

**3.2 Naive σ-symmetry.** `R(σ)=|Φ(σ)−Φ(1−σ)|` with `Φ(σ)=Σ w(n)n^{−σ}` vanishes at
σ=1/2 **by construction**, for every weight. A bare Dirichlet series has *no* functional
equation. A non-tautological test must use the **completed** object on complex `s`, `t≠0`
(§4).

**3.3 Simplex / tetrahedral geometry.** A `d`-simplex form gives the **Epstein** zeta of
its lattice (involution `s↔d−s`), not `ζ`. The factor `Γ(s/2)` is the *1-D scaling* Mellin
(dimension-independent — any Gaussian gives it), not a simplex feature; the `ζ` functional
equation needs the self-dual 1-D lattice `ℤ` (det 1), which is **not** a simplex (regular
simplex Grams are not self-dual; det ∈ {3,4,5,…}). **Simplex symbolism is a projection,
not the engine.**

**3.4 Directed flow / one-way orientation.** The scale-flow generator `D=−i d/du` is
self-adjoint, so `U_τ=exp(−iτD)` is **unitary**: `‖U_τ f‖=‖f‖` (verified, ratio
1.000000), and the orientation/arrow functional has *no consistent sign*. A reversible
unitary flow **cannot** create positivity. **Positivity is a capacity/contraction
property, not a flow-orientation property** (§9).

## 4. The completion-kernel test (decisive, non-tautological)

Define the complex-plane functional-equation residual
`R_FE(s)=|Ξ(s)−Ξ(1−s)|/(|Ξ(s)|+|Ξ(1−s)|)`, `Ξ=K·ζ`, over `σ∈[0.1,0.9]×t∈{2,10,30,60}`.
Unlike §3.2, at `t≠0` this does **not** auto-vanish.

| kernel `K` | median `R_FE` | verdict |
|---|---|---|
| raw ζ | 5.6e-01 | FAIL |
| **`π^{−s/2}Γ(s/2)`** | **9e-26** | **PASS** |
| full ξ | ~0 | PASS |
| wrong Γ(s/3) | 4.4e-01 | FAIL |
| wrong π^{−s} | 7.4e-01 | FAIL |
| fake e^{0.7s}Γ(s/2) | 5.9e-01 | FAIL |

**Only the correct archimedean factor passes.** The "missing bridge" of §3 was the
**archimedean completion / place at infinity**, not another finite arithmetic observable.

## 5. Definition of the Adelic Triskelion

`AT = (F, A∞, S; W)`:
- **F** — finite arithmetic / p-adic places / Euler product.
- **A∞** — archimedean real place / Gaussian / Γ factor.
- **S** — multiplicative scale action / involution / theta self-duality.
- **W** — constructed centre / phase-cross / positive-witness form.

It is a **diagrammatic normal form**: three arms circulate around a fixed centre
(`finite → completion → inversion → finite`). It is *not* a finite polytope; it is a
**local–global scale object**. Arm coordinates: `F` = primes; `A∞` = Gaussian/Mellin/Γ;
`S` = `t↔1/t, u=log t ↔ −u, s↔1−s`; centre `W` = `u=0, t=1, Re(s)=1/2`.

## 6. Root-object verification (`RootScore 6/6`)

| arm/test | result |
|---|---|
| **F** Euler product → ζ (Re s>1) | rel-err ~1e-6 |
| **A∞** Gaussian Mellin = ½π^{−s/2}Γ(s/2) | rel-err ~1e-17 |
| **S** theta self-duality | residual ~1e-31 |
| completed Ξ/ξ FE residual | ~1e-21 (PASS); raw ζ + fakes FAIL |
| **necessity** | remove F → no ζ; remove A∞ → raw ζ fails FE; remove S → no involution |

Each arm is **necessary**: this is exactly Riemann/Tate's completed-ζ construction
re-encoded as a tested 3-arm normal form (known mathematics, verified — not new).

## 7. Constructing the centre

`W = Centre(F,A∞,S)`, `Q_W = A∞ + P_F − R_S` (the three arm contributions summed; finite
min eig +0.00004, PSD with a near-null mode). Phase-cross identities: `J f(u)=f(−u)`,
`J²=I`, `D=−i d/du` Hermitian, `JDJ=−D`.

> **Honest caveat:** `JDJ=−D` holds for *any* reflection centre, so it does **not** alone
> pin `u₀=0`. The centre **location** is pinned non-tautologically by the **FE-axis scan**:
> `R(σ₀)=median|Ξ(s)−Ξ(2σ₀−s)|/(…)` vanishes (2e-21) **only at σ₀=1/2** and fails
> (0.08–0.17) at 0.40/0.45/0.55/0.60. The completed object is symmetric about `Re(s)=1/2`
> and no other axis; wrong centres fail.

## 8. Positive-witness scaffold

Finite witness space `H=L²([−U,U])`; `J`, `D` as above. Verified: `J²=I`, `D` Hermitian,
`JDJ=−D`, completed-kernel regression (§6), **Riemann–Weil explicit-formula balance to
residual 3.7e-10**, and the finite **Weil positivity form** PSD with a near-null mode.
Nulls fail (no-archimedean → indefinite, −5.03; fake-Γ → indefinite, −0.11; random
Hermitian → −3.91; shuffled primes → breaks the explicit-formula balance). *Finite
proof-facing scaffold, not a proof.*

## 9. Flow positivity (resolved: NO)

Question: does directed scale-flow generate positivity? **Answer: no.** `U_τ=exp(−iτD)`
is unitary (norm preserved); the arrow test has no consistent sign. The contractive
semigroup `exp(−τH)` (`‖·‖=0.96<1`) is generated by the **PSD capacity `H=A∞+P`**, not by
the scale flow `D` (whose semigroup is unitary). **Positivity = capacity contraction, not
orientation.**

## 10. Capacity-operator formulation (main consolidation)

`H = A∞ + P_F`, `R = R_S`, `Q_W = H − R = H^{1/2}(I−K)H^{1/2}`, `K=H^{−1/2}RH^{−1/2}`
(symmetric; reconstruction residual 4.5e-15). Positivity becomes a **capacity domination /
contraction** condition:

> **RH ⟺ `‖K‖ ≤ 1`** — the capacity-normalised reflection (prime/involution) strength is
> dominated by the archimedean+pole capacity. (This is the Weil/Connes positivity
> criterion in operator form; classical content.)

## 11. Capacity-limit findings — the shape of the wall

Cutoff ladder (basis size NC = 8…24, primes ≤ 2000):

| NC | 8 | 12 | 16 | 20 | 24 |
|---|---|---|---|---|---|
| `‖K_N‖` | 0.99958 | 0.99979 | 0.99981 | 0.99981 | 0.99981 |

- `‖K_N‖ < 1`, **approaching 1 from below**; `1−‖K_N‖` shrinks but
  **basis-resolution-dependently** (best fit `1/NC²`, R²=0.92) — **not a fundamental law**,
  not extrapolable to a proof.
- **Near-null mode is stable** (eigenvector overlaps across cutoffs → 0.99999998), at the
  **low spectral edge** (centre-of-mass 0.21→0.06), **top-mass ≈ 0 — does not escape to the
  boundary**, archimedean-carried.
- **Capacity ratio** `R/(A∞+P) = 0.9998` → reflection ≈ capacity (the marginal condition,
  made literal).
- Nulls fail in discriminating ways: **fake-Γ pushes `‖K‖=1.67 > 1`** (a wrong archimedean
  factor *violates* the contraction); no-archimedean → `H` not PSD.

> **The wall is marginal, gapless, intrinsic, and stable.** There is no finite spectral gap
> to exploit and no boundary artefact to remove. The finite evidence is **consistent with
> RH**, but the contraction becomes tight (`‖K‖→1`) only in the limit — **no finite
> computation decides the theorem.**

## 12. The exact infinite-limit theorem gap

To prove RH through this route one must prove, on the full **infinite adelic witness
space** `H∞`:
1. **Space.** Construct `H∞` (completion of the finite test-function bases / functions on
   the idele class group).
2. **Convergence.** `H_N → H` and `R_N → R` in a spectrum-controlling topology
   (strong-resolvent / Mosco).
3. **Domain.** Control `H^{−1/2}` (densely defined; `H ≻ 0` in the limit).
4. **Boundedness.** `K = H^{−1/2} R H^{−1/2}` exists and is bounded (the near-null margin
   is intrinsic/spread — verified — so no spectral-gap shortcut exists).
5. **No boundary leakage.** `‖K‖` is not lost/exceeded at the adelic boundary / scale ∞.
6. **Universality.** `‖K‖ ≤ 1` for **all** admissible test functions (Weil positivity).

Conditions 1–6 are **necessary and sufficient, hence RH-equivalent**.

*Where the analogous theorem is actually provable:* in the **function-field** case
(curves over `F_q`), the capacity contraction is forced by the Poincaré-duality
**intersection form** (Hodge index), and RH-for-curves is **Weil's theorem** (`|α|=√q`,
verified here for several curves). The **H4→E8** golden-trace-form lattice closure is a
second case where a geometric substrate forces the analogous integrality/positivity
(verified exactly: the 240-root E8 from `shell₁ ∪ (1/φ)shell₁`). The number field **lacks**
such a substrate — supplying it is the **Connes–Consani arithmetic site**, i.e. RH's open
heart.

## 13. What is new and what is classical

**Classical / known:** Euler product; Gaussian/Mellin Γ factor; theta self-duality;
completed-ζ functional equation; **Weil positivity criterion**; Connes-style
capacity/contraction framing; Hilbert–Pólya target; Wilson/Moody–Patera icosian E8;
function-field RH (Weil).

**Contribution of this programme:**
- a **tested Adelic-Triskelion normal form** of the completed-ζ architecture (each arm
  verified *necessary*);
- a sequence of **falsification tests** eliminating prime-gap-only observables, tautological
  σ-probes, simplex geometry, and directed-flow positivity;
- the **constructed centre** `Q_W = A∞ + P_F − R_S`, pinned to `Re(s)=1/2` non-tautologically;
- the **capacity-operator consolidation** `Q_W = H^{1/2}(I−K)H^{1/2}`, positivity ⟺ `‖K‖≤1`;
- a **finite-cutoff characterisation** showing a stable, intrinsic, marginal near-null mode
  and pinpointing the infinite-limit wall with six explicit conditions.

**Not claimed:** no proof of RH; no theorem proving `‖K‖≤1` in the limit; no Hilbert–Pólya
operator with spectrum equal to the zeros; no replacement for Connes/Weil/Tate.

## 14. Claim boundary

> **This work does not prove the Riemann Hypothesis.** It consolidates a tested normal-form
> representation of the completed-zeta architecture and its finite capacity-operator
> positivity scaffold. The remaining unsolved step is proving that the capacity-normalised
> reflection operator `K` exists and satisfies `‖K‖ ≤ 1` in the full infinite adelic witness
> space for all admissible test functions. **That infinite-dimensional theorem is
> RH-equivalent.**

## 15. Conclusion

The Adelic Triskelion is the object the programme identified: a three-arm completed-ζ
normal form with a constructed centre. The finite arm supplies the Euler product, the
archimedean arm the Γ completion, the scale arm the involution. The centre is
`Q_W = A∞ + P_F − R_S`, reformulated as a capacity contraction. Directed flow is **not**
the source of positivity; **capacity is**. Finite-cutoff experiments show a stable,
intrinsic near-null mode and `‖K_N‖→1` from below, with discriminating null failures. The
remaining wall is **theorem-level, not empirical**: prove the limiting capacity-normalised
reflection operator is contractive on the full adelic witness space. That is the
RH-equivalent positivity theorem — the honest frontier.

---

### References (classical)
Riemann (1859); Tate, *Fourier analysis in number fields and Hecke's zeta-functions*
(thesis, 1950); Weil, *Sur les "formules explicites"…* (positivity criterion); Connes,
*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*;
Connes–Consani (arithmetic site); Wilson / Moody–Patera (icosian E8); Berry–Keating
(Hilbert–Pólya scaling). *Programme data:* `data/*.json` (per-WO summaries).
