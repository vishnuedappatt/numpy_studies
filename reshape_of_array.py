import numpy as np


# created a 1D array is converted to 3D array using  reshap


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.shape)

newarr = arr.reshape(4, 3)

print(newarr.shape)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2,2,3)

print(newarr)