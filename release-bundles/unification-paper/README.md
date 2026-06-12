# Unification paper — Closure under an Invariant Form (LOCAL DRAFT)

**Status: local working draft. Not pushed anywhere. Not yet hostile-reviewed.**

One principle across geometry, arithmetic, and physics: *a structure closes when it is
positive under its proper invariant form `B`*. Three graded instances —
- **Geometry** `H4→E8`: the form delivers closure, **exact (proved)**.
- **Arithmetic** (RH): the witness operator `A=A∞−A_P`, `A≥0 ⟺ RH(L)` — form known,
  positivity = the wall, **open**.
- **Physics** (boundary scattering): shared determinant/flux architecture, **analogy only**.

The unification is the **principle + its instances** (one proved), explicitly **not** a
cross-domain proof. Firewall: no domain implies another; no physical model implies/is
implied by ζ. No RH proof claimed. Grounded in the `vfd_core` trace-form lens
(WO-VFD-INVARIANT-TRACE-FORM-LAW-001).

## Layout
```
papers/closure-under-an-invariant-form.tex/.pdf   the paper
figures/make_figures.py                           regenerates all 5 figures
figures/fig_*.pdf                                  generated figures (E8 + witness use real data)
```

## Reproduce
```bash
cd figures && python3 make_figures.py        # needs numpy, matplotlib; reuses the
                                             # icosian-closure-object cache for the L symbol
cd ../papers && pdflatex closure-under-an-invariant-form.tex   # twice
```

## Figures
- `fig_unification_map` — the principle, three graded instances, the firewall.
- `fig_form_relativity` — the φ anchor: self-adjointness is form-relative (exact).
- `fig_e8_coxeter` — 240 E8 roots in the Coxeter plane (8 rings × 30, verified) — instance G.
- `fig_witness_symbol` — the scale-axis operator symbol + operator↔known-zeros (~1e-7) — instance A.
- `fig_cylinder` — the scale-phase closure object V₁ (interpretation).
