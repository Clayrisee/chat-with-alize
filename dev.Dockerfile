FROM python:3.9.16-slim-bullseye

WORKDIR /workspace


RUN apt update -q && apt install -yq wget git

COPY requirements.txt ./

RUN pip install --upgrade pip \
    && pip --default-timeout=1000 install --user -r requirements.txt