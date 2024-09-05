import numpy as np

rng = np.random.default_rng()

rng_array = rng.integers(low=10, size=20)  # Randomised integer array

sorted_rng_array = np.sort(rng_array)

print(sorted_rng_array.reshape(4, 5))
