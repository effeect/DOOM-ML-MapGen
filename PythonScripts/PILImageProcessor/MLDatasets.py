# TensorFlow and tf.keras
import tensorflow as tf
import pandas as pd
import os
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

from app import lineDefCreator

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

#Printing out essential details to help debugging
print("TensorFlow version : {}".format(tf.__version__))
print("Eager execution : {}".format(tf.executing_eagerly()))

#Using two linear regression algorithms to get the correct result
# https://www.geeksforgeeks.org/linear-regression-using-tensorflow/

#Global Data Lists for Application
pointX = []
pointY = []
iPointX = []
iPointY = []

#Results (TEMP)
resultsY = []
resultsX = []

#This function processes the data from
def prepareData( filename ) :
    #Reading file
    dfTemp = pd.read_csv(filename)
    df = dfTemp.copy()
    df.head()

    #Popping each individual mark
    imagePoints = df.pop('imagePoint')
    points = df.pop('point')

    #Making Copies
    npImagePoints = imagePoints
    npPoints = points

    #NewDataPoints

    #String issue with data, this isn't the best way to solve the problem but it's a minimal cost in the grand scheme of things
    for i in npPoints:
        tempPointX = float(i.split(',',1)[0].replace('[',''))
        tempPointY = float(i.split(',',1)[1].replace(']',''))
        pointX.append(tempPointX)
        pointY.append(tempPointX)

    for i in npImagePoints:
        tempImagePointX = float(i.split(',',1)[0].replace('[',''))
        tempImagePointY = float(i.split(',',1)[1].replace(']',''))
        iPointX.append(tempImagePointX)
        iPointY.append(tempImagePointY)

#TRAINING VERTEX POINTS
def trainVertexPoints() :
    def build_model():
        model = keras.Sequential([
            layers.Dense(64, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(1)
        ])

        optimizer = tf.keras.optimizers.RMSprop(0.001)

        model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=['mae', 'mse'])
        return model

    EPOCHS = 20

    modelX = build_model()
    modelY = build_model()

    # Using TF.Keras to normalise data arrays
    tfiPointX = np.asarray(iPointX)
    tfPointX = np.asarray(pointX)
    tfiPointY = tf.keras.utils.normalize(iPointY)
    tfPointY = tf.keras.utils.normalize(pointY)

    historyX = modelX.fit( tfiPointX , tfPointX, epochs=EPOCHS)
    historyY = modelY.fit( tfiPointY , tfPointY, epochs=EPOCHS)

    resultsX = modelX.predict(tfiPointX,batch_size=32)
    resultsY = modelY.predict(tfiPointY,batch_size=32)
    print(resultsX)
    print(resultsY)

    return [resultsX , resultsY ]

# Creates new Linedef with original Linedef Data
def trainLineDef( filename, dataObject):


    dataVertex = dataObject

    xCoords = dataObject[0]
    yCoords = dataObject[1]



    print(type(xCoords))
    print(yCoords)

    #DataPoints
    v1x = []
    v1y = []
    v2x = []
    v2y = []

    dfLinedef = lineDefCreator( filename )

    #Note : Add ID functionality once the linedef creation is stable
    for i, row in dfLinedef.iterrows() :
        v1x.append(row[2][0])
        v1y.append(row[2][1])
        v2x.append(row[4][0])
        v2y.append(row[4][1])

    def build_model():
        model = keras.Sequential([
            layers.Dense(64, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(1)
        ])

        optimizer = tf.keras.optimizers.RMSprop(0.001)

        model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=['mae', 'mse'])
        return model

    #Linedef Generation
    modelPoint1 = build_model()
    modelPoint2 = build_model()
    modelPoint3 = build_model()
    modelPoint4 = build_model()

    v1xResults = modelPoint1.fit( xCoords, v1x)
    v1yResults = modelPoint2.fit( yCoords, v1y)
    v2xResults = modelPoint3.fit( xCoords, v2x)
    v2yResults = modelPoint4.fit( yCoords, v2y)




prepareData("CATWALK.csv")
data = trainVertexPoints()
print("Data")
print(data[0][0])
trainLineDef( "CATWALK.json" , data )