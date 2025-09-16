The demo code can be found under `youtube_subtitles_v4`.

1. Install requirements of both applications by: 

```bash
pip install -r youtube_subtitles_v4/frontend/requirements.txt
pip install -r youtube_subtitles_v4/worker/requirements.txt
```

2. Replace `YOUR_SQS_QUEUE_NAME_HERE`, `YOUR_SNS_TOPIC_NAME_HERE`, `YOUR_SERVER_URL` and `YOUR_REGION_HERE` with the correspondent values in both the `frontend/app.py` and `frontend/app.py`.
2. Under `youtube_subtitles_v4`, complete the `# TODO`s in `worker/worker.py` and `fronetend/app.py`. Make sure you understand the code, especially, the `/job_update` endpoint in `app.py`.
3. Launch the `frontend` service via Pycharm UI or by:

```bash
cd youtube_subtitles_v4/frontend
python app.py
```

Make sure the frontend successfully subscribed to the SNS topic. 

3. Launch the `worker` service via Pycharm UI or by:

```bash
cd youtube_subtitles_v4/worker
python worker.py
```

4. Visit the app in http://localhost:8080 and test it end to end.

