# WO-RH-ARITHMETIC-ADDRESS-LOCK-001 — survey & verdict

**Executed honestly 2026-06-03. This is a survey of KNOWN mathematics against the
WO's six gates, plus the minimal prime-orbit model. It does not produce a new RH
object, and it re-aims the search.**

## The finding that inverts the premise

The WO asks for the "address-lock": primitive orbits = rational primes, length
`log p`, zeta = `ζ(s)`. **That structure is not missing.** It *is* the Euler product:

> minimal prime-orbit model: `Z(s) = ∏_p (1 − e^{−s log p})^{−1} = ∏_p (1−p^{−s})^{−1} = ζ(s)` ✓ (verified, `min_prime_orbit_model.py`)

and it is already realised **operator-theoretically** by the **Bost–Connes system**
(1995): a ℚ-native C*-dynamical system with a self-adjoint Hamiltonian `H` whose
eigenvalues are `{log n}` and whose partition function is `Tr(e^{−βH}) = ζ(β)`.

So **Gates 1–4 (ℚ-native, prime orbits, length `log p`, Euler product = ζ) are MET
by known objects.** The address-lock is locked. What is *not* met is **Gate 6**:
a self-adjoint operator whose **spectrum is the zeros** `{γ_n}` (Bost–Connes' spectrum
is `{log n}`, not the zeros). That is Hilbert–Pólya, and it is the wall.

## Gate table (Deliverable 1)

`✓` met · `~` partial/distributional · `✗` not met. Gates: 1 ℚ-native · 2 orbits=primes ·
3 length `log p` · 4 Euler product=ζ · 5 Weil explicit formula · 6 self-adjoint spectrum=zeros.

| candidate | 1 | 2 | 3 | 4 | 5 | 6 | verdict |
|---|---|---|---|---|---|---|---|
| **{3,3,5,3} honeycomb** | ✗ (ℚ(√5)) | ✗ geodesics | ✗ | ✗ Ihara/Selberg | ✗ | ~ (own spectrum) | mechanism exemplar (our prototype) |
| **Selberg surface** | ✗ | ✗ (geodesics) | ✗ (regulators) | ✗ Selberg ζ | ~ (geom. trace) | ✓ (own Laplacian) | right mechanism, wrong arithmetic |
| **Ihara (finite graph)** | ✗ | ✗ | ✗ | ✗ rational ζ | ✗ | ~ | finite proxy |
| **Bost–Connes** | ✓ | ~ (scale/symmetry) | ✓ (`log n`) | ✓ (`ζ` partition fn) | ~ | ✗ (spec `=log n`) | **address-lock MET, spectrum wrong** |
| **Connes adele class space** | ✓ | ✓ | ✓ | ✓ | ✓ | ~ (zeros as *absorption*; positivity unproven) | **closest; the wall is positivity** |
| **Weil explicit formula** | ✓ | ✓ | ✓ | ✓ | ✓ (defines it) | ✗ (an identity, no operator) | the benchmark every candidate must hit |
| **minimal prime-orbit model** | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ (no operator) | weak pass: structure only |

## The benchmark (Deliverable 3) — Weil explicit formula
The target every candidate must reproduce, term-for-term: prime powers `p^n` with
weights `log p` ⇄ nontrivial zeros `ρ`, plus the archimedean (Γ) term, the pole at
`s=1`, and the trivial zeros. Connes' adele-class trace formula reproduces this
exactly; the open part is the **positivity** of the trace (Weil positivity), which is
equivalent to RH.

## Operator-obstruction report (Deliverable 4)
| | Hilbert space | self-adjoint op | spectrum = zeros | trace = Weil | positivity |
|---|---|---|---|---|---|
| minimal model | ✗ | ✗ | ✗ | ✗ | ✗ |
| Bost–Connes | ✓ | ✓ (`spec=log n`) | ✗ | ✗ | n/a |
| Connes adeles | ✓ | ~ (distributional) | ~ (absorption) | ✓ | **unproven = RH** |

## Verdict (pass/fail)
- **Strong pass (= RH):** none. (A strong pass *is* a proof.)
- **Closest:** Connes' adele class space — reproduces the Weil explicit formula;
  the only missing piece is the positivity of the trace, which is RH itself.
- **Address-lock holders (Gates 1–4):** the Euler product, Bost–Connes. *Already done.*

## Re-aimed target
The honest correction to the WO: **stop searching for the `log p` address-lock — it
exists** (Euler product / Bost–Connes). The unbuilt object is the **spectral** one
(Gate 6): a self-adjoint operator whose spectrum is the zeros, equivalently the
**positivity** of the Connes/Weil trace. That positivity is the wall — the same
"lossless self-adjoint engine" named throughout, now located precisely at **Gate 6**,
in Connes' framework, as Weil positivity. No object here crosses it; crossing it is RH.

Scripts: `min_prime_orbit_model.py`. See also `../RH_OBJECT_TEST.md` (the 8-point test),
`../hyperbolic_600cell_honeycomb/` (the mechanism prototype).
