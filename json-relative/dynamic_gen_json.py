import json

data = {}
data['key'] = 'value'

## show result in console
json_data = json.dumps(data)
print(json_data)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
