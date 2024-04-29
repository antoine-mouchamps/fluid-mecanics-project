from matplotlib import pyplot as plt
from matplotlib.axes import Axes
import csv

plt.rcParams.update({'font.size': 15})

width = 0.025 # [m]

file = open('results/preliminaryreport-h=5.csv')
csvreader = csv.reader(file)

times = []
lifts = []
drags = []
for row in csvreader:
    times.append(float(row[1]))
    lifts.append(abs(float(row[5]))/width)
    drags.append(abs(float(row[10]))/width)
    
    
ax:Axes = None
fig, ax = plt.subplots()

ax.plot(times, lifts, label=r'Portance $|F_{Lift}|$')
ax.plot(times, drags, label=r'Trainée $|F_{Drag}|$')

ax.legend()

ax.set_xlim(left=0)
ax.set_xlabel(r'Temps $[s]$')
ax.set_ylim(bottom=0, top=0.001/width)
ax.set_ylabel(r'|Forces| $[mN/m]$')

# ax.grid(True)
fig.savefig('forces-with-time.pdf', bbox_inches='tight')

file.close()

heights = [0.5, 1, 2, 3, 4, 5, 7, 10]

means_lift = []
means_drag = []

for height in heights:
    file = open(f'results/preliminaryreport-h={height}.csv')
    csvreader = csv.reader(file)
    times = []
    raw_lifts = []
    raw_drags = []
    for row in csvreader:
        times.append(float(row[1]))
        raw_lifts.append(abs(float(row[5]))/width)
        raw_drags.append(abs(float(row[10]))/width)
        
    indices = [i for i in range(len(times)) if times[i] > 1000 and times[i] <= 1500]

    lifts = [raw_lifts[i] for i in indices]
    drags = [raw_drags[i] for i in indices]
    mean_lift = sum(lifts)/len(lifts)
    mean_drag = sum(drags)/len(drags)
    
    means_lift.append(mean_lift)
    means_drag.append(mean_drag)
        
    file.close()

ax:Axes = None
fig, ax = plt.subplots()

ax.plot(heights, means_lift, label=r'Portance $F_{Lift}$', marker="s", markerfacecolor='none')
ax.plot(heights, means_drag, label=r'Trainée $F_{Drag}$', marker="s", markerfacecolor='none')

ax.legend()

ax.set_xlim(left=0)
ax.set_xlabel(r'Hauteurs $[m]$')
ax.set_ylim(bottom=0.0)
ax.set_ylabel(r'Forces $[mN/m]$')

ax.grid(True)

fig.savefig('convergence-height.pdf', bbox_inches='tight')

means_lift = []
means_drag = []

lengths = [1, 3, 5, 7]
for length in lengths:
    file = open(f'results/preliminaryreport-h=5-l={length}.csv')
    csvreader = csv.reader(file)
    times = []
    raw_lifts = []
    raw_drags = []
    for row in csvreader:
        times.append(float(row[1]))
        raw_lifts.append(abs(float(row[5]))/width)
        raw_drags.append(abs(float(row[10]))/width)
        
    indices = [i for i in range(len(times)) if times[i] > 1000 and times[i] <= 1500]

    lifts = [raw_lifts[i] for i in indices]
    drags = [raw_drags[i] for i in indices]
    mean_lift = sum(lifts)/len(lifts)
    mean_drag = sum(drags)/len(drags)
    
    print(f'l:{mean_lift:.5f}, d:{mean_drag:.5f}')
    
    means_lift.append(mean_lift)
    means_drag.append(mean_drag)
        
    file.close()



ax:Axes = None
fig, ax = plt.subplots()

ax.plot(lengths, means_lift, label=r'Portance $F_{Lift}$', marker="s", markerfacecolor='none')
ax.plot(lengths, means_drag, label=r'Trainée $F_{Drag}$', marker="s", markerfacecolor='none')

ax.legend()

ax.set_xlim(left=0)
ax.set_xlabel(r"Longueur d'entrée $[m]$")
ax.set_ylim(bottom=0.0, top=0.025)
ax.set_ylabel(r'Forces $[mN/m]$')

ax.grid(True)

fig.savefig('convergence-length.pdf', bbox_inches='tight')