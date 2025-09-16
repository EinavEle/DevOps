
A **probe** is a diagnostic performed periodically by the **kubelet** on a container, usually by an HTTP request, to check the container status. 

- **Liveness probes** are used to determine the health of a container (a.k.a. health check), by a periodic checks. The container is restarting if the probe fails.
- **Readiness probes** are used to determine whether a Pod is ready to receive traffic (when it is prepared to accept requests, preventing traffic from being sent to Pods that are not fully operational, mostly because the pod is still initializing, or is about to terminate as part of a rolling update).

> [!NOTE]
> In Production, always specify Liveness and Readiness probes, they are essential to ensure the availability and proper functioning of applications within Pods.

### Define a Liveness probe

The `frontend` service exposes an endpoint called `/_healthz`. Upon an HTTP request, if the endpoint returns a `200` status code, it means "the server is alive".

In the below example, the `livenessProbe` entry defines a liveness probe for our Pod. 
Note the `command` and `args` entries, which override the default container command to intentionally terminate the server process after 60 seconds.
This behaviour simulates the case where the server is becoming unhealthy, and we expect the liveness probe to fail.  

```yaml
# k8s/liveness-demo.yaml

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
    command: ["sh", "-c"]
    args: ["timeout 60s /src/server; sleep 6000"]
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
    livenessProbe:
      initialDelaySeconds: 10
      httpGet:
        path: "/_healthz"
        port: 8080
```

After 60 seconds, the prob HTTP requests to `_healthz` will fail, thus, the **kubelet** will restart the container.

This restarting mechanism helps the application to be more available.
For example, when the server is entering a deadlock (the application is running, but unable to make progress),
restarting the container in such a state can help to make the application more available despite bugs.

By default, the HTTP probe is done every 10 seconds, and should be low-cost, it shouldn't affect the application performance. 

### Define a Readiness probe

Sometimes, applications are temporarily unable to serve traffic.
For example, an application might need to load large data or configuration files during startup, or depend on external services after startup. 
In such cases, you don't want to kill the application, but you don't want to send it requests either.

Kubernetes provides readiness probes to detect and mitigate these situations. 
A pod with containers reporting that they are not ready does not receive traffic through Kubernetes Services.

Readiness probes are configured similarly to liveness probes:

```yaml
# k8s/readiness-demo.yaml

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
#    command: ["sh", "-c"]
#    args: ["timeout 60s /src/server; sleep 6000"]
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
    livenessProbe:
      initialDelaySeconds: 10
      httpGet:
        path: "/_healthz"
        port: 8080
    readinessProbe:
      initialDelaySeconds: 10
      httpGet:
        path: "/"
        port: 8080
```

Usually a server has a dedicated endpoint for readiness probes. 
But in the above example, we use the default endpoint (`/`) to perform the readiness probe HTTP request.

Since the content served by the `/` endpoint depends on the currency service (`currencyservice`), if you scale it down to **0**, you'll notice how the readiness probe is failing:

```bash
kubectl scale deployment currencyservice --replicas=0
```

#### Readiness probes are critical to perform a successful rolling update 

In the context of a rolling update, readiness probes play a crucial role in ensuring a seamless transition.
When old replicaset Pods receive the SIGTERM signal from the kubelet, the Pod should start a graceful termination process. First of all it should stop receiving new requests.
By failing the readiness probes, the Pod indicates that it's not ready to receive new traffic. 
