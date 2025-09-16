Try to reduce the size of our `my_flask_app:0.0.1` image. Re-build and check the resulting image size.

<details>
  <summary>
     Solution
  </summary>

```bash
FROM python:3.8.12-slim-buster
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python3", "app.py"]
```
- When `--no-cache-dir` is specified, `pip` doesn't cache the downloaded packages.
- The `apt clean` command removes all the package files from the local cache l
- The command `rm -rf /var/lib/apt/lists/*` is used to remove the package lists from the `apt` cache directory.

</details>