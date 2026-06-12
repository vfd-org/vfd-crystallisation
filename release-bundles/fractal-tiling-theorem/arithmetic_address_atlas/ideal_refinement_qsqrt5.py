"""
ideal_refinement_qsqrt5.py
Grade D engine (ideal layer): refine a split rational prime into the two
conjugate prime ideals of Z[phi], and test whether cyclotomic-address data
selects one ideal or only the rational prime.

Theorem 5 (routing boundary): q | Phi_d(2) depends only on ord_q(2), a rational
invariant -> sigma-invariant -> CANNOT distinguish q from q'. Address is coarse.
"""
from sympy import factorint, sqrt_mod, isprime
from sympy import cyclotomic_poly


def prime_ideals(q):
    """Representatives of the prime ideals of Z[phi] over rational prime q.
    phi = (1+sqrt5)/2 ; reduce via a root of x^2-x-1 mod q."""
    if q == 5:
        return {"type": "ramified", "ideals": ["(sqrt5)"], "count": 1}
    r = q % 5
    if r in (2, 3):
        return {"type": "inert", "ideals": [f"({q})"], "count": 1}
    # split: x^2 - x - 1 = 0 mod q has two roots phi_1, phi_2 = sigma-conjugates
    roots = sorted(set(sqrt_mod(5, q, all_roots=True)))
    phis = sorted(set(((1 + s) * pow(2, q - 2, q)) % q for s in roots))
    return {"type": "split", "ideals": [f"(q={q}, phi≡{p})" for p in phis],
            "count": 2, "phi_residues": phis}


def address_selects_ideal(q, d):
    """Does 'q | Phi_d(2)' pick one ideal? No -- it depends only on q (sigma-invariant)."""
    pid = prime_ideals(q)
    return {"q": q, "d": d, "splits": pid["type"] == "split",
            "address_is_sigma_invariant": True,
            "selects_individual_ideal": False,
            "reason": "q | Phi_d(2) depends only on ord_q(2), invariant under sigma"}


if __name__ == "__main__":
    for q in [11, 31, 41, 151, 5, 3, 7]:
        print(q, prime_ideals(q))
    print("ideal selection:", address_selects_ideal(11, 10))
