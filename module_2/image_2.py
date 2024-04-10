import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi*3, np.pi*3, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, color='purple', linestyle=':')
plt.plot(X, S, color='cyan', linestyle='--')

plt.legend(('cos', 'sin'))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sini ja kosini funktiot')

plt.xticks([-3*np.pi, -5*np.pi/2, -2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi],
           [r'$-3\pi$', r'$-\frac{5\pi}{2}$', r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$',
            '0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$', r'$\frac{5\pi}{2}$', r'$3\pi$'])

plt.yticks([-1, -0.5, 0, 0.5, 1], [r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$'])

plt.show()
