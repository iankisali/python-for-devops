import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name='eu-north-1')
ec2_resource = boto3.resource('ec2', region_name='eu-north-1')

instance_id = ''

#getting volumes attached to instance_id
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

instance_volume = volumes['Volumes'][0]

#getting snapshots
snapshots = ec2_client.describe_snapshots(
    OwnerIds=["self"], 
    Filters=[
        {
            #filter volumes by volumeid
            "Name": 'volume-id',
            "Values": [instance_volume['VolumeId']]
        }
    ]
)

latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]

new_volume = ec2_client.create_volume(
    snapshotId=latest_snapshot['SnapshotId'],
    AvailabilityZone="eu-north-1a",
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'prod'
                }
            ]
        }
    ]
)

while True:
    vol = ec2_resource.Volume(new_volume['VolumeId'])
    print(vol.state)
    if vol.state == 'available':
        ec2_resource.Instance(instance_id).attach_volume(
            VolumeId=new_volume['VolumeId'],
            Device='/dev/xvdb'
    )
    break