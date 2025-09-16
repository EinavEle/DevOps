
## ConfigMap

Official docs [reference](https://kubernetes.io/docs/concepts/configuration/configmap/).

ConfigMap is a mechanism for storing non-sensitive configuration data in key-value pairs. 
Pods can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a volume.
ConfigMaps provide a convenient way to manage and **inject configuration settings into applications**, allowing for easy configuration changes without modifying the application's container image or restarting the Pod.

We continue with our `emailservice` service as an example.
This service is responsible to send users an order confirmation email (mock). The `templates` directory within the docker image contains a [file called `confirmation.html`](https://github.com/GoogleCloudPlatform/microservices-demo/tree/main/src/emailservice/templates), which an email template to be used. 

Let's say you want to create your own confirmation email template. Two approaches can be taken here:

1. Use the `emailservice:v0.7.0` image (built and managed by Google) as a base image in a Dockerfile, and build your own image with your own template file.  
2. Use the original `emailservice:v0.7.0` image, and mount a `template` directory into the container file system, with your own template. 

The first approach introduced the overhead of build and maintaining a Docker image, only because a single file has to be changed in the pre-built image.
The seconds approach can be easily achieved using a ConfigMap.  

```yaml 
# k8s/configmap-demo.yaml

apiVersion: v1
kind: ConfigMap
metadata:
  name: email-templates
data:
  # this known as "file-like" keys. In YAML, the "|" coming after the key allows to have multi-line values
  confirmation.html: |
    <html>
      <head>
        <title>Your Order Confirmation</title>
        <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
      </head>
      <style>
        body{
          font-family: 'DM Sans', sans-serif;
        }
      </style>
      <body>
        <h2>Your Order Confirmation</h2>
        <p>Thanks for shopping with us!<p>
        <h3>Order ID</h3>
        <p>#{{ order.order_id }}</p>  
      </body>
    </html>
```

As can be seen, ConfigMaps are similar to Secrets but are specifically intended to hold non-confidential data.

After applying the ConfigMap, let's update our Deployment accordingly:

```yaml 
# k8s/deployment-demo-configmap-mount.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: emailservice-deployment-demo
  labels:
    app: emailservice-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: emailservice-demo
  template:
    metadata:
        labels:
          app: emailservice-demo
          release: v0.7.0-stable
    spec:
      containers:
      - name: server
        image: gcr.io/google-samples/microservices-demo/emailservice:v0.7.0
        volumeMounts:
          - name: email-templates-vol
            mountPath: /email_server/templates
          - name: secret-volume
            mountPath: /etc/secret-volume
            readOnly: true
      volumes:
        - name: email-templates-vol
          configMap:
            name: email-templates
        - name: secret-volume
          secret:
            secretName: emailservice-user-pass
```

For this example, defining a volume and mounting it inside the container as `/email_server/templates` creates one file, `/email_server/templates/confirmation.html`, according to the `confirmation.html` key defined in the ConfigMap.

Similarly to Secrets, ConfigMap can also be consumed as environment variables.
