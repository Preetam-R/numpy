#zeros
import numpy as np
print("zeros matrix")
ar_zro = np.zeros(4) #this creates the array of zeros of 1 dimension
print(ar_zro) #note that the data type is float
print()
#we can also change the dimension or the array like
zero = np.zeros((3,4)) #3 is rows and 4 is coloumn
print(zero) #this is 2D array

#to change the data type of the zeros just give ",dtpye = int"

#-----------------------------------------------------------------------------------------------------------#
print()
print("ones matrix")
#ones 
ones = np.ones(5,dtype = int)
print(ones)

print()
ones1 = np.ones((4,4),dtype = int)
print(ones1)
print()
#-----------------------------------------------------------------------------------------------------------#

#identity matrix
print("identity matrix")
idn = np.eye(4)
print(idn)
print()
#-----------------------------------------------------------------------------------------------------------#
print("linspace") #this creates certain space in array like 
lin = np.linspace(0,20,num = 5,dtype = int) 
print(lin) #output is [ 0  5 10 15 20]