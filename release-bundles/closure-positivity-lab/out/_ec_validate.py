"""Calibrate the weight-2 Weil explicit-formula normalization against the conductor-11
elliptic-curve L (degree 2, weight 2, NO pole -- same structure as one icosian factor).

Find (conductor coefficient cN, gamma shift set MU) such that, for an EC L,
    2 * sum_{gamma>0} h(gamma)   ==   ARCH(h) - PRIME(h)
across several sigma.  Then that convention transfers to the icosian (degree 4 = two
such factors)."""
import math, cmath, re, sys

LOGPI = math.log(math.pi)


def dig(z):
    r = 0 + 0j
    while z.real < 12:
        r -= 1 / z; z = z + 1
    i = 1 / z; i2 = i * i
    return r + cmath.log(z) - .5 * i - i2 * (1/12 - i2*(1/120 - i2/252))


def gR(s):
    return -.5 * LOGPI + .5 * dig(s / 2)


def g(u, sg):
    return (sg / math.sqrt(2 * math.pi)) * math.exp(-(sg * sg) * u * u / 2)


def arch(sg, N, mus, cN, rmax=70, npts=6000):
    dr = 2 * rmax / npts; tot = 0.0; lN = math.log(N)
    for i in range(npts + 1):
        r = -rmax + i * dr
        s = cN * lN + 0j
        for mu in mus:
            s += gR(complex(.5 + mu, r)) + gR(complex(.5 + mu, -r))
        w = .5 if i in (0, npts) else 1.0
        tot += w * math.exp(-(r * r) / (2 * sg * sg)) * s.real
    return tot * dr / (2 * math.pi)


def prime(sg, ap):
    tot = 0.0
    for p, a in ap:
        an = a / math.sqrt(p)
        if abs(an) > 2:
            continue
        th = math.acos(max(-1, min(1, an / 2))); lp = math.log(p); k = 1
        while k * lp < 70 and p ** (k / 2.) < 1e12:
            tot += 2 * math.cos(k * th) * lp / p ** (k / 2.) * g(k * lp, sg)
            k += 1
    return tot


def main(path):
    txt = open(path).read()
    N = int(re.search(r"COND=(\d+)", txt).group(1))
    zeros = [float(x) for x in re.search(r"ZEROS=\[([^\]]*)\]", txt).group(1).split(",")]
    apv = re.search(r"AP=\[([^\]]*)\]", txt).group(1).split(",")
    ap = [(n + 1, int(v)) for n, v in enumerate(apv) if int(v) != 0 or (n + 1) in ()]
    ap = [(p, a) for p, a in ap if _isprime(p)]
    print(f"conductor={N}  #zeros={len(zeros)}  first zero={zeros[0]:.4f}  #a_p={len(ap)}")
    cands = [("cN=1, mu={1/2,3/2}", 1.0, [0.5, 1.5]),
             ("cN=0.5, mu={1/2,3/2}", 0.5, [0.5, 1.5]),
             ("cN=1, mu={0,1}", 1.0, [0.0, 1.0]),
             ("cN=0.5, mu={0,1}", 0.5, [0.0, 1.0])]
    sigmas = [2.0, 2.5, 3.0, 3.5]
    for name, cN, mus in cands:
        print(f"\n--- {name} ---")
        ok = True
        for sg in sigmas:
            A = arch(sg, N, mus, cN); P = prime(sg, ap)
            Z = 2 * sum(math.exp(-(z * z) / (2 * sg * sg)) for z in zeros)
            resid = (A - P) - Z
            flag = "OK" if abs(resid) < 0.02 else "x"
            if abs(resid) >= 0.02:
                ok = False
            print(f"  sigma={sg}: ARCH-PRIME={A-P:+.4f}  2sum_h(zeros)={Z:+.4f}  "
                  f"resid={resid:+.4f} {flag}")
        print(f"  => {'MATCHES' if ok else 'no'}")


def _isprime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            return False
    return True


if __name__ == "__main__":
    main(sys.argv[1])
