import boto3

ec2_resource = boto3.resource('ec2')
createid=ec2_resource.create_instances(
    ImageId='ami-0c2ab3b8efb09f272',
    InstanceType='t2.micro',
    MaxCount=2,
    MinCount=2,
    Tags=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Environment',
                    'Value': 'prod',
                },
                {                    
                    'Key': 'environment',
                    'Value': 'prod',
                },
            ]
        },
    ],
)
#print out each instance that is created
for instanceid in createid:
    print("Here are your instance id for prod environment:", instanceid)
