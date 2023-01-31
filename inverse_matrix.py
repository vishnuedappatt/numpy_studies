import numpy as np


matrix=np.array([[1,2,9],[3,4,9],[1,2,3]])
print(matrix)


inv=np.linalg.inv(matrix)
print(inv)


check=np.allclose(np.dot(matrix,inv),np.eye(3))
print(check)