import numpy as np
import matplotlib.pyplot as plt

x = [(-5, 0), (0, 4), (4, 8), (8, 10)]
y = [(0, 3), (3, 3), (3, 0), (0, 1)]

for i in range(len(x)):
    current_x = np.linspace(x[i][0], x[i][1])
    current_y = np.linspace(y[i][0], y[i][1])

    plt.plot(current_x, current_y, color='blue')

ax = plt.subplot()
# Align the y and x spines at 0
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# Hide top and right lines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

plt.show()