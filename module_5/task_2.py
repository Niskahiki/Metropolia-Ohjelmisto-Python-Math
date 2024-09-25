import numpy as np

A = np.array([[1, 2, 3],
              [1, 0, -2]])
B = np.array([[1],
              [4],
              [2]])
C = np.array([1, 0, 2])

tasks = [
    (A, B),
    (B, A),
    (A, C),
    (C, A),
    (B, C),
    (C, B)]

for task in tasks:
    try:
        result = np.dot(task[0], task[1])
        print(f"{task[0]}\nja\n{task[1]} tulos on:\n{result}")
    except ValueError:
        print(f"{task[0]}\nja\n{task[1]} tulosta ei pysty laskemaan.")

    print()
