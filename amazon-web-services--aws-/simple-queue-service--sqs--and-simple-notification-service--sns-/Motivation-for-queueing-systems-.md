As a motivation example for using queues systems, let's build simple "speech-to-text" system, inspired by the YouTube automatic speech recognition. 

YouTube's video subtitle feature provide users with a text-based translations of the spoken content in the video.
YouTube's automatic speech recognition system uses AI algorithms to analyze the audio content of videos and convert spoken words into text in a near-real-time latency. 

Our system is composed by two microservices (`frontend` and `worker`) as described below:

![.guides/img/youtube_subtitle_v1](./youtube_subtitle_v1.gif)

1. The `frontend` microservice acts as a user web interface, allows users to provide a link to YouTube video and click the submit button to start the processing (**step 1**).
2. The `frontend` create an HTTP request to the `worker` microservice (**step 2**) that responsible for downloading the video from YouTube servers, convert the audio file format and recognize text in the audio file using an AI model called [`openai/whisper-tiny`](https://huggingface.co/openai/whisper-tiny) (**step 3**).
3. The `worker` service then responds to the `frontend` service with the resulted text (**step 4**).
4. The `frontend` service responds to the end-user (**step 5**).


Let's do it...

### Demonstration

The demo code can be found under `youtube_subtitles_v1`.

1. Install requirements of both applications by: 

```bash
pip install -r youtube_subtitles_v1/frontend/requirements.txt
pip install -r youtube_subtitles_v1/worker/requirements.txt
```

2. Launch the `frontend` service via Pycharm UI or by:

```bash
cd youtube_subtitles_v1/frontend
python app.py
```

3. Launch the `worker` service via Pycharm UI or by:

```bash
cd youtube_subtitles_v1/worker
python worker.py
```

4. Visit the app in http://localhost:8080
5. Enter some youtube video (the video should be public and not contain age limit restriction).
6. Observe how does the `forntend` service request the `worker` service to analyse the video. 

