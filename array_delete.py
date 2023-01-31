import numpy as np

# delete just happen as in a copy not take in original array

array=np.array([1,2,3,6,7,8])
del_ary=np.delete(array,3)
print(array)
print(del_ary)
print(array)



# in 2D array
print("************************")
array=np.array([[1,2],[3,4]])
print(array)

print("************************")

del_ary=np.delete(array,2)
print(del_ary)


del_ary=np.delete(array,1,axis=1)  # delete last colimn
print(del_ary)


del_ary=np.delete(array,1,axis=0)   # delete last row
print(del_ary)