####################################################################################################
# loadDatset.py
####################################################################################################

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from keras.utils.np_utils import to_categorical

import matplotlib.pyplot as plt #TS

# ******************** SETTINGS ********************
gestures = range(0, 9 + 1)
samplesPerGesture = 100
featuresPerSample = 6 # unused
timestepsPerFeature = 251


def loadDataset():
    # ******************** LOAD DATA ********************
    rawData = pd.DataFrame(columns=['aX', 'aY', 'aZ', 'gX', 'gY', 'gZ'])

    for i in gestures:
        gestureDirectory = "gesture_number" + str(i)
        for j in range(1, samplesPerGesture + 1):
            fileName = "number" + str(i) + "_" + str(j) + ".csv"
            filePath = os.path.realpath("..\\data\\datasets\\" + gestureDirectory + "\\" + fileName)
            sampleData = pd.read_csv(filePath, names=["aX", "aY", "aZ", "gX", "gY", "gZ"], sep=",")

            sampleDataNormalized = sampleData

            aX = sampleData['aX']
            aXNormalized = (aX - aX.min()) / (aX.max() - aX.min())
            #plt.plot(aX)
            #plt.plot(aXNormalized)
            sampleDataNormalized['aX'] = aXNormalized

            aY = sampleData['aY']
            aYNormalized = (aY - aY.min()) / (aY.max() - aY.min())
            sampleDataNormalized['aY'] = aYNormalized

            aZ = sampleData['aZ']
            aZNormalized = (aZ - aZ.min()) / (aZ.max() - aZ.min())
            sampleDataNormalized['aZ'] = aZNormalized

            gX = sampleData['gX']
            gXNormalized = (gX - gX.min()) / (gX.max() - gX.min())
            sampleDataNormalized['gX'] = gXNormalized

            gY = sampleData['gY']
            gYNormalized = (gY - gY.min()) / (gY.max() - gY.min())
            sampleDataNormalized['gY'] = gYNormalized

            gZ = sampleData['gZ']
            gZNormalized = (gZ - gZ.min()) / (gZ.max() - gZ.min())
            sampleDataNormalized['gZ'] = gZNormalized

            #rawData = pd.concat([rawData, sampleData]) #TS
            rawData = pd.concat([rawData, sampleDataNormalized])

    # ******************** NORMALIZE DATA ********************
    normalizedData = rawData
        # [125500 (= gestures*samplesPerGesture*timestepsPerFeature) rows  x 6 (featuresPerSample) columns]
    print("description \"normalizedData\":\n", normalizedData.describe(), "\n\n")

    # ******************** CONVERT DATA INTO NUMPY ARRAY ********************
    normalizedData_allSamples = pd.DataFrame()
        # [1506 (= features*timestepsPerFeature = timesteps) rows x 1000 (= gestures*samplesPerGesture = samples) columns]
    labels_allSamples = []

    for i in gestures:
        for j in range(1, samplesPerGesture + 1):
            idx = i * samplesPerGesture * timestepsPerFeature + (j - 1) * timestepsPerFeature
                # idx = 0; 251; 502; 753; ...

            helper = normalizedData.iloc[idx:idx + timestepsPerFeature]
            helper2 = ((((helper['aX'].squeeze().append(helper['aY'].squeeze())).append(helper['aZ'].squeeze())).append(helper['gX'].squeeze())).append(helper['gY'].squeeze())).append(helper['gZ'].squeeze())
            normalizedData_oneSample = helper2.to_numpy().flatten().tolist()
            # [1506 (= features*timestepsPerFeature = timesteps) elements]

            idx = i * samplesPerGesture + (j - 1)
                # idx = 0; 1; 2; 3; ...; 999
            normalizedData_allSamples[idx] = normalizedData_oneSample
            normalizedData_allSamples = normalizedData_allSamples.copy()
            labels_allSamples.append(i)

    data = normalizedData_allSamples.transpose().to_numpy()
        # [1000 (= gestures*samplesPerGesture = samples) rows x 1506 (= features*timestepsPerFeature = timesteps) columns]
    print("shape \"data\": {0}\n\n".format(data.shape))
    labels = np.array(labels_allSamples)
        # [1000 (= gestures*samplesPerGesture = samples) rows]
    print("shape \"labels\": {0}\n\n".format(labels.shape))

    # ******************** SPLIT DATA ********************
    trainTestSplit = StratifiedShuffleSplit(n_splits=1, test_size=0.25)
    trainValidationSplit = StratifiedShuffleSplit(n_splits=1, test_size=0.25)

    for i, (idx_train, idx_test) in enumerate(trainTestSplit.split(data, labels)):
        data_train, data_test = data[idx_train], data[idx_test]
        labels_train, labels_test = labels[idx_train], labels[idx_test]
    print(
        "trainTestSplit:\nshape \"data_train\": {0}\nshape \"labels_train\": {1}\nshape \"data_test\": {2}\nshape \"labels_test\": {3}\n\n" \
        .format(data_train.shape, labels_train.shape, data_test.shape, labels_test.shape))

    for i, (idx_train, idx_validation) in enumerate(trainTestSplit.split(data_train, labels_train)):
        data_train, data_validation = data_train[idx_train], data_train[idx_validation]
        labels_train, labels_validation = labels_train[idx_train], labels_train[idx_validation]
    print(
        "trainValidationSplit:\nshape \"data_train\": {0}\nshape \"labels_train\": {1}\nshape \"data_validation\": {2}\nshape \"labels_validation\": {3}\n\n" \
        .format(data_train.shape, labels_train.shape, data_validation.shape, labels_validation.shape))

    # ******************** ONE-HOT ENCODE LABELS ********************
    labels_train = to_categorical(labels_train)
    labels_validation = to_categorical(labels_validation)
    labels_test = to_categorical(labels_test)

    return data_train, labels_train, data_validation, labels_validation, data_test, labels_test
