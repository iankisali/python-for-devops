import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-north-1")

#fetching volumes with name tag prod and where we are creating snapshots from
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            #filter volumes to create snapshots from
            "Name": 'tag:Name',
            "Values": ['prod', 'staging']
        }
    ]
)

#going through volumes list
for volume in volumes['Volumes']:
    #for aech volume we are getting list
    snapshots = ec2_client.describe_snapshots(
        OwnerIds=["self"], 
           Filters=[
        {
            #filter volumes by volumeid
            "Name": 'volume-id',
            "Values": [volume['VolumeId']]
        }
    ]
    )

    #sorting snapshots by creation time
    sort_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    #deletes snapshot from the 3rd snapshpt
    for snapshot in sort_by_date[2:]:
        response = ec2_client.delete_snapshpt(
            SnapshotId=snapshot['SnapshotId']
        )
        print(response)



'''
for snapshot in snapshots['Snapshots']:
    print(snapshot['StartTime'])

print("\n")

for snapshot in sort_by_date:
    print(snapshot['StartTime'])
'''