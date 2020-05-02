# My Functions
from imageProcessing import imageProcess
from VertexExtractor import GetVertexDataList

#General use functions
import pandas as pd
import math

# Matches up data from sources
def datasetCreator(pngFilename, jsonFilename) :
    #Calling data
    imageData = imageProcess(pngFilename)
    vertexData = GetVertexDataList(jsonFilename)

    dfImage = pd.DataFrame(data = imageData)
    dfVertices = pd.DataFrame(data = vertexData)

    print(dfVertices)
    print(dfImage)

    #Where the data is held
    MapDataset = []

    #Dataset creation nearest point (TAKES TIME)
    for i, row in dfVertices.iterrows():
        distance = 100
        point = [row[0],row[1]]
        distanceMaker = []
        tempPoint = [0,0]

        for j, imageRow in dfImage.iterrows():
            imagePoint = [imageRow[0],imageRow[1]]

            #Massively CPU Intensive
            tempDist = abs(math.sqrt( ((point[0]-imagePoint[0])**2)+((point[1]-imagePoint[1])**2)))

            if tempDist < distance :
                distance = tempDist
                tempPoint = imagePoint


        result = {"point" : point ,"imagePoint ": tempPoint, "distance": round(distance)}
        print(result)
        MapDataset.append(result)

    print(MapDataset)
    df = pd.DataFrame(data = MapDataset)
    df.to_csv('CATWALK.csv')


datasetCreator("CATWALK.png","CATWALK.json")

