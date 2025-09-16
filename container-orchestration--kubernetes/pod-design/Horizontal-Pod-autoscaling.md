
A **HorizontalPodAutoscaler** (HPA for short) automatically updates the number of Pods to match demand, usually in a Deployment or StatefulSet.

The HorizontalPodAutoscaler controller periodically (by default every 15 seconds) adjusts the desired scale of its target (for example, a Deployment) to match observed metrics such as average CPU utilization, average memory utilization, or any other custom metric you specify.
The common use for HPA is to configure it to fetch metrics from a [Metrics Server](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/#metrics-server) API (should be installed as an add-on). 
Every 15 seconds, the HPA controller queries the Metric Server and fetches resource utilization metrics (e.g. CPU, Memory) for each Pod that are part of the HPA. 
The controller then calculates the desired replicas, and scale in/out based on the current replicas.

To demonstrate a HorizontalPodAutoscaler, you will first create a Deployment and a Service:

```yaml
# k8s/hpa-demo.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-hpa-demo
spec:
  selector:
    matchLabels:
      app: frontend-hpa-demo
  template:
    metadata:
      labels:
        app: frontend-hpa-demo
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
              memory: 64Mi
            limits:
              cpu: 80m
              memory: 128Mi
---
apiVersion: v1
kind: Service
metadata:
  name: frontend-hpa-demo-service
spec:
  selector:
    app: frontend-hpa-demo
  ports:
  - name: http
    port: 80
    targetPort: 8080
```

Now that the `frontend-hpa-demo` server is running, create the autoscaler:

```yaml
# k8s/hpa-autoscaler-demo.yaml

apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: frontend-hpa-demo
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: frontend-hpa-demo
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 60
```

When defining the pod specification, the resource **Requests**, like CPU and memory must be specified.
This is used to determine the resource utilization and used by the HPA controller to scale the target up or down.
In the above example, the HPA will scale up once the Pod is reaching 60% of the `.resources.requests.cpu`. 


Next, let's see how the autoscaler reacts to increased load. 
To do this, you'll start a different Pod to act as a client. 
The container within the client Pod runs in an infinite loop, sending queries to the `frontend-hpa-demo-service` service.

```bash 
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.05; do (wget -q -O- http://frontend-hpa-demo-service &); done"
```
