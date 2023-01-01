import os
import pandas as pd
import matplotlib.pyplot as plt

gestureDirectory = "gesture_number2"
filename = "number2_1.csv"


newPath = os.path.realpath("..\\data\\datasets\\"+gestureDirectory+"\\"+filename)


fileName = "../data/datasets/gesture_number1/number1_1.csv"

data = pd.read_csv(newPath, names=["Sample", "aX", "aY", "aZ","gX", "gY", "gZ"], sep=",")

# Plot 1

plt.figure(1)
plt.plot(data["aX"])
plt.plot(data["aY"])
plt.plot(data["aZ"])

plt.xlabel("samples")
plt.ylabel("a in m/s^2")
plt.legend(["aX", "aY", "aZ", "gX", "gY", "gZ"], loc="upper right")

plt.ylim((-20,25))
plt.grid()


plt.figure(2)
plt.plot(data["gX"])
plt.plot(data["gY"])
plt.plot(data["gZ"])
plt.legend(["gX", "gY", "gZ"], loc="upper right")
plt.ylim((-300,300))

plt.grid()
plt.show()