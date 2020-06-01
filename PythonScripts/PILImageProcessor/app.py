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

#Returns a Linedef list for Tensorflow Dataset
def lineDefCreator(jsonFilename) :
    DataListUpdated = []

    #Creating Linedef Dataset for TF
    linedefList = GetLinedefList(jsonFilename)
    vertexList = GetVertexDataList(jsonFilename)

    for i, row in linedefList.iterrows():
        index1 = row[1]
        index2 = row[2]
        #Grabs Linedef line
        DataListUpdated.append({"id" : row[0] ,"v1" : row[1] ,"v1point" : (vertexList.iloc[index1][0],vertexList.iloc[index1][1]) , "v2" : row[2]  , "v2point" : (vertexList.iloc[index2][0],vertexList.iloc[index2][1])})

    #Makes the data list into a dataframe
    df = pd.DataFrame(DataListUpdated)

    #This takes a while to compile
    newDataSet = []
    for i, row in df.iterrows():

        #Properties of Linedef
        idRes = row[0]
        indexV1 = row[1]
        indexV2 = row[3]
        #VertexPoint1 of Dataset
        DataPoint = row[2]
        trueDataPoint = row[4]
        for j, row2 in df.iterrows():
            DataPoint2 = row2[4]
            if(DataPoint2 == trueDataPoint) :
                newDataSet.append({"id" : idRes, "v1" : indexV1, "v1point" : DataPoint, "v2" : row2[3], "v2point" : DataPoint2, "isCorrect" : 1})
            else :
                newDataSet.append({"id" : idRes, "v1" : indexV1, "v1point" : DataPoint, "v2" : row2[3], "v2point" : DataPoint2, "isCorrect" : 0})

    dfTest = pd.DataFrame(newDataSet)
    print(dfTest)
    dfTest.to_csv("CATWALKLINEDEF.csv")

# datasetCreator("CATWALK.png","CATWALK.json")
lineDefCreator("CATWALK.json")

