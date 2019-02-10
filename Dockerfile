FROM python:3.7-slim

COPY data/example_input.csv /data/
COPY gpx_converter.py /

CMD ["python", "./gpx_converter.py"]