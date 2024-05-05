from analysis_tools import analysis, forces

width = 0.025 # [m]

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0-10',
         U=10,
         t_treshold=1500,
         dt=10,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0.25-10',
         U=10,
         t_treshold=1500,
         dt=10,
         L= 0.3+0.6*0.25,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0.5-10',
         U=10,
         t_treshold=1500,
         dt=10,
         L= 0.3+0.6*0.5,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-1-10',
         U=10,
         t_treshold=1500,
         dt=10,
         L= 0.3+0.6*1,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0-100',
         U=100,
         t_treshold=250,
         dt=1,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0.25-100',
         U=100,
         t_treshold=250,
         dt=1,
         L= 0.3+0.6*0.25,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0.5-100',
         U=100,
         t_treshold=250,
         dt=1,
         L= 0.3+0.6*0.5,
         )


analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-1-100',
         U=100,
         t_treshold=250,
         dt=1,
         L= 0.3+0.6*1,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0-1071',
         U=1071,
         t_treshold=20,
         dt=0.01,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0.25-1071',
         U=1071,
         t_treshold=20,
         dt=0.05,
         L= 0.3+0.6*0.25,
         )


analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0.5-1071',
         U=1071,
         t_treshold=20,
         dt=0.03,
         L= 0.3+0.6*0.5,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-1-1071',
         U=1071,
         t_treshold=20,
         dt=0.05,
         L= 0.3+0.6*1,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0-5000',
         U=5000,
         t_treshold=8,
         dt=0.01375,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0.25-5000',
         U=5000,
         t_treshold=8,
         dt=0.01375,
         L= 0.3+0.6*0.25,
         )

analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-0.5-5000',
         U=5000,
         t_treshold=8,
         dt=0.01375,
         L= 0.3+0.6*0.5,
         )


analysis(path='in-depth',
         directory='results/hexagon-18',
         file='AR-1-5000',
         U=5000,
         t_treshold=8,
         dt=0.01375,
         L= 0.3+0.6*1,
         )

forces(Res=[205, 2053, 21992, 102669],
       C_Ls_RMS= [[0.148, 1.575, 1.100, 1.352],  [0.042, 0.763, 0.158, 0.223],     [0.027, 0.214, 0.049, 0.047], [0.053, 0.108, 0.005, 0.021]],
       C_Ls_mean=[[-0.018, 0.034, 0.022, 0.002], [-0.004, -0.054, -0.006, -0.005], [0.014, 0.081, 0.002, 0.001], [0.051, -0.013, 0.000, 0.0]],
       C_Ds_mean=[[1.296, 2.244, 0.946, 1.946],  [1.067, 1.658, 1.288, 1.274],     [0.933, 1.038, 0.652, 0.499], [0.822, 0.664, 0.378, 0.285]],
       Sts      =[[0.129, 0.120, 0.140, 0.139],  [0.140, 0.120, 0.140, 0.139],     [0.140, 0.140, 0.224, 0.239], [0.140, 0.180, 0.224, 0.319]]
       )