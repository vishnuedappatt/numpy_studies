import numpy as np


array=np.array([1,3,5,6])
print(array)
print(type(array))

print('----------------------------------')
list=[1,0,3,5]
array=np.array(list)
print(array)
print(type(array))

print('----------------------------------')

# creating 0 diamention array
array_d0=np.array(12)
print(array_d0)

print('----------------------------------')
# creating 1 diamention array
array_d1=np.array([1,3,5,6])
print(array_d1)

print('----------------------------------')


print('----------------------------------')
# creating 2 diamention array
array_d2=np.array([[1,3,5,6],[2,4,6,8]])
print(array_d2) 
                # [[1 3 5 6]
                #  [2 4 6 8]]


print('----------------------------------')


print('----------------------------------')
# creating 3 diamention array
array_d3=np.array([ [ [1,3,5,6],[2,4,6,8] ] ,[ [1,3,5,6],[2,4,6,8] ] ])
print(array_d3)     
                     #[[[1 3 5 6]
                        # [2 4 6 8]]

                        # [[1 3 5 6]
                        # [2 4 6 8]]]
 
print('----------------------------------')



# to check how much diamentions array is this using ndim 
print(array_d0.ndim)    #1
print(array_d1.ndim)    #2
print(array_d2.ndim)    #3
print(array_d3.ndim)    #4

print('----------------------------------')



# we can also create what diamention we want it using ndmin argument in an array

array_d=np.array([1,3,5,6],ndmin=5)
print(array_d)    #[[[[[1 3 5 6]]]]]
print(array_d.ndim)   #5







