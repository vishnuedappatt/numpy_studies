import numpy as np


# for 1D array

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])  # print 1 column to 5 column

print(arr[4:])   # to print 4 column to end


print(arr[:4])   # get till 4 th column

print(arr[-3:-1])   #negative indexing

print(arr[1:6:2])    # indexing with step slicing between 1-6 column with a step of 2 




print('(-------------------------------------)')


# for 2D array


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])   # second row 1:4 indexing


print(arr[0:2, 2])    # first arguments how much rows we needed and second is what value we want
print(arr[1,2])

print(arr[0:2, 1:3])   # 0:2 row 1:3 column




