FROM python:3.10-buster

RUN mkdir -p /Projet_Linux

WORKDIR /Projet_Linux

COPY . .

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install virtualenv

RUN bash ./install.sh

CMD bash main.sh