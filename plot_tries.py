import numpy as np
from plt import *
import sys

task="linear_search"
if len(sys.argv)>1:
    task=sys.argv[1]
if task.endswith(".py"):task=task[:-3]

frac=1.0
if len(sys.argv)>2:
    frac=float(sys.argv[2])

from evalu import Evaluator

ev=Evaluator(f"results/{task}.json")
#ev.tries=[zw for zw in ev.tries if np.random.uniform()<frac]
ev.plot_tries()
plt.axhline(84822,color="red")
plt.axhline(35499,color="red",alpha=0.5)
#plt.axhline(ev.sol,color="green",alpha=0.5)
plt.show()


