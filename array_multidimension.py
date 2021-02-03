from numpy import *

arr1 = array([
            [1,2,3,6,8,7],
            [4,5,6,3,7,5]
        ])

arr2 = arr1.flatten()

arr3 = arr2.reshape(2,2,3)

print(arr1)
print(arr2)
print(arr3)