import numpy as np
import matplotlib.pyplot as plt

a = -0.0063
b = 0.55

x = np.linspace(0, 88)
y = a * x**2 + b * x

plt.plot(x, y)

plt.show()