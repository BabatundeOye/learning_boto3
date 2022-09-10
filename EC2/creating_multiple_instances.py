import boto3

ec2 = boto3.resource("ec2")
response=ec2.create_instances(ImageId='ami-0c2ab3b8efb09f272', InstanceType='t2.micro', 
            MaxCount=5, MinCount=5)
print(response)
