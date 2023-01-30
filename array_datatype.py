import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)    # int64


arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype) 

# define the type 

arr = np.array([1, 2, 3, 4], dtype='S')

print(type(arr[3]))
print(arr)
print(arr.dtype)



# using dtype we can convert the type into another type but in some case like string is convert to int then error comes there is another way


arr = np.array(['11', '21', '31'])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)



newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)