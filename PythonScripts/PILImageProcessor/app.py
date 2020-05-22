# My Functions
from imageProcessing import imageProcess
from VertexExtractor import GetVertexDataList
from lindefExtractor import GetLinedefList

#General use
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

def lineDefCreator(jsonFilename) :
    DataListUpdated = []

    #Creating Linedef Dataset for TF
    linedefList = GetLinedefList(jsonFilename)
    vertexList = GetVertexDataList(jsonFilename)

    print(vertexList)

    for i, row in linedefList.iterrows():
        index1 = row[1]
        index2 = row[2]
        DataListUpdated.append({"v1" : (vertexList.iloc[index1][0],vertexList.iloc[index1][1]) , "v2" : (vertexList.iloc[index2][0],vertexList.iloc[index2][1])})

    print(DataListUpdated)
    return DataListUpdated





# datasetCreator("CATWALK.png","CATWALK.json")
lineDefCreator("CATWALK.json")

