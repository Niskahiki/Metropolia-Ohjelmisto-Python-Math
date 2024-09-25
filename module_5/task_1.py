import numpy as np

a_A = np.array([[1, 2],
                [3, 1]])
a_B = np.array([[0, 1, 3],
                [2, -3, 5]])

print(f"a): {np.dot(a_A, a_B)}")

b_A = np.array([[1, 3, 5],
                [0, -2, 1],
                [2, -1, 4]])
b_B = np.array([[1],
                [-3],
                [-1]])

print(f"b): {np.dot(b_A, b_B)}")

c_A = np.array([[2, 0, 1],
                [1, -3, 4],
                [0, 1, 5]])
c_B = np.array([[3],
                [-5],
                [7]])

print(f"c): {np.dot(c_A, c_B)}")

d_A = np.array([[1, -4, 2],
                [3, 0, -2],
                [2, 1, 0]])
d_B = np.array([[5, 1, -1],
                [-2, 1, 3],
                [0, 3, 4]])

print(f"d): {np.dot(d_A, d_B)}")
