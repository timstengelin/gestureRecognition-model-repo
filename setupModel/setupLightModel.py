####################################################################################################
# setupLightModel.py
####################################################################################################

from setupFinalModel import *
import tensorflow as tf
from datetime import datetime
import os


def setupLightModel():
    # ******************** LOAD FINAL MODEL ********************
    model = setupFinalModel()

    # ******************** WRITE BYTEFILE ********************
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()

    with open('..\data\models\model_{0}.tflite'.format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")), 'wb') as fd:
        fd.write(tflite_model)


setupLightModel()
