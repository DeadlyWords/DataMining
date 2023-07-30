import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4,5,6,7])

time = [20.566870100001324, 23.45873810000012, 427.220321499998, 
     118.5005412999999, 26.154920499997388, 21.906652300000133,
     0.1, 0.114]

passedTests = [0, 6, 0, 21, 21, 4, 14, 20]

fig, ax1 = plt.subplots()

color = 'tab:blue'
custom_ticks = ['Middle Square', 'Lehmer', 'BBS', 'MT19937', 'Xoro128+', 'CBRNG', 'rand', 'rand48']
ax1.set_ylabel('Time for generating 30 million numbers (s)', color=color)
ax1.plot(time, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:red'
ax2.set_ylabel('Passed Tests', color=color)
ax2.plot(passedTests, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.xticks(x, custom_ticks)
plt.show()