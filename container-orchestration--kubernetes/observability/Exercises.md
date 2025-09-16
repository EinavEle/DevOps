
> Before start, make sure the online boutique service is deployed and specifically the 
> load generator service is working well.
> The load generator application creates realistic usage patterns on the website using Locust load generator.


### Exercise 1 -  Investigate service regression issues

Let's see how to use Grafana in order to find performance issue in your app. 

1. Apply a version of the Online Boutique with injected issues: 

```bash
kubectl apply -f k8s/online-boutique/release-0.8.0-performence-issue.yaml
```

2. Wait a few minutes to let the load generator to create some synthetic load. 

Let's say your customers are complaining about the responsiveness of the website. It became REALLY slow. 
You try to find which microservice responsible for the latency increase and to which extent.  

3. In your Grafana server, go to the **Explore** page. 
4. Try to use the query wizard to investigate. You can take a look on the pod's raw logs, but it's better if you visualize it. Hints:

   - You can query the data using a [Lucene QL](https://www.elastic.co/guide/en/kibana/7.17/lucene-query.html).
   - The `http.resp.took_ms` value can help.
   - If you want to "group-by" do it with fields end with `.keyword`.

5. When you're done, take a look on the `k8s/online-boutique/release-0.8.0-performence-issue.yaml` file, fix the relevant values and deploy a fixed version. 