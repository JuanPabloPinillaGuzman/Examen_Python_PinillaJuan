import json

myDatabase = "data/campustask.json"

def rF():
    try:
        with open(myDatabase, "r") as rf:
            return json.load(rf)
    except FileNotFoundError:
        return{}

def wF(data):
    with open(myDatabase,"w") as wf:
        json.dump(data,wf,indent=4)
    

        