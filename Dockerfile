FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip virtualenv

RUN mkdir -p Projet_Linux

WORKDIR /Projet_Linux

COPY . .

RUN bash ./install.sh

CMD bash main.sh