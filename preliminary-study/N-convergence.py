from matplotlib import pyplot as plt
from matplotlib.axes import Axes
import numpy as np
import datetime
import matplotlib.ticker as tick
import csv

plt.rcParams.update({'font.size': 15})

width = 0.025 # [m]

means_lift = []
means_drag = []

lengths = [0.5, 0.75, 1, 1.5]
elements = [3262, 7263, 13300, 29885]
execution_times = [5*60+9, 12*60+24, 27*60+0, 1*3600+16*60+54]

for length in lengths:
    file = open(f'results/preliminaryconvergence/n={length}.csv')
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

ax.plot([1, 2, 3, 4], means_lift, label=r'Portance $F_{Lift}$', marker="s", markerfacecolor='none')
ax.plot([1, 2, 3, 4], means_drag, label=r'Trainée $F_{Drag}$', marker="s", markerfacecolor='none')

ax2 = ax.twinx()
ax2.plot([1, 2, 3, 4], execution_times, 'r--', marker="s", markerfacecolor='none', label='Temps d\'exécution')

legend_1 = ax.legend(loc='upper right', bbox_to_anchor=(0, 0, 1, 0.38))
legend_1.remove()
ax2.legend(loc='lower right')
ax2.add_artist(legend_1)

ax.set_xlabel(r"Nombre d'éléments $[-]$")
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(elements)
ax.set_ylim(bottom=0.0, top=0.025)
ax.set_ylabel(r'Forces $[mN/m]$')
# ax2.set_ylim(bottom=0)

def timeTicks(xx, pos):
    d = datetime.timedelta(seconds=xx)
    return str(d)

formatter = tick.FuncFormatter(timeTicks)
ax2.yaxis.set_major_formatter(formatter)

plt.setp(ax2.yaxis.get_majorticklabels(),
            rotation=0,
            # ha="left", rotation_mode="anchor"
            )

ax2.set_ylabel(r"Temps $[hh:mm:ss]$")

ax.grid(True)

fig.savefig('convergence-elements.pdf', bbox_inches='tight')