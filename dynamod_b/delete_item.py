import boto3

dynamodb = boto3.resource("dynamodb")
table= dynamodb.Table("Samuel_L_Jackson_Movies")
response=table.delete_item(
    Key={
        'Movie': 'Jackie Brown', #item to be removed
        'Year': 1997
    }
)

print(response)

