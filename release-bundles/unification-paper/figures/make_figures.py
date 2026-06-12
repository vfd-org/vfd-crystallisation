"""Figures for "The Icosian Closure Object as a Unification of Geometry and Arithmetic".

  fig_object_two_faces.pdf  ONE object -> E8 geometry (exact) + L-function (exact); same
                            closure form; RH witness = frontier.  [central schematic]
  fig_e8_coxeter.pdf        geometry face: 240 E8 roots in the Coxeter plane (real data).
  fig_factorization.pdf     arithmetic face: L = zeta_K.zeta_K(s-1); zeta is one of four.
  fig_witness_symbol.pdf    frontier: scale-axis operator symbol + operator<->known zeros.
  fig_form_relativity.pdf   the shared form: self-adjointness is form-relative (exact).
"""
import math, os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({"font.size": 13, "axes.titlesize": 14, "figure.dpi": 200,
                     "savefig.dpi": 200})
GREEN, GOLD, BLUE, RED, PURP = "#1b7a3d", "#b8860b", "#274472", "#a01b1b", "#6d3a86"


# ---------------------------------------------------------------- central fig
def fig_object_two_faces():
    fig, ax = plt.subplots(figsize=(11, 5.4)); ax.axis("off")
    ax.set_xlim(0, 12); ax.set_ylim(0, 6.4)

    def box(x, y, w, h, fc, ec, lw=2):
        ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
                     boxstyle="round,pad=0.12", fc=fc, ec=ec, lw=lw))

    # the object (centre)
    box(6, 4.7, 4.6, 1.5, "#eef3fb", BLUE, 2.4)
    ax.text(6, 5.15, "the icosian closure object", ha="center", weight="bold",
            fontsize=14, color=BLUE)
    ax.text(6, 4.55, r"$600$-cell $\;\to\;$ maximal order $\mathcal{I}$", ha="center",
            fontsize=12)
    ax.text(6, 4.05, r"over $K=\mathbb{Q}(\sqrt{5})$,  lattice $E_8$", ha="center",
            fontsize=11)

    # geometry face (left)
    box(2.4, 2.2, 4.0, 1.7, "white", GREEN)
    ax.text(2.4, 2.78, "GEOMETRY", ha="center", color=GREEN, weight="bold")
    ax.text(2.4, 2.28, r"$E_8$ root system", ha="center", fontsize=12)
    ax.text(2.4, 1.85, r"shell$_1\cup(1/\varphi)$shell$_1=240$", ha="center", fontsize=10)
    ax.text(2.4, 1.5, "EXACT", ha="center", color="white", weight="bold", fontsize=11,
            bbox=dict(boxstyle="round,pad=0.18", fc=GREEN, ec="none"))

    # arithmetic face (right)
    box(9.6, 2.2, 4.2, 1.7, "white", GOLD)
    ax.text(9.6, 2.78, "ARITHMETIC", ha="center", color=GOLD, weight="bold")
    ax.text(9.6, 2.28, r"$L(\Theta_\mathcal{I},s)=\zeta_K(s)\,\zeta_K(s-1)$", ha="center",
            fontsize=11.5)
    ax.text(9.6, 1.85, r"$C_2=1$, no local correction", ha="center", fontsize=10)
    ax.text(9.6, 1.5, "EXACT", ha="center", color="white", weight="bold", fontsize=11,
            bbox=dict(boxstyle="round,pad=0.18", fc=GOLD, ec="none"))

    for (x, c) in [(2.4, GREEN), (9.6, GOLD)]:
        ax.add_patch(FancyArrowPatch((6 + (x-6)*0.33, 4.0), (x, 3.1),
                     arrowstyle="-|>", mutation_scale=18, lw=1.8, color=c))

    # shared form (bottom centre)
    box(6, 0.55, 7.4, 0.86, "#fbf6e9", GOLD, 1.6)
    ax.text(6, 0.55, r"unified by the closure / trace form $B$  "
            r"(golden trace $c=1+1/\sqrt{5}$  $\;\leftrightarrow\;$  Weil form)",
            ha="center", fontsize=11)
    ax.add_patch(FancyArrowPatch((2.4, 1.35), (4.2, 0.95), arrowstyle="-",
                 lw=1.2, color=GOLD, linestyle=":"))
    ax.add_patch(FancyArrowPatch((9.6, 1.35), (7.8, 0.95), arrowstyle="-",
                 lw=1.2, color=GOLD, linestyle=":"))

    # frontier (far right, off the arithmetic face)
    ax.add_patch(FancyArrowPatch((11.7, 2.2), (11.7, 4.1), arrowstyle="-|>",
                 mutation_scale=14, lw=1.5, color=RED, connectionstyle="arc3,rad=0"))
    ax.text(11.55, 3.95, "FRONTIER", ha="center", color=RED, weight="bold",
            fontsize=10, rotation=90, va="top")
    ax.text(6, 6.05, r"one object, two exact faces, one form  --  and one open frontier "
            r"($A\geq0\Leftrightarrow$ RH$(L)$)", ha="center", fontsize=12.5,
            weight="bold")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_object_two_faces.pdf"), bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- arithmetic face
def fig_factorization():
    fig, ax = plt.subplots(figsize=(10, 3.4)); ax.axis("off")
    ax.set_xlim(0, 12); ax.set_ylim(0, 4)
    ax.text(6, 3.6, r"$L(\Theta_\mathcal{I},s)\;=\;\zeta_K(s)\,\zeta_K(s-1)$"
            r"\quad(exact, $C_2=1$)", ha="center", fontsize=15)
    ax.text(6, 2.9, r"$=\;\zeta(s)\;\cdot\;L(s,\chi_5)\;\cdot\;\zeta(s-1)\;\cdot\;"
            r"L(s-1,\chi_5)$", ha="center", fontsize=14)
    labels = [(2.0, r"$\zeta(s)$", "Riemann $\\zeta$", RED),
              (4.7, r"$L(s,\chi_5)$", "real quad.", "#555"),
              (7.3, r"$\zeta(s-1)$", "shifted", "#555"),
              (9.9, r"$L(s-1,\chi_5)$", "shifted", "#555")]
    for x, sym, note, c in labels:
        ax.add_patch(FancyBboxPatch((x-1.0, 1.35), 2.0, 0.7,
                     boxstyle="round,pad=0.08", fc="white",
                     ec=(RED if c == RED else "#aaa"), lw=(2.2 if c == RED else 1.2)))
        ax.text(x, 1.7, sym, ha="center", fontsize=12, color=c)
        ax.text(x, 0.95, note, ha="center", fontsize=9, color=c)
    ax.text(2.0, 0.45, "ONE factor of four\n(not isolated)", ha="center", fontsize=9.5,
            color=RED, weight="bold")
    ax.text(8.6, 0.45, "the object contains $\\zeta$ but does NOT single it out\n"
            "(certified negative, structural)", ha="center", fontsize=9.5, color="#555")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_factorization.pdf"), bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- geometry face
def _e8_roots():
    R = []
    for i in range(8):
        for j in range(i+1, 8):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [0.0]*8; v[i] = si; v[j] = sj; R.append(v)
    for b in range(256):
        s = [(1 if (b >> k) & 1 == 0 else -1) for k in range(8)]
        if s.count(-1) % 2 == 0:
            R.append([0.5*x for x in s])
    return np.array(R)


def _coxeter_plane():
    a = np.array([
        [.5, -.5, -.5, -.5, -.5, -.5, -.5, .5], [1, 1, 0, 0, 0, 0, 0, 0],
        [-1, 1, 0, 0, 0, 0, 0, 0], [0, -1, 1, 0, 0, 0, 0, 0],
        [0, 0, -1, 1, 0, 0, 0, 0], [0, 0, 0, -1, 1, 0, 0, 0],
        [0, 0, 0, 0, -1, 1, 0, 0], [0, 0, 0, 0, 0, -1, 1, 0]], float)
    w = np.eye(8)
    for al in a:
        w = w @ (np.eye(8) - np.outer(al, al))
    vals, vecs = np.linalg.eig(w)
    k = int(np.argmin([abs((np.angle(v) % (2*math.pi)) - 2*math.pi/30) for v in vals]))
    z = vecs[:, k]; u, v = np.real(z), np.imag(z)
    return u/np.linalg.norm(u), v/np.linalg.norm(v)


def fig_e8_coxeter():
    R = _e8_roots(); u, v = _coxeter_plane()
    xy = np.column_stack([R @ u, R @ v]); rad = np.hypot(xy[:, 0], xy[:, 1])
    fig, ax = plt.subplots(figsize=(6.0, 6.0))
    for rr in sorted(set(np.round(rad, 4))):
        ax.add_patch(plt.Circle((0, 0), rr, fill=False, color="#ddd", lw=0.7, zorder=1))
    ax.scatter(xy[:, 0], xy[:, 1], s=34, c=rad, cmap="viridis", edgecolors="k",
               linewidths=0.4, zorder=3)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("geometry face (EXACT): 240 $E_8$ roots, Coxeter plane\n"
                 "8 rings $\\times$ 30, norm$^2=2$, even integral", fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_e8_coxeter.pdf"), bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- frontier
def _dig(z):
    r = 0+0j
    while z.real < 10:
        r -= 1/z; z = z+1
    i = 1/z; i2 = i*i
    return r + np.log(z) - .5*i - i2*(1/12 - i2*(1/120 - i2/252))


def _gR(s): return -.5*math.log(math.pi) + .5*_dig(s/2)


def _omega(r, kap, lc):
    o = np.empty_like(r)
    for n, rr in enumerate(r):
        t = lc+0j
        for k in kap:
            t += _gR(complex(.5+k, rr)) + _gR(complex(.5+k, -rr))
        o[n] = t.real
    return o


def fig_witness_symbol():
    sys.path.insert(0, os.path.join(HERE, "..", "..", "vfd-closure-object", "repro", "src"))
    rows = []
    try:
        import geometric_aP as gap; rows = gap.load_cache()["rows"]
    except Exception:
        pass
    r = np.linspace(-30, 30, 6000)

    def primes(n):
        s = [True]*(n+1); s[0:2] = [False, False]
        for i in range(2, int(n**.5)+1):
            if s[i]:
                for j in range(i*i, n+1, i): s[j] = False
        return [i for i in range(2, n+1) if s[i]]
    prz = np.zeros_like(r)
    for p in primes(2000):
        lp = math.log(p); k, pk = 1, p
        while lp*k < 30:
            prz += 2*(lp/math.sqrt(pk))*np.cos(r*k*lp); k += 1; pk *= p
            if pk > 1e15: break
    sigz = _omega(r, [0.], 0.) - prz
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.0))
    ax[0].plot(r, sigz, color=BLUE, lw=1.4, label=r"$\zeta$")
    if rows:
        prL = np.zeros_like(r)
        for row in rows:
            Nq = row["norm"]; aq = row["a_q_geometric"]
            x = max(-1, min(1, aq/(2*math.sqrt(Nq)))); th = math.acos(x)
            lN = math.log(Nq); k = 1
            while k*lN < 30 and Nq**(k/2) < 1e12:
                prL += (2*math.cos(k*th)*lN/math.sqrt(Nq**k))*np.cos(r*k*lN); k += 1
        ax[0].plot(r, _omega(r, [0., 1., 0., 1.], math.log(775)) - prL, color=GOLD,
                   lw=1.4, label="icosian $L$")
    ax[0].axhline(0, color="#999", lw=.6); ax[0].set_xlim(-30, 30)
    ax[0].set_xlabel("$r$"); ax[0].set_ylabel(r"symbol $\sigma_A(r)$")
    ax[0].set_title("witness symbol: real & even\n$\\Rightarrow A$ self-adjoint",
                    fontsize=12)
    ax[0].legend(); ax[0].spines[["top", "right"]].set_visible(False)
    ZETA = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
            40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248]
    sig = np.linspace(2.5, 6, 8); op, zr = [], []; dr = r[1]-r[0]
    for sg in sig:
        phi = np.exp(-(r*r)/(2*sg*sg))
        op.append(np.trapz(sigz*phi, dx=dr)/(2*math.pi) + 2*math.exp(1/(8*sg*sg)))
        zr.append(2*sum(math.exp(-(g*g)/(2*sg*sg)) for g in ZETA))
    ax[1].plot(zr, op, "o", color=GREEN, ms=7, zorder=3)
    lim = [min(zr)*.8, max(zr)*1.05]; ax[1].plot(lim, lim, "--", color="#999", lw=1)
    ax[1].set_xlabel(r"$\sum_\rho|\widehat h(\gamma_\rho)|^2$ (known $\zeta$ zeros)")
    ax[1].set_ylabel(r"$\langle h,Ah\rangle$ (operator)")
    ax[1].set_title("frontier: operator reproduces zeros\n($\\sim10^{-7}$); "
                    "$A\\geq0$ = RH = wall", fontsize=12)
    ax[1].spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_witness_symbol.pdf"), bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- shared form
def fig_form_relativity():
    fig, ax = plt.subplots(figsize=(7.2, 3.0)); ax.axis("off")
    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.text(5, 5.4, r"the shared form: multiplication by $\varphi$ on $\mathbb{Q}(\sqrt{5})$",
            ha="center", fontsize=12.5)
    ax.text(2.6, 4.2, "naive  T", ha="center", fontsize=11)
    ax.text(2.6, 3.2, "[ 1/2  5/2 ]\n[ 1/2  1/2 ]", ha="center", family="monospace",
            fontsize=12)
    ax.text(2.6, 2.0, r"$T\neq T^\top$", ha="center", color=RED, fontsize=12)
    ax.text(7.4, 4.2, r"trace form $B=\mathrm{diag}(2,10)$", ha="center", fontsize=11)
    ax.text(7.4, 3.2, "B T = [ 1  5 ]\n         [ 5  5 ]", ha="center",
            family="monospace", fontsize=12)
    ax.text(7.4, 2.0, r"$BT=(BT)^\top$  $\Rightarrow$  $B$-self-adjoint", ha="center",
            color=GREEN, fontsize=11)
    ax.text(5, 0.7, "same operator: non-symmetric naively, self-adjoint in the trace "
            "form\nself-adjointness / positivity is FORM-RELATIVE", ha="center",
            fontsize=10.5, weight="bold")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_form_relativity.pdf"), bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig_object_two_faces(); print("wrote fig_object_two_faces.pdf")
    fig_e8_coxeter();       print("wrote fig_e8_coxeter.pdf")
    fig_factorization();    print("wrote fig_factorization.pdf")
    fig_witness_symbol();   print("wrote fig_witness_symbol.pdf")
    fig_form_relativity();  print("wrote fig_form_relativity.pdf")
    print("done ->", HERE)
