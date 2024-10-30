import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1)
y = np.linspace(4, 4)
x2 = np.linspace(1, 4)
y2 = np.linspace(4, 0)

ax = plt.subplot()
# Align the y and x spines at 0
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# Hide top and right lines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

plt.plot(x, y, color='blue')
plt.plot(x2, y2, color='blue')
plt.show()