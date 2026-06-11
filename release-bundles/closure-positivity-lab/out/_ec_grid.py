"""Grid-search the weight-2 explicit-formula normalization against the conductor-11 EC.
ARCH(a,b) = (1/2pi) int h(r)[ a*logN + b*(sum_mu gR(.5+mu+ir)+gR(.5+mu-ir)) ] dr
PRIME(c)  = c * sum_{p,k} 2 cos(k th) logp p^{-k/2} g(k logp)
Find (a,b,c) making  ARCH(a,b) - PRIME(c) == 2 sum_{gamma>0} h(gamma)  across sigma."""
import math, cmath, re, sys, itertools
LOGPI = math.log(math.pi)
MU = [0.5, 1.5]                                          # weight-2, degree 2 (Gamma_C(s+1/2))


def dig(z):
    r = 0 + 0j
    while z.real < 12:
        r -= 1 / z; z = z + 1
    i = 1 / z; i2 = i * i
    return r + cmath.log(z) - .5*i - i2*(1/12 - i2*(1/120 - i2/252))


def gR(s):
    return -.5*LOGPI + .5*dig(s/2)


def g(u, sg):
    return (sg/math.sqrt(2*math.pi))*math.exp(-(sg*sg)*u*u/2)


def arch(sg, N, a, b, rmax=70, npts=6000):
    dr = 2*rmax/npts; tot = 0.0; lN = math.log(N)
    for i in range(npts+1):
        r = -rmax+i*dr; s = a*lN+0j
        for mu in MU:
            s += b*(gR(complex(.5+mu, r))+gR(complex(.5+mu, -r)))
        w = .5 if i in (0, npts) else 1.0
        tot += w*math.exp(-(r*r)/(2*sg*sg))*s.real
    return tot*dr/(2*math.pi)


def prime(sg, ap, c):
    tot = 0.0
    for p, a_ in ap:
        an = a_/math.sqrt(p)
        if abs(an) > 2:
            continue
        th = math.acos(max(-1, min(1, an/2))); lp = math.log(p); k = 1
        while k*lp < 70 and p**(k/2.) < 1e12:
            tot += c*2*math.cos(k*th)*lp/p**(k/2.)*g(k*lp, sg)
            k += 1
    return tot


def main(path):
    txt = open(path).read()
    N = int(re.search(r"COND=(\d+)", txt).group(1))
    zeros = [float(x) for x in re.search(r"ZEROS=\[([^\]]*)\]", txt).group(1).split(",")]
    apv = re.search(r"AP=\[([^\]]*)\]", txt).group(1).split(",")
    ap = [(n+1, int(v)) for n, v in enumerate(apv) if _isprime(n+1)]
    sigmas = [2.0, 2.5, 3.0]
    best = None
    for a, b, c in itertools.product([0.5, 1.0], [0.5, 1.0], [1.0, 2.0]):
        res = []
        for sg in sigmas:
            A = arch(sg, N, a, b); P = prime(sg, ap, c)
            Z = 2*sum(math.exp(-(z*z)/(2*sg*sg)) for z in zeros)
            res.append(abs((A-P)-Z))
        m = max(res)
        if best is None or m < best[0]:
            best = (m, a, b, c, res)
    print(f"conductor={N}  zeros={len(zeros)}  primes={len(ap)}\n")
    print("grid (a*logN, b*gamma, c*prime) -> max |resid| over sigma=2,2.5,3:")
    rows = []
    for a, b, c in itertools.product([0.5, 1.0], [0.5, 1.0], [1.0, 2.0]):
        res = []
        for sg in sigmas:
            A = arch(sg, N, a, b); P = prime(sg, ap, c)
            Z = 2*sum(math.exp(-(z*z)/(2*sg*sg)) for z in zeros)
            res.append((A-P)-Z)
        mark = "  <== BEST" if (a, b, c) == best[1:4] else ""
        flag = "CLOSES" if max(abs(x) for x in res) < 0.01 else ""
        print(f"  a={a} b={b} c={c}: resid={[round(x,4) for x in res]}  "
              f"max={max(abs(x) for x in res):.4f} {flag}{mark}")
    print(f"\nBEST: a={best[1]} b={best[2]} c={best[3]}  max|resid|={best[0]:.5f}")


def _isprime(n):
    if n < 2:
        return False
    for d in range(2, int(n**.5)+1):
        if n % d == 0:
            return False
    return True


if __name__ == "__main__":
    main(sys.argv[1])
