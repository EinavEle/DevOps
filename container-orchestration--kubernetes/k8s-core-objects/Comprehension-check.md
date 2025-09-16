
Given the below Pod YAML manifest:

```yaml 
apiVersion: v1
kind: Pod
metadata:
  name: nginx-with-sidecar
  labels:
    app: nginx-with-sidecar
spec:
  containers:
    - name: nginx
      image: nginx:1.14
      ports:
        - containerPort: 80
    - name: sidecar-container
      image: busybox:latest
      command: ["/bin/sh", "-c", "while true; do echo 'Sidecar Container Running'; sleep 10; done"]
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx-with-sidecar
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

Answer the below 5 questions


{Check It!|assessment}(multiple-choice-773521503)
{Check It!|assessment}(multiple-choice-2448431791)
{Check It!|assessment}(multiple-choice-317181447)
{Check It!|assessment}(multiple-choice-75825568)
{Check It!|assessment}(multiple-choice-2637826073)
{Check It!|assessment}(multiple-choice-2215413810)


Given the following Secret and Pod: 

```yaml 
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  password: cGFzc3dvcmQxMjM=
  username: dXNlcgo=
---
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mycontainer
    image: busybox:latest
    command: ["sleep", "3600"]
    volumeMounts:
    - name: secret-volume
      mountPath: "/etc/my-secret"
  volumes:
  - name: secret-volume
    secret:
      secretName: my-secret
```

Getting a Shell access to `mypod`, answer the below 3 questions: 


{Check It!|assessment}(multiple-choice-1215390473)
{Check It!|assessment}(multiple-choice-3057221120)
{Check It!|assessment}(multiple-choice-2864629798)
{Check It!|assessment}(multiple-choice-314115748)
{Check It!|assessment}(multiple-choice-2214460725)
{Check It!|assessment}(multiple-choice-103146920)
{Check It!|assessment}(multiple-choice-3312795360)

