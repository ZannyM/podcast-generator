# Use the lastest ubuntu image
FROM ubuntu:latest

# update package list and install dependancies

RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/* 

RUN ln -s /usr/bin/python3.10 /usr/bin/python

# upgrade pip and install dependancies
RUN pip3 install --upgrade pip && \
    pip3 install --break-system-packages PyYAML

COPY feed.py /usr/bin/feed.py

COPY entrypoint.sh /entrypoint.sh 

# Ensure the entrypoint script has execution permissions
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]