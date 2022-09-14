import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.describe_snapshots(SnapshotIds=['snap-09f208374cbc73d47'])
print(response)