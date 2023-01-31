import numpy as np

# integer indexing

array=np.array([1,3,5,7,8,9])
print(array)

index=np.array([2,3])
print(array[index])


print(array[[1,2,5]])


print("---------------")
array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)


print(array[[1,2,2,2],[0,1,0,2]])



print("---------------")

# boolean indexing

array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)




print("---------------")

print(array[array>5])


print("---------------")


value=array[array<5]*10
print(value)
print(array[array<5])
