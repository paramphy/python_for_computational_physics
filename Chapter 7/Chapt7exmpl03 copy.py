import sys
from random import randint  # randint(a, b) picks a random integer in
# the range(a, b), inclusive.
from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import *

# Allow animation
# Defined droplet coordinates(all droplets) to be at point 100, 100.
atoms = np.ones([400, 2]) * 100
grid = np.zeros([400,2])
probablity = np.zeros([400,1])

    

#print(grid)
# show initial configuration
fig, ax = plt.subplots()
ax.set_xlabel("Position along X axis")
ax.set_ylabel("Position along Y axis")
ax.set_title("Diffusion of particles")  # Add a title to the axes.
ax.plot(grid[:,0], grid[:,1])

(ln,) = plt.plot(atoms[:, 0], atoms[:, 1], "ro")


def init():
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 200)
    return (ln,)


def update(frame):
    # How many steps to take
    N = int(frame)
    for i in range(N):
        # Go through all atoms
        for j in range(400):
            # Move each atom ( or not) in the x and / or y direction.
            atoms[j, 0] += randint(-1, 1)
            atoms[j, 1] += randint(-1, 1)
            # Check for boundary collision
            x, y = (atoms[j, 0], atoms[j, 1])
            if x == 200:
                atoms[j, 0] = 198

            elif x == 0:
                atoms[j, 0] = 2
            if y == 200:
                atoms[j, 1] = 198
            elif y == 0:
                atoms[j, 1] = 2
        #print(atoms)
        for j in range(0,400,10):
            if j-5<=atoms[j,0]<=j+5 and j-5<=atoms[j,1]<=j+5:
                probablity[j] = 1
            else:
                probablity[j] = 0    
            print(probablity)
            
    ln.set_data(atoms[:, 0], atoms[:, 1])
    #ln.set_data(np.linspace(0,400,40), probablity)
    return (ln,)


# See how things look now .
ani = FuncAnimation(
    fig, update, frames=np.linspace(0, 200, 500), init_func=init, blit=True
)
f = r"Chapter 7\diffusion.gif"
writergif = animation.PillowWriter(fps=60)
#ani.save(
#    f,
#    writer=writergif,
#    progress_callback=lambda i, n: print(f"Saving frame {i} of {n}"),
#)
plt.show()
