import boto3

sqs = boto3.client('sqs')


response = sqs.create_queue(
    QueueName='docs-queue')
    
print('Queue created')
