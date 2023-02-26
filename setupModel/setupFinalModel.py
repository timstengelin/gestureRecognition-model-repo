####################################################################################################
# setupFinalModel.py
####################################################################################################

import numpy as np
from keras import models
from keras import layers
from loadDataset import loadDataset


def setupFinalModel():
    # ******************** LOAD DATASET ********************
    data_train, labels_train, data_validation, labels_validation, data_test, labels_test = loadDataset()

    # ******************** DEFINE MODEL ********************
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(1506,)))
    model.add(layers.Dropout(0.1))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.1))
    model.add(layers.Dense(10, activation='softmax'))

    # ******************** COMPILE MODEL ********************
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # ******************** TRAIN MODEL ********************
    history = model.fit(np.concatenate((data_train, data_validation), axis=0),
                        np.concatenate((labels_train, labels_validation), axis=0),
                        epochs=80,
                        batch_size=8)

    # ******************** EVALUATE MODEL ********************
    results = model.evaluate(data_test, labels_test)
    print("test loss: {0}, test accuarcy: {1}".format(results[0], results[1]))

    # ******************** SHOW MODEL SUMMARY ********************
    model.summary()

    return model
