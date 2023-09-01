from evalu import Evaluator
import numpy as np
from plt import *
import sys

fn=sys.argv[0]
fn=fn[:fn.find(".")]

from const import init_range,evaluations

from phase_search import phase_search,matrices


if __name__=="__main__":
    debug=False
    if "--d" in sys.argv:
        debug=True
        sys.argv.remove("--d")
        print("entering debug mode")
    temp=100
    if len(sys.argv)>1:
        temp=float(sys.argv[1])
    ev=Evaluator(phase_search,repeat=1 if debug else 100)
    ev.run(temp=temp,dx=30,dy=30)
    ev.plot()
    plt.show()
    ev.print_stats()
    
    if not debug:ev.save(f"results/{fn}.json")

    np.savez_compressed(f"matrices_{temp}l.npz",q=matrices)
    
    
    
