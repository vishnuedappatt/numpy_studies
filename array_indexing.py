import numpy as np


# for 1D array

arr = np.array([1, 2, 3, 4])
print(arr[0])    #1
print(arr[2] + arr[3])  #  3+4=7
print(arr[-1])  # negative index 
print("------------------------------------")

# for 2D array
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0,3])     # 1st take ist row 3 column value    = 4
print(arr[1,3])     # 2nd take ist row 3 column value    = 9
print(arr[0,-1])    # negative indexing 1 st row last column
print(arr[-1,-1])   # negative indexing last row last column
print(arr[-2,0])    # first row and column
print(arr[0,1]+arr[1,4])     # 1st take ist row 1 column value adding with 2nd row  4 th column value *  2+10=12  *


print("------------------------------------")

# for 3D array   combinations of 2d array

arr = np.array([  [[1, 2, 3], [4, 5, 6]]  , [[7, 8, 9], [10, 11, 12]] ])

print(arr[0, 0, 2])      
print(arr[1, 1, 2])   
print(arr[-1,-2,-3])

