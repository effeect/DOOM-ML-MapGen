# Linedef Extractor
# Note : I'm purging some of the data from the linedef dataset to get the extraction to work better https://doom.fandom.com/wiki/Linedef_type

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

#Function from pandas to extract to json object
from pandas.io.json import json_normalize

from VertexExtractor import GetVertexDataList

# Thanks to https://www.geeksforgeeks.org/pandas-parsing-json-dataset/

#Grabs the data points, not used in application but can be used for debugging potenial files
def GetLinedefList( filename ) :
    with open(filename) as f :
        data = json.load(f)

    linedef = json_normalize(data['linedefs'])

    dfModified = linedef[["id","v1","v2"]].copy()

    print(dfModified)
    return dfModified
