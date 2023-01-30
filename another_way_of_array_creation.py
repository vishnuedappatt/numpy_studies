import numpy as np

# ARANGE 

arr=np.arange(1,10)
print(arr)

arr=np.arange(1,10,2)
print(arr)

arr=np.arange(10,dtype="f")
print(arr)



# ZEROs

arr=np.zeros([3,3],dtype="i")
print(arr)


arr=np.zeros([4,3],dtype="i")     # row 4 column 3    get all values as zeros
print(arr)




# ONES     
# default type is float


arr=np.ones([3,4])     # row 3 column 4    get all values as ones
print(arr)


arr=np.ones([3,4],dtype='i')     # row 3 column 4    get all values as ones
print(arr)



# LINSPACE 

print(help(np.linspace))