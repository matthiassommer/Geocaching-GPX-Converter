import configparser 

inputFile = None
delimiter = None

def readConfig():
    configParser = configparser.RawConfigParser()   
    configParser.read_file(open(r'config.txt'))

    global inputFile
    inputFile = configParser.get('config', 'input')

    global delimiter
    delimiter = configParser.get('config', 'delimiter')