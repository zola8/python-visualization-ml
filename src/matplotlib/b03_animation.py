# https://www.youtube.com/watch?v=OZOOLe2imFo

import random

import matplotlib.pyplot as plt

head_tails = [0, 0]

for _ in range(100_000):
    head_tails[random.randint(0, 1)] += 1
    plt.bar(["Heads", "Tails"], head_tails, color=["red", "blue"])
    plt.pause(0.01)

plt.show()
