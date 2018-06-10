import boto3
from moto import mock_s3, mock_sns
from testBoto.s3_unittest.mymodule import MyModel


@mock_s3
def test_my_model_save():
    conn = boto3.resource('s3', region_name='us-east-1')
    # We need to create the bucket since this is all in Moto's 'virtual' AWS account
    conn.create_bucket(Bucket='mybucket')

    model_instance = MyModel('steve', 'is awesome')
    model_instance.save()

    body = conn.Object('mybucket', 'steve').get()['Body'].read().decode("utf-8")
    print(body)
    assert body == 'is awesome'


@mock_sns
def test_my_model_save2():
    conn = boto3.resource('sns', region_name='us-east-1')
    conn.create_sns(PhoneNumber="1234567890", Message="message")

    model_instance = MyModel('steve', 'is awesome')
    model_instance.post()

    body = conn.Object('mybucket', 'steve').get()['Body'].read().decode("utf-8")
    assert body == 'is awesome'


if __name__ == '__main__':
    test_my_model_save()
    # test_my_model_save2()
