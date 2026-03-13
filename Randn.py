#randn
#this function generates numbers close to zero
#this may be positive or negative as well
import numpy as np
print("this is for 1D array\n")
var = np.random.randn(5)  #for 1D array
print(var)
print("--"*30)
print("\nthis is for multi-dimension array\n")
var1 = np.random.randn(3,3)  #multi-D array
print(var1)
