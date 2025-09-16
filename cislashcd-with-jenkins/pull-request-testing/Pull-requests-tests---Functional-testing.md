Functional testing evaluates whether the app works as intended. 
It involves testing the application against some pre-defined scenario (usually the common scenario of your customers), and ensure that the software meets its functional objectives.

Implement functional testing in the `pr-testing.Jenkinsfile` under the **Functional test** stage. 

- Build a docker container for the app.
- Run the container in the background, while publishing the correct ports.
- Analyze simple sentences with clear sentiments:

```shell
# Sentence: Intel is happy and excited to launch the new generation of processors
# Expect positive labels: optimism, excitement
curl localhost:8081/analyze?text=Intel%20is%20happy%20and%20excited%20to%20launch%20the%20new%20generation%20of%20processors

# Sentence: This is terrible movie
# Expect negative labels: disappointment, disgust, fear
curl localhost:8081/analyze?text=This%20is%20terrible%20movie.

# Sentence: This is terrible movie
# Expect neutral labels: neutral
curl localhost:8081/analyze?text=This%20is%20a%20neutral%20statement
```

- Compare the results to the expected sentiments.
- Stop and remove the container from disk.

**Note**: In general, running services within the Jenkins agent, as we did in the above testing, is not a good idea. It's better to deploy the application under test (AUT) in test environments. 
