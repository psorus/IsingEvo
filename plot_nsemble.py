import numpy as np
from plt import *
import os
import sys

from evalu import Evaluator

from tqdm import tqdm

plt.figure(figsize=(10,6))

methods={"huge_phase":"Ising 50x50",
         "random_search":"Random Search",
         "large_phase":"Ising 30x30",
         "phase_search":"Ising 10x10",
         "ising_search":"Ising 900",
         #"local_search":"",#like Ising 900, only taking the better value
         "mutation_search":"Mutation",#random value, close. Either better, or ignore
         "mixture_search":"Mixture",#mix two values, close. Either better, or ignore
         "2d_search":"Cellular Evolution",#update but locally
         "annealing_search":"Simulated Annealing"}

def calculate(task):
    ev=Evaluator(f"numpy:npz/{task}.json.npz")
    
    want_to=[84822,35499,49322,70999,13822,98645,21676,63145,57176,27645]
    
    def test_one(lis):
        return np.sum([zw in lis for zw in want_to])
    
    def test(ev):
        lis=[test_one(lis) for lis in ev.mtries]
        return np.mean(lis),np.std(lis)/np.sqrt(len(lis))
    
    return test(ev)    


x=list(methods.keys())
y=[calculate(zw) for zw in tqdm(x)]
err=np.array([zw[1] for zw in y])
y=np.array([zw[0] for zw in y])
x=np.array([methods[zw] for zw in x])

col="orange"
plt.bar(x,y,color=col,alpha=0.7)
plt.bar(x,y,color=col,fill=False,edgecolor="maroon",linewidth=1.5,alpha=0.7)

for i,nam in enumerate(x):
    #nam=nam.replace(" based","")
    if y[i]>5:
        va="top"
        delta=-0.10
        color="brown"
    else:
        va="bottom"
        delta=+0.10
        color="black"
    plt.annotate(nam,xy=(i,(y[i]+delta)),xytext=(i,(y[i]+delta)),ha="center",va=va,rotation=90,color=color)
    print(nam,y[i])



#plt.xticks(rotation=90)
plt.xticks([])
plt.ylabel("Best solutions found")
plt.ylim(0,8)

plt.tight_layout()

plt.savefig("imgs/nsemble.png",format="png",dpi=600)
plt.savefig("imgs/nsemble.pdf",format="pdf")
plt.savefig("last.png")


plt.show()


            
