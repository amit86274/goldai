
import json

def save_metadata(path,features,params):
    with open(path,"w") as f:
        json.dump({
            "features":features,
            "params":params
        },f,indent=2)
