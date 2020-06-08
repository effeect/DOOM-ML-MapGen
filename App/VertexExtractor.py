# VERTEX EXTRACTOR
# This python script grabs
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

#Function from pandas to extract to json object
from pandas.io.json import json_normalize


# Thanks to https://www.geeksforgeeks.org/pandas-parsing-json-dataset/
#Give filename to extracted UDMF map in order to process map data
def GetVertexDataList( filename ) :
    with open(filename) as f :
        data = json.load(f)

    #Converts JSON to PD.DataFrame
    vertices = json_normalize(data['vertices'])

    minNumberX = 9999
    minNumberY = 9999

    #Simple addition to make the vertexs scale properly with the image processing. A little messy but functional
    for i, row in vertices.iterrows() :
        if row[0] < minNumberX :
            minNumberX = row[0]
        if row[1] < minNumberY :
            minNumberY = row[1]

    # Making sure numbers aren't going negative
    print(abs(minNumberX))
    print(abs(minNumberY))

    for i, row in vertices.iterrows() :
        row[0] += abs(minNumberX)
        row[1] += abs(minNumberY)

    return vertices

# Function to call
# GetVertexDataList('CATWALK.json')
