#Solve this system of equations for a through f.
# a/5 +b+c+d−e−f=   24.1312
# a+c−d+ 5e+f=   46.2798
# −a−3b+ 2c−d−e−f=−61.83725
# b−c+d+ 2e=   31.1466
# a−2b+ 3c+d/2   =   51.2106
# a/2−2b−2c−d+e−6f=−5.7008
from pylab import *
import numpy as np
from scipy.linalg import solve

M = np.array([[1/5, 1, 1, 1 ,-1, -1], 
    [1, 0, 1, -1, 5, 1],
    [-1, -3, 2, -1, -1, -1],
    [0, 5, -1, 1, 2, 0],
    [1,-2, 3, 1/2, 0, 0],
    [1/2, -2, -2, -1, 1, -6]])

b = np.array([24.1312, 46.2798, -61.8372, 31.1466, 51.2106, -5.7008])

x = solve(M, b)
print(M, b)
print(x)