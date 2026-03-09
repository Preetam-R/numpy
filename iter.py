import numpy as np
arr = np.random.randint(1,20,15)
print(arr)
print()
for i in arr:
    print(i)

arr = arr.reshape(5,3)
print(arr)
print()
for i in arr:
    print(i)  #this iterates the whole row

#if you want to iterate through every element 
#then use nested for loop

for j in arr:
    for k in j:
        print(k)

#Note: for loop will be equivalent to the number of dimensions


#to over come this all we have on function/method 
#np.nditer(arr) in for loop
print()
for i in np.nditer(arr):
    print(i)

#while dealing with more data in iteration we may not know their indexes so
#for that we have use ndenumerate(arr) in for loop

print()
for i,d in np.ndenumerate(arr):
    print(i,d)