FROM python:3.7-slim

LABEL maintainer="matthiassommer@posteo.de"

COPY data/example_input.csv /data/
COPY src /
COPY config.txt /

CMD ["python", "./main.py"]