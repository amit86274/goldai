
import json
def save_metadata(path,sequence_length,features,params):
    with open(path,"w") as f:
        json.dump({"sequence_length":sequence_length,
                   "features":features,
                   "parameters":params},f,indent=2)
