# The “volume” of a 2-sphere x2 + y2 = r2 (AKA a “circle”) is (1)πr2.
# The volume of a 3-sphere x2 + y2 + z2 = r2 is (4/3)πr3. The equation
# for a 4-sphere is x2 + y2 + z2 + w2 = r2. We can guess, by extrapolation
# from the 2-dimensional and 3-dimensional cases, that the “volume” of
# a 4-sphere is απr4. Use Monte Carlo integration to estimate α.

from random import uniform
from math import *
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def function(x):
    y = sin(x)
    return y


# Since the radius is 1, we can leave it out of most calculations.
N = 1000000  # number of random points in unit cube

count = 0

for j in range(N):

    point = [uniform(-1, 1), uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)]

    if (
        point[0] * point[0]
        + point[1] * point[1]
        + point[2] * point[2]
        + point[3] * point[3]
        < 1
    ):
        count = count + 1

print(count)
Answer = 2 ** len(point) * float(count) / float(N)

# Make sure to use float, otherwise the answer comes out zero!
# Also note that in this case the volume of our ” known ” volume(the unit
# cube) is 1 so multiplying by that volume was easy.


alpha = Answer / pi

print("The value of alpha:", alpha, "+/−", 4 * sqrt(N) / float(N))
