#The data shown in figure 2 is most usefully analyzed by looking
#  at theratioof the two microphone signals.  Plot this ratio, 
#  with frequencyon thexaxis.  Be sure to clean up the graph with
#  appropriate scales,axes labels, and a title.
from matplotlib import pyplot as plt
import numpy as np

file = open('Chapter 0\microphones.txt','r')

f = []
m1 = []
m2 = []

with open('Chapter 0\microphones.txt','r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        f.append(float(word[0]))
        m1.append(float(word[1]))
        m2.append(float(word[2]))

frequecy = np.array(f)
mic1 = np.array(m1)
mic2 = np.array(m2)
ratio = mic2/mic1

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(frequecy, mic1, label='Microphone 1')  # Plot some data on the axes.
ax.plot(frequecy, mic2, label='Microphone 2')  # Plot more data on the axes...
ax.plot(frequecy,ratio, label='Ratio')
ax.set_xlabel('Frequency (Hz)')  # Add an x-label to the axes.
ax.set_ylabel('Amplitude (arbitrary units)’)')  # Add a y-label to the axes.
ax.set_title("Chapter 0 Problem 01")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()