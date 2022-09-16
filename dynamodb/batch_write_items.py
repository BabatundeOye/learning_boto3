import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Samuel_L_Jackson_Movies")
#Batch writing items to table 
with table.batch_writer() as batch:
    batch.put_item(Item={"Movie":"Goodfellas", "Year":1990})
    batch.put_item(Item={"Movie":"Jurassic Park", "Year":1993})
    batch.put_item(Item={"Movie":"The Hateful Eight", "Year":2015})
    batch.put_item(Item={"Movie":"Pulp Fiction", "Year":1994})
    batch.put_item(Item={"Movie":"Django Unchained", "Year":2012})
    batch.put_item(Item={"Movie":"Jackie Brown", "Year":1997})
    batch.put_item(Item={"Movie":"The Avengers", "Year":2012})
    batch.put_item(Item={"Movie":"Captain America", "Year":2014})
    batch.put_item(Item={"Movie":"Chi-Raq", "Year":2015})
    batch.put_item(Item={"Movie":"The Cleaner", "Year":2007})
    
    print(batch)