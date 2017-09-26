CSV-to-GPX-Converter for geocaching.com
======

This python script allows to convert a CSV to a GPX file which you can then upload with GSAK to Geocaching.com. 

## Input
You have to provide the GC number and the coordinates for each geocache within the CSV file. Thats the minimal requirement for a successful upload later-on.

The python script is configured to work with this pattern:

```
GC-Code;LAT;LON
GC10020;N33° 41.876;W117° 57.297
```

If you know some Python you can easily adjust it to your needs. You can also contact me if you need help.

## Output
The script creates a GPX file with this format

```
<gpx>
	<wpt lat="33.697933" lon="117.954950"><name>GC10020</name></wpt>
</gpx>
```


## Setup GSAK

* Download and install [GSAK](http://www.gsak.net)
* Install these two macros in GSAK: [SetCorrectedFlag](http://gsak.net/board/index.php?showtopic=31875&st=0&#entry239020) and [CorrectedCoord2GCcom](http://gsak.net/board/index.php?s=84bf3b6d3d9508f637d2d5000a5d6163&showtopic=32407)

## Upload with GSAK
* First, import the converted GPX file in GSAK
* Second, run SetCorrectedFlag (to be found under Macro)
* Third, run CorrectedCoord2GCcom to start the upload
* Fourth, watch and enjoy :)

If this is helpful you may want to [support me](https://www.paypal.me/SommerMatthias/5).
