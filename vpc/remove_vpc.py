import boto3
client=boto3.client("ec2")
response = client.delete_vpc(
    VpcId='vpc-0315f6601c15b4348',
    
)
print(response)