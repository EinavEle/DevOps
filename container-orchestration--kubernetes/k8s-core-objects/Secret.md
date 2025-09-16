
## Secrets 

Kubernetes **Secrets** are a way to securely store and manage sensitive information such as passwords, API keys, or certificates in the cluster.
Secrets can be created independently of the Pods that use them, so there is less risk of the Secret (and its data) being exposed during the workflow of creating, viewing, and editing Pods.

Secrets can be **mounted as files** or exposed **as environment variables** within Pods.

Suppose you have to provide a username and password for the `emailservice` service:

- Username `online-boutique-emailer`
- Password `39528$vdg7Jb`.

Before applying secrets to the cluster, the data has to be encoded in Base64:

```console
$ echo -n 'online-boutique-emailer' | base64
b25saW5lLWJvdXRpcXVlLWVtYWlsZXI=

$ echo -n '39528$vdg7Jb' | base64
Mzk1MjgkdmRnN0pi
```

Here is the Secret manifest you can use to create a Secret that holds your username and password:

```yaml
# k8s/secret-demo.yaml

apiVersion: v1
kind: Secret
metadata:
  name: emailservice-user-pass
type: Opaque
data:
  username: b25saW5lLWJvdXRpcXVlLWVtYWlsZXI=
  password: Mzk1MjgkdmRnN0pi
```

Alternatively, if you don't want to specify sensitive data in YAML files, you can create the same Secret using the `kubectl create secret` command:

```bash
kubectl create secret generic emailservice-user-pass --from-literal='username=online-boutique-emailer' --from-literal='password=39528$vdg7Jb'
```

The created Secret is an `Opaque` type secret.
It is used to store an arbitrary user-defined data.
Kubernetes support [other types](https://kubernetes.io/docs/concepts/configuration/secret/#secret-types) of secrets for different usages.

```console 
$ kubectl get secret emailservice-user-pass
NAME                     TYPE     DATA   AGE
emailservice-user-pass   Opaque   2      2m6s
```

The below example provides the secret data as environment variables to the running container:

```yaml
# k8s/deployment-demo-secret-env-var.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: emailservice-deployment-demo
  labels:
    app: emailservice-demo
spec:
  replicas: 3
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
        env:
          - name: EMAIL_SERVER
            value: "smtp.gmail.com"
          - name: EMAIL_SERVER_ADMIN_USER
            valueFrom:
              secretKeyRef:
                name: emailservice-user-pass
                key: username
          - name: EMAIL_SERVER_ADMIN_PASSWORD
            valueFrom:
              secretKeyRef:
                name: emailservice-user-pass
                key: password
```

In your shell, display the content of `EMAIL_SERVER_ADMIN_USER` and `EMAIL_SERVER_ADMIN_PASSWORD` container environment variable:

```console
$ kubectl get pods -l app=emailservice-demo
NAME                            READY   STATUS    RESTARTS      AGE
emailservice-55df5dcf48-6xbgx   1/1     Running   1 (91m ago)   19h

$ kubectl exec -it emailservice-55df5dcf48-6xbgx -- /bin/sh -c 'echo $EMAIL_SERVER_ADMIN_USER && echo $EMAIL_SERVER_ADMIN_PASSWORD'
online-boutique-emailer
39528$vdg7Jb
```

Secrets can also be mounted as file in the Pod's container file system:

```yaml
# k8s/deployment-demo-secret-mount.yaml

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
          # name must match the volume name below
          - name: secret-volume
            mountPath: /etc/secret-volume
            readOnly: true
      # The secret data is exposed to Containers in the Pod through a Volume.
      volumes:
        - name: secret-volume
          secret:
            secretName: emailservice-user-pass
```
The secret data is exposed to the Container through a Volume mounted under `/etc/secret-volume`.

```console
$ kubectl get pods -l app=emailservice-demo
NAME                                            READY   STATUS    RESTARTS      AGE
emailservice-deployment-demo-7484ddf954-pdbzz   1/1     Running   0              65s
```

Get a shell access to a running Pod's, in a similar way done for Docker containers:

```bash
kubectl exec -it emailservice-deployment-demo-7484ddf954-pdbzz -- /bin/bash
```

In the Pod's shell:

```console
root@emailservice-deployment-demo-7484ddf954-pdbzz:/email_server# ls /etc/secret-volume
password  username

root@emailservice-deployment-demo-7484ddf954-pdbzz:/email_server# cat /etc/secret-volume/username
online-boutique-emailer

root@emailservice-deployment-demo-7484ddf954-pdbzz:/email_server# cat /etc/secret-volume/password
39528$vdg7Jb
```
