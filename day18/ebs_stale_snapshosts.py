import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    deleted_snapshots = []

    # Get all EBS snapshots
    snapshots_response = ec2.describe_snapshots(OwnerIds=['self'])

    # Get all active EC2 instances and their attached volumes
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_volumes = set()

    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            for block_device in instance.get('BlockDeviceMappings', []):
                if 'Ebs' in block_device:
                    active_volumes.add(block_device['Ebs']['VolumeId'])

    # Iterate through each snapshot and delete if conditions are met
    for snapshot in snapshots_response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        if not volume_id:
            # If snapshot is not attached to any volume, delete it
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            deleted_snapshots.append(snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
        else:
            try:
                # Check if the volume exists
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                volume = volume_response['Volumes'][0]

                if volume_id not in active_volumes:
                    # If volume exists but is not attached to any running instance, delete the snapshot
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    deleted_snapshots.append(snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as the volume {volume_id} is not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # If the volume is not found (deleted), delete the snapshot
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    deleted_snapshots.append(snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume {volume_id} was not found.")

    return {
        'statusCode': 200,
        'body': f"Deleted snapshots: {deleted_snapshots}" if deleted_snapshots else "No snapshots were deleted."
    }
