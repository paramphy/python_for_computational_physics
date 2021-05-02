# The file Ba137.txt contains two columns.  The first is counts from a
# Geiger counter, the second is time in seconds.
# (a)  Make a useful graph of this data.
# (b)  If this data follows an exponential curve, then plotting the
#  naturallog of the data (or plotting the raw data on a logrithmic scale)
#  willresult in a straight line.  Determine whether this is the case,
#  andexplain your conclusion with —you guessed it— an appropriategraph.

from matplotlib import pyplot as plt
import numpy as np

N = []
t = []

with open("Chapter 0\Ba137.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        N.append(float(word[0]))
        t.append(float(word[1]))

N = np.array(N)
t = np.array(t)
logN = np.log(N)
# N_theoratical =

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(t, logN, label="Data")  # Plot some data on the axes.

ax.set_xlabel("Time")  # Add an x-label to the axes.
ax.set_ylabel("N")  # Add a y-label to the axes.
ax.set_title("Chapter 0 Problem 03")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
