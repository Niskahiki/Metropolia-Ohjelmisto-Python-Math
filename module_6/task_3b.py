import numpy as np
import matplotlib.pyplot as plt

a = -1.5
b = -3
c = 7

x = np.linspace(-4, 2)
y = a * x**2 + b * x + c

plt.plot(x, y)

ax = plt.subplot()
# Align the y and x spines at 0
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# Hide top and right lines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

plt.show()