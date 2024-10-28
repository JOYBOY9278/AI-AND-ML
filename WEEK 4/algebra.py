import numpy as np
from numpy import array

number_of_units=50
print("Scalar : ",number_of_units)

A= np.array([1,2,3,4]) 
B = np.array([-4,-3, -2, -1])
print("\nVector :\n",A)
26
print(B)

C= np.array([[2,-2],[3,1],[1,4]])
print("\nMatrix A:\n",C)

print("Matrix A Transpose: \n",np.transpose(C))

T = array([
[[1,2,3], [4,5,6], [7,8,9]],
[[11,12,13], [14,15,16], [17,18,19]],
[[21,22,23], [24,25,26], [27,28,29]],
])
print(T.shape)
print("\nTensor:\n",T)
n=np.gradient(C)
print("\nGradient : \n",n)
w, v = np.linalg.eig(T)
mat_norm = np.linalg.norm(T)
print("\nEigen values:\n",w)
print("\nEigen vectors:\n",v)
print("\nMatrix norm:", mat_norm)
