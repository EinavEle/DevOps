There are some circumstances where you may want to control which node the Pod is deployed on.
For example, to ensure that a Pod ends up on a node with an SSD attached to it, or to co-locate Pods from two different services that communicate a lot into the same availability zone.

You can constrain a Pod so that it is restricted to run on particular node(s), or to prefer to run on particular nodes. 

First, let's add another node to your Minikube cluster:

```bash 
minikube node add
```

> [!WARNING]
> As multinode clusters in Minikube is currently experimental, there might be networking and DNS issues.
> Make sure to delete the node when you're done. 

Like many other Kubernetes objects, nodes have **labels**. We will use  [label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to assign Pods to Nodes. 
Kubernetes populates a standard set of labels on all nodes in a cluster:

```console
$ kubectl get nodes --show-labels
minikube       Ready    control-plane   22d   v1.27.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=minikube,kubernetes.io/os=linux,minikube.k8s.io/commit=fd7ecd9c4599bef9f04c0986c4a0187f98a4396e,minikube.k8s.io/name=minikube,minikube.k8s.io/primary=true,minikube.k8s.io/updated_at=2023_10_11T07_10_41_0700,minikube.k8s.io/version=v1.31.2,node-role.kubernetes.io/control-plane=,node.kubernetes.io/exclude-from-external-load-balancers=
minikube-m02   Ready    <none>          69s   v1.27.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=minikube-m02,kubernetes.io/os=linux
```

Let's manually attach the label `gpu=true` to one of your nodes:

```console
$ kubectl label nodes minikube-m02 gpu=true
node/minikube-m02 labeled
```

### Node selectors

There are [several ways](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) to facilitate the Node selection, [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) is the simplest recommended form. 
You can add the `nodeSelector` field to your Pod specification and specify the node labels you want the target node to have.
Kubernetes only schedules the Pod onto nodes that have each of the labels you specify.

```yaml
# k8s/node-selector-demo.yaml

apiVersion: v1
kind: Pod
metadata:
  name: frontend-pod
  labels:
    app: frontend-demo
spec:
  nodeSelector:
    gpu: 'true'
  containers:
  - name: server
    image: gcr.io/google-samples/microservices-demo/frontend:v0.8.0
    ports:
      - containerPort: 8080
    env:
      - name: PORT
        value: "8080"
      - name: PRODUCT_CATALOG_SERVICE_ADDR
        value: "productcatalogservice:3550"
      - name: CURRENCY_SERVICE_ADDR
        value: "currencyservice:7000"
      - name: CART_SERVICE_ADDR
        value: "cartservice:7070"
      - name: RECOMMENDATION_SERVICE_ADDR
        value: "recommendationservice:8080"
      - name: SHIPPING_SERVICE_ADDR
        value: "shippingservice:50051"
      - name: CHECKOUT_SERVICE_ADDR
        value: "checkoutservice:5050"
      - name: AD_SERVICE_ADDR
        value: "adservice:9555"
      - name: ENABLE_PROFILER
        value: "0"
    resources:
      requests:
        cpu: 50m
        memory: 5Mi
      limits:
        cpu: 100m
        memory: 128Mi
```

Make sure the Pod has been scheduled on the labelled Node. 

Try to delete the Node and re-apply the Pod. What happened? 

### Taints and Tolerations

We've seen that Node Selector is a simple mechanism to attract a Pod on specific Node (or group of nodes) by a label.
This technique is useful, for example, to schedule Pods on Nodes with specific hardware specification.

But what if we want to ensure that **only** those specific Pods use the dedicated Node?
For example, Nodes with an expensive GPU, it is desirable to keep pods that don't need the GPU off of those nodes, thus leaving room for later-arriving pods that do need the GPU. 

**Taints and Tolerations** can help us.

[Taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) allow a node to **repel** a set of pods.

Let's add a **taint** to a node using `kubectl taint`:

```bash 
kubectl taint nodes minikube-m02 gpu=true:NoSchedule
```

The taint has key `gpu`, value `true`, and taint effect `NoSchedule`.
This means that **no pod will be able to schedule** onto `minikube-m02` unless it has a matching **toleration**.

A **Tolerations** allow the scheduler to schedule pods with matching taints.
To tolerate the above taint, you can specify toleration in the pod specification.

```yaml
# k8s/taint-toleration-demo.yaml

apiVersion: v1
kind: Pod
metadata:
  name: frontend-pod
  labels:
    app: frontend-demo
spec:
  nodeSelector:
    gpu: true
  tolerations:
  - key: "gpu"
    operator: "Equal"
    value: "true"
    effect: "NoSchedule"
  containers:
  - name: server
    image: gcr.io/google-samples/microservices-demo/frontend:v0.8.0
    ports:
      - containerPort: 8080
    env:
      - name: PORT
        value: "8080"
      - name: PRODUCT_CATALOG_SERVICE_ADDR
        value: "productcatalogservice:3550"
      - name: CURRENCY_SERVICE_ADDR
        value: "currencyservice:7000"
      - name: CART_SERVICE_ADDR
        value: "cartservice:7070"
      - name: RECOMMENDATION_SERVICE_ADDR
        value: "recommendationservice:8080"
      - name: SHIPPING_SERVICE_ADDR
        value: "shippingservice:50051"
      - name: CHECKOUT_SERVICE_ADDR
        value: "checkoutservice:5050"
      - name: AD_SERVICE_ADDR
        value: "adservice:9555"
      - name: ENABLE_PROFILER
        value: "0"
    resources:
      requests:
        cpu: 50m
        memory: 5Mi
      limits:
        cpu: 100m
        memory: 128Mi
```

The above defined toleration would allow to schedule the Pod onto `minikube-m02`.

**Note**: Taints and Tolerations **do not** guarantee that the pods only prefer these nodes. 
So the pods may be scheduled on the other untainted nodes. 
To guarantee that group of pods would be scheduled on a node, and **only** them, both **node selector** and **taint and tolerations** should be used.

To remove the taint: 

```bash 
kubectl taint nodes minikube-m02 gpu=true:NoSchedule-
```
