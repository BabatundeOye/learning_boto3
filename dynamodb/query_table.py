import boto3
from boto3.dynamodb.conditions import Key, Attr #Key and Attr are used when 
#the condition is related to either the key or attribute of an item

dynamodb = boto3.resource("dynamodb")
table= dynamodb.Table("Samuel_L_Jackson_Movies")

response = table.query(
    KeyConditionExpression=Key("Movie").eq("Goodfellas")
)
items = response["Items"]
print(items)
