
import json

def read_json(filename):
    with open(filename, 'r') as f:
        content = json.load(f)
    return content

