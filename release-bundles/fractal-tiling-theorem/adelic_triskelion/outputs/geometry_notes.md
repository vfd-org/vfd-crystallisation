# The Adelic Triskelion — geometry notes

A **diagram** of the completed-zeta local–global architecture. **Not a proof of RH.**
It visualises the three layers the prior WOs established as the actual structure of the
completed object, around the fixed witness axis `Re(s)=1/2`.

## Coordinates
Scale coordinate `u = log t`; scale inversion `t ↔ 1/t` is `u ↔ −u`; the fixed scale
`t=1` is `u=0`, identified with the critical line `Re(s)=1/2`. Cylindrical `(r,θ,z)`,
three arms at phases `0, 2π/3, 4π/3` (verified, test T1).

## Arm A — finite p-adic places (Euler product / ζ)
Discrete prime nodes: `r_p = r0 + a·log p`, `θ_p = ω·log p + φ_A`, `z_p = b·log log p`,
node size `= Λ(p) = log p`. Granular and discrete — the finite places. (Only primes
appear: test T3.) *What it encodes:* the arithmetic source `ζ(s)=∏(1−p^{−s})^{−1}`.

## Arm B — archimedean Γ completion (the place at infinity)
Continuous ribbon, intensity `= exp(−π u²)` — the **Gaussian heat kernel** whose Mellin
transform is exactly `½ π^{−s/2}Γ(s/2)`. This is the completion kernel **verified** in
WO-VFD-RH-COMPLETION-KERNEL-001 as the *unique* implementer of `s↔1−s`. Strongest at
the centre `u=0` (test T4). *What it encodes:* the archimedean local factor.

## Arm C — scale action / involution
Ribbon over `u=log t` with `r(u)=r(−u)` (even) and `z(u)=−z(−u)` (odd), so the
`u↔−u` pairing is realised as reflection through the centre (test T2, errors ~1e-16).
Faint chords connect `u` to `−u`. *What it encodes:* the multiplicative scale action and
the functional-equation involution `s↔1−s`, whose **fixed axis is the critical line**.

## Centre — the witness axis
Vertical line `x=y=0`, labelled `Re(s)=1/2` (`u=0`, `t=1`): the fixed point of the
completed scale circulation (test T5). The three arms circulate
`finite arithmetic → archimedean completion → scale inversion → finite arithmetic`
around this still axis.

## Honest status
- This is a **rigorous visual geometry** of the completed local–global architecture, with
  every arm tied to an established fact (Euler product / verified Γ-completion kernel /
  `s↔1−s` involution). It is **not** a proof of RH and asserts nothing new mathematically.
- Per the prior WOs (SIMPLEX, COMPLETION-KERNEL, TRACE-FORM-SEARCH): the completion is the
  **scale/adele action at the place at infinity**, not a finite polytope — which is why
  this is drawn as a *dynamic scale geometry* (helical, inversion-paired), **not** a
  static simplex/tetrahedron. The open piece (a geometric substrate over Spec ℤ forcing
  positivity = the arithmetic site) is what the diagram does **not** supply — that is RH.
