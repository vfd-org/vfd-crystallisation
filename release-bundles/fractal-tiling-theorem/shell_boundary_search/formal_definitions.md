# Shell-Boundary Problem — formal definitions

**Definition (shell-boundary problem).** A tuple `P = (X, T, h, B, Q)`:
- `X` state space, `T: X → X` transformation;
- `h: X → ℝ` *shell index* (scale, magnitude, frequency, depth, phase layer);
- `S_k = {x : h(x)=k}` the shells; `∂X = {orbits with h(Tⁿx) → ∞}` the **shell boundary**;
- `B ≻ 0` a positive form; `Q(x) = containment(x) − leakage(x)` the **capacity**.

**Shell drift.** `Δh(x) = h(Tx) − h(x)`.

**Rung.** The local transition `S_k → S_{k+Δ}` induced by one step of `T`; its *type* is
the discrete label (e.g. Collatz parity bit, NS transfer direction) that determines `Δh`
and the sign of `Q`.

**Admissibility grammar.** The set of rung-type sequences realisable by actual orbits.

**Closure certificate.** A finitely specified object proving boundary leakage is
controlled (`Q ≥ 0` beyond some shell, or escape rung-words inadmissible).

**Outcomes.** `CLOSED` (certificate found) / `CRITICAL` (`Q ≈ 0`, unresolved) /
`ESCAPING` (positive drift or certified leakage) / `WRONG_BOUNDARY` (shell mis-chosen) /
`UNKNOWN` (no certificate found in the chosen class).

**Theorem schema (general closure).** *If there exist `B ≻ 0` and a certificate `C`
such that the shell capacity `Q_k ≥ 0` for all `k ≥ K`, then no orbit escapes through
`∂X`.* The domain work is choosing `h` and constructing `C`.

**Guardrail.** A reduction/search method, not an oracle. No-certificate ≠ no-solution:
the shell may be wrong, the certificate class too weak, or the problem genuinely open.
