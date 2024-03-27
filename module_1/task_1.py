import numpy as np

# Task 1
print("\n-- Task1 --")

a = 2.493

print(np.degrees(a))

b = 0.911

print(np.degrees(b))

# Task 2
print("\n-- Task2 --")

a = 137.7

print(np.radians(a))

b = 62.3

print(np.radians(b))

# Task 3
print("\n-- Task3 --")

degree_list = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for degree in degree_list:
    print(f"{degree}° = {np.radians(degree)}rad")
