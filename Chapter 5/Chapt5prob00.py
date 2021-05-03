from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint

N = 10000  # number of steps to take


alpha = 1
beta = -1
gama = 0.3
delta = 0.2
omega = 1

state = np.zeros([2])

state[0] = 0
state[1] = 1

time = np.linspace(0, 100, N)


def pendulum(state, time):

    # Differential equation for an undamped pendulum.
    # state[0] should be angular position, state[1]
    # should be angular velocity.

    g0 = state[1]
    g1 = (
        -delta * state[1]
        - beta * state[0]
        - alpha * state[0] ** 3
        + gama * np.cos(omega * time)
    )

    return np.array([g0, g1])


answer = odeint(pendulum, state, time)

fig, ax = plt.subplots()  # Create a figure and an axes.
# ax.plot(time, answer[:, 0], label="Data")  # Plot some data on the axes.
ax.plot(answer[:, 0], answer[:, 1], label="Data")  # Plot some data on the axes.
ax.set_xlabel("Angle")  # Add an x-label to the axes.
ax.set_ylabel("Angular Velocity")  # Add a y-label to the axes.
ax.set_title("Duffing oscillator")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
