import json
import requests

djson = {"parameter": [{"name": "VERSION", "value": "123"}, {"name": "Yes", "value": "No"}]}

# r = requests.post("{https://jenkins_url_replaced:port}/job/{jenkins_job}/build?json={}".format(json.dumps(djson)),
#                   auth=('{auth_username}', '{auth_password}'))


r = requests.post("{https://jenkins_url_replaced:port}/job/{jenkins_job}/build",params="json={}".format(json.dumps(djson)),
                  auth=('{auth_username}', '{auth_password}'))


print(djson)
print(r.status_code)