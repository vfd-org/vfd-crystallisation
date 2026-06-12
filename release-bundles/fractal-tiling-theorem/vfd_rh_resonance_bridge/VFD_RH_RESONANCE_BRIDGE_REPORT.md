# WO-RH-VFD-RESONANCE-BRIDGE-001 — Report

**Constructing the VFD closure/leakage bridge for RH.**
Status: research / proof-architecture. **No RH proof is claimed.**

## Question

> Does VFD supply a genuinely new closure/leakage bridge object for RH, or is it
> currently only a powerful interpretation?

## Answer (one line)

VFD supplies **one** non-circular candidate bridge object — the Weil functional
with a parameter-free geometric prime side and a finite self-adjoint Hecke
operator — which is the **classical** Weil/Hilbert–Pólya criterion; the naive
resonance and leakage functionals are decorative or circular. **Grade 2.**

## Deliverables and findings

- **A — Translation table** (`translation_table.md`). Every VFD term maps to a
  standard object; three identifications are non-trivial (closure energy = Weil
  functional; resonance operator = self-adjoint Brandt operator; emitters =
  explicit formula).
- **B — Prime resonance field** (`prime_resonance_field.py`).
  - B1 naive field `P_X(σ,t)`: **not a usable diagnostic** (weak `|z|<2` and
    circular — `P_X` is the leading term of `log ζ`).
  - B2 prime fluctuation `(ψ(x)−x)/√x`: spectral peaks **at the zeros**, 8/8
    matched to `<0.2` (`results/plots/prime_fluctuation_spectrum.png`). Real,
    non-circular, but it **is** the explicit formula — no simplification of RH.
- **C — Leakage functionals** (`leakage_functionals.py`). All three killed
  honestly: `L1/L2` symmetric-by-construction (decorative); `L3=ξ(s)−ξ(1−s)`
  identically zero (`≤1e−27` everywhere, detects nothing).
- **D — Closure forms** (`closure_form_candidates.py`).
  - D1 `Q(x)=Tr(nrd x)=|Ax|²`: a real positive form (Gram det 625) — but
    coefficient-side, blind to the zeros.
  - D3 self-adjoint defect: `R−R^*=0` **exactly in the mass measure** (4 in the
    naive basis) — self-adjoint "only on the right boundary"; coefficient-side.
  - D2 `Q(h)=W(h)=ARCH−PRIME`: the **only** candidate that encodes completion +
    mirror + zeros; `Q≥0 ∀h ⟺ RH`. RH-equivalent (the wall).
- **E — Resonator + theorem targets** (`THEOREM_TARGETS.md`). The canonical
  `(H,R,Θ,∂,Q)` is defined; `R` is genuinely self-adjoint with spectrum `a_P`;
  the three theorem templates (T1 Weil, T2 Hilbert–Pólya, T3 leakage) are stated
  with what each needs and why each is open.
- **F — Comparison** (below).
- **Validation tests 1–6** (`experiments_known_zeros.py`): only D2 passes all
  five structural tests; test 6 (spectrum) is the strong non-circular sanity.

## F — Comparison against existing RH programmes

| programme | what it solves | where it sticks | what VFD adds | merely relabelling? |
|---|---|---|---|---|
| **Hilbert–Pólya** | reduces RH to "find self-adjoint `H` with spectrum `γ_n`" | no canonical `H` for the zeros | a **finite** self-adjoint `R` with the correct **Hecke** spectrum, built parameter-free from geometry | no — but `R` is for the Hecke spectrum, not the zeros (β-class gap) |
| **Weil positivity** | RH ⟺ `W(h)≥0 ∀h` | proving the positivity | a **parameter-free geometric prime side** for `W(h)`, ζ-calibrated to `1e−6` | partly — the criterion is classical; the geometric instantiation is new |
| **Connes trace / absorption** | spectral realisation; critical zeros = absorption spectrum | needs the same positivity / the adelic operator | the icosian/Brandt arena is an explicit class-number-1 instance of the quaternionic side | no, but it does not cross Connes' wall |
| **Quantum chaos / trace formula** | zero statistics = GUE (β=2) | not a proof; a statistical law | identifies the substrate class as β=4 (GSE) and the gap to β=2 explicitly | no — clarifies the obstruction |
| **de Branges** | positivity in Hilbert spaces of entire functions | structural positivity unproved | nothing decisive here | n/a |

**Net:** VFD does not produce a new reduction; it produces a *parameter-free,
geometric instantiation* of the Weil/Hilbert–Pólya object, plus a sharp
statement of the obstruction (β=4 vs β=2). That is genuine, and it is Grade 2.

## The wall, precisely

`Q[f]=|A_∞ f|²` with a geometric `A_∞` would be the proof — and writing that
square **is** the proof. We can write `A` for the finite coefficient-side forms
(D1, D3); we cannot derive `A_∞` for the zero-side form (D2/Weil). The
obstruction is concrete: the self-adjoint operator we have lives on the β=4
(GSE) Hecke side; the zeta zeros are β=2 (GUE); the archimedean/adelic completion
across that class boundary is open (`ADELIC_SCALING.md`, Tier-3).

## Reproduce

```bash
python3 prime_resonance_field.py      # B: naive field (decorative) + spectrum (real)
python3 leakage_functionals.py        # C: L1/L2/L3 all killed honestly
python3 closure_form_candidates.py    # D: D1/D2/D3 (needs sibling icosian bundle)
python3 experiments_known_zeros.py    # validation tests 1-6 + spectrum plot
```

Outputs in `results/tables/*.json` and `results/plots/`.

## Claim boundary

See `CLAIM_BOUNDARY.md`. Grade 2; `rh_claim: NO_RH_PROOF_CLAIMED`. The success
criterion the WO set — *"a non-circular candidate closure form that can be
tested against Weil positivity / Hilbert–Pólya / trace-form structures"* — is
met by D2, with the honest caveat that it is the classical criterion in
parameter-free geometric dress, not a new route through the wall.
