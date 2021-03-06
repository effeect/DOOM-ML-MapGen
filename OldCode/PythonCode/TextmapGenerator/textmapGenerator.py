# This file handles the JSON generated results from ML5 project and convert them to the correct TEXTMAP format for the DOOM engine to run
import json
import random

text_file = open("TEST3.txt", "wt")

start = """namespace = "ZDoomTranslated";
//Converted to UDMF with wad2udmf by Christopher M Freund
thing {
 x = 20;
 y = 3921;
angle = 90;
type = 1;
} """

text_file.write(start)

# Vertices Generation
def vertexGen( filename ):
    contents = ""
    with open(filename, 'r') as j:
        contents = json.loads(j.read())

    number = -1
    #Grabs each attribute and converts it to the correct textmap format
    for vertex in contents :
        x = vertex["x"]
        y = vertex["y"]
        number += 1
        data = (number,x,y)
        structure = "vertex //vertex %d \n{ \n x = %s; \n y = %s; \n}"
        string = (structure % data)
        print(string)
        text_file.write(string)

# The Linedef can be updated with diffirent IDs and collision https://doom.fandom.com/wiki/Linedef
# The ID number can be updated in order to generate better maps
def linedefGen(stringOriginal):
    string = ""
    contents = ""
    numbers = []
    with open('linedef.json', 'r') as j:
        contents = json.loads(j.read())

    firstVertex = -1
    secondVertex = 0

    for linedef in contents :
        firstVertex += 1
        secondVertex += 1

        vertex1 = linedef["v1"]
        vertex2 = linedef["v2"]

        numbers.append(firstVertex)

        # Formatting data
        data = ( firstVertex , random.choice(numbers) , random.choice(numbers) )
        data = ( firstVertex , vertex1 , vertex2 )

        structure = "linedef //linedef %d \n{ \n id = 0; \n twosided = true;\n v1 = %d; \n v2 = %d; \n}"
        string = (structure % data)
        print(string)
        text_file.write(string)

def sectorGen(jsonFile):
    e = "e"

def sidedefGen(jsonFile):
    e = "e"

def thingsGen(jsonFile):
    e = "e"

vertexGen('jsonStuff.json')
linedefGen("ifijo")

