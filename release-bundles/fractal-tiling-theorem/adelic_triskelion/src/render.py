import sys, os; sys.path.insert(0,os.path.dirname(__file__))
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import geometry as G
OUT=os.path.join(os.path.dirname(__file__),"..","outputs")
pa=G.prime_arm(200); ar=G.archimedean_arm(); sc=G.scale_arm(); ax=G.witness_axis()
DARK="#0a0d14"
# ---- 2D top-down ----
fig,axp=plt.subplots(figsize=(8,8)); fig.patch.set_facecolor(DARK); axp.set_facecolor(DARK)
axp.plot(0,0,marker='+',ms=18,color='white',mew=2)            # witness axis (top view = point)
# arm B ribbon (archimedean) — opacity by Gaussian
pts=np.column_stack([ar['x'],ar['y']]); segs=np.stack([pts[:-1],pts[1:]],axis=1)
lc=LineCollection(segs,colors=[(0.4,0.8,1,min(1,0.15+0.85*p)) for p in ar['profile'][:-1]],linewidths=3)
axp.add_collection(lc)
# arm C ribbon (scale) + mirror chords u<->-u
axp.plot(sc['x'],sc['y'],color='#c08bff',lw=1.6,alpha=0.8)
n=len(sc['u'])
for i in range(0,n//2,18):
    j=n-1-i
    axp.plot([sc['x'][i],sc['x'][j]],[sc['y'][i],sc['y'][j]],color='#c08bff',lw=0.5,alpha=0.25)
# arm A prime nodes
axp.scatter([d['x'] for d in pa],[d['y'] for d in pa],s=[8+9*d['size'] for d in pa],
            c='#ffd27f',edgecolors='#7a5b1f',linewidths=0.4,zorder=5)
for d in pa:
    if d['p'] in (2,3,5,7,11,13): axp.annotate(str(d['p']),(d['x'],d['y']),color='#ffe9b0',fontsize=8,zorder=6)
axp.set_xlim(-3,3);axp.set_ylim(-3,3);axp.set_aspect('equal');axp.axis('off')
axp.set_title("The Adelic Triskelion (top view)\nfinite p-adic • archimedean Γ • scale/involution — around Re(s)=1/2",
              color='white',fontsize=11)
fig.text(0.5,0.02,"diagram of the completed local-global architecture — NOT a proof of RH",
         ha='center',color='#888',fontsize=8)
fig.savefig(os.path.join(OUT,"adelic_triskelion_2d.png"),dpi=130,facecolor=DARK); plt.close(fig)
# ---- 3D ----
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure(figsize=(9,9)); fig.patch.set_facecolor(DARK)
a3=fig.add_subplot(111,projection='3d'); a3.set_facecolor(DARK)
a3.plot(ax['x'],ax['y'],ax['z'],color='white',lw=2)                 # witness axis
a3.scatter([d['x'] for d in pa],[d['y'] for d in pa],[d['z'] for d in pa],
           s=[6+7*d['size'] for d in pa],c='#ffd27f',depthshade=True)
# arm B coloured by Gaussian profile
a3.scatter(ar['x'],ar['y'],ar['z'],c=ar['profile'],cmap='cool',s=6)
a3.plot(sc['x'],sc['y'],sc['z'],color='#c08bff',lw=1.4,alpha=0.85)
for i in range(0,len(sc['u'])//2,28):
    j=len(sc['u'])-1-i
    a3.plot([sc['x'][i],sc['x'][j]],[sc['y'][i],sc['y'][j]],[sc['z'][i],sc['z'][j]],color='#c08bff',lw=0.4,alpha=0.3)
a3.set_axis_off(); a3.set_title("The Adelic Triskelion (3D helical scale geometry)\nNOT a proof of RH",color='white')
fig.savefig(os.path.join(OUT,"adelic_triskelion_3d.png"),dpi=130,facecolor=DARK); plt.close(fig)
print("[render] 2d + 3d PNG written")
# ---- interactive Plotly ----
try:
    import plotly.graph_objects as go
    f=go.Figure()
    f.add_trace(go.Scatter3d(x=ax['x'],y=ax['y'],z=ax['z'],mode='lines',line=dict(color='white',width=6),name='Re(s)=1/2 axis'))
    f.add_trace(go.Scatter3d(x=[d['x'] for d in pa],y=[d['y'] for d in pa],z=[d['z'] for d in pa],
        mode='markers',marker=dict(size=[3+2*d['size'] for d in pa],color='#ffd27f'),
        text=[f"p={d['p']}" for d in pa],name='finite p-adic places'))
    f.add_trace(go.Scatter3d(x=ar['x'],y=ar['y'],z=ar['z'],mode='markers',
        marker=dict(size=3,color=ar['profile'],colorscale='ice'),name='archimedean Γ completion'))
    f.add_trace(go.Scatter3d(x=sc['x'],y=sc['y'],z=sc['z'],mode='lines',line=dict(color='#c08bff',width=4),name='scale action / involution'))
    f.update_layout(template='plotly_dark',title="The Adelic Triskelion — completed local-global architecture (NOT a proof of RH)")
    f.write_html(os.path.join(OUT,"adelic_triskelion_interactive.html"))
    print("[render] interactive HTML written")
except Exception as e:
    print("[render] plotly skipped:", e)
