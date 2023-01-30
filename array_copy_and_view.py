# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

print("----------------------------------------------")

# The copy SHOULD NOT be affected by the changes made to the original array.

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

print("----------------------------------------------")
# changes made un view variable also effected by original array
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)



# check a variable is carrying an array in view function or not
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()   
y = arr.view()  

print(x.base) # its a copy then base is get None
print(y.base)  # its a view then get exact the original array



# The copy returns None.
# The view returns the original array.