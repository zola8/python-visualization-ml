import matplotlib.pyplot as plt
import numpy as np


def scatter_3d():
    ax = plt.axes(projection='3d')
    x = np.random.random(100)
    y = np.random.random(100)
    z = np.random.random(100)
    ax.scatter(x, y, z)
    ax.set_title("3D scatter plot")
    plt.show()


def line_3d():
    ax = plt.axes(projection='3d')
    x = np.arange(0, 50, 0.1)
    # y = np.sin(x)
    y = np.arange(0, 50, 0.1)
    z = np.cos(x)
    ax.plot(x, y, z)
    plt.show()


def surface_plot():
    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)
    X, Y = np.meshgrid(x, y)

    # R = np.sqrt(X ** 2 + Y ** 2)
    # Z = np.sin(R)
    Z = np.sin(X) * np.cos(Y)

    # Plot the surface
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap="Spectral")

    plt.show()


if __name__ == '__main__':
    # scatter_3d()
    # line_3d()
    surface_plot()
