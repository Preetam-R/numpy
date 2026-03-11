#Given arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), get:

# The first 5 elements

# The last 3 elements

# Every second element

import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("original array\n",arr)
print("\nthe first five elements.")
print(arr[0:5])
print("\nlast three elements")
print(arr[-3:])
print("\nevery second elements")
print(arr[0::2])
