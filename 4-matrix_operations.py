import numpy as np 

m1 = np.array([[1, 2], [4, 5]])
m2 = np.array([[7, 8], [10, 11]])
print("Matrix m1:\n", m1)
print("Matrix m2:\n", m2)
m = np.dot(m1, m2)  
transposee_m = m.T
inverse_m = np.linalg.inv(m)
print("Matrix m:\n", m)
print("Transpose of m:\n", transposee_m)
print("Inverse of m:\n", inverse_m)