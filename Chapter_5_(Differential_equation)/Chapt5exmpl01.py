from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint

N = 1000  # number of steps to take

gravity = 9.8
length = 9.8
beta = 0.1


state = np.zeros([2])

state[0] = 0
state[1] = 1

time = np.linspace(0, 100, N)


def pendulum(state, time):

    # Differential equation for an damped pendulum.
    # state[0] should be angular position, state[1]
    # should be angular velocity.

    g0 = state[1]
    g1 = -gravity / length * np.sin(state[0]) - beta * state[1]

    return np.array([g0, g1])


answer = odeint(pendulum, state, time)

fig, ax = plt.subplots()  # Create a figure and an axes.
# ax.plot(time, answer[:, 0], label="Data")  # Plot some data on the axes.
ax.plot(
    answer[:, 0], answer[:, 1], label="beta = 0.1, g/l = 1"
)  # Plot some data on the axes.
ax.set_xlabel("Angle")  # Add an x-label to the axes.
ax.set_ylabel("Angular velocity")  # Add a y-label to the axes.
ax.set_title("Damped Pendulum Phase Space")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
