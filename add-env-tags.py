import boto3

ec2_client_virginia = boto3.client('ec2',region_name = "us-east-1")
ec2_resource_virginia = boto3.resource('ec2',region_name = "us-east-1")

ec2_client_stockholm = boto3.client('ec2',region_name = "eu-north-1")
ec2_resource_stockholm = boto3.resource('ec2',region_name = "eu-north-1")

instance_ids_virginia = []
instance_ids_stockholm = []

reservations_virginia = ec2_client_virginia.describe_instances()["Reservations"]
reservations_stockholm = ec2_client_stockholm.describe_instances()["Reservations"]

for reservation in reservations_virginia:
    instances = reservation["Instances"]

    #collect all instance ids into list and add tags for all instanceId 
    for instance in instances:
        instance_ids_virginia.append(instance["InstanceId"])

response = ec2_resource_virginia.create_tags(
    Resources=instance_ids_virginia,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)

for reservation in reservations_stockholm:
    instances = reservation["Instances"]

    #collect all instance ids into list and add tags for all instanceId 
    for instance in instances:
        instance_ids_stockholm.append(instance["InstanceId"])

response = ec2_resource_stockholm.create_tags(
    Resources=instance_ids_stockholm,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)