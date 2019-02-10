FROM python:3.7-slim

ADD gpx_converter.py /
ADD data/example_input.csv /data/

CMD ["python", "./gpx_converter.py"]