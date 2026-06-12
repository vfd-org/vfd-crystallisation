# WO-RH-D2-MODULAR-SCATTERING-POSITIVITY-001 — results

**Executed 2026-06-03.** Stop climbing the lattice ladder; test the **d=2 arithmetic
scattering boundary** H²/SL(2,ℤ) where ζ already lives, then locate the positivity wall.

All claims are gated or stamped. Honest one-line verdict up front:

> **STRONG PASS on the scattering channel; the positivity wall is confirmed, not crossed.**
> The d=2 modular surface is the correct arithmetic testbed: ζ sits inside its
> scattering coefficient φ(s)=ξ(2s−1)/ξ(2s), and **the Riemann zeros are exactly its
> scattering resonances** (poles at s=¼+iγ/2). The Weil explicit formula is reproduced
> to machine precision and the completed positivity form is PSD — but full positivity
> for all test functions remains **RH = the wall**, unchanged.

## What was found (per workstream)

| WS | result | scope |
|---|---|---|
| **A** dimension-line audit | line = (d−1)/2 → Riemann needs **d=2**; H⁴=1.5, H⁹=4.0 are the wrong lines. Climbing E8→E10→E12 moves *away* from 1/2. | [VERIFIED] |
| **B** scattering harness | φ(s)=ξ(2s−1)/ξ(2s) built; φ(s)φ(1−s)=1 to 1e-32; **\|φ(½+it)\|=1 exactly** (unitary on the line); pole at s=1 (constant eigenfunction). ζ is manifestly inside φ. | [VERIFIED] |
| **C** resonances / phase | **\|φ\| spikes to ~10⁶–10⁷ exactly at s=¼+iγₙ/2** and drops to ~1–2 between → **the Riemann zeros are the modular scattering resonances**. Phase θ(t)=arg φ(½+it)=−2 arg ξ(1+2it) tracks ζ's argument (continuous-spectrum phase). | [VERIFIED] resonance localization; [INTERPRETIVE-bounded] phase↔count |
| **E/F** positivity | explicit formula gated to **9e-16**; completed Weil form PSD and equal to the zero side; **prime-only strongly indefinite (min eig −34.6)** → completion (pole+archimedean) is required to reach positivity. | [VERIFIED] gate; [NULL/OPEN] positivity = wall |
| **D** absorption vs emission | the zeros enter as **poles (resonances/absorption)**, not emitted eigenvalues — consistent with the Connes "absorption" picture (zeros = spectral *gaps*, not sources). | [INTERPRETIVE-bounded] |
| **G** Connes bridge | H²/SL(2,ℤ) → φ contains ζ → Weil explicit formula → **Connes adele-class space** (its adelic completion); the open piece is **Weil positivity = RH**. | [VERIFIED map]; [OPEN] |

## The decisive new fact

The Riemann zeros are **not** the Laplace (Maass) eigenvalues of the modular surface
and they are **not** on the modular critical line Re(s)=½. They are the **scattering
resonances** — poles of φ at **s = ¼ + iγ/2** (under RH). RH ⟺ these resonances sit
exactly on Re(s)=¼ ⟺ ρ on Re=½. So the d=2 surface genuinely *contains* the Riemann
zeros, as resonances of a unitary scattering channel — and proving they sit on that
line is exactly Weil positivity.

## What this does NOT claim (per the WO §14)

Not claimed: the modular surface proves RH; φ proves zeros on the line; Connes proves
RH; phase correlation proves positivity; baby-RH implies Riemann RH. **Honest claim:**
the d=2 modular scattering channel is the correct classical arithmetic testbed, ζ lives
in it as resonances, and **positivity remains the wall**.

## Files
```
src/modular_scattering.py   WS-A/B/C: phi(s), unitarity, resonances=zeros, phase
src/d2_positivity.py        WS-A/E/F: dimension audit + gated explicit-formula Weil form
reports/                    DIMENSION_LINE_AUDIT, MODULAR_SCATTERING_REPORT,
                            SCATTERING_PHASE_ZERO_COUNT, D2_WEIL_POSITIVITY_OBSTRUCTION,
                            ABSORPTION_VS_EMISSION_TRACE_TEST, D2_TO_CONNES_BRIDGE
```

## Relation to prior work
This reaches the **same wall** as the route_b operator program (Connes/Weil positivity,
validated there on ζ to 0.01%, knife-edge marginal). The new content is the **explicit
d=2 scattering realization**: the zeros as resonances of φ(s) on the modular surface,
the shortest classical-arithmetic road to that wall. See
`../RH_DIMENSION_AND_COSMOLOGY_SYNTHESIS.md` and `../RH_FRONTIER.md`. LOCAL, not pushed.
