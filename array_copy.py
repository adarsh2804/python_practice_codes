from numpy import *
# from array import *

arr1 = array([1, 2, 3, 4])
arr2 = arr1.view()  # shallow copy
arr3 = arr1.copy()  # deep copy

arr1[1] = 7

print(arr1)
print(arr2)
print(arr3)

print(id(arr1))
print(id(arr2))
print(id(arr3))
