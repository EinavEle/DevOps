Let's see Kubernetes cluster in all his glory! 

**Online Boutique** is a microservices demo application, consists of an 11-tier microservices.
The application is a web-based e-commerce app where users can browse items, add them to the cart, and purchase them.

Here is the app architecture and description of each microservice:

![](./k8s_online-boutique-arch.png)


| Service                                              | Language      | Description                                                                                                                       |
| ---------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| frontend                           | Go            | Exposes an HTTP server to serve the website. Does not require signup/login and generates session IDs for all users automatically. |
| cartservice                     | C#            | Stores the items in the user's shopping cart in Redis and retrieves it.                                                           |
| productcatalogservice | Go            | Provides the list of products from a JSON file and ability to search products and get individual products.                        |
| currencyservice             | Node.js       | Converts one money amount to another currency. Uses real values fetched from European Central Bank. It's the highest QPS service. |
| paymentservice               | Node.js       | Charges the given credit card info (mock) with the given amount and returns a transaction ID.                                     |
| shippingservice             | Go            | Gives shipping cost estimates based on the shopping cart. Ships items to the given address (mock)                                 |
| emailservice                   | Python        | Sends users an order confirmation email (mock).                                                                                   |
| checkoutservice             | Go            | Retrieves user cart, prepares order and orchestrates the payment, shipping and the email notification.                            |
| recommendationservice | Python        | Recommends other products based on what's given in the cart.                                                                      |
| adservice                         | Java          | Provides text ads based on given context words.                                                                                   |
| loadgenerator                 | Python/Locust | Continuously sends requests imitating realistic user shopping flows to the frontend.                                              |


To deploy the app in you cluster, perform the below command from the root directory of your shared repo (make sure the YAML file exists): 

```bash 
kubectl apply -f k8s/online-boutique/release-0.8.0.yaml
```

By default, applications running within the cluster are not accessible from outside the cluster.
There are various techniques available to enable external access, we will cover some of them later on.

Using port forwarding allows developers to establish a temporary tunnel for debugging purposes and access applications running inside the cluster from their local machines.

```bash
# Change nginx-75f59d57f4-4nd6q to the name of the Pod
kubectl port-forward svc/frontend 8080:80
```

> Note:   
> If you run minikube on a remote machine, and want to access the application using the EC2 public ip address, perform:
> 
> ```bash
> kubectl port-forward svc/frontend 8080:80 --address 0.0.0.0
> ```
