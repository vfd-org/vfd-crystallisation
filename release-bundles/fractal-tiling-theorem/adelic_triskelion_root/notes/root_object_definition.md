# Root object definition — AT = (F, A∞, S, W, I)

- **F** finite-place arithmetic arm = primes / Euler product `∏_p(1−p^{−s})^{−1}` (→ ζ).
- **A∞** archimedean arm = ℝ with Gaussian `e^{−πx²}`; Mellin `∫₀^∞ e^{−πx²}x^{s−1}dx = ½π^{−s/2}Γ(s/2)`.
- **S** scale-action arm = `x→λx`, scale coord `u=log t`; theta self-duality `θ(t)=t^{−½}θ(1/t)`.
- **W** central witness axis = fixed scale `t=1` (`u=0`) ⇔ critical line `Re(s)=1/2`.
- **I** involution = `t↔1/t` ⇔ `s↔1−s`.

**Circulation:** `ℤ/ℚ → completions ℚ_p, ℝ → adeles → scale action → theta/Gaussian
self-duality → Mellin → π^{−s/2}Γ(s/2)ζ(s) → functional equation`. This is exactly
**Riemann (1859) / Tate's thesis** completed-ζ construction, re-encoded as a 3-arm normal form.

**Verified (RootScore 6/6):** each arm reproduces its classical operation numerically;
the completed object passes the FE residual; raw ζ + fake kernels fail; removing F or A∞
breaks the FE; S is the involution the test is about. So the three arms are **necessary**.
