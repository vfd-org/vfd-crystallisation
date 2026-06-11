# Task: WO for BSD T_E s-regularised convergence

## Goal

Discharge H_{BSD-Conv} (the cascade Hecke operator convergence
hypothesis) so `papers/millennium-bsd-formal/bsd-formal.tex` can be
promoted from "conditional on H_{BSD-Conv} + H_{BSD-Spec}" to
"conditional only on the spectral identification H_{BSD-Spec}."

The cascade Hecke operator T_E is defined as the formal sum

  T_E = Σ_{p ∤ N} ω_p · (T_p - a_p(E) · id)
  with ω_p = (log p / √p) · φ^{-v_φ(p)}.

The naive termwise bound gives ‖term_p‖ ≤ 2 log p, hence Σ
diverges. To make T_E converge we introduce s-regularization:

  T_E(s) = Σ_p ω_p · p^{-s} · (T_p - a_p(E) · id)

For Re(s) > 1, ‖T_E(s)‖ ≤ Σ_p 2 log p · p^{-Re(s)} converges
absolutely. We then ask: for what spectral data of T_E(s) does
the analytic continuation to s = 0 (or s = 1, or wherever) make
sense, and what is the kernel?

## What's needed

- B_BSD_1: state the s-regularization explicitly and prove
  absolute convergence on Re(s) > 1.
- B_BSD_2: describe the analytic continuation strategy (Rankin-
  Selberg, symmetric square, etc.).
- B_BSD_3: identify the s-value where ker T_E(s) = rank E(Q)
  (per cascade Eichler-Shimura). For the cascade, this should be
  s = 0 (the BSD-relevant evaluation).
- B_BSD_4: prove or sketch convergence in a region containing s = 0,
  using known L-function bounds (Hasse-Weil + Deligne).

## Constraints (no downgrades)

- Cite classical Eichler-Shimura, Rankin-Selberg, Deligne.
- Show explicit upper bounds with constants.
- The goal is to remove H_{BSD-Conv} as a separate hypothesis;
  the result should depend only on H_{BSD-Spec} (the spectral
  identification with rank E(Q)).

## Required output (Sections A-F per codex_derive template)
