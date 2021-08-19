import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

def func(time, amplitude, frequency, delta):

    displacement = amplitude*np.sin((frequency*time) + delta)
    return displacement


# ratio = float(input("Ratio between two frequencies: "))
wa = float(input("Frequency of the first wave: "))
wb = float(input("Frequency of the second wave: "))
# delta = float(input("Input the value of delta in multiple of pi: "))
A = 1.00 #float(input("Amplitude for first wave A: "))
B = 1.00 #float(input("Amplitude for first wave B: "))

fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
line, = ax.plot([], [], lw=3)
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Lissajouscurve")  # Add a title to the axes.

def init():
    line.set_data([], [])
    return line,

def animate(i):
    
    t = np.linspace(-np.pi, np.pi, 1000)
    x = func(t, A, wa, i/200*np.pi)
    y = func(t, B, wb, 0)
    line.set_data(x, y)
    return line,
    #print(np.pi, delta*np.pi)

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

anim.save('lissajouscurvefor'+'wa='+str(wa)+'wb='+str(wb)+'.gif', writer='imagemagick')
