import numpy as np
from plt import *


def thefunc(x):
    x=np.round(x)
    x+=1
    x/=100
    return np.abs(np.sin(x))


evals=[]
def call(x, curr):
    if not curr is None:
        global evals
        evals.append(curr)
    return thefunc(x)


def linear_search(n=100000):
    best=0
    score=None

    for i in range(n):
        ac=call(i,score)
        if score is None or ac<score:
            score=ac
            best=i
    return best


sol=linear_search()
score=call(sol,None)
print("Solution: ",sol)
print("Score: ",score)
print("pi?: ",sol/(100*np.pi))

linfit=np.polyfit(np.log(range(1,1+len(evals))),np.log(evals),1)
power=linfit[0]
print("Power: ",power)
mult=linfit[1]
print("Mult: ",mult)

x=np.arange(1,len(evals)+1)
fit=np.exp(mult)*x**power

plt.plot(x,evals)
plt.plot(x,fit,label="fit")
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.show()


