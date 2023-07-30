import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4])

time = [23.45873810000012, 
     118.5005412999999, 26.154920499997388,
     0.1, 0.114]

passedTests = [5,19, 21,14, 19]

fig, ax1 = plt.subplots()

color = 'tab:blue'
custom_ticks = ['Lehmer','MT19937', 'Xoro128+','rand', 'rand48']
ax1.set_ylabel('Time for generating 30 million numbers (s)', color=color)
ax1.plot(time, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:red'
ax2.set_ylabel('Passed Tests', color=color)
ax2.plot(passedTests, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0, max(passedTests)+2)
plt.xticks(x, custom_ticks)
ax1.tick_params(axis='x', labelrotation = 45)
plt.show()