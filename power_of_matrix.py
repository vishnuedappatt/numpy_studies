import numpy as np



array=np.matrix([[1,2],[1,2]])
print(array)

power=np.linalg.matrix_power(array,2)
print(power)


power=array * array
print(power)      # twoes are same 




power=np.linalg.matrix_power(array,0)   # get identity matrix in 2*2 matrix like [1 0]
                                                                                # [0 1]

print(power)

array=np.matrix([[1,2],[1,2]])
print(array)

power=np.linalg.matrix_power(array,-1)
print(power)


# first inverse and then multiply * n
