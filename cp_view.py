import numpy as np
var = np.array([1,2,3,4])
co = var.copy()
print(var)
print(co)

#view
print(var.view())

#difference between copy and view is 

#copy- it own the original data and create new array 
#view - doesn't owns the data

#copy - changes made in the copy array do not affect the original data 
#view - the changes made in the view array will affect the o9riginal data