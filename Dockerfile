FROM ghcr.io/astral-sh/uv:python3.11-bookworm

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*
