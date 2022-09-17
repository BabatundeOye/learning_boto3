import boto3

sqs = boto3.client('sqs')

response = sqs.delete_queue(
    QueueUrl='https://us-west-2.queue.amazonaws.com/281588703096/docs-queue'
)

print('Queue Deleted')