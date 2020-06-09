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
                newDataSet.append({"id" : idRes, "v1x" : DataPoint[0], "v1y" : DataPoint[1], "v2x" : DataPoint2[0], "v2y" : DataPoint2[1], "isCorrect" : 1})

    dfTest = pd.DataFrame(newDataSet)
    print("DatasetDone")

    print(dfTest)

    return dfTest

def main() :
    obj1 = lineDefCreator('Dataset/BLACKTWR2.json')
    obj2 = lineDefCreator('Dataset/CANYON2.json')
    obj3 = lineDefCreator('Dataset/CATWALK2.json')
    obj4 = lineDefCreator('Dataset/MAP01.json')
    obj5 = lineDefCreator('Dataset/MAP03.json')

    frames = [obj1,obj2,obj3,obj4,obj4]
    result = pd.concat(frames)
    print(result)
    result.to_csv("COMBINEDDATAFINAL2.csv")

main()


