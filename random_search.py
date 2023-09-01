from evalu import Evaluator
import numpy as np
from plt import *
import sys

fn=sys.argv[0]
fn=fn[:fn.find(".")]

from const import init_range,evaluations


def random_search(call,n=evaluations,maximum=init_range):
    best=0
    score=None

    for j in range(n):
        i=np.random.randint(0,maximum)
        ac=call(i,score)
        if score is None or ac<score:
            score=ac
            best=i
    return best


if __name__=="__main__":
    ev=Evaluator(random_search)
    ev.run()
    ev.plot()
    plt.show()
    ev.print_stats()
    
    ev.save(f"results/{fn}.json")
    
    
    
