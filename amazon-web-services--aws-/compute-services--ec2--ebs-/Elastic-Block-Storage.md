## Create and mount EBS volume to your EC2 instance

1. In EC2 the navigation pane, choose **Volumes**\.
2. Choose **Create volume**\.
3. For **Volume type**, choose the type of volume to create, `SSD gp3`\. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html).
4. For **Size**, enter the size of the volume, 5GiB\. 
5. For **Availability Zone**, choose the Availability Zone in which to create the volume\. A volume can be attached only to an instance that is in the same Availability Zone\.
6. For **Snapshot ID**, keep the default value \(**Don't create volume from a snapshot**\)\.
7. Assign custom tags to the volume, in the **Tags** section, choose **Add tag**, and then enter a tag key and value pair\.
8. Choose **Create volume**\.
   **Note**  
   The volume is ready for use when the **Volume state** is **available**\.
9. To use the volume, attach it to an instance\. 
10. Connect to your instance over SSH.
11. [Format and mount the attached volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html) and write some data to the mounted EBS.


## Run application, open security group

1. Use `scp` to copy the files in our shared repo under `simple_flask_webserver` from your local machine to the instance.
2. Run the app by `python3 app.py` (install requirements if needed).
3. Define the appropriate rules in the instance's security group.
4. Visit the app.

