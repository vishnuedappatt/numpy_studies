import numpy as np


matrix=np.matrix("1 2;3 4")
print(matrix)


matrix1=np.matrix([[1,3],[5,6]])
print(matrix1) 



# addition sub division are same and multiplication is using  * for matrix multiplication in multiplication class



mul=matrix1*matrix
print(mul)

mul=matrix.dot(matrix1)
print(mul)

trans=mul.T
print(trans)