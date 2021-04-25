import numpy as np

t = np.linspace(0, 50, 100)
yi = 10
vi = 5
yi = yi + np.zeros(100)
vi = vi + np.zeros(100)
g = -10
yt = yi + vi*t + 0.5*g*t**2
print(t, yt)