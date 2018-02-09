import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Heart/heart20180205.csv")

time = df['Time']
hRate = df['Heart Rate']


startTime = '05:30:00'
endTime = '6:00:00'

bpmAtWork = [hRate[i] for i in range(len(hRate)) if time[i] >= startTime and time[i] <= endTime]
timeAtWork = [time[i] for i in range(len(time)) if time[i] >= startTime and time[i] <= endTime]


fig, ax = plt.subplots()
plt.plot(timeAtWork, bpmAtWork)  # plots bpm along xaxis and time along y axis for readability
plt.xticks(rotation='vertical')
start, end = ax.get_xlim()  # sets y limits to start and end of list
print(start, end)
ax.xaxis.set_ticks(np.arange(start, end, 50))  # limits every y axis label to every 10th point
plt.tight_layout()  # shows all label values
plt.show()  # prints plot to screens


