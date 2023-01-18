####################################################################################################
# setupModel.py
####################################################################################################

import matplotlib.pyplot as plt
from keras import models
from keras import layers
from loadDataset import loadDataset
from sklearn.model_selection import StratifiedShuffleSplit
from keras.utils.np_utils import to_categorical


def setupParameterizationModel():
    # ******************** LOAD DATASET ********************
    data, labels = loadDataset()

    # ******************** SPLIT DATA ********************
    trainTestSplit = StratifiedShuffleSplit(n_splits = 1, test_size = 0.25)
    trainValidationSplit =  StratifiedShuffleSplit(n_splits = 1, test_size = 0.25)

    for i, (idx_train, idx_test) in enumerate(trainTestSplit.split(data, labels)):
        data_train, data_test = data[idx_train], data[idx_test]
        labels_train, labels_test = labels[idx_train], labels[idx_test]
    print("trainTestSplit:\nshape \"data_train\": {0}\nshape \"labels_train\": {1}\nshape \"data_test\": {2}\nshape \"labels_test\": {3}\n" \
          .format(data_train.shape, labels_train.shape, data_test.shape, labels_test.shape))

    for i, (idx_train, idx_validation) in enumerate(trainTestSplit.split(data_train, labels_train)):
        data_train, data_validation = data_train[idx_train], data_train[idx_validation]
        labels_train, labels_validation = labels_train[idx_train], labels_train[idx_validation]
    print("trainValidationSplit:\nshape \"data_train\": {0}\nshape \"labels_train\": {1}\nshape \"data_validation\": {2}\nshape \"labels_validation\": {3}\n" \
          .format(data_train.shape, labels_train.shape, data_validation.shape, labels_validation.shape))

    # ******************** ONE-HOT ENCODE LABELS ********************
    labels_train = to_categorical(labels_train)
    labels_validation = to_categorical(labels_validation)
    labels_test = to_categorical(labels_test)

    # ******************** DEFINE MODEL ********************
    model = models.Sequential()
    model.add(layers.Dense(512, activation='relu', input_shape=(1506,)))
    model.add(layers.Dropout(0.25))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dropout(0.25))
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
                        epochs=100,
                        batch_size=8,
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
    plt.plot(epochs, acc, 'bo', label='training accuracy')
    plt.plot(epochs, val_acc, 'b', label='validation accuracy')
    plt.title('training and validation accuracy')
    plt.xlabel('epochs')
    plt.ylabel('accuracy')
    plt.legend()

    # ******************** EVALUATE MODEL ********************
    results = model.evaluate(data_test, labels_test)
    print(results)

    # ******************** SHOW PLOTS ********************
    plt.show()

setupParameterizationModel()