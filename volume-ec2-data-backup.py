import boto3
import schedule

ec2_client = boto3.client('ec2', region_name='eu-north-1')

def create_volume_snapshots():

    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                #filter volumes to create snapshots from
                "Name": 'tag:Name',
                "Values": ['prod', 'staging']
            }
        ]
    )

    #creating snapshot
    for volume in volumes["Volumes"]:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume["VolumeId"]
        )
        print(new_snapshot)

#schedule to take snapshots everyday
schedule.every().day.do(create_volume_snapshots)

#running scheduler
while True:
    schedule.run_pending()