import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("Samuel_L_Jackson_Movies")

response =  table.scan()

response['Items']

print(response)