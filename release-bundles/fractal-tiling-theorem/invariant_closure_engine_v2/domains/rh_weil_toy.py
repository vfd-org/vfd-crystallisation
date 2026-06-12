"""Frontier domain C2.  RH / Weil-positivity toy model (beyond FE residual).
Builds the finite Weil explicit-formula quadratic form D = A(arch) + P(pole) - R(primes)
on a Gaussian test-function basis, and classifies its positivity vs fake completions.

Closure-mode mapping:
  FE s<->1-s symmetry          = ISOMETRIC/reflective closure  (cheap, always holds)
  Weil positivity D >= 0       = a POSITIVE INVARIANT FORM      (the real wall)

We also attempt to find a basis where positivity 'diagonalises or simplifies'. It does
diagonalise trivially (it's a symmetric matrix) but the eigen-decomposition gives NO
finite certificate that the INFINITE form stays >= 0 -- the near-null mode persists and
its limit is exactly RH.  So RH is marked UNCHANGED."""
import sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "positive_witness_operator", "src"))
import witness_core as W


def run():
    real = W.weil_form(arch="real", primes="real")
    nulls = {
        "no_arch (P-R)":   W.weil_form(arch="none", primes="real")["min_eig"],
        "fake_Gamma(s/3)": W.weil_form(arch="fake", primes="real")["min_eig"],
        "shuffled_primes": W.weil_form(arch="real", primes="shuffle")["min_eig"],
    }
    eigs = real["eigs"]
    near_null = float(eigs.min())
    # "basis simplification" attempt: the form IS diagonalised by its eigenbasis, but
    # the smallest eigenvalue -> 0+ ; no finite basis makes the infinite-limit obvious.
    return dict(
        finite_weil_min_eig=near_null,
        finite_weil_is_PSD=bool(near_null > -1e-3),
        eigs_low=[float(x) for x in np.sort(eigs)[:4]],
        nulls=nulls,
        nulls_indefinite=bool(all(v < -1e-4 for v in nulls.values())),
        closure_mode="POSITIVE-FORM (symmetric/Weil) with a persistent near-null mode (lambda_min -> 0+)",
        fe_vs_positivity="FE symmetry = isometric/reflective closure (cheap); Weil positivity = the real wall",
        basis_search="form diagonalises in its eigenbasis but no finite basis certifies the infinite-limit positivity",
        rh_status="UNCHANGED: finite form PSD only with near-null mode; infinite-limit positivity = RH (Connes arithmetic site)",
        no_rh_claim=True)


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2, default=str))
