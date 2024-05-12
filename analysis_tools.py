from matplotlib import pyplot as plt
from matplotlib.axes import Axes
import csv
import numpy as np
import numpy.fft as fft

from adimensionnal_numbers import Strouhal, Reynolds, C_L, C_D

plt.rcParams.update({'font.size': 15})

width = 0.025 # [m]

def analysis(path, directory, file, U, t_treshold, dt, y_lims=[-5, 5], D=0.3, L=0.3):
    print(f'file: {file}')
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
    ax.semilogy(freqs, abs(spectrum)**2)
    ax.axvline(x = freq, color = 'black', linestyle="dashed", linewidth=1)
    # ax.annotate('f_1', 
    #             xy=(freq, 0), 
    #             xytext=(freq, 0),
    #             arrowprops = dict(facecolor='black', shrink=0.05)
    #             )
    ax.set_xlabel(r'Fréquence [Hz]')
    ax.set_ylabel(r'$PSD_{F_{Lift}}\;\mathrm{\left[(mN/m)^2\right]}$')
    
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
    
    C_Ls_periodic = [C_Ls[i] for i in indices]
    C_Ds_periodic = [C_Ds[i] for i in indices]
    print(f'C_lift_mean: {np.sum(C_Ls_periodic)/len(C_Ls_periodic):.3f} and C_lift_RMS: {np.sqrt(np.sum([C*C for C in C_Ls_periodic])/len(C_Ls_periodic)):.3f}')
    print(f'C_drag_mean: {np.sum(C_Ds_periodic)/len(C_Ds_periodic):.3f}')

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

    plt.close(fig)
    fileee.close()
    
    print('\n')
    
    
def forces(Res, C_Ls_RMS, C_Ls_mean, C_Ds_mean, Sts):
    ARs = [0, 0.25, 0.5, 1]
    ax:Axes = None
        
    fig, ax = plt.subplots()
    for C_D, AR in zip(C_Ds_mean, ARs):
        ax.semilogx(Res, C_D, label=r'$AR$={}'.format(AR), marker="o", linestyle="dotted")

    ax.legend()

    ax.set_xlabel(r'$Re$')
    ax.set_ylabel(r'$\overline{C_D}$')
    ax.set_ylim(top=3)
    
    ax.grid()

    ax.grid(True)
    fig.savefig(f'drag_evolution.pdf', bbox_inches='tight')
    plt.close(fig)
    
    
    fig, ax = plt.subplots()
    for St, AR in zip(Sts, ARs):
        ax.semilogx(Res, St, label=r'$AR$={}'.format(AR), marker="o", linestyle="dotted")

    ax.legend()

    ax.set_xlabel(r'$Re$')
    ax.set_ylabel(r'$St$')
    
    ax.grid()

    ax.grid(True)
    fig.savefig(f'St_evolution.pdf', bbox_inches='tight')
    plt.close(fig)
    
    
    fig, ax = plt.subplots()  
    for C_L, AR in zip(C_Ls_mean, ARs):
        ax.semilogx(Res, np.abs(C_L), label=r'$AR$={}'.format(AR), marker="o", linestyle="dotted")

    ax.legend()

    ax.set_xlabel(r'$Re$')
    ax.set_ylabel(r'$\overline{C_L}$')
    ax.set_ylim(top=0.5)
    
    ax.grid()

    ax.grid(True)
    fig.savefig(f'lift_mean_evolution.pdf', bbox_inches='tight')
    plt.close(fig)
    
    
    fig, ax = plt.subplots()  
    for C_L, AR in zip(C_Ls_RMS, ARs):
        ax.semilogx(Res, C_L, label=r'$AR$={}'.format(AR), marker="o", linestyle="dotted")

    ax.legend()

    ax.set_xlabel(r'$Re$')
    ax.set_ylabel(r'$C_{L,RMS}$')
    ax.set_ylim(top=3)
    
    ax.grid()

    ax.grid(True)
    fig.savefig(f'lift_RMS_evolution.pdf', bbox_inches='tight')
    plt.close(fig)