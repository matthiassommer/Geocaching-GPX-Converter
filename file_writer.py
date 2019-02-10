import os

def writeToFile(filePath, output):
    filePath = os.path.splitext(filePath)[0] + '.gpx'

    gpx_output_file = open(filePath, "w")
    gpx_output_file.write(output)
    gpx_output_file.close()