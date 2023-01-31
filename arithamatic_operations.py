import numpy as np

array=np.array([1,2,4,5,6,7])
print(array)

print(array+2)   # adding 2 to all element

print(array*2)    # multiply 2 to all elements

print(array/10)    #divide 10 by all elements

print(array ** 2)

print(array % 2)

array[2]=10
print(array)



array1=np.array([1,2,3])
array2=np.array([2,2,2])
print(array1+array2)




array3=array.reshape(3,2)
print(array3)
# print(array3+array2)

print("----------------------------")
print(array3.size)

a=np.resize(array3,(2,3))
print(a)



print(array3.resize((2,3)))


array_t=np.array([1,3,5,6])
a_b=array_t.resize(5)
print(array_t.size)


