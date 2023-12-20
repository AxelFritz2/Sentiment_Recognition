FROM ubuntu:latest
LABEL authors="axel"

ENTRYPOINT ["top", "-b"]