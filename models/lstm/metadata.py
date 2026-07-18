import json
def save_metadata(path,sequence_length,features,params):
    json.dump({"sequence_length":sequence_length,"features":features,"parameters":params},open(path,"w"),indent=2)
