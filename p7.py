# Create a 4×4 array with values from 0 to 15 and:

# Extract the first row

# Extract the last column

# Extract the 2×2 block in the top-left corner​


import numpy as np
arr = np.arange(0,16).reshape(4,4)
print(arr)

print("\nextracting first row.......")
print(arr[0])

print("\nextracting last coloumn.....")
print(arr[:,-1])

print("\nextracting top left corner.....")
print(arr[:2,:2])