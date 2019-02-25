CSV-to-GPX-Converter for geocaching.com
======

This python script converts coordinates from a CSV to a GPX file. Using the two provided GSAK scripts, you can then easily upload your coordinates to geocaching.com. The provided scripts automatically update the coordinates for each geocache.

## Input
You have to provide the GC number and the coordinates for each geocache within the CSV file. Thats the minimal requirement for a successful upload via the geocaching.com API.

The python script is configured to work with this pattern:

```
GC-Code;LAT;LON
GC10020;N33° 41.876;W117° 57.297
```

If you know some Python you can easily adjust it to your needs. You can also contact me if you need help.

## Output
The python script creates a GPX file with this format

```
<gpx>
	<wpt lat="33.697933" lon="117.954950"><name>GC10020</name></wpt>
</gpx>
```

## Configuration
The config.txt file contains the configuration parameters for the script. The `input` parameter specifies the relative path the input file having the raw input. The gpx output file will be saved in the same location with the same filename.

The parameter `delimiter` lets you define the data delimiter. In the above example, if was a semicolon.

## Setup GSAK

Download and install [GSAK](http://www.gsak.net)

### Install macros
Install these two macros in GSAK: [SetCorrectedFlag](http://gsak.net/board/index.php?showtopic=31875&st=0&#entry239020) and [CorrectedCoord2GCcom](http://gsak.net/board/index.php?s=84bf3b6d3d9508f637d2d5000a5d6163&showtopic=32407). Both can be found under gsak-scripts.

In GSAK, go to `Macro -> Execute -> Install` or press `CTRL+M -> Install`. Select a .gsk file and click install. Repeat for the second macro.


### Upload with GSAK
* First, import the converted GPX file in GSAK (CTRL+O)
* Run the macro `SetCorrectedFlag` (CTRL+M and doubleclick on it). This will set a flag on all your imported geocaches so the next macro can pick them up for upload.
* Then, run the macro `CorrectedCoord2GCcom` and wait until all coordinates are uploaded.


## Docker build
You can also use the provided Dockerfile to build and run the python script.

```
docker build --rm -t gpx-converter .
docker run gpx-converter

# copy gpx to host (replace container id with the real one.)
docker ps -a
docker cp <containerid>:/data/example_input.gpx ./output.gpx
```


# Support
If this saved you some time, you may want to [support me](https://www.paypal.me/SommerMatthias/5).
