import numpy as np
from plt import *

tasks=["huge_phase","large_phase","phase_search","random_search"]
labels=["Ising 50x50","Ising 30x30","Ising 10x10","Random Search"]

tasks={labl:f"numpy:npz/{zw}.json.npz" for labl,zw in zip(labels,tasks)}

from evalu import Evaluator
from tqdm import tqdm

for nam,fn in tqdm(tasks.items()):
    ev=Evaluator(fn)
    ev.plot_mean_performance(label=nam)

x=np.arange(1,1e5)
plt.plot(x,1/x,label="1/x")


plt.xscale("log")
plt.yscale("log")


plt.legend()
plt.show()



