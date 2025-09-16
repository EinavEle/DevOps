Docker multi-stage builds are used to create optimized Docker images by copying artifacts you build in other images into your main image. Here's a simple example demonstrating the use of multi-stage builds:
```bash
FROM golang:1.17 AS builder
WORKDIR /app
COPY . .
RUN go build main.go

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/main .
ENTRYPOINT ["./main"]
```
In the first build stage (the `builder` image), we use the `golang:1.17` image which contains the Go programming language and its development tools pre-installed. We then copy our source code and compile our app using the `go build` build tool. We ended up with a single binary (also known as **Build Artifact**), which contains all we need to run our app.

Now that our app is compiled and packed into a single artifact, we have nothing to do with the Go compiler and other Go-specific tools that were needed to compile and build our Go application, which are part of the `golang:1.17` image. Instead of working hard to clean and minimize our original image, we are starting **another build stage** using the `alpine:latest` base image and copy into it only what we need - the compiled `/app/myapp` artifact from the previous build image.

At the end, Docker discards any intermediate build and keeps only the final stage image. By using multi-stage builds, we can take advantage of the build stage to compile and build the application, and then copy only the necessary artifacts into the final stage, resulting in a smaller and more optimized Docker image.