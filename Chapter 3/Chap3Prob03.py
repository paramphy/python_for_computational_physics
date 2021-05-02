import numpy as np
from matplotlib import pyplot as plt


def func(t, y0=10, w=2):

    y = y0 * np.sin(w * t)
    return y


def velocityfunc(t, y0=10, w=2):

    y = w * y0 * np.cos(w * t)
    return y


t = np.linspace(0, 10, 1000)
y = func(t)
v = velocityfunc(t)

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(y, v, label="Phase Diagram")  # Plot some data on the axes.
ax.set_xlabel("y")  # Add an x-label to the axes.
ax.set_ylabel("v")  # Add a y-label to the axes.
ax.set_title("Chapter 3 Problem 03")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
