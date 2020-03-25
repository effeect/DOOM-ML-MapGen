# Built with PopOS
# source ./venv/bin/activate

# Note : There needs to a dataset for each element of DOOM

# Importing libraries, template from https://www.tensorflow.org/datasets/overview
from __future__ import absolute_import, division, print_function, unicode_literals

# Special thanks to :
# https://www.tensorflow.org/io/api_docs/python/tfio/json/JSONDataset
# https://github.com/tensorflow/io/tree/v0.9.0/tensorflow_io/json

from typing import Dict, Any

import pathlib

from conversion import txtToJson
import numpy
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_io as tfio
import tensorflow_io.json as tf_json_io
import seaborn as sns
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers

#Part of TF Docs, can be found @ https://stackoverflow.com/questions/55535518/modulenotfounderror-no-module-named-tensorflow-docs-when-creating-tensorflow
import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

txtToJson('JSONData/TEXTMAP.txt')

# Just disables the warning, doesn't enable AVX/FMA
import os

# Make sure to import these libs with python3 -m pip

filename = "JSONData/testData.json"

cols = tf_json_io.list_json_columns(filename)

# List of functions for each element of the map
# https://stackoverflow.com/questions/38381887/how-to-read-json-files-in-tensorflow

# https://www.tensorflow.org/tutorials/keras/regression

feature_cols = ["floatfeature"]

feature_dataset = tf_json_io.JSONDataset(filename, feature_cols)
datasetpd = pd.read_json(filename,"records")

dataset = datasetpd.copy()
print(dataset)



linedefsDataset = datasetpd.copy()
linedefsDatasetTrain = linedefsDataset.sample(frac=0.8,random_state=0)
linedefsDatasetTest = linedefsDataset.drop(linedefsDatasetTrain.index)

linedefTrainLabels = linedefsDatasetTrain.pop('floatfeature')
linedefsStats = linedefsDatasetTrain.describe()
linedefsStats = linedefsStats.transpose()


def norm(x): #Normailisation function
    return(x - linedefsStats['mean']) / linedefsStats['std']

#The values need to be normalised before going into the dataset

normLinedefTrainedData = norm(linedefsDatasetTrain)
normLinedefTestData = norm(linedefsDatasetTest)

def build_model():
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=[len(linedefsDatasetTrain.keys())]),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001) #We can change this in future

    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mae', 'mse']) #MSE stands for MEAN SQUARED ERROR
    return model

model = build_model()
model.summary()

example_batch = normLinedefTrainedData[:2]
example_result = model.predict(example_batch)
print(example_result)

EPOCHS = 1000

history = model.fit(
    normLinedefTrainedData,
    linedefTrainLabels,
    epochs=EPOCHS,
    validation_split=0.2,
    verbose=0,
    callbacks=[tfdocs.modeling.EpochDots()])


hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()

plotter = tfdocs.plots.HistoryPlotter(smoothing_std=2)

plotter.plot({'Basic': history}, metric = "mae")
plt.ylim([0, 10])
plt.ylabel('1')

plotter.plot({'Basic': history}, metric = "mse")
plt.ylim([0, 20])
plt.ylabel('2')





def get_linedefs():
    '''   BLOCKING
    BLOCKMONSTERS
    TWOSIDED
    DONTPEGTOP
    DONTPEGBOTTOM
    SECRET
    SOUNDBLOCK
    DONTDRAW
    MAPPED
    RAILING
    PASSUSE
    REPEAT_SPECIAL
    BLOCK_FLOATERS
    THREEDMIDTEX
    SPAC_Use
    SPAC_MCross
    SPAC_Impact
    SPAC_Push
    SPAC_PCross
    SPAC_UseThrough
    TRANSLUCENT
    MONSTERSCANACTIVATE
    BLOCK_PLAYERS
    BLOCKEVERYTHING
    SPAC_Cross
    SPAC_AnyCross
    SPAC_MUse
    SPAC_MPush
    FIRSTSIDEONLY
    ZONEBOUNDARY
    CLIP_MIDTEX
    WRAP_MIDTEX
    CHECKSWITCHRANGE
    BLOCKPROJECTILE
    BLOCKUSE
    BLOCKSIGHT
    BLOCKHITSCAN
    ThreeDMIDTEX_IMPASS'''

sidedefsDataset = "placeholder"

def get_sidedefs():
    ''' alpha
    clipmidtex
    comment
    light
    lightabsolute
    lightfog
    nodecals
    nofakecontrast
    offsetx_bottom
    offsetx_mid
    offsetx_top
    offsetx
    offsety_bottom
    offsety_mid
    offsety_top
    offsety
    scalex_bottom
    scalex_mid
    scalex_top
    scaley_bottom
    scaley_mid
    scaley_top
    sector
    smoothlighting
    texturebottom
    texturemiddle
    texturetop
    wrapmidtex '''

vertexDataset = "placeholder"
def get_vertexes():
    # x
    # y
    '''d'''

sectorDataset = "placeholder"
def get_sectors():
    '''xpanningfloor
    ypanningfloor
    xpanningceiling
    ypanningceiling
    xscalefloor
    yscalefloor
    xscaleceiling
    yscaleceiling
    rotationfloor
    rotationceiling
    ceilingplane_a
    ceilingplane_b
    ceilingplane_c
    ceilingplane_d
    floorplane_a
    floorplane_b
    floorplane_c
    floorplane_d
    lightfloor
    lightceiling
    lightfloorabsolute
    lightceilingabsolute
    alphafloor
    alphaceiling
    renderstylefloor
    renderstyleceiling
    gravity
    lightcolor
    fadecolor
    desaturation
    silent
    nofallingdamage
    dropactors
    norespawn
    soundsequence
    hidden
    waterzone
    moreids
    damageamount
    damagetype
    damageinterval
    leakiness
    damageterraineffect
    damagehazard
    floorterrain
    ceilingterrain
    portal_ceil_alpha
    portal_ceil_blocksound
    portal_ceil_disabled
    portal_ceil_nopass
    portal_ceil_norender
    portal_ceil_overlaytype
    portal_floor_alpha
    portal_floor_blocksound
    portal_floor_disabled
    portal_floor_nopass
    portal_floor_norender
    portal_floor_overlaytype
    noattack '''

# def get_segs()
# def get_ssectors():
# def get_nodes
# def get_reject():
# def blockmap():
