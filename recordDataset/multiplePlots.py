import os
import pandas as pd
import matplotlib.pyplot as plt

#**************** Plot  settings ****************************

# Select the gesture wich should be plotted
gestureDirectory = "gesture_number7"
fileName = "number7_"
# File typ must always be .csv
fileTyp = ".csv"

# Select the number of files wich should be visualized
startFile = 1
endFile = 100

# When True legend will also be visualized
withLegend = True

#************************************************************


# Create a list of all file names and paths
fileNames = list()
filepaths = list()
for i in range(startFile, endFile+1):
    name = fileName+str(i)+fileTyp
    newPath = os.path.realpath("..\\data\\datasets\\"+gestureDirectory+"\\"+name)
    filepaths.append(newPath)
    fileNames.append(name)


fig2, axs2 = plt.subplots(1, 3, figsize = [15,5])
fig2.tight_layout(pad=3.0)   # Space between the subplots

fig1, axs1 = plt.subplots(1, 3, figsize = [15,5])
fig1.tight_layout(pad=3.0)   # Space between the subplots


# Plot all values of the Files in different subplots
for path in filepaths:
    data = pd.read_csv(path, names=["Sample", "aX", "aY", "aZ", "gX", "gY", "gZ"], sep=",")

    axs1[0].plot(data["aX"])
    axs1[1].plot(data["aY"])
    axs1[2].plot(data["aZ"])

    axs2[0].plot(data["gX"])
    axs2[1].plot(data["gY"])
    axs2[2].plot(data["gZ"])

axs1[0].set_title("aX")
axs1[1].set_title("aY")
axs1[2].set_title("aZ")

axs2[0].set_title("gX")
axs2[1].set_title("gY")
axs2[2].set_title("gZ")

axs1[0].set_ylim([-5,30])
axs1[1].set_ylim([-15,15])
axs1[2].set_ylim([-15,20])

axs2[0].set_ylim([-200,200])
axs2[1].set_ylim([-200,200])
axs2[2].set_ylim([-200,200])

for ax in axs1.flat:
    ax.set(xlabel='Samples', ylabel='m/s^2')
    ax.grid()

for gx in axs2.flat:
    gx.set(xlabel='Samples', ylabel='Deg./Sec.')
    gx.grid()

if withLegend:
    axs1[2].legend(fileNames, loc="upper left", bbox_to_anchor=(1, 1))
    axs2[2].legend(fileNames, loc="upper left", bbox_to_anchor=(1, 1))
    fig1.tight_layout()
    fig2.tight_layout()

plt.show()