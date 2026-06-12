"""
factor_and_cyclotomic_address.py
Grade A/B engine: factorisation + cyclotomic address of a^n +/- 1.

Theorem 4 (plus route):  a^n + 1 = prod_{d | 2n, d not| n} Phi_d(a)
                         (for n = 2^k m, m odd: active d have v2(d) = k+1)
Theorem 3 (minus route): a^n - 1 = prod_{d | n} Phi_d(a)
Theorem 1 (order law):   q | Phi_d(a), q not| d, q not| a  =>  ord_q(a) = d  (q ≡ 1 mod d)
"""
from sympy import factorint, divisors, cyclotomic_poly, isprime


def v2(n):
    a = 0
    while n % 2 == 0:
        n //= 2
        a += 1
    return a, n  # (2-adic valuation, odd part)


def active_sectors(n, sign):
    """Active cyclotomic d-sectors of a^n + sign (sign in {+1,-1})."""
    if sign == -1:
        return sorted(divisors(n))
    # plus side: d | 2n, d not| n  <=>  v2(d) = v2(n)+1
    return sorted(d for d in divisors(2 * n) if n % d != 0)


def cyclotomic_address(n, sign, a=2, small_bound=64):
    out = {
        "expr": f"{a}^{n}{'+1' if sign == 1 else '-1'}",
        "n": n, "a": a, "sign": sign,
        "n_factor": dict(factorint(n)),
        "v2_oddpart": v2(n),
    }
    sectors = active_sectors(n, sign)
    out["num_sectors"] = len(sectors)
    small = [d for d in sectors if d <= small_bound]
    out["small_sectors"] = {}
    for d in small:
        val = int(cyclotomic_poly(d, a))
        out["small_sectors"][d] = {"Phi_d(a)": val, "prime": bool(isprime(val))}
    return out


def composite_witness(n, sign, a=2):
    """For a^n+1 with n not a power of 2, return a forced divisor (Grade A)."""
    if sign != 1:
        return None
    k, m = v2(n)
    if m == 1:
        return None  # n is a power of 2 -> Fermat number, no forced factor here
    d = a ** (2 ** k) + 1                     # 2^(2^k)+1 divides a^n+1
    assert (pow(a, n, d) + 1) % d == 0
    return d


if __name__ == "__main__":
    for n, s in [(136279840, 1), (136279856, 1), (136279841, -1)]:
        addr = cyclotomic_address(n, s)
        w = composite_witness(n, s)
        print(addr["expr"], "| sectors:", addr["num_sectors"],
              "| small:", list(addr["small_sectors"]),
              "| forced divisor:", w)
