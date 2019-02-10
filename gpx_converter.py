import csv
import re
import config_reader

# RegEx for a valid GC code
gccodeRegExp = re.compile(r'^(GC|gc|Gc|gC)[a-zA-Z0-9]{2,6}$')

def convert2Gpx(filePath):
  input_file = open(filePath, mode='r', encoding='utf-8-sig')
  reader = csv.reader(input_file, delimiter=config_reader.delimiter)

  output = '<?xml version="1.0" encoding="utf-8"?>\n<gpx xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0" creator="Groundspeak Pocket Query" xsi:schemaLocation="http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd http://www.groundspeak.com/cache/1/0/1 http://www.groundspeak.com/cache/1/0/1/cache.xsd" xmlns="http://www.topografix.com/GPX/1/0">\n'

  rows_converted = 0
  rows_total = 0

  for row in reader:  
      rows_total += 1

      gccode = row[0]
      validCode = gccodeRegExp.match(gccode)
      if (not validCode): 
        print ("Invalid entry: ", gccode)
        continue

      lat = row[-2]
      lon = row[-1]
      
      # get minutes and degree from lat, e.g. N33° 41.876
      splitLat = re.split('[NS°\ "]+', lat)
      latDeg = splitLat[1]
      latMin = splitLat[2]
      
      # get minutes and degree from lon, e.g. W117° 57.297
      splitLon = re.split('[EW°\ "]+', lon)
      # degree is 117
      lonDeg = splitLon[1]
      # minutes is 57.297
      lonMin = splitLon[2]

      # convert decimal minutes to decimal degrees: degree + minutes/60, e.g. 33+(41.876/60)
      convertedLat = int(latDeg) + float(latMin)/60
      if ('S' in lat):
          convertedLat = convertedLat * (-1)
      
      convertedLon = int(lonDeg) + float(lonMin)/60
      if ('W' in lon):
          convertedLon = convertedLon * (-1)
      
      # build row and append to gpx, e.g. <wpt lat="33.697933" lon="-117.954950"><name>GC10020</name></wpt>
      convertedRow = '<wpt lat="' + "{0:.6f}".format(convertedLat) +'" lon="' + "{0:.6f}".format(convertedLon) + '"><name>' + gccode + '</name></wpt>\n'
      output += convertedRow

      rows_converted += 1

  input_file.close()

  output += '</gpx>'

  print('Imported rows ', rows_total)
  print('Converted rows ', rows_converted)

  return output