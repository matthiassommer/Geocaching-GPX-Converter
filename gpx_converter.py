"""
Created on Sun Sep 24 2017

@author: Matthias Sommer

minimal gpx:
<gpx>
  <wpt lat="43.261417" lon="16.653483"><name>GC4EJAZ</name></wpt>
</gpx>

Input:
GC10020;N33° 41.876;W117° 57.297;

Output:
<wpt lat="33.697933" lon="117.954950"><name>GC10020</name></wpt>
"""

import csv
import re

# read csv file
file = open('C:/Users/Matthias/Desktop/GC-Barny-Extractor/BarneyMysts.csv', 'r')
reader = csv.reader(file, delimiter=';')

gpxFile = '<gpx>'

for row in reader:
    print(row)
    
    gccode = row[0]
    lat = row[1]
    lon = row[2]
    
    # get minutes and degree from lat / lon
    splitLat = re.split('[NSEW°\ "]+', lat)
    latDeg = splitLat[1]
    latMin = splitLat[2]
    
    splitLat = re.split('[NSEW°\ "]+', lon)
    lonDeg = splitLat[1]
    lonMin = splitLat[2]

    # convert to decimal minutes to decimal degrees: degree + minutes/60, e.g. 43+(15.685/60)
    convertedLat = int(latDeg) + float(latMin)/60
    convertedLon = int(lonDeg) + float(lonMin)/60
    
    # build row to append to gpx, e.g. <wpt lat="43.261417" lon="16.653483"><name>GC4EJAZ</name></wpt>
    convertedRow = '<wpt lat="' + str(convertedLat) +'" lon="' + str(convertedLon) + '"><name>' + gccode + '</name></wpt>'
    gpxFile += convertedRow

file.close()

gpxFile += '</gpx>'

#  write to file
text_file = open("barny_output.gpx", "w")
text_file.write(gpxFile)
text_file.close()