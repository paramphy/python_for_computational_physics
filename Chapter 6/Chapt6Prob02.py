#Calculate ∫π-0 sin(x) dx using Monte Carlo techniques. Report your
#uncertainty in the result, and compare with the known result.

from random import uniform
from math import *
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def function(x):
    y = sin(x)
    return(y)

# Since the radius is 1, we can leave it out of most calculations.
N = 1000000  # number of random points in unit cube
spherecount = 0  # number of points with in sphere
cylindercount = 0 # number of points within the cylinder
sphere_x = []
sphere_y = []
sphere_z = []
cylinder_x = []
cylinder_y = []
cylinder_z = []


for j in range(N):
    point =[uniform(-1,1), uniform(-1,1), uniform(-1,1)]
    if  point[0]*point[0] + point[1]*point[1] + point[2]*point[2] < 1:
        spherecount = spherecount + 1
        sphere_x.append(point[0])
        sphere_y.append(point[1])
        sphere_z.append(point[2])
        if (point[0]+0.5)*(point[0]+0.5) + point[1]*point[1] < 0.5*0.5:
            cylindercount = cylindercount + 1
            cylinder_x.append(point[0])
            cylinder_y.append(point[1])
            cylinder_z.append(point[2])

sphere_x = np.array(sphere_x)
sphere_y = np.array(sphere_y)
sphere_z = np.array(sphere_z)
cylinder_x = np.array(cylinder_x)
cylinder_y = np.array(cylinder_y)
cylinder_z = np.array(cylinder_z)

fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')

#ax.scatter(sphere_x, sphere_y, sphere_z, c = sphere_z)
#ax.scatter(cylinder_x, cylinder_y, cylinder_z, c=cylinder_z)
#ax.set_title('3D surface of volume of interest')
#plt.show()





Answer = float(cylindercount)/ float(N)
# Make sure to use float, otherwise the answer comes out zero!
# Also note that in this case the volume of our ” known ” volume(the unit
# cube) is 1 so multiplying by that volume was easy.

print(
    "The volume of the region is ", Answer, "+/−", 4 * sqrt(N) / float(N)
)
