
Deploy 2 EC2 instances within your VPC, in each instance, run our so-called simple flask webserver. 

We will use the `locust` Python package to perform a load test.
[Locust](https://docs.locust.io/en/stable/quickstart.html) is an easy to use, scriptable and scalable performance testing tool.

Install it by:

```bash
pip install locust
```

Take a look on the file under Launch the locust test UI by:

```bash 
cd http_load_test
locust
```

Open http://localhost:8089. 
Provide the host name of your server and try it out!

During the load test, turn off one of your instance, observe the behavior.


## Spot check

When you turned of one of your registered ALB instances, how long did it take for the ALB to stop routing traffic?

<details>
  <summary>
     Solution
  </summary>
    For target group with default Health Checks:   
    - Unhealthy threshold = 2 consecutive health check failures
    - Interval = 30 seconds

    So it takes 1 minutes for the LB to stop routing traffic to the unhealthy instance. 
</details>