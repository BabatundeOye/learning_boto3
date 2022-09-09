#how to create vpc


import boto3
client=boto3.client("ec2")
response=client.create_vpc(CidrBlock='10.0.0.0/16')
print(response)



#checking for vpc id
'''
import boto3
client=boto3.client("ec2")
x=client.describe_vpcs()
no_of_vpcs=x["Vpcs"]

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
'''