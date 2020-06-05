# My Functions
from VertexExtractor import GetVertexDataList
from lindefExtractor import GetLinedefList

#General use
import pandas as pd
import math

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
                # newDataSet.append({"id" : idRes, "v1" : indexV1, "v1point" : DataPoint[0], "v2" : row2[3], "v2point" : DataPoint2, "isCorrect" : 1})
                newDataSet.append({"id" : idRes, "v1x" : DataPoint[0], "v1y" : DataPoint[1], "v2x" : trueDataPoint[0], "v2y" : trueDataPoint[1], "isCorrect" : 1})

            else :
                # newDataSet.append({"id" : idRes, "v1" : indexV1, "v1point" : DataPoint[0], "v2" : row2[3], "v2point" : DataPoint2, "isCorrect" : 0})
                newDataSet.append({"id" : idRes, "v1x" : DataPoint[0], "v1y" : DataPoint[1], "v2x" : trueDataPoint[0], "v2y" : trueDataPoint[1], "isCorrect" : 0})

    dfTest = pd.DataFrame(newDataSet)
    print(dfTest)
    dfTest.to_csv("CATWALKLINEDEFTest2.csv")

lineDefCreator("CATWALK.json")
