# Given two 1D arrays of length 3, stack them:
# Vertically to make a 2×3 array

# Horizontally to make a 3×2 array
import numpy as np
arr = np.random.randint(0,10,6)
print(arr)
print("\nmaking 2X3....")
arr = arr.reshape(2,3)
print(arr)
print("making 3X2.....")
arr = arr.reshape(3,2)
print(arr)


