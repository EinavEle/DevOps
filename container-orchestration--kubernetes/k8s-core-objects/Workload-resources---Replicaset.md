### Workload resources 

Usually you don't need to create Pods directly. 
Each Pod is meant to run a single instance of a given application. 
If you want to scale your application horizontally, you should replicate the Pod in different nodes. Replicated Pods are usually created and managed as a group by a **Workload Resource**.

Workload resources create and manage multiple Pods for you, with many added benefits.
They handle replication and rollout and automatic healing in case of Pod failure.
For example, if a Node fails, a workload resource notices that Pods on that Node have stopped working and creates a replacement Pod. 

Available workload resources are:

- **Deployment** (and, indirectly, **ReplicaSet**), the most common way to run an stateless applications on your cluster.
- A **StatefulSet** lets you run Pods connected to a persistent storage.
- A **DaemonSet** lets you run single Pod on each Node of your cluster.
- You can use a **Job** (or a **CronJob**) to define tasks that (periodically) run to completion and then stop.

**Note:** Workload resources don't run containers directly, the only object in Kubernetes that does so is the Pod.
All other workload resources **only manage Pods**. For that reason, workload resources are also known as **Controllers**.
In Kubernetes, controllers are control loops that watch the state of your Pods, then make or request changes where needed. Each controller tries to move the current state closer to the desired state.

In this tutorial we will focus on **Deployment** and **ReplicaSet**. 

### ReplicaSet

A **ReplicaSet**'s purpose is to maintain a stable set of replica Pods running at any given time.
As such, it is often used to guarantee the availability of a specified number of identical Pods.

Here is an example of ReplicaSet:

```yaml 
# k8s/replicaset-demo.yaml 

apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: emailservice-replicaset-demo
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
    spec:
      containers:
      - name: server
        image: gcr.io/google-samples/microservices-demo/emailservice:v0.7.0
```

In this example:

- The `.spec.template` field contains a [PodTemplates](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates). PodTemplates are specifications for creating Pods. As you can see it's very similar to `Pod` YAML described in the previous section.
  We can also notice that pods created from this template hold a label with key `app` and value `emailservice`.
- The ReplicaSet creates three replicated Pods, indicated by the `.spec.replicas` field.
- The `.spec.selector.matchLabels` field defines how the created ReplicaSet finds which Pods to manage (remember that ReplicaSet is a controller that manage Pods). In this case, the ReplicaSet will manage all Pods that match the label `app: emailservice-demo`, corresponding to the label we gave in the Pod template. 

Let's apply this ReplicaSet in the cluster.

```bash 
kubectl apply -f k8s/replicaset-demo.yaml
```

You can then get the current ReplicaSets deployed:

```bash 
kubectl get rs
```

You can also check for the Pods brought up as part of the ReplicaSet:

```bash 
kubectl get pods -l app=emailservice-demo
```

Let's play with your ReplicaSet:

- Delete one of the pods owned by the ReplicaSet. What happened? 
- A ReplicaSet can be easily scaled up or down by simply updating the `.spec.replicas` field. Try it out...
- Create a Pod (separately to the ReplicaSet) in the cluster, with the same label key and value as you gave in the PodTemplate. What happened? Why? 
- Try to update the image version in the YAML manifest to `emailservice:v0.8.0`, and perform `kubectl apply` with the updated YAML file. What happened? Why? 

Delete your ReplicaSet before moving on to the next section:

```bash
kubectl delete replicaset emailservice-replicaset-demo
```
