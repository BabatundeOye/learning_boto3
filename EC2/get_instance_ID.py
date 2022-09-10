import boto3

ec2=boto3.client('ec2')
x=ec2.describe_instances()

#print(x)
#x.keys()
#print(x.keys()) #to get the dict-keys in "x"
#print(len(x['Reservations']))

data=x['Reservations']#[0] #information relating to reservation


#data_instance=data['Instances']
#for i in range (len(data_instance)):
    #print(f"instance id is {data_instance[i]['InstanceId']}")    
    
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        print(instance_id)