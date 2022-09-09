import boto3
import os
import glob

cwd=os.getcwd()
cwd=cwd+"/upload_file/" #you are to create a folder in the cwd and moves all pictures there
files=glob.glob(cwd+"*.jpg")

for file in files:
    s3=boto3.client('s3')
    #print(file) This will print the files in the cwd
    s3.upload_file(
    Filename=file,
    Bucket="copper12stone",
    Key=file.split("/")[-1]
    )
    

    
    