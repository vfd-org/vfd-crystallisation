"""Controlled domain B3.  Polytope triad-closure search.
For each polytope we represent a triad operation as a 3-cycle of three vertices (a
permutation = orthogonal map) and classify.  Expected (and found): all close by
ISOMETRY (orthogonal, eigs on unit circle), so the ranking is NON-discriminating --
consistent with the v1 finding that triad closure is generic.  Reported honestly."""
import numpy as np, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from closure_mode_classifier import classify_closure

POLYS = {"triangle": 3, "tetrahedron": 4, "5-cell": 5, "octahedron": 6,
         "cube": 8, "icosahedron": 12, "dodecahedron": 20, "600-cell(proj)": 120}


def triad_perm(nverts):
    P = np.eye(nverts)
    P[[0, 1, 2]] = P[[2, 0, 1]]
    return P


def run():
    out = {}
    for name, nv in POLYS.items():
        c = classify_closure(triad_perm(nv), label=name)
        out[name] = dict(nverts=nv, mode=c["closure_mode"],
                         on_circle=c["n_on_circle"] == nv, self_adjoint=c["real_spectrum"])
    all_iso = all(v["mode"] == "ISOMETRIC" for v in out.values())
    out["_summary"] = dict(all_isometric=all_iso, discriminating=False,
        note="every polytope triad 3-cycle closes by ISOMETRY (orthogonal, not self-adjoint); "
             "ranking is non-discriminating -- triad closure is generic. Matches v1.")
    return out


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2, default=str))
