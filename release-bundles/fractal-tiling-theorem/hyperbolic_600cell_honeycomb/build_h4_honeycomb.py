"""
build_h4_honeycomb.py
Construct and verify the {3,3,5,3} regular honeycomb of HYPERBOLIC 4-space H^4
(600-cells filling H^4), and generate a finite 'onion' patch in the Poincare ball.

Method: the Coxeter group [3,3,5,3] is a discrete reflection group of O(4,1).
Build the 5 reflection generators from the Schlafli/Gram matrix (signature (4,1)),
verify the Coxeter relations, then BFS the orbit of a 600-cell CELL-CENTRE.
"""
import numpy as np, json, os
np.set_printoptions(suppress=True)

LABELS = [3, 3, 5, 3]; n = 5
HERE = os.path.dirname(os.path.abspath(__file__))

# --- Gram matrix of the form (Lorentzian) ---
M = np.eye(n)
for i, m in enumerate(LABELS):
    M[i, i+1] = M[i+1, i] = -np.cos(np.pi/m)
ev = np.linalg.eigvalsh(M)
sig = (int((ev > 1e-9).sum()), int((ev < -1e-9).sum()))
print(f"form signature (+,-) = {sig}  -> {'HYPERBOLIC H^4 (Lorentzian)' if sig==(4,1) else 'NOT (4,1)!'}")

# --- reflection generators: s_i = I - 2 e_i e_i^T M  (isometries of M) ---
G = []
for i in range(n):
    E = np.zeros((n, n)); E[i, i] = 1.0
    G.append(np.eye(n) - 2*E @ M)

def order(A, mx=40):
    P = np.eye(n)
    for k in range(1, mx+1):
        P = P @ A
        if np.allclose(P, np.eye(n), atol=1e-7): return k
    return None

print("verifying Coxeter relations [3,3,5,3]:")
ok = all(order(G[i]) == 2 for i in range(n))                     # reflections
rel = [order(G[i] @ G[i+1]) for i in range(n-1)]
ok &= rel == LABELS                                              # adjacent orders
ok &= all(order(G[i] @ G[j]) == 2 for i in range(n) for j in range(i+2, n))  # commuting
print(f"  s_i^2=1, (s_i s_i+1) orders = {rel} (want {LABELS}), non-adjacent commute: {ok}")
print(f"  => group is genuinely [3,3,5,3]: {ok and sig==(4,1)}")

# --- standard Lorentz coordinates (diagonalise M to diag(1,1,1,1,-1)) ---
w, Q = np.linalg.eigh(M)
idx = np.argsort(w)                      # negative eigenvalue first
w, Q = w[idx], Q[:, idx]
T = (np.diag(np.sqrt(np.abs(w))) @ Q.T)  # y = T x ; form becomes J=diag(-1,1,1,1,1)
J = np.diag(np.sign(w))                  # sign(w) sorted: (-1,+,+,+,+)

def to_std(x): return T @ x
def jnorm(y): return y @ J @ y

# --- seed = 600-cell cell centre = fixed point of finite [3,3,5] (nodes 0..3) ---
seed = np.linalg.solve(M, np.eye(n)[:, 4])    # fundamental weight w_5 = M^{-1} e_5
print(f"cell-centre B(p,p) = {seed @ M @ seed:.4f}  (<0 => proper point of H^4)")

def normalize(x):
    y = to_std(x); q = jnorm(y)
    if q >= 0: return None                    # not timelike
    y = y / np.sqrt(-q)
    if y[0] < 0: y = -y                        # future-pointing (time = index 0)
    return y

def ball(y):                                  # hyperboloid -> Poincare ball
    return y[1:] / (1.0 + y[0])

def key(y): return tuple(np.round(y, 5))

# --- BFS the honeycomb (onion shells = BFS depth) ---
s0 = seed.copy()
y0 = normalize(s0)
seen = {key(y0): 0}
coords = {key(y0): (s0.copy(), 0)}
frontier = [s0]; depth = 0; MAXDEPTH = 14
while frontier and depth < MAXDEPTH and len(seen) < 1500:
    depth += 1; nxt = []
    for x in frontier:
        for g in G:
            xx = g @ x
            yy = normalize(xx)
            if yy is None: continue
            k = key(yy)
            if k not in seen:
                seen[k] = depth; coords[k] = (xx.copy(), depth); nxt.append(xx)
    frontier = nxt
    print(f"  shell {depth}: +{len(nxt)} cells  (cumulative {len(seen)})")

# --- save the patch (Poincare-ball centres of the 600-cells) ---
pts = []
for k, (x, d) in coords.items():
    y = normalize(x); b = ball(y)
    pts.append({"shell": d, "poincare": [round(float(c), 6) for c in b],
                "radius": round(float(np.linalg.norm(b)), 6)})
pts.sort(key=lambda r: (r["shell"], r["radius"]))
json.dump({"honeycomb": "{3,3,5,3}", "space": "H^4", "model": "Poincare ball",
           "cell": "600-cell {3,3,5}", "signature": sig, "verified": bool(ok),
           "n_cells": len(pts), "cells": pts},
          open(os.path.join(HERE, "results", "honeycomb_patch.json"), "w"), indent=1)
print(f"\nBUILT: {len(pts)} 600-cell centres of the {{3,3,5,3}} H^4 honeycomb")
print(f"  shells (onion): radii grow {min(p['radius'] for p in pts if p['radius']>1e-6):.3f} "
      f"-> {max(p['radius'] for p in pts):.3f} toward the H^4 boundary sphere")
print("  saved -> results/honeycomb_patch.json")
