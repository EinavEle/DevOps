### Exercise 1 - Expose the 2048 game outside the cluster

If you haven't done it yet, deploy the [2048 game dockerized image](https://hub.docker.com/r/alexwhen/docker-2048) as a Deployment in the cluster.

Inspired by the above `Ingress`, expose the 2048 app, so you can play the game using a public URL, without `port-forward`ing.  

### Exercise 2 - Canary using Nginx 

You can add [nginx annotations](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/) to specific Ingress objects to customize their behavior.

In some cases, you may want to "canary" a new set of changes by sending a small number of requests to a different service than the production service. 
The [canary annotation](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/#canary) enables the Ingress spec to act as an alternative service for requests to route to depending on the rules applied.

In this exercise we'll deploy a canary for the `frontend` service. 

- Make sure the Online Boutique service is up and running in your cluster.
- Deploy the YAML under `k8s/online-boutique/release-0.9.0-frontend.yaml` - this is a Deployment and Service of the `frontend` service version `0.9.0` (which you have `0.8.0` installed on your cluster). 
- If you haven't done it before, create an `Ingress` pointing to your main `frontend` Deployment.
- Create an `Ingress` pointing to your canary Deployment. Here is a skeleton with appropriate annotations: 

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: canary
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "5"
spec:
  ingressClassName: nginx
  rules:
     # TODO ....
```

This Ingress routes 5% of the traffic to the canary deployment. Make sure the `host` entry is the same as the main Ingress. 

- Test your configurations by periodically access the application. 

```bash
/bin/sh -c "while sleep 0.05; do (wget -q -O- http://LOAD_BALANCER_DOMAIN &); done"
```

**Bonus**: Use [different annotations](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/) to perform a canary deployment which routes users based on a request header `FOO=bar`, instead of specific percentage.

Similarly, you can use the Nginx ingress controller to split the traffic using [other strategies, like blue-green, or A/B testing](https://docs.nginx.com/nginx-service-mesh/tutorials/trafficsplit-deployments/). 

### Exercise 3 - Setup HTTPS connections with your ingress controller 

Generate a self-signed certificate and private key with (change values accordingly):

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout KEY_FILE -out CERT_FILE -subj "/CN=YOUR_HOST" -addext "subjectAltName = DNS:YOUR_HOST"
```

Then create the secret in the cluster via:

```bash
kubectl create secret tls CERT_NAME --key KEY_FILE --cert CERT_FILE
```

The resulting secret will be of type `kubernetes.io/tls`.

Inspired by https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/networking/tls-example-ingress.yaml, define your ingress to accept HTTPS requests.

You can force your incoming traffic to use HTTPS by adding the following annotation to the `ingress` object:

```text
nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
```