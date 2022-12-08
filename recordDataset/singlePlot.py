import os
import pandas as pd
import matplotlib.pyplot as plt

gestureDirectory = "gesture_number1"
filename = "number1_1.csv"


newPath = os.path.realpath("..\\data\\datasets\\"+gestureDirectory+"\\"+filename)


fileName = "../data/datasets/gesture_number1/number1_1.csv"

data = pd.read_csv(newPath, names=["Sample", "aX", "aY", "aZ"], sep=",")

# Plot 1

plt.figure(1)
plt.plot(data["aX"])
plt.plot(data["aY"])
plt.plot(data["aZ"])

plt.xlabel("samples")
plt.ylabel("a in m/s^2")
plt.legend(["aX", "aY", "aZ"], loc="upper right")

plt.grid()
plt.show()

# Plot 2

fig, axs = plt.subplots(2, 2, figsize = [10,5])
fig.tight_layout(pad=3.5)   # Space between the subplots

axs[0,0].plot(data["aX"], "Blue")
axs[0,0].plot(data["aY"], "Orange")
axs[0,0].plot(data["aZ"], "Green")
axs[0,0].legend(["aX", "aY", "aZ"], loc="upper right")

axs[0,1].plot(data["aX"], "Blue")
axs[0,1].set_title("aX")

axs[1,0].plot(data["aY"], "Orange")
axs[1,0].set_title("aY")

axs[1,1].plot(data["aZ"], "Green")
axs[1,1].set_title("aZ")

for ax in axs.flat:
    ax.set(xlabel='samples', ylabel='a in m/s^2')
    ax.grid()

plt.show()