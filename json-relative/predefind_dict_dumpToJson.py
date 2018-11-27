import json

def dumpJsonData(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


jsonTemplate = {
    'META':{
        'PREFIX':'1'
    }
}

print(json.dumps(jsonTemplate))

jsonTemplate['META']['PREFIX'] = '2'

print(json.dumps(jsonTemplate))


dumpJsonData('test.json', json.dumps(jsonTemplate))