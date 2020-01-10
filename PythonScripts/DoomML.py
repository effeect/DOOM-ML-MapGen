# Built with Ubuntu 19.10, please note that Tensorflow_io.json has issues running on Windows machines

# source ./venv/bin/activate

# Note : There needs to a dataset for each element of DOOM

# Importing libraries, template from https://www.tensorflow.org/datasets/overview
from __future__ import absolute_import, division, print_function, unicode_literals

# Special thanks to :
# https://www.tensorflow.org/io/api_docs/python/tfio/json/JSONDataset
# https://github.com/tensorflow/io/tree/v0.9.0/tensorflow_io/json

from typing import Dict, Any

import pathlib

import json
import numpy
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_io as tfio
import tensorflow_io.json as tf_json_io
import seaborn as sns
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from pandas.io.json import json_normalize

#Part of TF Docs, can be found @ https://stackoverflow.com/questions/55535518/modulenotfounderror-no-module-named-tensorflow-docs-when-creating-tensorflow
import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

# We aren't using this module but it does disable some annoying errors due to Ubuntu 19.10
import os

# Thanks to https://www.geeksforgeeks.org/pandas-parsing-json-dataset/
filename = "JSONData/DATASET.json"

with open(filename) as f :
    d = json.load(f)

#We are normalizing the data
things = json_normalize(d['things'])
linedefs = json_normalize(d['linedefs'])
sidedefs = json_normalize(d['sidedefs'])
vertices = json_normalize(d['vertices'])
sectors = json_normalize(d['sectors'])

print(vertices)

def vertexModel(file):
    vertexDataset = vertices.copy() #NEEDS TO BE CHANGED TO FILE

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
        epochs=EPOCHS, validation_split=0.2, verbose=0,
        callbacks=[tfdocs.modeling.EpochDots()])

    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    hist.tail()


vertexModel(filename)
