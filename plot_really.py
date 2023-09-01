import numpy as np
from plt import *
import os
import json

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

fold="results"
fold="easy"

optimal_sol=1.7e-5

files=os.listdir(fold)
files={zw[:-5]:fold+"/"+zw for zw in files if zw.endswith(".json")}

def loadone(fn):
    with open(fn,"r") as f:
        data=json.load(f)["stats"]
    print(data.keys())
    return data

dic={key:loadone(files[key]) for key in methods}


def measurable1(dic):
    #how often does it find the optimal solution
    sol=dic["Quality"]
    sol=np.array(sol)
    return np.mean(sol<=optimal_sol)

def measurable2(dic):
    #assuming it does, how long does it take
    sol=dic["Quality"]
    sol=np.array(sol)
    dt=dic["Time till best"]
    dt=np.array(dt)
    return np.mean(dt[sol<=optimal_sol])

def measurable3(dic):
    #same as 2, but punish for not finding the optimal solution at all, by setting the time to the maximum
    sol=dic["Quality"]
    sol=np.array(sol)
    dt=dic["Time till best"]
    dt=np.array(dt)
    return np.mean(dt[sol<=optimal_sol])+100000*np.mean(sol>optimal_sol)

def measurable4(dic):
    #I mean we have the ll fit, why not plot it
    sol=dic["power"]
    sol=np.array(sol)
    sol=sol[np.logical_not(np.isnan(sol))]
    return np.mean(sol)

def measurable5(dic):
    #I mean we have the ll fit, why not plot it
    sol=dic["Quality"]
    sol=np.array(sol)
    sol=sol[np.logical_not(np.isnan(sol))]
    return np.mean(sol)

measurable=measurable5

x=list(dic.keys())
y=np.array([measurable(dic[key]) for key in x])
x=np.array([methods[key] for key in x])

order=np.argsort(y)
x=x[order]
y=y[order]

plt.bar(x,y)

for i,nam in enumerate(x):
    #nam=nam.replace(" based","")
    if i>6:
        va="top"
        delta=-0.10
        color="white"
    else:
        va="bottom"
        delta=+0.10
        color="black"
    plt.annotate(nam,xy=(i,(y[i]*(1+delta))),xytext=(i,(y[i]*(1+delta))),ha="center",va=va,rotation=90,color=color)
    print(nam,y[i])

plt.xticks([])

plt.ylabel("Average Quality found")

#plt.axhline(0,linestyle="--",color="black")
#plt.axhline(1,linestyle="--",color="black")

plt.yscale("log")


plt.axhline(2.5e-3,linestyle="--",color="red",label="local minima")
plt.axhline(1.64e-5,linestyle="--",color="green",label="global minima")
plt.ylim(bottom=1e-5)

plt.legend(loc="upper left",frameon=True)

plt.savefig("imgs/really.png",format="png",dpi=600)
plt.savefig("imgs/really.pdf",format="pdf")
plt.savefig("last.png")


plt.show()






