from analysis_tools import analysis

width = 0.025 # [m]

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='10',
         U=10,
         time_interval=[1600, 1800],
         t_treshold=1250,
         )