import numpy as np



matrix=np.array([[1,2],[3,4]])

matrix1=np.array([[1,2],[3,4]])

# Addition

add=matrix+matrix1
print(add)


# Sub

sub=matrix-matrix1
print(sub)


# Mul
# mul=matrix*matrix1 
# print(mul)

mul=matrix.dot(matrix1)  # in metrix case its right 
print(mul)