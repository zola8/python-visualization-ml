# https://stackoverflow.com/questions/33742845/how-to-animate-a-seaborns-heatmap-or-correlation-matrix

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import animation

fig = plt.figure()


def init():
    sns.heatmap(np.zeros((10, 10)), vmax=.8, square=True, cbar=False)


def animate(i):
    data = data_list[i]
    sns.heatmap(data, vmax=.8, square=True, cbar=False)


data_list = []
for j in range(20):
    data = np.random.rand(10, 10)
    data_list.append(data)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=20, repeat=False)

# savefile = r"test3.gif"
# pillowwriter = animation.PillowWriter(fps=20)
# anim.save(savefile, writer=pillowwriter)

plt.show()
