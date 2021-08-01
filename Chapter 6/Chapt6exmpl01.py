from random import random
from math import sqrt

# Since the radius is 1, we can leave it out of most calculations.
N = 1000000  # number of random points in unit cube
count = 0  # number of points with in sphere
for j in range(N):
    point = (random(), random(), random())
    if point[0] * point[0] + point[1] * point[1] + point[2] * point[2] < 1:
        count = count + 1
Answer = float(count) / float(N)
# Make sure to use float, otherwise the answer comes out zero!
# Also note that in this case the volume of our ” known ” volume(the unit
# cube) is 1 so multiplying by that volume was easy.
Answer = Answer * 4  # Actual volume is 4 x our test volume.
print(
    "The volume of a hemisphere of radius 1 is ", Answer, "+/−", 4 * sqrt(N) / float(N)
)
