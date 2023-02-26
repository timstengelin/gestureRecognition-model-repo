####################################################################################################
# setupParameterizationModel.py
####################################################################################################

import matplotlib.pyplot as plt
import numpy as np
from keras import models
from keras import layers
from loadDataset import loadDataset
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def setupParameterizationModel():
    # ******************** LOAD DATASET ********************
    data_train, labels_train, data_validation, labels_validation, data_test, labels_test = loadDataset()

    # ******************** DEFINE MODEL ********************
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(1506,)))
    model.add(layers.Dropout(0.1))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.1))
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
                        epochs=80,
                        batch_size=8,
                        validation_data=(data_validation, labels_validation))
    print('\n\n')

    # ******************** PRINT MODEL SUMMARY ********************
    model.summary()
    print('\n\n')

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
    plt.plot(epochs, acc, 'bo', label='training accuracy')
    plt.plot(epochs, val_acc, 'b', label='validation accuracy')
    plt.title('training and validation accuracy')
    plt.xlabel('epochs')
    plt.ylabel('accuracy')
    plt.legend()

    # ******************** EVALUATE MODEL ********************
    results = model.evaluate(data_test, labels_test)
    print("test loss: {0}, test accuarcy: {1}".format(results[0], results[1]))

    # ******************** PREDICT LABELS FOR TEST DATA ********************
    predictions = model.predict(data_test)
    predictions

    print("shape: {0}, sum: {1}, largest entry: {2}\n\n".format(predictions[0].shape, np.sum(predictions[0]), np.argmax(predictions[0])))

    labels_predictions = np.argmax(predictions, axis=1)
    labels_test_nonCategorial = np.argmax(labels_test, axis=1)
    cm = confusion_matrix(labels_test_nonCategorial, labels_predictions, normalize='true')
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)

    # ******************** SHOW PLOTS ********************

    disp.plot()
    plt.show()

setupParameterizationModel()
