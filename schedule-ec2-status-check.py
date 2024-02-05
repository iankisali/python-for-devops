import boto3
import schedule

ec2_client = boto3.client('ec2',region_name = "us-east-1")
ec2_resourcs = boto3.resource('ec2',region_name = "us-east-1")

#checks only running instance state
def check_instance_status():
    instanceStatuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )

    for status in instanceStatuses["InstanceStatuses"]:
        ins_status = status["InstanceStatus"]["Status"]
        sys_status = status["SystemStatus"]["Status"]
        state = status["InstanceState"]["Name"]
        print(f"Instance {status["InstanceId"]} is {state} with instance state {ins_status} and system status is {sys_status}")
        print("\n")

schedule.every(5).minutes.do(check_instance_status)
#schedule.every().monday.at("12:00")

#running scheduler
while True:
    schedule.run_pending()