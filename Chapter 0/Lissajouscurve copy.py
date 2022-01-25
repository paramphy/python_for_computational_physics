import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("seaborn-pastel")


def funcx(t, a, b):

    x = (a - b) * np.cos(t) + b * np.cos((t * a / b) - 1)
    return x


def funcy(t, a, b):

    x = (a - b) * np.sin(t) - b * np.sin((t * a / b) - 1)
    return x


fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
(line,) = ax.plot([], [], lw=3)
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Lissajouscurve")  # Add a title to the axes.


def init():
    line.set_data([], [])
    return (line,)


def animate(i):
    a = 1.00
    b = float(i) / 200.00 * a
    t = np.linspace(-10, 11, 1000)
    x = funcx(t, a, b)
    y = funcy(t, a, b)
    line.set_data(x, y)
    return (line,)


anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=5, blit=True)

anim.save("lissajouscurvefor" + "wa=" + "wb=" + ".gif", writer="imagemagick")
