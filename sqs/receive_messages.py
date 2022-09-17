import boto3

sqs = boto3.client('sqs')


response = sqs.receive_message(
    QueueUrl='https://sqs.us-west-2.amazonaws.com/281588703096/docs-queue',
)

messages = response['Messages']

for message in messages:
    data=message['Body']
    print(data)