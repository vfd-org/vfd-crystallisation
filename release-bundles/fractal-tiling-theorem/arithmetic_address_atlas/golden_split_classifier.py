"""
golden_split_classifier.py
Grade C engine: route prime factors into Q(sqrt5) by splitting type, and
verify the golden split law.

Theorem 2 (golden split law): 5 | d, q | Phi_d(2), q not| d  =>  q ≡ 1 (mod 5)
                              => q SPLITS in Q(sqrt5).
"""
from sympy import factorint, cyclotomic_poly


def split_type(p):
    """Splitting of rational prime p in Q(sqrt5)."""
    r = p % 5
    if r == 0:
        return "ramified"
    return "split" if r in (1, 4) else "inert"


def classify_phi(d, a=2):
    val = int(cyclotomic_poly(d, a))
    fac = factorint(val)
    rows = []
    for q in fac:
        rows.append({"q": q, "q_mod5": q % 5, "type": split_type(q),
                     "intrinsic": d % q == 0})
    return {"d": d, "Phi_d(a)": val, "factors": rows,
            "golden_d": d % 5 == 0,
            "all_split_nonintrinsic": all(r["type"] == "split"
                                          for r in rows if not r["intrinsic"])}


def split_fraction(dlist, a=2):
    tot = spl = 0
    for d in dlist:
        for r in classify_phi(d, a)["factors"]:
            if r["intrinsic"] and r["q"] == 5:
                continue
            tot += 1
            spl += (r["type"] == "split")
    return spl / tot if tot else 0.0


if __name__ == "__main__":
    print("golden (5|d):")
    for d in [5, 10, 15, 20, 25, 30, 40, 50, 60]:
        c = classify_phi(d)
        print(f"  d={d:>3} Phi={c['Phi_d(a)']:>8} "
              f"{[(r['q'], r['type']) for r in c['factors']]} "
              f"all_split={c['all_split_nonintrinsic']}")
    print("control (5∤d):")
    for d in [3, 7, 8, 16, 32, 64]:
        c = classify_phi(d)
        print(f"  d={d:>3} Phi={c['Phi_d(a)']:>10} "
              f"{[(r['q'], r['type']) for r in c['factors']]}")
    print(f"golden split-fraction   = {split_fraction([5,10,15,20,25,30,40,50,60]):.3f}")
    print(f"control split-fraction  = {split_fraction([3,7,9,11,13,16,32,64]):.3f}")
