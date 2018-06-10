import boto3


class MyModel(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def save(self):
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.put_object(Bucket='mybucket', Key=self.name, Body=self.value)

    def post(self):
        sns = boto3.client('sns', region_name='us-east-1')
        sns.publish(PhoneNumber="+1234567890", Message="message")

