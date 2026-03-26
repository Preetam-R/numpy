import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Matrix multiplication
C = np.dot(A, B)          # or A @ B

# Transpose
C_T = C.T

print("A @ B =\n", C)
print("\nTranspose =\n", C_T)
