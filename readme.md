CSV-to-GPX-Converter for geocaching.com
======

## Description
This python script allows to convert a CSV to a GPX file which you can then upload with GSAK to Geocaching.

# Input
For a successful upload, you have to provide the GC number and the coordinates. 
The script is configured to work with this pattern:
GC-Code;LAT;LON
GC10020;N33° 41.876;W117° 57.297

If you know some Python you can easily adjust it to your needs.

#Output
It creates a minimal GPX file with this format
<gpx>
	<wpt lat="33.697933" lon="117.954950"><name>GC10020</name></wpt>
</gpx>


## Upload with GSAK

* Download and install [GSAK](http://www.gsak.net)
* In GSAK, install these two macros: SetCorrectedFlag and CorrectedCoord2GCcom
* Upload:
** First, import the converted GPX file
** Second, run SetCorrectedFlag (to be found under Makro)
** Third, run CorrectedCoord2GCcom to start the upload
** Fourth, watch and enjoy :)

If this is helpful you may want to [support me](https://www.paypal.me/SommerMatthias/5).
