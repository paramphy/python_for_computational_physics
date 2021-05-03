# Program to plot the motion of a ”spring y pendulum ” .

from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint

N = 1000  # number of steps to take

# We actually have FOUR parameters to track, here :
# L , Ldot , theta, and thetadot .
# So instead of the usual Nx2 array , make it Nx4.
# Each 4−element row will be used for the state of
# the system at one instant, and each instant is
# separated by time dt. I’ll use the order given above.

y = np.zeros([4])
Lo = 1.0  #unstretched spring length
L = 1.0  # Initial stretch of spring
vo = 0.0  #initial velocity
thetao = 0.3  # radians
omegao = 0.0  #initial angular velocity
y[0] = L  # setinitial state
y[1] = vo
y[2] = thetao
y[3] = omegao
time = np.linspace(0, 25, N)

k = 3.5  # spring constant , in N/m
m = 0.2  # mass , in kg
gravity = 9.8  # g , in m/sˆ2


def springpendulum(y, time):

    # This defines the set of differential equations
    # we are solving. Note that there are more than
    # just the usual two derivatives!

    g0 = y[1]
    g1 = (Lo + y[0]) * y[3] * y[3] - k / m * y[0] + gravity * np.cos(y[2])
    g2 = y[3]
    g3 = -(gravity * np.sin(y[2]) + 2.0 * y[1] * y[3]) / (Lo + y[0])
    return np.array([g0, g1, g2, g3])


# Now we do the calculations.
answer = odeint(springpendulum, y, time)
# Now graph the results.
# rather than graph in terms of t, I’m going
# to graph the track the mass takes in 2D.
# This will require that I change L, theta data
# to x, y data.
# print(answer)

xdata = (Lo + answer[:, 0]) * np.sin(answer[:, 2])
ydata = -(Lo + answer[:, 0]) * np.cos(answer[:, 2])
# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(xdata, ydata, label="Data")  # Plot some data on the axes.
ax.set_xlabel("Horizontal position")  # Add an x-label to the axes.
ax.set_ylabel("Vertical position")  # Add a y-label to the axes.
ax.set_title("Chapter 4 Problem 00")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
