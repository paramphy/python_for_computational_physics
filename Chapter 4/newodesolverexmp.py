from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 10, 1000)


def lotkavolterra(t, z, a, b, c, d):

    x, y = z

    return [a * x - b * x * y, -c * y + d * x * y]


sol = solve_ivp(lotkavolterra, [0, 15], [10, 5], args=(1.5, 1, 3, 1), dense_output=True)

t = np.linspace(0, 15, 300)

z = sol.sol(t)

plt.plot(t, z.T)

plt.xlabel("t")

plt.legend(["x", "y"], shadow=True)

plt.title("Lotka-Volterra System")

plt.show()
