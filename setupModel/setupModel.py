####################################################################################################
# setupModel.py
####################################################################################################

import matplotlib.pyplot as plt
from keras import models
from keras import layers
from loadDataset import loadDataset


def setupModel():
    # LOAD DATASET
    data_train, labels_train, data_validation, labels_validation, data_test, labels_test = loadDataset()

    # ******************** DEFINE MODEL ********************
    model = models.Sequential()
    model.add(layers.Dense(128, activation='relu', input_shape=(1506,)))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
        # end network with Dense layer of size 10  --> for each input sample, network will output 10-dimensional vector, which each entry encoding a different output class
        # softmax activation --> network will output probability distribution over the 10 different output classes

    # ******************** COMPILE MODEL ********************
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
        # encoding the labels via categorical encoding (also known as one-hot encoding) and using categorical_crossentropy as a loss function

    # ******************** TRAIN MODEL ********************
    history = model.fit(data_train,
                        labels_train,
                        epochs=20,
                        batch_size=10,
                        validation_data=(data_validation, labels_validation))

    # ******************** PLOT TRAINING AND VALIDATION LOSS ********************
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(loss) + 1)

    plt.figure()
    plt.plot(epochs, loss, 'bo', label='training loss')
    plt.plot(epochs, val_loss, 'b', label='validation loss')
    plt.title('training and validation loss')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend()

    # ******************** PLOT TRAINING AND VALIDATION ACCURACY ********************
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    plt.figure()
    plt.plot(epochs, acc, 'bo', label='training acc')
    plt.plot(epochs, val_acc, 'b', label='validation acc')
    plt.title('training and validation accuracy')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend()

    # ******************** EVALUATE MODEL ********************
    results = model.evaluate(data_test, labels_test)
    print(results)

    # ******************** SHOW PLOTS ********************
    plt.show()

setupModel()
