import numpy as np

"Inverse of Matrix"

x = np.array([[1,2],[3,4]])
y = np.linalg.inv(x) 
print ("Original Matrix :-")
print (x)
print ("Inverse Matrix :-") 
print (y)

"Transpose of Matrix"

a = np.array([[1,2],[3,4]])
b = np.transpose(a)
print ("Original Matrix :-")
print (a)
print ("Transpose Matrix :-") 
print (b)

"Multiplication of Matrices"

m1 = np.array([[1,4,7],[2,5,8]])
m2 = np.array([[1,4],[2,5],[3,6]])
m3 = np.dot(m1,m2) 
print ("Original Matrices :-")
print (m1)
print (m2)
print ("Resultant Matrix :-") 
print (m3)

