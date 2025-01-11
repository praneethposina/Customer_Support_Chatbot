# Ubuntu as base image
FROM ubuntu:22.04

# environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=80

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

EXPOSE 80

# Start Ollama and Flask app
CMD ollama serve & python3 app.py
