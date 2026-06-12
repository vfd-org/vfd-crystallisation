# WS-D — Absorption versus emission

**Question.** Are the zeros *emitted* spectral modes (eigenvalues of a self-adjoint
operator, `+Σ h(γ)`) or *absorbed* modes (Connes' "spectral realization as absorption",
`−Σ h(γ)`)?

## What the scattering picture settles (no new sim needed — it follows from WS-B/C)

The zeros enter φ(s) as **poles** (resonances at s=ρ/2), **not** as the Laplace
eigenvalues of the modular surface. In scattering language a pole of the
scattering matrix on the *unphysical* side is a **resonance / decaying mode**, not a
bound state. This is exactly Connes' framing: the zeros appear as an **absorption
spectrum** in the continuous Eisenstein channel — the places where the unitary
scattering "swallows" a mode — rather than as emitted point eigenvalues. The
modular surface's *emitted* discrete spectrum is the **Maass cusp forms** (a different,
genuinely self-adjoint set); the **Riemann zeros are the absorption/resonance set.**

## Consequences for the three questions in the WO

1. **Sign convention.** The absorption convention (`−Σ`, zeros as missing modes)
   matches Connes' adele-class-space realization, where the zeros are where the
   continuous spectrum is *removed*, not added.
2. **Why zeros aren't normal emitted eigenmodes.** Because they are resonances of a
   *continuous* (Eisenstein) channel, not eigenvalues of the *discrete* (cuspidal)
   one. A naive "build a self-adjoint operator with the zeros as eigenvalues" looks
   for them in the wrong spectrum.
3. **A spectral hole, not a source.** This vindicates the "structure in the gaps"
   intuition in a precise, non-mystical way: the missing object is the operator whose
   **absorption** spectrum is the resonance set — Connes' arithmetic site — and the
   open step is the **positivity** of its trace.

## Scope

[INTERPRETIVE-bounded but grounded]: the absorption-vs-emission distinction is a
*correct structural reading* of the resonance computation (WS-C), and it aligns with
Connes' published framework. It does **not** by itself change the positivity verdict —
absorption sign-convention does not make the form provably PSD for all test functions.
The wall is unchanged.
