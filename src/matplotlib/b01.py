# https://www.youtube.com/watch?v=OZOOLe2imFo

import matplotlib.pyplot as plt
import numpy as np


def scatter_example():
    x_data = np.random.rand(50) * 100
    y_data = np.random.rand(50) * 100
    # 50 points between 0..1 -> 0..100
    print(x_data)
    plt.scatter(x_data, y_data)
    plt.show()


def line_example():
    years = [2020 + x for x in range(10)]
    weights = [80, 83, 84, 86, 82, 81, 79, 84, 85, 88]
    plt.plot(years, weights)
    plt.show()


def bar_example():
    x = ["C++", "Java", "Python", "Ruby", "Scala"]
    y = [100, 340, 630, 80, 25]
    plt.bar(x, y, width=0.5)
    plt.show()


def histogram_example():
    ages = np.random.normal(20, 1.5, 1000)
    # plt.hist(ages, bins=20)
    plt.hist(ages, bins=20, cumulative=True)
    plt.show()


def pie_example():
    labels = ["C++", "Java", "Python", "Ruby", "Scala"]
    values = [100, 340, 630, 80, 25]
    explodes = [0, 0.2, 0, 0, 0]
    plt.pie(values, labels=labels, explode=explodes, autopct='%.1f%%')
    plt.show()


def boxplot_example():
    # heights = np.random.normal(172, 8, 300)
    # plt.boxplot(heights)

    first = np.linspace(0, 10, 25)
    second = np.linspace(10, 200, 25)
    third = np.linspace(200, 210, 25)
    fourth = np.linspace(210, 230, 25)
    fifth = np.linspace(230, 250, 25)
    data = np.concatenate((first, second, third, fourth, fifth))
    plt.boxplot(data)
    plt.show()


def subplots_example():
    x = np.arange(100)
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(x, np.sin(x))
    axs[0, 0].set_title("sin(x)")

    axs[0, 1].plot(x, np.cos(x))
    axs[0, 1].set_title("cos(x)")

    axs[1, 0].plot(x, np.random.random(100))
    axs[1, 0].set_title("random(x)")

    axs[1, 1].plot(x, np.log(x))
    axs[1, 1].set_title("log(x)")

    fig.suptitle("Four Plots")
    fig.tight_layout()
    plt.savefig("four_plot.png", dpi=300, transparent=True, pad_inches=0.2)
    # plt.show()



if __name__ == '__main__':
    # scatter_example()
    # line_example()
    # bar_example()
    # histogram_example()
    # pie_example()
    # boxplot_example()
    subplots_example()

# https://www.youtube.com/watch?v=OZOOLe2imFo
