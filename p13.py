# Given arr = np.array([3, 7, 2, 9, 4, 6]), use boolean indexing to:

# Get all elements greater than 5

# Set all elements less than 5 to 0

import numpy as np
arr = np.array([3, 7, 2, 9, 4, 6])

arr = arr[arr>5]
print(arr)

var = arr.copy()
var[var<5]=0



