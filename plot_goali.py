import numpy as np
from plt import *
import os
import json



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

dic={key:loadone(files[key]) for key in files}


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

x=np.array(list(dic.keys()))
y=np.array([measurable(dic[key]) for key in x])

order=np.argsort(y)
x=x[order]
y=y[order]

plt.plot(x,y,"o")
plt.xticks(rotation=90)

#plt.axhline(0,linestyle="--",color="black")
#plt.axhline(1,linestyle="--",color="black")

plt.yscale("log")

plt.show()






