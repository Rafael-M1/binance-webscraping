FROM python:3.13.2-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir playwright -vv \
    && playwright install --with-deps --only-shell chromium

COPY . /app

CMD ["python", "main.py"]