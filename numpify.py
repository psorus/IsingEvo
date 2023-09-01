import numpy as np
import os
from plt import *
import sys

from evalu import Evaluator

from tqdm import tqdm

fold="results/"
putin="npz/"
files=os.listdir(fold)
files={zw[:-5]:fold+"/"+zw for zw in files if zw.endswith(".json")}


if len(sys.argv)>1:
    files={key:val for key,val in files.items() if sys.argv[1] in key}



for nam,fn in tqdm(files.items()):
    print(nam)
    ev=Evaluator(fn)
    ev.go_numpy(fn.replace(fold,putin))


