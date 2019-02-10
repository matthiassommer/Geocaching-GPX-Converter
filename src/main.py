"""
@author: Matthias Sommer, www.matthiassommer.it

Minimal gpx file format:
<gpx>
  <wpt lat="43.261417" lon="16.653483"><name>GC4EJAZ</name></wpt>
</gpx>

Example input:
GC10020;N33° 41.876;W117° 57.297;

Converted output:
<wpt lat="33.697933" lon="-117.954950"><name>GC10020</name></wpt>
"""

import gpx_converter
import config_reader
import file_writer

class GpxConverter(object):
  def run(self):
    config_reader.readConfig()
    converted = gpx_converter.convert2Gpx(config_reader.inputFile)
    file_writer.writeToFile(config_reader.inputFile, converted)

if __name__ == '__main__':
  GpxConverter().run()