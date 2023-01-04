import os
import pandas as pd
import numpy as np

# ******************** SETTINGS ********************
gestures = range(0, 4 + 1)
samplesPerGesture = 100
featuresPerSample = 6 # unused
timestepsPerFeature = 251


def loadDataset():
    # ******************** LOAD DATA ********************
    data = pd.DataFrame(columns=['aX', 'aY', 'aZ', 'gX', 'gY', 'gZ'])
    labels = np.array(gestures)

    for i in gestures:
        gestureDirectory = "gesture_number" + str(i)
        for j in range(1, samplesPerGesture + 1):
            fileName = "number" + str(i) + "_" + str(j) + ".csv"
            filePath = os.path.realpath("..\\data\\datasets\\" + gestureDirectory + "\\" + fileName)
            sampleData = pd.read_csv(filePath, names=["aX", "aY", "aZ", "gX", "gY", "gZ"], sep=",")
            data = pd.concat([data, sampleData])

    # ******************** NORMALIZE DATA ********************
    print("description \"data\":\n", data.describe())
    normalizedData = (data - data.min()) / (data.max() - data.min())
    # [125500 (= gestures*samplesPerGesture*timestepsPerFeature) rows  x 6 (featuresPerSample) columns]
    print("description \"normalizedData\":\n", normalizedData.describe())

    # ******************** CONVERT DATA INTO NUMPY ARRAY ********************
    normalizedData_allSamples = pd.DataFrame()
    # [1506 (= features*timestepsPerFeature = timesteps) rows x 1000 (= gestures*samplesPerGesture = samples) columns]

    for i in gestures:
        for j in range(1, samplesPerGesture + 1):
            idx = i * samplesPerGesture * timestepsPerFeature + (j - 1) * timestepsPerFeature
            # idx = 0; 251; 502; 753; ...
            normalizedData_oneSample = normalizedData.iloc[idx:idx + timestepsPerFeature].to_numpy().flatten().tolist()
            # [1506 (= features*timestepsPerFeature = timesteps) elements]
            idx = i * samplesPerGesture + (j - 1)
            # idx = 0; 1; 2; 3; ...; 999
            normalizedData_allSamples[idx] = normalizedData_oneSample
            normalizedData_allSamples = normalizedData_allSamples.copy()

    normalizedData_allSamples = normalizedData_allSamples.transpose().to_numpy()
    # [1000 (= gestures*samplesPerGesture = samples) rows x 1506 (= features*timestepsPerFeature = timesteps) columns]

    print('bp')


loadDataset()