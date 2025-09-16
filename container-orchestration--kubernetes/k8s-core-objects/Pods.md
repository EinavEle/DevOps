## Workloads

A **Workload** is an application running on Kubernetes.
Whether your workload is a single Docker container, or several containers that work together (e.g. HA mongo cluster), on Kubernetes you run it inside a set of **Pods**.

In this tutorial we will cover the following workloads:

- Pod
- ReplicaSet
- Deployment

### Pods

Official docs [reference](https://kubernetes.io/docs/concepts/workloads/pods/). 

Pods are the smallest deployable units of computing that you can create and manage in Kubernetes.
A Pod is a group of one or more containers (usually one), with **shared storage** and **network resources**, and a specification for how to run the containers.

The following is an example of a Pod which consists of a container running the image `emailservice:v0.7.0`. This is the image upon which the `emailservice` service, from the Online Boutique app, is based on.

```yaml
# k8s/pod-demo.yaml

apiVersion: v1
kind: Pod
metadata:
  name: emailservice-pod-test
  labels:
    project: online-boutique
    env: prod
    release: v0.7.0-stable
spec:
  containers:
  - name: server
    image: gcr.io/google-samples/microservices-demo/emailservice:v0.7.0
```

To create the Pod shown above, run the following command (the above content can be found in `k8s/simple-pod.yaml`):

```bash
kubectl apply -f k8s/simple-pod.yaml
```

When a Pod gets created, the new Pod is scheduled to run on a Node in your cluster.
The Pod remains on that node until the Pod finishes execution, the Pod object is deleted, the Pod is evicted for lack of resources, or the node fails.

The `labels` attached to the pod can be used to list or describe it.

Labels are key/value pairs that are attached to objects such as Pods.
Labels are intended to be used to specify identifying attributes of objects that are meaningful and relevant to users, as well as organizing a subsets of objects.
[Read here](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/) about labeling best practice.

```console
$ kubectl get pods -l release=v0.7.0-stable
NAME                    READY   STATUS    RESTARTS   AGE
emailservice-pod-test   1/1     Running   0          14s
$ kubectl describe pods -l release=v0.7.0-stable
Name:             emailservice-pod-test
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 24 Sep 2023 16:34:48 +0000
Labels:           app=online-boutique
                  env=prod
                  release=v0.7.0-stable
Annotations:      <none>
Status:           Running
IP:               10.244.0.87
IPs:
  IP:  10.244.0.87
Containers:
  server:
    Container ID:   docker://b93064757aa593c7be63edbb4796cdb468ccf1f5d527f0872e7adc7692127f7c
    Image:          gcr.io/google-samples/microservices-demo/emailservice:v0.7.0
    Image ID:       docker-pullable://gcr.io/google-samples/microservices-demo/emailservice@sha256:53d0416f79e3d4ba8d2092d7c48880375e3398f6e086996aa12b2e68d0a04976
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Sun, 24 Sep 2023 16:34:49 +0000
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-lw7mq (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-lw7mq:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  21m   default-scheduler  Successfully assigned default/emailservice-pod-test to minikube
  Normal  Pulled     21m   kubelet            Container image "gcr.io/google-samples/microservices-demo/emailservice:v0.7.0" already present on machine
  Normal  Created    21m   kubelet            Created container server
  Normal  Started    21m   kubelet            Started container server
```

In the above output we can see a detailed description of the pod. Reviewing all the presented information can be overwhelmed, but here are a few important notes:

- In you don't specify in which **namespace** to create the Pod object, the `default` namespace is used.
- Each Pod is assigned a unique IP address.
- Pod **events** can help you debug your pod state. 
