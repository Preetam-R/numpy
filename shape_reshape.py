#shape
import numpy as np
arr = np.array([
    [1,2],[1,2]
])
print(arr)
print()
print(arr.shape)   #this tells you no. of rows and coloumn in array (row,coloumn)
print()

#to convert it into 1D array into multi-D array 
arr1 = np.array([1,2,3,4,5],ndmin=5)
print(arr1)
print()

#reshape
#using reshape we can change the shape of the existing matrix
arry = np.arange(0,12)
print(arry)
print()
arry = arry.reshape(3,4)  #like change to (3,4)
print(arry)

print()
x1 = np.arange(1,13)
print(x1)
print()
x1 = x1.reshape(2,3,2)
print(x1)