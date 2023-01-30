

# SHAPE



#array is one diamentional then get the size of the array

import numpy as np

arr=np.array([1,2,4,6])
print(arr.shape)   #(4,)


arr=np.array([[1,2,4,6],[1,3,5,6]])
print(arr.shape)    #  (2,4)





# SIZE

arr=np.array([[1,2,4,6],[1,3,5,6]])
print(arr.size)    # total number of elements 4*2



# DTYPE

print(arr.dtype)