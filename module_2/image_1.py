from matplotlib import pyplot as plt, patches
import numpy as np

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move x-axis and y-axis to centre from the sides
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Remove upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Shows whole circle. (The axes are now centered)
ax.axis('equal')

# Remove y-axis values between 1.00 and -1.00 from the circle axes
plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

degrees = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
colors = np.array(['red', 'green', 'blue', 'orange', 'red', 'green', 'blue', 'orange', 'red', 'green'])

# Convert degrees to radians
radians = np.deg2rad(degrees)

# Count x and y positions with cos and sin
x = np.cos(radians)
y = np.sin(radians)

# Draw dots on the circle
plt.scatter(x, y, color=colors, marker='X')

# Descriptive text for dots
text = [r'30°', r'45°', r'60°', r'90°', r'120°', r'135°', r'150°', r'180°', r'270°', r'360°']


# Draw descriptive text for dots
for i in range(len(degrees)):
    plt.annotate(text[i],
                 xy=(x[i], y[i]),
                 xycoords='data',
                 xytext=(+30, +5),
                 textcoords='offset points',
                 fontsize=12,
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))


plt.show()
