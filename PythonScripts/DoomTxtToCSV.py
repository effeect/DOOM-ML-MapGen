#Written by Oliver Dimes

#This is a simple conversion script I created to make the text into JSON since the file format is custom. This script can be used both ways!

#Thanks to https://www.vipinajayakumar.com/parsing-text-with-python/ and https://stackoverflow.com/questions/51345024/read-text-file-and-parse-in-python/51345210#51345210

def txtToJson(filename) : # This function is to convert a TEXTMAP doom file to useable JSON
    fin = open("TEXTMAPedited.txt", "rt")
    data = fin.read()
    data = data.replace(';', ',')
    data = data.replace('=', ':')
    fin.close()

    fin = open("TEXTMAPedited.txt", "wt")
    fin.write(data)
    fin.close()

def JsonToTxt(filename) : # This function is to put JSON back into TEXTMAP which allows for DOOM to run
    fin = open("TEXTMAPedited.txt", "rt")
    data = fin.read()
    data = data.replace(',', ';')
    data = data.replace(':', '=')
    fin.close()

    fin = open("TEXTMAPedited.txt", "wt")
    fin.write(data)
    fin.close()