import numpy as np


array=np.arange(1,7)
array1=np.zeros(6)
print(array1)
array_out=np.concatenate((array1,array))

p_out=np.zeros(12)
array_out=np.concatenate((array1,array),out=p_out)
print(p_out)
print(array_out)