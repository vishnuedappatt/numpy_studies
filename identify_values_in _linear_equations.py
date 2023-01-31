import numpy as np

# for example 2x+2y=10 and 2x+y=22  find x and y
# then it we will represents like [2 2 ,  and [10,22]
#                                  2 1] 


a=np.array([[2,2],[2,1]])
b=np.array([10,22])

solve=np.linalg.solve(a,b)
print(solve)