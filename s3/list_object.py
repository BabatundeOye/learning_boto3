import boto3

s3=boto3.client("s3")
objects=s3.list_objects(Bucket="copperpark12")["Contents"] #to list the content
len(objects) #to check the quantity of objects in a bucket

#check if objects exists
if len(objects)>0:
    print("objects exists")
    
for object in objects:
    print(object["Key"])