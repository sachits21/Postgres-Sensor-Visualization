# syntax=docker/dockerfile:1.4
FROM ubuntu:22.04

# Install OS-level packages
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get --yes upgrade && \
    apt-get --yes install --no-install-recommends \
    python3.10-full tini build-essential

# Create and activate virtual environment
ENV VIRTUAL_ENV="/root/.venv"
RUN python3.10 -m venv "$VIRTUAL_ENV"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt /

# Update pip
RUN pip install -U pip
RUN pip install -r /requirements.txt

# Setup root home directory
WORKDIR /root/take_home_project

# Install package
COPY src src
COPY pyproject.toml ./
RUN pip install --editable .
EXPOSE 8000
ENTRYPOINT ["tini", "-v", "--"]
#CMD gunicorn --bind 0.0.0.0:8000 dash_app.server