import numpy as np
from plt import *

from evalu import thefunc
from const import init_range

fact=1
x=np.arange(0,init_range//fact)
y=np.array([thefunc(xx) for xx in x])

def tripleiter(q):
    last=[]
    for qq in q:
        last.append(qq)
        if len(last)>3:
            last=last[1:]
        if len(last)==3:
            yield last

minima=0
minx,miny=[],[]
for (_,a),(i,b),(_,c) in tripleiter(enumerate(y)):
    if a>b and c>b:
        minima+=1
        minx.append(i)
        miny.append(b)

minx,miny=np.array(minx),np.array(miny)

ordered=minx[np.argsort(miny)]

print(minima)


plt.figure(figsize=(10,6))

col="darkgreen"
col="darkblue"

bins=30
bins=20

plt.hist(miny,bins=bins,color=col,alpha=0.5)#,edgecolor="darkgreen",linewidth=5)
plt.hist(miny,bins=bins,color=col,edgecolor=col,linewidth=5,fill=False)

xt=[0,0.001,0.002,0.003,0.004,0.005]
xl=[r"$0\%$",r"$0.1\%$",r"$0.2\%$",r"$0.3\%$",r"$0.4\%$",r"$0.5\%$"]
plt.xticks(xt,xl)



plt.xlabel("Function value at local minima")
plt.ylabel("Number of occurences")

plt.savefig("imgs/dist.png",format="png",dpi=600)
plt.savefig("imgs/dist.pdf",format="pdf")
plt.savefig("last.png")

plt.show()

exit()

plt.plot(minx,miny)
plt.show()

print(ordered[:10])

print(np.sum(y<1.7e-5))


