
import json

def to_json(data):
    return json.dumps(data)

def from_json(text):
    return json.loads(text)
