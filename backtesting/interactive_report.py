
import json
def export_report(data,path):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=2)
