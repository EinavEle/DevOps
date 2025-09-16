
## Services

Every Pod in a cluster gets its own unique cluster-wide IP address, and Pods can communicate with all other pods on any other node. 

But using Pods IP is not practical. If you use a Deployment to run your app, that Deployment can create and destroy Pods dynamically. 
From one moment to the next, you don't know how many of those Pods are working and healthy; you might not even know what those healthy Pods are named. 
Kubernetes Pods are created and destroyed to match the desired state of your cluster.
Pods are ephemeral resources (you should not expect that an individual Pod is reliable and durable).

Enter **Services**.

The Service is an abstraction to help you expose **groups of Pods** over a network.
Each Service object defines a logical set of **Endpoints** (usually these endpoints are Pods) along with a policy about how to make those pods accessible.

The set of Pods targeted by a Service is usually determined by a `selector` that you define.

Here is an example for Service exposing port `8080` for all Pods in the cluster labelled by the `app: emailservice-demo` key and value (this was the Pod label in the `emailservice-deployment-demo` Deployment):

```yaml
# k8s/service-demo.yaml

apiVersion: v1
kind: Service
metadata:
  name: my-emailservice
spec:
  selector:
    app: emailservice-demo
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
```

Apply the above Service, and describe the created object:

```console
$ kubectl applt -f k8s/service-demo.yaml
service/my-emailservice created

$ kubectl describe svc my-emailservice
Name:              my-emailservice
Namespace:         default
Labels:            <none>
Annotations:       <none>
Selector:          app=emailservice-demo
Type:              ClusterIP
IP Family Policy:  SingleStack
IP Families:       IPv4
IP:                10.100.220.135
IPs:               10.100.220.135
Port:              <unset>  8080/TCP
TargetPort:        8080/TCP
Endpoints:         10.244.0.48:8080,10.244.0.51:8080,10.244.0.58:8080 + 1 more...
Session Affinity:  None
Events:            <none>
```

`Endpoints` are the set of Pods IP that the Service is routing traffic to. 
The controller for that Service continuously scans for Pods that match this selector.

You should now be able to communicate with the `my-emailservice` Service on `10.100.220.135:8080` (change the IP to your service IP) from any node in your cluster, and **the request will be randomly routed to one of the endpoints**. 

The above created service can be used only for consumption inside your cluster.

### Service DNS 

Kubernetes is shipped a internal DNS server, called [CoreDNS](https://coredns.io/), for resolving addresses and service discovery within the cluster. 
The CoreDNS server is running as a Pod in the `kube-system` namespace. 
It watches the Kubernetes API for new Services and creates a set of DNS records for each one.

Instead of accessing your service by its IP address, you can simply use the Service name as the domain name:

```bash 
curl -v --http2-prior-knowledge my-emailservice:8080
```

This request returns nothing, but the `200` status code indicates a successful communication with the server.

### Service type 

[Kubernetes Service types](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types) allow you to specify what kind of Service you want. Here is some of the main types:

- `ClusterIP` (the default type) - Exposes the Service on a cluster-internal IP, allow usage only from within the cluster. 
- `NodePort` - Exposes the Service on each Node's IP at a static port. 
- `LoadBalancer` - Exposes the Service externally using an external load balancer (e.g. AWS Application Load Balancer). This type requires integration between your Kubernetes cluster to a cloud provider.


Let's see an example of `NodePort`: 

```yaml
# k8s/service-nodeport-demo.yaml

apiVersion: v1
kind: Service
metadata:
  name: my-emailservice-external
spec:
  type: NodePort
  selector:
    app: emailservice-demo
  ports:
    - protocol: TCP
      nodePort: 30002
      port: 8080
      targetPort: 8080
```

When applying this Service, each node proxies the `port` (the same port number on every Node) into your Service.

This method allows you to access the Service from outside the cluster, by expose one or more nodes' IP addresses directly: 

```console
$ minikube ip
192.168.49.2

$ curl -v --http2-prior-knowledge  192.168.49.2:30002
```
