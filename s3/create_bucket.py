import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("copper13stone")
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    },
    
)
print(response)

#pip install boto3
#pip3.7 install boto3