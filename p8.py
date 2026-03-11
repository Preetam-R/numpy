# Given a = np.array([1, 2, 3]) and b = np.array([4, 5, 6]), compute:

# Element-wise sum

# Element-wise product

# Element-wise square of a​

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a)
print(b)

print("\n----OPERTAIONS----\n")
print("\nElement wise sum")
print(a+b)
print(np.add(a,b))

print("\nelement wise product")
print(a*b)
print(np.multiply(a,b))

print("\nelement wise square of a")
print(a**2)
print(np.square(a))
