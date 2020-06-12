# My Functions
from VertexExtractor import GetVertexDataList
from lindefExtractor import GetLinedefList

#General use
import pandas as pd
import math




#Returns a Linedef list for ML5js Dataset
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
                newDataSet.append({"id":idRes,"v1x":DataPoint[0],"v1y":DataPoint[1],"v2x":DataPoint2[0],"v2y":DataPoint2[1],"isCorrect":1})

    dfTest = pd.DataFrame(newDataSet)
    print("DatasetDone")
    print(dfTest)
    return dfTest

def main() :
    obj1 = lineDefCreator('Dataset/CANYON.json')
    obj2 = lineDefCreator('Dataset/CATWALK.json')
    obj3 = lineDefCreator('Dataset/COMBINE.json')
    obj4 = lineDefCreator('Dataset/FISTULA.json')
    obj5 = lineDefCreator('Dataset/GARRISON.json')
    obj6 = lineDefCreator('Dataset/GERYON.json')
    obj7 = lineDefCreator('Dataset/MEPHISTO.json')
    obj8 = lineDefCreator('Dataset/MINOS.json')
    obj9 = lineDefCreator('Dataset/NESSUS.json')
    obj10 = lineDefCreator('Dataset/PARADOX.json')
    obj11 = lineDefCreator('Dataset/SUBSPACE.json')
    obj12  = lineDefCreator('Dataset/SUBTERRA.json')
    obj13  = lineDefCreator('Dataset/TEETH.json')
    obj14  = lineDefCreator('Dataset/VESPERAS.json')
    obj15  = lineDefCreator('Dataset/VIRGIL.json')


    frames = [obj1,obj2,obj3,obj4,obj4,obj5,obj6,obj7,obj8,obj9,obj10,obj11,obj12,obj13,obj14,obj15]
    result = pd.concat(frames)
    print(result)
    result.to_csv("DATASET.csv")

main()


