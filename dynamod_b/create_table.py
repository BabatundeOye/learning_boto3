import boto3

dynamodb = boto3.resource("dynamodb") #Get the service resource

table = dynamodb.create_table(  #create the dynamodb table 
    TableName="Samuel_L_Jackson_Movies",
        KeySchema=[
        {
            "AttributeName": "Movie",
            "KeyType": "HASH" #partition key
        },
        {
            "AttributeName": "Year",
            "KeyType": "RANGE" #sort key
        },
    ],
    AttributeDefinitions=[
        {
            "AttributeName": "Movie",
            "AttributeType": "S"
        },
        {
            'AttributeName': "Year",
            'AttributeType': "N"
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    }    
    )
    
    # Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)