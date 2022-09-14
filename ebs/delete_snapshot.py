
import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.delete_snapshot(
    SnapshotId='snap-02bf0b7250e044a64',
)

print(response)
