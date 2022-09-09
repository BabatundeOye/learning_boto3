
#describe all vpc available in your account
'''
import boto3
client=boto3.client("ec2")
describe=client.describe_vpcs()
print(describe)
'''

#Quantity of vpc

import boto3
client=boto3.client("ec2")
describe=client.describe_vpcs()
print(len(describe))
