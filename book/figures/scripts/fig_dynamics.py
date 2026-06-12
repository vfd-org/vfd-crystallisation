#!/usr/bin/env python3
"""ch07-wave-vs-diffusion.png — data-real on the 600-cell graph.

The same disturbance, started at one corner, evolved two ways:
  first-order in time (diffusion): it slumps and dies, never travels.
  second-order in time (a wave):   it propagates outward as a front and rings.
This is the contrast the inner clock-mirror forces: time that carries signals.
"""
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import _style as S

S.apply()
d = np.load(S.DATA)
A = d["adjacency"].astype(float)
L = np.diag(A.sum(1)) - A
N = A.shape[0]

# graph distance from source vertex 0 (BFS)
src = 0
dist = np.full(N, -1); dist[src] = 0
q = deque([src])
while q:
    u = q.popleft()
    for v in np.where(A[u] > 0)[0]:
        if dist[v] < 0:
            dist[v] = dist[u] + 1; q.append(v)
shells = np.arange(dist.max() + 1)


def profile(u):
    """mean |field| at each graph distance from the source."""
    return np.array([np.abs(u[dist == s]).mean() for s in shells])


# stable step from the largest Laplacian eigenvalue
lmax = np.linalg.eigvalsh(L)[-1]
dt = 0.9 / np.sqrt(lmax)

u0 = np.zeros(N); u0[src] = 1.0

# diffusion: u_{t+1} = u_t - dt^2 L u_t  (first order, heat-like)
ud = u0.copy(); diff_snaps = []
steps = [6, 18, 36]
for t in range(max(steps) + 1):
    if t in steps:
        diff_snaps.append((t, profile(ud)))
    ud = ud - dt * dt * (L @ ud)

# wave: u_{tt} = -L u  (leapfrog, second order)
uw_prev = u0.copy()
uw = u0 - 0.5 * dt * dt * (L @ u0)
wave_snaps = []
for t in range(1, max(steps) + 1):
    if t in steps:
        wave_snaps.append((t, profile(uw)))
    uw_next = 2 * uw - uw_prev - dt * dt * (L @ uw)
    uw_prev, uw = uw, uw_next

fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.3), sharex=True)
greys = [S.FAINT, S.FOLD, S.INK]
for (t, p), g in zip(diff_snaps, greys):
    axes[0].plot(shells, p, "-o", color=g, ms=3.5, lw=1.4,
                 label=f"step {t}")
oranges = ["#e0a878", "#c9783f", S.ACCENT]
for (t, p), g in zip(wave_snaps, oranges):
    axes[1].plot(shells, p, "-o", color=g, ms=3.5, lw=1.4,
                 label=f"step {t}")

axes[0].set_title("First-order time: diffusion", fontsize=11.5, pad=8)
axes[0].text(0.5, 0.9, "the disturbance slumps and dies",
             transform=axes[0].transAxes, ha="center", fontsize=9.5,
             color=S.INK, style="italic")
axes[1].set_title("Second-order time: a wave", fontsize=11.5, pad=8)
axes[1].text(0.5, 0.92, "the disturbance travels outward and rings back",
             transform=axes[1].transAxes, ha="center", fontsize=9.5,
             color=S.ACCENT, style="italic")
for ax, loc in zip(axes, ["upper right", "center right"]):
    ax.set_xlabel("steps away from the struck corner")
    ax.legend(frameon=False, fontsize=8.8, loc=loc)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
axes[0].set_ylabel("strength of the disturbance")
S.save(fig, "ch07-wave-vs-diffusion")
plt.close(fig)
print("diameter:", int(dist.max()), "| dt:", round(dt, 4))
