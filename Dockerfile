FROM python:3.7-slim

LABEL maintainer="matthiassommer@posteo.de"

COPY data/example_input.csv /data/
COPY gpx_converter.py /

CMD ["python", "./gpx_converter.py"]