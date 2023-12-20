FROM python:3.10-buster

RUN mkdir -p /Projet_Linux

WORKDIR /Projet_Linux

COPY . .

RUN apt-get update && \
    apt-get install -y <autres dépendances nécessaires>

RUN bash ./install.sh

CMD bash main.sh
