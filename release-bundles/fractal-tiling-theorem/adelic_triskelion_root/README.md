# WO-VFD-ADELIC-TRISKELION-ROOT-OBJECT-001

Tests the Adelic Triskelion `AT=(F,A∞,S,W,I)` as a **testable root object** of the
completed-ζ architecture (not a proof of RH).

**Result: STRONG PASS as a normal-form (RootScore 6/6).** Each arm reproduces its
classical operation — F: Euler product→ζ (1e-6); A∞: Gaussian Mellin=½π^{−s/2}Γ(s/2)
(1e-17); S: theta self-duality (1e-31); completed Ξ passes the FE residual (8e-31) while
raw ζ + fake kernels fail; and arm-removal breaks the structure (remove A∞→raw ζ fails;
remove F→Γ·non-arithmetic series fails; remove S→no FE). So all three arms are
**necessary**.

**Honest status:** this is exactly Riemann(1859)/Tate's completed-ζ construction
re-encoded as a 3-arm normal form — KNOWN mathematics verified, NOT new, NOT a proof. The
visual helix is representational. The remaining gap is a **positive self-adjoint witness
operator** (`notes/proof_gap_positive_operator.md`) → next WO-VFD-RH-POSITIVE-ADELIC-
WITNESS-OPERATOR-001.

Run: `python3 src/run_root_object.py` → `outputs/root_score_summary.json`. LOCAL.
