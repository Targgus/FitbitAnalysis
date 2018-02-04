import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("steps20180203.csv")

totalSteps = df['Total Steps']
time = df['Time']

stepsToWork = [totalSteps[i] for i in range(len(totalSteps)) if time[i] >= '05:30:00' and time[i] <= '06:45:00']
timeToWork = [time[i] for i in range(len(time)) if time[i] >= '05:30:00' and time[i] <= '06:45:00']

# plt.plot(time, totalSteps)
plt.plot(timeToWork, stepsToWork)
plt.xticks(rotation='vertical')
plt.show()
