Create a Docker Compose project in the `docker-compose.yaml` file to provision the service (all 3 microservices) in a single command (`docker compose up`).
Deploy the compose project locally.

Deployment notes:

- Don't configure your compose file to build the images. Instead, push the `yolo5` and `polybot` images to DockerHub or an [ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-console.html) repo and use these images. 
- Don't manage AWS credentials yourself, and **never** hard-code AWS credentials in the `docker-compose.yaml` file. 
- Don't hard-code your telegram token in the compose file, this is a sensitive data. [Read here](https://docs.docker.com/compose/use-secrets/) how to provide your compose project this data in a safe way.  
- Use `snyk` to clean your images from any HIGH and CRITICAL security vulnerabilities.
