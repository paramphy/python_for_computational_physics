from matplotlib import pyplot as plt
import numpy as np

g = -10
h = 0
t = np.linspace(0, 10, 100)
v = 100 + g*t
s = h + v*t
g1 = g+np.zeros(100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots(3, 1, sharey=True)  # Create a figure and an axes.
ax[0].plot(t, g1)
ax[1].plot(t, v)  # Plot some data on the axes.
ax[2].plot(t, s)
ax[0].set_xlabel('Time')  # Add an x-label to the axes.
ax[1].set_xlabel('Time')  # Add an x-label to the axes.
ax[2].set_xlabel('Time')  # Add an x-label to the axes.
ax[0].set_ylabel('Acceleration (m/s2')  # Add a y-label to the axes.
ax[1].set_ylabel('Velocity (m/s)')  # Add a y-label to the axes.
ax[2].set_ylabel('Position (m)')  # Add a y-label to the axes.
fig.suptitle('Chapter 0 Problem 05')
#ax.set_title("Chapter 0 Problem 05")  # Add a title to the axes.
#ax.legend()  # Add a legend.
plt.show()