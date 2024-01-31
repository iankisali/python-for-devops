import boto3

#ec2_client = boto3.client('ec2')

# passing in region instead of using default region
ec2_client = boto3.client('ec2', region_name="us-east-1")

ec2_resource = boto3.resource('ec2')

new_vpc = ec2_resource.create_vpc(
    CidrBlock="10.0.0.0/16"
)

new_vpc.create_subnet(
    CidrBlock="10.0.1.0/24"
)

new_vpc.create_subnet(
    CidrBlock="10.0.2.0/24"
)

new_vpc.create_tags(
    Tags = [
                {
                    'Key': 'Name',
                    'Value': 'my-vpc'
                },
            ]
)

all_vpcs = ec2_client.describe_vpcs()
vpcs = all_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_ass_set = vpc["CidrBlockAssociationSet"]
    for ass_set in cidr_block_ass_set:
        print(ass_set["CidrBlockState"])