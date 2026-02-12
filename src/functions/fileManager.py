import json

def openJson(path):
    with open(path) as data:
        d = json.load(data)
        return d

def saveData(path, data):
    file = open(path, 'w')
    file.write(json.dumps(data))
    file.close()

