FROM python:3-alpine

LABEL maintainer="Matthias Sommer, matthiassommer@posteo.de"

COPY data/example_input.csv /data/
COPY src /
COPY config.txt /

ENTRYPOINT [ "python", "./main.py" ]