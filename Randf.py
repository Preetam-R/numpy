#ranf()
#this allows you to generate the random value which is specified with shape and value 
#this will generate float value------- where the element which is specified is not included eg.[0.0,1.0)

import numpy as np
v1 = np.random.ranf(10) #this doesn't give you multi-dimension array 

print(v1)


#randint
#this gives the range of random intger value 
var = np.random.randint(0,10,6)  #0-specifies starting value    10-specifies ending value which is not included  6-specifies total number of elements
print(var)