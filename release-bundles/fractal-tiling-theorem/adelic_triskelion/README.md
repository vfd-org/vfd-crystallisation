# WO-VFD-ADELIC-TRISKELION-GEOMETRY-001 — The Adelic Triskelion

A rigorous **visual geometry** (not a proof) of the completed-zeta local–global
architecture: a three-arm helical *scale* geometry around the fixed witness axis
`Re(s)=1/2`.

- **Arm A** — finite p-adic places (prime nodes, Euler product).
- **Arm B** — archimedean Γ completion: Gaussian `exp(−π u²)` ribbon = the heat kernel
  whose Mellin is `π^{−s/2}Γ(s/2)` (the completion kernel verified in COMPLETION-KERNEL-001).
- **Arm C** — scale action / involution: `u=log t`, `u↔−u` ⇔ `t↔1/t` ⇔ `s↔1−s`.
- **Centre** — fixed witness axis `Re(s)=1/2` (`u=0`, `t=1`).

**Why a scale geometry, not a simplex:** SIMPLEX-WITNESS-KERNEL-SEARCH-001 showed the
completion is the scale/adele action at the place at infinity (self-dual 1-D), *not* a
finite polytope. So the Triskelion is drawn as a dynamic, inversion-paired helix, not a
static tetrahedron.

**It does NOT prove RH.** It is the local–global completion architecture made visual; the
open piece (a positivity-forcing geometric substrate over Spec ℤ) is exactly what the
picture does not contain — that is RH.

Run: `python3 src/render.py` → `outputs/adelic_triskelion_{2d,3d}.png` + `_interactive.html`.
Tests: `python3 tests/test_triskelion.py` (threefold 2π/3, scale inversion u↔−u, prime-only
arm, Gaussian profile, axis invariance — all pass). LOCAL, not pushed.
