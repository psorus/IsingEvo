from evalu import Evaluator
import numpy as np
from plt import *
import sys

fn=sys.argv[0]
fn=fn[:fn.find(".")]

from const import init_range,evaluations


def local_search(call,n=evaluations,maximum=init_range,parallel=900,keepanyway=0.1):

    library=np.random.randint(0,maximum,parallel)
    score=[]
    bestscore=None
    bestval=None
    for value in library:
        ac=call(value,bestscore)
        score.append(ac)
        if bestscore is None or ac<bestscore:
            bestscore=ac
            bestval=value
    score=np.array(score)

    def update_mix(i,j,bestscore,bestval):
        newval=(library[i]+library[j])//2
        newscore=call(newval,bestscore)
        if newscore<score[i]:
            library[i]=newval
            score[i]=newscore
            if newscore<bestscore:
                bestscore=newscore
                bestval=newval
        elif np.random.uniform(0,1)<keepanyway:
            library[i]=newval
            score[i]=newscore
        return bestscore,bestval
    def update_mutate(i,bestscore,bestval):
        newval=np.random.normal(library[i],100,1)[0]
        newscore=call(newval,bestscore)
        if newscore<score[i]:
            library[i]=newval
            score[i]=newscore
            if newscore<bestscore:
                bestscore=newscore
                bestval=newval
        return bestscore,bestval
    def update(i,j,bestscore,bestval):
        if np.random.uniform(0,1)<0.5:
            i,j=j,i
        if np.random.uniform(0,1)<0.5:
            return update_mix(i,j,bestscore,bestval)
        else:
            return update_mutate(i,bestscore,bestval)

    def update_one(bestscore,bestval):
        i=np.random.randint(0,parallel-1)
        j=i+1
        return update(i,j,bestscore,bestval)

    for i in range(n):
        bestscore,bestval=update_one(bestscore,bestval)

    return int(np.round(bestval))
    return int(library[np.argmin(score)])

if __name__=="__main__":
    ev=Evaluator(local_search)
    ev.run()
    ev.plot()
    plt.show()
    ev.print_stats()
    
    ev.save(f"results/{fn}.json")
    
    
    
