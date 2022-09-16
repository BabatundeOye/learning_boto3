import boto3

#line 3 to line 9 creates instances
ec2_resource = boto3.resource('ec2')
ec2_resource.create_instances(
    ImageId='ami-0c2ab3b8efb09f272', 
    InstanceType='t2.micro', 
    MaxCount=1, 
    MinCount=1)


#list of instances 

ec2=boto3.client('ec2')
response=ec2.describe_instances()
data=response['Reservations']

for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        print(instance_id)
        
#create tags for instances created
response=ec2_client.create_tags(
TAGS = [
    {
        'Key': 'Environment',
        'Value': 'dev'
    }
]

instances = ec2_resource.instances.filter(
    InstanceIds=[
        INSTANCE_ID,
    ],
)

for instance in data:
    instance.create_tags(Tags=TAGS)
    print(f'Tags successfully added to the instance {instance.id})'