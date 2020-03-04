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
import tensorflow_io as tfio
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

#Vertex Functions NEEDS A REWORKED MODEL
def vertex():
    #Making a copy of the Vertex Dataset

    df = vertices.copy()
    # Thanks for https://stackoverflow.com/questions/42286972/converting-from-pandas-dataframe-to-tensorflow-tensor-object

    # Splitting up the vertex coords
    xTensor = tf.constant(df['x'])
    yTensor = tf.constant(df['y'])
    #Creating Dataset

    dataset = tf.data.Dataset.from_tensor_slices((xTensor, yTensor))

    train_dataset = dataset.shuffle(300).batch(64)

    # Model Function
    def get_compiled_model():
        #Model for the function
        model = keras.Sequential([
            layers.Dense(256, activation='relu'),
            layers.Dense(256, activation='relu'),
            layers.Dense(2)
        ])

        optimizer = tf.keras.optimizers.Adam(0.01)

        model.compile(loss='mean_squared_error',
                      optimizer=optimizer,
                      metrics=['accuracy'])

        return model

    model = get_compiled_model()

    model.fit(train_dataset, epochs=1000)
    numpyArray = model.predict(train_dataset)

    result = pd.DataFrame(numpyArray)
    print(result)
    result.plot(x=0,y=1, kind='scatter')
    plt.show()

def linedefs() :
    number = 3

def sidedefs() :
    number = 1

def sectors() :
    bumner = 1

vertex()

def predictPoints(model, data):
    # https://stackoverflow.com/questions/42766458/tensorflow-predicting-sequences-what-is-x-and-y
    predicted = model.predict(data)
    predicted = np.reshape(predicted, (predicted.size,))
    return predicted
