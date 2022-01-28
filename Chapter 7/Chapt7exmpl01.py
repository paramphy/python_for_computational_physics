from random import choice
import numpy as np
import matplotlib.pyplot as plt
from math import *

N = 2000  # number of steps
# set up storage space
x = np.zeros(N)
t = np.arange(N)
# Do the walk
for i in range(1, N):
    if choice(["forward", "back"]) == "back":
        # take a step back
        x[i] = x[i - 1] - 1
    else:
        x[i] = x[i - 1] + 1

#RMS = np.array([sqrt(i * i) for i in x])

# syntax for 3-D projection
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(t, x, label="Steps")  # Plot some data on the axes.
#ax.plot(t, RMS, label="RMS")  # Plot more data on the axes...
ax.set_xlabel("t")  # Add an x-label to the axes.
ax.set_ylabel("x")  # Add a y-label to the axes.
ax.set_title("Chapter 7 example 01")  # Add a title to the axes.
ax.legend()  # Add a legend.
ax.vlines(5,-50,10)
plt.show()
