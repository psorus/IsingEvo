import numpy as np
from plt import *

import json

from tqdm import tqdm


def thefunc(x):
    x=np.round(x)
    x+=1
    x/=100
    return np.abs(np.sin(x))

def debug_types(q):
    if type(q) is dict:
        return {key:debug_types(val) for key,val in q.items()}
    elif type(q) is list:
        return type(q[0])
    else:
        return type(q)



class Evaluator(object):
    def __init__(self, func, repeat=100):
        if callable(func):
            self.func = func
            self.evals=[]
            self.tries=[]
            self.sol=None
            self.mevals=[]
            self.mtries=[]
            self.msol=[]
        elif isinstance(func,dict):
            self.init_from_dic(func)
            self.func = lambda x:-1
        elif isinstance(func,str):
            if func.startswith("numpy:"):
                self.load_numpy(func[6:])
                self.func = lambda x:-1
            else:
                self.load(func)
                self.func = lambda x:-1
        self.repeat=repeat

    def to_dic(self):
        return {"evals":self.mevals,"tries":self.mtries,"sol":self.msol,"stats":self.gen_stats()}

    def init_from_dic(self,dic):
        self.mevals=dic["evals"]
        self.msol=dic["sol"]
        self.mtries=dic["tries"]

    def save(self,filename):
        #print(debug_types(self.to_dic()))
        #exit()
        with open(filename,"w") as f:
            json.dump(self.to_dic(),f,indent=2)

    def load(self,filename):
        with open(filename,"r") as f:
            dic=json.load(f)
        self.init_from_dic(dic)

    def go_numpy(self,filename):
        np.savez_compressed(filename, evals=np.array(self.mevals),tries=np.array(self.mtries),sol=np.array(self.msol))

    def load_numpy(self,filename):
        f=np.load(filename,allow_pickle=True)
        self.mevals=f["evals"]
        self.mtries=f["tries"]
        self.msol=f["sol"]



    def call(self,x, curr):
        #print("calling",x,curr,type(x),type(curr),type(float(x)))
        self.tries.append(float(x))
        if not curr is None:
            self.evals.append(float(curr))
        return float(thefunc(x))

    def get_evals(self):
        return self.evals

    def run(self, *args, **kwargs):
        def one_run():
            self.evals=[]
            self.tries=[]
            self.sol=None
            self.sol=self.func(self.call,*args, **kwargs)
            self.mevals.append(self.evals)
            self.mtries.append(self.tries)
            self.msol.append(self.sol)
        ret=[one_run() for i in tqdm(range(self.repeat),total=self.repeat)]
        return ret

    def llfit(self,which=-1):
        x=np.arange(1,1+len(self.mevals[which]))
        y=np.array(self.mevals[which])
        x=np.log(x)
        y=np.log(y)
        power, intercept = np.polyfit(x, y, 1)
        return power, intercept

    def combine_fit(self):
        powers,intercepts=[],[]
        for i in range(len(self.msol)):
            power,intercept=self.llfit(i)
            powers.append(power)
            intercepts.append(intercept)
        return np.mean(powers),np.mean(intercepts)

    def mean_performance(self):
        return np.mean(self.mevals,axis=0)

    def plot_mean_performance(self,*args,**kwargs):
        x=np.arange(1,1+len(self.mevals[0]))
        y=self.mean_performance()
        plt.plot(x,y,*args,**kwargs)

    def log_mean_performance(self):
        return np.exp(np.mean(np.log(self.mevals),axis=0))

    def plot(self):
        for i in range(len(self.mevals)):
            x=np.arange(1,1+len(self.mevals[i]))
            y=np.array(self.mevals[i])
            plt.plot(x,y,label=None if i else "measurements",alpha=0.2,color="black")
        self.plot_mean_performance(label="mean",color="red")
        lm=self.log_mean_performance()
        plt.plot(x,lm,label="log mean",color="blue")
        #power,intercept=self.combine_fit()
        #print(power,intercept)
        #pred=np.exp(intercept)*x**power
        #plt.plot(x,pred,label="fit",color="darkred")
        plt.legend(loc="upper right")
        plt.yscale("log")
        plt.xscale("log")

    def plot_tries(self,which=-1):
        plt.plot(np.arange(1,1+len(self.mtries[which])),self.mtries[-1],".")

    def solved(self):
        return len(self.msol)==self.repeat

    def tries_till_best(self,which):
        x=np.arange(1,1+len(self.mevals[which]))
        y=np.array(self.mevals[which])
        goal=np.min(y)
        return int(x[y<=goal][0])


    def gen_stats(self):
        assert self.solved(), "run the task first!"
        dic={}

        dic["Solution"]=[float(zw) for zw in self.msol]
        dic["Quality"]=[float(self.call(zw,None)) for zw in self.msol]
        dic["Pi multiplier"]=[float(zw/(100*np.pi)) for zw in self.msol]
        dic["Time till best"]=[self.tries_till_best(i) for i in range(len(self.msol))]
        dic["power"],dic["intercept"]=[],[]
        for a,b in [self.llfit(i) for i in range(len(self.msol))]:
            dic["power"].append(float(a))
            dic["intercept"].append(float(b))

        return dic


    def print_stats(self):
        assert self.solved(), "solve the task first!"
        [print(f"{key}: {val}") for key,val in self.gen_stats().items()]
        #print("Solution: ", self.sol)
        #print("Quality: ", self.call(self.sol,None))
        #print("Pi multiplier: ", self.sol/(100*np.pi))


