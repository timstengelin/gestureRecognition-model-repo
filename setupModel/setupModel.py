####################################################################################################
# setupModel.py
####################################################################################################

from keras import models
from keras import layers

from setupModel.loadDataset import loadDataset


def vectorize_data():
    print('TODO')


def setupModel():
    # LOAD DATASET
    loadDataset()

    # ENCODING THE DATA
    train_data = 0
    test_data = 0

    # ENCODING THE LABELS
    train_labels = 0
    test_labels = 0
        # encoding the labels via categorical encoding (also known as one-hot encoding)

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

    # SETTING ASIDE A VALIDATION SET
    # maybe TODO
    val_data = 0
    train_partial_data = 0

    val_labels = 0
    train_partial_labels = 0

    # TRAINING THE MODEL
    history = model.fit(train_partial_data,
                        train_partial_labels,
                        epochs=4,
                        batch_size=10,
                        validation_data=(val_data, val_labels))

    # PLOTTING THE TRAINING AND VALIDATION LOSS
    # TODO

    # PLOTTING THE TRAINING AND VALIDATION ACCURACY
    # TODO

    # EVALUATE MODEL
    results = model.evaluate(test_data, test_labels)
    print(results)


setupModel()
