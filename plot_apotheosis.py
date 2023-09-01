import numpy as np
from plt import *
import os
from const import init_range

from matplotlib import colors

f=np.load("apotheosis.npz")
q,f,t=f["q"],f["f"],f["t"]


plt.figure(figsize=(10,6))


plt.imshow(q,cmap="hot",vmin=0,vmax=0.25)
#plt.imshow(q,norm=colors.LogNorm(vmin=q.min(), vmax=q.max()),cmap="jet")
plt.colorbar(orientation="horizontal",location="top",label="Relative Standard Deviation of the population")

def convf(val):
    print(val)
    return r"$%d$".replace("%d",str(int(val*10)))


plt.xticks(list(range(len(f))),[convf(ff) for ff in f])
plt.yticks(list(range(len(t))),t)

plt.ylabel(r"$\beta$")
plt.xlabel(r"Function Evaluations / $10^{4}$")

plt.savefig("imgs/apotheosis.png",format="png",dpi=600)
plt.savefig("imgs/apotheosis.pdf",format="pdf")
plt.savefig("last.png")

plt.show()







