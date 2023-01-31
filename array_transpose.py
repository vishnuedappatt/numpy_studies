import numpy as np


array=np.arange(1,11).reshape(2,5)
print(array)


array_t=np.transpose(array)
print(array_t)


print("----------------------------------")


array=np.arange(1,25).reshape(4,2,3)
print(array)

print("----------------------------------")


array_t=np.transpose(array)
print(array_t)



print("----------------------------------")

array=np.arange(1,11).reshape(2,5)
print(array)


array_t=np.transpose(array,(1,0))
print(array_t)


