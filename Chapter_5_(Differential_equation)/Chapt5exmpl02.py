from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint

N = 10000  # number of steps to take

gravity = 9.8
length = 9.8
beta = 0.5
A = 1.5
omega = 0.9


state = np.zeros([2])

state[0] = 0
state[1] = 1

time = np.linspace(0, 500, N)


def pendulum(state, time):

    # Differential equation for an undamped pendulum.
    # state[0] should be angular position, state[1]
    # should be angular velocity.

    g0 = state[1]
    g1 = (
        -gravity / length * np.sin(state[0])
        - beta * state[1]
        + A * np.cos(omega * time)
    )

    return np.array([g0, g1])


answer = odeint(pendulum, state, time)

fig, ax = plt.subplots()  # Create a figure and an axes.
# ax.plot(time, answer[:, 0], label="Data")  # Plot some data on the axes.
ax.plot(answer[:, 0], answer[:, 1], label="Data")  # Plot some data on the axes.
ax.set_xlabel("Time")  # Add an x-label to the axes.
ax.set_ylabel("Angle")  # Add a y-label to the axes.
ax.set_title("Damped Forced Pendulum")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
