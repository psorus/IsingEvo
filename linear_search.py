from evalu import Evaluator
import numpy as np
from plt import *
import sys

fn=sys.argv[0]
fn=fn[:fn.find(".")]

from const import init_range


def linear_search(call,n=init_range):
    best=0
    score=None

    for i in range(n):
        ac=call(i,score)
        if score is None or ac<score:
            score=ac
            best=i
    return best

if __name__=="__main__":
    ev=Evaluator(linear_search)
    ev.run()
    ev.plot()
    plt.show()
    ev.print_stats()
    
    ev.save(f"results/{fn}.json")
    
    
    
