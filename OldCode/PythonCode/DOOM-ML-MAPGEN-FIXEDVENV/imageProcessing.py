# This script is a rework of my original MarvinJS solution. I chose to redo it in Python to allow for a more automated process
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2
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
# https://stackoverflow.com/questions/44101894/extraction-of-coordinates-of-corners-using-harris-corner-detection-and-also-ret/52173485
# https://answers.opencv.org/question/186538/to-find-the-coordinates-of-corners-detected-by-harris-corner-detection/
def Harris_Corner_Detection(image):
    img = cv2.imread(image)

    #Displays Original Image for Debug Purposes
    cv2.imshow('Original Image', img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    dst = cv2.cornerHarris(gray, 5, 3, 0.04)
    ret, dst = cv2.threshold(dst, 0.1 * dst.max(), 255, 0)

    dst = np.uint8(dst)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)

    for i in range(1, len(corners)):
        print(corners[i])

    img[dst > 0.1 * dst.max()] = [0, 0, 255]

    return corners


Harris_Corner_Detection("CATWALK.png")