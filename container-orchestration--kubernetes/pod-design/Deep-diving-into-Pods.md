

In this tutorial we will take a closer look on Pods characteristics, how they are designed and scheduled on nodes properly. Please fasten your seat belt. 

Throughout this tutorial, we will work with the `frontend` service (the main service of the [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) app).

Let's create a `frontend` Pod:

```yaml
# k8s/resources-demo.yaml 

apiVersion: v1
kind: Pod
metadata:
  name: frontend-pod
  labels:
    app: frontend-demo
spec:
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

## Describe Pod

The `kubectl describe` command displays a comprehensive set of information about the specified pod:

```console
$ kubectl describe pod frontend-pod
Name:             frontend-pod
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 26 Oct 2023 18:53:00 +0000
Labels:           app=frontend-demo
Annotations:      <none>
Status:           Running
IP:               10.244.0.48
IPs:
  IP:  10.244.0.48
Containers:
  server:
    Container ID:   docker://04601c1f153a380555d343613db121e445bdcdc02963d549638c50fac7e770cd
    Image:          gcr.io/google-samples/microservices-demo/frontend:v0.8.0
    Image ID:       docker-pullable://gcr.io/google-samples/microservices-demo/frontend@sha256:048d9344b759afffd52f4585fb11ee5842f013857eec1136b60973f9ee2fc8f0
    Port:           8080/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Thu, 26 Aug 2023 18:53:01 +0000
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     100m
      memory:  128Mi
    Requests:
      cpu:     50m
      memory:  5Mi
    Environment:
      PORT:                          8080
      PRODUCT_CATALOG_SERVICE_ADDR:  productcatalogservice:3550
      CURRENCY_SERVICE_ADDR:         currencyservice:7000
      CART_SERVICE_ADDR:             cartservice:7070
      RECOMMENDATION_SERVICE_ADDR:   recommendationservice:8080
      SHIPPING_SERVICE_ADDR:         shippingservice:50051
      CHECKOUT_SERVICE_ADDR:         checkoutservice:5050
      AD_SERVICE_ADDR:               adservice:9555
      ENABLE_PROFILER:               0
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-8t2bj (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-8t2bj:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  33m   default-scheduler  Successfully assigned default/frontend-pod to minikube
  Normal  Pulled     33m   kubelet            Container image "gcr.io/google-samples/microservices-demo/frontend:v0.8.0" already present on machine
  Normal  Created    33m   kubelet            Created container server
  Normal  Started    33m   kubelet            Started container server
```


This command is very useful for diagnosing issues, understanding the current [state of a pod](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) and [containers](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-states), and gathering information for debugging purposes, [Pod conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions), Volumes, Network and Events.
