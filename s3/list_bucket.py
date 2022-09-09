#List existing buckets


import boto3
#resource=boto3.resource("s3")
s3 = boto3.client('s3')

#line 5 and 6 is the same 

response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')





