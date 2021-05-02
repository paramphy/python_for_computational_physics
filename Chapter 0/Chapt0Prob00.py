# Graph both of the following functions on a single figure, with
# a usefully-sized scale.
# (a)x4e−2x
# (b)[x2e−xsin(x2)]2
# Make sure your figure has legend, range, title, axis labels, and so on.

# importing matplotlib module
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

ya = x ** 4 * np.exp(-2 * x)
yb = (x ** 2 * np.exp(-x) * np.sin(x ** 2)) ** 2

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, ya, label="(a)")  # Plot some data on the axes.
ax.plot(x, yb, label="(b)")  # Plot more data on the axes...
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Chapter 0 Problem 00")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
