"""Calibration domains A1-A3 (answers known) -- the classifier MUST rediscover these.
A1 finite cycles/permutations -> ISOMETRIC (not self-adjoint).
A2 contraction maps          -> DISSIPATIVE (Q>0).
A3 rotations/unitary         -> ISOMETRIC (norm conserved)."""
import numpy as np, math, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from closure_mode_classifier import classify_closure


def cyc(k):
    P = np.roll(np.eye(k), 1, axis=0)
    return P


def run():
    out = {}
    for k in [3, 4, 5]:
        c = classify_closure(cyc(k), label=f"{k}-cycle")
        out[f"cycle_{k}"] = dict(mode=c["closure_mode"], expect="ISOMETRIC",
                                 ok=c["closure_mode"] == "ISOMETRIC", real_spectrum=c["real_spectrum"])
    for lam in [0.5, 0.9]:
        M = lam * np.array([[1.0, 0.3], [0.0, 1.0]])   # contraction (rho=lam<1)
        c = classify_closure(M, label=f"contraction_{lam}")
        out[f"contraction_{lam}"] = dict(mode=c["closure_mode"], expect="DISSIPATIVE",
                                         ok=c["closure_mode"] == "DISSIPATIVE",
                                         dissipative_defect=c["dissipative_defect"])
    th = 2 * math.pi / 7
    R = np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])
    c = classify_closure(R, label="rotation")
    out["rotation_2pi/7"] = dict(mode=c["closure_mode"], expect="ISOMETRIC",
                                 ok=c["closure_mode"] == "ISOMETRIC", isometry_residual=c["isometry_residual"])
    # a defective rho=1 system -> CRITICAL (Jordan block)
    J = np.array([[1.0, 1.0], [0.0, 1.0]])
    c = classify_closure(J, label="jordan_block")
    out["jordan_rho1_defective"] = dict(mode=c["closure_mode"], expect="CRITICAL",
                                        ok=c["closure_mode"] == "CRITICAL")
    # an escaping system rho>1 -> NONE
    c = classify_closure(np.array([[1.5, 0.0], [0.0, 0.7]]), label="escape")
    out["escape_rho>1"] = dict(mode=c["closure_mode"], expect="NONE",
                               ok=c["closure_mode"] == "NONE")
    out["_all_ok"] = all(v["ok"] for v in out.values() if isinstance(v, dict) and "ok" in v)
    return out


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2, default=str))
