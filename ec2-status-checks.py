import boto3

ec2_client = boto3.client('ec2',region_name = "us-east-1")
ec2_resourcs = boto3.resource('ec2',region_name = "us-east-1")

reservations  = ec2_client.describe_instances()

for reservation in reservations["Reservations"]:
    instances = reservation["Instances"]
    for instance in instances:
        print(f"Instance id {instance["InstanceId"]} is {instance["State"]["Name"]}")

instanceStatuses = ec2_client.describe_instance_status()

for status in instanceStatuses["InstanceStatuses"]:
    ins_status = status["InstanceStatus"]["Status"]
    sys_status = status["SystemStatus"]["Status"]
    state = status["InstanceState"]["Name"]
    print(f"Instance {status["InstanceId"]} is {state} with instance state {ins_status} and system status is {sys_status}")