FROM python:3

ADD gpx_converter.py /
ADD data/barny_01_19.csv /data/

CMD ["python", "./gpx_converter.py"]