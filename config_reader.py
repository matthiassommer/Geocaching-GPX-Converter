import configparser 

def readConfig():
    configParser = configparser.RawConfigParser()   
    configParser.read_file(open(r'config.txt'))

    folder = configParser.get('config', 'folder')
    filename = configParser.get('config', 'filename')
    fileExt = configParser.get('config', 'fileExt')

    return folder, filename, fileExt