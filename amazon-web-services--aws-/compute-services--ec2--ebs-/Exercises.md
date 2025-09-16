# Exercise 1 - Control EC2 from AWS cli 

Perform the below operations using AWS cli directly on your instance.

1. Stop your instance. 
2. Start it. 
3. Add the tag `ENV=test` to your instance.
4. Get the Network Interface id attached to the instance.  


<details>
  <summary>
     Solution
  </summary>

1. `aws ec2 stop-instances --instance-ids <your-instance-id>`
2. `aws ec2 start-instances --instance-ids <your-instance-id>`
3. `aws ec2 create-tags --resources <your-instance-id> --tags Key=ENV,Value=test`
4. `aws ec2 describe-instances --instance-ids i-0ba57202a6f7d7302 --query 'Reservations[*].Instances[*].NetworkInterfaces[*].NetworkInterfaceId'`

</details>


# Exercise 2 - Change instance properties

1. Change your instance type from `*.micro` to `*.nano`.
2. Change the availability zone of your instance. 
3. Add tag

<details>
  <summary>
     Solution
  </summary>

1. Stop the instance first, then, with the instance still selected, choose **Actions**, **Instance settings**, **Change instance type**.
2. It's not possible to change the AZ :-)
3. In the navigation pane, choose the **Tags** tab, enter the key and value for the tag. When you are finished adding tags, choose **Save**.

</details>

# Exercise 3 - boto3 

`boto3` is the AWS SDK for Python, which allows Python developers to write software that makes use of AWS services. 

1. Install it by `pip install boto3` (it's recommended to install it using PyCharm's terminal in an existed Python venv).
2. Write to python code that:
   1. Stops your EC2 instance.
   2. Creates an AMI from the instance. 

<details>
  <summary>
     Solution
  </summary>


```python
import boto3

region = 'your-region-code'

# Create an EC2 client object
ec2 = boto3.client('ec2', region_name=region)

# Stop the EC2 instance with the given instance id
instance_id = 'your-instance-id'
ec2.stop_instances(InstanceIds=[instance_id])

# Wait until the instance is stopped
waiter = ec2.get_waiter('instance_stopped')
waiter.wait(InstanceIds=[instance_id])

# Create an AMI from the stopped instance
image_name = 'my-ami'
response = ec2.create_image(InstanceId=instance_id, Name=image_name)

# Get the ID of the created AMI
ami_id = response['ImageId']
print(f"Created AMI with ID: {ami_id}")
```

</details>


# Exercise 4 - Create an encrypted EBS and migrate disks

1. In KMS, [create encryption key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk). Make sure your IAM user can administer this key and delete it.
2. [Create a volume snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html#ebs-create-snapshot) of the EBS you provisioned and mounted in the previous section.
3. Create an **encrypted EBS from the EBS snapshot**. Use the encrypted keys you’ve just created in KMS.
4. Attach and mount the encrypted volume to your instance, as follows:
    1. Generate new UUID for the encrypted disk by:
       ```shell
       sudo xfs_admin -U generate <device-name>
       ```
    2. Copy the generated uuid, and add the following entry to `/etc/fstab`:
       ```shell
       UUID=<device-uuid>  /data  xfs  defaults,nofail  0  2
       ```
       while `<device-uuid>` is your generated device UUID.

   Make sure the data from the unencrypted volume has been migrated successfully to the encrypted volume.
5. In KMS page, disable your encryption key. What happened to the data in your instance?
6. Stop the machine and start it again, [what happened](https://docs.aws.amazon.com/kms/latest/developerguide/services-ebs.html#ebs-cmk) to the data in your instance?


## Exercise 5 - EC2 instance metadata

EC2 instance metadata is a service provided by AWS that allows an EC2 instance to retrieve information about itself (**from within itself**), 
such as its instance ID, hostname, and IP address, without the need for authentication.
This information can be accessed using a special URL or by using the EC2 instance metadata service API.

There is a static IP address reserved by AWS to retrieve instance metadata: 

```text
http://169.254.169.254/latest/meta-data/
```

Connect to your instance, and use `curl` and the instance metadata URL to retrieve: 

- Get the subnet ID of the instance
- Get the instance tags
- Get the list of available public keys

<details>
  <summary>
     Solution
  </summary>

- `http://169.254.169.254/latest/meta-data/network/interfaces/macs/<your-interface-mac-address>/subnet-id`
- `http://169.254.169.254/latest/meta-data/tags/instance`
- `http://169.254.169.254/latest/meta-data/public-keys/`


</details>


# (optional) Exercise 4 - Network test between two instances

Work with a friend on the same region.
Use the `iperf` tool to measure network performance between two EC2 instances. 
You'll measure the bandwidth and latency of the connection using the `iperf` output.

1. Install `iperf` on both you and your friend machine:

```bash
sudo apt-get update
sudo apt-get install iperf3
```

2. Some of you should run the server:

```bash 
iperf3 -s
```

3. The other participant should run the client:

```bash
iperf3 -c <SERVER_IP>
```

Make sure the appropriate ports are opened. 

