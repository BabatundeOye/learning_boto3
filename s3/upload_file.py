import boto3
#import pathlib
#import os


s3_client= boto3.client('s3')

bucket_name="copper12stone"
object_name='sample_upload'
#file_name= os.path.join(pathlib.Path(__file__).parent.resolve(), "blue-dolphin.jpg")
file_name='blue-dolphin.jpg'
response = s3_client.upload_file(file_name, bucket_name, object_name)

#cd into your folder where you file to be uploaded is located and print working directory . 
#use the working directory as your filename or
#change your working directory in the terminal by clicking on the cwd 