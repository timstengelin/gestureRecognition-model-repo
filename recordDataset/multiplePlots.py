import pandas as pd
import matplotlib.pyplot as plt

#**************** Plot  settings ****************************

# Select the gesture wich should be plotted
fileName = "number1_"
# File typ must always be .csv
fileTyp = ".csv"

# Select the number of files wich should be visualized
startFile = 1
endFile = 4

# When True legend will also be visualized
withLegend = True

#************************************************************


# Create a list of all file names
fileNames = list()
for i in range(startFile, endFile+1):
    fileNames.append(fileName+str(i)+fileTyp)

fig, axs = plt.subplots(1, 3, figsize = [15,5])
fig.tight_layout(pad=3.0)   # Space between the subplots

# Plot all values of the Files in different subplots
for name in fileNames:
    data = pd.read_csv(name, names=["Sample", "aX", "aY", "aZ"], sep=",")

    axs[0].plot(data["aX"], )
    axs[1].plot(data["aY"])
    axs[2].plot(data["aZ"])

axs[0].set_title("aX")
axs[1].set_title("aY")
axs[2].set_title("aZ")

axs[0].set_ylim([-5,25])
axs[1].set_ylim([-10,10])
axs[2].set_ylim([-10,10])

for ax in axs.flat:
    ax.set(xlabel='samples', ylabel='a in m/s^2')
    ax.grid()

if withLegend:
    axs[2].legend(fileNames, loc="upper left", bbox_to_anchor=(1, 1))
    plt.tight_layout()

plt.show()