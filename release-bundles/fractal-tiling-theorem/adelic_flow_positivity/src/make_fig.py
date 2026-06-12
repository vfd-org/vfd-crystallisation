import numpy as np, math, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.linalg import expm
N=48; du=16.0/(N-1); off=np.ones(N-1)/(2*du)
D=np.diag(-1j*off,1)+np.diag(1j*off,-1)
H=D.conj().T@D+0.2*np.eye(N)
taus=np.linspace(0,3,13)
flow=[float(np.linalg.norm(expm(-1j*t*D),2)) for t in taus]
capn=[float(np.linalg.norm(expm(-t*H),2)) for t in taus]
fig,ax=plt.subplots(figsize=(8,5))
ax.plot(taus,flow,'o-',color='#c08bff',label='scale flow exp(-iτD) UNITARY -> no positivity')
ax.plot(taus,capn,'s-',color='#1f9e89',label='capacity exp(-τH), H>=0 CONTRACTION -> positivity')
ax.axhline(1,color='k',lw=0.6,ls=':'); ax.set_xlabel('tau'); ax.set_ylabel('operator norm')
ax.set_title('Positivity from the PSD CAPACITY, not flow orientation')
ax.legend(fontsize=9); fig.tight_layout(); fig.savefig('outputs/figures/flow_vs_capacity_norms.png',dpi=110); plt.close(fig)
print("OK", flow[0], round(flow[-1],3), round(capn[-1],3))
