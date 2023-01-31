import numpy as np


array=np.arange(1,7)
print(array)


# INSERT

array_insert=np.insert(array,2,30)
print(array_insert)
print(array)



# APPEND
array_insert=np.append(array,30)
print(array_insert,'insert')

print('-------------------------')

array=np.array([[1,2,3],[4,5,6]])
print(array)

print('-------------------------')

array_insert=np.insert(array,2,30,axis=1)  # axis 1 add straight as vertical
print(array_insert)



array_insert=np.insert(array,2,30,axis=0)   # axis zero add down as horizontal
print(array_insert)



# APPEND


array_insert=np.append(array,[[30],[40]],axis=1)  # axis 1 add straight as vertical
print(array_insert,'lst')



