
import json
def save_report(stats,path):
    with open(path,"w") as f:
        json.dump(stats,f,indent=2)
