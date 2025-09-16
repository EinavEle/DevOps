This page is aimed for course staff only, if you are a student, you can skip it. 

Preparation needed to enable auto testing for this project. 

1. As students build VPC in AWS, it's recommended to cover the "Intro to cloud computing" unit from AWS course before. 
1. In the **TLS Handshake** page, you may need to change the url of https://raw.githubusercontent.com/alonitac/atech-devops-june-2023/main/networking_project/tls_webserver/cert-ca-aws.pem according to your group's GitHub repo. It should be a url to the raw `networking_project/tls_webserver/cert-ca-aws.pem` file existed in the shared repo. 
1. In the shared AWS account, create a user `github-action` with permissions on EC2 (it can be part of the limited `students` group).
1. Generate access CLI access keys.
1. In the group shared GitHub repo, go to **Settings**, under **Secrets and variables**, click on **Actions**.
1. Define the following **Repository secrets**:

   - `AWS_ACCESS_KEY_ID` with the generated access id as a value.
   - `AWS_SECRET_ACCESS_KEY` with the generated access key as a value.
   - `COURSE_STAFF_SSH_KEY` with the following value:

```text
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
```
