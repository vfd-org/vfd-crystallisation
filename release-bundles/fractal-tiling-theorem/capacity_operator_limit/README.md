# WO-VFD-RH-CAPACITY-OPERATOR-LIMIT-001

Tracks the finite capacity contraction `K_N = H_N^{−1/2} R_N H_N^{−1/2}`
(`Q_W = H^{1/2}(I−K)H^{1/2}`, `H=A∞+P_F`) and isolates the infinite-limit positivity wall.
**STRONG PASS as the sharpest proof-facing formulation; NOT a proof of RH.**

**The shape of the wall (deliverable):**
- `‖K_N‖`: 0.99958→0.99981 — **< 1, approaches 1 from below**.
- near-null mode: **stable** (overlaps →0.99999998), **low spectral edge**, **top-mass≈0 — does NOT
  escape to the boundary**, archimedean-carried.
- capacity ratio `R/(A∞+P) = 0.9998` → reflection ≈ capacity (marginal).
- nulls fail: no-arch → H not PSD; **fake-Γ → ‖K‖=1.67>1**; random → indefinite.
- gap `1−‖K_N‖` shrinks (best `1/NC²`) but **basis-resolution-dependent, not a law** — not extrapolable.
- **wall = intrinsic, spread, marginal positivity (`‖K‖→1`, no spectral gap) — the hardest case.**

The exact remaining theorem is in `outputs/operator_obstruction_statement.md` (conditions 1–6,
RH-equivalent). Run `python3 src/run_capacity.py`. KNOWN Weil/Connes; not new, not a proof. LOCAL.
