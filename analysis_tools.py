from matplotlib import pyplot as plt
from matplotlib.axes import Axes
import csv
import numpy as np
import numpy.fft as fft

from adimensionnal_numbers import Strouhal, Reynolds, C_L, C_D

plt.rcParams.update({'font.size': 15})

width = 0.025 # [m]

def analysis(path, directory, file, U, t_treshold, dt, y_lims=[-5, 5], D=0.3, L=0.3):
    Re = Reynolds(U/1000, D)
    print(f'Reynolds Number: {Re:.2f}')
    
    fileee = open(f'{path}/{directory}/{file}.csv')
    csvreader = csv.reader(fileee)

    times = []
    raw_lifts = []
    raw_drags = []
    i = 0
    for row in csvreader:
        if(len(row) == 35):
            i += 1
            if(i > 1):
                times.append(float(row[1]))
                raw_lifts.append(float(row[5])/width)
                raw_drags.append(float(row[10])/width)
    
    indices = [i for i in range(len(times)) if times[i] > t_treshold]
    
    spectrum = fft.rfft([raw_lifts[i] for i in indices])
    freqs = fft.rfftfreq(len(indices), d=dt)
    
    freq = abs(freqs[[i for i in range(1, len(spectrum)) if round(abs(spectrum[i]),5) == round(max(abs(spectrum[1:])),5)][0]])
    
    fig, ax = plt.subplots()
    ax.semilogy(freqs, abs(spectrum), label=r'$C_{d}$')
    ax.legend()
    ax.set_xlabel(r'Frequency')
    ax.set_ylabel(r'|A|')
    
    ax.grid()
    
    fig.savefig(f'{path}/FFT-{file}-{round(Re)}.pdf', bbox_inches='tight')
    
    # i_max1 = [i for i in range(len(times)) if times[i] > t1-t1/10 and times[i] <= t1+t1/10][0]
    # i_max2 = [i for i in range(len(times)) if times[i] > t2-t2/10 and times[i] <= t2+t2/10][0]
    
    # print(f'max 1: {C_L(raw_lifts[i_max2]/1000, U/1000, L):.2f}, max 2: {C_L(raw_lifts[i_max2]/1000, U/1000, L):.2f}')

    # freq = 1/(times[i_max2] - times[i_max1])
    
    print(f'frequency: {freq:.2E} Hz')
    print(f'Strouhal Number: {Strouhal(U/1000, D, freq):.3f}')

    # lifts = [raw_lifts[i] for i in range(i_max1, i_max2+1)]
    # drags = [raw_drags[i] for i in range(i_max1, i_max2+1)]
    # mean_lift = sum(lifts)/len(lifts)
    # mean_drag = sum(drags)/len(drags)

    # print(f'Mean lift:{mean_lift:.5f} mN/m, Mean drag:{mean_drag:.5f} mN/m')
    # print(f'Mean C_lift:{C_L(mean_lift/1000, U/1000, L):.2f}, Mean C_drag:{C_D(mean_drag/1000, U/1000, D):.2f}')
        
    ax:Axes = None
    fig, ax = plt.subplots()
    
    C_Ls = [C_L(lift/1000, U/1000, L) for lift in raw_lifts]
    C_Ds = [C_D(drag/1000, U/1000, D) for drag in raw_drags]
    
    print(f'C_drag: {C_Ds[-1]:.3f}')

    ax.plot(times, C_Ls, label=r'$C_{\ell}$')
    ax.plot(times, C_Ds, label=r'$C_{d}$')

    ax.legend()

    ax.set_xlim(left=0)
    ax.set_xlabel(r'Temps $[s]$')
    ax.set_ylim(y_lims)
    ax.set_ylabel(r'|Forces| $[mN/m]$')
    
    ax.grid()

    # ax.grid(True)
    fig.savefig(f'{path}/{file}-{round(Re)}.pdf', bbox_inches='tight')

    fileee.close()
    
    print('\n')
    
def forces(Res, C_Ls_RMS, C_Ds, Sts):
    ax:Axes = None
    fig, ax = plt.subplots()
    
    ARs = [0, 0.25, 0.5, 1]
    
    for C_D, AR in zip(C_Ds, ARs):
        ax.semilogx(Res, C_L, label=r'$C_{{d}} pour AR={}$'.format(AR))

    ax.legend()

    ax.set_xlabel(r'Re')
    ax.set_ylabel(r'C_{{d}}')
    
    ax.grid()

    ax.grid(True)
    fig.savefig(f'lifts_evolution.pdf', bbox_inches='tight')