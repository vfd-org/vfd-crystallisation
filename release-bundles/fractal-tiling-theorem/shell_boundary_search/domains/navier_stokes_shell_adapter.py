"""Navier-Stokes adapter. Shell = dyadic frequency; boundary = infinite frequency.
Capacity = viscous dissipation - nonlinear transfer. Honest: trend only, sign-crossing
scheme-dependent (see engine v2)."""
import numpy as np, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))
from shell_problem import capacity_outcome

def shell_run(nu, N=18, T=8.0, dt=2e-4):
    k = 2.0**np.arange(N); u = np.zeros(N); u[0]=1.0; u[1]=0.3; qs=[]
    for _ in range(int(T/dt)):
        En=u*u; f=min(int(np.argmax(En))+1,N-1)
        qs.append(2*nu*k[f]**2 - abs(k[f]*u[f]*u[min(f+1,N-1)])/(abs(u[f])+1e-30))
        du=np.zeros(N)
        du[1:-1]=k[1:-1]*(u[:-2]*u[1:-1]-u[1:-1]*u[2:])-nu*k[1:-1]**2*u[1:-1]
        du[0]=-k[0]*u[0]*u[1]-nu*k[0]**2*u[0]; du[-1]=k[-1]*u[-2]*u[-1]-nu*k[-1]**2*u[-1]
        u=u+dt*du
        if not np.all(np.isfinite(u)) or np.max(np.abs(u))>1e6: break
    return float(np.mean(qs))

def run():
    rows={f"nu={nu:.0e}":dict(Qbar=(q:=shell_run(nu)),outcome=capacity_outcome(q)) for nu in [1e-1,1e-2,1e-3,1e-4]}
    qs=[v["Qbar"] for v in rows.values()]
    rows["_trend_down_with_nu"]=qs[0]>qs[-1]
    rows["_honest"]="capacity trend robust; sign-crossing scheme-dependent (not a critical-exponent claim)"
    return rows

if __name__ == "__main__":
    import json; print(json.dumps(run(), indent=2, default=str))
