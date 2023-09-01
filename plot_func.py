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
print(ordered[:10])
print(np.sort(miny)[:10])

print(minima)

exerpt=[30,20000]
#x=x[exerpt[0]:exerpt[1]]
#y=y[exerpt[0]:exerpt[1]]

plt.figure(figsize=(10,4))


plt.plot(x,y)
plt.yscale('log')
plt.xscale('log')

plt.xlim(*exerpt)

plt.xlabel("Input")
plt.ylabel("Function Output")

yt=[1,1e-1,1e-2,1e-3,1e-4]
yl=[r"$1$",r"$10^{-1}$",r"$10^{-2}$",r"$10^{-3}$",r"$10^{-4}$"]
plt.yticks(yt,yl)

plt.ylim([5e-5,1.1])

lowest=0.1
lowx,lowy=[],[]
for xx,yy in zip(x,y): 
    if xx<exerpt[0]:
        continue
    if yy<lowest:
        lowest=yy
        lowx.append(xx)
        lowy.append(yy)

plt.plot(lowx,lowy,color='black',linestyle='dashed',alpha=0.2)



plt.savefig("imgs/func.png",format='png',dpi=600)
plt.savefig("imgs/func.pdf",format='pdf')
plt.savefig("last.png")

plt.show()

#plt.plot(minx,miny)
#plt.show()

#print(ordered[:10])

#print(np.sum(y<1.7e-5))


