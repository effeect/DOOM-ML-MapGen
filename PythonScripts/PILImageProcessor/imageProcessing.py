# This script is a rework of my original MarvinJS solution. I chose to redo it in Python to allow for a more automated process
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Note, rough estimation suggests 5x map marker modifier is needed can be changed
def imageProcess(filename) :
    #Declaring data object
    data = []
    #Loading image for modification
    with Image.open(filename) as im:
        px = im.load()
        #Grabbing values
        width,height = im.size
        print(width , height)

        #For loop
        for x in range(width) :
            for y in range(height) :
                #Removes white space from the image
                if px[x,y] != (255,255,255,0) :
                    data.append({"x" : x*5, "y" : y*5,"color" :  px [ x , y ]})

        print(type(data))

        return data



# Function to read through all of the data Points (Not Needed)
def printPlotData( filename ):
    data = filename

    for i in data:
        plt.plot(i[0], i[1], 'ro')

    plt.show()



#Test Code (Call it from here if you only want image processing
imageProcess('CATWALK.png')
