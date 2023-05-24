import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Slicing
print(arr[1:4])    # Output: [2 3 4]
print(arr[2:])     # Output: [3 4 5]
print(arr[:3])     # Output: [1 2 3]
print(arr[::2])    # Output: [1 3 5]
