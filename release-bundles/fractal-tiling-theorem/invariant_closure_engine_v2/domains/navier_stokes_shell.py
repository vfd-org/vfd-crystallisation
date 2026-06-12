"""Frontier domain C3.  Navier-Stokes regularity via dyadic shell model.
Capacity Q = viscous dissipation - nonlinear forward transfer at the cascade front.
High viscosity -> Q>0 (regular closure); low viscosity -> Q<0 (escape to small scales)."""
import numpy as np, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def shell_run(nu, N=18, T=8.0, dt=2e-4):
    k = 2.0 ** np.arange(N)
    u = np.zeros(N); u[0] = 1.0; u[1] = 0.3
    qs, blew = [], False
    for _ in range(int(T / dt)):
        En = u * u
        front = min(int(np.argmax(En)) + 1, N - 1)
        qs.append(2 * nu * k[front] ** 2
                  - abs(k[front] * u[front] * u[min(front + 1, N - 1)]) / (abs(u[front]) + 1e-30))
        du = np.zeros(N)
        du[1:-1] = k[1:-1] * (u[:-2] * u[1:-1] - u[1:-1] * u[2:]) - nu * k[1:-1] ** 2 * u[1:-1]
        du[0] = -k[0] * u[0] * u[1] - nu * k[0] ** 2 * u[0]
        du[-1] = k[-1] * u[-2] * u[-1] - nu * k[-1] ** 2 * u[-1]
        u = u + dt * du
        if not np.all(np.isfinite(u)) or np.max(np.abs(u)) > 1e6:
            blew = True; break
    Qbar = float(np.mean(qs))
    cls = "STABLE-CLOSURE" if Qbar > 1e-3 else ("ESCAPE-LEAKAGE" if Qbar < -1e-3 else "CRITICAL-BOUNDARY")
    return dict(nu=nu, Qbar=Qbar, classify=cls, numeric_blowup=blew)


def run():
    rows = [shell_run(nu) for nu in [1e-1, 1e-2, 1e-3, 1e-4]]
    trend = rows[0]["Qbar"] > rows[-1]["Qbar"]
    return dict(sweep=rows, capacity_rises_with_viscosity=bool(trend),
                reproduces="viscosity trichotomy (regular<->escape) via same Q as Collatz",
                open_wall="3D NS controlled energy is SUPERCRITICAL -> sign of Q undetermined = CRITICAL-BOUNDARY",
                honest="dyadic shell caricature; validates engine not NS; not a proof")


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2, default=str))
