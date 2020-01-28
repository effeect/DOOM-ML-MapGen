# Built with Ubuntu 19.10, compiling it on other system may lead to significant problems

# source ./venv/bin/activate

# https://stackoverflow.com/questions/42766458/tensorflow-predicting-sequences-what-is-x-and-y

# Importing libraries, template from https://www.tensorflow.org/datasets/overview
from __future__ import absolute_import, division, print_function, unicode_literals

# Special thanks to :
# https://www.tensorflow.org/io/api_docs/python/tfio/json/JSONDataset
# https://github.com/tensorflow/io/tree/v0.9.0/tensorflow_io/json

from typing import Dict, Any

import pathlib
import itertools
import json
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
# import tensorflow_io as tfio
# import tensorflow_io.json as tf_json_io
import seaborn as sns
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from pandas.io.json import json_normalize

#Part of TF Docs, can be found @ https://stackoverflow.com/questions/55535518/modulenotfounderror-no-module-named-tensorflow-docs-when-creating-tensorflow
# import tensorflow_docs as tfdocs
# import tensorflow_docs.plots
# import tensorflow_docs.modeling

# We aren't using this module but it does disable some annoying errors due to Ubuntu 19.10
import os

# Thanks to https://www.geeksforgeeks.org/pandas-parsing-json-dataset/
filename = "JSONData/DATASET.json"

with open(filename) as f :
    d = json.load(f)

# This pandas function puts our JSON data in the right place
things = json_normalize(d['things'])
linedefs = json_normalize(d['linedefs'])
sidedefs = json_normalize(d['sidedefs'])
vertices = json_normalize(d['vertices'])
sectors = json_normalize(d['sectors'])

vertices.plot(x='x',y='y', kind='scatter')

print(vertices)

#I'm choosing Vertex Model first since it only contains two features
def vertexModel(file):
    vertexDataset = vertices.copy()

    #These two lines seperate the data into two seperate components
    train = vertexDataset.sample(frac=0.8, random_state=0)
    test = vertexDataset.drop(train.index)

    train_labels = train.pop("x")
    test_labels = test.pop("x")

    trainStats = train.describe()
    trainStats = train.transpose()

    # Normalization function for data
    # def norm(x):
    #     return (x - trainStats['mean']) / trainStats['std']
    #
    # normed_train_data = norm(train)
    # normed_test_data = norm(test)

    def build_model():
        model = keras.Sequential([
            layers.Dense(64, activation='relu', input_shape=[len(train.keys())]),
            layers.Dense(64, activation='relu'),
            layers.Dense(1)
        ])

        optimizer = tf.keras.optimizers.RMSprop(0.001)

        model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=['mae', 'mse'])
        return model

    model = build_model()
    model.summary()

    example_batch = train[:10]
    example_result = model.predict(example_batch)

    EPOCHS = 1000
    history = model.fit(
        train, train_labels,
        epochs=EPOCHS, validation_split=0.2, verbose=0)

    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    hist.tail()

#Another method
def vertexModelTwo():
    df = vertices.copy()

    #Visual display of scattergram
    df.plot(x='x',y='y', kind='scatter')


    # Thanks for https://stackoverflow.com/questions/42286972/converting-from-pandas-dataframe-to-tensorflow-tensor-object

    # Splitting up the vertex coords
    xTensor = tf.constant(df['x'])
    yTensor = tf.constant(df['y'])
    print(xTensor)
    print(type(xTensor))
    #Creating Dataset
    dataset = tf.data.Dataset.from_tensor_slices((xTensor, yTensor))




    print(type(dataset))
    train_dataset = dataset.shuffle(300).batch(64)
    print(dataset)

    # https://www.tensorflow.org/datasets/add_dataset

    # Model Function
    def get_compiled_model():
        #Model for the function
        model = keras.Sequential([
            layers.Dense(64, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(1)
        ])

        optimizer = tf.keras.optimizers.Adagrad(0.001)

        model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=['mae', 'mse'])

        return model

    # https://www.tensorflow.org/guide/keras/rnn
    def model_generation():
        model = tf.keras.Sequential()
        model.add(layers.Embedding(input_dim=1000, output_dim=64))

        # The output of GRU will be a 3D tensor of shape (batch_size, timesteps, 256)
        model.add(layers.GRU(256, return_sequences=True))

        # The output of SimpleRNN will be a 2D tensor of shape (batch_size, 128)
        model.add(layers.SimpleRNN(128))

        model.add(layers.Dense(10, activation='softmax'))

        model.summary()

    def estimator():
        #Building a baseline regressor
        regressor = tf.estimator.BaselineRegressor()

        print(type(train_dataset))


        #Defining feature columns
        x = tf.feature_column.numeric_column('x')
        y = tf.feature_column.numeric_column('y')



    estimator()





    # model_generation()
    model = get_compiled_model()

    model.fit(train_dataset, epochs=100)
    NewStuff = model.predict(train_dataset).flatten()

    #Gives us the new data
    print(NewStuff)

def things():
    number = 4

def linedefs() :
    number = 3

def sidedefs() :
    number = 1

def sectors() :
    bumner = 1

vertexModelTwo()

def predictPoints(model, data):
    # https://stackoverflow.com/questions/42766458/tensorflow-predicting-sequences-what-is-x-and-y
    predicted = model.predict(data)
    predicted = np.reshape(predicted, (predicted.size,))
    return predicted
