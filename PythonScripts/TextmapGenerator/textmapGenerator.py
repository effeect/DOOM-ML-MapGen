# This file handles the JSON generated results from ML5 project

import json

# Vertices Generation
def vertexGen( filename ):
    contents = ""
    with open('jsonStuff.json', 'r') as j:
        contents = json.loads(j.read())
        print(contents)

    number = -1
    #Grabs each attribute
    for vertex in contents :
        x = vertex["x"]
        y = vertex["y"]
        number += 1
        data = (number,x,y)
        structure = "vertex //vertex %d \n{ \n x = %s; \n y = %s; \n}"
        string = (structure % data)
        print(string)




vertexGen('jsonStuff.json')

def linedefGen(jsonFile):
    e = "e"

def sectorGen(jsonFile):
    e = "e"

def sidedefGen(jsonFile):
    e = "e"

def thingsGen(jsonFile):
    e = "e"


print("hello world")