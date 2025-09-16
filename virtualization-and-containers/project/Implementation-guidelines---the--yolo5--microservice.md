
[Yolo5](https://github.com/ultralytics/yolov5) is a state-of-the-art object detection AI model. It is known for its high accuracy object detection in images and videos.
You'll work with a lightweight model that can detect [80 objects](https://github.com/ultralytics/yolov5/blob/master/data/coco128.yaml) while running on your old, poor, CPU machine. 

The service files are under the `docker_project/yolo5` directory. Copy these files to your repo.

#### Develop the app

The `yolo5/app.py` app is a flask based webserver, with a single endpoint `/predict`, which can be used to predict objects in images.  

To use this endpoint, you don't send the image directly in the HTTP request. Instead, you attach a query parameter called `imgName` to the URL (e.g. `localhost:8081/predict?imgName=street.jpeg`), which represents an image name stored in an **S3 bucket**. 
The service downloads this image from the S3 bucket and detect objects in it. 

Take a look on the code, and complete the `# TODO`s. Feel free to change/add any functionality as you wish!

#### Build and run the app

The `yolo5` app can be running only as a Docker container. This is because the app depends on many files that don't exist on your local machine, but do exist in the [`ultralytics/yolov5`](https://hub.docker.com/r/ultralytics/yolov5) base image.

Take a look at the provided `Dockerfile`, it's already implemented for you, no need to touch.

If you run the container on your local machine, you may need to **mount** (as a volume) the directory containing the AWS credentials on your local machine (`$HOME/.aws/credentials`) to allow the container communicate with S3.  

**Note: Never build a docker image with AWS credentials stored in it! Never commit AWS credentials in your source code! Never!**

Once the image was built and run successfully, you can communicate with it directly by:

```bash
curl -X POST localhost:8081/predict?imgName=street.jpeg
```

For example, here is an image and the corresponding results summary:

<img src=".guides/img/image5.png" width="60%">


```json
{
    "prediction_id": "9a95126c-f222-4c34-ada0-8686709f6432",
    "original_img_path": "data/images/street.jpeg",
    "predicted_img_path": "static/data/9a95126c-f222-4c34-ada0-8686709f6432/street.jpeg",
    "labels": [
      {
        "class": "person",
        "cx": 0.0770833,
        "cy": 0.673675,
        "height": 0.0603291,
        "width": 0.0145833
      },
      {
        "class": "traffic light",
        "cx": 0.134375,
        "cy": 0.577697,
        "height": 0.0329068,
        "width": 0.0104167
      },
      {
        "class": "potted plant",
        "cx": 0.984375,
        "cy": 0.778793,
        "height": 0.095064,
        "width": 0.03125
      },
      {
        "class": "stop sign",
        "cx": 0.159896,
        "cy": 0.481718,
        "height": 0.0859232,
        "width": 0.053125
      },
      {
        "class": "car",
        "cx": 0.130208,
        "cy": 0.734918,
        "height": 0.201097,
        "width": 0.108333
      },
      {
        "class": "bus",
        "cx": 0.285417,
        "cy": 0.675503,
        "height": 0.140768,
        "width": 0.0729167
      }
    ],
    "time": 1692016473.2343626
}
```

The model detected a _person_, _traffic light_, _potted plant_, _stop sign_, _car_, and a _bus_. Try it yourself with different images.
