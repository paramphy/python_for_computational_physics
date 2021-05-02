# A ball is thrown upwards with initial velocity vo= 5m/s and
# an initial height yo =  3  m.   Write  a  Python  program
# to  plot  y(t)  from t=  0 until the ball hits the ground

import numpy as np
from scipy.optimize import brentq


def func(t, y0=3, v0=5, g=-10):

    y = y0 + v0 * t + 0.5 * g * t ** 2

    return y


root = brentq(func, 0, 10)

print(root)

t = np.linspace(0, root, 1000)

y = func(t)

print(y)
