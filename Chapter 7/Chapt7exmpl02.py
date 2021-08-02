from random import choice
from scipy.optimize import curve_fit
import numpy as np
from math import *
from matplotlib import pyplot as plt

def power ( x , a , b ) :
    return a*x**b

steps = 200 # number of steps
boys = 2000 # number of frat boys
# setup storage space
x = np.zeros(steps)
t = np.arange(steps)
xsum = np.zeros(steps)
x2sum = np.zeros(steps)
# Do the walks
for j in range(boys):
    for i in range(1, steps):
        if choice([0 , 1]) == 1:
            x[i] = x[i-1] - 1
        else:
            x[i] = x[i-1] + 1
# add x , xˆ2 to running sums
    for i in range(steps):
        xsum[i] = xsum[i] + x[i]
        x2sum[i] = x2sum[i] + x[i]**2
# rescale averages
xavg = [float(i)/float(boys) for i in xsum]
RMS = [sqrt(float(i)/float(boys)) for i in x2sum]
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.set_xlabel( "Time ( Step number ) " )
ax.set_ylabel( "Average and RMS position(Steps)" )
ax.plot(t , xavg )
ax.plot(t ,RMS)
# Check least−square s fit , see what the power dependenceis.
# I assume that the RMS displacement goes as D = A∗tˆB
popt , pcov = curve_fit(power, t, RMS)
print ("Power fit: y ( t ) = A ∗ t ˆB : ")
print ('A =',popt[0],'+/-',sqrt(pcov[0,0]))
print ('B =',popt[1],'+/-',sqrt(pcov[1,1]))
# Plot the curve fit on top of that last graph
ax.plot(t , power(t , popt[0], popt[1]))
plt.show()