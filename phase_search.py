from evalu import Evaluator
import numpy as np
from plt import *
import sys

fn=sys.argv[0]
fn=fn[:fn.find(".")]

from const import init_range,evaluations

from tqdm import tqdm

def xy(i,dx,dy):
    return i%dx,i//dx
def I(x,y,dx,dy):
    return x+y*dx

def find_neighbors(i,dx,dy):
    #infinite border conditions
    x,y=xy(i,dx,dy)
    neighbors=[]
    if x>0:
        neighbors.append(i-1)
    else:
        neighbors.append(I(dx-1,y,dx,dy))
    if x<dx-1:
        neighbors.append(i+1)
    else:
        neighbors.append(I(0,y,dx,dy))
    if y>0:
        neighbors.append(i-dx)
    else:
        neighbors.append(I(x,dy-1,dx,dy))
    if y<dy-1:
        neighbors.append(i+dx)
    else:
        neighbors.append(I(x,0,dx,dy))
    return neighbors

def random_neighbor(i,dx,dy):
    return np.random.choice(find_neighbors(i,dx,dy))

def list_to_matrix(lis,dx,dy):
    assert len(lis)==dx*dy
    return np.array(lis).reshape((dx,dy))

matrices=[]

def phase_search(call,n=evaluations,maximum=init_range,temp=100,dx=10,dy=10,keepanyway=0.1,saveall=True):
    global matrices
    parallel=dx*dy

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
        if np.random.uniform(0,1)<np.exp(temp*(score[i]-newscore)):
        #if newscore<score[i]:
            library[i]=newval
            score[i]=newscore
            if newscore<bestscore:
                bestscore=newscore
                bestval=newval
        return bestscore,bestval
    def update_mutate(i,bestscore,bestval):
        newval=np.random.normal(library[i],100,1)[0]
        newscore=call(newval,bestscore)
        if np.random.uniform(0,1)<np.exp(temp*(score[i]-newscore)):
        #if newscore<score[i]:
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
        i=np.random.randint(0,parallel)
        j=random_neighbor(i,dx,dy)
        return update(i,j,bestscore,bestval)

    for i in tqdm(range(n),total=n):
        bestscore,bestval=update_one(bestscore,bestval)
        if saveall or not i%(dx*dy):
             matrices.append(list_to_matrix(library,dx,dy))

    return int(np.round(bestval))

if __name__=="__main__":
    temp=100
    if len(sys.argv)>1:
        temp=float(sys.argv[1])
    ev=Evaluator(phase_search)
    ev.run(temp=temp)
    ev.plot()
    plt.show()
    ev.print_stats()
    
    ev.save(f"results/{fn}.json")

    np.savez_compressed(f"matrices_{temp}.npz",q=matrices)
    
    
    
