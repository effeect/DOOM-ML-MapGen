# My Functions
from VertexExtractor import GetVertexDataList
from lindefExtractor import GetLinedefList

#General use
import pandas as pd
import math





#Returns a Linedef list for ML5js Dataset
def lineDefCreator(jsonFilename) :
    #Creating Linedef Dataset for TF
    linedefList = GetLinedefList(jsonFilename)
    vertexList = GetVertexDataList(jsonFilename)

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


