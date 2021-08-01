#Calculate ∫π-0 sin(x) dx using Monte Carlo techniques. Report your
#uncertainty in the result, and compare with the known result.

from random import random
from math import *

def function(x):
    y = sin(x)
    return(y)

# Since the radius is 1, we can leave it out of most calculations.
N = 1000000  # number of random points in unit cube
count = 0  # number of points with in sphere

for j in range(N):
    point =[ pi*random(), random()]
    if point[1] - sin(point[0]) < 0:
        count = count + 1

print(count)
Answer = float(count) / float(N)
# Make sure to use float, otherwise the answer comes out zero!
# Also note that in this case the volume of our ” known ” volume(the unit
# cube) is 1 so multiplying by that volume was easy.
Answer = pi*Answer  # Actual volume is 4 x our test volume.
print(
    "The volume of a hemisphere of radius 1 is ", Answer, "+/−", 4 * sqrt(N) / float(N)
)
