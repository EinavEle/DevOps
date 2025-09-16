### Deployment

We started our tutorial with a bare Pod, then moved to work with a ReplicaSet.
However, this is not good enough. For example, as you've probability noticed, Replicaset does not automatically update containers when image version is updates. 

A **Deployment** is a higher-level concept that manages ReplicaSets and provides declarative updates to Pods along with a lot of other useful features.
In most cases, **ReplicaSet is not being used directly**. Kubernetes' docs recommending using Deployments instead of directly using ReplicaSets.

The following is an example of a Deployment:

```yaml
# k8s/deployment-demo.yaml

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
    spec:
      containers:
      - name: server
        image: gcr.io/google-samples/microservices-demo/emailservice:v0.7.0
```

To see the Deployment rollout status, run `kubectl rollout status deployment/emailservice-deployment-demo`

Under the hood, the Deployment object created a ReplicaSet (`rs`) for you:

```console
$ kubectl get rs
NAME                                      DESIRED   CURRENT   READY   AGE
emailservice-deployment-demo-75675f5897   3         3         3       18s
```

#### Updating a Deployment 

A Deployment's rollout is triggered if and only if the Deployment's Pod template (that is, `.spec.template`) is changed.

Let's update the `emailservice-deployment-demo` Pods to use the `emailservice:v0.8.0` image instead of the `emailservice:v0.7.0` image.
In the Deployment YAML manifest, edit the `.spec.template.spec.containers[0].image` value, and apply again.

Run `kubectl get rs` to see that the Deployment updated the Pods by **creating a new ReplicaSet** and scaling it up to 3 replicas, as well as scaling down **the old ReplicaSet** to 0 replicas.
This actually means that the Deployment manipulate ReplicaSet objects for you.

This process is known as `RollingUpdate`. 

```console
$ kubectl describe deployments emailservice-deployment-demo
Name:                   emailservice-deployment-demo
Namespace:              default
CreationTimestamp:      Thu, 28 Sep 2023 20:10:41 +0000
Labels:                 app=emailservice-demo
Annotations:            deployment.kubernetes.io/revision: 2
Selector:               app=emailservice-demo
Replicas:               3 desired | 3 updated | 3 total | 3 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=emailservice-demo
  Containers:
   server:
    Image:        gcr.io/google-samples/microservices-demo/emailservice:v0.8.0
    Port:         <none>
    Host Port:    <none>
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  emailservice-deployment-demo-976d85c7c (0/0 replicas created)
NewReplicaSet:   emailservice-deployment-demo-599c84db5d (3/3 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  76s   deployment-controller  Scaled up replica set emailservice-deployment-demo-976d85c7c to 3
  Normal  ScalingReplicaSet  30s   deployment-controller  Scaled up replica set emailservice-deployment-demo-599c84db5d to 1
  Normal  ScalingReplicaSet  28s   deployment-controller  Scaled down replica set emailservice-deployment-demo-976d85c7c to 2 from 3
  Normal  ScalingReplicaSet  28s   deployment-controller  Scaled up replica set emailservice-deployment-demo-599c84db5d to 2 from 1
  Normal  ScalingReplicaSet  26s   deployment-controller  Scaled down replica set emailservice-deployment-demo-976d85c7c to 1 from 2
  Normal  ScalingReplicaSet  25s   deployment-controller  Scaled up replica set emailservice-deployment-demo-599c84db5d to 3 from 2
  Normal  ScalingReplicaSet  23s   deployment-controller  Scaled down replica set emailservice-deployment-demo-976d85c7c to 0 from 1
```

If you look at the above Deployment closely, you will see that it first creates a new Pod, then deletes an old Pod, and creates another new one.
It does not kill old Pods until a sufficient number of new Pods have come up, and does not create new Pods until a sufficient number of old Pods have been killed. 


Deployment ensures that only a certain number of Pods are down while they are being updated.
By default, it ensures that at least 75% of the desired number of Pods are up (25% **max unavailable**).

Deployment also ensures that only a certain number of Pods are created above the desired number of Pods.
By default, it ensures that at most 125% of the desired number of Pods are up (25% **max surge**).

When you updated the Deployment, it created a new ReplicaSet (`emailservice-deployment-demo-599c84db5d`) and scaled it up to 1 and waited for it to come up.
Then it scaled down the old ReplicaSet to 2 and scaled up the new ReplicaSet to 2 so that at least 3 Pods were available and at most 4 Pods were created at all times.
It then continued scaling up and down the new and the old ReplicaSet, with the same rolling update strategy.
Finally, you'll have 3 available replicas in the new ReplicaSet, and the old ReplicaSet is scaled down to 0.

> [!IMPORTANT]
> During a RollingUpdate, new versions of an application are gradually rolled out while old versions are gradually scaled down. This means that for a brief period, both the old and new versions of the application may be running concurrently in the cluster.
> this simultaneous running of multiple versions can potentially lead to compatibility issues. For example, if the new version of the application introduces changes to the data schema or format that are incompatible with the old version, it can lead to issues when both versions are accessing the same data store concurrently.


#### Failed Deployment

A Deployment enters various states during its lifecycle.
It can be progressing while rolling out a new ReplicaSet, it can be complete while the Deployment scaled up its newest ReplicaSet, or it can fail to progress.

Sometimes, your Deployment may get stuck trying to deploy its newest ReplicaSet without ever completing. 
This could happen due to various reasons, for example, insufficient resources (CPU or RAM), or image pull errors.

The Deployment will try to reach its desire state for 10 minutes (this value can be changed in `.spec.progressDeadlineSeconds`), after that, the Deployment will indicate (in the Deployment status) that the Deployment progress has stalled.

Let's play with your deployment:

- Scale up and down your deployment
- Try to update the Deployment to the image `emailservice:v0.7.1`. What happened? How did you resolve?
