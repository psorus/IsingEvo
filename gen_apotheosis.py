import numpy as np
from plt import *
import os
from const import init_range
from tqdm import tqdm


temps=[1,3,10,30,100,300,1000,3000,10000,30000]
temps=[1,10,100,1000,10000]
#temps=[float(t) for t in temps]

addon=""
#addon="h"
addon="l"

files={t:[f"matrices_{float(t)}{addon}.npz",f"matrices_{int(t)}{addon}.npz"] for t in temps}
#files={t:[f"matr1ces_{float(t)}{addon}.npz",f"matr1ces_{int(t)}{addon}.npz"] for t in temps}
files={key:val[0] if os.path.exists(val[0]) else val[1] for key,val in files.items()}
print(files)

qs={t:np.load(fn)["q"] for t,fn in files.items()}

def metric(q):
    return np.std(q)/init_range
#def metric(q):
#    d1=np.mean(np.abs(q-np.roll(q,1,axis=0)))
#    d2=np.mean(np.abs(q-np.roll(q,1,axis=1)))
#    d=np.mean([d1,d2])
#    return d/init_range


def get_one(t,frac):
    q=qs[t]
    q=q[int(len(q)*frac)-1]
    return q

def plot_one(t,frac):
    q=get_one(t,frac)
    epoch=int(frac*1e5)
    return metric(q)
    return np.std(q)/init_range

fracs=[0.05,0.3,0.6,1.0]
fracs=[0.05*zw for zw in list(range(1,21))]
fracs=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
mat=[]
for i,temp in enumerate(tqdm(temps)):
    zw=[]
    for j,frac in enumerate(fracs):
        zw.append(plot_one(temp,frac))
    mat.append(zw)
mat=np.array(mat)

np.savez_compressed("apotheosis",q=mat,f=fracs,t=temps)







