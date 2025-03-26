FROM python:3.13.2-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    bash \
    chromium \
    chromium-driver \
    libnss3 \
    libfreetype6 \
    libharfbuzz0b \
    ca-certificates \
    fonts-liberation 

RUN pip install --upgrade pip
RUN pip install playwright -vv
RUN playwright install --with-deps chromium

COPY . /app

CMD ["python", "main.py"]