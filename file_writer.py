def writeToFile(folder, filename, output):
  gpx_output_file = open(folder + filename + ".gpx", "w")
  gpx_output_file.write(output)
  gpx_output_file.close()