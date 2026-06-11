"""Animation: the zeros snapping into focus as the prime-waves switch on.

Same engine as make_diffraction.py, swept over the number of prime ideals included.
Frame k uses the first k prime-waves; the interference density D(gamma) sharpens until
the 33 independently-computed PARI zeros (red) lock onto the fringes.  Geometry only --
NO zero data enters D; the red lines are the external check.

Writes an MP4 (ffmpeg) if available, else a GIF (pillow).
"""
import json, math, os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
from lab.curve_stage_b import curve_ap_table          # noqa: E402
from lab.sos_probe import _arch_kernel                # noqa: E402

BLUE, RED = "#274472", "#a01b1b"
plt.rcParams.update({"font.size": 12, "figure.dpi": 130})


def _waves(nmax, U):
    rows = curve_ap_table(nmax)
    rows = sorted(rows, key=lambda r: r["norm"])       # switch on by increasing norm
    waves = []
    for r in rows:
        Nq, a, kind = r["norm"], r["a_P"], r["kind"]
        if kind == "bad" or abs(a / (2 * math.sqrt(Nq))) > 1:
            continue
        th = math.acos(max(-1.0, min(1.0, a / (2 * math.sqrt(Nq)))))
        lN = math.log(Nq); k = 1
        comp = []
        while k * lN < U * 3:
            comp.append((k * lN, (2 * math.cos(k * th)) * lN / math.sqrt(Nq ** k)))
            k += 1
        waves.append((Nq, comp))
    return waves


def make(nmax=3000, gmax=26.0, U=6.0, fps=12):
    waves = _waves(nmax, U)
    g = np.linspace(0.2, gmax, 2400)
    omega = np.array([_arch_kernel(x) for x in g]) / (2 * math.pi)
    zeros = []
    zp = os.path.join(H, "..", "out", "curve_zeros.json")
    if os.path.exists(zp):
        zeros = json.load(open(zp)).get("L_zeros", [])

    # cumulative prime contribution after including the first n distinct prime ideals
    counts = list(range(1, len(waves) + 1))
    # subsample frame counts so the movie isn't 400 frames: dense early, sparse late
    frames = sorted(set([1, 2, 3, 4, 5, 6, 8, 10, 13, 16, 20, 25, 32, 40, 55, 75,
                          100, 140, 200, 300, len(waves)]))
    frames = [f for f in frames if f <= len(waves)]

    fig, ax = plt.subplots(figsize=(12, 5))
    line, = ax.plot([], [], color=BLUE, lw=1.5)
    for z in zeros:
        ax.axvline(z, color=RED, lw=0.9, alpha=0.75)
    ax.set_xlim(0.2, gmax); ax.set_xlabel("$\\gamma$  (height on the critical line)")
    ax.set_ylabel("interference density $D(\\gamma)$")
    ax.spines[["top", "right"]].set_visible(False)
    txt = ax.text(0.015, 0.93, "", transform=ax.transAxes, fontsize=12, weight="bold")
    sub = ax.text(0.015, 0.85, "red = 33 PARI zeros (independent)", transform=ax.transAxes,
                  fontsize=9, color=RED)

    def density(nprimes):
        prime = np.zeros_like(g)
        for Nq, comp in waves[:nprimes]:
            for u, amp in comp:
                prime += amp * np.cos(g * u) * math.exp(-(u * u) / (2 * U * U))
        return omega - prime / math.pi

    ymax = float(np.max(density(len(waves)))) * 1.15
    ymin = float(np.min(density(len(waves)))) * 1.15
    ax.set_ylim(ymin, ymax)

    def update(nprimes):
        D = density(nprimes)
        line.set_data(g, D)
        txt.set_text(f"{nprimes} prime ideal(s) switched on")
        return line, txt

    ax.set_title("Zeros snapping into focus as the prime-waves switch on "
                 "(diffraction, geometry only)", fontsize=12.5)
    fig.tight_layout()
    anim = animation.FuncAnimation(fig, update, frames=frames, blit=False)
    out_mp4 = os.path.join(H, "anim_diffraction.mp4")
    out_gif = os.path.join(H, "anim_diffraction.gif")
    try:
        anim.save(out_mp4, writer=animation.FFMpegWriter(fps=fps, bitrate=2400))
        print("wrote", out_mp4)
    except Exception as e:
        print("ffmpeg unavailable (%s); writing GIF" % e)
        anim.save(out_gif, writer=animation.PillowWriter(fps=fps))
        print("wrote", out_gif)
    plt.close(fig)


if __name__ == "__main__":
    make()
