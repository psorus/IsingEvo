from evalu import Evaluator
import numpy as np
from plt import *
import sys

fn=sys.argv[0]
fn=fn[:fn.find(".")]

from const import init_range,evaluations


def mutation_search(call,n=evaluations,maximum=init_range):
    curr=np.random.randint(0,maximum)
    score=call(curr,None)

    def mutate(value):
        value=np.random.normal(value,100,1)[0]
        value=np.abs(value)
        if value>maximum:
            value=2*maximum-value
        return value


    for j in range(n):
        newone=mutate(curr)
        newscore=call(newone,score)

        if score is None or newscore<score:
            score=newscore
            curr=newone
    return curr


if __name__=="__main__":
    ev=Evaluator(mutation_search)
    ev.run()
    ev.plot()
    plt.show()
    ev.print_stats()
    
    ev.save(f"results/{fn}.json")
    
    
    
