import numpy as np
from plt import *
import os
import json
from tqdm import tqdm

import sys

files=os.listdir("results")
files={zw[:-5]:"results/"+zw for zw in files if zw.endswith(".json")}

if len(sys.argv)>1:
    files={key:val for key,val in files.items() if sys.argv[1] in key}

def loadone(fn):
    with open(fn,"r") as f:
        data=json.load(f)["stats"]
    return data

for file in tqdm(files):
    with open(f"easy/{file}.json","w") as f:
        f.write(json.dumps({"stats":loadone(files[file])},indent=2))







