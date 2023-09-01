from evalu import Evaluator
import numpy as np
from plt import *
import sys

fn=sys.argv[0]
fn=fn[:fn.find(".")]

from const import init_range,evaluations

from phase_search import phase_search,matrices


if __name__=="__main__":
    temp=100
    if len(sys.argv)>1:
        temp=float(sys.argv[1])
    ev=Evaluator(phase_search,repeat=3)
    ev.run(temp=temp,dx=50,dy=50,n=evaluations*50,saveall=False)
    ev.plot()
    plt.show()
    ev.print_stats()
    
    ev.save(f"results/{fn}.json")
    print(len(matrices))

    np.savez(f"matrices_{temp}f.npz",q=matrices)
    
    
    
