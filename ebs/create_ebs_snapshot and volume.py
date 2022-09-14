#create ebs snapshot from volume

import boto3
ec2_client = boto3.client("ec2")
response=ec2_client.create_snapshot( Description='snapshot fom basevolume using python',
    VolumeId='string')

print(response)

#create ebs volume from snapshot 
'''
import boto3
ec2_client = boto3.client("ec2")
response = ec2_client.create_volume(
    AvailabilityZone='us-west-2c',
    Encrypted=True,
    Size=10,
    SnapshotId='string',
    VolumeType='gp2')
    
print(response)
'''