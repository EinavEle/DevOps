
As can be seen from the above YAML manifest and Pod description, when you specify a Pod, you can optionally specify how much of each resource (CPU and memory) a container needs: 

```text 
Limits:
  cpu:     100m
  memory:  128Mi
Requests:
  cpu:     50m
  memory:  5Mi
```

What do the **Limits** and **Requests** mean? 

### Resource limits

When you specify a resource **Limits** for a container, the **kubelet** enforces those limits, as follows:

- If the container tries to consume more than the allowed amount of memory, the system kernel terminates the process that attempted the allocation, with an out of memory (OOM) error.
- If the container tries to consume more than the allowed amount of CPU, it is just not allowed to do it.

Let's connect to the Pod and create an artificial CPU load, using he `stress` command:

```console 
$ kubectl exec -it frontend-pod -- /bin/sh
/src # apk update
...

/src # apk add stress-ng
(1/5) Installing judy (1.0.5-r1)
(2/5) Installing libmd (1.0.4-r2)
(3/5) Installing libbsd (0.11.7-r1)
(4/5) Installing liblksctp (1.0.19-r3)
(5/5) Installing stress-ng (0.14.00-r0)
Executing busybox-1.36.0-r9.trigger
OK: 25 MiB in 37 packages

/src # stress-ng --cpu 2 --vm 1 --vm-bytes 50M -v
stress-ng: info:  [723] defaulting to a 86400 second (1 day, 0.00 secs) run per stressor
stress-ng: info:  [723] dispatching hogs: 2 cpu, 1 vm
```

Watch the Pod's CPU and memory metrics in the Kubernetes UI Dashboard. Although the stress test tries to use 2 cpus, it's limited to 100m (100 mili-cpu, which is equivalent to 0.1 cpu), as specified in the `.resources.limits.cpu` entry.
In addition, the Pod **is** able to use a `50M` of memory as it's below the specified limit (128 megabytes). 

Let's try to use more than the memory limit:


```console
/src # stress-ng --cpu 2 --vm 1 --vm-bytes 500M -v
stress-ng: info:  [723] defaulting to a 86400 second (1 day, 0.00 secs) run per stressor
stress-ng: info:  [723] dispatching hogs: 2 cpu, 1 vm
```

Watch how the processed is killed by the kernel using a `SIGKILL` signal. 

### Resources requests 

While resources limits is quite straight forward, resources request has a completely different purpose. 

When you specify the resource **Requests** for containers in a Pod, the **kube-scheduler** uses this information to decide which node to place the Pod on. How?   

When a Pod is created, the kube-scheduler should select a Node for the Pod to run on. Each node has a maximum capacity for CPU and RAM. 
The scheduler ensures that the resource CPU and memory requests of the scheduled containers is less than the capacity of the node.

```console
$ kubectl get nodes
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   15d   v1.27.4

$ kubectl describe nodes minikube
Name:               minikube
[ ... lines removed for clarity ...]
Capacity:
  cpu:                2
  ephemeral-storage:  30297152Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             3956276Ki
  pods:               110
Allocatable:
  cpu:                2
  ephemeral-storage:  30297152Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             3956276Ki
  pods:               110
[ ... lines removed for clarity ...]
Non-terminated Pods:          (23 in total)
  Namespace                   Name                                          CPU Requests  CPU Limits  Memory Requests  Memory Limits  Age
  ---------                   ----                                          ------------  ----------  ---------------  -------------  ---
  default                     adservice-746b758986-vh7zt                    100m (5%)     300m (15%)  180Mi (4%)       300Mi (7%)     15d
  default                     cartservice-5d844fc8b7-rl7fp                  200m (10%)    300m (15%)  64Mi (1%)        128Mi (3%)     15d
  default                     checkoutservice-5b8645f5f4-gbpwn              50m (2%)      200m (10%)  64Mi (1%)        128Mi (3%)     15d
  default                     currencyservice-79b446569d-dqq7l              50m (2%)      200m (10%)  64Mi (1%)        128Mi (3%)     15d
  default                     emailservice-55df5dcf48-5ksdz                 50m (2%)      200m (10%)  64Mi (1%)        128Mi (3%)     15d
  default                     frontend-66b6775756-bxhbq                     50m (2%)      200m (10%)  64Mi (1%)        128Mi (3%)     15d
  default                     frontend-pod                                  50m (2%)      100m (5%)   5Mi (0%)         128Mi (3%)     50m
  default                     loadgenerator-78964b9495-rphvs                50m (2%)      500m (25%)  256Mi (6%)       512Mi (13%)    15d
  default                     paymentservice-8f98685c6-cjcmx                50m (2%)      200m (10%)  64Mi (1%)        128Mi (3%)     15d
  default                     productcatalogservice-5b9df8d49b-ng6pz        100m (5%)     200m (10%)  64Mi (1%)        128Mi (3%)     15d
  default                     recommendationservice-5b4bbc7cd4-rkdft        50m (2%)      200m (10%)  220Mi (5%)       450Mi (11%)    15d
  default                     redis-cart-76b9545755-nr785                   70m (3%)      125m (6%)   200Mi (5%)       256Mi (6%)     15d
  default                     shippingservice-648c56798-m8vjh               100m (5%)     200m (10%)  64Mi (1%)        128Mi (3%)     15d
  kube-system                 coredns-5d78c9869d-jkx8m                      100m (5%)     0 (0%)      70Mi (1%)        170Mi (4%)     15d
  kube-system                 etcd-minikube                                 100m (5%)     0 (0%)      100Mi (2%)       0 (0%)         15d
  kube-system                 kube-apiserver-minikube                       250m (12%)    0 (0%)      0 (0%)           0 (0%)         15d
  kube-system                 kube-controller-manager-minikube              200m (10%)    0 (0%)      0 (0%)           0 (0%)         15d
  kube-system                 kube-proxy-kv6m6                              0 (0%)        0 (0%)      0 (0%)           0 (0%)         15d
  kube-system                 kube-scheduler-minikube                       100m (5%)     0 (0%)      0 (0%)           0 (0%)         15d
  kube-system                 metrics-server-7746886d4f-t5btd               100m (5%)     0 (0%)      200Mi (5%)       0 (0%)         15d
  kube-system                 storage-provisioner                           0 (0%)        0 (0%)      0 (0%)           0 (0%)         15d
  kubernetes-dashboard        dashboard-metrics-scraper-5dd9cbfd69-lm4s2    0 (0%)        0 (0%)      0 (0%)           0 (0%)         15d
  kubernetes-dashboard        kubernetes-dashboard-5c5cfc8747-86kzb         0 (0%)        0 (0%)      0 (0%)           0 (0%)         15d
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests      Limits
  --------           --------      ------
  cpu                1820m (91%)   2925m (146%)
  memory             1743Mi (45%)  2840Mi (73%)
```

By looking at the “Pods” section, you can see which Pods are taking up space on the node.

Note that although actual memory resource usage on nodes is low (`45%`), the scheduler still refuses to place a Pod on a node if the memory request is more than the available capacity of the node. 
This protects against a resource shortage on a node when resource usage later increases, for example, during a daily peak in request rate.

Test it yourself! Try to change the `.resources.request.cpu` to a larger value (e.g. `300m` instead of `50m`), and re-apply the Pod. What happened? 

Since the total CPU requests on that node is `91%` (`1820m` out of `2000m` CPU), you can see that if a new Pod requests more than `180m` or more than `1.2Gi` of memory, that Pod will not fit on that node.

> [!NOTE]
> In Production, always specify resource request and limit. It allows an efficient resource utilization and ensures that containers have the necessary resources to run effectively and scale as needed within the cluster.

## Configure Quality of Service for Pods

What happened if a container exceeds its memory request and the node that it runs on becomes short of memory overall? it is likely that the Pod the container belongs to will be **evicted**.

When you create a Pod, Kubernetes assigns a **Quality of Service (QoS) class** to each Pod as a consequence of the resource constraints that you specify for the containers in that Pod.
QoS classes are used by Kubernetes to decide which Pods to evict from a Node experiencing [Node Pressure](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/). 

1. [Guaranteed](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed) - The Pod specifies resources request and limit. CPU and Memory requests and limit are equal.
2. [Burstable](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable) - The Pod specifies resources request and limit. But CPU and Memory requests and limit are not equal.
3. [BestEffort](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#besteffort) - The Pod does not specify resources request or limit for some of its containers.


When a Node runs out of resources, Kubernetes will first evict `BestEffort` Pods running on that Node, followed by `Burstable` and finally `Guaranteed` Pods.
When this eviction is due to resource pressure, **only Pods exceeding resource requests are candidates** for eviction.

Try to simulate Node pressure by overloading the node from a `Guaranteed` Pod, `Burstable` Pod and `BestEffort` Pod, and see the behaviour. 
