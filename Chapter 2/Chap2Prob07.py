from scipy.misc import derivative
import numpy as np
from matplotlib import pyplot as plt
import math


def func(x):

    y = math.sin(x)
    
    return(y)

def differ(x):

    y = derivative(func,x)

    return(y)



x = np.linspace(0,50,1000)
y = np.sin(x)
dydx = []

for i in x:
    f = derivative(func, i)
    dydx.append(f)

dydx = np.array(dydx)

print(x, y)

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y, label = 'f(x)')  # Plot some data on the axes.
ax.plot(x, dydx, label='df/dx')  # Plot more data on the axes...
ax.set_xlabel('x')  # Add an x-label to the axes.
ax.set_ylabel('y')  # Add a y-label to the axes.
ax.set_title("Chapter 0 Problem 00")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()