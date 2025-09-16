|||important
The tutorial should be done on your EKS cluster.
|||


The Kubernetes networking model facilitates communication between pods within a cluster, and from the outside world into the cluster.

- Pods can communicate with each other using their internal IP addresses. 
  Every pod in a cluster can reach every other pod without NAT.
- **Services** provide a stable endpoint (`ClusterIP`) that abstracts the underlying pod instances. Services enable load balancing and automatic discovery of pod changes.
  Pods can use the service name as a DNS entry to connect to other services.
- The **kube-proxy** is a network proxy that runs on each node in your cluster. It allows network communication to your Pods from network sessions inside or outside your cluster.


So far, we've seen how to use Services to publish services only for consumption **inside your cluster**.

## Expose applications outside the cluster using a Service of type `LoadBalancer`

Kubernetes allows you to create a Service of `type=LoadBalancer` (no need to apply the below example):

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: LoadBalancer
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
  clusterIP: 10.0.171.239
```

This Service takes effect only on cloud providers which support external load balancers (like AWS ELB). 
Applying this Service will **provision a load balancer for your Service**. 

![.guides/img/k8s_lb-service](./k8s_lb-service.png)


Traffic from the Elastic Load Balancer is directed to the backend Pods by the Service. The cloud provider decides how it is load balanced across different cluster's Nodes.

Note than the actual creation of the load balancer happens asynchronously, and information about the provisioned balancer is published in the Service's `.status.loadBalancer` field.
