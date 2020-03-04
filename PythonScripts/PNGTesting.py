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
import seaborn as sns
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from pandas.io.json import json_normalize

#This function decodes the map PNG into a tensor
def mapTensorConversion(filename):
    # Documentation available at : https://www.tensorflow.org/api_docs/python/tf/io/decode_png
    map_image = tf.read_file( filename )
    map_decoded = tf.image.decode_png( map_image )
    print(map_decoded)

    # Returns the map as a UINT8 Tensor
    return map_decoded

mapTensorConversion("JSONData/CATWALK.png")
