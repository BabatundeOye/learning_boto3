import boto3

sqs = boto3.client('sqs')

response = sqs.send_message(
    QueueUrl='https://sqs.us-west-2.amazonaws.com/281588703096/docs-queue',
    MessageBody='working with python',
)


print('Message sent')