# Exercise 1 - Application Load Balancer with TLS termination

### Create TLS certificate

We would like our load balancers to listen on HTTPS protocol for clients connection. In order to achieve that, we need to create and sign a digital certificate.

In order to create your own SSL certificate, perform the following in your local machine (`openssl` required):
1. Generate private key as private.pem
   ```
   openssl genrsa -out private.pem 2048
   ```
2. Generate public key as public.pem
   ```
   openssl rsa -in private.pem -outform PEM -pubout -out public.pem
   ```
3. Create a CSR (Certificate Signing Request) as certificate.csr
   ```
   openssl req -new -key private.pem -out certificate.csr
   ```
4. Create a Self-signed certificate as certificate.crt
   ```
   openssl x509 -req -days 365 -in certificate.csr -signkey private.pem -out certificate.crt
   ```

IAM securely encrypts your private keys and stores the encrypted version in IAM SSL certificate storage. You cannot manage your certificates from the IAM Console.

5. To upload a server certificate to IAM (make sure your local aws cli is configured with the proper credentials)
   ```shell
   aws iam upload-server-certificate --server-certificate-name <your-cert-name> --certificate-body file://certificate.crt --private-key file://private.pem
   ```

### Add an HTTPS listener to your load balancer

1. On the navigation pane, under **Load Balancing**, choose **Load Balancers**\.

2. Select a load balancer, and choose **Listeners**, **Add listener**\.

3. For **Protocol : port**, choose **HTTPS** and keep the default port or enter a different port\.

4. For **Default actions**, choose **Add action**, **Forward to** and choose a target group\.

5. For **Security policy**, we recommend that you keep the default security policy\.

6. For **Default SSL certificate**, choose **From IAM** and choose the certificate that you uploaded\.

7. Choose **Save**\.

8. Test your load balancer over HTTPS.



# Exercise 2 - Working with sticky sessions

Sticky session is a load balancing technique commonly used in web applications that require maintaining user session state.
It ensures that all requests from a particular user are routed **to the same instance** that initially handled their request, allowing the server to maintain session data and provide a consistent user experience.
This is particularly useful for applications that rely on session-specific information or personalized settings.

1. On the navigation pane, under **Load Balancing**, choose **Target Groups**\.

2. Choose the name of the target group to open its details page\.

3. On the **Group details** tab, in the **Attributes** section, choose **Edit**\.

4. On the **Edit attributes** page, do the following:

    1. Select **Stickiness**\.

    2. For **Stickiness type**, select **Load balancer generated cookie**\.

    3. For **Stickiness duration**, specify a value between 1 second and 7 days\.

    4. Choose **Save changes**\.

5. Make sure stickiness is applied by requesting the URL multiple times and validating that you always communicate with the same instance.  

