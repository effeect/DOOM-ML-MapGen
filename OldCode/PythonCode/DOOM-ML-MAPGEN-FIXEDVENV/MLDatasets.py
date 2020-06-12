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
from imageProcessing import Harris_Corner_Detection

#Printing out essential details to help debugging
print("1111111111111")
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

    # String issue with data, this isn't the best way to solve the problem but it's a minimal cost in the grand scheme of things
    for i in npPoints:
        tempPointX = float(i.split(',',1)[0].replace('[',''))
        tempPointY = float(i.split(',',1)[1].replace(']',''))
        pointX.append(tempPointX)
        pointY.append(tempPointY)

    for i in npImagePoints:
        tempImagePointX = float(i.split(',',1)[0].replace('[',''))
        tempImagePointY = float(i.split(',',1)[1].replace(']',''))
        iPointX.append(tempImagePointX)
        iPointY.append(tempImagePointY)

    print(pointX)
    print(pointY)

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

    return [np.round(resultsX) , np.round(resultsY)]

#Uses the values from the image and gives an accurate data representation
def trainVertex():

    #The model function here creates a keras based model with two inputs and two outputs.
    def build_model() :
        # Thanks to https://www.pyimagesearch.com/2019/02/04/keras-multiple-inputs-and-mixed-data/
        inputA = keras.Input(shape=(1,))
        inputB = keras.Input(shape=(1,))

        # IMAGE COORDINATE ----------------
        x1 = keras.layers.Dense(64, activation="relu")(inputA)
        x1 = keras.layers.Dense(32, activation="relu")(x1)
        x1 = keras.layers.Dense(4, activation="relu")(x1)
        x1 = keras.Model(inputs=inputA, outputs=x1)

        y1 = keras.layers.Dense(64, activation="relu")(inputB)
        y1 = keras.layers.Dense(32, activation="relu")(y1)
        y1 = keras.layers.Dense(4, activation="relu")(y1)
        y1 = keras.Model(inputs=inputB, outputs=y1)


        #Combining the two outputs into one.
        combined = keras.layers.concatenate([x1.output, y1.output])

        z = keras.layers.Dense(2, activation="relu")(combined)
        z = keras.layers.Dense(1, activation="linear")(z)

        linedefModel = keras.Model(inputs=[x1.input,y1.input], outputs = z)


        #Optimizer Settings
        opt = keras.optimizers.Adam(lr=1e-3, decay=1e-3 / 200)
        linedefModel.compile(loss="mean_absolute_percentage_error", optimizer=opt)



    print("---------BELOW------------")

# Creates new Linedef with original Linedef Data
def trainLineDef( filename, dataObject):

    dataVertex = dataObject
    for i in dataVertex :
        i[0] = np.round(i[0] * 5)
        i[1] = np.round(i[1] * 5)
        print(type(i[0]))

    df = pd.read_csv("CATWALKLINEDEF.csv")
    linedefdf = df.copy()

    print(linedefdf)
    #Data
    v1x = []
    v1y = []
    v2x = []
    v2y = []
    isCorrect = []

    # DATA MODIFICATION -------------------------------
    tempVertex1 = []
    tempVertex2 = []
    tempIsCorrect = []
    tempVertex1 = linedefdf.pop("v1point")
    tempVertex2 = linedefdf.pop("v2point")
    tempIsCorrect = linedefdf.pop("isCorrect")

    # For loops to fix the string to CSV issue, it may take a couple of minutes to process depending on the machine
    for i in tempVertex1 :
        tempPointX = float(i.split(',',1)[0].replace('(',''))
        tempPointY = float(i.split(',',1)[1].replace(')',''))
        v1x.append(tempPointX)
        v1y.append(tempPointY)
    for i in tempVertex2 :
        tempPointX = float(i.split(',',1)[0].replace('(',''))
        tempPointY = float(i.split(',',1)[1].replace(')',''))
        v2x.append(tempPointX)
        v2y.append(tempPointY)

    # Conversion to NumPy arrays for Keras

    isCorrect = np.asarray(tempIsCorrect)

    v1x = np.asarray(v1x)
    v1y = np.asarray(v1y)
    v2x = np.asarray(v2x)
    v2y = np.asarray(v2y)

    # MACHINE LEARNING MODEL ------------------------------

    results = []
    def build_model():
        # Thanks to https://www.pyimagesearch.com/2019/02/04/keras-multiple-inputs-and-mixed-data/
        # Each input represents a diffirent part of the
        inputA = keras.Input(shape=(1,))
        inputB = keras.Input(shape=(1,))
        inputC = keras.Input(shape=(1,))
        inputD = keras.Input(shape=(1,))

        # FIRST COORDINATE ------------------------------
        x1 = keras.layers.Dense(64, activation="relu")(inputA)
        x1 = keras.layers.Dense(32, activation="relu")(x1)
        x1 = keras.layers.Dense(4, activation="relu")(x1)
        x1 = keras.Model(inputs=inputA, outputs=x1)

        y1 = keras.layers.Dense(64, activation="relu")(inputB)
        y1 = keras.layers.Dense(32, activation="relu")(y1)
        y1 = keras.layers.Dense(4, activation="relu")(y1)
        y1 = keras.Model(inputs=inputB, outputs=y1)

        # SECOND COORDINATE ----------------------------
        x2 = keras.layers.Dense(64, activation="relu")(inputC)
        x2 = keras.layers.Dense(32, activation="relu")(x2)
        x2 = keras.layers.Dense(4, activation="relu")(x2)
        x2 = keras.Model(inputs=inputC, outputs=x2)

        y2 = keras.layers.Dense(64, activation="relu")(inputD)
        y2 = keras.layers.Dense(32, activation="relu")(y2)
        y2 = keras.layers.Dense(4, activation="relu")(y2)
        y2 = keras.Model(inputs=inputD, outputs=y2)


        #Combining the two outputs into one.
        combined = keras.layers.concatenate([x1.output, y1.output,x2.output,y2.output])

        z = keras.layers.Dense(4, activation="relu")(combined)
        z = keras.layers.Dense(1, activation="linear")(z)

        linedefModel = keras.Model(inputs=[x1.input,y1.input,x2.input,y2.input], outputs = z)


        #Optimizer Settings (To be modified)
        opt = keras.optimizers.Adam(lr=1e-3, decay=1e-3 / 200)
        linedefModel.compile(loss="mean_absolute_percentage_error", optimizer=opt)

        #Note might be a good idea to have this as a seperate function
        linedefModel.fit([v1x,v1y,v2x,v2y] , isCorrect , batch_size=10,epochs=10)
        print(type(v1x))
        # DOESNT
        dataVertexCopy1 = dataVertex.copy()
        dataVertexCopy2 = dataVertex.copy()

        # https://github.com/tensorflow/tensorflow/issues/21894
        np.random.shuffle(dataVertexCopy2)

        for x in dataVertexCopy1 :
            for y in dataVertexCopy2 :

                tempx1 = np.asarray(dataVertexCopy1[0])[:10]
                tempy1 = np.asarray(dataVertexCopy1[1])[:10]
                tempx2 = np.asarray(dataVertexCopy2[0])[:10]
                tempy2 = np.asarray(dataVertexCopy2[1])[:10]

                tempPreds = linedefModel.predict( [ tempx1 , tempy1, tempx2 , tempy2] )

                # tempPreds = linedefModel.predict( [dataVertexCopy1[0]:10 , dataVertexCopy1[1] , dataVertexCopy2[0] , dataVertexCopy2[1] ] )

                print(tempPreds)

                # if tempPreds > 0.5 :
                #     results.append({"X1" : dataVertexCopy1[0], "Y1" : dataVertexCopy1[1], "X2" : dataVertexCopy2[0], "Y2" : dataVertexCopy2[1] ,"Bool " : tempPreds})
                #     print(results)

        for k in results :
            print(k)

    build_model()


    #Linedef Generation
    # modelPoint1 = build_model()
    # modelPoint2 = build_model()
    # modelPoint3 = build_model()
    # modelPoint4 = build_model()
    #
    # v1xResults = modelPoint1.fit( xCoords, v1x)
    # v1yResults = modelPoint2.fit( yCoords, v1y)
    # v2xResults = modelPoint3.fit( xCoords, v2x)
    # v2yResults = modelPoint4.fit( yCoords, v2y)


# prepareData("CATWALK.csv")
#
# data = trainVertexPoints()

data = Harris_Corner_Detection("FISTULA.png")

trainLineDef( "CATWALK.json" , data)