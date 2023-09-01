import numpy as np
from plt import *
from matplotlib import patches as pat


tasks=[]
labels=[]

for zw in [1,10,100,1000,10000]:
    tasks.append(f"comp{zw}")
    labels.append(r"$\beta=%d$"%zw)


alphas=[1.0 for zw in labels]


colors=["maroon","red","orange","blue","green"]


#tasks.append("annealing_search")
#labels.append("Annealing")
#colors.append("purple")
#alphas.append(1.0)


tasks={labl:f"numpy:npz/{zw}.json.npz" for labl,zw in zip(labels,tasks)}





fig=plt.figure(figsize=(10,8))


from evalu import Evaluator
from tqdm import tqdm

evs={fn:Evaluator(fn) for fn in tqdm(tasks.values())}

def main_lines(xmax=1.0,maxy=1):
    for (nam,fn),color,alpha in zip(tasks.items(),colors,alphas):
        ev=evs[fn]
        y=ev.mean_performance()
        x=np.arange(1,len(y)+1)
        which=np.where(y<maxy)
        x=x[which]
        y=y[which]
        plt.plot(x,y,color=color,alpha=alpha,lw=3,label=nam)
        #ev.plot_mean_performance(label=nam,color=color,alpha=alpha,lw=3)
    plt.axhline(1.64692442e-05,color="black",lw=1,alpha=0.5,ls="dotted",xmax=xmax)
    plt.axhline(3.01443534e-05,color="black",lw=1,alpha=0.5,ls="dashed",xmax=xmax)
    plt.axhline(4.66135975e-05,color="black",lw=1,alpha=0.5,ls="dashdot",label="lowest solutions",xmax=xmax)

main_lines()

x=np.arange(1,1e5)
#make theory
#first: 1/10^5
#second: 1-(1-(1/10^5))^2
#prob=(1-1e-5)**x
#plt.plot(x,prob,label="theory")


plt.xscale("log")
plt.yscale("log")
plt.xlabel("Function Evaluations")
plt.ylabel("Solution Found")

#plt.xlim(left=30)
#plt.ylim(top=1e-1)

plt.legend(loc="lower left",frameon=True,framealpha=1.0)
ax=plt.gca()

l, b, h, w = .6, .5, .35, .27
ax2 = fig.add_axes([l, b, w, h])
#plt.plot([1, 4, 6, 2, 1, 5, 2], color='green', lw=3, label="inside plot")
main_lines(0.97,9.7e-5)
plt.xscale("log")
plt.yscale("log")

plt.xlim(left=10000,right=110000)
plt.ylim(top=1e-4,bottom=2e-5)
plt.axis("off")
ax2._frameon=True
plt.yticks([],color="red")
ax2.set_yticks([])
plt.xticks([])

rect=pat.Rectangle((10000,2e-5),9.5e4,8e-5,fill=False,color="black",lw=1)
ax.add_patch(rect)

rl,rb,rh,rw=7.3e-3,1.3e3,1.5,1e5

rect3=pat.Rectangle((rb,rl),rw,rh,fill=False,color="black",lw=1)
ax.add_patch(rect3)

rect2=pat.Rectangle((10000,2e-5),9e4,8e-5,fill=False,color="red",lw=2,alpha=0.5)
#ax2.add_patch(rect2)

ax.plot([1e4,rb],[1e-4,rl],"--",color="black",lw=1)
ax.plot([1.05e5,rb+rw],[1e-4,rl],"--",color="black",lw=1)

#draw square lbhw
#ax2.plot([1,1,1e5,1e5,1],[1e-4,2e-5,2e-5,1e-4,1e-4],color="red",lw=3)


plt.savefig("imgs/emperature.png",dpi=300,format="png")
plt.savefig("imgs/emperature.pdf",format="pdf")
plt.savefig("last.png")

plt.show()



