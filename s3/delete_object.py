import boto3

#Delete single object
s3=boto3.client("s3")
s3.delete_object(Bucket="copper12stone",Key="sample_uploads")

#delete multiple objects
import os
import glob

#find all objects from the bucket
objects=s3.list_objects(Bucket="copper12stone")["Contents"]
#len(objects)

#iteration and will list all objects 
#for object in objects: 
   # print(object["Key"])
   
for object in objects: 
    response=s3.delete_object(Bucket="copper12stone",Key=object["Key"])
    print(response)