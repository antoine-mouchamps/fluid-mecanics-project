from analysis_tools import analysis, forces

width = 0.025 # [m]

# analysis(path='in-depth',
#          directory='results/hexagon-18',
#          file='AR-0-10',
#          U=10,
#          t_treshold=1500,
#          dt=10,
#          )

# analysis(path='in-depth',
#          directory='results/hexagon-18',
#          file='AR-0.25-10',
#          U=10,
#          t_treshold=1500,
#          dt=10,
#          )

# analysis(path='in-depth',
#          directory='results/hexagon-18',
#          file='AR-0.5-10',
#          U=10,
#          t_treshold=1500,
#          dt=10,
#          )

# analysis(path='in-depth',
#          directory='results/hexagon-18',
#          file='AR-1-10',
#          U=10,
#          t_treshold=1500,
#          dt=10,
#          )

# analysis(path='in-depth',
#          directory='results/hexagon-18',
#          file='AR-0-100',
#          U=100,
#          t_treshold=250,
#          dt=1,
#          )

# analysis(path='in-depth',
#          directory='results/hexagon-18',
#          file='AR-0.25-100',
#          U=100,
#          t_treshold=250,
#          dt=1,
#          )

# analysis(path='in-depth',
#          directory='results/hexagon-18',
#          file='AR-0.5-100',
#          U=100,
#          t_treshold=250,
#          dt=1,
#          )


# analysis(path='in-depth',
#          directory='results/hexagon-18',
#          file='AR-1-100',
#          U=100,
#          t_treshold=250,
#          dt=1,
#          )

# analysis(path='in-depth',
#          directory='results/hexagon-18',
#          file='AR-0-1071',
#          U=1071,
#          t_treshold=25,
#          dt=0.25,
#          )

# analysis(path='in-depth',
#          directory='results/hexagon-18',
#          file='AR-0-5000',
#          U=5000,
#          t_treshold=2,
#          dt=0.005,
#          )

forces(Res=[205, 2053, 21992, 102669],
       C_Ls_RMS=[],
       C_Ds=[[1.301, 2.256, 0, 0], [0.070, 1.679, 0, 0], [0.932, 1.042, 0, 0], [0.822, 0.664, 0, 0]],
       Sts =[[0.129, 0.120, 0, 0], [0.140, 0.120, 0, 0], [0.140, 0.140, 0, 0], [0.140, 0.180, 0, 0]]
       )