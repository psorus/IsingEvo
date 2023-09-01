import numpy as np
from plt import *
import sys

from const import init_range


task=1.0
if len(sys.argv)>1:
    task=float(sys.argv[1])

addon=""
if len(sys.argv)>2:
    addon=sys.argv[2]



fn=f"matr1ces_{task}{addon}.npz"
try:
    f=np.load(fn)
except:
    fn=f"matr1ces_{int(task)}{addon}.npz"
    f=np.load(fn)

q=f["q"]

#modulo=100
modulo=np.prod(q.shape[1:])

modulo=1
modulo=5

for i,qq in enumerate(q):
    if not i%modulo:
        plt.close()
        plt.title(f"Update step {i}")
        qq=np.reshape(qq,[int(np.sqrt(qq.shape[0]))]*2)
        plt.imshow(qq,vmin=0,vmax=init_range)
        plt.show()






