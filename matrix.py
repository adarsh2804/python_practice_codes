from numpy import *

arr1 = array([
            [1,2,3],
            [4,5,6]
        ])

m = matrix(arr1)

mat = matrix('1 2 3; 5 4 6; 9 6 7')
mat1 = matrix('1 2 3; 5 4 6; 9 6 7')
mat2 = mat * mat1

print(m)
print(mat)
print(mat.diagonal())
print(mat.max())
print(mat2)