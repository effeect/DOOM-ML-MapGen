# TensorFlow and tf.keras
import tensorflow as tf
import pandas as pd
import os
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

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



prepareData("CATWALK.csv")

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

    EPOCHS = 1000

    model = build_model()

    # Using TF.Keras to normalise data arrays
    tfiPointX = np.asarray(iPointX)
    tfPointX = np.asarray(pointX)
    tfiPointY = tf.keras.utils.normalize(iPointY)
    tfPointY = tf.keras.utils.normalize(pointY)

    history = model.fit( tfiPointX , tfPointX, epochs=EPOCHS)
    results = model.predict(tfiPointX,batch_size=32)

    print(results)





trainVertexPoints()