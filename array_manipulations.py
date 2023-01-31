import numpy as np


# CONVERT TO 1D ARRAY

# USING FLATTEN


array=np.array([[1,2,4],[1,3,6]])
print(array)

array_sample=array.flatten()
print(array_sample)



array_sample=array.flatten(order="K")  #ROW WISE
print(array_sample)


array_sample=array.flatten(order="F")    # COLUMN WISE
print(array_sample)


print("_____________--------------------------________________")
# RAVEL

array_r=np.ravel(array)
print(array_r)

array_r=array.ravel()
print(array_r)


