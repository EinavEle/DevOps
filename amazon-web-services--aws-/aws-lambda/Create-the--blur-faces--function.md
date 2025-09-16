
1. Create a **Container image** Lambda function based on the Docker image built from `face-blur-lambdas/blur-faces/Dockerfile`. Use an existing Docker image, or create an ECR and build the image by:

    2. Open the Amazon ECR console at [https://console\.aws\.amazon\.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).
    3. In the navigation pane, choose **Repositories**\.
    4. On the **Repositories** page, choose **Create repository**\.
    5. For **Repository name**, enter a unique name for your repository\.
    6. Choose **Create repository**\.
    7. Select the repository that you created and choose **View push commands** to view the steps to build and push an image to your new repository\.

2. Add the following env var to this function:
   `OUTPUT_BUCKET=<bucket-name>` where `<bucket-name>` is another bucket to which the processes videos will be uploaded (create one if needed).
3. This function is CPU and RAM intensive since it processes the video frame-by-frame. Make sure this it has enough time and space to finish (in the **General Configuration** tab, increase the timeout to 5 minutes and the memory to 2048MB).
