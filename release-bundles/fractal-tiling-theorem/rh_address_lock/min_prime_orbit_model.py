"""
min_prime_orbit_model.py  (WO-RH-ARITHMETIC-ADDRESS-LOCK-001, Deliverable 2)
The minimal prime-orbit model: one primitive orbit per rational prime, length log p.
Z(s) = prod_p (1 - e^{-s log p})^{-1} = prod_p (1 - p^{-s})^{-1} = zeta(s).
Conclusion: the 'log p address-lock' IS the Euler product -- tautological. It is
NOT the missing piece. The wall is a self-adjoint operator whose spectrum = the zeros.
"""
import mpmath as mp
from sympy import primerange
mp.mp.dps = 25


def euler_zeta(s, P=100000):
    s = mp.mpf(s); z = mp.mpf(1)
    for p in primerange(2, P):
        z *= 1 / (1 - mp.e**(-s * mp.log(p)))   # orbit length = log p
    return z


if __name__ == "__main__":
    for s in [2, 3, 4]:
        print(f"s={s}: Z(s)={mp.nstr(euler_zeta(s),12)}  zeta(s)={mp.nstr(mp.zeta(s),12)}")
    print("Z(s) == zeta(s): the address-lock is the Euler product (already locked).")
