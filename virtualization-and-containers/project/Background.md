In this project, you'll design, develop and deploy an object detection service that consists of multiple containerized microservices. 

Users send images through an interactive Telegram bot, the service detects objects in the image and send the results to the user.

The service consists of 3 microservices: 

- `polybot`: Telegram Bot container.
- `yolo5`: Image prediction container based on the Yolo5 pre-train deep learning model.
- `mongo`: MongoDB cluster to store data.
