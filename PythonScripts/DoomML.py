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

# Just disables the warning, doesn't enable AVX/FMA
import os

#This function serves as a constructor for the data in question
def map(linedefData,sidedefData,vertexData,sectorData):
    lineDefCols="placeholder"