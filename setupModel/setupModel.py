####################################################################################################
# setupModel.py
####################################################################################################

from keras import models
from keras import layers

from setupModel.loadDataset import loadDataset


def setupModel():
    # LOAD DATASET
    data_train, labels_train, data_validation, labels_validation, data_test, labels_test = loadDataset()

    # MODEL DEFINITON
    model = models.Sequential()
    model.add(layers.Dense(32, activation='relu', input_shape=(6,250,)))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
        # end network with Dense layer of size 10  --> for each input sample, network will output 10-dimensional vector, which each entry encoding a different output class
        # softmax activation --> network will output probability distribution over the 10 different output classes

    # COMPILING THE MODEL
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
        # encoding the labels via categorical encoding (also known as one-hot encoding) and using categorical_crossentropy as a loss function

    # TRAINING THE MODEL
    history = model.fit(data_train,
                        labels_train,
                        epochs=20,
                        batch_size=10,
                        validation_data=(data_validation, labels_validation))

    # PLOTTING THE TRAINING AND VALIDATION LOSS
    # TODO

    # PLOTTING THE TRAINING AND VALIDATION ACCURACY
    # TODO

    # EVALUATE MODEL
    results = model.evaluate(data_test, labels_test)
    print(results)


setupModel()
