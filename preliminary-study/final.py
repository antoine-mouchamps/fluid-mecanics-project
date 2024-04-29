from matplotlib import pyplot as plt
from matplotlib.axes import Axes
import csv
import numpy as np

plt.rcParams.update({'font.size': 15})

width = 0.025 # [m]

file = open('results/preliminaryreport-final.csv')
csvreader = csv.reader(file)

times = []
raw_lifts = []
raw_drags = []
for row in csvreader:
    times.append(float(row[1]))
    raw_lifts.append(abs(float(row[5]))/width)
    raw_drags.append(abs(float(row[10]))/width)
    
indices = [i for i in range(len(times)) if times[i] > 1000 and times[i] <= 1500]
i_max1 = [i for i in range(len(times)) if times[i] > 650 and times[i] <= 900][0]
i_max2 = [i for i in range(len(times)) if times[i] > 900 and times[i] <= 1100][0]

print(f'frequency: {1/(times[i_max2] - times[i_max1])} Hz')

lifts = [raw_lifts[i] for i in indices]
drags = [raw_drags[i] for i in indices]
mean_lift = sum(lifts)/len(lifts)
mean_drag = sum(drags)/len(drags)

print(f'l:{mean_lift:.5f}, d:{mean_drag:.5f}')
    
ax:Axes = None
fig, ax = plt.subplots()

ax.plot(times, raw_lifts, label=r'Portance $|F_{Lift}|$')
ax.plot(times, raw_drags, label=r'Trainée $|F_{Drag}|$')

ax.legend()

ax.set_xlim(left=0)
ax.set_xlabel(r'Temps $[s]$')
ax.set_ylim(bottom=0, top=0.001/width)
ax.set_ylabel(r'|Forces| $[mN/m]$')

# ax.grid(True)
fig.savefig('forces-final-with-times.pdf', bbox_inches='tight')

file.close()