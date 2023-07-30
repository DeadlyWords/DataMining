import matplotlib.pyplot as plt

x = [20739838, 682106452, 895431078, 2092213417, 933663541,
     420124958, 113937770, 1544170913, 540660796, 882687915]

sorted = x.sort()

plt.figure(figsize=(15, 8))
plt.hist(x, edgecolor="red", bins=sorted)
plt.show()
