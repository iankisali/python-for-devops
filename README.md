# Python Programming for DevOps and Cloud

This repo contains case studies and examples of using Python in DevOps and Cloud as an automation tool.

This is a documentation of what specific python file in this repo does:

| Directory/File name | Description |
| ------------ | ----------- |
Recap | Directory containing recap projects on Python. This include data types, varianbles, functions, condiitionals, error handling using Try / Except, loops, sets, dictionaries, modules, classes, objects, OOP and API requests |
eks-cluster-tf | Directory containing terraform files to create and deploy a simple nginx on Amazon EKS. Files create a VPC, public and public subnets, EKS cluster with 3 worker nodes, autoscaling groups, IAM roles and nodegroup. |
infrastructure-provisioning-tf | Directory containing terraform files to create simple infrastructure in AWS. Creates a VPC, subnets, internet gateway, route table, security group, ami and 2 instances. |
add-env-tags.py | Python file that gets all EC2 instances in a region and adds the right tags. |
cleanup-ec2-snapshots.py | Script creating ec2 instances with env tags, get all snapshots, deletes them except last 2 snapshots. Also created scheduled tasks for cleanup and deleting snapshots except last 2 for each volume. |
ec2-status-checks.py | Script to print all ec2 instances state and their status. |
eks-status-check.py | Script to get all EKS clusters and print information i.e status, endpoint and k8s version. |
infr-provisioning-python.py | Script to create basic infrastructure in the cloud. Creates VPC and 2 subnets with their env tags.  |
restore-ec2-volume.py | Script that creates 2 ec2 servers with environment tags, create new volume from snapshot and attach to ec2 instance. |
schedule-ec2-status-check.py | Script scheduled to check instance and system status in a region after every 5 minutes. |
volume-ec2-data-backup.py | Script to get volume ids, create snapshots from the volumes, scheduled tasks for the backup task and creating snapshots for only production servers. |
website-monitoring.py | Script to monitor a simple nginx website. Include functions to send email when website is down, connecting to server via ssh, restarting and rebooting server incase it goes down. |
