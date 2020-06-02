# This script is a rework of my original MarvinJS solution. I chose to redo it in Python to allow for a more automated process
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2 as cv
import numpy as np

#This number refers
imageScalarFactor = 5

def imageProcess(filename) :
    #Declaring data object
    data = []
    linedefData = []
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
                    data.append({"x" : x * imageScalarFactor, "y" : y * imageScalarFactor,"color" :  px [ x , y ]})
                    linedefData.append({"x" : x, "y" : y})

    #Returns Data
    return data

# Function to read through all of the data Points (Not Needed)
def printPlotData( filename ):
    data = filename

    for i in data:
        plt.plot(i[0], i[1], 'ro')

    plt.show()


#Test Code (Call it from here if you only want image processing
imageProcess('CATWALK.png')

# https://www.youtube.com/watch?v=KH8Mq9FPVPw
def Harris_Corner_Detection(image):
    img = cv.imread(image)
    cv.imshow('img', img)

    greyscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    greyscale = np.float32(greyscale)

    dst = cv.cornerHarris(greyscale, 2, 3, 0.04)
    dst = cv.dilate(dst, None)

    img[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv.imshow('dst', img)
    cv.waitKey()


Harris_Corner_Detection("CATWALK.png")