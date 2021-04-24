from matplotlib import pyplot as plt
import numpy as np

N = []
t = []

with open('Chapter 0\Ba137.txt','r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        N.append(float(word[0]))
        t.append(float(word[1]))

N = np.array(N)
t = np.array(t)
logN = np.log(N)
N0 = 30000
lamda = 0.00425
N_theoratical = N0*np.exp(-lamda*t) 

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(t, N, label='Experimental')  # Plot some data on the axes.
ax.plot(t, N_theoratical, label='Theoratical')
ax.set_xlabel('Time')  # Add an x-label to the axes.
ax.set_ylabel('N')  # Add a y-label to the axes.
ax.set_title("Chapter 0 Problem 03")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()