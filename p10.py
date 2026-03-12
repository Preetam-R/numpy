# Create an array of 10 random numbers between 0 and 1 and find:

# The maximum value

# The index of the maximum value

# The mean of the array

import numpy as np


arr = np.random.rand(10)
print(arr)


print(f"\nthe maximum:{np.max(arr)}")
print(f"the index of max number is:{np.argmax(arr)}")
print(f"the mean of the array is:{np.mean(arr)}")
