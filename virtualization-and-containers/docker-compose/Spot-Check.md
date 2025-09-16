The startup order of different services in docker compose is sometimes critical. In the above tutorial, it's clear that the `web` service depends on the `redis` service. Add the `depends_on` directive to your `docker-compose.yml` file to specify explicit startup order.

<details>
  <summary>
     Solution
  </summary>

```bash
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/code
    environment:
      FLASK_DEBUG: "true"
    depends_on:
      - redis
  redis:
    image: "redis:alpine"
```

</details>