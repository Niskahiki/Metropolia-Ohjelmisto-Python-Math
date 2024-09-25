import numpy as np

A = np.array([[1, 0.5],
              [2, 1]])
B = np.array([[-1, -2],
              [2, 4]])

print(f"AB:\n{np.dot(A, B)}")
print(f"BA:\n{np.dot(B, A)}")
