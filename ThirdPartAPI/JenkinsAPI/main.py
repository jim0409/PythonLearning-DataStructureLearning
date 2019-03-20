import json
import requests

jenkins_url = "https://sample.jenkins.root.com:sampleport"
job_name = "/job/test/build/"
URL = jenkins_url + job_name
user_mail = 'sampleuser@sample.mail.com'
# https://stackoverflow.com/questions/45466090/how-to-get-the-api-token-for-jenkins
jenkins_token = 'test&jenkins&token'


# hereby, the jenkins job do have parameters with {"VERSION":"123", "Yes":"No"}
djson = {"parameter": [{"name": "VERSION", "value": "123"}, {"name": "Yes", "value": "No"}]}


r = requests.post( URL , params="json={}".format(json.dumps(djson)),
                  auth=(user_mail, jenkins_token))

print(djson)
print(r.status_code)
