import numpy as np
from plt import *
import os
from const import init_range

temps=[1,10,100,1000,10000]
#temps=[float(t) for t in temps]

addon=""
addon="h"
addon="l"

files={t:[f"matrices_{float(t)}{addon}.npz",f"matrices_{int(t)}{addon}.npz"] for t in temps}
files={key:val[0] if os.path.exists(val[0]) else val[1] for key,val in files.items()}
print(files)

qs={t:np.load(fn)["q"] for t,fn in files.items()}

plt.figure(figsize=(10,8))


def get_one(t,frac):
    q=qs[t]
    q=q[int(len(q)*frac)-1]
    return q

def plot_one(t,frac,i,j):
    q=get_one(t,frac)
    epoch=int(frac*1e5)
    plt.imshow(q,vmin=0,vmax=init_range)
    print(np.std(q)/1e5)
    plt.axis("off")
    plt.xlabel("tom")
    #plt.title("%d, %d"%(t,epoch))
    if j==0:
        plt.title(r"$\beta=%d$"%(t))

fracs=[0.05,0.3,0.6,1.0]
lis=[]
for i,temp in enumerate(temps):
    for j,frac in enumerate(fracs):
        plt.subplot(len(fracs),len(temps),j*len(temps)+i+1)
        plot_one(temp,frac,i,j)

for i in range(len(fracs)):
    plt.subplot(len(fracs),len(temps),i*len(temps)+1)
    plt.text(-0.2,0.5,r"$t=%d$"%(100000*fracs[i]),rotation=90,transform=plt.gca().transAxes,va="center",ha="left")


plt.tight_layout()

plt.savefig("imgs/phase.png",format="png",dpi=600)
plt.savefig("imgs/phase.pdf",format="pdf")
plt.savefig("last.png")

plt.show()







