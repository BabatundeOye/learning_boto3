import boto3

sqs = boto3.client('sqs')

response = sqs.get_queue_url(
    QueueName='docs-queue',
)

#print(response)

url = response['QueueUrl']
print(url)