# This file handles the JSON generated results from ML5 project and convert them to the correct TEXTMAP format for the DOOM engine to run
import json
import random

# Vertices Generation
def vertexGen( filename ):
    contents = ""
    with open('jsonStuff.json', 'r') as j:
        contents = json.loads(j.read())
        print(contents)

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

# The Linedef can be updated with diffirent IDs and collision https://doom.fandom.com/wiki/Linedef
# The ID number can be updated in order to generate better maps
def linedefGen(stringOriginal):
    string = ""
    contents = ""
    numbers = []
    with open('jsonStuff.json', 'r') as j:
        contents = json.loads(j.read())
        print(contents)

    firstVertex = -1
    secondVertex = 0

    for linedef in contents :
        firstVertex += 1
        secondVertex += 1

        numbers.append(firstVertex)

        # Formatting data
        data = ( firstVertex , random.choice(numbers) , random.choice(numbers) )
        structure = "linedef //linedef %d \n{ \n id = 0; \n twosided = true;\n v1 = %d; \n v2 = %d; \n}"
        string = (structure % data)
        print(string)

    print(numbers)

def sectorGen(jsonFile):
    e = "e"

def sidedefGen(jsonFile):
    e = "e"

def thingsGen(jsonFile):
    e = "e"

vertexGen('jsonStuff.json')
linedefGen("ifijo")