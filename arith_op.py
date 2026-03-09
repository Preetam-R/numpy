#arithmatic opertaions
#addition
import numpy as np
v1 = np.random.randint(1,20,6)
print(v1)

v1 = v1 + 3
print(v1)
print("\nadding 2 arrays")

#adding to arrays
x1 = np.random.randint(1,20,6)
print(x1)
print()
x2 = np.random.randint(1,20,6)
print(x2)
print()
add = x1 + x2
print(add)

#we have predefined functions too in this
Add = np.add(x1,x2)
print(Add)

#subtract
sub = np.subtract(x1,x2)
print("\nsubtaction\n:",sub)

multi = np.multiply(x1,x2)
print("\nmultiplication:\n",multi)

div = np.divide(x1,x2)
print("\ndivision:\n",div)

#mod
mod = np.mod(x1,x2)
print("\nmodulus:\n",mod)

#you can also do power and reciprocal too
#using np.power(x1,x2)| np.reciprocal(x1,x2)

#we also have
# ➤ np.min(x)

# ➤ np.max(x)

# ➤ np.argmin(x)   np.argmax(x) --->  this gives the index of the min and max numbers present in the array  axis 0 - col| 1 means row 

# np.sqrt(x)

# ➤ np.sin(x)

# np.cos(x)

# np.cumsum(x)



