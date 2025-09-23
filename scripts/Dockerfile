FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pillow requests

WORKDIR /app
COPY header-image.py /app/header-image.py

ENTRYPOINT ["python", "header-image.py"]

# Usage:
# docker build -t header-image .
#
#  docker run --rm -v $(pwd):/app header-image  "https://images.unsplash.com/photo-1651990892631-723da6447d7d" "async-agentic-coding.jpg"

# written by chatgpt