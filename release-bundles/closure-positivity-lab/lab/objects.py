"""The seed registry of finite closure objects.

Each returns a ClosureObject carrying (B, T): B the invariant form, T the structure
operator.  Families:
  * golden     -- mult-by-alpha on K=Q(sqrt5), trace form B=[[2,1],[1,3]] (the EXACT
                  programme anchor).  Self-adjoint always; positive IFF alpha totally pos.
  * lattice    -- root-lattice Gram (E8/D4/A4) and an indefinite Lorentzian control.
  * scheme     -- the V600 closure operator C_phi = L + phi^-2 I, from the real
                  120-vertex 600-cell adjacency.
  * wrongform  -- mult-by-phi paired with the WRONG form (B=I): gate must REJECT.
  * icosian    -- the boundary entry: finite face self-adjoint & positive, but the
                  all-places (Weil) positivity IS RH -> asymptotic_open=True.
"""
from __future__ import annotations
import itertools, json, math, os
import numpy as np
from .core import ClosureObject

PHI = (1 + 5 ** 0.5) / 2
HERE = os.path.dirname(os.path.abspath(__file__))

# trace form on basis {1, phi}:  Tr(1)=2, Tr(phi)=1, Tr(phi^2)=Tr(1+phi)=3
B_GOLD = np.array([[2.0, 1.0], [1.0, 3.0]])


def _mult_alpha(a, b):
    """matrix of x -> (a+b*phi) x on {1, phi}:  1->(a,b), phi->(b, a+b)."""
    return np.array([[a, b], [b, a + b]], float)


def golden(name, a, b, note):
    return ClosureObject(name=name, family="golden", B=B_GOLD.copy(),
                         T=_mult_alpha(a, b), is_fixed_point=True,
                         fixed_point_reason="O_K is closed under multiplication",
                         notes=note,
                         extra={"alpha": f"{a}+{b}phi"})


# --------------------------------------------------------------- Q(sqrt2) family
B_SQRT2 = np.array([[2.0, 0.0], [0.0, 4.0]])           # Tr(1)=2, Tr(sqrt2)=0, Tr(2)=4


def _mult_sqrt2(a, b):
    """matrix of x -> (a+b*sqrt2) x on {1, sqrt2}: 1->(a,b), sqrt2->(2b,a)."""
    return np.array([[a, 2 * b], [b, a]], float)


def sqrt2(name, a, b, note):
    return ClosureObject(name=name, family="sqrt2", B=B_SQRT2.copy(),
                         T=_mult_sqrt2(a, b), is_fixed_point=True,
                         fixed_point_reason="O_K(sqrt2) closed under multiplication",
                         notes=note, extra={"alpha": f"{a}+{b}sqrt2"})


# --------------------------------------------------------------- Cartan helper
def _cartan(n, edges):
    C = 2.0 * np.eye(n)
    for i, j in edges:
        C[i, j] = C[j, i] = -1.0
    return C


A2 = _cartan(2, [(0, 1)])
A3 = _cartan(3, [(0, 1), (1, 2)])
E6 = _cartan(6, [(0, 1), (1, 2), (2, 3), (3, 4), (2, 5)])
E7 = _cartan(7, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (3, 6)])
AFF_A1 = np.array([[2, -2], [-2, 2]], float)           # affine: PSD singular (eig 0,4)


# --------------------------------------------------------------- root lattices
E8 = np.array([
    [2, 0, -1, 0, 0, 0, 0, 0], [0, 2, 0, -1, 0, 0, 0, 0],
    [-1, 0, 2, -1, 0, 0, 0, 0], [0, -1, -1, 2, -1, 0, 0, 0],
    [0, 0, 0, -1, 2, -1, 0, 0], [0, 0, 0, 0, -1, 2, -1, 0],
    [0, 0, 0, 0, 0, -1, 2, -1], [0, 0, 0, 0, 0, 0, -1, 2]], float)
D4 = np.array([[2, -1, 0, 0], [-1, 2, -1, -1], [0, -1, 2, 0], [0, -1, 0, 2]], float)
A4 = np.array([[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]], float)
LORENTZ = np.array([[2, -3], [-3, 2]], float)          # indefinite control


def lattice(name, G, fixed, reason, note):
    n = G.shape[0]
    return ClosureObject(name=name, family="lattice", B=np.eye(n), T=G,
                         is_fixed_point=fixed, fixed_point_reason=reason, notes=note)


# --------------------------------------------------------------- V600 / C_phi
def _vertices_600():
    V = []
    for i in range(4):                                  # 8 of type (+-1,0,0,0)
        for s in (1, -1):
            v = [0, 0, 0, 0]; v[i] = s; V.append(v)
    for s in itertools.product((0.5, -0.5), repeat=4):  # 16 of type (+-1/2)^4
        V.append(list(s))
    base = [PHI, 1.0, 1.0 / PHI, 0.0]                   # 96 even perms of (phi,1,1/phi,0)/2
    seen = set()
    for perm in itertools.permutations(range(4)):
        if _parity(perm) != 0:
            continue
        for signs in itertools.product((1, -1), repeat=3):
            w = [0.0, 0.0, 0.0, 0.0]; si = 0
            for pos, idx in enumerate(perm):
                val = base[pos]
                if abs(val) > 1e-12:
                    w[idx] = val * signs[si] / 2.0; si += 1
                else:
                    w[idx] = 0.0
            key = tuple(round(x, 6) for x in w)
            if key not in seen:
                seen.add(key); V.append(w)
    return np.array(V)


def _parity(perm):
    perm = list(perm); n = len(perm); seen = [False] * n; par = 0
    for i in range(n):
        if not seen[i]:
            j = i; c = 0
            while not seen[j]:
                seen[j] = True; j = perm[j]; c += 1
            par += c - 1
    return par % 2


def cphi_600():
    V = _vertices_600()
    G = V @ V.T
    A = (np.abs(G - PHI / 2) < 1e-6).astype(float)      # neighbours: dot = phi/2
    np.fill_diagonal(A, 0)
    deg = A.sum(1)
    L = np.diag(deg) - A
    C = L + (PHI ** -2) * np.eye(len(V))
    n_nb = int(round(deg.mean()))
    return ClosureObject(name="V600 C_phi = L + phi^-2 I", family="scheme",
                         B=np.eye(len(V)), T=C, is_fixed_point=True,
                         fixed_point_reason="closure operator's defining geometry (600-cell)",
                         notes=f"600-cell graph, {len(V)} verts, deg={n_nb}",
                         extra={"n_vertices": len(V), "degree": n_nb})


# --------------------------------------------------------------- 24-cell C_phi
def cphi_24():
    V = []
    for i in range(4):
        for j in range(i + 1, 4):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [0.0, 0.0, 0.0, 0.0]; v[i] = si; v[j] = sj; V.append(v)
    V = np.array(V)                                     # 24 vertices (D4 roots)
    G = V @ V.T
    A = (np.abs(G - 1.0) < 1e-6).astype(float)          # neighbours: dot = 1 (dist sqrt2)
    np.fill_diagonal(A, 0)
    L = np.diag(A.sum(1)) - A
    C = L + (PHI ** -2) * np.eye(len(V))
    return ClosureObject(name="24-cell C_phi", family="scheme", B=np.eye(len(V)), T=C,
                         is_fixed_point=True, fixed_point_reason="24-cell self-dual geometry",
                         notes=f"24-cell graph, {len(V)} verts, deg={int(A.sum(1).mean())}",
                         extra={"n_vertices": len(V)})


# --------------------------------------------------------------- wrong form
def wrong_form():
    """mult-by-phi in the {1, sqrt5} basis: T = [[1/2,5/2],[1/2,1/2]] is NOT symmetric.
    Paired with the naive (non-invariant) form B=I, the gate must reject it -- the
    invariant trace form here is diag(2,10), not I.  Same operator as mult-phi, wrong form."""
    T = np.array([[0.5, 2.5], [0.5, 0.5]])
    return ClosureObject(name="mult-phi, WRONG form (B=I)", family="wrongform",
                         B=np.eye(2), T=T, is_fixed_point=True,
                         fixed_point_reason="same object, naive (non-invariant) form",
                         notes="naive form: BT not symmetric -> gate REJECTS (true form is diag(2,10))")


# --------------------------------------------------------------- icosian boundary
def icosian_boundary():
    """The RH instance.  Finite face: take the symmetric Brandt-type matrix at a good
    prime with eigenvalues {N+1 (Eisenstein), a_q (cuspidal)} -- self-adjoint, real,
    finite-positive.  But the positivity that the framework actually needs is the
    all-places Weil positivity of the cuspidal L, which IS RH -> asymptotic_open."""
    aq, N = 8, 31                                       # good factor at the level prime
    # symmetric 2x2 with eigenvalues N+1 and aq (Eisenstein vs cuspidal)
    lo, hi = sorted((aq, N + 1)); c = (lo + hi) / 2; r = (hi - lo) / 2
    T = np.array([[c, r], [r, c]])                      # eigenvalues lo, hi
    try:
        rows = json.load(open(os.path.join(HERE, "..", "..", "icosian-rh-geometric",
                                            "repro", "data", "geometric_aP.json")))["rows"]
        all_sa = all(r_["self_adjoint"] for r_ in rows)
        all_ram = all(r_["ramanujan_ok"] for r_ in rows)
    except Exception:
        all_sa = all_ram = None
    return ClosureObject(name="icosian cuspidal L (RH instance)", family="icosian",
                         B=np.eye(2), T=T, is_fixed_point=True,
                         fixed_point_reason="maximal icosian order, class number 1",
                         asymptotic_open=True,
                         notes="finite Brandt face positive; all-places Weil positivity = RH(L), OPEN",
                         extra={"brandt_all_self_adjoint": all_sa,
                                "brandt_all_ramanujan": all_ram})


def registry():
    return [
        # golden Q(sqrt5)
        golden("mult-phi", 0, 1, "phi: conj 1-phi<0 -> NOT totally positive"),
        golden("mult-phi^2", 1, 1, "phi^2: both conjugates >0 -> totally positive"),
        golden("mult-(2+phi)", 2, 1, "2+phi: totally positive"),
        golden("mult-(phi-2)", -2, 1, "phi-2: both conjugates <0 -> totally negative"),
        golden("mult-sqrt5", -1, 2, "sqrt5 = 2phi-1: conjugate -sqrt5 -> indefinite"),
        # second field Q(sqrt2): the law must not be Q(sqrt5)-specific
        sqrt2("mult-(1+sqrt2)", 1, 1, "1+sqrt2: conj 1-sqrt2<0 -> NOT totally positive"),
        sqrt2("mult-(3+sqrt2)", 3, 1, "3+sqrt2: both conjugates >0 -> totally positive"),
        # root lattices / cascade rungs
        lattice("E8 Gram", E8, True, "unique even unimodular rank-8 lattice (self-dual)",
                "E8: posdef, self-dual"),
        lattice("E7 Gram", E7, True, "root lattice of E7", "E7: posdef"),
        lattice("E6 Gram", E6, True, "root lattice of E6", "E6: posdef"),
        lattice("D4 Gram", D4, True, "root lattice of D4 (GR rung)", "D4: posdef"),
        lattice("A4 Gram", A4, True, "root lattice of A4", "A4: posdef"),
        lattice("A3 Gram", A3, True, "root lattice of A3", "A3: posdef"),
        lattice("A2 Gram", A2, True, "root lattice of A2", "A2: posdef"),
        # non-positive self-adjoint controls
        lattice("Lorentzian [[2,-3],[-3,2]]", LORENTZ, False,
                "indefinite: not a positive lattice", "control: indefinite Gram"),
        lattice("affine A1~ [[2,-2],[-2,2]]", AFF_A1, False,
                "affine: PSD but singular (eig 0)", "control: PSD-singular, not pos-def"),
        # closure-operator schemes
        cphi_600(),
        cphi_24(),
        # gate tests
        wrong_form(),
        # the open boundary
        icosian_boundary(),
    ]
