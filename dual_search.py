from evalu import Evaluator
import numpy as np
from plt import *
import sys

fn=sys.argv[0]
fn=fn[:fn.find(".")]

from const import init_range,evaluations


def dual_search(call,n=evaluations,maximum=init_range,parallel=100,keepanyway=0.1):

    library=np.random.randint(0,maximum,parallel)
    score=[]
    bestscore=None
    for value in library:
        ac=call(value,bestscore)
        score.append(ac)
        if bestscore is None or ac<bestscore:
            bestscore=ac
    score=np.array(score)

    def update_mix(bestscore):
        i,j=np.random.randint(0,parallel,2)
        maxtries=100
        while i==j or score[i]==bestscore:
            i=np.random.randint(0,parallel)
            maxtries-=1
            if maxtries==0:
                return bestscore
        newval=(library[i]+library[j])//2
        newscore=call(newval,bestscore)
        if newscore<score[i]:
            library[i]=newval
            score[i]=newscore
            if newscore<bestscore:
                bestscore=newscore
        elif np.random.uniform(0,1)<keepanyway:
            library[i]=newval
            score[i]=newscore
        return bestscore
    def update_mutate(bestscore):
        i=np.random.randint(0,parallel)
        newval=np.random.normal(library[i],100,1)[0]
        newscore=call(newval,bestscore)
        if newscore<score[i]:
            library[i]=newval
            score[i]=newscore
            if newscore<bestscore:
                bestscore=newscore
        return bestscore
    def update(bestscore):
        if np.random.uniform(0,1)<0.5:
            return update_mix(bestscore)
        else:
            return update_mutate(bestscore)

    for i in range(n):
        bestscore=update(bestscore)

    return int(library[np.argmin(score)])

if __name__=="__main__":
    ev=Evaluator(dual_search)
    ev.run()
    #ev.plot()
    #plt.show()
    ev.print_stats()
    
    ev.save(f"results/{fn}.json")
    
    
    
