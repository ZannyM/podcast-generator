# Use the lastest ubuntu image
FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-venv \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install PyYAML

# Set PATH to use virtual environment
ENV PATH="/venv/bin:$PATH"
COPY feed.py /usr/bin/feed.py

COPY entrypoint.sh /entrypoint.sh 

# Ensure the entrypoint script has execution permissions
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]