import numpy as np
import matplotlib.pyplot as plt

a = 1
b = -4
c = 3

x = np.linspace(-2, 6)
y = a * x**2 + b * x + c

plt.plot(x, y)

plt.show()